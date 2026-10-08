# Symbols (page 2 of 2)
Previous: [SYMBOLS.md](SYMBOLS.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `test_defaults_are_self_consistent` | method | `tests/test_facade.py:157` | `def test_defaults_are_self_consistent(self)` |
| `test_defaults_keep_duress_alert_off` | method | `tests/test_facade.py:154` | `def test_defaults_keep_duress_alert_off(self)` |
| `test_defaults_keep_the_facade_off` | method | `tests/test_facade.py:149` | `def test_defaults_keep_the_facade_off(self)` |
| `test_disabled_facade_serves_the_real_login` | method | `tests/test_facade.py:469` | `def test_disabled_facade_serves_the_real_login(self, client)` |
| `test_duress_alert_is_opt_in_and_generically_named` | method | `tests/test_facade.py:372` | `def test_duress_alert_is_opt_in_and_generically_named(self, app, fast_hasher, audit_records)` |
| `test_duress_phrase_marks_the_session` | method | `tests/test_facade.py:432` | `def test_duress_phrase_marks_the_session(self, facade_client)` |
| `test_duress_phrase_yields_a_duress_ticket` | method | `tests/test_facade.py:300` | `def test_duress_phrase_yields_a_duress_ticket(self, app, gate_config)` |
| `test_enabled_without_a_hash_fails_open_to_the_real_app` | method | `tests/test_facade.py:474` | `def test_enabled_without_a_hash_fails_open_to_the_real_app(self, tmp_path)` |
| `test_environment_overrides_mapping` | method | `tests/test_facade.py:172` | `def test_environment_overrides_mapping(self, monkeypatch)` |
| `test_from_config_builds_a_working_hasher` | method | `tests/test_facade.py:231` | `def test_from_config_builds_a_working_hasher(self)` |
| `test_gate_configured_requires_enabled_and_a_hash` | method | `tests/test_facade.py:183` | `def test_gate_configured_requires_enabled_and_a_hash(self)` |
| `test_gate_endpoint_is_absent_when_facade_disabled` | method | `tests/test_facade.py:465` | `def test_gate_endpoint_is_absent_when_facade_disabled(self, client)` |
| `test_hash_is_salted_so_two_hashes_differ` | method | `tests/test_facade.py:218` | `def test_hash_is_salted_so_two_hashes_differ(self, fast_hasher)` |
| `test_hash_then_verify_accepts_the_phrase` | method | `tests/test_facade.py:210` | `def test_hash_then_verify_accepts_the_phrase(self, fast_hasher)` |
| `test_issue_rejects_an_unknown_mode` | method | `tests/test_facade.py:256` | `def test_issue_rejects_an_unknown_mode(self)` |
| `test_issue_then_verify_round_trips_the_mode` | method | `tests/test_facade.py:251` | `def test_issue_then_verify_round_trips_the_mode(self)` |
| `test_mapping_overrides_defaults` | method | `tests/test_facade.py:165` | `def test_mapping_overrides_defaults(self)` |
| `test_maximum_length_phrase_is_accepted` | method | `tests/test_facade.py:337` | `def test_maximum_length_phrase_is_accepted(self, app, fast_hasher)` |
| `test_minimum_length_phrase_is_accepted` | method | `tests/test_facade.py:325` | `def test_minimum_length_phrase_is_accepted(self, app, fast_hasher)` |
| `test_miss_without_a_duress_hash` | method | `tests/test_facade.py:314` | `def test_miss_without_a_duress_hash(self, app, fast_hasher)` |
| `test_protected_paths_csv_is_parsed` | method | `tests/test_facade.py:177` | `def test_protected_paths_csv_is_parsed(self)` |
| `test_real_phrase_reveals_the_login` | method | `tests/test_facade.py:417` | `def test_real_phrase_reveals_the_login(self, facade_client)` |
| `test_real_phrase_yields_a_real_ticket` | method | `tests/test_facade.py:292` | `def test_real_phrase_yields_a_real_ticket(self, app, gate_config)` |
| `test_too_long_phrase_is_a_miss` | method | `tests/test_facade.py:355` | `def test_too_long_phrase_is_a_miss(self, app, gate_config)` |
| `test_too_short_phrase_is_a_miss` | method | `tests/test_facade.py:349` | `def test_too_short_phrase_is_a_miss(self, app, gate_config)` |
| `test_verify_rejects_a_malformed_stored_hash` | method | `tests/test_facade.py:224` | `def test_verify_rejects_a_malformed_stored_hash(self, fast_hasher)` |
| `test_verify_rejects_a_non_string_stored_hash` | method | `tests/test_facade.py:227` | `def test_verify_rejects_a_non_string_stored_hash(self, fast_hasher)` |
| `test_verify_rejects_a_non_string_token` | method | `tests/test_facade.py:277` | `def test_verify_rejects_a_non_string_token(self)` |
| `test_verify_rejects_a_ticket_signed_with_another_key` | method | `tests/test_facade.py:267` | `def test_verify_rejects_a_ticket_signed_with_another_key(self)` |
| `test_verify_rejects_a_wrong_phrase` | method | `tests/test_facade.py:214` | `def test_verify_rejects_a_wrong_phrase(self, fast_hasher)` |
| `test_verify_rejects_an_empty_stored_hash` | method | `tests/test_facade.py:221` | `def test_verify_rejects_an_empty_stored_hash(self, fast_hasher)` |
| `test_verify_rejects_an_expired_ticket` | method | `tests/test_facade.py:261` | `def test_verify_rejects_an_expired_ticket(self)` |
| `test_verify_rejects_garbage_and_none` | method | `tests/test_facade.py:272` | `def test_verify_rejects_garbage_and_none(self)` |
| `test_wrong_phrase_is_a_miss_with_no_ticket` | method | `tests/test_facade.py:307` | `def test_wrong_phrase_is_a_miss_with_no_ticket(self, app, gate_config)` |
| `test_wrong_phrase_keeps_the_cover_and_does_not_redirect` | method | `tests/test_facade.py:409` | `def test_wrong_phrase_keeps_the_cover_and_does_not_redirect(self, facade_client)` |
| `test_compute_sri_format` | function | `tests/test_integrity.py:19` | `def test_compute_sri_format()` |
| `test_jinja_global_registered` | function | `tests/test_integrity.py:51` | `def test_jinja_global_registered(app)` |
| `test_manifest_exists_and_pins_crypto` | function | `tests/test_integrity.py:25` | `def test_manifest_exists_and_pins_crypto()` |
| `test_manifest_hashes_match_files` | function | `tests/test_integrity.py:37` | `def test_manifest_hashes_match_files()` |
| `test_template_integrity_resolves_both_forms` | function | `tests/test_integrity.py:44` | `def test_template_integrity_resolves_both_forms()` |
| `test_verify_build_passes_on_clean_tree` | function | `tests/test_integrity.py:55` | `def test_verify_build_passes_on_clean_tree()` |
| `_FakeS3` | class | `tests/test_padding.py:128` | `class _FakeS3` |
| `_FakeUpload` | class | `tests/test_padding.py:136` | `class _FakeUpload` |
| `__init__` | method | `tests/test_padding.py:129` | `def __init__(self)` |
| `__init__` | method | `tests/test_padding.py:139` | `def __init__(self, body)` |
| `put_object` | method | `tests/test_padding.py:132` | `def put_object(self, Bucket, Key, Body)` |
| `read` | method | `tests/test_padding.py:142` | `def read(self)` |
| `test_bucket_boundaries` | function | `tests/test_padding.py:38` | `def test_bucket_boundaries()` |
| `test_cache_holds_tables_not_pad_bytes` | function | `tests/test_padding.py:99` | `def test_cache_holds_tables_not_pad_bytes()` |
| `test_config_from_env_falls_back_on_garbage` | function | `tests/test_padding.py:94` | `def test_config_from_env_falls_back_on_garbage(monkeypatch)` |
| `test_config_from_env_override` | function | `tests/test_padding.py:87` | `def test_config_from_env_override(monkeypatch)` |
| `test_file_controller_accepts_bucketed_upload` | method | `tests/test_padding.py:152` | `def test_file_controller_accepts_bucketed_upload(app)` |
| `test_file_controller_rejects_unpadded_upload` | method | `tests/test_padding.py:146` | `def test_file_controller_rejects_unpadded_upload(app)` |
| `test_message_controller_accepts_bucketed_envelope` | function | `tests/test_padding.py:120` | `def test_message_controller_accepts_bucketed_envelope(app, tmp_path, monkeypatch)` |
| `test_message_controller_rejects_malformed_base64` | function | `tests/test_padding.py:113` | `def test_message_controller_rejects_malformed_base64(app, tmp_path, monkeypatch)` |
| `test_message_controller_rejects_unpadded_envelope` | function | `tests/test_padding.py:105` | `def test_message_controller_rejects_unpadded_envelope(app, tmp_path, monkeypatch)` |
| `test_pad_output_length_is_bucketed` | function | `tests/test_padding.py:44` | `def test_pad_output_length_is_bucketed()` |
| `test_pad_rejects_oversize` | function | `tests/test_padding.py:56` | `def test_pad_rejects_oversize()` |
| `test_pad_roundtrip_file_kind` | function | `tests/test_padding.py:33` | `def test_pad_roundtrip_file_kind()` |
| `test_pad_roundtrip_message_sizes` | function | `tests/test_padding.py:26` | `def test_pad_roundtrip_message_sizes()` |
| `test_pad_uses_fresh_randomness` | function | `tests/test_padding.py:49` | `def test_pad_uses_fresh_randomness()` |
| `test_unpad_rejects_corrupt_prefix` | function | `tests/test_padding.py:66` | `def test_unpad_rejects_corrupt_prefix()` |
| `test_unpad_rejects_non_bucket_length` | function | `tests/test_padding.py:61` | `def test_unpad_rejects_non_bucket_length()` |
| `test_unpad_rejects_wrong_kind` | function | `tests/test_padding.py:74` | `def test_unpad_rejects_wrong_kind()` |
| `test_wire_lengths` | function | `tests/test_padding.py:80` | `def test_wire_lengths()` |
| `_FakeProcess` | class | `tests/test_secure_channel.py:260` | `class _FakeProcess` |
| `_fake_mono` | method | `tests/test_secure_channel.py:573` | `def _fake_mono()` |
| `_fake_mono` | method | `tests/test_secure_channel.py:606` | `def _fake_mono()` |
| `_fake_popen` | method | `tests/test_secure_channel.py:263` | `def _fake_popen(cmd)` |
| `_fake_sleep` | method | `tests/test_secure_channel.py:576` | `def _fake_sleep(secs)` |
| `_fake_sleep` | method | `tests/test_secure_channel.py:609` | `def _fake_sleep(secs)` |
| `_fake_sleep_file` | method | `tests/test_secure_channel.py:627` | `def _fake_sleep_file(secs)` |
| `_raise` | method | `tests/test_secure_channel.py:471` | `def _raise()` |
| `_raise_lookup` | method | `tests/test_secure_channel.py:536` | `def _raise_lookup(pid, sig)` |
| `_raise_os` | method | `tests/test_secure_channel.py:548` | `def _raise_os(pid, sig)` |
| `_raise_perm` | method | `tests/test_secure_channel.py:542` | `def _raise_perm(pid, sig)` |
| `_raise_pg` | method | `tests/test_secure_channel.py:290` | `def _raise_pg(pid, sig)` |
| `_record_kill` | method | `tests/test_secure_channel.py:293` | `def _record_kill(pid, sig)` |
| `fake_launcher` | function | `tests/test_secure_channel.py:67` | `def fake_launcher(cmd, log_path)` |
| `fake_launcher` | function | `tests/test_secure_channel.py:105` | `def fake_launcher(cmd, log_path)` |
| `fake_launcher` | method | `tests/test_secure_channel.py:419` | `def fake_launcher(cmd, log_path)` |
| `fake_launcher` | method | `tests/test_secure_channel.py:445` | `def fake_launcher(cmd, log_path)` |
| `fake_launcher` | method | `tests/test_secure_channel.py:737` | `def fake_launcher(cmd, log_path)` |
| `test_audit_details_default_verb_and_empty_urls` | function | `tests/test_secure_channel.py:334` | `def test_audit_details_default_verb_and_empty_urls()` |
| `test_audit_details_never_carry_urls` | function | `tests/test_secure_channel.py:122` | `def test_audit_details_never_carry_urls()` |
| `test_channel_diagnostics_missing_absolute_path` | function | `tests/test_secure_channel.py:656` | `def test_channel_diagnostics_missing_absolute_path(tmp_path)` |
| `test_channel_diagnostics_reports_availability` | function | `tests/test_secure_channel.py:636` | `def test_channel_diagnostics_reports_availability(tmp_path)` |
| `test_channel_state_file_permissions` | function | `tests/test_secure_channel.py:153` | `def test_channel_state_file_permissions(tmp_path)` |
| `test_channel_status_defaults_and_single_side_active` | function | `tests/test_secure_channel.py:229` | `def test_channel_status_defaults_and_single_side_active()` |
| `test_cleanup_scratch_suppresses_rmtree_errors` | function | `tests/test_secure_channel.py:463` | `def test_cleanup_scratch_suppresses_rmtree_errors(tmp_path, monkeypatch)` |
| `test_cloudflared_cmd_matches_origin_scheme` | function | `tests/test_secure_channel.py:733` | `def test_cloudflared_cmd_matches_origin_scheme(tmp_path)` |
| `test_config_blank_values_fall_back_to_defaults` | function | `tests/test_secure_channel.py:186` | `def test_config_blank_values_fall_back_to_defaults()` |
| `test_config_defaults_to_disabled_without_binaries` | function | `tests/test_secure_channel.py:30` | `def test_config_defaults_to_disabled_without_binaries()` |
| `test_config_env_beats_mapping` | function | `tests/test_secure_channel.py:219` | `def test_config_env_beats_mapping()` |
| `test_config_explicit_values_are_preserved` | function | `tests/test_secure_channel.py:203` | `def test_config_explicit_values_are_preserved()` |
| `test_config_reads_mode_and_port_from_env` | function | `tests/test_secure_channel.py:37` | `def test_config_reads_mode_and_port_from_env()` |
| `test_config_reads_origin_scheme` | function | `tests/test_secure_channel.py:706` | `def test_config_reads_origin_scheme()` |
| `test_config_rejects_out_of_range_port` | function | `tests/test_secure_channel.py:47` | `def test_config_rejects_out_of_range_port()` |
| `test_default_killer_falls_back_to_kill` | function | `tests/test_secure_channel.py:286` | `def test_default_killer_falls_back_to_kill(monkeypatch)` |
| `test_default_killer_ignores_non_positive_pid` | function | `tests/test_secure_channel.py:276` | `def test_default_killer_ignores_non_positive_pid(monkeypatch)` |
| `test_default_launcher_detaches_process` | function | `tests/test_secure_channel.py:254` | `def test_default_launcher_detaches_process(monkeypatch)` |
| `test_env_template_documents_channel_keys` | function | `tests/test_secure_channel.py:139` | `def test_env_template_documents_channel_keys()` |
| `test_manager_init_blank_binaries_fall_back` | function | `tests/test_secure_channel.py:302` | `def test_manager_init_blank_binaries_fall_back()` |
| `test_manager_rejects_invalid_mode` | function | `tests/test_secure_channel.py:90` | `def test_manager_rejects_invalid_mode(tmp_path)` |
| `test_manager_starts_hybrid_with_injected_launcher` | function | `tests/test_secure_channel.py:64` | `def test_manager_starts_hybrid_with_injected_launcher(tmp_path)` |
| `test_manager_stop_clears_state_with_killer` | function | `tests/test_secure_channel.py:101` | `def test_manager_stop_clears_state_with_killer(tmp_path)` |
| `test_normalize_onion_shapes` | function | `tests/test_secure_channel.py:555` | `def test_normalize_onion_shapes()` |
| `test_origin_scheme_parsing` | function | `tests/test_secure_channel.py:696` | `def test_origin_scheme_parsing()` |
| `test_origin_url_points_at_loopback` | function | `tests/test_secure_channel.py:719` | `def test_origin_url_points_at_loopback()` |
| `test_pid_live_branches` | function | `tests/test_secure_channel.py:527` | `def test_pid_live_branches(monkeypatch, tmp_path)` |
| `test_port_boundaries_accept_edges_and_reject_outside` | function | `tests/test_secure_channel.py:175` | `def test_port_boundaries_accept_edges_and_reject_outside()` |
| `test_read_log_tail_returns_trailing_lines` | function | `tests/test_secure_channel.py:671` | `def test_read_log_tail_returns_trailing_lines(tmp_path)` |
| `test_read_state_filters_bad_pids` | function | `tests/test_secure_channel.py:357` | `def test_read_state_filters_bad_pids(tmp_path)` |
| `test_resolve_binary_absolute_path_must_exist` | function | `tests/test_secure_channel.py:511` | `def test_resolve_binary_absolute_path_must_exist(tmp_path)` |
| `test_resolve_binary_with_default_launcher_requires_path` | function | `tests/test_secure_channel.py:480` | `def test_resolve_binary_with_default_launcher_requires_path(tmp_path)` |
| `test_resolve_binary_with_injected_launcher_skips_which` | function | `tests/test_secure_channel.py:497` | `def test_resolve_binary_with_injected_launcher_skips_which(tmp_path)` |
| `test_rotate_disabled_state_raises` | function | `tests/test_secure_channel.py:322` | `def test_rotate_disabled_state_raises(tmp_path)` |
| `test_rotate_without_state_raises` | function | `tests/test_secure_channel.py:311` | `def test_rotate_without_state_raises(tmp_path)` |
| `test_s3_probe_detects_live_endpoint` | function | `tests/test_secure_channel.py:771` | `def test_s3_probe_detects_live_endpoint(app)` |
| `test_s3_probe_skips_dead_endpoint` | function | `tests/test_secure_channel.py:763` | `def test_s3_probe_skips_dead_endpoint(app)` |
| `test_start_creates_nested_state_dirs` | function | `tests/test_secure_channel.py:416` | `def test_start_creates_nested_state_dirs(tmp_path)` |
| `test_start_tor_only_creates_nested_state_dirs` | function | `tests/test_secure_channel.py:442` | `def test_start_tor_only_creates_nested_state_dirs(tmp_path)` |
| `test_status_for_drops_non_positive_pids` | function | `tests/test_secure_channel.py:348` | `def test_status_for_drops_non_positive_pids()` |
| `test_superadmin_channel_routes_require_superadmin` | function | `tests/test_secure_channel.py:133` | `def test_superadmin_channel_routes_require_superadmin(client)` |
| `test_superadmin_channel_section_is_readable` | function | `tests/test_secure_channel.py:685` | `def test_superadmin_channel_section_is_readable()` |
| `test_url_validators_accept_only_expected_shapes` | function | `tests/test_secure_channel.py:55` | `def test_url_validators_accept_only_expected_shapes()` |
| `test_validators_reject_non_string_inputs` | function | `tests/test_secure_channel.py:164` | `def test_validators_reject_non_string_inputs()` |
| `test_wait_helpers_include_deadline_instant` | function | `tests/test_secure_channel.py:597` | `def test_wait_helpers_include_deadline_instant(tmp_path, monkeypatch)` |
| `test_wait_helpers_respect_deadline_and_content` | function | `tests/test_secure_channel.py:564` | `def test_wait_helpers_respect_deadline_and_content(tmp_path, monkeypatch)` |
| `test_write_state_creates_nested_dirs` | function | `tests/test_secure_channel.py:408` | `def test_write_state_creates_nested_dirs(tmp_path)` |
| `test_write_state_is_sorted_and_ephemeral` | function | `tests/test_secure_channel.py:378` | `def test_write_state_is_sorted_and_ephemeral(tmp_path)` |
| `test_write_state_twice_in_existing_dir` | function | `tests/test_secure_channel.py:397` | `def test_write_state_twice_in_existing_dir(tmp_path)` |
| `test_audit_event_includes_ip_and_ua_by_default` | function | `tests/test_security.py:12` | `def test_audit_event_includes_ip_and_ua_by_default(app, audit_records, monkeypatch)` |
| `test_audit_event_redacts_ip_and_ua_when_disabled` | function | `tests/test_security.py:29` | `def test_audit_event_redacts_ip_and_ua_when_disabled(app, audit_records, monkeypatch)` |
| `test_json_csrf_protect_accepts_valid_header_token` | function | `tests/test_security.py:57` | `def test_json_csrf_protect_accepts_valid_header_token(app)` |
| `test_json_csrf_protect_passes_get_through_without_token` | function | `tests/test_security.py:77` | `def test_json_csrf_protect_passes_get_through_without_token(app)` |
| `test_json_csrf_protect_rejects_missing_token` | function | `tests/test_security.py:45` | `def test_json_csrf_protect_rejects_missing_token(app)` |
| `view` | function | `tests/test_security.py:47` | `def view()` |
| `view` | function | `tests/test_security.py:59` | `def view()` |
| `view` | function | `tests/test_security.py:79` | `def view()` |
| `_client_compute_proof` | function | `tests/test_srp.py:34` | `def _client_compute_proof(username, password, salt_hex, server_a_secret, server_a, server_b)` |
| `_client_derive_verifier` | function | `tests/test_srp.py:27` | `def _client_derive_verifier(username, password, salt_hex)` |
| `_h` | function | `tests/test_srp.py:16` | `def _h()` |
| `_hint` | function | `tests/test_srp.py:23` | `def _hint()` |
| `test_srp6a_full_roundtrip_matches_server_proofs` | function | `tests/test_srp.py:74` | `def test_srp6a_full_roundtrip_matches_server_proofs()` |
| `test_srp6a_wrong_password_produces_mismatched_proof` | function | `tests/test_srp.py:104` | `def test_srp6a_wrong_password_produces_mismatched_proof()` |
| `test_database_path_default_outside_a_context` | function | `tests/test_utils.py:18` | `def test_database_path_default_outside_a_context(monkeypatch)` |
| `test_database_path_honors_env_outside_a_context` | function | `tests/test_utils.py:13` | `def test_database_path_honors_env_outside_a_context(monkeypatch)` |
| `test_database_path_prefers_the_configured_path` | function | `tests/test_utils.py:8` | `def test_database_path_prefers_the_configured_path(app)` |
| `build_manifest` | function | `tools/generate_sri.py:66` | `def build_manifest(cdn, local)` |
| `collect_local_assets` | function | `tools/generate_sri.py:41` | `def collect_local_assets()` |
| `fetch_cdn_assets` | function | `tools/generate_sri.py:56` | `def fetch_cdn_assets()` |
| `main` | function | `tools/generate_sri.py:81` | `def main(argv)` |
| `render_manifest` | function | `tools/generate_sri.py:76` | `def render_manifest(manifest)` |
| `Mutation` | class | `tools/mutation_test.py:56` | `class Mutation` |
| `_is_equivalent_bool` | method | `tools/mutation_test.py:67` | `def _is_equivalent_bool(tokens, index)` |
| `apply_mutation` | method | `tools/mutation_test.py:109` | `def apply_mutation(source, mutation)` |
| `collect` | method | `tools/mutation_test.py:121` | `def collect(targets, limit)` |
| `discover_mutations` | method | `tools/mutation_test.py:79` | `def discover_mutations(path, source)` |
| `main` | method | `tools/mutation_test.py:157` | `def main(argv)` |
| `purge_bytecode` | method | `tools/mutation_test.py:133` | `def purge_bytecode()` |
| `run_suite` | method | `tools/mutation_test.py:142` | `def run_suite(python, tests)` |
| `AssetReference` | class | `tools/verify_build.py:34` | `class AssetReference(HTMLParser)` |
| `__init__` | method | `tools/verify_build.py:37` | `def __init__(self)` |
| `_normalize_reference` | method | `tools/verify_build.py:60` | `def _normalize_reference(ref)` |
| `check_bucket_parity` | method | `tools/verify_build.py:126` | `def check_bucket_parity(failures)` |
| `check_local_hashes` | method | `tools/verify_build.py:95` | `def check_local_hashes(manifest, failures)` |
| `check_template_references` | method | `tools/verify_build.py:110` | `def check_template_references(manifest, failures)` |
| `expected_for_reference` | method | `tools/verify_build.py:76` | `def expected_for_reference(manifest, ref)` |
| `handle_starttag` | method | `tools/verify_build.py:42` | `def handle_starttag(self, tag, attrs)` |
| `integrity_attribute_ok` | method | `tools/verify_build.py:85` | `def integrity_attribute_ok(integrity, ref, expected)` |
| `load_manifest` | method | `tools/verify_build.py:71` | `def load_manifest()` |
| `main` | method | `tools/verify_build.py:141` | `def main()` |
| `Cache` | class | `utils/cache.py:6` | `class Cache` |
| `__init__` | method | `utils/cache.py:8` | `def __init__(self)` |
| `delete` | method | `utils/cache.py:20` | `def delete(self, key)` |
| `get` | method | `utils/cache.py:11` | `def get(self, key)` |
| `set` | method | `utils/cache.py:16` | `def set(self, key, value, ttl)` |
| `_cached_manifest_text` | function | `utils/integrity.py:42` | `def _cached_manifest_text()` |
| `clear_manifest_cache` | function | `utils/integrity.py:72` | `def clear_manifest_cache()` |
| `compute_file_sri` | function | `utils/integrity.py:36` | `def compute_file_sri(path, algorithm)` |
| `compute_sri` | function | `utils/integrity.py:30` | `def compute_sri(data, algorithm)` |
| `integrity_for` | function | `utils/integrity.py:55` | `def integrity_for(key)` |
| `load_manifest` | function | `utils/integrity.py:47` | `def load_manifest()` |
| `manifest_path` | function | `utils/integrity.py:25` | `def manifest_path()` |
| `template_integrity` | function | `utils/integrity.py:77` | `def template_integrity(key)` |
| `external_url` | function | `utils/mailer.py:22` | `def external_url(path)` |
| `mail_is_configured` | function | `utils/mailer.py:38` | `def mail_is_configured()` |
| `send_transactional_email` | function | `utils/mailer.py:51` | `def send_transactional_email(subject, recipients, body)` |
| `PaddingConfig` | class | `utils/padding.py:78` | `class PaddingConfig` |
| `PaddingError` | class | `utils/padding.py:73` | `class PaddingError(ValueError)` |
| `_cached_bucket_table` | method | `utils/padding.py:128` | `def _cached_bucket_table(fingerprint)` |
| `_parse_buckets` | method | `utils/padding.py:95` | `def _parse_buckets(raw, fallback)` |
| `bucket_for` | method | `utils/padding.py:149` | `def bucket_for(plaintext_len, kind, config)` |
| `buckets_for` | method | `utils/padding.py:84` | `def buckets_for(self, kind)` |
| `cached_tables` | method | `utils/padding.py:142` | `def cached_tables(config)` |
| `config_from_env` | method | `utils/padding.py:109` | `def config_from_env()` |
| `is_allowed_ciphertext_len` | method | `utils/padding.py:214` | `def is_allowed_ciphertext_len(ciphertext_len, kind, config)` |
| `max_plaintext_bytes` | method | `utils/padding.py:90` | `def max_plaintext_bytes(self, kind)` |
| `pad` | method | `utils/padding.py:169` | `def pad(plaintext, kind, config)` |
| `unpad` | method | `utils/padding.py:183` | `def unpad(padded, kind, config)` |
| `wire_ciphertext_len` | method | `utils/padding.py:209` | `def wire_ciphertext_len(bucket)` |
| `SubscriptionPlans` | class | `utils/plans.py:3` | `class SubscriptionPlans` |
| `get_plan` | method | `utils/plans.py:30` | `def get_plan(plan_name)` |
| `validate_plan_payment` | method | `utils/plans.py:42` | `def validate_plan_payment(plan_name, amount_paid)` |
| `_is_trial_elapsed` | function | `utils/scheduler.py:54` | `def _is_trial_elapsed(user)` |
| `_now_utc` | function | `utils/scheduler.py:32` | `def _now_utc()` |
| `check_trial_expiration` | function | `utils/scheduler.py:72` | `def check_trial_expiration()` |
| `cleanup_old_messages` | function | `utils/scheduler.py:118` | `def cleanup_old_messages()` |
| `init_scheduler` | function | `utils/scheduler.py:37` | `def init_scheduler(app, mail)` |
| `_correlation_id` | function | `utils/security.py:72` | `def _correlation_id()` |
| `_extract_csrf_token` | function | `utils/security.py:172` | `def _extract_csrf_token()` |
| `_get_audit_logger` | function | `utils/security.py:46` | `def _get_audit_logger()` |
| `audit_event` | function | `utils/security.py:86` | `def audit_event(event)` |
| `constant_time_compare` | function | `utils/security.py:123` | `def constant_time_compare(a, b)` |
| `hash_secret` | function | `utils/security.py:135` | `def hash_secret(secret)` |
| `json_csrf_protect` | function | `utils/security.py:193` | `def json_csrf_protect(view)` |
| `new_one_time_code` | function | `utils/security.py:163` | `def new_one_time_code(length)` |
| `verify_secret` | function | `utils/security.py:156` | `def verify_secret(secret, expected_hash)` |
| `wrapper` | function | `utils/security.py:207` | `def wrapper()` |
| `SRPSessionStore` | class | `utils/srp6a.py:150` | `class SRPSessionStore` |
| `__init__` | method | `utils/srp6a.py:158` | `def __init__(self, storage_uri)` |
| `_hash` | function | `utils/srp6a.py:60` | `def _hash()` |
| `_hash_int` | function | `utils/srp6a.py:68` | `def _hash_int()` |
| `_key` | method | `utils/srp6a.py:168` | `def _key(username)` |
| `compute_k` | function | `utils/srp6a.py:73` | `def compute_k()` |
| `compute_proofs` | function | `utils/srp6a.py:107` | `def compute_proofs(username, salt_hex, verifier, server_a, server_b, server_b_secret)` |
| `compute_u` | function | `utils/srp6a.py:78` | `def compute_u(server_a, server_b)` |
| `generate_server_challenge` | function | `utils/srp6a.py:91` | `def generate_server_challenge(verifier)` |
| `hello` | method | `utils/srp6a.py:224` | `def hello(store, username, client_a_hex, salt_hex, verifier_hex)` |
| `i2osp` | function | `utils/srp6a.py:47` | `def i2osp(value)` |
| `load` | method | `utils/srp6a.py:202` | `def load(self, username)` |
| `save` | method | `utils/srp6a.py:172` | `def save(self, username, salt_hex, verifier_hex, server_a_hex, server_b_hex, server_b_secret_hex)` |
| `verify` | method | `utils/srp6a.py:260` | `def verify(store, username, client_m1_hex)` |
| `Config` | class | `utils/utils.py:103` | `class Config` |
| `Payload` | class | `utils/utils.py:80` | `class Payload(TypedDict)` |
| `__getitem__` | method | `utils/utils.py:165` | `def __getitem__(self, key)` |
| `__init__` | method | `utils/utils.py:145` | `def __init__(self, config_dict)` |
| `as_bool` | function | `utils/utils.py:29` | `def as_bool(value, default)` |
| `database_path` | function | `utils/utils.py:12` | `def database_path()` |
| `load_payload` | method | `utils/utils.py:168` | `def load_payload()` |
| `sanitize_path` | function | `utils/utils.py:49` | `def sanitize_path(path)` |
| `about` | function | `views/about.py:6` | `def about()` |
| `delete_vault` | function | `views/account.py:130` | `def delete_vault()` |
| `get_deniable_vault_controller` | function | `views/account.py:51` | `def get_deniable_vault_controller()` |
| `get_vault` | function | `views/account.py:85` | `def get_vault()` |
| `put_vault` | function | `views/account.py:107` | `def put_vault()` |
| `settings` | function | `views/account.py:65` | `def settings()` |
| `PlanForm` | class | `views/admin.py:174` | `class PlanForm(FlaskForm)` |
| `UserEditForm` | class | `views/admin.py:141` | `class UserEditForm(FlaskForm)` |
| `_audit_action` | function | `views/admin.py:31` | `def _audit_action(actor, action, target_user, ip, details)` |
| `_channel_diagnostics` | function | `views/admin.py:116` | `def _channel_diagnostics(manager)` |
| `_channel_manager` | function | `views/admin.py:48` | `def _channel_manager()` |
| `_read_log_tail` | function | `views/admin.py:84` | `def _read_log_tail(state_dir, limit)` |
| `_s3_reachable` | function | `views/admin.py:54` | `def _s3_reachable(timeout)` |
| `admin` | method | `views/admin.py:186` | `def admin()` |
| `admin_contacts` | method | `views/admin.py:705` | `def admin_contacts()` |
| `edit_plan` | method | `views/admin.py:337` | `def edit_plan(plan_name)` |
| `manage_plans` | method | `views/admin.py:313` | `def manage_plans()` |
| `superadmin` | method | `views/admin.py:373` | `def superadmin()` |
| `superadmin_channel_rotate` | method | `views/admin.py:682` | `def superadmin_channel_rotate()` |
| `superadmin_channel_start` | method | `views/admin.py:620` | `def superadmin_channel_start()` |
| `superadmin_channel_stop` | method | `views/admin.py:659` | `def superadmin_channel_stop()` |
| `superadmin_edit_user` | method | `views/admin.py:208` | `def superadmin_edit_user(username)` |
| `superadmin_resend_confirmation` | method | `views/admin.py:523` | `def superadmin_resend_confirmation(username)` |
| `superadmin_reset_mfa` | method | `views/admin.py:476` | `def superadmin_reset_mfa(username)` |
| `superadmin_toggle_suspend` | method | `views/admin.py:570` | `def superadmin_toggle_suspend(username)` |
| `ContactForm` | class | `views/auth.py:108` | `class ContactForm(FlaskForm)` |
| `LoginForm` | class | `views/auth.py:124` | `class LoginForm(FlaskForm)` |
| `MFAForm` | class | `views/auth.py:103` | `class MFAForm(FlaskForm)` |
| `PhoneVerificationForm` | class | `views/auth.py:98` | `class PhoneVerificationForm(FlaskForm)` |
| `RegisterForm` | class | `views/auth.py:114` | `class RegisterForm(FlaskForm)` |
| `_recovery_key` | method | `views/auth.py:266` | `def _recovery_key()` |
| `_srp_key` | method | `views/auth.py:255` | `def _srp_key()` |
| `confirm_email` | method | `views/auth.py:344` | `def confirm_email(token)` |
| `contact` | method | `views/auth.py:454` | `def contact()` |
| `decorated_function` | method | `views/auth.py:87` | `def decorated_function()` |
| `decorator` | method | `views/auth.py:85` | `def decorator(f)` |
| `get_auth_controller` | method | `views/auth.py:132` | `def get_auth_controller()` |
| `get_csrf_token` | method | `views/auth.py:619` | `def get_csrf_token()` |
| `get_public_key` | method | `views/auth.py:485` | `def get_public_key()` |
| `get_recovery_bundle` | method | `views/auth.py:534` | `def get_recovery_bundle()` |
| `get_user_keys` | method | `views/auth.py:503` | `def get_user_keys()` |
| `handle_register` | method | `views/auth.py:150` | `def handle_register()` |
| `login` | method | `views/auth.py:234` | `def login()` |
| `logout` | method | `views/auth.py:337` | `def logout()` |
| `recover` | method | `views/auth.py:242` | `def recover()` |
| `resend_phone_verification` | method | `views/auth.py:384` | `def resend_phone_verification()` |
| `reset_with_recovery` | method | `views/auth.py:559` | `def reset_with_recovery()` |
| `role_required` | function | `views/auth.py:71` | `def role_required()` |
| `show_register` | method | `views/auth.py:143` | `def show_register()` |
| `srp_hello` | method | `views/auth.py:278` | `def srp_hello()` |
| `srp_verify` | method | `views/auth.py:299` | `def srp_verify()` |
| `toggle_mfa` | method | `views/auth.py:429` | `def toggle_mfa()` |
| `verify_mfa` | method | `views/auth.py:407` | `def verify_mfa()` |
| `verify_phone` | method | `views/auth.py:367` | `def verify_phone()` |
| `_build_cover_service` | function | `views/facade.py:71` | `def _build_cover_service(config)` |
| `_facade_cover` | function | `views/facade.py:48` | `def _facade_cover()` |
| `_ticket_mode` | function | `views/facade.py:86` | `def _ticket_mode(gate)` |
| `facade_gate` | function | `views/facade.py:60` | `def facade_gate()` |
| `register_facade` | function | `views/facade.py:33` | `def register_facade(app)` |
| `render_cover` | function | `views/facade.py:41` | `def render_cover()` |
| `faq` | function | `views/faq.py:7` | `def faq()` |
| `landing` | function | `views/faq.py:12` | `def landing()` |
| `UploadForm` | class | `views/file.py:15` | `class UploadForm(FlaskForm)` |
| `download` | method | `views/file.py:56` | `def download(filename)` |
| `upload` | method | `views/file.py:25` | `def upload()` |
| `MessageForm` | class | `views/message.py:19` | `class MessageForm(FlaskForm)` |
| `api_secure_message` | method | `views/message.py:49` | `def api_secure_message()` |
| `messages` | method | `views/message.py:29` | `def messages()` |
| `privacy` | function | `views/privacy.py:6` | `def privacy()` |
| `SubscriptionForm` | class | `views/subscription.py:24` | `class SubscriptionForm(FlaskForm)` |
| `__init__` | method | `views/subscription.py:26` | `def __init__(self)` |
| `payment_success` | method | `views/subscription.py:86` | `def payment_success()` |
| `subscribe` | method | `views/subscription.py:37` | `def subscribe()` |
| `secure_sync` | function | `views/sync.py:29` | `def secure_sync()` |
| `sync_page` | function | `views/sync.py:79` | `def sync_page()` |
| `terms` | function | `views/terms.py:6` | `def terms()` |
| `MFAEnableForm` | class | `views/views.py:15` | `class MFAEnableForm(FlaskForm)` |
| `home` | method | `views/views.py:21` | `def home()` |

