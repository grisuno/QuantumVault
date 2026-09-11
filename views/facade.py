"""Cover facade HTTP integration: before-request cover and the gate endpoint.

When the facade is configured, anonymous visitors to the protected pages
see a configurable cover instead of the application, and ``POST /gate``
accepts the secret phrase. A correct phrase stores the signed ticket in
the session and redirects to the ordinary login page; a miss keeps the
cover. Nothing in the response distinguishes a miss from a hit to an
unauthenticated observer.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from flask import Flask, Response, redirect, request, session, url_for
from flask_login import current_user
from flask_wtf.csrf import generate_csrf

from controllers.cover import (
    CoverRenderer,
    CoverService,
    CoverValidationError,
    CustomCoverStore,
)
from controllers.facade import FacadeConfig, FacadeGate, GateOutcome

GATE_TICKET_KEY = "qv_gate_ticket"
GATE_MODE_KEY = "qv_gate_mode"
GATE_ENDPOINT = "/gate"


def register_facade(app: Flask) -> Optional[FacadeGate]:
    """Install the facade on ``app`` when it is enabled and configured."""
    config = FacadeConfig.from_mapping(app.config)
    if not config.gate_configured:
        return None
    gate = FacadeGate.build(config, app.config["SECRET_KEY"])
    service = _build_cover_service(config)

    def render_cover() -> Response:
        body = service.render(generate_csrf(), GATE_ENDPOINT, config.gate_field)
        response = Response(body, status=200, mimetype="text/html")
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.before_request
    def _facade_cover() -> Optional[Response]:
        if not config.hide_login:
            return None
        if request.path not in config.protected_paths:
            return None
        if current_user.is_authenticated:
            return None
        if _ticket_mode(gate) is not None:
            return None
        return render_cover()

    @app.post(GATE_ENDPOINT)
    def facade_gate() -> Response:
        decision = gate.evaluate(request.form.get("q", ""))
        if decision.outcome is GateOutcome.MISS or not decision.ticket:
            return render_cover()
        session[GATE_TICKET_KEY] = decision.ticket
        session[GATE_MODE_KEY] = decision.outcome.value
        return redirect(url_for("auth.login"))

    return gate


def _build_cover_service(config: FacadeConfig) -> CoverService:
    renderer = CoverRenderer()
    store = CustomCoverStore(Path(config.cover_dir), renderer)
    try:
        return CoverService(
            renderer,
            store,
            config.cover_template,
            config.cover_custom_template,
            config.cover_variables(),
        )
    except CoverValidationError:
        return CoverService(renderer, store, config.cover_template, "", {})


def _ticket_mode(gate: FacadeGate) -> Optional[str]:
    token = session.get(GATE_TICKET_KEY)
    mode = gate.ticket.verify(token)
    if mode is None:
        session.pop(GATE_TICKET_KEY, None)
        return None
    session[GATE_MODE_KEY] = mode
    return mode
