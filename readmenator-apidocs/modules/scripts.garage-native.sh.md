# `scripts/garage-native.sh`

> Source: [scripts/garage-native.sh:1](../../scripts/garage-native.sh#L1) | language `sh` | coverage 50.0% | [API index](../index.md)

Run Garage (S3-compatible object storage) natively, without Docker.

Idempotent: if the S3 API is already reachable on :3900 it does nothing. Otherwise it ensures a local garage binary exists (downloading a pinned release and verifying its checksum when necessary), writes a development config with project-local data directories under .run/garage, starts the server in the background, provisions the bucket and a scoped access key, and writes the resulting S3 credentials into .env so the app picks them up.  Override knobs via the environment: GARAGE_VERSION   release to download                 (default 1.0.1) GARAGE_BIN       path to (or destination for) garage (default .run/garage-bin/garage) GARAGE_SHA256    pin the binary checksum             (optional, recommended)  This script is invoked by `make garage-up`, which `make run` calls as a prerequisite when Docker is not available.

## Contents

- **Functions:** [`upsert_env`](#upsert_env), [`s3_reachable`](#s3_reachable), [`gcmd`](#gcmd)

## Functions

<a id="upsert_env"></a>

### `upsert_env`

`function` | [scripts/garage-native.sh:46](../../scripts/garage-native.sh#L46)

```bash
upsert_env()
```

Insert or update a KEY=value line in .env without disturbing other lines.

---

<a id="s3_reachable"></a>

### `s3_reachable`

`function` | [scripts/garage-native.sh:56](../../scripts/garage-native.sh#L56)

```bash
s3_reachable()
```

---

<a id="gcmd"></a>

### `gcmd`

`function` | [scripts/garage-native.sh:141](../../scripts/garage-native.sh#L141)

```bash
gcmd()
```

---
