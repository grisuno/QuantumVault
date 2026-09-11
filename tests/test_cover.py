"""Specification tests for the QV-FACADE-2 configurable cover templates.

Behaviour is specified per collaborator (catalog, sanitizer, renderer,
custom store, service) and end-to-end through the HTTP cover flow, so a
regression in any layer fails a focused test rather than only the surface.
"""

from __future__ import annotations

import pytest

from app_factory import create_app
from controllers.cover import (
    CATALOG_IDS,
    CUSTOM_TEMPLATE_ID,
    DEFAULT_TEMPLATE_ID,
    CoverRenderer,
    CoverService,
    CoverTemplateError,
    CoverValidationError,
    CustomCoverStore,
    _COVER_VARIABLE_SPECS,
    catalog,
    sanitize_cover_variables,
)
from controllers.facade import FacadeConfig, GatePhraseHasher

REAL_PHRASE = "correct horse battery"
SECRET_KEY = "cover-test-secret-key-not-for-production"
CUSTOM_OK = (
    b"<!doctype html><html><body><h1>{{ brand }}</h1>"
    b"<form method=\"post\" action=\"{{ gate_endpoint }}\">"
    b"<input type=\"hidden\" name=\"csrf_token\" value=\"{{ csrf_token }}\">"
    b"<input name=\"{{ gate_field }}\"><button>{{ newsletter_action }}</button>"
    b"</form></body></html>"
)
CUSTOM_MARKER = CUSTOM_OK.replace(b"<h1>{{ brand }}</h1>", b"<h1>ZZCUSTOM {{ brand }}</h1>")
MAX_TEMPLATE_BYTES = 65536


@pytest.fixture
def fast_hasher() -> GatePhraseHasher:
    return GatePhraseHasher(time_cost=1, memory_cost=8, parallelism=1, hash_len=16, salt_len=16)


@pytest.fixture
def renderer() -> CoverRenderer:
    return CoverRenderer()


@pytest.fixture
def store(tmp_path, renderer) -> CustomCoverStore:
    return CustomCoverStore(tmp_path / "cover", renderer)


def _facade_overrides(fast_hasher, **extra):
    overrides = {
        "TESTING": True,
        "WTF_CSRF_SSL_STRICT": False,
        "QV_FACADE_ENABLED": "1",
        "QV_FACADE_GATE_HASH": fast_hasher.hash(REAL_PHRASE),
        "QV_FACADE_COVER_BRAND": "Findex",
    }
    overrides.update(extra)
    return overrides


def _client(tmp_path, fast_hasher, **extra):
    application = create_app(
        config_overrides={
            "SQLALCHEMY_DATABASE_PATH": str(tmp_path / "users.db"),
            **_facade_overrides(fast_hasher, **extra),
        },
        security_overrides={
            "force_https": False,
            "content_security_policy": None,
            "strict_transport_security": False,
        },
    )
    return application.test_client()


class TestCatalog:
    def test_catalog_ships_five_distinct_templates(self):
        templates = catalog()
        assert len(templates) == 5
        assert len(CATALOG_IDS) == len(set(CATALOG_IDS))

    def test_default_template_exists(self):
        assert DEFAULT_TEMPLATE_ID in CATALOG_IDS

    def test_every_template_validates_and_renders(self, renderer):
        variables = sanitize_cover_variables({})
        system = {"csrf_token": "tok", "gate_endpoint": "/gate", "gate_field": "q"}
        for template in catalog():
            renderer.validate(template.source)
            rendered = renderer.render(template.source, variables, system)
            assert "/gate" in rendered
            assert "csrf_token" in rendered
            assert "QuantumVault" not in rendered


