# QuantumVault v8 - one-shot dev orchestration.
#
# Uso:
#   make help            # lista targets
#   make                 # alias de `make run` (arranca la app asumiendo deps OK)
#   make setup           # build completo desde cero
#   make run             # arranca la app Flask en foreground (y redis local si hace falta)
#   make stop            # baja el Flask y el redis local que arrancó `make run`
#   make audit           # corre la auditoría zero-trust
#   make clean           # borra caches y artefactos locales (NO toca instance/users.db)

# --- Config -------------------------------------------------------------------

PYTHON       ?= python3
VENV         ?= .venv
VENV_BIN     := $(VENV)/bin
PY           := $(VENV_BIN)/python
PIP          := $(VENV_BIN)/pip
PORT         ?= 4443
HOST         ?= 0.0.0.0
APP_MODULE   ?= app:app
COMPOSE      ?= docker compose
REDIS_PORT   ?= 6379
REDIS_PIDFILE := .run/redis.pid
REDIS_LOGFILE := .run/redis.log
REDIS_DAEMONIZED := .run/redis.daemonized
GARAGE_S3_PORT ?= 3900
GARAGE_PIDFILE := .run/garage.pid
GARAGE_LOGFILE := .run/garage.log

# Detect Kali/Debian PEP 668 and prefer pipx-managed virtualenv.
HAS_VENV     := $(shell $(PYTHON) -c "import venv" 2>/dev/null && echo yes || echo no)
HAS_PIPX     := $(shell command -v pipx >/dev/null 2>&1 && echo yes || echo no)

.DEFAULT_GOAL := help

# --- Targets ------------------------------------------------------------------

.PHONY: help
help:                           ## Show this help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: setup
setup: venv deps env ## First-time setup that does NOT touch docker: venv + deps + .env + tokens.
	@if command -v docker >/dev/null 2>&1; then \
	  echo "[setup] docker found - bringing up garage + redis + bootstrapping bucket ..."; \
	  $(MAKE) compose-up; \
	  $(MAKE) garage-init; \
	else \
	  echo "[setup] docker not found - skipping compose and garage bootstrap."; \
	  echo "[setup] To finish the infra side, either:"; \
	  echo "         sudo apt install -y docker.io docker-compose-v2 && ./run setup"; \
	  echo "         or run garage+redis on :3900/:6379 manually and use 'make run-local'."; \
	fi
	@echo
	@echo "Setup complete. Next: 'make run' (with docker) or 'make run-local' (no docker)"

.PHONY: venv
venv:                           ## Create a fresh Python virtualenv at $(VENV).
	@if [ ! -d "$(VENV)" ]; then \
	  echo "[venv] creating $(VENV) ..."; \
	  if [ "$(HAS_VENV)" = "yes" ]; then \
	    $(PYTHON) -m venv $(VENV); \
	  elif [ "$(HAS_PIPX)" = "yes" ]; then \
	    pipx install virtualenv >/dev/null 2>&1 || true; \
	    $(PYTHON) -m virtualenv $(VENV); \
	  else \
	    echo "ERROR: need python3-venv or pipx. apt-get install -y python3-venv" 1>&2; \
	    exit 1; \
	  fi; \
	else \
	  echo "[venv] $(VENV) already exists, skipping"; \
	fi

.PHONY: deps
deps: venv                      ## Install Python dependencies into the venv.
	@echo "[deps] upgrading pip + installing requirements ..."
	@$(PIP) install --upgrade pip wheel >/dev/null
	@$(PIP) install -r requirements.txt

