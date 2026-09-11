"""QV-FACADE-2 cover template catalog, sanitization, and sandboxed rendering.

The facade's public page is operator-configurable. Five innocuous
templates ship with the application, and an operator may place a custom
Jinja template in the cover directory and select it. Every variable is
untrusted input: it is bounded, stripped of control and spoofing
characters, and rendered with autoescaping so a variable can never inject
markup. Template source is rendered in a sandbox with a closed variable
allow-list; scripts, event handlers, external form actions, template
imports, and attribute traversal are rejected before rendering.
"""

from __future__ import annotations

import os
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Optional

from jinja2 import StrictUndefined, TemplateError, TemplateSyntaxError, meta
from jinja2.sandbox import SandboxedEnvironment


class CoverValidationError(ValueError):
    """Raised when a cover variable violates its contract."""


class CoverTemplateError(ValueError):
    """Raised when a cover template violates the template contract."""

CUSTOM_TEMPLATE_ID = "custom"
DEFAULT_TEMPLATE_ID = "search_portal"

_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)
_FILENAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

_MAX_TITLE_LENGTH = 120
_MAX_TAGLINE_LENGTH = 240
_MAX_BODY_LENGTH = 4000
_MAX_FOOTER_LENGTH = 320
_MAX_EMAIL_LENGTH = 254
_MAX_LABEL_LENGTH = 120
_MAX_TEMPLATE_BYTES = 65536
_ALLOWED_EXTENSIONS = (".html", ".htm", ".jinja", ".jinja2")
_ALLOWED_FILTERS = ("escape", "e", "upper", "lower", "trim", "capitalize")

_FORBIDDEN_TOKENS = (
    "{% import",
    "{% from",
    "{% include",
    "{% extends",
    "{% macro",
    "self.",
    "__class__",
    "__globals__",
    "__subclasses__",
    "cycler",
    "joiner",
    "namespace",
    "<script",
    "</script",
    "javascript:",
    "onerror=",
    "onload=",
    "onclick=",
    "onmouseover=",
    "onfocus=",
    "onblur=",
    "<iframe",
    "<object",
    "<embed",
    "<meta http-equiv",
    "srcdoc=",
    'action="http',
    "action='http",
    "action=//",
    'action="//',
)

_DEFAULT_VARIABLES: dict[str, str] = {
    "brand": "Findex",
    "title": "Findex",
    "tagline": "Search the web",
    "headline": "Findex",
    "body_text": "Search the web for pages, images, and answers.",
    "footer_text": "Findex is a free service.",
    "contact_email": "support@example.org",
    "newsletter_label": "Search",
    "newsletter_action": "Search",
}

_SYSTEM_VARIABLES = frozenset({"csrf_token", "gate_endpoint", "gate_field"})


@dataclass(frozen=True)
class CoverVariableSpec:
    """Bounds for one operator-configurable cover variable."""

    name: str
    max_length: int

    @property
    def multiline(self) -> bool:
        """Return whether the variable preserves line breaks."""
        return self.name in _MULTILINE_VARIABLES

    @property
    def is_email(self) -> bool:
        """Return whether the variable must be a valid email address."""
        return self.name in _EMAIL_VARIABLES


_MULTILINE_VARIABLES = frozenset({"body_text", "footer_text"})
_EMAIL_VARIABLES = frozenset({"contact_email"})

_COVER_VARIABLE_SPECS: tuple[CoverVariableSpec, ...] = (
    CoverVariableSpec("brand", _MAX_TITLE_LENGTH),
    CoverVariableSpec("title", _MAX_TITLE_LENGTH),
    CoverVariableSpec("tagline", _MAX_TAGLINE_LENGTH),
    CoverVariableSpec("headline", _MAX_TITLE_LENGTH),
    CoverVariableSpec("body_text", _MAX_BODY_LENGTH),
    CoverVariableSpec("footer_text", _MAX_FOOTER_LENGTH),
    CoverVariableSpec("contact_email", _MAX_EMAIL_LENGTH),
    CoverVariableSpec("newsletter_label", _MAX_LABEL_LENGTH),
    CoverVariableSpec("newsletter_action", _MAX_LABEL_LENGTH),
)
_COVER_VARIABLE_NAMES = frozenset(spec.name for spec in _COVER_VARIABLE_SPECS)


