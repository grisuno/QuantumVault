# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 72 | **Total Symbols Extracted:** 434 | **Total Imports:** 353

## Structural Knowledge Map
> **Note:** The visual graph below has been intelligently pruned to the top 300 most relevant nodes to prevent rendering crashes. Full details of all 72 files are documented below.

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
    app_factory_py["app_factory.py (py)"]
    class app_factory_py mod;
    app_factory_py__is_production["_is_production"]
    class app_factory_py__is_production fn;
    app_factory_py --> app_factory_py__is_production
    app_factory_py__build_csp["_build_csp"]
    class app_factory_py__build_csp fn;
    app_factory_py --> app_factory_py__build_csp
    app_factory_py__build_talisman_kwargs["_build_talisman_kwargs"]
    class app_factory_py__build_talisman_kwargs fn;
    app_factory_py --> app_factory_py__build_talisman_kwargs
    app_factory_py__configure_secret_key["_configure_secret_key"]
    class app_factory_py__configure_secret_key fn;
    app_factory_py --> app_factory_py__configure_secret_key
    app_factory_py__configure_session["_configure_session"]
    class app_factory_py__configure_session fn;
    app_factory_py --> app_factory_py__configure_session
    views_admin_py["admin.py (py)"]
    class views_admin_py mod;
    views_admin_py_UserEditForm["UserEditForm"]
    class views_admin_py_UserEditForm cls;
    views_admin_py --> views_admin_py_UserEditForm
    views_admin_py_PlanForm["PlanForm"]
    class views_admin_py_PlanForm cls;
    views_admin_py --> views_admin_py_PlanForm
    views_admin_py_admin["admin"]
    class views_admin_py_admin fn;
    views_admin_py --> views_admin_py_admin
    views_admin_py_superadmin_edit_user["superadmin_edit_user"]
    class views_admin_py_superadmin_edit_user fn;
    views_admin_py --> views_admin_py_superadmin_edit_user
    views_admin_py_manage_plans["manage_plans"]
    class views_admin_py_manage_plans fn;
    views_admin_py --> views_admin_py_manage_plans
    views_auth_py["auth.py (py)"]
    class views_auth_py mod;
    views_auth_py_role_required["role_required"]
    class views_auth_py_role_required fn;
    views_auth_py --> views_auth_py_role_required
    views_auth_py_PhoneVerificationForm["PhoneVerificationForm"]
    class views_auth_py_PhoneVerificationForm cls;
    views_auth_py --> views_auth_py_PhoneVerificationForm
    views_auth_py_MFAForm["MFAForm"]
    class views_auth_py_MFAForm cls;
    views_auth_py --> views_auth_py_MFAForm
    views_auth_py_ContactForm["ContactForm"]
    class views_auth_py_ContactForm cls;
    views_auth_py --> views_auth_py_ContactForm
    views_auth_py_RegisterForm["RegisterForm"]
    class views_auth_py_RegisterForm cls;
    views_auth_py --> views_auth_py_RegisterForm
    controllers_auth_py["auth.py (py)"]
    class controllers_auth_py mod;
    controllers_auth_py__now_utc["_now_utc"]
    class controllers_auth_py__now_utc fn;
    controllers_auth_py --> controllers_auth_py__now_utc
    controllers_auth_py_AuthController["AuthController"]
    class controllers_auth_py_AuthController cls;
    controllers_auth_py --> controllers_auth_py_AuthController
    controllers_auth_py___init__["__init__"]
    class controllers_auth_py___init__ fn;
    controllers_auth_py --> controllers_auth_py___init__
    controllers_auth_py_register["register"]
    class controllers_auth_py_register fn;
    controllers_auth_py --> controllers_auth_py_register
    controllers_auth_py_send_confirmation_email["send_confirmation_email"]
    class controllers_auth_py_send_confirmation_email fn;
    controllers_auth_py --> controllers_auth_py_send_confirmation_email
    utils_security_py["security.py (py)"]
    class utils_security_py mod;
    utils_security_py__get_audit_logger["_get_audit_logger"]
    class utils_security_py__get_audit_logger fn;
    utils_security_py --> utils_security_py__get_audit_logger
    utils_security_py__correlation_id["_correlation_id"]
    class utils_security_py__correlation_id fn;
    utils_security_py --> utils_security_py__correlation_id
    utils_security_py_audit_event["audit_event"]
    class utils_security_py_audit_event fn;
    utils_security_py --> utils_security_py_audit_event
    utils_security_py_constant_time_compare["constant_time_compare"]
    class utils_security_py_constant_time_compare fn;
    utils_security_py --> utils_security_py_constant_time_compare
    utils_security_py_hash_secret["hash_secret"]
    class utils_security_py_hash_secret fn;
    utils_security_py --> utils_security_py_hash_secret
    enc_dec_go["enc_dec.go (go)"]
    class enc_dec_go mod;
    enc_dec_go_deriveAESKey["deriveAESKey"]
    class enc_dec_go_deriveAESKey fn;
    enc_dec_go --> enc_dec_go_deriveAESKey
    enc_dec_go_encryptFile["encryptFile"]
    class enc_dec_go_encryptFile fn;
    enc_dec_go --> enc_dec_go_encryptFile
    enc_dec_go_decryptFile["decryptFile"]
    class enc_dec_go_decryptFile fn;
    enc_dec_go --> enc_dec_go_decryptFile
    enc_dec_go_main["main"]
    class enc_dec_go_main fn;
    enc_dec_go --> enc_dec_go_main
    views_subscription_py["subscription.py (py)"]
    class views_subscription_py mod;
    views_subscription_py_SubscriptionForm["SubscriptionForm"]
    class views_subscription_py_SubscriptionForm cls;
    views_subscription_py --> views_subscription_py_SubscriptionForm
    views_subscription_py_subscribe["subscribe"]
    class views_subscription_py_subscribe fn;
    views_subscription_py --> views_subscription_py_subscribe
    views_subscription_py_payment_success["payment_success"]
    class views_subscription_py_payment_success fn;
    views_subscription_py --> views_subscription_py_payment_success
    views_subscription_py___init__["__init__"]
    class views_subscription_py___init__ fn;
    views_subscription_py --> views_subscription_py___init__
    utils_scheduler_py["scheduler.py (py)"]
    class utils_scheduler_py mod;
    utils_scheduler_py__now_utc["_now_utc"]
    class utils_scheduler_py__now_utc fn;
    utils_scheduler_py --> utils_scheduler_py__now_utc
    utils_scheduler_py_init_scheduler["init_scheduler"]
    class utils_scheduler_py_init_scheduler fn;
    utils_scheduler_py --> utils_scheduler_py_init_scheduler
    utils_scheduler_py__is_trial_elapsed["_is_trial_elapsed"]
    class utils_scheduler_py__is_trial_elapsed fn;
    utils_scheduler_py --> utils_scheduler_py__is_trial_elapsed
    utils_scheduler_py_check_trial_expiration["check_trial_expiration"]
    class utils_scheduler_py_check_trial_expiration fn;
    utils_scheduler_py --> utils_scheduler_py_check_trial_expiration
    utils_scheduler_py_cleanup_old_messages["cleanup_old_messages"]
    class utils_scheduler_py_cleanup_old_messages fn;
    utils_scheduler_py --> utils_scheduler_py_cleanup_old_messages
    controllers_deniable_vault_py["deniable_vault.py (py)"]
    class controllers_deniable_vault_py mod;
    controllers_deniable_vault_py__base64_length["_base64_length"]
    class controllers_deniable_vault_py__base64_length fn;
    controllers_deniable_vault_py --> controllers_deniable_vault_py__base64_length
    controllers_deniable_vault_py_canonical_json["canonical_json"]
    class controllers_deniable_vault_py_canonical_json fn;
    controllers_deniable_vault_py --> controllers_deniable_vault_py_canonical_json
    controllers_deniable_vault_py_EnvelopeValidationError["EnvelopeValidationError"]
    class controllers_deniable_vault_py_EnvelopeValidationError cls;
    controllers_deniable_vault_py --> controllers_deniable_vault_py_EnvelopeValidationError
    controllers_deniable_vault_py__coerce_int["_coerce_int"]
    class controllers_deniable_vault_py__coerce_int fn;
    controllers_deniable_vault_py --> controllers_deniable_vault_py__coerce_int
    controllers_deniable_vault_py__coerce_kdf["_coerce_kdf"]
    class controllers_deniable_vault_py__coerce_kdf fn;
    controllers_deniable_vault_py --> controllers_deniable_vault_py__coerce_kdf
    enc_dec_py["enc_dec.py (py)"]
    class enc_dec_py mod;
    enc_dec_py_derive_aes_key["derive_aes_key"]
    class enc_dec_py_derive_aes_key fn;
    enc_dec_py --> enc_dec_py_derive_aes_key
    enc_dec_py_encrypt_file_in_memory["encrypt_file_in_memory"]
    class enc_dec_py_encrypt_file_in_memory fn;
    enc_dec_py --> enc_dec_py_encrypt_file_in_memory
    enc_dec_py_decrypt_file_in_memory["decrypt_file_in_memory"]
    class enc_dec_py_decrypt_file_in_memory fn;
    enc_dec_py --> enc_dec_py_decrypt_file_in_memory
    enc_dec_py__build_s3_client["_build_s3_client"]
    class enc_dec_py__build_s3_client fn;
    enc_dec_py --> enc_dec_py__build_s3_client
    enc_dec_py_main["main"]
    class enc_dec_py_main fn;
    enc_dec_py --> enc_dec_py_main
    views_file_py["file.py (py)"]
    class views_file_py mod;
    views_file_py_UploadForm["UploadForm"]
    class views_file_py_UploadForm cls;
    views_file_py --> views_file_py_UploadForm
    views_file_py_upload["upload"]
    class views_file_py_upload fn;
    views_file_py --> views_file_py_upload
    views_file_py_download["download"]
    class views_file_py_download fn;
    views_file_py --> views_file_py_download
    views_message_py["message.py (py)"]
    class views_message_py mod;
    views_message_py_MessageForm["MessageForm"]
    class views_message_py_MessageForm cls;
    views_message_py --> views_message_py_MessageForm
    views_message_py_messages["messages"]
    class views_message_py_messages fn;
    views_message_py --> views_message_py_messages
    views_message_py_api_secure_message["api_secure_message"]
    class views_message_py_api_secure_message fn;
    views_message_py --> views_message_py_api_secure_message
    tests_test_deniable_vault_py["test_deniable_vault.py (py)"]
    class tests_test_deniable_vault_py mod;
    tests_test_deniable_vault_py_config["config"]
    class tests_test_deniable_vault_py_config fn;
    tests_test_deniable_vault_py --> tests_test_deniable_vault_py_config
    tests_test_deniable_vault_py_validator["validator"]
    class tests_test_deniable_vault_py_validator fn;
    tests_test_deniable_vault_py --> tests_test_deniable_vault_py_validator
    tests_test_deniable_vault_py__ciphertext["_ciphertext"]
    class tests_test_deniable_vault_py__ciphertext fn;
    tests_test_deniable_vault_py --> tests_test_deniable_vault_py__ciphertext
    tests_test_deniable_vault_py__valid_envelope["_valid_envelope"]
    class tests_test_deniable_vault_py__valid_envelope fn;
    tests_test_deniable_vault_py --> tests_test_deniable_vault_py__valid_envelope
    tests_test_deniable_vault_py__make_user["_make_user"]
    class tests_test_deniable_vault_py__make_user fn;
    tests_test_deniable_vault_py --> tests_test_deniable_vault_py__make_user
    models_contact_py["contact.py (py)"]
    class models_contact_py mod;
    models_contact_py_ContactModel["ContactModel"]
    class models_contact_py_ContactModel cls;
    models_contact_py --> models_contact_py_ContactModel
    models_contact_py_ContactDB["ContactDB"]
    class models_contact_py_ContactDB cls;
    models_contact_py --> models_contact_py_ContactDB
    models_contact_py___init__["__init__"]
    class models_contact_py___init__ fn;
    models_contact_py --> models_contact_py___init__
    models_contact_py__init_db["_init_db"]
    class models_contact_py__init_db fn;
    models_contact_py --> models_contact_py__init_db
    models_contact_py_create_contact["create_contact"]
    class models_contact_py_create_contact fn;
    models_contact_py --> models_contact_py_create_contact
    models_message_py["message.py (py)"]
    class models_message_py mod;
    models_message_py_MessageModel["MessageModel"]
    class models_message_py_MessageModel cls;
    models_message_py --> models_message_py_MessageModel
    models_message_py_MessageDB["MessageDB"]
    class models_message_py_MessageDB cls;
    models_message_py --> models_message_py_MessageDB
    models_message_py___init__["__init__"]
    class models_message_py___init__ fn;
    models_message_py --> models_message_py___init__
    models_message_py_save_message["save_message"]
    class models_message_py_save_message fn;
    models_message_py --> models_message_py_save_message
    models_message_py_get_messages["get_messages"]
    class models_message_py_get_messages fn;
    models_message_py --> models_message_py_get_messages
    scripts_email_tool_py["email_tool.py (py)"]
    class scripts_email_tool_py mod;
    scripts_email_tool_py__build_mail_app["_build_mail_app"]
    class scripts_email_tool_py__build_mail_app fn;
    scripts_email_tool_py --> scripts_email_tool_py__build_mail_app
    scripts_email_tool_py_cmd_test_smtp["cmd_test_smtp"]
    class scripts_email_tool_py_cmd_test_smtp fn;
    scripts_email_tool_py --> scripts_email_tool_py_cmd_test_smtp
    scripts_email_tool_py_cmd_link["cmd_link"]
    class scripts_email_tool_py_cmd_link fn;
    scripts_email_tool_py --> scripts_email_tool_py_cmd_link
    scripts_email_tool_py_cmd_confirm["cmd_confirm"]
    class scripts_email_tool_py_cmd_confirm fn;
    scripts_email_tool_py --> scripts_email_tool_py_cmd_confirm
    scripts_email_tool_py_build_parser["build_parser"]
    class scripts_email_tool_py_build_parser fn;
    scripts_email_tool_py --> scripts_email_tool_py_build_parser
    views_account_py["account.py (py)"]
    class views_account_py mod;
    views_account_py_get_deniable_vault_controller["get_deniable_vault_controller"]
    class views_account_py_get_deniable_vault_controller fn;
    views_account_py --> views_account_py_get_deniable_vault_controller
    views_account_py_settings["settings"]
    class views_account_py_settings fn;
    views_account_py --> views_account_py_settings
    views_account_py_get_vault["get_vault"]
    class views_account_py_get_vault fn;
    views_account_py --> views_account_py_get_vault
    views_account_py_put_vault["put_vault"]
    class views_account_py_put_vault fn;
    views_account_py --> views_account_py_put_vault
    views_account_py_delete_vault["delete_vault"]
    class views_account_py_delete_vault fn;
    views_account_py --> views_account_py_delete_vault
    models_user_py["user.py (py)"]
    class models_user_py mod;
    models_user_py_UserModel["UserModel"]
    class models_user_py_UserModel cls;
    models_user_py --> models_user_py_UserModel
    models_user_py_UserDB["UserDB"]
    class models_user_py_UserDB cls;
    models_user_py --> models_user_py_UserDB
    models_user_py_get_id["get_id"]
    class models_user_py_get_id fn;
    models_user_py --> models_user_py_get_id
    models_user_py_is_active["is_active"]
    class models_user_py_is_active fn;
    models_user_py --> models_user_py_is_active
    models_user_py___init__["__init__"]
    class models_user_py___init__ fn;
    models_user_py --> models_user_py___init__
    scripts_test_bloque1_py["test_bloque1.py (py)"]
    class scripts_test_bloque1_py mod;
    scripts_test_bloque1_py__FakeUser["_FakeUser"]
    class scripts_test_bloque1_py__FakeUser cls;
    scripts_test_bloque1_py --> scripts_test_bloque1_py__FakeUser
    scripts_test_bloque1_py__load_user["_load_user"]
    class scripts_test_bloque1_py__load_user fn;
    scripts_test_bloque1_py --> scripts_test_bloque1_py__load_user
    scripts_test_bloque1_py_check["check"]
    class scripts_test_bloque1_py_check fn;
    scripts_test_bloque1_py --> scripts_test_bloque1_py_check
    scripts_test_bloque1_py___init__["__init__"]
    class scripts_test_bloque1_py___init__ fn;
    scripts_test_bloque1_py --> scripts_test_bloque1_py___init__
    scripts_test_bloque1_py_is_authenticated["is_authenticated"]
    class scripts_test_bloque1_py_is_authenticated fn;
    scripts_test_bloque1_py --> scripts_test_bloque1_py_is_authenticated
    tests_conftest_py["conftest.py (py)"]
    class tests_conftest_py mod;
    tests_conftest_py__push_request_context["_push_request_context"]
    class tests_conftest_py__push_request_context fn;
    tests_conftest_py --> tests_conftest_py__push_request_context
    tests_conftest_py_app["app"]
    class tests_conftest_py_app fn;
    tests_conftest_py --> tests_conftest_py_app
    tests_conftest_py_client["client"]
    class tests_conftest_py_client fn;
    tests_conftest_py --> tests_conftest_py_client
    tests_conftest_py__ListLogHandler["_ListLogHandler"]
    class tests_conftest_py__ListLogHandler cls;
    tests_conftest_py --> tests_conftest_py__ListLogHandler
    tests_conftest_py_audit_records["audit_records"]
    class tests_conftest_py_audit_records fn;
    tests_conftest_py --> tests_conftest_py_audit_records
    views_sync_py["sync.py (py)"]
    class views_sync_py mod;
    views_sync_py_secure_sync["secure_sync"]
    class views_sync_py_secure_sync fn;
    views_sync_py --> views_sync_py_secure_sync
    views_sync_py_sync_page["sync_page"]
    class views_sync_py_sync_page fn;
    views_sync_py --> views_sync_py_sync_page
    client_go["client.go (go)"]
    class client_go mod;
    client_go_main["main"]
    class client_go_main fn;
    client_go --> client_go_main
    client_py["client.py (py)"]
    class client_py mod;
    utils_srp6a_py["srp6a.py (py)"]
    class utils_srp6a_py mod;
    utils_srp6a_py_i2osp["i2osp"]
    class utils_srp6a_py_i2osp fn;
    utils_srp6a_py --> utils_srp6a_py_i2osp
    utils_srp6a_py__hash["_hash"]
    class utils_srp6a_py__hash fn;
    utils_srp6a_py --> utils_srp6a_py__hash
    utils_srp6a_py__hash_int["_hash_int"]
    class utils_srp6a_py__hash_int fn;
    utils_srp6a_py --> utils_srp6a_py__hash_int
    utils_srp6a_py_compute_k["compute_k"]
    class utils_srp6a_py_compute_k fn;
    utils_srp6a_py --> utils_srp6a_py_compute_k
    utils_srp6a_py_compute_u["compute_u"]
    class utils_srp6a_py_compute_u fn;
    utils_srp6a_py --> utils_srp6a_py_compute_u
    controllers_file_py["file.py (py)"]
    class controllers_file_py mod;
    controllers_file_py__log_s3_error["_log_s3_error"]
    class controllers_file_py__log_s3_error fn;
    controllers_file_py --> controllers_file_py__log_s3_error
    controllers_file_py_safe_filename["safe_filename"]
    class controllers_file_py_safe_filename fn;
    controllers_file_py --> controllers_file_py_safe_filename
    controllers_file_py_FileController["FileController"]
    class controllers_file_py_FileController cls;
    controllers_file_py --> controllers_file_py_FileController
    controllers_file_py___init__["__init__"]
    class controllers_file_py___init__ fn;
    controllers_file_py --> controllers_file_py___init__
    controllers_file_py__key["_key"]
    class controllers_file_py__key fn;
    controllers_file_py --> controllers_file_py__key
    utils_utils_py["utils.py (py)"]
    class utils_utils_py mod;
    utils_utils_py_as_bool["as_bool"]
    class utils_utils_py_as_bool fn;
    utils_utils_py --> utils_utils_py_as_bool
    utils_utils_py_sanitize_path["sanitize_path"]
    class utils_utils_py_sanitize_path fn;
    utils_utils_py --> utils_utils_py_sanitize_path
    utils_utils_py_Payload["Payload"]
    class utils_utils_py_Payload cls;
    utils_utils_py --> utils_utils_py_Payload
    utils_utils_py_Config["Config"]
    class utils_utils_py_Config cls;
    utils_utils_py --> utils_utils_py_Config
    utils_utils_py_load_payload["load_payload"]
    class utils_utils_py_load_payload fn;
    utils_utils_py --> utils_utils_py_load_payload
    tests_test_security_py["test_security.py (py)"]
    class tests_test_security_py mod;
    tests_test_security_py_test_audit_event_includes_ip_and_ua_by_default["test_audit_event_includes_ip_and_ua_by_default"]
    class tests_test_security_py_test_audit_event_includes_ip_and_ua_by_default fn;
    tests_test_security_py --> tests_test_security_py_test_audit_event_includes_ip_and_ua_by_default
    tests_test_security_py_test_audit_event_redacts_ip_and_ua_when_disabled["test_audit_event_redacts_ip_and_ua_when_disabled"]
    class tests_test_security_py_test_audit_event_redacts_ip_and_ua_when_disabled fn;
    tests_test_security_py --> tests_test_security_py_test_audit_event_redacts_ip_and_ua_when_disabled
    tests_test_security_py_test_json_csrf_protect_rejects_missing_token["test_json_csrf_protect_rejects_missing_token"]
    class tests_test_security_py_test_json_csrf_protect_rejects_missing_token fn;
    tests_test_security_py --> tests_test_security_py_test_json_csrf_protect_rejects_missing_token
    tests_test_security_py_test_json_csrf_protect_accepts_valid_header_token["test_json_csrf_protect_accepts_valid_header_token"]
    class tests_test_security_py_test_json_csrf_protect_accepts_valid_header_token fn;
    tests_test_security_py --> tests_test_security_py_test_json_csrf_protect_accepts_valid_header_token
    tests_test_security_py_test_json_csrf_protect_passes_get_through_without_token["test_json_csrf_protect_passes_get_through_without_token"]
    class tests_test_security_py_test_json_csrf_protect_passes_get_through_without_token fn;
    tests_test_security_py --> tests_test_security_py_test_json_csrf_protect_passes_get_through_without_token
    controllers_message_py["message.py (py)"]
    class controllers_message_py mod;
    controllers_message_py_MessageController["MessageController"]
    class controllers_message_py_MessageController cls;
    controllers_message_py --> controllers_message_py_MessageController
    controllers_message_py___init__["__init__"]
    class controllers_message_py___init__ fn;
    controllers_message_py --> controllers_message_py___init__
    controllers_message_py_send_encrypted_message["send_encrypted_message"]
    class controllers_message_py_send_encrypted_message fn;
    controllers_message_py --> controllers_message_py_send_encrypted_message
    controllers_message_py_get_messages["get_messages"]
    class controllers_message_py_get_messages fn;
    controllers_message_py --> controllers_message_py_get_messages
    server_go["server.go (go)"]
    class server_go mod;
    server_go_main["main"]
    class server_go_main fn;
    server_go --> server_go_main
    server_go_handleConnection["handleConnection"]
    class server_go_handleConnection fn;
    server_go --> server_go_handleConnection
    views_views_py["views.py (py)"]
    class views_views_py mod;
    views_views_py_MFAEnableForm["MFAEnableForm"]
    class views_views_py_MFAEnableForm cls;
    views_views_py --> views_views_py_MFAEnableForm
    views_views_py_home["home"]
    class views_views_py_home fn;
    views_views_py --> views_views_py_home
    server_py["server.py (py)"]
    class server_py mod;
    models_deniable_vault_py["deniable_vault.py (py)"]
    class models_deniable_vault_py mod;
    models_deniable_vault_py_DeniableVaultDB["DeniableVaultDB"]
    class models_deniable_vault_py_DeniableVaultDB cls;
    models_deniable_vault_py --> models_deniable_vault_py_DeniableVaultDB
    models_deniable_vault_py___init__["__init__"]
    class models_deniable_vault_py___init__ fn;
    models_deniable_vault_py --> models_deniable_vault_py___init__
    models_deniable_vault_py__init_db["_init_db"]
    class models_deniable_vault_py__init_db fn;
    models_deniable_vault_py --> models_deniable_vault_py__init_db
    models_deniable_vault_py_upsert["upsert"]
    class models_deniable_vault_py_upsert fn;
    models_deniable_vault_py --> models_deniable_vault_py_upsert
    models_deniable_vault_py_get["get"]
    class models_deniable_vault_py_get fn;
    models_deniable_vault_py --> models_deniable_vault_py_get
    tests_test_srp_py["test_srp.py (py)"]
    class tests_test_srp_py mod;
    tests_test_srp_py__h["_h"]
    class tests_test_srp_py__h fn;
    tests_test_srp_py --> tests_test_srp_py__h
    tests_test_srp_py__hint["_hint"]
    class tests_test_srp_py__hint fn;
    tests_test_srp_py --> tests_test_srp_py__hint
    tests_test_srp_py__client_derive_verifier["_client_derive_verifier"]
    class tests_test_srp_py__client_derive_verifier fn;
    tests_test_srp_py --> tests_test_srp_py__client_derive_verifier
    tests_test_srp_py__client_compute_proof["_client_compute_proof"]
    class tests_test_srp_py__client_compute_proof fn;
    tests_test_srp_py --> tests_test_srp_py__client_compute_proof
    tests_test_srp_py_test_srp6a_full_roundtrip_matches_server_proofs["test_srp6a_full_roundtrip_matches_server_proofs"]
    class tests_test_srp_py_test_srp6a_full_roundtrip_matches_server_proofs fn;
    tests_test_srp_py --> tests_test_srp_py_test_srp6a_full_roundtrip_matches_server_proofs
    scripts_makeadmin_py["makeadmin.py (py)"]
    class scripts_makeadmin_py mod;
    scripts_makeadmin_py__resolve_db_path["_resolve_db_path"]
    class scripts_makeadmin_py__resolve_db_path fn;
    scripts_makeadmin_py --> scripts_makeadmin_py__resolve_db_path
    scripts_makeadmin_py__print_user_summary["_print_user_summary"]
    class scripts_makeadmin_py__print_user_summary fn;
    scripts_makeadmin_py --> scripts_makeadmin_py__print_user_summary
    scripts_makeadmin_py_cmd_promote["cmd_promote"]
    class scripts_makeadmin_py_cmd_promote fn;
    scripts_makeadmin_py --> scripts_makeadmin_py_cmd_promote
    scripts_makeadmin_py_build_parser["build_parser"]
    class scripts_makeadmin_py_build_parser fn;
    scripts_makeadmin_py --> scripts_makeadmin_py_build_parser
    scripts_makeadmin_py_main["main"]
    class scripts_makeadmin_py_main fn;
    scripts_makeadmin_py --> scripts_makeadmin_py_main
    controllers_sync_py["sync.py (py)"]
    class controllers_sync_py mod;
    controllers_sync_py_SyncController["SyncController"]
    class controllers_sync_py_SyncController cls;
    controllers_sync_py --> controllers_sync_py_SyncController
    controllers_sync_py___init__["__init__"]
    class controllers_sync_py___init__ fn;
    controllers_sync_py --> controllers_sync_py___init__
    controllers_sync_py_get_storage_usage["get_storage_usage"]
    class controllers_sync_py_get_storage_usage fn;
    controllers_sync_py --> controllers_sync_py_get_storage_usage
    app_py["app.py (py)"]
    class app_py mod;
    app_py_main["main"]
    class app_py_main fn;
    app_py --> app_py_main
    app_py__is_production_like["_is_production_like"]
    class app_py__is_production_like fn;
    app_py --> app_py__is_production_like
    models_superadmin_audit_py["superadmin_audit.py (py)"]
    class models_superadmin_audit_py mod;
    models_superadmin_audit_py_SuperadminAuditDB["SuperadminAuditDB"]
    class models_superadmin_audit_py_SuperadminAuditDB cls;
    models_superadmin_audit_py --> models_superadmin_audit_py_SuperadminAuditDB
    models_superadmin_audit_py___init__["__init__"]
    class models_superadmin_audit_py___init__ fn;
    models_superadmin_audit_py --> models_superadmin_audit_py___init__
    models_superadmin_audit_py__init_db["_init_db"]
    class models_superadmin_audit_py__init_db fn;
    models_superadmin_audit_py --> models_superadmin_audit_py__init_db
    models_superadmin_audit_py_record["record"]
    class models_superadmin_audit_py_record fn;
    models_superadmin_audit_py --> models_superadmin_audit_py_record
    models_superadmin_audit_py_recent["recent"]
    class models_superadmin_audit_py_recent fn;
    models_superadmin_audit_py --> models_superadmin_audit_py_recent
    utils_cache_py["cache.py (py)"]
    class utils_cache_py mod;
    utils_cache_py_Cache["Cache"]
    class utils_cache_py_Cache cls;
    utils_cache_py --> utils_cache_py_Cache
    utils_cache_py___init__["__init__"]
    class utils_cache_py___init__ fn;
    utils_cache_py --> utils_cache_py___init__
    utils_cache_py_get["get"]
    class utils_cache_py_get fn;
    utils_cache_py --> utils_cache_py_get
    utils_cache_py_set["set"]
    class utils_cache_py_set fn;
    utils_cache_py --> utils_cache_py_set
    utils_cache_py_delete["delete"]
    class utils_cache_py_delete fn;
    utils_cache_py --> utils_cache_py_delete
    utils_mailer_py["mailer.py (py)"]
    class utils_mailer_py mod;
    utils_mailer_py_external_url["external_url"]
    class utils_mailer_py_external_url fn;
    utils_mailer_py --> utils_mailer_py_external_url
    utils_mailer_py_mail_is_configured["mail_is_configured"]
    class utils_mailer_py_mail_is_configured fn;
    utils_mailer_py --> utils_mailer_py_mail_is_configured
    utils_mailer_py_send_transactional_email["send_transactional_email"]
    class utils_mailer_py_send_transactional_email fn;
    utils_mailer_py --> utils_mailer_py_send_transactional_email
    scripts_doctor_py["doctor.py (py)"]
    class scripts_doctor_py mod;
    models_plans_py["plans.py (py)"]
    class models_plans_py mod;
    models_plans_py_PlanDB["PlanDB"]
    class models_plans_py_PlanDB cls;
    models_plans_py --> models_plans_py_PlanDB
    models_plans_py___init__["__init__"]
    class models_plans_py___init__ fn;
    models_plans_py --> models_plans_py___init__
    models_plans_py__init_db["_init_db"]
    class models_plans_py__init_db fn;
    models_plans_py --> models_plans_py__init_db
    models_plans_py_get_plan["get_plan"]
    class models_plans_py_get_plan fn;
    models_plans_py --> models_plans_py_get_plan
    models_plans_py_get_all_plans["get_all_plans"]
    class models_plans_py_get_all_plans fn;
    models_plans_py --> models_plans_py_get_all_plans
    controllers_contact_py["contact.py (py)"]
    class controllers_contact_py mod;
    controllers_contact_py_ContactController["ContactController"]
    class controllers_contact_py_ContactController cls;
    controllers_contact_py --> controllers_contact_py_ContactController
    controllers_contact_py___init__["__init__"]
    class controllers_contact_py___init__ fn;
    controllers_contact_py --> controllers_contact_py___init__
    controllers_contact_py_create_contact["create_contact"]
    class controllers_contact_py_create_contact fn;
    controllers_contact_py --> controllers_contact_py_create_contact
    controllers_contact_py_get_user_contacts["get_user_contacts"]
    class controllers_contact_py_get_user_contacts fn;
    controllers_contact_py --> controllers_contact_py_get_user_contacts
    views_faq_py["faq.py (py)"]
    class views_faq_py mod;
    views_faq_py_faq["faq"]
    class views_faq_py_faq fn;
    views_faq_py --> views_faq_py_faq
    views_faq_py_landing["landing"]
    class views_faq_py_landing fn;
    views_faq_py --> views_faq_py_landing
    pq_decrypt_password_py["pq_decrypt_password.py (py)"]
    class pq_decrypt_password_py mod;
    wsgi_py["wsgi.py (py)"]
    class wsgi_py mod;
    tests_test_auth_phone_py["test_auth_phone.py (py)"]
    class tests_test_auth_phone_py mod;
    tests_test_auth_phone_py_test_verify_phone_page_renders["test_verify_phone_page_renders"]
    class tests_test_auth_phone_py_test_verify_phone_page_renders fn;
    tests_test_auth_phone_py --> tests_test_auth_phone_py_test_verify_phone_page_renders
    tests_test_auth_phone_py_test_resend_endpoint_is_registered["test_resend_endpoint_is_registered"]
    class tests_test_auth_phone_py_test_resend_endpoint_is_registered fn;
    tests_test_auth_phone_py --> tests_test_auth_phone_py_test_resend_endpoint_is_registered
    tests_test_auth_phone_py_test_resend_route_accepts_only_post["test_resend_route_accepts_only_post"]
    class tests_test_auth_phone_py_test_resend_route_accepts_only_post fn;
    tests_test_auth_phone_py --> tests_test_auth_phone_py_test_resend_route_accepts_only_post
    utils_plans_py["plans.py (py)"]
    class utils_plans_py mod;
    utils_plans_py_SubscriptionPlans["SubscriptionPlans"]
    class utils_plans_py_SubscriptionPlans cls;
    utils_plans_py --> utils_plans_py_SubscriptionPlans
    utils_plans_py_get_plan["get_plan"]
    class utils_plans_py_get_plan fn;
    utils_plans_py --> utils_plans_py_get_plan
    utils_plans_py_validate_plan_payment["validate_plan_payment"]
    class utils_plans_py_validate_plan_payment fn;
    utils_plans_py --> utils_plans_py_validate_plan_payment
    templates_terms_py["terms.py (py)"]
    class templates_terms_py mod;
    templates_terms_py_terms["terms"]
    class templates_terms_py_terms fn;
    templates_terms_py --> templates_terms_py_terms
    views_about_py["about.py (py)"]
    class views_about_py mod;
    views_about_py_about["about"]
    class views_about_py_about fn;
    views_about_py --> views_about_py_about
    views_privacy_py["privacy.py (py)"]
    class views_privacy_py mod;
    views_privacy_py_privacy["privacy"]
    class views_privacy_py_privacy fn;
    views_privacy_py --> views_privacy_py_privacy
    views_terms_py["terms.py (py)"]
    class views_terms_py mod;
    views_terms_py_terms["terms"]
    class views_terms_py_terms fn;
    views_terms_py --> views_terms_py_terms
    lol_py["lol.py (py)"]
    class lol_py mod;
    static_js_qv_crypto_js["qv-crypto.js (js)"]
    class static_js_qv_crypto_js mod;
    static_js_qv_crypto_js_concatBytes["concatBytes"]
    class static_js_qv_crypto_js_concatBytes fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_concatBytes
    static_js_qv_crypto_js_hexToBytes["hexToBytes"]
    class static_js_qv_crypto_js_hexToBytes fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_hexToBytes
    static_js_qv_crypto_js_bytesToHex["bytesToHex"]
    class static_js_qv_crypto_js_bytesToHex fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_bytesToHex
    static_js_qv_crypto_js_bytesToBase64["bytesToBase64"]
    class static_js_qv_crypto_js_bytesToBase64 fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_bytesToBase64
    static_js_qv_crypto_js_bytesToBase32["bytesToBase32"]
    class static_js_qv_crypto_js_bytesToBase32 fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_bytesToBase32
    static_js_account_js["account.js (js)"]
    class static_js_account_js mod;
    static_js_account_js_setStatus["setStatus"]
    class static_js_account_js_setStatus fn;
    static_js_account_js --> static_js_account_js_setStatus
    static_js_account_js_csrfToken["csrfToken"]
    class static_js_account_js_csrfToken fn;
    static_js_account_js --> static_js_account_js_csrfToken
    static_js_account_js_apiRequest["apiRequest"]
    class static_js_account_js_apiRequest fn;
    static_js_account_js --> static_js_account_js_apiRequest
    static_js_account_js_loadState["loadState"]
    class static_js_account_js_loadState fn;
    static_js_account_js --> static_js_account_js_loadState
    static_js_account_js_collectSlots["collectSlots"]
    class static_js_account_js_collectSlots fn;
    static_js_account_js --> static_js_account_js_collectSlots
    static_js_qv_deniable_js["qv-deniable.js (js)"]
    class static_js_qv_deniable_js mod;
    static_js_qv_deniable_js_toBytes["toBytes"]
    class static_js_qv_deniable_js_toBytes fn;
    static_js_qv_deniable_js --> static_js_qv_deniable_js_toBytes
    static_js_qv_deniable_js_frame["frame"]
    class static_js_qv_deniable_js_frame fn;
    static_js_qv_deniable_js --> static_js_qv_deniable_js_frame
    static_js_qv_deniable_js_unframe["unframe"]
    class static_js_qv_deniable_js_unframe fn;
    static_js_qv_deniable_js --> static_js_qv_deniable_js_unframe
    static_js_qv_deniable_js_sealSlot["sealSlot"]
    class static_js_qv_deniable_js_sealSlot fn;
    static_js_qv_deniable_js --> static_js_qv_deniable_js_sealSlot
    static_js_qv_deniable_js_openSlot["openSlot"]
    class static_js_qv_deniable_js_openSlot fn;
    static_js_qv_deniable_js --> static_js_qv_deniable_js_openSlot
    static_js_messages_js["messages.js (js)"]
    class static_js_messages_js mod;
    static_js_messages_js_getCsrfToken["getCsrfToken"]
    class static_js_messages_js_getCsrfToken fn;
    static_js_messages_js --> static_js_messages_js_getCsrfToken
    static_js_messages_js_handleSend["handleSend"]
    class static_js_messages_js_handleSend fn;
    static_js_messages_js --> static_js_messages_js_handleSend
    static_js_messages_js_collectEnvelopes["collectEnvelopes"]
    class static_js_messages_js_collectEnvelopes fn;
    static_js_messages_js --> static_js_messages_js_collectEnvelopes
    static_js_messages_js_handleDecryptInbox["handleDecryptInbox"]
    class static_js_messages_js_handleDecryptInbox fn;
    static_js_messages_js --> static_js_messages_js_handleDecryptInbox
    static_js_messages_js_initEditor["initEditor"]
    class static_js_messages_js_initEditor fn;
    static_js_messages_js --> static_js_messages_js_initEditor
    static_js_upload_js["upload.js (js)"]
    class static_js_upload_js mod;
    static_js_upload_js_getCsrfToken["getCsrfToken"]
    class static_js_upload_js_getCsrfToken fn;
    static_js_upload_js --> static_js_upload_js_getCsrfToken
    static_js_upload_js_getUsername["getUsername"]
    class static_js_upload_js_getUsername fn;
    static_js_upload_js --> static_js_upload_js_getUsername
    static_js_upload_js_getPublicKey["getPublicKey"]
    class static_js_upload_js_getPublicKey fn;
    static_js_upload_js --> static_js_upload_js_getPublicKey
    static_js_upload_js_handleUpload["handleUpload"]
    class static_js_upload_js_handleUpload fn;
    static_js_upload_js --> static_js_upload_js_handleUpload
    static_js_upload_js_handleDownload["handleDownload"]
    class static_js_upload_js_handleDownload fn;
    static_js_upload_js --> static_js_upload_js_handleDownload
    scripts_garage_native_sh["garage-native.sh (sh)"]
    class scripts_garage_native_sh mod;
    scripts_garage_native_sh_upsert_env["upsert_env"]
    class scripts_garage_native_sh_upsert_env fn;
    scripts_garage_native_sh --> scripts_garage_native_sh_upsert_env
    scripts_garage_native_sh_s3_reachable["s3_reachable"]
    class scripts_garage_native_sh_s3_reachable fn;
    scripts_garage_native_sh --> scripts_garage_native_sh_s3_reachable
    scripts_garage_native_sh_gcmd["gcmd"]
    class scripts_garage_native_sh_gcmd fn;
    scripts_garage_native_sh --> scripts_garage_native_sh_gcmd
    static_js_coded_text_js["coded-text.js (js)"]
    class static_js_coded_text_js mod;
    static_js_coded_text_js_randomChar["randomChar"]
    class static_js_coded_text_js_randomChar fn;
    static_js_coded_text_js --> static_js_coded_text_js_randomChar
    static_js_coded_text_js_animateElement["animateElement"]
    class static_js_coded_text_js_animateElement fn;
    static_js_coded_text_js --> static_js_coded_text_js_animateElement
    static_js_coded_text_js_init["init"]
    class static_js_coded_text_js_init fn;
    static_js_coded_text_js --> static_js_coded_text_js_init
    static_js_recover_js["recover.js (js)"]
    class static_js_recover_js mod;
    static_js_recover_js_setStatus["setStatus"]
    class static_js_recover_js_setStatus fn;
    static_js_recover_js --> static_js_recover_js_setStatus
    static_js_recover_js_handleRecover["handleRecover"]
    class static_js_recover_js_handleRecover fn;
    static_js_recover_js --> static_js_recover_js_handleRecover
    static_js_recover_js_init["init"]
    class static_js_recover_js_init fn;
    static_js_recover_js --> static_js_recover_js_init
    static_js_register_js["register.js (js)"]
    class static_js_register_js mod;
    static_js_register_js_showRecoveryCode["showRecoveryCode"]
    class static_js_register_js_showRecoveryCode fn;
    static_js_register_js --> static_js_register_js_showRecoveryCode
    static_js_register_js_handleRegister["handleRegister"]
    class static_js_register_js_handleRegister fn;
    static_js_register_js --> static_js_register_js_handleRegister
    static_js_register_js_init["init"]
    class static_js_register_js_init fn;
    static_js_register_js --> static_js_register_js_init
    static_js_login_js["login.js (js)"]
    class static_js_login_js mod;
    static_js_login_js_handleLogin["handleLogin"]
    class static_js_login_js_handleLogin fn;
    static_js_login_js --> static_js_login_js_handleLogin
    static_js_login_js_init["init"]
    class static_js_login_js_init fn;
    static_js_login_js --> static_js_login_js_init
    scripts_garage_init_sh["garage-init.sh (sh)"]
    class scripts_garage_init_sh mod;
    scripts_garage_init_sh_upsert_env["upsert_env"]
    class scripts_garage_init_sh_upsert_env fn;
    scripts_garage_init_sh --> scripts_garage_init_sh_upsert_env
    __init___py["__init__.py (py)"]
    class __init___py mod;
    controllers___init___py["__init__.py (py)"]
    class controllers___init___py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    make_sh["make.sh (sh)"]
    class make_sh mod;
    models___init___py["__init__.py (py)"]
    class models___init___py mod;
    test_sh["test.sh (sh)"]
    class test_sh mod;
    tests___init___py["__init__.py (py)"]
    class tests___init___py mod;
    utils___init___py["__init__.py (py)"]
    class utils___init___py mod;
    views___init___py["__init__.py (py)"]
    class views___init___py mod;
    ext_os["os"]
    class ext_os ext;
    app_py -.->|imports| ext_os
    ext_sys["sys"]
    class ext_sys ext;
    app_py -.->|imports| ext_sys
    ext_app_factory["app_factory"]
    class ext_app_factory ext;
    app_py -.->|imports| ext_app_factory
    ext_utils_utils["utils.utils"]
    class ext_utils_utils ext;
    app_py -.->|imports| ext_utils_utils
    ext___future__["__future__"]
    class ext___future__ ext;
    app_factory_py -.->|imports| ext___future__
    ext_json["json"]
    class ext_json ext;
    app_factory_py -.->|imports| ext_json
    ext_logging["logging"]
    class ext_logging ext;
    app_factory_py -.->|imports| ext_logging
    app_factory_py -.->|imports| ext_os
    ext_secrets["secrets"]
    class ext_secrets ext;
    app_factory_py -.->|imports| ext_secrets
    app_factory_py -.->|imports| ext_sys
    ext_datetime["datetime"]
    class ext_datetime ext;
    app_factory_py -.->|imports| ext_datetime
