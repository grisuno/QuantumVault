#!/usr/bin/env bash
# Bootstrap a fresh Garage deployment for QuantumVault.
#
# What this does:
#   1. Waits for the admin API to respond.
#   2. Connects the local node to the cluster (single-node layout).
#   3. Creates the quantumvault bucket.
#   4. Creates a scoped API key with read+write on that bucket only.
#   5. Emits the credentials for .env (S3_ACCESS_KEY / S3_SECRET_KEY).
#
# Usage:
#   docker compose up -d garage
#   scripts/garage-init.sh
#
# The script reads GARAGE_RPC_SECRET and GARAGE_ADMIN_TOKEN from the .env file
# (or the environment) so the admin API can be authenticated.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
ADMIN_URL="${GARAGE_ADMIN_URL:-http://localhost:3903}"
BUCKET="${S3_BUCKET:-quantumvault}"
KEY_NAME="${GARAGE_KEY_NAME:-quantumvault-app}"

# Load .env if present.
if [[ -f "$PROJECT_DIR/.env" ]]; then
    set -a
    # shellcheck disable=SC1091
    source "$PROJECT_DIR/.env"
    set +a
fi

# Insert or update a KEY=value line in .env without disturbing other lines.
upsert_env() {
    local key="$1" value="$2" file="$PROJECT_DIR/.env"
    [[ -f "$file" ]] || touch "$file"
    if grep -qE "^${key}=" "$file"; then
        sed "s|^${key}=.*|${key}=${value}|" "$file" > "$file.tmp" && mv "$file.tmp" "$file"
    else
        printf '%s=%s\n' "$key" "$value" >> "$file"
    fi
}

if [[ -z "${GARAGE_ADMIN_TOKEN:-}" ]]; then
    echo "ERROR: GARAGE_ADMIN_TOKEN is not set. Add it to .env first." >&2
    exit 1
fi

GARAGE_BIN="${GARAGE_BIN:-docker compose exec -T garage /garage}"

# Wait for the admin API to come up.
echo "[garage-init] waiting for admin API at $ADMIN_URL ..."
for _ in $(seq 1 30); do
    if curl -fsS -H "Authorization: Bearer $GARAGE_ADMIN_TOKEN" \
            "$ADMIN_URL/health" >/dev/null 2>&1; then
        break
    fi
    sleep 1
done

# Locate the node ID (created on first start).
NODE_ID="$($GARAGE_BIN node id -q 2>/dev/null | head -1 || true)"
if [[ -z "$NODE_ID" ]]; then
    # Fall back to docker exec.
    NODE_ID="$(docker compose exec -T garage /garage node id 2>/dev/null | awk '/^[a-f0-9]/ {print $1; exit}')"
fi
if [[ -z "$NODE_ID" ]]; then
    echo "ERROR: could not determine local node ID. Is the garage container running?" >&2
    exit 1
fi
echo "[garage-init] node id: $NODE_ID"

# Assign and apply a single-node layout.
echo "[garage-init] applying single-node layout ..."
docker compose exec -T garage /garage layout assign --version 1 -z dc1 -c 1 "$NODE_ID"
docker compose exec -T garage /garage layout apply --version 1

# Create the bucket (idempotent).
echo "[garage-init] ensuring bucket $BUCKET exists ..."
if ! docker compose exec -T garage /garage bucket info "$BUCKET" >/dev/null 2>&1; then
    docker compose exec -T garage /garage bucket create "$BUCKET"
fi

# Create the scoped API key. The key name is a positional argument in
# Garage v1.0 (`key create [name]`).
echo "[garage-init] creating scoped key $KEY_NAME ..."
KEY_OUTPUT="$(docker compose exec -T garage /garage key create "$KEY_NAME" 2>&1 || true)"

# If no key was generated, ask the operator to create one manually.
if ! echo "$KEY_OUTPUT" | grep -q '^Key ID'; then
    echo ""
    echo "A new API key was not generated. Either the name already exists or"
    echo "the command failed. Output was:"
    echo "$KEY_OUTPUT"
    echo "To create one manually:"
    echo "  docker compose exec garage /garage key create $KEY_NAME"
    echo "Then paste the Key ID and Secret key into .env as S3_ACCESS_KEY / S3_SECRET_KEY."
    exit 0
fi

ACCESS_KEY="$(echo "$KEY_OUTPUT" | awk -F': *' '/^Key ID/ {print $2; exit}')"
SECRET_KEY="$(echo "$KEY_OUTPUT" | awk -F': *' '/^Secret key/ {print $2; exit}')"

if [[ -z "$ACCESS_KEY" || -z "$SECRET_KEY" ]]; then
    echo "ERROR: could not parse key output:" >&2
    echo "$KEY_OUTPUT" >&2
    exit 1
fi

# Allow the new key read+write on the bucket.
docker compose exec -T garage /garage bucket allow \
    --read --write --owner "$BUCKET" --key "$KEY_NAME"

# Persist the credentials directly into .env so the app picks them up on the
# next start without a manual copy step.
upsert_env S3_ACCESS_KEY "$ACCESS_KEY"
upsert_env S3_SECRET_KEY "$SECRET_KEY"
upsert_env S3_ENDPOINT_URL "${S3_ENDPOINT_URL:-http://localhost:3900}"
upsert_env S3_BUCKET "$BUCKET"
upsert_env S3_REGION "${S3_REGION:-garage}"

echo ""
echo "[garage-init] success. Wrote S3_ACCESS_KEY and S3_SECRET_KEY to .env:"
echo "  S3_ACCESS_KEY=$ACCESS_KEY"
echo "  S3_SECRET_KEY=$SECRET_KEY"
echo "Restart the app (e.g. 'make run') to load the new credentials."
