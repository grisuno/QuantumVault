"""WSGI entry point for production deployments.

Run with gunicorn (or any WSGI server) behind a TLS-terminating
reverse proxy::

    gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 2 \
             --access-logfile - --error-logfile - \
             quantumvault.wsgi:application

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

from .app_factory import create_app  # noqa: E402


def main() -> None:
    """Run the packaged application under gunicorn.

    The console script ``quantumvault`` installed by the wheel executes
    this callable. Bind address and worker counts are overridable with
    ``QV_BIND_HOST``, ``QV_BIND_PORT``, ``GUNICORN_WORKERS``, and
    ``GUNICORN_THREADS``; trusted proxy IPs come from
    ``QV_TRUSTED_PROXY_IPS``.
    """
    import sys

    from gunicorn.app.wsgiapp import WSGIApplication

    host = os.environ.get("QV_BIND_HOST", "127.0.0.1")
    port = os.environ.get("QV_BIND_PORT", "8080")
    workers = os.environ.get("GUNICORN_WORKERS", "4")
    threads = os.environ.get("GUNICORN_THREADS", "2")
    trusted_proxies = os.environ.get("QV_TRUSTED_PROXY_IPS", "127.0.0.1")
    sys.argv = [
        "quantumvault",
        "--bind", f"{host}:{port}",
        "--workers", workers,
        "--threads", threads,
        "--forwarded-allow-ips", trusted_proxies,
        "quantumvault.wsgi:application",
    ]
    WSGIApplication("%(prog)s [OPTIONS]").run()


# The gunicorn process import-binds ``application``; the factory call
# runs once at worker boot. There is no global state shared across
# workers beyond the Redis connection and the SQLite file.
application = create_app()
app = application  # convenience alias for `flask --app quantumvault.wsgi:app shell`
