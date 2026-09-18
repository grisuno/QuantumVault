# Second Brain

*Last synthesized: 2026-09-18 | 81 files | 3 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `app_factory.py`, `utils.py`, `user.py`. Architecturally it is 5 layers, dominant presentation (33 files) across 3 import-based communities. Recorded risk surface: 0 security findings and 2 dependency cycles.

Surprising tissue lives between views, static/js, orphans: 0 extracted cross-community imports and 2 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (65% file coverage), 0 security findings, 17 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 81 |
| Symbols | 741 |
| Resolved imports | 108 |
| Languages | go, js, py, sh |
| Communities | 3 |
| Doc coverage | 65% (53/81 files) |
| Security findings | 0 |
| Estimated read cost | ~29352 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target QuantumVault
```

## Concept Wiki

- [views (46 files, cohesion 1.00)](./community_0_views.md)
- [static/js (8 files, cohesion 1.00)](./community_1_static_js.md)
- [orphans (27 files, cohesion 0.00)](./community_2_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `app_factory.py` | 46.8 |
| `utils/utils.py` | 30.8 |
| `models/user.py` | 30.7 |
| `views/auth.py` | 24.9 |
| `views/admin.py` | 21.9 |

## Strongest Connections

- 0 -> 2: shares_context (strength 0.5, INFERRED)
- 1 -> 2: shares_context (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