.PHONY: env
env:                            ## Create .env from .env.example (if missing) and fill Garage tokens.
	@if [ ! -f .env ]; then \
	  echo "[env] copying .env.example -> .env"; \
	  cp .env.example .env; \
	fi
	@if ! grep -q '^GARAGE_RPC_SECRET=' .env || grep -q '^GARAGE_RPC_SECRET=$$' .env; then \
	  echo "[env] generating GARAGE_RPC_SECRET"; \
	  grep -v '^GARAGE_RPC_SECRET=' .env > .env.tmp; \
	  echo "GARAGE_RPC_SECRET=$$(openssl rand -hex 32)" >> .env.tmp; \
	  mv .env.tmp .env; \
	fi
	@if ! grep -q '^GARAGE_ADMIN_TOKEN=' .env || grep -q '^GARAGE_ADMIN_TOKEN=$$' .env; then \
	  echo "[env] generating GARAGE_ADMIN_TOKEN"; \
	  grep -v '^GARAGE_ADMIN_TOKEN=' .env > .env.tmp; \
	  echo "GARAGE_ADMIN_TOKEN=$$(openssl rand -hex 32)" >> .env.tmp; \
	  mv .env.tmp .env; \
	fi
	@echo "[env] syncing tokens into garage.toml (replacing REPLACE_WITH_OPENSSL_RAND_HEX_32) ..."
	@RPC=$$(grep '^GARAGE_RPC_SECRET=' .env | cut -d= -f2); \
	 ADM=$$(grep '^GARAGE_ADMIN_TOKEN=' .env | cut -d= -f2); \
	 $(PYTHON) -c "import re,sys; p='garage.toml'; t=open(p).read(); t=re.sub(r'rpc_secret = \"REPLACE_WITH_OPENSSL_RAND_HEX_32\"', f'rpc_secret = \"$$RPC\"', t); t=re.sub(r'admin_token = \"REPLACE_WITH_OPENSSL_RAND_HEX_32\"', f'admin_token = \"$$ADM\"', t); open(p,'w').write(t)"
	@echo "[env] .env + garage.toml are in sync"

.PHONY: compose-up
compose-up:                     ## Bring up Garage + Redis in the background.
	@if ! command -v docker >/dev/null 2>&1; then \
	  echo "[compose] docker not found. Install it with:"; \
	  echo "    sudo apt install -y docker.io docker-compose-v2"; \
	  echo "    sudo usermod -aG docker $$USER   # then log out/in"; \
	  echo "Or use 'make run-local' to skip docker entirely."; \
	  exit 1; \
	fi
	@echo "[compose] starting garage + redis ..."
	@$(COMPOSE) up -d
	@echo "[compose] waiting for healthchecks ..."
	@$(COMPOSE) ps

.PHONY: compose-down
compose-down:                   ## Stop the docker compose stack (keeps volumes).
	@$(COMPOSE) down

.PHONY: garage-init
garage-init:                    ## Bootstrap the quantumvault bucket + scoped API key in Garage.
	@echo "[garage] bootstrapping bucket + key (idempotent) ..."
	@bash scripts/garage-init.sh
	@echo
	@echo "[garage] credentials were written to .env. Restart the app ('make run') to load them."

.PHONY: garage-status
garage-status:                  ## Show Garage cluster + bucket + key status.
	@$(COMPOSE) exec garage /garage status 2>/dev/null || true
	@$(COMPOSE) exec garage /garage bucket list 2>/dev/null || true
	@$(COMPOSE) exec garage /garage key list 2>/dev/null || true

# Returns "up" if the Garage S3 API is reachable, "down" otherwise.
GARAGE_STATE = $(shell timeout 1 bash -c 'exec 3<>/dev/tcp/127.0.0.1/$(GARAGE_S3_PORT)' 2>/dev/null && echo up || echo down)

.PHONY: garage-up
garage-up:                      ## Start Garage natively (no docker): download, run, provision, write .env.
	@bash scripts/garage-native.sh

.PHONY: garage-down
garage-down:                    ## Stop the native garage server started by `make garage-up`.
	@if [ -f $(GARAGE_PIDFILE) ]; then \
	  pid=$$(cat $(GARAGE_PIDFILE) 2>/dev/null || true); \
	  if [ -n "$$pid" ] && kill -0 "$$pid" 2>/dev/null; then \
	    echo "[garage] stopping pid $$pid ..."; \
	    kill "$$pid" || true; \
	    for i in 1 2 3 4 5 6 7 8 9 10; do \
	      if ! kill -0 "$$pid" 2>/dev/null; then break; fi; \
	      sleep 0.2; \
	    done; \
	    if kill -0 "$$pid" 2>/dev/null; then echo "[garage] force-killing $$pid"; kill -9 "$$pid" || true; fi; \
	  fi; \
	  rm -f $(GARAGE_PIDFILE); \
	elif [ "$(GARAGE_STATE)" = "up" ]; then \
	  echo "[garage] WARNING: something is listening on :$(GARAGE_S3_PORT) but we did not start it; leaving it alone."; \
	else \
	  echo "[garage] nothing to stop"; \
	fi

.PHONY: garage-native-status
garage-native-status:           ## Show whether the native garage S3 API is up.
	@echo "[garage] :$(GARAGE_S3_PORT) state: $(GARAGE_STATE)"
	@if [ -f $(GARAGE_PIDFILE) ]; then echo "[garage] pidfile: $$(cat $(GARAGE_PIDFILE))"; fi

