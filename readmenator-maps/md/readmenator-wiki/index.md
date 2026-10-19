# Second Brain

*Last synthesized: 2026-10-19 | 90 files | 8 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `app_factory.py`, `user.py`, `utils.py`. Architecturally it is 5 layers, dominant presentation (33 files) across 8 import-based communities. Recorded risk surface: 0 security findings and 2 dependency cycles.

Surprising tissue lives between views: auth, views: facade, utils: 8 extracted cross-community imports and 12 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (69% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 90 |
| Symbols | 814 |
| Resolved imports | 123 |
| Languages | go, js, py, sh |
| Communities | 8 |
| Doc coverage | 69% (62/90 files) |
| Security findings | 0 |
| Estimated read cost | ~32675 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target QuantumVault
```

## Concept Wiki

- [views: auth (16 files, cohesion 0.48)](./community_0_views_auth.md)
- [views: facade (11 files, cohesion 0.41)](./community_1_views_facade.md)
- [utils (10 files, cohesion 0.57)](./community_2_utils.md)
- [quantumvault/static/js (9 files, cohesion 0.89)](./community_3_quantumvault_static_js.md)
- [controllers (8 files, cohesion 0.47)](./community_4_controllers.md)
- [views: deniable_vault (8 files, cohesion 0.50)](./community_5_views_deniable_vault.md)
- [quantumvault (2 files, cohesion 1.00)](./community_6_quantumvault.md)
- [orphans (26 files, cohesion 0.00)](./community_7_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `quantumvault/app_factory.py` | 48.8 |
| `models/user.py` | 30.7 |
| `utils/utils.py` | 28.8 |
| `views/auth.py` | 24.9 |
| `views/admin.py` | 21.9 |

## Strongest Connections

- 4 -> 1: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)
- 0 -> 2: depends_on (strength 0.9, EXTRACTED)
- 0 -> 5: depends_on (strength 0.9, EXTRACTED)
- 1 -> 5: depends_on (strength 0.9, EXTRACTED)
- 1 -> 2: depends_on (strength 0.9, EXTRACTED)
- 1 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 2: depends_on (strength 0.9, EXTRACTED)
- 0 -> 6: shares_context (strength 0.5, INFERRED)
- 0 -> 7: shares_context (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
