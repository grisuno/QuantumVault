# Second Brain

*Last synthesized: 2026-10-07 | 88 files | 8 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `app_factory.py`, `user.py`, `utils.py`. Architecturally it is 5 layers, dominant presentation (33 files) across 8 import-based communities. Recorded risk surface: 0 security findings and 2 dependency cycles.

Surprising tissue lives between views: auth, views: facade, static/js: 10 extracted cross-community imports and 10 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (68% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 88 |
| Symbols | 813 |
| Resolved imports | 122 |
| Languages | go, js, py, sh |
| Communities | 8 |
| Doc coverage | 68% (60/88 files) |
| Security findings | 0 |
| Estimated read cost | ~32276 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target readmenator_QuantumVault_n680m_q4
```

## Concept Wiki

- [views: auth (14 files, cohesion 0.44)](./community_0_views_auth.md)
- [views: facade (11 files, cohesion 0.41)](./community_1_views_facade.md)
- [static/js (9 files, cohesion 0.89)](./community_2_static_js.md)
- [controllers (8 files, cohesion 0.47)](./community_3_controllers.md)
- [views: deniable_vault (8 files, cohesion 0.50)](./community_4_views_deniable_vault.md)
- [utils (8 files, cohesion 0.47)](./community_5_utils.md)
- [tools (4 files, cohesion 0.67)](./community_6_tools.md)
- [orphans (26 files, cohesion 0.00)](./community_7_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `app_factory.py` | 48.8 |
| `models/user.py` | 30.7 |
| `utils/utils.py` | 28.8 |
| `views/auth.py` | 24.9 |
| `views/admin.py` | 21.9 |

## Strongest Connections

- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 1 -> 5: depends_on (strength 0.9, EXTRACTED)
- 1 -> 0: depends_on (strength 0.9, EXTRACTED)
- 1 -> 6: depends_on (strength 0.9, EXTRACTED)
- 1 -> 4: depends_on (strength 0.9, EXTRACTED)
- 0 -> 5: depends_on (strength 0.9, EXTRACTED)
- 0 -> 4: depends_on (strength 0.9, EXTRACTED)
- 2 -> 5: depends_on (strength 0.9, EXTRACTED)
- 6 -> 5: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
