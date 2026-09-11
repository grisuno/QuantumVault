# Subsystem: tests

## tests/__init__.py
- Layer: testing
- Language: py

## tests/conftest.py
- Layer: testing
- Language: py
- Symbols:
  - `_push_request_context` (function, line 34) `def _push_request_context()`
  - `app` (function, line 52) `def app(tmp_path)`
  - `client` (function, line 77) `def client(app)`
  - `_ListLogHandler` (class, line 82) `class _ListLogHandler(Handler)`
  - `audit_records` (method, line 94) `def audit_records()`
  - `__init__` (method, line 85) `def __init__(self)`
  - `emit` (method, line 89) `def emit(self, record)`
- Depends on: `app_factory.py`, `utils/security.py`

## tests/test_auth_phone.py
- Layer: testing
- Language: py
- Symbols:
  - `test_verify_phone_page_renders` (function, line 18) `def test_verify_phone_page_renders(client)`
  - `test_resend_endpoint_is_registered` (function, line 25) `def test_resend_endpoint_is_registered(app)`
  - `test_resend_route_accepts_only_post` (function, line 31) `def test_resend_route_accepts_only_post(app)`

## tests/test_deniable_vault.py
- Layer: testing
- Language: py
- Symbols:
  - `config` (function, line 50) `def config()`
  - `validator` (function, line 56) `def validator(config)`
  - `_ciphertext` (function, line 61) `def _ciphertext(config, length)`
  - `_valid_envelope` (function, line 71) `def _valid_envelope(config)`
  - `_make_user` (function, line 91) `def _make_user(app, username, role)`
  - `_login` (function, line 120) `def _login(client, app, username, role)`
  - `_csrf` (function, line 130) `def _csrf(client)`
  - `TestDeniableVaultConfig` (class, line 140) `class TestDeniableVaultConfig`
  - `TestEnvelopeValidator` (class, line 185) `class TestEnvelopeValidator`
  - `TestRandomContainer` (class, line 272) `class TestRandomContainer`
  - `TestDeniableVaultDB` (class, line 293) `class TestDeniableVaultDB`
  - `TestDeniableVaultController` (class, line 325) `class TestDeniableVaultController`
  - `TestDeniableVaultApi` (class, line 390) `class TestDeniableVaultApi`
  - `test_defaults_are_self_consistent` (method, line 141) `def test_defaults_are_self_consistent(self)`
  - `test_expected_ct_length_matches_base64_formula` (method, line 150) `def test_expected_ct_length_matches_base64_formula(self, config)`
  - `test_mapping_overrides_defaults` (method, line 154) `def test_mapping_overrides_defaults(self)`
  - `test_environment_overrides_mapping` (method, line 161) `def test_environment_overrides_mapping(self, monkeypatch)`
  - `test_allowed_kdf_csv_is_parsed` (method, line 166) `def test_allowed_kdf_csv_is_parsed(self, monkeypatch)`
  - `test_public_parameters_round_trip_to_json` (method, line 172) `def test_public_parameters_round_trip_to_json(self, config)`
  - `test_accepts_a_well_formed_envelope` (method, line 186) `def test_accepts_a_well_formed_envelope(self, validator, config)`
  - `test_rejects_non_dict` (method, line 189) `def test_rejects_non_dict(self, validator)`
  - `test_rejects_wrong_schema_version` (method, line 194) `def test_rejects_wrong_schema_version(self, validator, config)`
  - `test_rejects_unknown_kdf` (method, line 200) `def test_rejects_unknown_kdf(self, validator, config)`
  - `test_rejects_iterations_below_minimum` (method, line 206) `def test_rejects_iterations_below_minimum(self, validator, config)`
  - `test_rejects_iterations_above_maximum` (method, line 212) `def test_rejects_iterations_above_maximum(self, validator, config)`
  - `test_rejects_wrong_slot_count` (method, line 218) `def test_rejects_wrong_slot_count(self, validator, config)`
  - `test_rejects_bad_salt_length` (method, line 224) `def test_rejects_bad_salt_length(self, validator, config)`
  - `test_rejects_non_hex_salt` (method, line 230) `def test_rejects_non_hex_salt(self, validator, config)`
  - `test_rejects_bad_nonce_length` (method, line 236) `def test_rejects_bad_nonce_length(self, validator, config)`
  - `test_rejects_ciphertext_of_wrong_length` (method, line 242) `def test_rejects_ciphertext_of_wrong_length(self, validator, config)`
  - `test_rejects_unequal_slot_ciphertext_lengths` (method, line 248) `def test_rejects_unequal_slot_ciphertext_lengths(self, validator, config)`
  - `test_rejects_invalid_base64_ciphertext` (method, line 254) `def test_rejects_invalid_base64_ciphertext(self, validator, config)`
  - `test_rejects_missing_slot_keys` (method, line 260) `def test_rejects_missing_slot_keys(self, validator, config)`
  - `test_random_container_passes_validation` (method, line 273) `def test_random_container_passes_validation(self, config, validator)`
  - `test_random_containers_differ` (method, line 276) `def test_random_containers_differ(self, config)`
  - `test_random_container_has_fixed_shape` (method, line 281) `def test_random_container_has_fixed_shape(self, config)`
  - `test_upsert_then_get_round_trips_verbatim` (method, line 294) `def test_upsert_then_get_round_trips_verbatim(self, tmp_path)`
  - `test_upsert_replaces_existing_row` (method, line 303) `def test_upsert_replaces_existing_row(self, tmp_path)`
  - `test_get_missing_returns_none` (method, line 309) `def test_get_missing_returns_none(self, tmp_path)`
  - `test_exists` (method, line 313) `def test_exists(self, tmp_path)`
  - `_controller` (method, line 326) `def _controller(self, tmp_path)`
  - `test_load_or_provision_mints_when_absent` (method, line 331) `def test_load_or_provision_mints_when_absent(self, app, tmp_path)`
  - `test_load_or_provision_is_stable` (method, line 339) `def test_load_or_provision_is_stable(self, app, tmp_path)`
  - `test_save_then_load_round_trips` (method, line 346) `def test_save_then_load_round_trips(self, app, tmp_path)`
  - `test_save_rejects_invalid_envelope` (method, line 354) `def test_save_rejects_invalid_envelope(self, app, tmp_path)`
  - `test_reset_replaces_with_a_valid_random_container` (method, line 363) `def test_reset_replaces_with_a_valid_random_container(self, app, tmp_path)`
  - `test_audit_is_generic_and_never_contains_ciphertext` (method, line 373) `def test_audit_is_generic_and_never_contains_ciphertext(self, app, tmp_path, audit_records)`
  - `test_settings_page_requires_authentication` (method, line 391) `def test_settings_page_requires_authentication(self, client)`
  - `test_get_api_requires_authentication` (method, line 395) `def test_get_api_requires_authentication(self, client)`
  - `test_settings_page_renders_for_authenticated_user` (method, line 399) `def test_settings_page_renders_for_authenticated_user(self, client, app)`
  - `test_get_always_returns_an_envelope_and_parameters` (method, line 406) `def test_get_always_returns_an_envelope_and_parameters(self, client, app)`
  - `test_put_without_csrf_is_rejected` (method, line 414) `def test_put_without_csrf_is_rejected(self, client, app)`
  - `test_put_get_reset_round_trip` (method, line 422) `def test_put_get_reset_round_trip(self, client, app)`
  - `test_put_rejects_malformed_envelope` (method, line 447) `def test_put_rejects_malformed_envelope(self, client, app)`
  - `test_vault_is_scoped_to_the_authenticated_user` (method, line 461) `def test_vault_is_scoped_to_the_authenticated_user(self, client, app)`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

