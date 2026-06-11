"""Local development entry point.

This script exists for the ``make run`` workflow: the Werkzeug dev
server with SSL on the loopback port. It is the only place in the
codebase where the dev server is started. Production deployments use
``wsgi.py`` and gunicorn instead.

The Werkzeug interactive debugger is intentionally NOT enabled: even
with ``FLASK_DEBUG=1`` we never want the debug PIN surface exposed on
a network-reachable port. To get a debugger for local work, run the
app under an IDE debugger against this file.
"""

import os
import sys

from app_factory import create_app
from utils.utils import Config, load_payload


def main() -> None:
    config = Config(load_payload())

    # Refuse to start with the Werkzeug debug PIN if the operator
    # accidentally flips FLASK_DEBUG=1 on a network-reachable interface.
    debug = os.environ.get("FLASK_DEBUG") == "1" and not _is_production_like()

    cert = config.cert
    key = config.key
    if not (os.path.exists(cert) and os.path.exists(key)):
        sys.stderr.write(
            f"FATAL: SSL material missing. Expected cert={cert!r} key={key!r}\n"
            "Generate self-signed material with: openssl req -x509 -newkey rsa:2048 "
            "-nodes -keyout key.pem -out cert.pem -days 365 -subj '/CN=localhost'\n"
        )
        sys.exit(1)

    upload_folder = os.environ.get("QV_UPLOAD_FOLDER", "users")
    os.makedirs("instance", exist_ok=True, mode=0o700)
    os.makedirs(upload_folder, exist_ok=True, mode=0o700)

    app = create_app()
    # use_reloader=False keeps the Werkzeug auto-reloader off in dev too:
    # the previous behaviour reloaded the process on every file change,
    # which made the @login_manager.user_loader closure flip and the
    # SRP sessions in Redis go stale. The developer can run with
    # FLASK_DEBUG_RELOAD=1 explicitly if they want hot reload.
    use_reloader = os.environ.get("FLASK_DEBUG_RELOAD") == "1"
    app.run(
        debug=debug,
        host=config.host,
        port=config.port,
        ssl_context=(cert, key),
        use_reloader=use_reloader,
    )


def _is_production_like() -> bool:
    """Return True if the runtime looks like a public-facing deployment.

    The heuristic is intentionally conservative: any deployment with a
    non-loopback bind address is treated as production. The Werkzeug
    debugger is forbidden on those binds.
    """
    bind = os.environ.get("QV_BIND_HOST", "0.0.0.0")
    return bind not in ("127.0.0.1", "localhost", "::1")


if __name__ == "__main__":
    main()
