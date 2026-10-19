# quantumvault

*Community 6 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `quantumvault` with dominant language py (cohesion 1.00). Central symbols: no extracted symbols. Documented purpose: QuantumVault application package.  Holds the application factory, the production WSGI entry point, and the served web assets (templates and static files) so a p.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `quantumvault/__init__.py` | py | utility | 0 | yes |
| `utils/version.py` | py | utility | 0 | yes |

## Key Symbols

- No symbols extracted in this community.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 1
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 6 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (views: auth) and community 6 (quantumvault).
- [INFERRED] shares_context community 1 <-> 6 (strength 0.5): Inferred shared context (language py) with no import path between community 1 (views: facade) and community 6 (quantumvault).
- [INFERRED] shares_context community 2 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (utils) and community 6 (quantumvault).
- [INFERRED] shares_context community 3 <-> 6 (strength 0.5): Inferred shared context (layer utility) with no import path between community 3 (quantumvault/static/js) and community 6 (quantumvault).
- [INFERRED] shares_context community 4 <-> 6 (strength 0.5): Inferred shared context (language py) with no import path between community 4 (controllers) and community 6 (quantumvault).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- What would break if the most connected file in quantumvault changed?
- Should quantumvault be split, given cohesion 1.00?

## Sources

- `quantumvault/__init__.py`
- `utils/version.py`