.PHONY: redis-ping
redis-ping:                     ## Sanity check: is Redis reachable from the host?
	@redis-cli ping

# Helper: returns "up" if Redis is reachable on REDIS_PORT, "down" otherwise.
# We try redis-cli first (most reliable signal), then fall back to a raw TCP
# probe via bash's /dev/tcp. Either path resolves in well under a second.
REDIS_STATE = $(shell { command -v redis-cli >/dev/null 2>&1 && timeout 1 redis-cli -p $(REDIS_PORT) ping 2>/dev/null | grep -q PONG && echo up; } \
                      || { timeout 1 bash -c 'exec 3<>/dev/tcp/127.0.0.1/$(REDIS_PORT)' 2>/dev/null && echo up; } \
                      || echo down)

# Sub-make target used by redis-up's wait loop. Returns exit 0 if redis is
# reachable, exit 1 otherwise. Defined here so redis-up can re-evaluate the
# probe on every loop iteration; not added to .PHONY so it stays out of
# `make help`.
redis-is-up:
	@command -v redis-cli >/dev/null 2>&1 && timeout 1 redis-cli -p $(REDIS_PORT) ping 2>/dev/null | grep -q PONG
.PHONY: redis-up
redis-up:                       ## Start a local redis-server (no docker) if :$(REDIS_PORT) is free.
	@mkdir -p .run
	@if $(MAKE) --no-print-directory redis-is-up >/dev/null 2>&1; then \
	  echo "[redis] already up on :$(REDIS_PORT) (skipping)"; \
	else \
	  if ! command -v redis-server >/dev/null 2>&1; then \
	    echo "ERROR: redis-server not installed. Run: sudo apt install -y redis-server" 1>&2; \
	    exit 1; \
	  fi; \
	  echo "[redis] starting redis-server on :$(REDIS_PORT) (daemonized, pidfile=$(REDIS_PIDFILE)) ..."; \
	  redis-server --daemonize yes --port $(REDIS_PORT) \
	               --pidfile $(abspath $(REDIS_PIDFILE)) \
	               --logfile $(abspath $(REDIS_LOGFILE)) \
	               --dir $(abspath .run); \
	  for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do \
	    if $(MAKE) --no-print-directory redis-is-up >/dev/null 2>&1; then \
	      echo "[redis] up"; touch $(REDIS_DAEMONIZED); break; \
	    fi; \
	    sleep 0.2; \
	  done; \
	  if ! $(MAKE) --no-print-directory redis-is-up >/dev/null 2>&1; then \
	    echo "ERROR: redis failed to come up. Tail of $(REDIS_LOGFILE):" 1>&2; \
	    tail -n 20 $(REDIS_LOGFILE) 1>&2 || true; exit 1; \
	  fi; \
	fi


.PHONY: redis-down
redis-down:                     ## Stop the local redis-server started by `make redis-up`.
	@if [ -f $(REDIS_PIDFILE) ]; then \
	  pid=$$(cat $(REDIS_PIDFILE) 2>/dev/null || true); \
	  if [ -n "$$pid" ] && kill -0 "$$pid" 2>/dev/null; then \
	    echo "[redis] stopping pid $$pid ..."; \
	    kill "$$pid" || true; \
	    for i in 1 2 3 4 5 6 7 8 9 10; do \
	      if ! kill -0 "$$pid" 2>/dev/null; then break; fi; \
	      sleep 0.2; \
	    done; \
	    if kill -0 "$$pid" 2>/dev/null; then echo "[redis] force-killing $$pid"; kill -9 "$$pid" || true; fi; \
	  fi; \
	  rm -f $(REDIS_PIDFILE); \
	elif [ "$(REDIS_STATE)" = "up" ]; then \
	  echo "[redis] WARNING: a redis is listening on :$(REDIS_PORT) but we did not start it."; \
	  echo "[redis] not killing it (would be rude). Use 'redis-cli -p $(REDIS_PORT) shutdown nosave' manually if you want it down."; \
	else \
	  echo "[redis] nothing to stop"; \
	fi
	@rm -f $(REDIS_DAEMONIZED)

.PHONY: redis-status
redis-status:                   ## Show whether the local redis is up.
	@echo "[redis] :$(REDIS_PORT) state: $(REDIS_STATE)"
	@if [ -f $(REDIS_PIDFILE) ]; then echo "[redis] pidfile: $$(cat $(REDIS_PIDFILE))"; fi

