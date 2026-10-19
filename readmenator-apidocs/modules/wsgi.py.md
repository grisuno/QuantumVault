# `wsgi`

> Source: [wsgi.py:1](../../wsgi.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

WSGI entry point for production deployments.

Run with gunicorn (or any WSGI server) behind a TLS-terminating
reverse proxy::

    gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 2 \
             --access-logfile - --error-logfile - \
             wsgi:application

The reverse proxy (nginx, Caddy, ALB) terminates TLS and forwards
``X-Forwarded-Proto``. The factory wires up ProxyFix only when the
operator sets ``QV_TRUSTED_PROXY=1`` so the request scheme is
reconstructed correctly inside Flask.

The Werkzeug dev server is never reachable through this module; that
keeps the public surface small.
