# `scripts/garage-init.sh`

> Source: [scripts/garage-init.sh:1](../../scripts/garage-init.sh#L1) | language `sh` | coverage 100.0% | [API index](../index.md)

Bootstrap a fresh Garage deployment for QuantumVault.

What this does: 1. Waits for the admin API to respond. 2. Connects the local node to the cluster (single-node layout). 3. Creates the quantumvault bucket. 4. Creates a scoped API key with read+write on that bucket only. 5. Emits the credentials for .env (S3_ACCESS_KEY / S3_SECRET_KEY).  Usage: docker compose up -d garage scripts/garage-init.sh  The script reads GARAGE_RPC_SECRET and GARAGE_ADMIN_TOKEN from the .env file (or the environment) so the admin API can be authenticated.

## Contents

- **Functions:** [`upsert_env`](#upsert_env)

## Functions

<a id="upsert_env"></a>

### `upsert_env`

`function` | [scripts/garage-init.sh:35](../../scripts/garage-init.sh#L35)

```bash
upsert_env()
```

Insert or update a KEY=value line in .env without disturbing other lines.

---
