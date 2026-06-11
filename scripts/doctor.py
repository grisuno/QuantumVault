#!/usr/bin/env python
"""Doctor: import every project module and report the first error.

Used by `make doctor`. Exits 0 on success, 1 on any import failure.
"""

import os
import sys

# Ensure the project root is importable regardless of how this script is
# invoked (python scripts/doctor.py, python -m, etc).
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

import importlib

MODULES = [
    # Third-party
    "flask",
    "flask_login",
    "flask_wtf",
    "flask_cors",
    "flask_limiter",
    "flask_mail",
    "pydantic",
    "cryptography",
    "boto3",
    "botocore",
    "redis",
    "pytz",
    "dotenv",
    "apscheduler",
    "paypalrestsdk",
    "clicksend_client",
    "werkzeug",
    # Project
    "utils.utils",
    "utils.srp6a",
    "utils.scheduler",
    "utils.mailer",
    "utils.cache",
    "models.user",
    "models.message",
    "models.plans",
    "models.contact",
    "controllers.auth",
    "controllers.file",
    "controllers.message",
    "controllers.sync",
    "controllers.contact",
]

missing = []
for m in MODULES:
    try:
        importlib.import_module(m)
    except Exception as e:
        last = str(e).strip().splitlines()[-1] if str(e).strip() else ""
        missing.append((m, type(e).__name__, last))

if missing:
    print("FAIL:")
    for m, etype, msg in missing:
        print(f"  - {m}: {etype}: {msg}")
    sys.exit(1)

print("OK: all project + dependency modules import cleanly")