@dataclass(frozen=True)
class CoverTemplate:
    """One built-in cover page definition."""

    template_id: str
    display_name: str
    source: str


def _strip_unsafe(value: str) -> str:
    output: list[str] = []
    for character in value:
        if character in ("\n", "\t"):
            output.append(character)
            continue
        if unicodedata.category(character).startswith("C"):
            continue
        output.append(character)
    return "".join(output)


def _sanitize_text(name: str, value: str, spec: CoverVariableSpec) -> str:
    normalized = unicodedata.normalize("NFKC", value)
    cleaned = _strip_unsafe(normalized)
    if spec.multiline:
        cleaned = "\n".join(line.rstrip() for line in cleaned.split("\n")).strip()
    else:
        cleaned = " ".join(cleaned.split())
    if len(cleaned) > spec.max_length:
        raise CoverValidationError(f"{name} exceeds {spec.max_length} characters")
    return cleaned


def _sanitize_email(name: str, value: str) -> str:
    candidate = " ".join(_strip_unsafe(unicodedata.normalize("NFKC", value)).split()).lower()
    if len(candidate) > _MAX_EMAIL_LENGTH or not _EMAIL_RE.match(candidate):
        raise CoverValidationError(f"{name} is not a valid email address")
    return candidate


def sanitize_cover_variables(raw: Mapping[str, Any]) -> dict[str, str]:
    """Return a fully populated, sanitized cover variable map."""
    if not isinstance(raw, Mapping):
        raise CoverValidationError("cover variables must be a mapping")
    unknown = set(raw) - _COVER_VARIABLE_NAMES
    if unknown:
        raise CoverValidationError(f"unknown cover variables: {sorted(unknown)}")
    result: dict[str, str] = {}
    for spec in _COVER_VARIABLE_SPECS:
        candidate = raw.get(spec.name)
        if candidate is None or (isinstance(candidate, str) and not candidate.strip()):
            candidate = _DEFAULT_VARIABLES[spec.name]
        if not isinstance(candidate, str):
            raise CoverValidationError(f"{spec.name} must be a string")
        result[spec.name] = (
            _sanitize_email(spec.name, candidate)
            if spec.is_email
            else _sanitize_text(spec.name, candidate, spec)
        )
    return result


class CoverRenderer:
    """Validate and render cover templates in a sandbox with a closed context."""

    def __init__(self) -> None:
        """Create the sandboxed environment used for every cover template."""
        self._environment = SandboxedEnvironment(
            autoescape=True,
            undefined=StrictUndefined,
            auto_reload=False,
            cache_size=0,
        )
        self._environment.globals = {}
        self._environment.filters = {
            name: self._environment.filters[name]
            for name in _ALLOWED_FILTERS
            if name in self._environment.filters
        }

    @property
    def allowed_variables(self) -> frozenset[str]:
        """Return the closed set of variable names a cover may reference."""
        return _COVER_VARIABLE_NAMES | _SYSTEM_VARIABLES

    def validate(self, source: str) -> frozenset[str]:
        """Return referenced variables, or raise when the template is unsafe."""
        if not isinstance(source, str) or not source.strip():
            raise CoverTemplateError("cover template source must be non-empty")
        lowered = source.lower()
        for token in _FORBIDDEN_TOKENS:
            if token.lower() in lowered:
                raise CoverTemplateError(f"cover template uses forbidden construct: {token}")
        try:
            parsed = self._environment.parse(source)
        except TemplateSyntaxError as exc:
            raise CoverTemplateError(f"cover template syntax error: {exc.message}") from exc
        referenced = frozenset(meta.find_undeclared_variables(parsed))
        unknown = referenced - self.allowed_variables
        if unknown:
            raise CoverTemplateError(f"cover template references unknown variables: {sorted(unknown)}")
        return referenced

    def render(self, source: str, variables: Mapping[str, str], system: Mapping[str, str]) -> str:
        """Render a validated template with sanitized variables and system values."""
        self.validate(source)
        context = {name: variables.get(name, "") for name in _COVER_VARIABLE_NAMES}
        context.update({name: system.get(name, "") for name in _SYSTEM_VARIABLES})
        try:
            return self._environment.from_string(source).render(**context)
        except TemplateError as exc:
            raise CoverTemplateError(f"cover template failed to render: {exc}") from exc


