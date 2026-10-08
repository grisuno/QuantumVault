# Subsystem: root

## __init__.py
- Layer: utility
- Language: py

## app.py
- Doc: Local development entry point.
- Layer: utility
- Language: py
- Symbols:
  - `main` (function, line 21) `def main()`
  - `_is_production_like` (function, line 58) `def _is_production_like()`
- Depends on: `app_factory.py`, `utils/utils.py`
- Imported by: `scripts/test_bloque1.py`

## app_factory.py
- Doc: Application factory for QuantumVault.
- Layer: presentation
- Language: py
- Symbols:
  - `_is_production` (function, line 71) `def _is_production()`
  - `_build_csp` (function, line 82) `def _build_csp()`
  - `_build_talisman_kwargs` (function, line 119) `def _build_talisman_kwargs()`
  - `_configure_secret_key` (function, line 160) `def _configure_secret_key(app, config)`
  - `_configure_session` (function, line 203) `def _configure_session(app)`
  - `_configure_logging` (function, line 220) `def _configure_logging(app)`
  - `create_app` (function, line 237) `def create_app(config_overrides, security_overrides)`
  - `load_user` (function, line 416) `def load_user(user_id)`
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

## client.go
- Layer: infrastructure
- Language: go
- Symbols:
  - `main` (function, line 13) `func main(`

## client.py
- Layer: infrastructure
- Language: py

## enc_dec.go
- Layer: utility
- Language: go
- Symbols:
  - `deriveAESKey` (function, line 20) `func deriveAESKey(`
  - `encryptFile` (function, line 24) `func encryptFile(`
  - `decryptFile` (function, line 45) `func decryptFile(`
  - `main` (function, line 69) `func main(`

## enc_dec.py
- Doc: Offline admin tool for ML-KEM-512 key-wrap encryption (QuantumVault).
- Layer: utility
- Language: py
- Symbols:
  - `derive_aes_key` (function, line 36) `def derive_aes_key(shared_secret)`
  - `encrypt_file_in_memory` (function, line 49) `def encrypt_file_in_memory(data, aes_key)`
  - `decrypt_file_in_memory` (function, line 65) `def decrypt_file_in_memory(nonce, ciphertext, aes_key)`
  - `_build_s3_client` (function, line 81) `def _build_s3_client(region)`
  - `main` (function, line 103) `def main()`

## install.sh
- Doc: Script para instalar prerrequisitos y compilar el proyecto postcuantum Fecha: 26 de junio de...
- Layer: utility
- Language: sh

## make.sh
- Layer: utility
- Language: sh

## pq_decrypt_password.py
- Layer: utility
- Language: py

## server.go
- Layer: utility
- Language: go
- Symbols:
  - `main` (function, line 11) `func main(`
  - `handleConnection` (function, line 40) `func handleConnection(`

## server.py
- Layer: utility
- Language: py

## test.sh
- Layer: testing
- Language: sh

## wsgi.py
- Doc: WSGI entry point for production deployments.
- Layer: utility
- Language: py
- Depends on: `app_factory.py`