```

---

## Architecture Reference

### GO (3 files)

#### `client.go`
**Path:** `client.go`

**Functions:**
- `main` (line 13)

#### `enc_dec.go`
**Path:** `enc_dec.go`

**Functions:**
- `deriveAESKey` (line 20)
- `encryptFile` (line 24)
- `decryptFile` (line 45)
- `main` (line 69)

#### `server.go`
**Path:** `server.go`

**Functions:**
- `main` (line 11)
- `handleConnection` (line 40)

### JS (9 files)

#### `account.js`
**Path:** `static/js/account.js`

**Functions:**
- `setStatus` (line 19)
- `csrfToken` (line 30)
- `apiRequest` (line 36)
- `loadState` (line 54)
- `collectSlots` (line 59)
- `handleConfigure` (line 73)
- `handleOpen` (line 98)
- `handleReset` (line 120)
- `init` (line 133)

#### `coded-text.js`
**Path:** `static/js/coded-text.js`

**Functions:**
- `randomChar` (line 12)
- `animateElement` (line 18)
- `init` (line 49)

#### `login.js`
**Path:** `static/js/login.js`

**Functions:**
- `handleLogin` (line 11)
- `init` (line 43)

#### `messages.js`
**Path:** `static/js/messages.js`

**Functions:**
- `getCsrfToken` (line 11)
- `handleSend` (line 17)
- `collectEnvelopes` (line 43)
- `handleDecryptInbox` (line 60)
- `initEditor` (line 87)
- `init` (line 108)

#### `qv-crypto.js`
**Path:** `static/js/qv-crypto.js`

**Functions:**
- `concatBytes` (line 52) - *-- Encoding helpers ---*
- `hexToBytes` (line 63)
- `bytesToHex` (line 72)
- `bytesToBase64` (line 78)
- `bytesToBase32` (line 89)
- `base64ToBytes` (line 107)
- `bytesToBigInt` (line 114)
- `i2osp` (line 121)
- `mod` (line 131)
- `modPow` (line 135)
- `randomBytes` (line 153)
- `H` (line 162)
- `Hint` (line 166)
- `deriveKeyFromPassphrase` (line 178) - *-- WebCrypto symmetric primitives --- Derive a 256-bit key from a passphrase with a caller-chosen PBKDF2 iteration count. This is the single PBKDF2...*
- `deriveMasterKey` (line 199)
- `aesGcmEncrypt` (line 203)
- `aesGcmDecrypt` (line 214)
- `computeK` (line 244) - *-- SRP-6a (QV-SRP-1), mirrors utils/srp6a.py ---*
- `deriveVerifier` (line 249)
- `srpLogin` (line 257) - *Run a full SRP-6a login against the server, verifying the server proof M2.*
- `generateIdentity` (line 309) - *-- Hybrid identity and key wrapping ---*
- `parsePublicKey` (line 337)
- `parsePrivateBlob` (line 345)
- `deriveWrapKey` (line 353)
- `wrapKey` (line 365) - *Seal a file encryption key to a recipient's hybrid public key.*
- `unwrapKey` (line 389) - *Recover a file encryption key using the recipient's hybrid private blob.*
- `generateRecoveryCode` (line 411) - *-- Account recovery (QV-RECOVERY-1) ---  A high-entropy recovery code independently re-wraps the same hybrid privateBlob that the password wraps. I...*
- `normalizeRecoveryCode` (line 422) - *Normalize a user-entered recovery code: strip surrounding whitespace, remove group separators, and uppercase, so "abcd-efgh" and "ABCDEFGH"*
- `wrapPrivateKeyForRecovery` (line 430) - *Re-wrap an existing privateBlob under a key derived from a recovery code, using the same PBKDF2-SHA256 + AES-256-GCM scheme as the password path, w...*
- `derivePublicKeyFromPrivateBlob` (line 449) - *Reconstruct the public key (the same {v, mlkem, x} structure produced by generateIdentity) from a decrypted privateBlob. The noble ML-KEM-768 secre...*
- `postJson` (line 467) - *-- Network helpers ---*
- `buildRegistration` (line 490) - *-- High-level flows used by templates --- Build the zero-knowledge registration payload entirely in the browser.  Returns `{ payload, recoveryCode ...*
- `register` (line 524)
- `recoverAccount` (line 535) - *Reset SRP credentials and the password-encrypted private key using a QV-RECOVERY-1 recovery code, without ever exposing the user's keypair to the s...*
- `login` (line 586)
- `encryptAndUpload` (line 591) - *Generate a fresh file key, encrypt the file, wrap the key, and upload.*
- `downloadAndDecrypt` (line 620) - *Download an encrypted file and its key, then decrypt it in the browser.*
- `fetchPublicKey` (line 658) - *Fetch a user's hybrid public key so the browser can wrap content to them.*
- `sendSecureMessage` (line 673) - *Encrypt a message to a recipient (keeping a sender-readable outbox copy) and POST the opaque envelope. The plaintext and the CEK never leave the br...*
- `decryptInbox` (line 703) - *Decrypt a batch of inbox envelopes with the user's password. The master key and private blob are derived once and reused, so this stays cheap even ...*

#### `qv-deniable.js`
**Path:** `static/js/qv-deniable.js`

**Functions:**
- `toBytes` (line 47)
- `frame` (line 55) - *Frame a payload as [len(4) | payload | random padding] of exactly `paddedLength` bytes. `paddedLength` is shared by every slot so the*
- `unframe` (line 64)
- `sealSlot` (line 82) - *Encrypt one slot's framed plaintext under a passphrase, returning the {salt, nonce, ct} object the envelope stores.*
- `openSlot` (line 102) - *Attempt to open one slot with a passphrase. Returns the payload bytes on success or null when the passphrase does not authenticate this slot.*
- `buildDeniableVault` (line 125) - *Build a deniable container from a list of slot specifications.  `slots` is an array of `{ passphrase, data }`; `data` may be a string or a Uint8Arr...*
- `openDeniableVault` (line 170) - *Open a container with a passphrase. Tries every slot; only the slot whose passphrase matches will authenticate. Returns `{ index, data, text }` for...*

#### `recover.js`
**Path:** `static/js/recover.js`

**Functions:**
- `setStatus` (line 14)
- `handleRecover` (line 22)
- `init` (line 79)

#### `register.js`
**Path:** `static/js/register.js`

**Functions:**
- `showRecoveryCode` (line 16) - *Display the one-time QV-RECOVERY-1 code in a modal and wait for the user to acknowledge they have saved it before continuing. The code is shown*
- `handleRegister` (line 42)
- `init` (line 109)

#### `upload.js`
**Path:** `static/js/upload.js`

**Functions:**
- `getCsrfToken` (line 11)
- `getUsername` (line 16)
- `getPublicKey` (line 23)
- `handleUpload` (line 40)
- `handleDownload` (line 74)
- `init` (line 96)

### PY (55 files)

#### `__init__.py`
**Path:** `__init__.py`

*No symbols extracted*

#### `app.py`
**Path:** `app.py`

**Functions:**
- `main` (line 21)
- `_is_production_like` (line 58) - *Return True if the runtime looks like a public-facing deployment.

The heuristic is intentionally conservative: any deployment with a
non-loopback bind address is treated as production. The Werkzeug
debugger is forbidden on those binds.*

#### `app_factory.py`
**Path:** `app_factory.py`

**Functions:**
- `_is_production` (line 70) - *Return True unless the operator explicitly opts into dev mode.*
- `_build_csp` (line 81) - *Return the strict Content-Security-Policy used in production.

The policy allows:

- ``'self'`` for everything by default
- the JSDelivr CDN pinned to the specific packages the SPA needs
  (Bootstrap CSS, EasyMDE CSS/JS, marked). These are loaded with
  SRI from the templates.
- ``'unsafe-inline'`` for styles is required because EasyMDE injects
  inline styles; for scripts it is forbidden.
- WebAssembly is allowed (``'wasm-unsafe-eval'``) so the client can
  later compile liboqs-portable to WASM and avoid pure-JS PQ.

Adding a new third-party origin to this list is a security review
gate. Do not add origins without updating docs/SECURITY_TODO.md.*
- `_build_talisman_kwargs` (line 112) - *Return kwargs to pass to ``Talisman`` based on the runtime env.*
- `_configure_secret_key` (line 153) - *Set ``app.config['SECRET_KEY']`` from env, payload.json, or a random value.

The previous code set a fresh 24-byte hex on every process start.
That is correct for development (sessions reset, no surprises) but
in production the operator MUST set ``FLASK_SECRET_KEY`` (or
``SECRET_KEY``) to a stable, 32+ byte value. Otherwise every
gunicorn worker restart invalidates every session, including
CSRF tokens, and the audit log will show a flood of CSRF rejections.

For backward compatibility, ``payload.json``'s ``SECRET_KEY`` is
accepted as a third source so a project that was bootstrapped by
``make env`` keeps working without a code change. The env var
always wins over ``payload.json`` so an operator can override.*
- `_configure_session` (line 196) - *Apply session lifetime and cookie hardening.

The defaults are deliberately conservative:

- 8 hours of permanent session lifetime (then user must re-login)
- 30 minutes of idle lifetime (rolling refresh on every request)
- Cookies are HttpOnly, SameSite=Lax, and Secure in production*
- `_configure_logging` (line 213) - *Wire up a structured application logger.

The Werkzeug access log goes through Flask's default handler at
INFO. Application errors use the standard ``app.logger``. The
audit logger (``quantumvault.audit``) is configured separately in
:mod:`utils.security` and writes one-line JSON to stdout.*
- `create_app` (line 230) - *Build and return a fully-configured Flask application.

Args:
    config_overrides: Values to merge into ``app.config`` after
        defaults are applied. Useful for tests that need to swap
        the database path or disable the rate limiter.
    security_overrides: Values to merge into the Talisman kwargs.
        Used by tests to disable CSP and the HTTPS redirect without
        forking the whole factory.

Returns:
    A Flask application ready to be served by gunicorn or the
    Werkzeug dev server.*
- `load_user` (line 408)

#### `client.py`
**Path:** `client.py`

*No symbols extracted*

#### `__init__.py`
**Path:** `controllers/__init__.py`

*No symbols extracted*

#### `auth.py`
**Path:** `controllers/auth.py`

**Classs:**
- `AuthController` (line 57) - *Handles zero-knowledge registration and SRP-6a authentication.*

**Functions:**
- `_now_utc` (line 48) - *Return the current time as a timezone-aware UTC datetime.

Avoids the deprecated ``datetime.utcnow()`` which returns a naive
value and triggers a DeprecationWarning in Python 3.12+.*
- `__init__` (line 60) - *Initialize the controller.

Args:
    db_path: Path to the SQLite user database.
    mail: Configured Flask-Mail instance for transactional email.
    storage_uri: Redis URI backing the ephemeral SRP session store.*
- `register` (line 75) - *Register a user from client-generated zero-knowledge credentials.

Args:
    username: The desired unique username.
    srp_salt: SRP salt (hex) generated on the client.
    srp_verifier: SRP verifier (hex) generated on the client.
    public_key: The user's hybrid public key blob (opaque).
    encrypted_private_key: The password-encrypted private key blob (opaque).
    kdf_salt: Salt (hex) for the client-side key derivation function.
    email: The user's email address.
    phone: The user's phone number.
    first_name: The user's first name.
    last_name: The user's last name.
    recovery_salt: Optional QV-RECOVERY-1 PBKDF2 salt (hex), generated on the client.
    encrypted_private_key_recovery: Optional QV-RECOVERY-1 AES-256-GCM
        wrapping of the same private key blob, keyed by a
        client-generated recovery code instead of the password.

Returns:
    True on success, False if validation fails or persistence errors.*
- `send_confirmation_email` (line 155) - *Email the account-confirmation link to a freshly registered user.

The link targets :func:`views.auth.confirm_email`. When SMTP is not
configured, or the send fails, the link is logged at WARNING so an
operator can still verify the account from the server logs; this keeps
local and bare-VPS deployments usable before mail credentials exist.

Args:
    email: The recipient address.
    username: The account username (used for the greeting).
    token: The single-use confirmation token stored on the account.

Returns:
    True if the mail server accepted the message, False otherwise.*
- `srp_hello` (line 201) - *Begin an SRP-6a login and return the salt and server challenge B.*
- `srp_verify` (line 220) - *Complete an SRP-6a login and return the authenticated user and proof.*
- `send_sms_verification` (line 252) - *Send a verification code via SMS.*
- `verify_phone_code` (line 273) - *Verify a phone verification code for a user.

The stored value is the peppered hash; the supplied code is
hashed in the same way and the two digests are compared in
constant time.*
- `resend_phone_code` (line 309) - *Issue and send a fresh phone verification code.

Generates a new one-time code, stores its peppered hash with a
30-minute expiry (overwriting any previous pending code), and
dispatches it by SMS. Returns False when the account is unknown,
has no phone number, is already verified, or the SMS provider is
not configured, so the caller can surface an honest result.

Args:
    username: The account requesting a new code.

Returns:
    True if a new code was generated, stored, and accepted by the
    SMS provider; False otherwise.*
- `_is_code_valid` (line 348) - *Return True if a verification code has not yet expired.*
- `verify_mfa_code` (line 368) - *Verify a multi-factor authentication code for a user.*
- `send_mfa_code` (line 392) - *Generate, store, and send an MFA code to the user's phone.*
- `toggle_mfa` (line 415) - *Enable or disable MFA for a user.*

#### `contact.py`
**Path:** `controllers/contact.py`

**Classs:**
- `ContactController` (line 4) - *Handles logic related to contact messages.*

**Functions:**
- `__init__` (line 6) - *Initialize the ContactController with the database path.

Args:
    db_path (str): Path to the SQLite database file.*
- `create_contact` (line 14) - *Create a new contact message.

Args:
    user_id (int): ID of the user sending the message.
    subject (str): Subject of the message.
    message (str): Content of the message.

Returns:
    bool: True if the message was created successfully, False otherwise.*
- `get_user_contacts` (line 36) - *Retrieve all contact messages for a user.

Args:
    user_id (int): ID of the user.

Returns:
    list[ContactModel]: List of contact messages.*

#### `deniable_vault.py`
**Path:** `controllers/deniable_vault.py`

**Classs:**
- `EnvelopeValidationError` (line 104) - *Raised when an envelope violates a structural invariant.*
- `DeniableVaultConfig` (line 134) - *Immutable structural limits for a deniable vault container.*
- `EnvelopeValidator` (line 272) - *Validate the structure of an opaque deniable vault envelope.

The validator never decrypts. It checks only the shape: the schema
version, the KDF identifier and iteration count, the exact slot count,
each slot's hex and base64 fields, and the fixed ciphertext length
that makes every container identical in size.*
- `DeniableVaultController` (line 393) - *Coordinate validation, provisioning, persistence, and auditing.*

**Functions:**
- `_base64_length` (line 81) - *Return the length of the standard base64 encoding of ``byte_length`` bytes.*
- `canonical_json` (line 86) - *Serialize an envelope deterministically for storage and sizing.

Keys are sorted and separators are compact so the same logical
envelope always serializes to the same bytes. Both the size check in
:class:`EnvelopeValidator` and the persistence path in
:class:`DeniableVaultController` use this single function, so the
bytes that are measured are exactly the bytes that are stored.

Args:
    envelope: The envelope mapping to serialize.

Returns:
    The canonical JSON string.*
- `_coerce_int` (line 108) - *Return ``value`` coerced to int, falling back to ``default``.*
- `_coerce_kdf` (line 118) - *Return an allow-list of KDF identifiers from a value.

Accepts a comma-separated string (as found in environment variables)
or any iterable of strings.*
- `from_mapping` (line 148) - *Build a config from a mapping, with environment overrides.

Resolution order for every field is: environment variable, then
``mapping`` entry (e.g. ``app.config``), then the module default.
Defaults are intentionally not written to ``payload.json`` so the
repository carries no per-deployment hint that the feature exists;
an operator overrides them per-host via the environment.

Args:
    mapping: A mapping such as ``app.config``.
    env: Environment to read overrides from. Defaults to
        ``os.environ``; injectable for tests.

Returns:
    The resolved, immutable configuration.*
- `expected_ct_b64_length` (line 213) - *Return the exact base64 length every slot ciphertext must have.

A slot's ciphertext is the fixed plaintext length plus the GCM
tag, base64-encoded. Fixing it makes every container byte-for-byte
the same shape.*
- `random_container` (line 222) - *Return a well-formed container filled with random, unopenable data.

Used to provision an account that has not activated the feature and
to reset one. The result is structurally indistinguishable from an
activated container: random hex salts and nonces, and random
base64 ciphertext of exactly the expected length. No passphrase can
open it, which is the correct behavior for an unactivated vault.

Returns:
    A fresh random envelope dict.*
- `public_parameters` (line 250) - *Return the parameters the browser needs to build a container.

The browser reads these instead of hard-coding them, so a change
to the server policy propagates to clients without a code change.
The values are non-secret: they describe the container shape,
which is identical for every account.*
- `__init__` (line 281) - *Bind the validator to a configuration.*
- `validate` (line 285) - *Validate ``envelope``, raising on the first violation.

Args:
    envelope: The decoded JSON envelope to validate.

Raises:
    EnvelopeValidationError: If any structural invariant is
        violated. The message names the violated invariant and
        never echoes ciphertext.*
- `_validate_slot` (line 339) - *Validate a single slot.

Args:
    index: The slot's position, used only in error messages.
    slot: The slot mapping to validate.

Raises:
    EnvelopeValidationError: If the slot is malformed or its
        ciphertext is not the fixed expected length.*
- `_validate_hex` (line 376) - *Validate that ``value`` is hex of exactly ``expected_length``.

Raises:
    EnvelopeValidationError: If the value is not a hex string of
        the expected length.*
- `__init__` (line 401) - *Initialize the controller.

Args:
    db: The opaque container store.
    config: The structural limits in force.
    validator: The validator to use. Defaults to one bound to
        ``config``; injectable for tests.*
- `load_or_provision` (line 419) - *Return ``username``'s container, minting a random one if absent.

The mint-on-read behavior is what makes "has a container"
universal: any account that has ever opened its settings has an
indistinguishable container, so the mere existence of one is not
evidence of a hidden vault.

Args:
    username: The owning account.

Returns:
    The decoded envelope, always present.*
- `save` (line 441) - *Validate and persist a container for ``username``.

Args:
    username: The owning account.
    envelope: The decoded JSON envelope from the client.

Raises:
    EnvelopeValidationError: If the envelope is structurally
        invalid; nothing is persisted in that case.*
- `reset` (line 456) - *Overwrite ``username``'s container with a fresh random one.

Reset replaces rather than deletes: removing the row would leave a
gap that distinguishes a user who deactivated from one who never
activated. A random container keeps existence universal.

Args:
    username: The owning account.

Returns:
    The new random envelope.*
- `exists` (line 474) - *Return True if ``username`` already has a stored container.*
- `read` (line 171)

#### `file.py`
**Path:** `controllers/file.py`

**Classs:**
- `FileController` (line 49) - *Persistence for end-to-end encrypted files and their wrapped FEKs.*

**Functions:**
- `_log_s3_error` (line 26) - *Log a failed S3 operation without raising further.*
- `safe_filename` (line 31) - *Return a filename safe to embed in an S3 key.

Applies :func:`werkzeug.utils.secure_filename` to strip any path
components and control characters, then rejects any residual
shell-meta characters and NUL bytes. Returns an empty string
for empty/None input.*
- `__init__` (line 52)
- `_key` (line 57) - *Build the S3 key for a user's encrypted file or FEK.

The username is the server's truth (it came from the
authenticated session), so it does not need additional
validation. The filename is expected to have been normalized
via :func:`safe_filename` by the caller.*
- `get_storage_usage` (line 69) - *Sum the bytes used by ``username``'s encrypted files in S3.*
- `upload_encrypted_file` (line 83) - *Persist an already-encrypted file and its wrapped FEK to S3.*
- `get_encrypted_file_and_key` (line 107) - *Fetch a user's encrypted file and its wrapped FEK from S3.