class CustomCoverStore:
    """Persist and load operator cover templates inside an isolated directory."""

    def __init__(self, directory: Path, renderer: CoverRenderer) -> None:
        """Bind the store to its directory and the validating renderer."""
        self._directory = directory
        self._renderer = renderer

    @property
    def directory(self) -> Path:
        """Return the absolute template directory."""
        return self._directory

    def store(self, filename: object, data: object) -> str:
        """Validate and persist an uploaded template, returning its stored name."""
        safe_name = self._safe_name(filename)
        extension = Path(safe_name).suffix.lower()
        if extension not in _ALLOWED_EXTENSIONS:
            raise CoverTemplateError(f"cover template extension {extension!r} is not allowed")
        if not isinstance(data, (bytes, bytearray)) or not data:
            raise CoverTemplateError("cover template payload must be non-empty bytes")
        if len(data) > _MAX_TEMPLATE_BYTES:
            raise CoverTemplateError(f"cover template exceeds {_MAX_TEMPLATE_BYTES} bytes")
        try:
            source = bytes(data).decode("utf-8")
        except UnicodeDecodeError as exc:
            raise CoverTemplateError("cover template must be valid UTF-8") from exc
        self._renderer.validate(source)
        self._directory.mkdir(parents=True, exist_ok=True)
        target = self._directory / safe_name
        temporary = target.with_suffix(target.suffix + ".tmp")
        temporary.write_text(source, encoding="utf-8")
        os.chmod(temporary, 0o600)
        os.replace(temporary, target)
        return safe_name

    def load(self, name: object) -> str:
        """Read and validate a stored template, refusing path escape."""
        path = self._resolve(name)
        if not path.is_file():
            raise CoverTemplateError("cover template not found")
        source = path.read_text(encoding="utf-8")
        self._renderer.validate(source)
        return source

    def list_names(self) -> list[str]:
        """Return the sorted names of stored templates."""
        if not self._directory.is_dir():
            return []
        return sorted(
            entry.name
            for entry in self._directory.iterdir()
            if entry.is_file() and entry.suffix.lower() in _ALLOWED_EXTENSIONS
        )

    def _safe_name(self, name: object) -> str:
        if not isinstance(name, str):
            raise CoverTemplateError("cover template name must be a string")
        candidate = name.replace("\\", "/").rsplit("/", 1)[-1].strip()
        if candidate.startswith(".") or not _FILENAME_RE.match(candidate):
            raise CoverTemplateError("cover template name is not a safe filename")
        return candidate

    def _resolve(self, name: object) -> Path:
        safe_name = self._safe_name(name)
        candidate = (self._directory / safe_name).resolve()
        base = self._directory.resolve()
        if candidate.parent != base:
            raise CoverTemplateError("cover template path escapes the store")
        return candidate


