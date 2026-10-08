# orphans

*Community 7 | 26 files | cohesion 0.00*

## Definition

This community groups 26 file(s) rooted at `root` with dominant language py (cohesion 0.00). Central symbols: `Cache`, `CheckResult`, `DoctorReport`, `Mutation`, `SRPSessionStore`, `SubscriptionPlans`, `__init__`, `_build_s3_client`. Core file: `scripts/doctor.py` (28 symbols). Documented purpose: Offline admin tool for ML-KEM-512 key-wrap encryption (QuantumVault).  WARNING.

## Files

### `.` (11 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `__init__.py` | py | utility | 0 | no |
| `client.go` | go | infrastructure | 1 | no |
| `client.py` | py | infrastructure | 0 | no |
| `enc_dec.go` | go | utility | 4 | no |
| `enc_dec.py` | py | utility | 5 | yes |

### `scripts` (3 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `scripts/doctor.py` | py | utility | 28 | yes |
| `scripts/garage-init.sh` | sh | utility | 1 | yes |
| `scripts/garage-native.sh` | sh | utility | 3 | yes |

### `tests` (3 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/__init__.py` | py | testing | 0 | no |
| `tests/test_auth_phone.py` | py | testing | 3 | yes |
| `tests/test_doctor.py` | py | testing | 12 | yes |

### `utils` (3 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `utils/cache.py` | py | infrastructure | 5 | yes |
| `utils/plans.py` | py | utility | 3 | no |
| `utils/srp6a.py` | py | utility | 14 | yes |

### `controllers` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `controllers/__init__.py` | py | presentation | 0 | no |

### `models` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `models/__init__.py` | py | business_logic | 0 | no |

### `static/js` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `static/js/coded-text.js` | js | utility | 3 | yes |

### `templates` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `templates/terms.py` | py | presentation | 1 | no |

### `tools` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tools/mutation_test.py` | py | testing | 8 | yes |

### `views` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `views/__init__.py` | py | presentation | 0 | no |

*... and 6 more files in this community.*


## Key Symbols