.PHONY: db-reset
db-reset:                       ## Wipe the dev SQLite database (NEVER use in prod).
	@echo "[db] removing instance/users.db"
	@rm -f instance/users.db
	@mkdir -p instance
	@echo "[db] done. Next user registration will create the schema fresh."

# Same as db-reset, kept as a friendlier alias. The name `cleandb` is what
# most newcomers reach for; the destructive behaviour is identical.
#
# The force gate reads three signals (in order of preference):
#   1. QV_FORCE=1 environment variable:    QV_FORCE=1 make cleandb
#   2. FORCE goal on the command line:     make cleandb force
#      (FORCE is a stub phony target declared below so make does not
#      try to resolve it as a file and the word "force" reaches
#      MAKECMDGOALS where the recipe can see it.)
#   3. --force goal:                       make cleandb --force
#      (works the same way as "force" — make treats extra words after
#      the first target as additional goals, and we declare --force
#      as a no-op phony so make does not error out trying to find it.)
# If none of those are present, the recipe refuses with a clear hint
# rather than wiping the database silently. The previous version used
# $$1 inside the recipe, which is always empty (recipes run in a
# fresh shell, so positional parameters are never set), so the
# `--force` check could never match.
.PHONY: cleandb force --force
force --force: ; @true
cleandb:                       ## DESTRUCTIVE: wipe instance/users.db (refuses unless QV_FORCE=1, FORCE, or --force).
	@if [ ! -f instance/users.db ]; then \
	  echo "[cleandb] nothing to do (instance/users.db does not exist)"; \
	  exit 0; \
	fi; \
	 force_ok=0; \
	 if [ "$$QV_FORCE" = "1" ]; then force_ok=1; fi; \
	 for g in $(MAKECMDGOALS); do \
	   if [ "$$g" = "force" ] || [ "$$g" = "--force" ] || [ "$$g" = "FORCE" ]; then force_ok=1; break; fi; \
	 done; \
	 if [ "$$force_ok" != "1" ]; then \
	   echo "ERROR: 'make cleandb' removes the dev database."; \
	   echo "       Re-run with 'make cleandb --force', 'make cleandb force', or 'QV_FORCE=1 make cleandb'."; \
	   echo "       To keep a copy first, run 'make backupdb'."; \
	   exit 2; \
	 fi; \
	 $(MAKE) db-reset

.PHONY: backupdb
backupdb:                      ## Snapshot instance/users.db to backups/users-YYYYMMDD-HHMMSS.db.
	@if [ ! -f instance/users.db ]; then echo "[backupdb] nothing to back up"; exit 0; fi
	@mkdir -p backups
	@ts=$$(date -u +%Y%m%d-%H%M%S); \
	 dest="backups/users-$$ts.db"; \
	 cp -p instance/users.db "$$dest" && chmod 600 "$$dest"; \
	 echo "[backupdb] wrote $$dest"

.PHONY: run
run:                            ## Run the Flask app in foreground; starts docker compose OR a local redis if available.
	@if [ ! -f .env ]; then echo "ERROR: .env missing. Run 'make env' first." 1>&2; exit 1; fi
	@if [ ! -d "$(VENV)" ]; then echo "ERROR: venv missing. Run 'make deps' first." 1>&2; exit 1; fi
	@if command -v docker >/dev/null 2>&1; then \
	  if ! $(COMPOSE) ps --services --filter "status=running" 2>/dev/null | grep -q -E 'garage|redis'; then \
	    echo "[run] compose services not running. Starting them ..."; \
	    $(MAKE) compose-up; \
	  fi; \
	else \
	  echo "[run] docker not installed; starting a local redis + native garage ..."; \
	  $(MAKE) redis-up; \
	  $(MAKE) garage-up; \
	fi
	@echo "[run] starting Flask on $(HOST):$(PORT) (QV_ENV=dev) ..."
	@cd $(CURDIR) && QV_ENV=dev FLASK_DEBUG=1 $(PY) app.py

.PHONY: run-local
run-local:                      ## Run Flask without touching docker (you manage garage/redis yourself).
	@if [ ! -f .env ]; then echo "ERROR: .env missing. Run 'make env' first." 1>&2; exit 1; fi
	@if [ ! -d "$(VENV)" ]; then echo "ERROR: venv missing. Run 'make deps' first." 1>&2; exit 1; fi
	@echo "[run-local] prerequisites expected: redis on $$STORAGE_URI_HOST, garage on $$S3_ENDPOINT_URL"
	@echo "[run-local] starting Flask on $(HOST):$(PORT) (QV_ENV=dev) ..."
	@cd $(CURDIR) && QV_ENV=dev FLASK_DEBUG=1 $(PY) app.py