_CATALOG: tuple[CoverTemplate, ...] = (
    CoverTemplate(
        "search_portal",
        "Search portal",
        """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{{ title }}</title>
<style>
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:#fff;color:#202124}
header{padding:1.5rem 2rem;border-bottom:1px solid #e8eaed;font-size:1.5rem;font-weight:700;color:#4285f4}
main{max-width:42rem;margin:12vh auto 0;padding:0 1.5rem;text-align:center}
h1{font-size:2.25rem;margin:0 0 .5rem}.tagline{color:#5f6368;margin:0 0 2rem}
form{display:flex;gap:.5rem}input[type=search]{flex:1;padding:.85rem 1.1rem;border:1px solid #dadce0;border-radius:24px}
button{padding:.85rem 1.5rem;border:1px solid #dadce0;border-radius:24px;background:#f8f9fa;cursor:pointer}
footer{margin-top:4rem;padding:1.5rem;text-align:center;color:#70757a;font-size:.8rem}
</style></head><body>
<header>{{ brand }}</header>
<main><h1>{{ headline }}</h1><p class="tagline">{{ tagline }}</p>
<form method="post" action="{{ gate_endpoint }}" autocomplete="off">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
<input type="search" name="{{ gate_field }}" placeholder="{{ tagline }}" aria-label="{{ tagline }}" autofocus>
<button type="submit">{{ newsletter_action }}</button></form></main>
<footer>{{ footer_text }} <a href="mailto:{{ contact_email }}">{{ contact_email }}</a></footer>
</body></html>""",
    ),
    CoverTemplate(
        "newsletter",
        "Newsletter landing",
        """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{{ title }}</title>
<style>
body{margin:0;font-family:Georgia,serif;background:#f7f4ee;color:#1a1a1a}
header{border-bottom:3px double #c9c2b6;padding:2rem 1.5rem;text-align:center}
.brand{letter-spacing:.35em;text-transform:uppercase;font-size:.8rem}
h1{margin:.4rem 0;font-size:2.6rem}.sub{font-style:italic;color:#5a544b}
main{max-width:48rem;margin:0 auto;padding:2rem 1.5rem}
article{white-space:pre-line;line-height:1.7}
.subscribe{margin-top:2.5rem;border-top:1px solid #c9c2b6;padding-top:1.5rem}
form{display:flex;gap:.6rem;flex-wrap:wrap}input{flex:1;padding:.6rem .8rem;border:1px solid #b7afa2}
button{padding:.6rem 1rem;background:#1a1a1a;color:#f7f4ee;border:0;cursor:pointer}
footer{border-top:1px solid #c9c2b6;margin-top:3rem;padding:1.5rem;text-align:center;font-size:.85rem;color:#5a544b}
</style></head><body>
<header><div class="brand">{{ brand }}</div><h1>{{ headline }}</h1><p class="sub">{{ tagline }}</p></header>
<main><article>{{ body_text }}</article>
<section class="subscribe"><h2>{{ newsletter_label }}</h2>
<form method="post" action="{{ gate_endpoint }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
<input type="email" name="{{ gate_field }}" placeholder="{{ contact_email }}" autocomplete="email" required>
<button type="submit">{{ newsletter_action }}</button></form></section></main>
<footer>{{ footer_text }} <a href="mailto:{{ contact_email }}">{{ contact_email }}</a></footer>
</body></html>""",
    ),
    CoverTemplate(
        "tech_blog",
        "Technology blog",
        """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{{ title }}</title>
<style>
body{margin:0;font-family:'Segoe UI',Roboto,Arial,sans-serif;background:#0e1116;color:#e6edf3}
header{padding:2rem 1.5rem;background:#161b22;border-bottom:1px solid #2a313a}
.brand{color:#4c8bf5;font-weight:700;letter-spacing:.08em}
main{max-width:48rem;margin:0 auto;padding:2rem 1.5rem}
.post{white-space:pre-line;line-height:1.75}
.box{margin-top:2.5rem;background:#161b22;border:1px solid #2a313a;border-radius:10px;padding:1.5rem}
form{display:flex;gap:.6rem;flex-wrap:wrap}input{flex:1;padding:.65rem .8rem;border-radius:6px;border:1px solid #2a313a;background:#0b0e13;color:#e6edf3}
button{padding:.65rem 1rem;border-radius:6px;border:0;background:#4c8bf5;color:#fff;cursor:pointer}
footer{margin-top:3rem;padding:1.5rem;border-top:1px solid #2a313a;color:#9aa7b4;font-size:.85rem;text-align:center}
</style></head><body>
<header><div class="brand">{{ brand }}</div><h1>{{ headline }}</h1><p>{{ tagline }}</p></header>
<main><div class="post">{{ body_text }}</div>
<section class="box"><h2>{{ newsletter_label }}</h2>
<form method="post" action="{{ gate_endpoint }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
<input type="text" name="{{ gate_field }}" placeholder="{{ tagline }}" required>
<button type="submit">{{ newsletter_action }}</button></form></section></main>
<footer>{{ footer_text }} <a href="mailto:{{ contact_email }}">{{ contact_email }}</a></footer>
</body></html>""",
    ),
    CoverTemplate(
        "art_gallery",
        "Art gallery",
        """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{{ title }}</title>
<style>
body{margin:0;font-family:'Helvetica Neue',Arial,sans-serif;background:#fbfbf9;color:#111}
header{padding:4rem 1.5rem 2rem;text-align:center}
.brand{text-transform:uppercase;letter-spacing:.5em;font-size:.7rem;color:#7b7b76}
h1{font-size:3rem;font-weight:300;margin:1rem 0 .5rem}.sub{color:#7b7b76}
main{max-width:44rem;margin:0 auto;padding:1rem 1.5rem 3rem}
figure{white-space:pre-line;line-height:1.9;border-left:1px solid #111;padding-left:1.5rem}
form{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:2.5rem}
input{flex:1;padding:.7rem .9rem;border:1px solid #111;background:transparent}
button{padding:.7rem 1rem;background:#111;color:#fbfbf9;border:0;cursor:pointer}
footer{margin-top:3rem;padding:2rem;text-align:center;color:#7b7b76;font-size:.8rem;border-top:1px solid #e3e3df}
</style></head><body>
<header><div class="brand">{{ brand }}</div><h1>{{ headline }}</h1><p class="sub">{{ tagline }}</p></header>
<main><figure>{{ body_text }}</figure>
<form method="post" action="{{ gate_endpoint }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
<input type="text" name="{{ gate_field }}" placeholder="{{ tagline }}">
<button type="submit">{{ newsletter_action }}</button></form></main>
<footer>{{ footer_text }} <a href="mailto:{{ contact_email }}">{{ contact_email }}</a></footer>
</body></html>""",
    ),
    CoverTemplate(
        "nonprofit",
        "Nonprofit organization",
        """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{{ title }}</title>
<style>
body{margin:0;font-family:'Trebuchet MS',Verdana,sans-serif;background:#fff;color:#14231d}
header{padding:2.5rem 1.5rem;background:linear-gradient(135deg,#1f6f54,#2f8f6d);color:#fff}
.brand{text-transform:uppercase;letter-spacing:.2em;font-size:.75rem;opacity:.9}
main{max-width:50rem;margin:0 auto;padding:2rem 1.5rem}
.mission{white-space:pre-line;line-height:1.8;background:#eef6f1;border-radius:12px;padding:1.5rem}
form{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:2.5rem}
input{flex:1;padding:.7rem .9rem;border-radius:8px;border:1px solid #bcd6c9}
button{padding:.7rem 1rem;border-radius:8px;border:0;background:#1f6f54;color:#fff;cursor:pointer}
footer{margin-top:3rem;padding:2rem;background:#eef6f1;text-align:center;color:#5c7568;font-size:.85rem}
</style></head><body>
<header><div class="brand">{{ brand }}</div><h1>{{ headline }}</h1><p>{{ tagline }}</p></header>
<main><div class="mission">{{ body_text }}</div>
<form method="post" action="{{ gate_endpoint }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
<input type="email" name="{{ gate_field }}" placeholder="{{ contact_email }}">
<button type="submit">{{ newsletter_action }}</button></form></main>
<footer>{{ footer_text }} <a href="mailto:{{ contact_email }}">{{ contact_email }}</a></footer>
</body></html>""",
    ),
)

