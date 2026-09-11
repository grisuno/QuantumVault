"""Mutation testing harness for the QuantumVault facade and cover contracts.

Each discovered token mutation is applied in place, the test suite is run,
and the mutation is classified as killed (tests fail) or survived (tests
pass). A survivor indicates a gap in the tests and yields a non-zero exit
status. The harness runs the suite with ``-B`` and purges bytecode caches
so a restored source is always reloaded rather than served from a stale
``.pyc`` compiled from a mutant.
"""

from __future__ import annotations

import argparse
import io
import os
import subprocess
import sys
import tokenize
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TARGETS = (
    "controllers/facade.py",
    "controllers/cover.py",
)
OPERATOR_MUTATIONS = {
    "==": "!=",
    "!=": "==",
    "<": "<=",
    "<=": "<",
    ">": ">=",
    ">=": ">",
    "and": "or",
    "or": "and",
    "True": "False",
    "False": "True",
}
NAME_TOKEN_TYPES = {tokenize.NAME, tokenize.OP}
KEYWORD_TOKEN_TYPES = {getattr(tokenize, "KEYWORD", tokenize.NAME)}
IGNORED_TOKEN_TYPES = {
    tokenize.NL,
    tokenize.NEWLINE,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.COMMENT,
    tokenize.ENCODING,
    tokenize.ENDMARKER,
}
SKIP_BOOL_KEYWORDS = frozenset(
    {"frozen", "slots", "kw_only", "autoescape", "auto_reload", "cache_size"}
)


@dataclass(frozen=True, slots=True)
class Mutation:
    """A single token replacement and where it lives."""

    path: Path
    line: int
    column: int
    original: str
    replacement: str
    description: str


def _is_equivalent_bool(tokens: list[tokenize.TokenInfo], index: int) -> bool:
    if index < 2:
        return False
    previous = tokens[index - 1]
    before = tokens[index - 2]
    return (
        previous.type == tokenize.OP
        and previous.string == "="
        and before.string in SKIP_BOOL_KEYWORDS
    )


def discover_mutations(path: Path, source: str) -> list[Mutation]:
    """Return every token-level mutation the harness can apply to a module."""
    mutations: list[Mutation] = []
    reader = io.StringIO(source).readline
    tokens = [
        token
        for token in tokenize.generate_tokens(reader)
        if token.type not in IGNORED_TOKEN_TYPES
    ]
    for index, token in enumerate(tokens):
        if token.type not in NAME_TOKEN_TYPES and token.type not in KEYWORD_TOKEN_TYPES:
            continue
        if token.string in {"True", "False"} and _is_equivalent_bool(tokens, index):
            continue
        replacement = OPERATOR_MUTATIONS.get(token.string)
        if replacement is None:
            continue
        mutations.append(
            Mutation(
                path=path,
                line=token.start[0],
                column=token.start[1],
                original=token.string,
                replacement=replacement,
                description=f"{path.name}:{token.start[0]} {token.string} -> {replacement}",
            )
        )
    return mutations


def apply_mutation(source: str, mutation: Mutation) -> str:
    """Return source with one token replaced at its exact position."""
    lines = source.splitlines(keepends=True)
    index = mutation.line - 1
    line = lines[index]
    column = mutation.column
    if line[column : column + len(mutation.original)] != mutation.original:
        raise ValueError(f"mutation offset mismatch for {mutation.description}")
    lines[index] = line[:column] + mutation.replacement + line[column + len(mutation.original) :]
    return "".join(lines)


def collect(targets: list[str], limit: int) -> list[Mutation]:
    """Gather mutations across targets up to a global cap."""
    mutations: list[Mutation] = []
    for relative in targets:
        path = PROJECT_ROOT / relative
        source = path.read_text(encoding="utf-8")
        mutations.extend(discover_mutations(path, source))
        if len(mutations) >= limit:
            break
    return mutations[:limit]


def purge_bytecode() -> None:
    """Remove compiled caches so restored sources are always reloaded."""
    for cache in PROJECT_ROOT.rglob("__pycache__"):
        if ".venv" in cache.parts or ".git" in cache.parts:
            continue
        for artifact in cache.glob("*.pyc"):
            artifact.unlink(missing_ok=True)


def run_suite(python: str, tests: list[str]) -> bool:
    """Return whether the test suite passed."""
    command = [python, "-B", "-m", "pytest", "-q", "-x", *tests]
    environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    completed = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=environment,
    )
    return completed.returncode == 0


def main(argv: list[str] | None = None) -> int:
    """Run the mutation campaign and report killed versus survived mutants."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", nargs="*", default=list(DEFAULT_TARGETS))
    parser.add_argument("--tests", nargs="*", default=[])
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--max-mutants", type=int, default=120)
    parser.add_argument("--list", action="store_true", help="print mutants and exit")
    arguments = parser.parse_args(argv)

    mutations = collect(arguments.targets, arguments.max_mutants)
    if arguments.list:
        for mutation in mutations:
            print(mutation.description)
        print(f"discovered {len(mutations)} mutants")
        return 0

    purge_bytecode()
    killed = 0
    survived: list[Mutation] = []
    for mutation in mutations:
        path = mutation.path
        original = path.read_text(encoding="utf-8")
        try:
            path.write_text(apply_mutation(original, mutation), encoding="utf-8")
            passed = run_suite(arguments.python, arguments.tests)
        finally:
            path.write_text(original, encoding="utf-8")
        if passed:
            survived.append(mutation)
            print(f"SURVIVED {mutation.description}")
        else:
            killed += 1
            print(f"killed   {mutation.description}")

    total = len(mutations)
    print(f"\nmutants {total} killed {killed} survived {len(survived)}")
    if survived:
        print("survivors require stronger tests:")
        for mutation in survived:
            print(f"  - {mutation.description}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