# Production entry point. This is the target the operator's process
# supervisor (systemd, runit, k8s) should call. ``gunicorn`` binds
# to a local socket or a non-privileged port; a reverse proxy in
# front terminates TLS and forwards to the bound port.
.PHONY: serve
serve:                         ## Run gunicorn against the production WSGI module.
	@if [ ! -f .env ]; then echo "ERROR: .env missing. Run 'make env' first." 1>&2; exit 1; fi
	@if [ ! -d "$(VENV)" ]; then echo "ERROR: venv missing. Run 'make deps' first." 1>&2; exit 1; fi
	@if ! $(PY) -c "import gunicorn" 2>/dev/null; then \
	  echo "[serve] gunicorn not installed. pip install gunicorn==23.0.0"; \
	  $(PIP) install gunicorn==23.0.0; \
	fi
	@echo "[serve] starting gunicorn on $(HOST):$(PORT) (workers=$${GUNICORN_WORKERS:-4})"
	@cd $(CURDIR) && $(VENV_BIN)/gunicorn --bind $(HOST):$(PORT) \
	    --workers $${GUNICORN_WORKERS:-4} --threads $${GUNICORN_THREADS:-2} \
	    --access-logfile - --error-logfile - \
	    --forwarded-allow-ips="$${QV_TRUSTED_PROXY_IPS:-127.0.0.1}" \
	    wsgi:application

.PHONY: stop
stop:                           ## Stop the dev app, the docker compose stack, and any redis we started.
	@$(MAKE) kill
	@if command -v docker >/dev/null 2>&1; then \
	  echo "[stop] docker compose down ..."; \
	  $(COMPOSE) down 2>/dev/null || true; \
	fi
	@if [ -f $(REDIS_DAEMONIZED) ] || [ -f $(REDIS_PIDFILE) ]; then \
	  echo "[stop] bringing down local redis we started ..."; \
	  $(MAKE) redis-down; \
	else \
	  echo "[stop] no local redis pidfile ($(REDIS_PIDFILE)) and no daemonized marker — leaving :$(REDIS_PORT) alone"; \
	fi
	@if [ -f $(GARAGE_PIDFILE) ]; then \
	  echo "[stop] bringing down native garage we started ..."; \
	  $(MAKE) garage-down; \
	fi
	@echo "[stop] done"

.PHONY: kill
kill:                           ## Force-kill any process bound to :4443 and any python app.py.
	@echo "[kill] terminating python app.py processes ..."
	@for pat in "[a]pp.py"; do \
	   pids=$$(ps -eo pid=,args= 2>/dev/null \
	             | awk -v p="$$pat" '$$0 ~ p && $$0 !~ /awk/ {print $$1}'); \
	   if [ -n "$$pids" ]; then \
	     echo "[kill] killing pids: $$pids"; \
	     kill $$pids 2>/dev/null || true; \
	   fi; \
	 done; \
	 sleep 1
	@if command -v fuser >/dev/null 2>&1; then \
	  echo "[kill] freeing :4443 with fuser ..."; \
	  fuser -k 4443/tcp 2>/dev/null || true; \
	  sleep 1; \
	fi
	@leftover=$$(ps -ef | grep -E "python.*app\.py" | grep -v grep || true); \
	 if [ -n "$$leftover" ]; then \
	   echo "[kill] WARNING: still alive:"; \
	   echo "$$leftover"; \
	   exit 1; \
	 fi
	@if command -v ss >/dev/null 2>&1; then \
	  if ss -ltn 2>/dev/null | grep -q ':4443 '; then \
	    echo "[kill] WARNING: :4443 still in use"; exit 1; \
	  fi; \
	fi
	@echo "[kill] done, :4443 is free"

.PHONY: doctor
doctor:                         ## Import-smoke: try every project module, report missing deps.
	@if [ ! -d "$(VENV)" ]; then echo "ERROR: venv missing. Run 'make deps' first." 1>&2; exit 1; fi
	@echo "[doctor] importing project modules with the venv's python ..."
	@cd $(CURDIR) && $(PY) scripts/doctor.py

