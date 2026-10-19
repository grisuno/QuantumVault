"""QuantumVault application package.

Holds the application factory, the production WSGI entry point, and the
served web assets (templates and static files) so a pip-installed wheel
is a complete runnable application, not just a library of modules.
"""

from utils.version import __version__ as __version__
