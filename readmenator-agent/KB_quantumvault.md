# Subsystem: quantumvault

## quantumvault/__init__.py
- Doc: QuantumVault application package.
- Layer: utility
- Language: py
- Depends on: `utils/version.py`

## quantumvault/app_factory.py
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
- Imported by: `app.py`, `quantumvault/wsgi.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`

## quantumvault/wsgi.py
- Doc: WSGI entry point for production deployments.
- Layer: utility
- Language: py
- Symbols:
  - `main` (function, line 27) `def main()`
- Depends on: `quantumvault/app_factory.py`
