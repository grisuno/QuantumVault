# Subsystem: models

## models/__init__.py
- Layer: business_logic
- Language: py

## models/contact.py
- Layer: presentation
- Language: py
- Symbols:
  - `ContactModel` (class, line 8) `class ContactModel(BaseModel)`
  - `ContactDB` (class, line 26) `class ContactDB`
  - `__init__` (method, line 29) `def __init__(self, db_path)`
  - `_init_db` (method, line 38) `def _init_db(self)`
  - `create_contact` (method, line 52) `def create_contact(self, user_id, subject, message)`
  - `get_user_contacts` (method, line 89) `def get_user_contacts(self, user_id)`
  - `_convert_row_to_dict` (method, line 115) `def _convert_row_to_dict(self, row)`
  - `get_all_contacts` (method, line 139) `def get_all_contacts(self, page, per_page)`
  - `_convert_row_to_dict_with_username` (method, line 168) `def _convert_row_to_dict_with_username(self, row)`
- Imported by: `controllers/contact.py`

## models/deniable_vault.py
- Layer: business_logic
- Language: py
- Symbols:
  - `DeniableVaultDB` (class, line 30) `class DeniableVaultDB`
  - `__init__` (method, line 33) `def __init__(self, db_path)`
  - `_init_db` (method, line 43) `def _init_db(self)`
  - `upsert` (method, line 57) `def upsert(self, username, envelope)`
  - `get` (method, line 82) `def get(self, username)`
  - `exists` (method, line 101) `def exists(self, username)`
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

## models/message.py
- Layer: presentation
- Language: py
- Symbols:
  - `MessageModel` (class, line 27) `class MessageModel(BaseModel)`
  - `MessageDB` (class, line 43) `class MessageDB`
  - `__init__` (method, line 46) `def __init__(self, base_path)`
  - `save_message` (method, line 55) `def save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)`
  - `get_messages` (method, line 87) `def get_messages(self, recipient, page, per_page)`
  - `delete_old_messages` (method, line 172) `def delete_old_messages(self, recipient, days)`
- Imported by: `controllers/message.py`, `utils/scheduler.py`

## models/plans.py
- Layer: business_logic
- Language: py
- Symbols:
  - `PlanDB` (class, line 4) `class PlanDB`
  - `__init__` (method, line 6) `def __init__(self, db_path)`
  - `_init_db` (method, line 15) `def _init_db(self)`
  - `get_plan` (method, line 37) `def get_plan(self, plan_name)`
  - `get_all_plans` (method, line 50) `def get_all_plans(self)`
  - `create_plan` (method, line 60) `def create_plan(self, name, storage_quota, trial_days, price)`
  - `update_plan` (method, line 78) `def update_plan(self, name, storage_quota, trial_days, price)`
  - `delete_plan` (method, line 113) `def delete_plan(self, name)`
  - `_convert_row_to_dict` (method, line 127) `def _convert_row_to_dict(self, row)`
  - `validate_plan_payment` (method, line 139) `def validate_plan_payment(self, plan_name, amount_paid)`
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

## models/superadmin_audit.py
- Layer: business_logic
- Language: py
- Symbols:
  - `SuperadminAuditDB` (class, line 32) `class SuperadminAuditDB`
  - `__init__` (method, line 35) `def __init__(self, db_path)`
  - `_init_db` (method, line 45) `def _init_db(self)`
  - `record` (method, line 75) `def record(self, actor, action, target_user, ip, details)`
  - `recent` (method, line 119) `def recent(self, limit)`
- Imported by: `views/admin.py`

## models/user.py
- Layer: presentation
- Language: py
- Symbols:
  - `UserModel` (class, line 8) `class UserModel(BaseModel, UserMixin)`
  - `UserDB` (class, line 83) `class UserDB`
  - `get_id` (method, line 52) `def get_id(self)`
  - `is_active` (method, line 70) `def is_active(self)`
  - `__init__` (method, line 85) `def __init__(self, db_path)`
  - `_init_db` (method, line 105) `def _init_db(self)`
  - `_has_phone_unique_constraint` (method, line 193) `def _has_phone_unique_constraint(self)`
  - `_drop_phone_unique_if_present` (method, line 214) `def _drop_phone_unique_if_present(self)`
  - `_migrate_from_v7` (method, line 271) `def _migrate_from_v7(self, legacy_columns)`
  - `create_user` (method, line 325) `def create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled, recovery_salt, encrypted_private_key_recovery)`
  - `update_user_phone_status` (method, line 362) `def update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)`
  - `update_user_mfa_status` (method, line 396) `def update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)`
  - `update_user` (method, line 430) `def update_user(self, username, email_verified, confirmation_token)`
  - `get_user` (method, line 454) `def get_user(self, username)`
  - `get_user_by_id` (method, line 468) `def get_user_by_id(self, user_id)`
  - `get_user_by_email` (method, line 482) `def get_user_by_email(self, email)`
  - `get_user_by_phone` (method, line 496) `def get_user_by_phone(self, phone)`
  - `get_user_by_confirmation_token` (method, line 510) `def get_user_by_confirmation_token(self, token)`
  - `get_recovery_bundle` (method, line 524) `def get_recovery_bundle(self, username)`
  - `reset_credentials_with_recovery` (method, line 548) `def reset_credentials_with_recovery(self, username, srp_salt, srp_verifier, kdf_salt, encrypted_private_key)`
  - `update_role` (method, line 579) `def update_role(self, username, role, storage_quota, subscription_status)`
  - `count_users` (method, line 592) `def count_users(self)`
  - `get_all_users` (method, line 603) `def get_all_users(self)`
  - `_parse_datetime` (method, line 615) `def _parse_datetime(value)`
  - `_convert_row_to_dict` (method, line 638) `def _convert_row_to_dict(self, row)`
  - `fetch_one` (method, line 694) `def fetch_one(self, query, params)`
  - `value` (method, line 655) `def value(name, default)`
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`
