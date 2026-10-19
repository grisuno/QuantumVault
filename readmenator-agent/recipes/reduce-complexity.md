# Recipe: Reduce File Complexity

Target hotspot: `quantumvault/static/js/qv-crypto.js`
(complexity 0.6, centrality 1.0)

1. Read dependents: `grep -n 'quantumvault/static/js/qv-crypto.js' readmenator-agent/ARCHITECTURE*.md`
2. Extract functions/classes into new files in the same subsystem
3. Update imports
4. Regenerate: `readmenator .`
