# Recipe: Fix a Dependency Cycle

Target cycle: `static/js/qv-crypto.js` -> `static/js/register.js` -> `static/js/qv-crypto.js`

1. Read the imports between these files: `grep -n '^import\|^from\|#include' static/js/qv-crypto.js`, `grep -n '^import\|^from\|#include' static/js/register.js`
2. Move the shared symbols into a new leaf module both sides import
3. Verify: `readmenator . && grep -c 'Dependency Cycles' readmenator-agent/GOTCHAS.md`