CATALOG_BY_ID: dict[str, CoverTemplate] = {template.template_id: template for template in _CATALOG}
CATALOG_IDS: tuple[str, ...] = tuple(CATALOG_BY_ID)


def catalog() -> tuple[CoverTemplate, ...]:
    """Return the built-in cover template catalog."""
    return _CATALOG


class CoverService:
    """Select, validate, and render the configured cover page."""

    def __init__(
        self,
        renderer: CoverRenderer,
        custom_store: CustomCoverStore,
        template_id: str,
        custom_name: str,
        variables: Mapping[str, Any],
    ) -> None:
        """Bind the service to a template selection and variable payload."""
        self._renderer = renderer
        self._custom_store = custom_store
        self._template_id = template_id
        self._custom_name = custom_name
        self._variables = sanitize_cover_variables(variables)

    @property
    def variables(self) -> dict[str, str]:
        """Return the sanitized variable map."""
        return dict(self._variables)

    def render(self, csrf_token: str, gate_endpoint: str, gate_field: str) -> str:
        """Render the selected cover with system values injected by the server."""
        source = self._source()
        system = {
            "csrf_token": csrf_token,
            "gate_endpoint": gate_endpoint,
            "gate_field": gate_field,
        }
        return self._renderer.render(source, self._variables, system)

    def _source(self) -> str:
        if self._template_id == CUSTOM_TEMPLATE_ID and self._custom_name:
            try:
                return self._custom_store.load(self._custom_name)
            except CoverTemplateError:
                return CATALOG_BY_ID[DEFAULT_TEMPLATE_ID].source
        template = CATALOG_BY_ID.get(self._template_id)
        if template is None:
            template = CATALOG_BY_ID[DEFAULT_TEMPLATE_ID]
        return template.source
