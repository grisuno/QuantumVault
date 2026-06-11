"""WSGI entry point for production deployments.

Run with gunicorn (or any WSGI server) behind a TLS-terminating
reverse proxy::

    gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 2 \\
             --access-logfile - --error-logfile - \\
             wsgi:application

The reverse proxy (nginx, Caddy, ALB) terminates TLS and forwards
``X-Forwarded-Proto``. The factory wires up ProxyFix only when the
operator sets ``QV_TRUSTED_PROXY=1`` so the request scheme is
reconstructed correctly inside Flask.

The Werkzeug dev server is never reachable through this module; that
keeps the public surface small.
"""

import os

# Required for production. Refuse to start without a stable secret.
os.environ.setdefault("QV_ENV", "production")

from app_factory import create_app  # noqa: E402

# The gunicorn process import-binds ``application``; the factory call
# runs once at worker boot. There is no global state shared across
# workers beyond the Redis connection and the SQLite file.
application = create_app()
app = application  # convenience alias for `flask --app wsgi:app shell`
