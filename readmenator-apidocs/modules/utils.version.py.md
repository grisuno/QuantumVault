# `utils.version`

> Source: [utils/version.py:1](../../utils/version.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

QuantumVault package version.

Single source of truth for packaging.

deploynator bumps this file on every release; pyproject.toml reads it via
setuptools dynamic version so the PyPI artifact version always matches the
git tag.