Returns:
    A 3-tuple of ``(ciphertext, wrapped_fek, error)``. On success
    ``error`` is ``None``; on failure it contains a human-readable
    reason and the byte values are ``None``.*
- `list_encrypted_files` (line 137) - *List the encrypted files that belong to ``username``.*

#### `message.py`
**Path:** `controllers/message.py`

**Classs:**
- `MessageController` (line 15) - *Handles message persistence in the zero-knowledge flow.*

**Functions:**
- `__init__` (line 18) - *Initialize the controller.

Args:
    users_path: Base directory under which each user has a
        ``messages/`` subdirectory.
    users_db_path: Path to the SQLite user database, used to verify
        that a message recipient is a registered account.*
- `send_encrypted_message` (line 31) - *Persist an opaque message envelope for the recipient.

Args:
    sender: Sender's username.
    recipient: Recipient's username.
    encrypted_message_b64: AES-256-GCM ciphertext (base64) of the
        message body, with the IV prepended by the browser.
    cek_for_recipient: Hybrid-wrapped CEK to the recipient's public
        key (base64 JSON from qv-crypto).
    cek_for_sender: Hybrid-wrapped CEK to the sender's public key
        (so the outbox copy is readable).

Returns:
    True on success, False otherwise.*
- `get_messages` (line 73) - *Return opaque message envelopes for the user.

