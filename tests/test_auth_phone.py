"""Regression tests for the phone-verification page and resend route.

The verify-phone template links its "Resend Verification Code" button to
``auth.resend_phone_verification``. Before that endpoint existed, simply
rendering the page raised a Jinja ``BuildError`` (HTTP 500). These tests
pin both the render and the endpoint registration.

The resend POST itself is not invoked here: like every auth route it
constructs an ``AuthController``, which opens a Redis-backed SRP session
store, and the test environment has no Redis (``STORAGE_URI=memory://``).
Confirming the endpoint is registered is enough to prove the template's
``url_for`` resolves, which is the bug under test.
"""

from __future__ import annotations


def test_verify_phone_page_renders(client):
    """GET /verify_phone must render without a url_for BuildError."""
    response = client.get("/verify_phone?username=alice")
    assert response.status_code == 200
    assert b"Verify Your Phone Number" in response.data


def test_resend_endpoint_is_registered(app):
    """The resend endpoint the template links to must exist."""
    endpoints = {rule.endpoint for rule in app.url_map.iter_rules()}
    assert "auth.resend_phone_verification" in endpoints


def test_resend_route_accepts_only_post(app):
    """The resend endpoint is POST-only so a GET cannot trigger an SMS."""
    methods = set()
    for rule in app.url_map.iter_rules():
        if rule.endpoint == "auth.resend_phone_verification":
            methods = rule.methods
    assert "POST" in methods
    assert "GET" not in methods