class TestSanitizer:
    def test_empty_payload_fills_defaults(self):
        result = sanitize_cover_variables({})
        assert result["brand"] == "Findex"
        assert result["contact_email"] == "support@example.org"

    def test_unknown_variable_is_rejected(self):
        with pytest.raises(CoverValidationError):
            sanitize_cover_variables({"unknown": "x"})

    def test_invalid_email_is_rejected(self):
        with pytest.raises(CoverValidationError):
            sanitize_cover_variables({"contact_email": "not-an-email"})

    def test_control_characters_are_stripped(self):
        result = sanitize_cover_variables({"brand": "Fin\x00dex\x07"})
        assert result["brand"] == "Findex"

    def test_overlong_value_is_rejected(self):
        with pytest.raises(CoverValidationError):
            sanitize_cover_variables({"tagline": "x" * 5000})

    def test_multiline_body_preserves_line_breaks(self):
        result = sanitize_cover_variables({"body_text": "line1\nline2"})
        assert "\n" in result["body_text"]

    def test_single_line_value_flattens_line_breaks(self):
        result = sanitize_cover_variables({"brand": "line1\nline2"})
        assert result["brand"] == "line1 line2"

    @pytest.mark.parametrize(
        "spec", [spec for spec in _COVER_VARIABLE_SPECS if not spec.is_email],
        ids=lambda spec: spec.name,
    )
    def test_multiline_flag_matches_spec(self, spec):
        result = sanitize_cover_variables({spec.name: "first\nsecond"})[spec.name]
        if spec.multiline:
            assert "\n" in result
        else:
            assert "\n" not in result

    def test_text_boundary_is_inclusive(self):
        exact = "x" * 120
        assert sanitize_cover_variables({"brand": exact})["brand"] == exact
        with pytest.raises(CoverValidationError):
            sanitize_cover_variables({"brand": exact + "x"})

    def test_email_boundary_is_inclusive(self):
        exact = "a" * 64 + "@" + "b" * 63 + "." + "c" * 63 + "." + "d" * 61
        assert len(exact) == 254
        assert sanitize_cover_variables({"contact_email": exact})["contact_email"] == exact
        with pytest.raises(CoverValidationError):
            sanitize_cover_variables({"contact_email": "a" * 64 + "@" + "b" * 63 + "." + "c" * 63 + "." + "d" * 62})


class TestRenderer:
    def test_variables_are_autoescaped(self, renderer):
        variables = sanitize_cover_variables({"brand": "<b>X</b>"})
        rendered = renderer.render("{{ brand }}", variables, {})
        assert "&lt;b&gt;" in rendered

    def test_unknown_variable_is_rejected(self, renderer):
        with pytest.raises(CoverTemplateError):
            renderer.validate("{{ secret }}")

    def test_dunder_access_is_rejected(self, renderer):
        with pytest.raises(CoverTemplateError):
            renderer.validate('{{ "".__class__ }}')

    def test_inline_script_is_rejected(self, renderer):
        with pytest.raises(CoverTemplateError):
            renderer.validate("<script>alert(1)</script>")

    def test_external_form_action_is_rejected(self, renderer):
        with pytest.raises(CoverTemplateError):
            renderer.validate('<form action="https://evil.example"></form>')

    def test_template_import_is_rejected(self, renderer):
        with pytest.raises(CoverTemplateError):
            renderer.validate("{% import 'os' as os %}")

    def test_blank_source_is_rejected(self, renderer):
        with pytest.raises(CoverTemplateError):
            renderer.validate("   ")


