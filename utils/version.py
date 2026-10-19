"""QuantumVault package version. Single source of truth for packaging.

deploynator bumps this file on every release; pyproject.toml reads it via
setuptools dynamic version so the PyPI artifact version always matches the
git tag.
"""

__version__ = "0.1.2"
