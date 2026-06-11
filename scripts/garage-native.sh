#!/usr/bin/env bash
# Run Garage (S3-compatible object storage) natively, without Docker.
#
# Idempotent: if the S3 API is already reachable on :3900 it does nothing.
# Otherwise it ensures a local garage binary exists (downloading a pinned
# release and verifying its checksum when necessary), writes a development
# config with project-local data directories under .run/garage, starts the
# server in the background, provisions the bucket and a scoped access key, and
# writes the resulting S3 credentials into .env so the app picks them up.
#
# Override knobs via the environment:
#   GARAGE_VERSION   release to download                 (default 1.0.1)
#   GARAGE_BIN       path to (or destination for) garage (default .run/garage-bin/garage)
#   GARAGE_SHA256    pin the binary checksum             (optional, recommended)
#
# This script is invoked by `make garage-up`, which `make run` calls as a
# prerequisite when Docker is not available.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

RUN_DIR="$PROJECT_DIR/.run"
GARAGE_HOME="$RUN_DIR/garage"
GARAGE_CONFIG="$GARAGE_HOME/garage.toml"
GARAGE_PID="$RUN_DIR/garage.pid"
GARAGE_LOG="$RUN_DIR/garage.log"
GARAGE_VERSION="${GARAGE_VERSION:-1.0.1}"
GARAGE_BIN="${GARAGE_BIN:-$RUN_DIR/garage-bin/garage}"
S3_API_HOST="127.0.0.1"
S3_API_PORT="3900"
ADMIN_ADDR="127.0.0.1:3903"
BUCKET="${S3_BUCKET:-quantumvault}"
KEY_NAME="${GARAGE_KEY_NAME:-quantumvault-app}"

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

s3_reachable() {
    timeout 1 bash -c "exec 3<>/dev/tcp/${S3_API_HOST}/${S3_API_PORT}" 2>/dev/null
}

# Fast path: only skip when the API is already serving AND .env already holds
# credentials. A reachable server with no credentials (e.g. a previous partial
# run) still needs provisioning.
if s3_reachable && [[ -n "${S3_ACCESS_KEY:-}" && -n "${S3_SECRET_KEY:-}" ]]; then
    echo "[garage-native] S3 API is up and .env already has credentials (skipping)."
    exit 0
fi

mkdir -p "$RUN_DIR" "$GARAGE_HOME/meta" "$GARAGE_HOME/data" "$(dirname "$GARAGE_BIN")"

# --- 1. Resolve or download the garage binary -------------------------------
if [[ ! -x "$GARAGE_BIN" ]] && command -v garage >/dev/null 2>&1; then
    GARAGE_BIN="$(command -v garage)"
fi

if [[ ! -x "$GARAGE_BIN" ]]; then
    arch="$(uname -m)"
    case "$arch" in
        x86_64|amd64) target="x86_64-unknown-linux-musl" ;;
        aarch64|arm64) target="aarch64-unknown-linux-musl" ;;
        *)
            echo "ERROR: unsupported architecture '$arch'." >&2
            echo "Download garage manually and place it at: $GARAGE_BIN" >&2
            exit 1
            ;;
    esac
    url="https://garagehq.deuxfleurs.fr/_releases/v${GARAGE_VERSION}/${target}/garage"
    echo "[garage-native] downloading garage v${GARAGE_VERSION} (${target}) ..."
    if ! curl -fSL --retry 3 -o "$GARAGE_BIN" "$url"; then
        echo "ERROR: could not download garage from $url" >&2
        echo "Install it manually and place the binary at $GARAGE_BIN" >&2
        exit 1
    fi

    actual_sha="$(sha256sum "$GARAGE_BIN" | awk '{print $1}')"
    if [[ -n "${GARAGE_SHA256:-}" ]]; then
        if [[ "$GARAGE_SHA256" != "$actual_sha" ]]; then
            echo "ERROR: checksum mismatch (expected $GARAGE_SHA256, got $actual_sha)." >&2
            rm -f "$GARAGE_BIN"
            exit 1
        fi
        echo "[garage-native] checksum verified against pinned GARAGE_SHA256."
    elif curl -fSL -o "$GARAGE_BIN.sha256sum" "${url}.sha256sum" 2>/dev/null; then
        expected_sha="$(awk '{print $1}' "$GARAGE_BIN.sha256sum" | head -1)"
        if [[ "$expected_sha" != "$actual_sha" ]]; then
            echo "ERROR: checksum mismatch (expected $expected_sha, got $actual_sha)." >&2
            rm -f "$GARAGE_BIN"
            exit 1
        fi
        echo "[garage-native] checksum verified against upstream .sha256sum."
    else
        echo "[garage-native] WARNING: could not fetch a checksum to verify the download."
        echo "[garage-native] Pin it with GARAGE_SHA256=<sha256> for a trusted setup."
    fi
    chmod +x "$GARAGE_BIN"
fi

echo "[garage-native] using binary: $GARAGE_BIN"