The browser unwraps each CEK with the user's private blob; the
server only returns the opaque envelopes.

Args:
    username: User whose mailbox to read.
    page: 1-indexed page number.
    per_page: Messages per page.

Returns:
    A tuple ``(messages, total_pages)`` of opaque messages.*

#### `sync.py`
**Path:** `controllers/sync.py`

**Classs:**
- `SyncController` (line 7)

**Functions:**
- `__init__` (line 8)
- `get_storage_usage` (line 14) - *Calcula el uso de almacenamiento del usuario en S3.*

#### `enc_dec.py`
**Path:** `enc_dec.py`

**Functions:**
- `derive_aes_key` (line 36) - *Derive a 32-byte AES key from an ML-KEM shared secret.

Args:
    shared_secret: The raw shared secret bytes from ``KeyEncapsulation``.

Returns:
    A 32-byte AES-256 key suitable for use with :class:`AESGCM`.*
- `encrypt_file_in_memory` (line 49) - *Encrypt ``data`` in memory with AES-256-GCM and return nonce + ciphertext.

Args:
    data: The plaintext bytes to encrypt.
    aes_key: The 32-byte AES key.

Returns:
    A tuple ``(nonce, ciphertext)`` where ``nonce`` is 12 random bytes.*
- `decrypt_file_in_memory` (line 65) - *Decrypt ``ciphertext`` in memory with AES-256-GCM and return the plaintext.

