"""Account settings page and the deniable vault JSON API (QV-DENIABLE-1).

The settings page is a normal, universal part of every authenticated
account, regardless of role. It deliberately does not advertise the
deniable vault as a special feature: the page looks the same for everyone,
and the API never tells the caller whether a hidden vault is configured.
That is by design. A deniable vault only protects the user if its presence
leaves no evidence; an obvious "you have a hidden vault" indicator would
make coercion more effective, not less.

Routes:

- ``GET    /account``            : render the account settings page
- ``GET    /api/account/vault``  : return the user's opaque container,
                                   minting an indistinguishable random one
                                   if the account has none yet
- ``PUT    /api/account/vault``  : validate and store a container
- ``DELETE /api/account/vault``  : reset the container to a fresh random one

The server validates container *structure* only; it never decrypts a slot
or sees a passphrase (see :mod:`controllers.deniable_vault`).
"""

from __future__ import annotations

from flask import (
    Blueprint,
    current_app,
    jsonify,
    render_template,
    request,
)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import current_user, login_required

from controllers.deniable_vault import (
    DeniableVaultConfig,
    DeniableVaultController,
    EnvelopeValidationError,
)
from models.deniable_vault import DeniableVaultDB
from utils.security import audit_event, json_csrf_protect


account_bp = Blueprint("account", __name__)
limiter = Limiter(key_func=get_remote_address)


def get_deniable_vault_controller() -> DeniableVaultController:
    """Build a controller bound to the active app's database and config.

    The database path and structural parameters are read from
    ``current_app.config`` so tests (which point the app at a temporary
    database and may override limits) and production share one code path.
    """
    config = DeniableVaultConfig.from_mapping(current_app.config)
    db = DeniableVaultDB(current_app.config["SQLALCHEMY_DATABASE_PATH"])
    return DeniableVaultController(db=db, config=config)


@account_bp.route("/account", methods=["GET"])
@login_required
def settings():
    """Render the account settings page."""
    controller = get_deniable_vault_controller()
    return render_template(
        "account.html",
        user=current_user,
        parameters=controller.config.public_parameters(),
    )


@account_bp.route("/api/account/vault", methods=["GET"])
@login_required
@limiter.limit("30 per minute")
def get_vault():
    """Return the user's container and the build parameters.

    The response always includes an ``envelope`` (a random one is minted on
    first access) and the structural ``parameters``. It never includes a
    "configured" flag: whether the container holds real data is exactly
    what must stay hidden.
    """
    controller = get_deniable_vault_controller()
    envelope = controller.load_or_provision(current_user.username)
    return jsonify(
        {
            "envelope": envelope,
            "parameters": controller.config.public_parameters(),
        }
    )


@account_bp.route("/api/account/vault", methods=["PUT"])
@login_required
@limiter.limit("10 per minute")
@json_csrf_protect
def put_vault():
    """Validate and store a container for the user."""
    data = request.get_json(silent=True) or {}
    envelope = data.get("envelope")
    if envelope is None:
        return jsonify({"success": False, "error": "Missing 'envelope'."}), 400

    controller = get_deniable_vault_controller()
    try:
        controller.save(current_user.username, envelope)
    except EnvelopeValidationError as exc:
        # The rejection reason describes structure, never contents, and the
        # event name is generic so it does not flag the feature in logs.
        audit_event("account_object_rejected", username=current_user.username, reason=str(exc))
        return jsonify({"success": False, "error": str(exc)}), 400

    return jsonify({"success": True})


@account_bp.route("/api/account/vault", methods=["DELETE"])
@login_required
@limiter.limit("10 per minute")
@json_csrf_protect
def delete_vault():
    """Reset the user's container to a fresh random one.

    Reset, not delete: removing the row would distinguish an account that
    deactivated from one that never activated. A random container keeps the
    "every account has one" invariant intact.
    """
    controller = get_deniable_vault_controller()
    controller.reset(current_user.username)
    return jsonify({"success": True})
