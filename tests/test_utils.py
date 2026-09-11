"""Contract tests for shared utility helpers."""

from __future__ import annotations

from utils.utils import database_path


def test_database_path_prefers_the_configured_path(app):
    with app.app_context():
        assert database_path() == app.config["SQLALCHEMY_DATABASE_PATH"]


def test_database_path_honors_env_outside_a_context(monkeypatch):
    monkeypatch.setenv("QV_USERS_DB", "/tmp/qv-custom.db")
    assert database_path() == "/tmp/qv-custom.db"


def test_database_path_default_outside_a_context(monkeypatch):
    monkeypatch.delenv("QV_USERS_DB", raising=False)
    assert database_path() == "instance/users.db"