Args:
    nonce: The 12-byte nonce from the encrypt step.
    ciphertext: The encrypted bytes.
    aes_key: The 32-byte AES key.

Returns:
    The original plaintext bytes.*
- `_build_s3_client` (line 81) - *Build a boto3 S3 client honoring the zero-trust environment convention.

Args:
    region: The region name (overrides ``S3_REGION`` for this call).

Returns:
    A configured ``boto3.client('s3')`` instance.*
- `main` (line 103) - *Run the offline admin CLI (encrypt or decrypt a single object).*

#### `lol.py`
**Path:** `lol.py`

*No symbols extracted*

#### `__init__.py`
**Path:** `models/__init__.py`

*No symbols extracted*

#### `contact.py`
**Path:** `models/contact.py`

**Classs:**
- `ContactModel` (line 8) - *Pydantic model for a contact message.

Attributes:
    id: Unique contact ID.
    user_id: ID of the user who sent the message.
    subject: Subject of the contact message.
    message: Content of the contact message.
    created_at: Timestamp when the message was created.
    status: Status of the message (e.g. 'pending', 'resolved').*
- `ContactDB` (line 26) - *Database operations for contact messages.*

**Functions:**
- `__init__` (line 29) - *Initialize the ContactDB with the database path.

Args:
    db_path: Path to the SQLite database file.*
- `_init_db` (line 38) - *Initialize the contacts table with all required fields.*
- `create_contact` (line 52) - *Create a new contact message.

Args:
    user_id: ID of the user sending the message.
    subject: Subject of the message.
    message: Content of the message.

Returns:
    True on success, False if validation fails or the DB write fails.*
- `get_user_contacts` (line 89) - *Retrieve all contact messages for a user.

Args:
    user_id: ID of the user.

Returns:
    List of contact message dictionaries, newest first. On DB
    error, returns an empty list and logs the failure.*
- `_convert_row_to_dict` (line 115) - *Convert an SQLite row to a dictionary.

Args:
    row: SQLite row.

Returns:
    Contact data as a dictionary.*
- `get_all_contacts` (line 139) - *Retrieve all contact messages with pagination.

Args:
    page: 1-based page number.
    per_page: Number of contacts per page.

Returns:
    ``(rows, total_count)``. ``rows`` may be empty on DB error.*
- `_convert_row_to_dict_with_username` (line 168) - *Convert an SQLite row to a dictionary, including username.*

#### `deniable_vault.py`
**Path:** `models/deniable_vault.py`

**Classs:**
- `DeniableVaultDB` (line 30) - *Persistence for per-user opaque deniable vault containers.*

**Functions:**
- `__init__` (line 33) - *Initialize the store and ensure its table exists.

Args:
    db_path: Path to the SQLite database file, shared with
        :class:`models.user.UserDB`.*
- `_init_db` (line 43) - *Create the ``deniable_vaults`` table on first use.*
- `upsert` (line 57) - *Insert or replace the container for ``username``.

The whole container is replaced atomically: a deniable vault has
no partial state, so a replace is always a full rewrite of the
opaque envelope.

Args:
    username: The owning account's username.
    envelope: The opaque container text to store verbatim.*
- `get` (line 82) - *Return the stored container for ``username``, or ``None``.

Args:
    username: The account to look up.

Returns:
    A dict with ``username``, ``envelope``, and ``updated_at``,
    or ``None`` when the account has no container.*
- `exists` (line 101) - *Return True if ``username`` has a stored container.*

#### `message.py`
**Path:** `models/message.py`

**Classs:**
- `MessageModel` (line 27) - *Pydantic model for a stored message envelope.

Attributes:
    id (Optional[str]): Message ID.
    sender (str): Sender username.
    message (str): Display text. With ZK messages this is the opaque
        payload returned to the client (the browser decrypts it).
    timestamp (Optional[datetime]): When the message was stored.*
- `MessageDB` (line 43) - *File-based operations for end-to-end encrypted messages.*

**Functions:**
- `__init__` (line 46) - *Initialize the MessageDB with the base directory for per-user mailboxes.

Args:
    base_path (str): Filesystem path under which each user has a
        ``messages/`` subdirectory.*
- `save_message` (line 55) - *Persist an opaque message envelope for the recipient.

Args:
    recipient (str): Recipient username.
    sender (str): Sender username.
    encrypted_message_b64 (str): AES-256-GCM(CEK, plaintext) as base64
        (IV prepended by the browser).
    cek_for_recipient (str): Hybrid-wrapped CEK to the recipient's
        public key (base64-encoded JSON from qv-crypto).
    cek_for_sender (str): Hybrid-wrapped CEK to the sender's public
        key (so the outbox copy is readable).
    message_id (str): Unique message ID.*
- `get_messages` (line 87) - *Return opaque message envelopes for the recipient.

The browser unwraps the CEK with the user's private blob. This
method never derives any key material.

Args:
    recipient (str): Username whose mailbox to read.
    page (int): 1-indexed page number.
    per_page (int): Messages per page.

