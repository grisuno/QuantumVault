# Recipe: Fix a Dependency Cycle

Target cycle: `quantumvault/static/js/qv-crypto.js` -> `quantumvault/static/js/register.js` -> `quantumvault/static/js/qv-crypto.js`

1. Read the imports between these files: `grep -n '^import\|^from\|#include' quantumvault/static/js/qv-crypto.js`, `grep -n '^import\|^from\|#include' quantumvault/static/js/register.js`
2. Move the shared symbols into a new leaf module both sides import
3. Verify: `readmenator . && grep -c 'Dependency Cycles' readmenator-agent/GOTCHAS.md`
