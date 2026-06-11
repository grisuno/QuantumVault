"""Tests for utils/security.py: audit log redaction and JSON CSRF protection."""

from __future__ import annotations

import json

from flask_wtf.csrf import generate_csrf

from utils.security import audit_event, json_csrf_protect


def test_audit_event_includes_ip_and_ua_by_default(app, audit_records, monkeypatch):
    monkeypatch.delenv("QV_AUDIT_LOG_IP", raising=False)
    monkeypatch.delenv("QV_AUDIT_LOG_UA", raising=False)

    with app.test_request_context(
        "/", environ_base={"REMOTE_ADDR": "203.0.113.5"},
        headers={"User-Agent": "pytest-agent/1.0"},
    ):
        audit_event("test_event")

    record = json.loads(audit_records[-1])
    assert record["event"] == "test_event"
    assert record["ip"] == "203.0.113.5"
    assert record["ua"] == "pytest-agent/1.0"
    assert "cid" in record


def test_audit_event_redacts_ip_and_ua_when_disabled(app, audit_records, monkeypatch):
    monkeypatch.setenv("QV_AUDIT_LOG_IP", "0")
    monkeypatch.setenv("QV_AUDIT_LOG_UA", "0")

    with app.test_request_context(
        "/", environ_base={"REMOTE_ADDR": "203.0.113.5"},
        headers={"User-Agent": "pytest-agent/1.0"},
    ):
        audit_event("test_event")

    record = json.loads(audit_records[-1])
    assert record["ip"] is None
    assert record["ua"] is None
    assert "cid" in record


def test_json_csrf_protect_rejects_missing_token(app):
    @json_csrf_protect
    def view():
        return "ok"

    with app.test_request_context("/", method="POST"):
        response = view()

    status = response[1] if isinstance(response, tuple) else response.status_code
    assert status == 403


def test_json_csrf_protect_accepts_valid_header_token(app):
    @json_csrf_protect
    def view():
        return "ok"

    from flask import session

    with app.test_request_context("/"):
        token = generate_csrf()
        session_csrf_token = session["csrf_token"]

    with app.test_request_context(
        "/", method="POST", headers={"X-CSRFToken": token}
    ):
        session["csrf_token"] = session_csrf_token
        result = view()

    assert result == "ok"


def test_json_csrf_protect_passes_get_through_without_token(app):
    @json_csrf_protect
    def view():
        return "ok"

    with app.test_request_context("/", method="GET"):
        assert view() == "ok"