## tests/test_security.py
- Layer: testing
- Language: py
- Symbols:
  - `test_audit_event_includes_ip_and_ua_by_default` (function, line 12) `def test_audit_event_includes_ip_and_ua_by_default(app, audit_records, monkeypatch)`
  - `test_audit_event_redacts_ip_and_ua_when_disabled` (function, line 29) `def test_audit_event_redacts_ip_and_ua_when_disabled(app, audit_records, monkeypatch)`
  - `test_json_csrf_protect_rejects_missing_token` (function, line 45) `def test_json_csrf_protect_rejects_missing_token(app)`
  - `test_json_csrf_protect_accepts_valid_header_token` (function, line 57) `def test_json_csrf_protect_accepts_valid_header_token(app)`
  - `test_json_csrf_protect_passes_get_through_without_token` (function, line 77) `def test_json_csrf_protect_passes_get_through_without_token(app)`
  - `view` (function, line 47) `def view()`
  - `view` (function, line 59) `def view()`
  - `view` (function, line 79) `def view()`
- Depends on: `utils/security.py`

## tests/test_srp.py
- Layer: testing
- Language: py
- Symbols:
  - `_h` (function, line 16) `def _h()`
  - `_hint` (function, line 23) `def _hint()`
  - `_client_derive_verifier` (function, line 27) `def _client_derive_verifier(username, password, salt_hex)`
  - `_client_compute_proof` (function, line 34) `def _client_compute_proof(username, password, salt_hex, server_a_secret, server_a, server_b)`
  - `test_srp6a_full_roundtrip_matches_server_proofs` (function, line 74) `def test_srp6a_full_roundtrip_matches_server_proofs()`
  - `test_srp6a_wrong_password_produces_mismatched_proof` (function, line 104) `def test_srp6a_wrong_password_produces_mismatched_proof()`
- Depends on: `utils/utils.py`