Returns:
    A tuple ``(messages, total_pages)`` where each message is
    opaque; the ``message`` field carries the JSON envelope
    ``{encrypted_message_b64, cek_for_recipient, cek_for_sender}``
    so the browser can decrypt it.*
- `delete_old_messages` (line 172) - *Delete messages older than ``days`` days from the recipient's mailbox.

Args:
    recipient (str): Username whose mailbox to prune.
    days (int): Age threshold in days; older messages are removed.*

#### `plans.py`
**Path:** `models/plans.py`

**Classs:**
- `PlanDB` (line 4) - *Database operations for subscription plans.*

**Functions:**
- `__init__` (line 6) - *Initialize the PlanDB with the database path.

Args:
    db_path (str): Path to the SQLite database file.*
- `_init_db` (line 15) - *Initialize the plans table with required fields.*
- `get_plan` (line 37) - *Retrieve a plan by name.

Args:
    plan_name (str): Name of the plan to search for.

Returns:
    Optional[Dict]: Plan data as a dictionary or None if not found.*
- `get_all_plans` (line 50) - *Retrieve all plans.

Returns:
    List[Dict]: List of dictionaries containing plan data.*
- `create_plan` (line 60) - *Create a new plan.

Args:
    name (str): Name of the plan.
    storage_quota (int): Storage quota in bytes.
    trial_days (int): Number of trial days.
    price (float): Price of the plan.*
- `update_plan` (line 78) - *Update an existing plan.

Args:
    name (str): Name of the plan to update.
    storage_quota (Optional[int]): New storage quota in bytes.
    trial_days (Optional[int]): New number of trial days.
    price (Optional[float]): New price of the plan.*
- `delete_plan` (line 113) - *Delete a plan by name.

Args:
    name (str): Name of the plan to delete.*
- `_convert_row_to_dict` (line 127) - *Convert an SQLite row to a dictionary.*
- `validate_plan_payment` (line 139) - *Validate that the paid amount matches the plan price.

Args:
    plan_name (str): Name of the plan.
    amount_paid (float): Amount paid.

Returns:
    bool: True if the amount matches the plan price within tolerance.*

#### `superadmin_audit.py`
**Path:** `models/superadmin_audit.py`

**Classs:**
- `SuperadminAuditDB` (line 32) - *Database operations for the superadmin audit log.*

**Functions:**
- `__init__` (line 35) - *Initialize the audit log and ensure its table exists.

Args:
    db_path: Path to the SQLite database file (shared with
        ``UserDB`` so the two are backed up together).*
- `_init_db` (line 45) - *Create the audit table on first use; no-op if it already exists.*
- `record` (line 75) - *Append one audit row and return its id.

The timestamp is generated server-side in UTC so two operators
in different timezones can correlate a single incident. The
return value is the new row's primary key, useful for tests
and for linking related log lines in the response.

Args:
    actor: Username of the superadmin performing the action.
    action: Short verb-noun identifier (e.g. ``reset_mfa``,
        ``resend_confirmation``, ``toggle_suspend``).
    target_user: Username the action was applied to, or None
        for global actions (none today, kept for future use).
    ip: Remote address that issued the request. ``None`` when
        the request did not carry one (e.g. background job).
    details: Free-text context, kept short. Use it for the
        state transition (e.g. ``active->inactive``) not for
        payloads that should never leave the audit log.

Returns:
    The new row's ``id``.*
- `recent` (line 119) - *Return the most recent ``limit`` audit rows, newest first.

Args:
    limit: Maximum rows to return. Capped at 500 to bound
        template rendering cost on a noisy superadmin.

Returns:
    List of dicts with keys ``id``, ``ts``, ``actor``,
    ``action``, ``target_user``, ``ip``, ``details``.*

#### `user.py`
**Path:** `models/user.py`

**Classs:**
- `UserModel` (line 8) - *Pydantic model for a user with Flask-Login support.

Attributes:
    id: Unique user ID.
    username: Unique username.
    role: User role (free, bronze, silver, gold, admin, superadmin).
    email: User's email address.
    phone: User's phone number.
    first_name: User's first name.
    last_name: User's last name.
    storage_quota: Storage quota in bytes.
    trial_start: Trial period start date.
    trial_end: Trial period end date.
    subscription_status: Subscription status (active, inactive).
    email_verified: Whether the email is verified.
    confirmation_token: Email confirmation token.
    phone_verified: Whether the phone number is verified.
    phone_verification_code_hash: Peppered hash of the phone verification code.
    phone_code_expires: Phone verification code expiration.
    mfa_code_hash: Peppered hash of the current MFA code.
    mfa_code_expires: MFA code expiration.
    mfa_enabled: Whether MFA is enabled for the user.*
- `UserDB` (line 83) - *Database operations for users.*

**Functions:**
- `get_id` (line 52) - *Return the user ID as a string (required by Flask-Login).

Returns:
    str: The user ID as a string, or an empty string when the
        user is anonymous.*
- `is_active` (line 70) - *Return True while the user can use the application.

Inactive (lapsed-subscription) users can still sign in to renew
or download their data, so we do NOT tie this to
``subscription_status``. The previous implementation returned
False for inactive users, which logged them out of every
@login_required route. Subscription-gated features should
check ``subscription_status`` directly in the view that needs
the gate, not via Flask-Login's activation hook.*
- `__init__` (line 85) - *Initialize the UserDB with the database path.

Args:
    db_path (str): Path to the SQLite database file.*
- `_init_db` (line 105) - *Initialize the users table with all fields for zero-knowledge auth.

The table stores only zero-knowledge credential material: the SRP salt
and verifier (the password itself is never received), the user's public
key, the password-encrypted private key blob, and the key-derivation
salt used to protect that blob. The server can decrypt none of it.

Phone verification codes and MFA codes are stored as peppered
SHA-256 digests (``*_code_hash`` columns) instead of plaintext so
a database dump does not hand an attacker ready-to-use codes.

The ``phone`` column is not unique: phone numbers are recycled by
carriers and SIM-swap attacks invalidate the uniqueness guarantee
anyway. ``email`` remains unique because it is the primary
recovery identity.

If the table was created by an older v7 schema (which carried
NOT NULL KEM blob columns the v8 controller never writes),
migrate in place: rebuild the table under the v8 shape and preserve
the surviving identity columns. The legacy password blobs are
intentionally dropped: v7 ciphertexts are useless without the
matching v7 KEM code path that has been removed.*
- `_has_phone_unique_constraint` (line 193) - *Return True if the ``users.phone`` column is UNIQUE.

SQLite does not expose UNIQUE column constraints via ``PRAGMA
table_info``; the only reliable signal is the auto-index that
SQLite materialises for any ``UNIQUE`` column (``sqlite_autoindex_users_N``).*
- `_drop_phone_unique_if_present` (line 214) - *Remove the UNIQUE constraint on ``users.phone``.

The v7 schema declared ``phone TEXT UNIQUE``. Carriers recycle
numbers, so the uniqueness guarantee is illusory; it also makes
account recovery hostile when a number changes hands.

SQLite forbids ``DROP INDEX`` on an auto-index backing a UNIQUE
column, so we have to rebuild the table. The rebuild follows
the same shape as :meth:`_migrate_from_v7` but copies every
column by position (the schema is now already v8-shaped thanks
to the prior migration step, so we know the column order).*
- `_migrate_from_v7` (line 271) - *Rebuild the users table to drop legacy v7 NOT NULL KEM columns.

SQLite cannot drop a column or relax a NOT NULL constraint in place,
so we rename the old table, create a fresh v8-shaped users table,
copy every surviving column, then drop the renamed legacy table.*
- `create_user` (line 325) - *Persist a new user from client-provided zero-knowledge credentials.

All cryptographic material (salt, verifier, public key, encrypted
private key, KDF salt) is generated on the client; this method only
stores opaque values and never derives or sees the password.
Phone and MFA codes are stored as the peppered hash supplied by
the controller; the plaintext only ever lives in the SMS that
leaves the building.

``recovery_salt`` and ``encrypted_private_key_recovery`` are the
QV-RECOVERY-1 fields: an independent PBKDF2 salt and AES-256-GCM
wrapping of the same ``privateBlob``, keyed by a client-generated
high-entropy recovery code instead of the account password. Both
are optional so older clients that do not yet generate a recovery
code can still register.*
- `update_user_phone_status` (line 362) - *Update phone verification status and related fields.

The ``phone_verification_code_hash`` parameter accepts the
peppered SHA-256 digest. Passing ``None`` clears the stored
hash (e.g. after the user verifies successfully).*
- `update_user_mfa_status` (line 396) - *Update MFA code, expiration, and enabled status.

The ``mfa_code_hash`` parameter accepts the peppered SHA-256
digest of the freshly-generated 6-digit code. ``mfa_enabled`` is
a tri-state: ``None`` leaves the value alone.*
- `update_user` (line 430) - *Update specific user fields.*
- `get_user` (line 454) - *Retrieve a user by username.

Args:
    username (str): Username to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_user_by_id` (line 468) - *Retrieve a user by ID.

Args:
    user_id (int): ID of the user to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_user_by_email` (line 482) - *Retrieve a user by email address.

Args:
    email (str): Email address to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_user_by_phone` (line 496) - *Retrieve a user by phone number.

Args:
    phone (str): Phone number to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_user_by_confirmation_token` (line 510) - *Retrieve a user by confirmation token.