class TestCustomStore:
    def test_valid_template_round_trips(self, store):
        name = store.store("custom.html", CUSTOM_OK)
        assert name == "custom.html"
        assert "custom.html" in store.list_names()
        assert "gate_endpoint" in store.load(name)

    def test_bad_extension_is_rejected(self, store):
        with pytest.raises(CoverTemplateError):
            store.store("custom.txt", CUSTOM_OK)

    def test_oversize_template_is_rejected(self, store):
        with pytest.raises(CoverTemplateError):
            store.store("big.html", b"x" * 70000)

    def test_path_traversal_is_neutralized(self, store):
        name = store.store("../../evil.html", CUSTOM_OK)
        assert name == "evil.html"
        assert (store.directory / name).resolve().parent == store.directory.resolve()

    def test_script_template_is_rejected(self, store):
        with pytest.raises(CoverTemplateError):
            store.store("x.html", b"<html><script>alert(1)</script></html>")

    def test_missing_template_raises(self, store):
        with pytest.raises(CoverTemplateError):
            store.load("missing.html")

    def test_non_bytes_payload_is_rejected(self, store):
        with pytest.raises(CoverTemplateError):
            store.store("x.html", "not bytes")

    def test_disallowed_character_filename_is_rejected(self, store):
        with pytest.raises(CoverTemplateError):
            store.store("a$b.html", CUSTOM_OK)

    def test_exactly_max_size_is_accepted(self, store):
        padded = CUSTOM_OK + b" " * (MAX_TEMPLATE_BYTES - len(CUSTOM_OK))
        assert store.store("max.html", padded) == "max.html"

    def test_nested_directory_is_created(self, tmp_path, renderer):
        nested = CustomCoverStore(tmp_path / "a" / "b" / "cover", renderer)
        assert nested.store("one.html", CUSTOM_OK) == "one.html"

    def test_two_templates_share_the_store(self, store):
        store.store("one.html", CUSTOM_OK)
        assert store.store("two.html", CUSTOM_OK) == "two.html"
        assert store.list_names() == ["one.html", "two.html"]

    def test_directory_with_allowed_suffix_is_ignored(self, store):
        store.directory.mkdir(parents=True, exist_ok=True)
        (store.directory / "decoy.html").mkdir()
        assert "decoy.html" not in store.list_names()


class TestCoverService:
    def test_selects_a_builtin_template(self, renderer, store):
        service = CoverService(renderer, store, "tech_blog", "", {"brand": "Acme"})
        rendered = service.render("tok", "/gate", "q")
        assert "Acme" in rendered

    def test_unknown_template_falls_back_to_default(self, renderer, store):
        service = CoverService(renderer, store, "does-not-exist", "", {})
        rendered = service.render("tok", "/gate", "q")
        assert "Findex" in rendered

    def test_missing_custom_template_falls_back_to_default(self, renderer, store):
        service = CoverService(renderer, store, CUSTOM_TEMPLATE_ID, "ghost.html", {})
        rendered = service.render("tok", "/gate", "q")
        assert "Findex" in rendered

    def test_custom_template_is_rendered(self, renderer, store):
        name = store.store("mine.html", CUSTOM_OK)
        service = CoverService(renderer, store, CUSTOM_TEMPLATE_ID, name, {"brand": "Mine"})
        rendered = service.render("tok", "/gate", "q")
        assert "Mine" in rendered
        assert "/gate" in rendered

    def test_builtin_selection_ignores_a_custom_name(self, renderer, store):
        name = store.store("mine.html", CUSTOM_MARKER)
        service = CoverService(renderer, store, "tech_blog", name, {"brand": "Acme"})
        rendered = service.render("tok", "/gate", "q")
        assert "ZZCUSTOM" not in rendered
        assert "Acme" in rendered

    def test_custom_selection_renders_the_custom_marker(self, renderer, store):
        name = store.store("mine.html", CUSTOM_MARKER)
        service = CoverService(renderer, store, CUSTOM_TEMPLATE_ID, name, {"brand": "Acme"})
        assert "ZZCUSTOM" in service.render("tok", "/gate", "q")


class TestCoverHttp:
    def test_default_cover_selects_search_portal(self, tmp_path, fast_hasher):
        client = _client(tmp_path, fast_hasher)
        response = client.get("/login")
        assert response.status_code == 200
        assert b"Findex" in response.data

    def test_configured_template_is_served(self, tmp_path, fast_hasher):
        client = _client(
            tmp_path,
            fast_hasher,
            QV_FACADE_COVER_TEMPLATE="newsletter",
            QV_FACADE_COVER_BODY="Community reporting since 1999",
        )
        response = client.get("/login")
        assert response.status_code == 200
        assert b"Community reporting since 1999" in response.data

    def test_gate_still_works_with_configured_template(self, tmp_path, fast_hasher):
        client = _client(
            tmp_path, fast_hasher, QV_FACADE_COVER_TEMPLATE="nonprofit"
        )
        token = client.get("/api/csrf-token").get_json()["csrf_token"]
        response = client.post("/gate", data={"q": REAL_PHRASE, "csrf_token": token})
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/login")
