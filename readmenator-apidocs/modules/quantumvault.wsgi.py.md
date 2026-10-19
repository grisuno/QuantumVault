# `quantumvault.wsgi`

> Source: [quantumvault/wsgi.py:1](../../quantumvault/wsgi.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

WSGI entry point for production deployments.

Run with gunicorn (or any WSGI server) behind a TLS-terminating
reverse proxy::

    gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 2              --access-logfile - --error-logfile -              quantumvault.wsgi:application

The reverse proxy (nginx, Caddy, ALB) terminates TLS and forwards
``X-Forwarded-Proto``. The factory wires up ProxyFix only when the
operator sets ``QV_TRUSTED_PROXY=1`` so the request scheme is
reconstructed correctly inside Flask.

The Werkzeug dev server is never reachable through this module; that
keeps the public surface small.

## Contents

- **Functions:** [`main`](#main)

## Functions

<a id="main"></a>

### `main`

`function` | [quantumvault/wsgi.py:27](../../quantumvault/wsgi.py#L27)

```python
def main() -> None
```

Run the packaged application under gunicorn.

The console script `[`quantumvault`](quantumvault.__init__.py.md)` installed by the wheel executes
this callable. Bind address and worker counts are overridable with
``QV_BIND_HOST``, ``QV_BIND_PORT``, ``GUNICORN_WORKERS``, and
``GUNICORN_THREADS``; trusted proxy IPs come from
``QV_TRUSTED_PROXY_IPS``.

---