Args:
    token (str): Confirmation token to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_recovery_bundle` (line 524) - *Return the QV-RECOVERY-1 bundle for a username, if one exists.

Args:
    username (str): Username to look up.

Returns:
    A dict with ``recovery_salt``, ``encrypted_private_key_recovery``,
    and ``public_key`` if the account has a recovery bundle
    configured, or ``None`` if the account does not exist or has
    not generated a recovery code (e.g. accounts created before
    QV-RECOVERY-1 was added).*
- `reset_credentials_with_recovery` (line 548) - *Replace a user's password-derived credentials after a verified recovery.

Called only after the caller has verified ``public_key_proof``
against the stored ``public_key`` (proof that the requester
possesses the recovery code, since it is the only way to recover
the matching ``privateBlob`` and re-derive the public key). The
``public_key`` and the underlying keypair are unchanged; only the
SRP verifier and the password-wrapping of the existing private key
blob are replaced.

Args:
    username (str): Username whose credentials are being reset.
    srp_salt (str): New SRP salt, hex-encoded.
    srp_verifier (str): New SRP verifier, hex-encoded.
    kdf_salt (str): New PBKDF2 salt for the password-wrapped private key, hex-encoded.
    encrypted_private_key (str): The same private key blob, re-wrapped under the new password.*
- `update_role` (line 579) - *Update a user's role, storage quota, and subscription status.

Args:
    username (str): Username of the user to update.
    role (str): New role for the user.
    storage_quota (int): New storage quota in bytes (default: 10MB).
    subscription_status (str): New subscription status (default: 'active').*
- `count_users` (line 592) - *Return the total number of users.

Implemented as ``SELECT COUNT(*)`` rather than ``len(get_all_users())``
so the home page does not materialise the entire table on every
request.*
- `get_all_users` (line 603) - *Retrieve all users.

Returns:
    list[dict]: List of dictionaries containing user data.*
- `_parse_datetime` (line 615) - *Parse a stored timestamp into a datetime, tolerating the format.

Args:
    value: A datetime, an ISO-like timestamp string, or None.

Returns:
    The parsed datetime, or None when the value is empty or unparseable.*
- `_convert_row_to_dict` (line 638) - *Convert a name-keyed SQLite row into a plain dictionary.

Reads access columns by name (the connection uses ``sqlite3.Row``), so
the mapping is robust to column ordering and additive migrations.

Args:
    row: A ``sqlite3.Row`` produced by a read query, or None.

Returns:
    A dictionary of user fields, or None when the row is empty.*
- `fetch_one` (line 694) - *Execute a query and return the first result as a dictionary.

Args:
    query (str): SQL query to execute.
    params (tuple): Parameters for the query (default: empty tuple).

Returns:
    Optional[dict]: First row as a dictionary or None if no results or an error occurs.*
- `value` (line 655)

#### `pq_decrypt_password.py`
**Path:** `pq_decrypt_password.py`

*No symbols extracted*

#### `doctor.py`
**Path:** `scripts/doctor.py`

*No symbols extracted*

#### `email_tool.py`
**Path:** `scripts/email_tool.py`

**Functions:**
- `_build_mail_app` (line 40) - *Build a minimal Flask app that only carries the mail configuration.

Intentionally avoids the full application factory (object storage, Redis,
security headers) so this tool runs on a bare host with nothing but SMTP
reachable.*
- `cmd_test_smtp` (line 63) - *Send a test email through the configured SMTP server.*
- `cmd_link` (line 91) - *Print the confirmation URL for a user without sending email.*
- `cmd_confirm` (line 114) - *Mark a user's email as verified directly in the database.*
- `build_parser` (line 133) - *Construct the argument parser for the three subcommands.*
- `main` (line 153) - *Parse arguments and dispatch to the selected subcommand.*

#### `makeadmin.py`
**Path:** `scripts/makeadmin.py`

**Functions:**
- `_resolve_db_path` (line 51) - *Return the absolute users.db path, anchored at the project root.

A bare ``instance/users.db`` only resolves when the script is run
from the project root. Anchoring at ``_PROJECT_ROOT`` lets an operator
invoke it from anywhere (cron, CI, a different cwd) without surprises.*
- `_print_user_summary` (line 64) - *Print the post-update user record so the operator can eyeball it.*
- `cmd_promote` (line 75) - *Promote ``args.username`` to the requested role (default: superadmin).*
- `build_parser` (line 126) - *Construct the argument parser for the makeadmin subcommands.*
- `main` (line 152) - *Parse arguments and dispatch to the selected subcommand.*

#### `test_bloque1.py`
**Path:** `scripts/test_bloque1.py`

**Classs:**
- `_FakeUser` (line 48)

**Functions:**
- `_load_user` (line 62)
- `check` (line 86)
- `__init__` (line 49)
- `is_authenticated` (line 54)
- `is_active` (line 56)
- `is_anonymous` (line 58)
- `get_id` (line 59)

#### `server.py`
**Path:** `server.py`

*No symbols extracted*

#### `terms.py`
**Path:** `templates/terms.py`

**Functions:**
- `terms` (line 6) - *Render the About page.*

#### `__init__.py`
**Path:** `tests/__init__.py`

*No symbols extracted*

#### `conftest.py`
**Path:** `tests/conftest.py`

**Classs:**
- `_ListLogHandler` (line 82) - *Collect emitted log messages in a list for assertions.*

**Functions:**
- `_push_request_context` (line 34) - *Neutralize pytest-flask's autouse request-context push.

pytest-flask installs an autouse ``_push_request_context`` fixture that
keeps an application/request context pushed for the whole test. That
ambient context makes Flask-Login's ``current_user`` proxy and
``client.session_transaction`` resolve against a stale context, so a
test that authenticates a second user on the same client still observes
the first user's data. This suite drives the app exclusively through the
``client`` fixture, which manages its own per-request context, so the
ambient push is both unnecessary and a correctness hazard. Overriding
the plugin fixture by name (conftest takes precedence over installed
plugins) replaces it with a no-op.*
- `app` (line 52) - *Return a QuantumVault Flask app configured for testing.*
- `client` (line 77) - *Return a Flask test client for the test app.*
- `audit_records` (line 94) - *Yield a list that is appended with each ``audit_event`` JSON line.

The audit logger has ``propagate = False`` (by design, so it never
mixes into the application log), so ``caplog`` cannot see it. This
fixture attaches a temporary handler directly to the audit logger
instead.*
- `__init__` (line 85)
- `emit` (line 89)

#### `test_auth_phone.py`
**Path:** `tests/test_auth_phone.py`

**Functions:**
- `test_verify_phone_page_renders` (line 18) - *GET /verify_phone must render without a url_for BuildError.*
- `test_resend_endpoint_is_registered` (line 25) - *The resend endpoint the template links to must exist.*
- `test_resend_route_accepts_only_post` (line 31) - *The resend endpoint is POST-only so a GET cannot trigger an SMS.*

#### `test_deniable_vault.py`
**Path:** `tests/test_deniable_vault.py`

**Classs:**
- `TestDeniableVaultConfig` (line 140)
- `TestEnvelopeValidator` (line 185)
- `TestRandomContainer` (line 272)
- `TestDeniableVaultDB` (line 293)
- `TestDeniableVaultController` (line 325)
- `TestDeniableVaultApi` (line 390)

**Functions:**
- `config` (line 50) - *Return the default deniable-vault configuration.*
- `validator` (line 56) - *Return a validator bound to the default configuration.*
- `_ciphertext` (line 61) - *Return a base64 ciphertext string of the given (or expected) length.*
- `_valid_envelope` (line 71) - *Build a structurally valid envelope for ``config``.

Every slot carries a ciphertext of the fixed expected length so the
fixed-size invariant holds. The contents are zero bytes; the validator
never inspects plaintext, only structure.*
- `_make_user` (line 91) - *Create a minimal user row in the test database and return it.*
- `_login` (line 120) - *Create and authenticate a user on ``client``'s session.*
- `_csrf` (line 130) - *Fetch a CSRF token bound to the client's session.*
- `test_defaults_are_self_consistent` (line 141)
- `test_expected_ct_length_matches_base64_formula` (line 150)
- `test_mapping_overrides_defaults` (line 154)
- `test_environment_overrides_mapping` (line 161)
- `test_allowed_kdf_csv_is_parsed` (line 166)
- `test_public_parameters_round_trip_to_json` (line 172)
- `test_accepts_a_well_formed_envelope` (line 186)
- `test_rejects_non_dict` (line 189)
- `test_rejects_wrong_schema_version` (line 194)
- `test_rejects_unknown_kdf` (line 200)
- `test_rejects_iterations_below_minimum` (line 206)
- `test_rejects_iterations_above_maximum` (line 212)
- `test_rejects_wrong_slot_count` (line 218)
- `test_rejects_bad_salt_length` (line 224)
- `test_rejects_non_hex_salt` (line 230)
- `test_rejects_bad_nonce_length` (line 236)
- `test_rejects_ciphertext_of_wrong_length` (line 242)
- `test_rejects_unequal_slot_ciphertext_lengths` (line 248)
- `test_rejects_invalid_base64_ciphertext` (line 254)
- `test_rejects_missing_slot_keys` (line 260)
- `test_random_container_passes_validation` (line 273)
- `test_random_containers_differ` (line 276)
- `test_random_container_has_fixed_shape` (line 281)
- `test_upsert_then_get_round_trips_verbatim` (line 294)
- `test_upsert_replaces_existing_row` (line 303)
- `test_get_missing_returns_none` (line 309)
- `test_exists` (line 313)
- `_controller` (line 326)
- `test_load_or_provision_mints_when_absent` (line 331)
- `test_load_or_provision_is_stable` (line 339)
- `test_save_then_load_round_trips` (line 346)
- `test_save_rejects_invalid_envelope` (line 354)
- `test_reset_replaces_with_a_valid_random_container` (line 363)
- `test_audit_is_generic_and_never_contains_ciphertext` (line 373)
- `test_settings_page_requires_authentication` (line 391)
- `test_get_api_requires_authentication` (line 395)
- `test_settings_page_renders_for_authenticated_user` (line 399)
- `test_get_always_returns_an_envelope_and_parameters` (line 406)
- `test_put_without_csrf_is_rejected` (line 414)
- `test_put_get_reset_round_trip` (line 422)
- `test_put_rejects_malformed_envelope` (line 447)
- `test_vault_is_scoped_to_the_authenticated_user` (line 461)

#### `test_security.py`
**Path:** `tests/test_security.py`

**Functions:**
- `test_audit_event_includes_ip_and_ua_by_default` (line 12)
- `test_audit_event_redacts_ip_and_ua_when_disabled` (line 29)
- `test_json_csrf_protect_rejects_missing_token` (line 45)
- `test_json_csrf_protect_accepts_valid_header_token` (line 57)
- `test_json_csrf_protect_passes_get_through_without_token` (line 77)
- `view` (line 47)
- `view` (line 59)
- `view` (line 79)

#### `test_srp.py`
**Path:** `tests/test_srp.py`

**Functions:**
- `_h` (line 16)
- `_hint` (line 23)
- `_client_derive_verifier` (line 27) - *Mirror ``deriveVerifier`` in qv-crypto.js: v = g^x mod N.*
- `_client_compute_proof` (line 34) - *Mirror ``srpLogin`` in qv-crypto.js: derive M1 and the expected M2.*
- `test_srp6a_full_roundtrip_matches_server_proofs` (line 74)
- `test_srp6a_wrong_password_produces_mismatched_proof` (line 104)

#### `__init__.py`
**Path:** `utils/__init__.py`

*No symbols extracted*

#### `cache.py`
**Path:** `utils/cache.py`

**Classs:**
- `Cache` (line 6) - *Redis-based caching layer.*

**Functions:**
- `__init__` (line 8)
- `get` (line 11) - *Retrieve a value from the cache.*
- `set` (line 16) - *Store a value in the cache with an optional TTL (seconds).*
- `delete` (line 20) - *Delete a key from the cache.*

#### `mailer.py`
**Path:** `utils/mailer.py`

**Functions:**
- `external_url` (line 22) - *Build an absolute URL for a root-relative path using the public host.

Args:
    path: A path such as ``/confirm/<token>``. A leading slash is added
        if missing.

Returns:
    The absolute URL, for example ``https://www.quantumvault.pro/confirm/x``.*
- `mail_is_configured` (line 38) - *Return True when SMTP credentials are present so a send can succeed.

A send is only attempted when both a username and password are set,
which lets callers fall back to logging a link in local or bare-VPS
deployments that have no mail account yet.*
- `send_transactional_email` (line 51) - *Send a plain-text transactional email through the configured server.

This never raises: a failure is logged and reported through the boolean
return so callers (registration, scheduler) degrade gracefully instead of
aborting the surrounding operation.

Args:
    subject: The email subject line.
    recipients: One or more destination addresses.
    body: The plain-text message body.

Returns:
    True if Flask-Mail accepted the message, False otherwise.*

#### `plans.py`
**Path:** `utils/plans.py`

**Classs:**
- `SubscriptionPlans` (line 3) - *Define los planes de suscripción disponibles.*

**Functions:**
- `get_plan` (line 30) - *Obtiene los detalles de un plan.

Args:
    plan_name (str): Nombre del plan.

Returns:
    Dict: Detalles del plan.*
- `validate_plan_payment` (line 42) - *Valida que el monto pagado coincide con el plan.*

#### `scheduler.py`
**Path:** `utils/scheduler.py`

**Functions:**
- `_now_utc` (line 32) - *Timezone-aware UTC ``now`` (avoids the deprecated ``datetime.utcnow()``).*
- `init_scheduler` (line 37) - *Start the background scheduler with the production job schedule.

The jobs run in a daemon thread, so they do not block the Flask
request loop. They are added idempotently: re-importing the module
does not register duplicates because :class:`BackgroundScheduler`
is local to this call.*
- `_is_trial_elapsed` (line 54) - *Return True if the user is on a free plan and the trial has ended.*
- `check_trial_expiration` (line 72)
- `cleanup_old_messages` (line 118)

#### `security.py`
**Path:** `utils/security.py`

**Functions:**
- `_get_audit_logger` (line 46) - *Return the process-wide audit logger, configured on first use.

The audit logger writes single-line JSON records to stdout. Every
security-relevant event (login success/failure, registration, MFA,
contact message, role change, account lockout, CSRF rejection) must
call :func:`audit_event` so that incident response has a single
stream to correlate against.*
- `_correlation_id` (line 72) - *Return the per-request correlation id, generating one if missing.

The id is stored on Flask's ``g`` so a single request emits multiple
audit events that share the same key, which is what an operator needs
when reconstructing a session.*
- `audit_event` (line 86) - *Emit a structured audit record.

Args:
    event: A short, snake_case event name, e.g. ``login_success`` or
        ``mfa_failure``.
    **fields: Additional structured fields to record. The keys
        ``ts`` (unix epoch in milliseconds), ``event``, ``cid``
        (correlation id), ``ip``, and ``ua`` are added automatically.

The ``ip`` and ``ua`` fields are recorded as ``None`` when
``QV_AUDIT_LOG_IP=0`` or ``QV_AUDIT_LOG_UA=0`` respectively, for
operators running for high-risk users (e.g. behind Tor) who do not
want client IP addresses or User-Agent strings persisted to logs.
Both default to enabled (``"1"``).*
- `constant_time_compare` (line 123) - *Return True if the two strings match in constant time.

A regular ``==`` leaks length and content-prefix information via
short-circuit evaluation. This wraps :func:`hmac.compare_digest`
which compares the whole input even when lengths differ.*
- `hash_secret` (line 135) - *Hash a short-lived secret (phone code, MFA, recovery code) for storage.

Uses SHA-256 with a server-side pepper. The pepper is read from the
``QV_SECRET_PEPPER`` environment variable and falls back to a value
derived from ``SECRET_KEY`` so the hash is non-deterministic across
reinstalls but stable for a given deployment.

The goal is to avoid storing plaintext codes in the database: a DB
dump no longer hands an attacker ready-to-use codes. Phone codes
are 6 digits and MFA codes are 6 digits, so a peppered SHA-256 is
more than sufficient: an attacker with the DB but without the
pepper must precompute a 10^6-entry rainbow table per deployment.*
- `verify_secret` (line 156) - *Verify a short-lived secret against its stored hash.*
- `new_one_time_code` (line 163) - *Return a cryptographically random numeric verification code.*
- `_extract_csrf_token` (line 172) - *Return the CSRF token from the request header or body.

Mirrors Flask-WTF's own lookup order so a client that sets either
``X-CSRFToken`` or ``X-CSRF-Token`` (the two spellings Flask-WTF accepts
in ``WTF_CSRF_HEADERS``), or a ``csrf_token`` form/JSON field, is handled
uniformly. The browser crypto in ``static/js/qv-crypto.js`` sends the
``X-CSRFToken`` header.*
- `json_csrf_protect` (line 193) - *Decorator: require a valid CSRF token on JSON state-changing requests.

The token is the one Flask-WTF issues through ``form.hidden_tag()`` or
``/api/csrf-token``. It is a *signed* value, so it is validated with
:func:`flask_wtf.csrf.validate_csrf`, which unsigns it and compares it to
the raw token held in the session; a direct string comparison against the
session value never matches and must not be used. A missing or invalid
token is rejected with HTTP 403 and recorded in the audit log.

GET, HEAD and OPTIONS pass through unchanged because they are not
state-changing. Use this on every ``/api/`` route that mutates state.*
- `wrapper` (line 207)

#### `srp6a.py`
**Path:** `utils/srp6a.py`

**Classs:**
- `SRPSessionStore` (line 150) - *Redis-backed store for the ephemeral state of an in-flight SRP login.

Each ``hello`` step persists the values needed to verify the subsequent
``verify`` step. Entries expire after :data:`SESSION_TTL_SECONDS` so an
abandoned handshake cannot be resumed later.*

**Functions:**
- `i2osp` (line 47) - *Encode an integer as a big-endian byte string padded to the length of N.

Args:
    value: Non-negative integer to encode (a group element).

Returns:
    The big-endian representation left-padded with zero bytes to
    ``N_BYTE_LENGTH``.*
- `_hash` (line 60) - *Return the SHA-256 digest of the concatenated byte chunks.*
- `_hash_int` (line 68) - *Return the SHA-256 digest of the concatenated chunks as an integer.*
- `compute_k` (line 73) - *Compute the SRP-6a multiplier parameter ``k = H(N | PAD(g))``.*
- `compute_u` (line 78) - *Compute the random scrambling parameter ``u = H(PAD(A) | PAD(B))``.

Args:
    server_a: The client public ephemeral value A.
    server_b: The server public ephemeral value B.

Returns:
    The scrambling parameter u as an integer.*
- `generate_server_challenge` (line 91) - *Generate the server ephemeral key pair (b, B) for a login challenge.

Args:
    verifier: The stored password verifier ``v`` for the user.

Returns:
    A tuple ``(b, B)`` where ``b`` is the secret ephemeral and
    ``B = (k * v + g**b) mod N`` is the public value sent to the client.*
- `compute_proofs` (line 107) - *Compute the expected client proof M1 and the server proof M2.

Args:
    username: The user identity I.
    salt_hex: The user salt as a hex string.
    verifier: The stored password verifier v.
    server_a: The client public ephemeral A.
    server_b: The server public ephemeral B.
    server_b_secret: The server secret ephemeral b.

Returns:
    A tuple ``(expected_m1, m2)`` of raw digest bytes.*
- `hello` (line 224) - *Process the SRP ``hello`` step and return the server challenge B.

Args:
    store: The ephemeral session store.
    username: The user identity.
    client_a_hex: The client public ephemeral A as a hex string.
    salt_hex: The stored user salt as a hex string.
    verifier_hex: The stored verifier as a hex string.

Returns:
    The server public ephemeral B as a hex string, or ``None`` if the
    client value A is invalid (``A mod N == 0``).*
- `verify` (line 260) - *Process the SRP ``verify`` step and return the server proof M2.

Args:
    store: The ephemeral session store.
    username: The user identity.
    client_m1_hex: The client proof M1 as a hex string.

Returns:
    The server proof M2 as a hex string on success, or ``None`` if no
    pending session exists or the client proof is invalid.*
- `__init__` (line 158) - *Initialize the store from a Redis connection URI.

Args:
    storage_uri: A ``redis://`` connection string (the same one used by
        the rate limiter).*
- `_key` (line 168) - *Return the Redis key for a username's pending SRP session.*
- `save` (line 172) - *Persist the ephemeral SRP challenge state for a username.

Args:
    username: The user identity.
    salt_hex: The user salt as a hex string.
    verifier_hex: The stored verifier as a hex string.
    server_a_hex: The client public ephemeral A as a hex string.
    server_b_hex: The server public ephemeral B as a hex string.
    server_b_secret_hex: The server secret ephemeral b as a hex string.*
- `load` (line 202) - *Load and consume the ephemeral SRP state for a username.

The entry is deleted on read so each challenge is single-use.

Args:
    username: The user identity.

Returns:
    The stored session dictionary, or ``None`` if no valid session
    exists (expired, missing, or already consumed).*

#### `utils.py`
**Path:** `utils/utils.py`

**Classs:**
- `Payload` (line 62) - *Non-secret application configuration loaded from ``payload.json``.*
- `Config` (line 85) - *Application configuration sourced from ``payload.json`` and the environment.

Non-secret defaults come from ``payload.json``; secrets and infrastructure
endpoints (mail credentials, object storage, Redis) are overlaid from
environment variables so that no credential is committed to the repository.

Every attribute is declared on the class so static analyzers see the
full shape; :meth:`__init__` populates them from the loaded payload.*

**Functions:**
- `as_bool` (line 11) - *Coerce an environment or payload value into a real boolean.

Strings such as ``"True"`` and ``"False"`` are both truthy when passed
straight to Flask, which silently enables flags that were meant to be
disabled. This normalizes them so ``MAIL_USE_TLS="False"`` disables TLS.

Args:
    value: The raw value from ``os.environ`` or ``payload.json``.
    default: The value to return when ``value`` is ``None``.

Returns:
    The coerced boolean.*
- `sanitize_path` (line 31) - *Sanitiza una ruta de archivo para prevenir LFI y path traversal.
- Elimina caracteres peligrosos
- Normaliza la ruta
- Asegura que no contenga '..' o rutas absolutas*
- `load_payload` (line 150) - *Load non-secret application configuration from ``payload.json``.

A local ``.env`` file is loaded first (when ``python-dotenv`` is available)
so environment-based secrets are populated before :class:`Config` reads them.

Returns:
    The parsed configuration dictionary.*
- `__init__` (line 127)
- `__getitem__` (line 147)

#### `__init__.py`
**Path:** `views/__init__.py`

*No symbols extracted*

#### `about.py`
**Path:** `views/about.py`

**Functions:**
- `about` (line 6) - *Render the About page.*

#### `account.py`
**Path:** `views/account.py`

**Functions:**
- `get_deniable_vault_controller` (line 50) - *Build a controller bound to the active app's database and config.

The database path and structural parameters are read from
``current_app.config`` so tests (which point the app at a temporary
database and may override limits) and production share one code path.*
- `settings` (line 64) - *Render the account settings page.*
- `get_vault` (line 77) - *Return the user's container and the build parameters.

The response always includes an ``envelope`` (a random one is minted on
first access) and the structural ``parameters``. It never includes a
"configured" flag: whether the container holds real data is exactly
what must stay hidden.*
- `put_vault` (line 99) - *Validate and store a container for the user.*
- `delete_vault` (line 122) - *Reset the user's container to a fresh random one.

Reset, not delete: removing the row would distinguish an account that
deactivated from one that never activated. A random container keeps the
"every account has one" invariant intact.*

#### `admin.py`
**Path:** `views/admin.py`

**Classs:**
- `UserEditForm` (line 23) - *Form for editing user details.

Intentionally does NOT carry these fields:

* ``confirmation_token`` — rotated by the resend-confirmation
  endpoint, never hand-edited. A static token cannot expire and
  would either lock the user out or be reused forever.
* ``phone_verification_code`` — same reason; the column stores
  a hash, not the cleartext code, so a superadmin UI input is
  meaningless.
* KEM/SRP blob columns (srp_salt, srp_verifier, public_key,
  encrypted_private_key, kdf_salt) — the server has no UI to
  rewrite them. Modifying any of them would silently brick the
  user's login.

``password`` is also absent: the server is zero-knowledge, so a
"change password" UI lives in the user's own profile, not here.*
- `PlanForm` (line 56) - *Form for creating or editing a subscription plan.*

**Functions:**
- `admin` (line 68) - *Plan catalog read view.

Plan CRUD lives at ``/admin<token>/plans`` and
``/admin<token>/plans/edit/<name>`` so a single page is not also
a destructive form. This view is now strictly a list of
available plans, with a per-row edit link.

User identity (list, edit, suspend, MFA reset, confirmation
rotation) is the superadmin panel's job and lives at
``/superadmin<token>``.*
- `superadmin_edit_user` (line 90) - *Full profile edit for a single user.

Lives under ``/superadmin<token>`` because every field here touches
identity directly (role, verifications, quota, subscription). Admin
role no longer has access: the superadmin panel is the only place
that can rewrite those columns.

Fields intentionally NOT editable through this form:

* ``confirmation_token`` — rotated by the resend-confirmation
  endpoint, never hand-edited (a static token cannot expire).
* ``phone_verification_code`` — same reason, lives in a hashed
  column anyway so even a superadmin should not see it.
* KEM/SRP blob columns (srp_salt, srp_verifier, public_key,
  encrypted_private_key, kdf_salt) — modifying any of these would
  silently brick the user's login. The server has no UI to rewrite
  them and never should.*
- `manage_plans` (line 195) - *Handle plan management.*
- `edit_plan` (line 219) - *Handle editing of plan details.*
- `superadmin` (line 255) - *Superadmin identity-recovery and inventory panel.

Read-only by design. The server is zero-knowledge, so it can never
decrypt user content; instead this view surfaces the actions a
superadmin actually has to perform during incident response:

* inventory of encrypted file names per user (metadata only)
* last 50 audit log entries (who did what to which account)
* the user table with per-row privileged action buttons

Mutating actions live in the three POST handlers below. The GET
handler must never accept a side-effect query string, otherwise an
attacker could trigger a reset by luring a superadmin to follow a
crafted link.*
- `superadmin_reset_mfa` (line 342) - *Disable MFA and clear the pending code for ``username``.

Used when a user loses their authenticator device. We do NOT
touch the password, the email, or the KEM material — losing a
second factor should not invalidate the rest of the identity.*
- `superadmin_resend_confirmation` (line 390) - *Issue a fresh ``confirmation_token`` for ``username``.

The token's 24h expiry is recomputed by ``update_user`` (see
models/user.py:337). If the user already verified, we still issue
a new token so the link can be reused as a magic-link login path
— useful when a user has lost access to their primary device.*
- `superadmin_toggle_suspend` (line 438) - *Flip ``subscription_status`` between active and inactive.

Suspension is a billing/operational lever (refuse new uploads,
block new devices) that does not require touching the KEM
material. Reactivation brings the user back into the same
position they were in before suspension.*
- `admin_contacts` (line 489)

#### `auth.py`
**Path:** `views/auth.py`

**Classs:**
- `PhoneVerificationForm` (line 97)
- `MFAForm` (line 102)
- `ContactForm` (line 107)
- `RegisterForm` (line 113)
- `LoginForm` (line 123)

**Functions:**
- `role_required` (line 70) - *Restrict a route to authenticated users holding one of the given roles.

The check is an intersection of ``VALID_ROLES`` and the caller-
supplied roles so a typo in a future route (e.g. ``role_required("user")``)
cannot accidentally grant access because the role never existed.*
- `get_auth_controller` (line 131)
- `show_register` (line 142)
- `handle_register` (line 149)
- `login` (line 233)
- `recover` (line 241) - *Render the QV-RECOVERY-1 account-recovery page.

Available to anonymous visitors: a forgotten password means the
visitor cannot authenticate, by definition.*
- `_srp_key` (line 254)
- `_recovery_key` (line 265)
- `srp_hello` (line 277) - *First SRP-6a step: receive the client public value A, return salt and B.*
- `srp_verify` (line 298) - *Second SRP-6a step: verify the client proof M1 and return server proof M2.*
- `logout` (line 336)
- `confirm_email` (line 343)
- `verify_phone` (line 366)
- `resend_phone_verification` (line 383) - *Re-send the phone verification code for an account.

The username is supplied as a query parameter by the verify-phone
template's resend form. The form carries the CSRF token, so the
app-wide CSRFProtect guard applies. The handler never reveals whether
the account exists: it always redirects back with a neutral message.*
- `verify_mfa` (line 406)
- `toggle_mfa` (line 428)
- `contact` (line 453) - *Render the contact form and persist a message from the current user.

The page is only meaningful for authenticated users: messages are tied to
a ``user_id`` foreign key in ``contacts``. Anonymous visitors are sent
to the login page so they can sign in (or register) before contacting.*
- `get_public_key` (line 484) - *Return a user's hybrid public key so the browser can wrap data to them.*
- `get_user_keys` (line 502) - *Provide the keys a user needs to decrypt their data client-side.

The caller must already be authenticated and asking for their own
material; the route refuses to return anyone else's keying data.*
- `get_recovery_bundle` (line 533) - *Return the QV-RECOVERY-1 bundle for a username, if one was generated.

No authentication is required: a forgotten password by definition
means the caller cannot log in. The returned values are opaque to
anyone without the recovery code: ``encrypted_private_key_recovery``
is AES-256-GCM ciphertext keyed by a PBKDF2 derivation of the
recovery code, so exposing it to an unauthenticated caller does not
weaken the zero-knowledge guarantees.*
- `reset_with_recovery` (line 558) - *Reset SRP credentials and the password-wrapped private key via QV-RECOVERY-1.

The browser has already decrypted ``encrypted_private_key_recovery``
using a key derived from the recovery code and reconstructed the
account's public key from the recovered private key blob (see
``derivePublicKeyFromPrivateBlob`` in ``static/js/qv-crypto.js``).
That reconstruction is supplied as ``public_key_proof``: AES-GCM
authentication means a wrong recovery code fails to decrypt at all,
so only a caller who supplied the correct code can produce a
``public_key_proof`` that matches the stored ``public_key``
byte-for-byte. The underlying keypair and ``public_key`` are not
changed; only the SRP verifier and the password-wrapping of the
existing private key blob are replaced.*
- `get_csrf_token` (line 618) - *Issue the CSRF token used by the SPA for state-changing JSON calls.*
- `decorator` (line 84)
- `decorated_function` (line 86)

#### `faq.py`
**Path:** `views/faq.py`

**Functions:**
- `faq` (line 6) - *Render the About page.*
- `landing` (line 11) - *Render the About page.*

#### `file.py`
**Path:** `views/file.py`

**Classs:**
- `UploadForm` (line 15) - *Formulario para la subida de archivos cifrados.*

**Functions:**
- `upload` (line 25) - *Maneja la subida de archivos cifrados desde el cliente.*
- `download` (line 56) - *Provide the encrypted file and its key for client-side decryption.

The filename comes from the URL and is used to look up a key under
the authenticated user's S3 prefix. The server never lets the
filename escape that prefix: any ``/``, ``\``, ``..`` or control
character is rejected before the S3 key is constructed, so a
crafted ``filename`` like ``../admin/files/x`` cannot exfiltrate
another user's ciphertext.*