# --- 2. Write a development config with project-local data dirs --------------
RPC_SECRET="${GARAGE_RPC_SECRET:-$(openssl rand -hex 32)}"
ADMIN_TOKEN="${GARAGE_ADMIN_TOKEN:-$(openssl rand -hex 32)}"
cat > "$GARAGE_CONFIG" <<EOF
metadata_dir = "$GARAGE_HOME/meta"
data_dir = "$GARAGE_HOME/data"
db_engine = "sqlite"

replication_factor = 1
rpc_bind_addr = "127.0.0.1:3901"
rpc_public_addr = "127.0.0.1:3901"
rpc_secret = "$RPC_SECRET"

[s3_api]
s3_region = "garage"
api_bind_addr = "${S3_API_HOST}:${S3_API_PORT}"

[admin]
api_bind_addr = "$ADMIN_ADDR"
admin_token = "$ADMIN_TOKEN"
EOF

gcmd() {
    "$GARAGE_BIN" -c "$GARAGE_CONFIG" "$@"
}

# --- 3. Start the server in the background (unless it is already running) ----
if s3_reachable; then
    echo "[garage-native] S3 API already up; (re)provisioning without starting a new server."
else
    echo "[garage-native] starting garage server (pidfile=$GARAGE_PID, log=$GARAGE_LOG) ..."
    nohup "$GARAGE_BIN" -c "$GARAGE_CONFIG" server >"$GARAGE_LOG" 2>&1 &
    echo $! > "$GARAGE_PID"
    for _ in $(seq 1 50); do
        if s3_reachable; then break; fi
        sleep 0.2
    done
    if ! s3_reachable; then
        echo "ERROR: garage did not come up. Tail of $GARAGE_LOG:" >&2
        tail -n 30 "$GARAGE_LOG" >&2 || true
        exit 1
    fi
    echo "[garage-native] S3 API is up on ${S3_API_HOST}:${S3_API_PORT}."
fi

# --- 4. Provision the single-node layout (idempotent) -----------------------
# A non-zero "Current cluster layout version" means a layout is already active,
# so we must not assign/apply again (that would fail with a version conflict).
LAYOUT_VERSION="$(gcmd layout show 2>/dev/null | awk -F': *' '/Current cluster layout version/ {print $2; exit}')"
if [[ -z "$LAYOUT_VERSION" || "$LAYOUT_VERSION" == "0" ]]; then
    NODE_ID="$(gcmd node id -q 2>/dev/null | head -1 | cut -d@ -f1 || true)"
    if [[ -z "$NODE_ID" ]]; then
        echo "ERROR: could not determine the garage node id." >&2
        tail -n 30 "$GARAGE_LOG" >&2 || true
        exit 1
    fi
    echo "[garage-native] applying single-node layout ..."
    gcmd layout assign -z dc1 -c 1G "$NODE_ID"
    gcmd layout apply --version 1
else
    echo "[garage-native] cluster layout already at version $LAYOUT_VERSION (skipping)."
fi

# --- 5. Ensure the bucket exists --------------------------------------------
if ! gcmd bucket info "$BUCKET" >/dev/null 2>&1; then
    echo "[garage-native] creating bucket $BUCKET ..."
    gcmd bucket create "$BUCKET"
fi

# --- 6. Ensure a working access key, reusing .env credentials when valid ----
if [[ -n "${S3_ACCESS_KEY:-}" && -n "${S3_SECRET_KEY:-}" ]] && gcmd key info "$S3_ACCESS_KEY" >/dev/null 2>&1; then
    echo "[garage-native] reusing existing key from .env ($S3_ACCESS_KEY)."
    gcmd bucket allow --read --write --owner "$BUCKET" --key "$S3_ACCESS_KEY" >/dev/null 2>&1 || true
else
    UNIQUE_KEY_NAME="${KEY_NAME}-$(date +%s)"
    echo "[garage-native] creating scoped key $UNIQUE_KEY_NAME ..."
    KEY_OUTPUT="$(gcmd key create "$UNIQUE_KEY_NAME" 2>&1 || true)"
    ACCESS_KEY="$(echo "$KEY_OUTPUT" | awk -F': *' '/^Key ID/ {print $2; exit}')"
    SECRET_KEY="$(echo "$KEY_OUTPUT" | awk -F': *' '/^Secret key/ {print $2; exit}')"
    if [[ -z "$ACCESS_KEY" || -z "$SECRET_KEY" ]]; then
        echo "ERROR: could not parse the created key. Output was:" >&2
        echo "$KEY_OUTPUT" >&2
        exit 1
    fi
    gcmd bucket allow --read --write --owner "$BUCKET" --key "$ACCESS_KEY"
    upsert_env S3_ACCESS_KEY "$ACCESS_KEY"
    upsert_env S3_SECRET_KEY "$SECRET_KEY"
    echo "[garage-native] wrote S3_ACCESS_KEY and S3_SECRET_KEY to .env."
fi

upsert_env S3_ENDPOINT_URL "http://${S3_API_HOST}:${S3_API_PORT}"
upsert_env S3_BUCKET "$BUCKET"
upsert_env S3_REGION "garage"

echo "[garage-native] ready. Garage is serving S3 on http://${S3_API_HOST}:${S3_API_PORT}."