- `main` (function, `client.go:13`) `func main(`
- `deriveAESKey` (function, `enc_dec.go:20`) `func deriveAESKey(`
- `encryptFile` (function, `enc_dec.go:24`) `func encryptFile(`
- `decryptFile` (function, `enc_dec.go:45`) `func decryptFile(`
- `main` (function, `enc_dec.go:69`) `func main(`
- `derive_aes_key` (function, `enc_dec.py:36`) `def derive_aes_key(shared_secret)` - Derive a 32-byte AES key from an ML-KEM shared secret.
- `encrypt_file_in_memory` (function, `enc_dec.py:49`) `def encrypt_file_in_memory(data, aes_key)` - Encrypt ``data`` in memory with AES-256-GCM and return nonce + ciphertext.
- `decrypt_file_in_memory` (function, `enc_dec.py:65`) `def decrypt_file_in_memory(nonce, ciphertext, aes_key)` - Decrypt ``ciphertext`` in memory with AES-256-GCM and return the plaintext.
- `_build_s3_client` (function, `enc_dec.py:81`) `def _build_s3_client(region)` - Build a boto3 S3 client honoring the zero-trust environment convention.
- `main` (function, `enc_dec.py:103`) `def main()` - Run the offline admin CLI (encrypt or decrypt a single object).
- `CheckResult` (class, `scripts/doctor.py:98`) `class CheckResult` - Outcome of one environment check with a repair hint.
- `DoctorReport` (class, `scripts/doctor.py:108`) `class DoctorReport` - Accumulated check results with derived exit status.
- `add` (method, `scripts/doctor.py:113`) `def add(self, result)` - Append one check result.
- `failures` (method, `scripts/doctor.py:118`) `def failures(self)` - Return every failing check.
- `exit_code` (method, `scripts/doctor.py:123`) `def exit_code(self)` - Return 0 when every check passes, 1 otherwise.
- `load_env_file` (method, `scripts/doctor.py:128`) `def load_env_file(path)` - Parse a dotenv file into a dict without third-party imports.
- `effective_env` (method, `scripts/doctor.py:147`) `def effective_env()` - Return process env overlaid with ``.env`` file values.
- `check_python` (method, `scripts/doctor.py:154`) `def check_python(minimum)` - Verify the interpreter meets the minimum supported version.
- `check_module` (method, `scripts/doctor.py:170`) `def check_module(name)` - Verify one Python module imports cleanly.
- `check_binary` (method, `scripts/doctor.py:186`) `def check_binary(name, env_override)` - Verify one system binary resolves via PATH or an override path.
- `check_env_file` (method, `scripts/doctor.py:210`) `def check_env_file()` - Verify the operator ``.env`` file exists.
- `parse_host_port` (method, `scripts/doctor.py:223`) `def parse_host_port(uri, default_port)` - Extract a TCP host and port from a Redis or HTTP(S) URL.
- `check_tcp` (method, `scripts/doctor.py:242`) `def check_tcp(name, host, port, timeout)` - Verify a TCP endpoint accepts connections.
- `debian_arch` (method, `scripts/doctor.py:261`) `def debian_arch(deb)` - Map the host CPU to a Cloudflare or Garage release architecture.
- `cloudflared_deb_url` (method, `scripts/doctor.py:270`) `def cloudflared_deb_url(version, arch)` - Build the official cloudflared .deb URL for a version and arch.
- `garage_bin_url` (method, `scripts/doctor.py:283`) `def garage_bin_url(version, target)` - Build the official garage binary URL for a version and target.
- `apt_command` (method, `scripts/doctor.py:288`) `def apt_command(packages)` - Build an apt install command, prefixed with sudo outside root.
- `run_command` (method, `scripts/doctor.py:298`) `def run_command(cmd)` - Run one shell command and capture its outcome.
- `download_file` (method, `scripts/doctor.py:319`) `def download_file(url, destination)` - Fetch a URL with curl when present, else urllib.
- `upsert_env` (method, `scripts/doctor.py:334`) `def upsert_env(key, value, path)` - Set one KEY=value pair in ``.env``, preserving other lines.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 7 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (views: auth) and community 7 (orphans).
- [INFERRED] shares_context community 1 <-> 7 (strength 0.5): Inferred shared context (language py) with no import path between community 1 (views: facade) and community 7 (orphans).
- [INFERRED] shares_context community 2 <-> 7 (strength 0.5): Inferred shared context (layer utility) with no import path between community 2 (static/js) and community 7 (orphans).
- [INFERRED] shares_context community 3 <-> 7 (strength 0.5): Inferred shared context (language py) with no import path between community 3 (controllers) and community 7 (orphans).

## Risks

- [taint high] `scripts/doctor.py` -> `scripts/doctor.py` via `subprocess` (0 hops)
- [taint medium] `scripts/doctor.py` -> `scripts/doctor.py` via `urllib.request` (0 hops)
- [taint high] `tools/mutation_test.py` -> `tools/mutation_test.py` via `subprocess` (0 hops)

## Open Questions

- Why do 15 file(s) lack file-level docs (e.g. `__init__.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `scripts/doctor.py` still required, or can it be isolated?
- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `__init__.py`
- `client.go`
- `client.py`
- `controllers/__init__.py`
- `enc_dec.go`
- `enc_dec.py`
- `install.sh`
- `make.sh`
- `models/__init__.py`
- `pq_decrypt_password.py`
- `scripts/doctor.py`
- `scripts/garage-init.sh`
- `scripts/garage-native.sh`
- `server.go`
- `server.py`
- `static/js/coded-text.js`
- `templates/terms.py`
- `test.sh`
- `tests/__init__.py`
- `tests/test_auth_phone.py`
- *... and 6 more*