#### `message.py`
**Path:** `views/message.py`

**Classs:**
- `MessageForm` (line 19) - *Form for sending messages.*

**Functions:**
- `messages` (line 29) - *Render the messages page; the browser handles all crypto.

Sending happens via the JSON API in /api/secure_message below.*
- `api_secure_message` (line 49) - *Accept an opaque end-to-end encrypted message envelope.

The browser already generated the CEK, encrypted the message body with
AES-256-GCM, and wrapped the CEK to the recipient's and sender's
hybrid public keys. The server stores only the opaque material.*

#### `privacy.py`
**Path:** `views/privacy.py`

**Functions:**
- `privacy` (line 6) - *Render the About page.*

#### `subscription.py`
**Path:** `views/subscription.py`

**Classs:**
- `SubscriptionForm` (line 24) - *Formulario para seleccionar un plan de suscripción.*

**Functions:**
- `subscribe` (line 37) - *Maneja la selección de planes y el proceso de pago.*
- `payment_success` (line 86) - *Maneja el éxito del pago y actualiza el plan del usuario.*
- `__init__` (line 26)

#### `sync.py`
**Path:** `views/sync.py`

**Functions:**
- `secure_sync` (line 29) - *Receive an already-encrypted file + wrapped FEK and persist them.

The server never sees the plaintext: the file body and the
wrapped key are opaque from the server's perspective. We only
enforce quota and basic input validation.*
- `sync_page` (line 79)

#### `terms.py`
**Path:** `views/terms.py`

**Functions:**
- `terms` (line 6) - *Render the About page.*

#### `views.py`
**Path:** `views/views.py`

**Classs:**
- `MFAEnableForm` (line 14)

**Functions:**
- `home` (line 20) - *Render the landing/home page.

The total user count is fetched with ``SELECT COUNT(*)`` directly
rather than loading every row into memory, so the cost is O(1)
regardless of the user table size.*

#### `wsgi.py`
**Path:** `wsgi.py`

*No symbols extracted*

### SH (5 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*

#### `make.sh`
**Path:** `make.sh`

*No symbols extracted*

#### `garage-init.sh`
**Path:** `scripts/garage-init.sh`

**Functions:**
- `upsert_env` (line 35) - *Insert or update a KEY=value line in .env without disturbing other lines.*

#### `garage-native.sh`
**Path:** `scripts/garage-native.sh`

**Functions:**
- `upsert_env` (line 46) - *Insert or update a KEY=value line in .env without disturbing other lines.*
- `s3_reachable` (line 56)
- `gcmd` (line 141)

#### `test.sh`
**Path:** `test.sh`

*No symbols extracted*