.PHONY: upgrade-deps
upgrade-deps:                   ## Refresh the venv to match the latest requirements.txt lock.
	@if [ ! -d "$(VENV)" ]; then $(MAKE) deps; fi
	@echo "[deps] upgrading pip + packages in $(VENV)..."
	@$(VENV_BIN)/python -m pip install --upgrade pip==26.1.2
	@$(VENV_BIN)/python -m pip install -r requirements.txt --upgrade
	@echo "[deps] generating requirements.lock (hashes) for supply-chain integrity"
	@$(VENV_BIN)/python -m pip install --quiet pip-tools==7.5.4 || true
	@$(VENV_BIN)/pip-compile --quiet --no-header --generate-hashes --output-file=requirements.lock requirements.txt 2>/dev/null || \
	  echo "[deps] pip-compile not available; requirements.txt is version-pinned but unhashed"

.PHONY: pip-audit
pip-audit:                      ## Check for known vulns in the current dependency tree.
	@if [ ! -d "$(VENV)" ]; then echo "[pip-audit] venv missing; run 'make deps'"; exit 1; fi
	@$(VENV_BIN)/python -m pip_audit --strict

.PHONY: bandit
bandit:                         ## Static security scan of every Python file we ship.
	@if [ ! -d "$(VENV)" ]; then echo "[bandit] venv missing; run 'make deps'"; exit 1; fi
	@$(VENV_BIN)/bandit -q -r views/ controllers/ models/ utils/ app_factory.py wsgi.py app.py -ll

.PHONY: semgrep
semgrep:                        ## Local Semgrep rules: crypto anti-patterns in our code.
	@command -v semgrep >/dev/null 2>&1 || { \
	  echo "[semgrep] not installed. Install: pip install semgrep==1.143.0"; exit 1; }
	@semgrep --config=p/python --config=p/owasp-top-ten \
	    --config=p/flask --config=p/javascript --config=p/secrets \
	    --error views/ controllers/ models/ utils/ app_factory.py wsgi.py app.py \
	    static/js/qv-crypto.js static/js/vendor/

.PHONY: audit
audit: pip-audit bandit         ## Run the security audit stack: pip-audit + bandit.
	@echo "[audit] scanning for hardcoded secrets ..."
	@fail=0; \
	 hits=$$(grep -rniE "(AKIA[0-9A-Z]{8,}|password\s*=\s*['\"][^'\"]{16,}['\"]|clicksend.*['\"][A-Za-z0-9]{16,}['\"])" \
	          --include=*.py --include=*.json --include=*.html \
	          --exclude-dir=env --exclude-dir=.venv --exclude-dir=v7 --exclude-dir=__pycache__ .); \
	 if [ -n "$$hits" ]; then \
	   echo "$$hits"; \
	   echo "[audit] FAIL: hardcoded secret pattern found"; \
	   fail=1; \
	 else \
	   echo "[audit] OK: no AKIA / hardcoded long passwords / hardcoded clicksend keys in project source"; \
	 fi; \
	 echo "[audit] checking payload.json does not leak MAIL_USERNAME / MAIL_PASSWORD ..."; \
	 leaks=$$($(PY) -c "import json,sys; d=json.load(open('payload.json')); sys.stdout.write('\n'.join('LEAK '+k for k in ('MAIL_USERNAME','MAIL_PASSWORD') if k in d))" 2>/dev/null); \
	 if [ -n "$$leaks" ]; then \
	   echo "$$leaks"; echo "[audit] FAIL"; fail=1; \
	 else \
	   echo "[audit] OK: payload.json is secret-free"; \
	 fi; \
	 echo "[audit] checking controllers/auth.py reads clicksend creds from os.environ ..."; \
	 if grep -E "configuration\.(username|password)\s*=" controllers/auth.py | grep -q os.environ; then \
	   echo "[audit] OK: clicksend config read from os.environ"; \
	 else \
	   echo "[audit] FAIL: controllers/auth.py clicksend config not sourced from env"; fail=1; \
	 fi; \
	 exit $$fail

.PHONY: clean
clean:                          ## Remove caches and build artefacts (keeps .env and instance/users.db).
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	@rm -rf $(VENV) .venv-tmp
	@rm -rf .run
	@echo "[clean] done"

.PHONY: nuke
nuke:                           ## DESTRUCTIVE: stop compose (with volumes) and remove instance/users.db.
	@echo "[nuke] THIS WILL WIPE DATA. Press Ctrl-C in 5s to abort ..."; sleep 5
	@$(COMPOSE) down -v
	@rm -rf instance/users.db
	@echo "[nuke] done"
