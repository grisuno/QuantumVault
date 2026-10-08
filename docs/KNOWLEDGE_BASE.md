# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. 88 files, 813 symbols, 524 imports. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Start here:** Statistics Dashboard for scope, God Nodes for blast radius, Architecture Reference for per-file API. Agents: prefer `readmenator-agent/INDEX.md` + `SYMBOLS.md`.

**Wiki:** prefer `readmenator-wiki/index.md` for progressive disclosure: one synthesis page per community, `connections.json` with EXTRACTED vs INFERRED confidence, `queries.md` log, `REPORT.md` audit.

**Confidence:** EXTRACTED = parsed from source, INFERRED = heuristic bridge, AMBIGUOUS = reported, never hidden. See `readmenator-wiki/REPORT.md`.

**Total Files Parsed:** 88 | **Total Symbols Extracted:** 813 | **Total Imports:** 524
 | **Resolved Imports:** 122

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:1e0fd0b | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Community Analysis](#community-analysis)
6. [Surprising Connections](#surprising-connections)
7. [Suggested Questions](#suggested-questions)
8. [Taint Propagation Map](#taint-propagation-map)
9. [Hotspot Analysis](#hotspot-analysis)
10. [Dependency Cycles](#dependency-cycles)
11. [Change Impact Analysis](#change-impact-analysis)
12. [Architecture Violations](#architecture-violations)
13. [Suggested Linting Rules](#suggested-linting-rules)
14. [Dataflow Analysis](#dataflow-analysis)
15. [Concept Graph](#concept-graph)
16. [Orphans](#orphans)
17. [Query Recipes](#query-recipes)
18. [Structural Knowledge Map](#structural-knowledge-map)
19. [UML Class Diagram](#uml-class-diagram)
20. [Code Property Graph](#code-property-graph)
21. [Architecture Reference](#architecture-reference)
    - [GO (3 files)](#go-3-files)
    - [JS (10 files)](#js-10-files)
    - [PY (70 files)](#py-70-files)
    - [SH (5 files)](#sh-5-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 88 |
| Total Symbols | 813 |
| Total Imports | 524 |
| Call Edges | 3894 |
| Inheritance Edges | 22 |
| Languages | 4 |
| Avg Symbols/File | 9.2 |
| Avg Imports/File | 6.0 |
| Resolved Imports | 122 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `app_factory.py` | 37 | 8 | py |
| `admin.py` | 25 | 19 | py |
| `test_secure_channel.py` | 19 | 67 | py |
| `auth.py` | 17 | 29 | py |
| `auth.py` | 16 | 14 | py |
| `secure_channel.py` | 15 | 37 | py |
| `security.py` | 15 | 10 | py |
| `enc_dec.go` | 14 | 4 | go |
| `doctor.py` | 13 | 28 | py |
| `subscription.py` | 13 | 4 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| presentation | 33 |
| utility | 30 |
| testing | 17 |
| infrastructure | 4 |
| business_logic | 4 |

### utility

- `__init__.py` (py, 0 symbols)
- `app.py` (py, 2 symbols)
- `enc_dec.go` (go, 4 symbols)
- `enc_dec.py` (py, 5 symbols)
- `install.sh` (sh, 0 symbols)
- `make.sh` (sh, 0 symbols)
- `pq_decrypt_password.py` (py, 0 symbols)
- `doctor.py` (py, 28 symbols)
- `garage-init.sh` (sh, 1 symbols)
- `garage-native.sh` (sh, 3 symbols)
- `makeadmin.py` (py, 5 symbols)
- `server.go` (go, 2 symbols)
- `server.py` (py, 0 symbols)
- `account.js` (js, 9 symbols)
- `coded-text.js` (js, 3 symbols)
- *... and 15 more*

### presentation

- `app_factory.py` (py, 8 symbols)
- `__init__.py` (py, 0 symbols)
- `auth.py` (py, 14 symbols)
- `contact.py` (py, 4 symbols)
- `deniable_vault.py` (py, 22 symbols)
- `facade.py` (py, 26 symbols)
- `file.py` (py, 9 symbols)
- `message.py` (py, 4 symbols)
- `secure_channel.py` (py, 37 symbols)
- `sync.py` (py, 3 symbols)
- `contact.py` (py, 9 symbols)
- `message.py` (py, 6 symbols)
- `user.py` (py, 27 symbols)
- `email_tool.py` (py, 6 symbols)
- `terms.py` (py, 1 symbols)
- *... and 18 more*

### infrastructure

- `client.go` (go, 1 symbols)
- `client.py` (py, 0 symbols)
- `messages.js` (js, 6 symbols)
- `cache.py` (py, 5 symbols)

### business_logic

- `__init__.py` (py, 0 symbols)
- `deniable_vault.py` (py, 6 symbols)
- `plans.py` (py, 10 symbols)
- `superadmin_audit.py` (py, 5 symbols)

### testing

- `test_bloque1.py` (py, 8 symbols)
- `test.sh` (sh, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `conftest.py` (py, 8 symbols)
- `test_account_facade.py` (py, 6 symbols)
- `test_auth_phone.py` (py, 3 symbols)
- `test_cover.py` (py, 52 symbols)
- `test_deniable_vault.py` (py, 55 symbols)
- `test_doctor.py` (py, 12 symbols)
- `test_facade.py` (py, 52 symbols)
- `test_integrity.py` (py, 6 symbols)
- `test_padding.py` (py, 24 symbols)
- `test_secure_channel.py` (py, 67 symbols)
- `test_security.py` (py, 8 symbols)
- `test_srp.py` (py, 6 symbols)
- *... and 2 more*

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `garage-init.sh` | 0.2000 | 0.0000 | 0.0000 | 0.00 | 2.00 |
| 2 | `mailer.py` | 0.1438 | 0.0161 | 0.0161 | 0.00 | 1.33 |
| 3 | `padding.py` | 0.1397 | 0.0492 | 0.0492 | 0.00 | 1.08 |
| 4 | `security.py` | 0.1334 | 0.0513 | 0.0513 | 0.00 | 1.00 |
| 5 | `test_auth_phone.py` | 0.1333 | 0.0000 | 0.0000 | 0.00 | 1.33 |
| 6 | `message.py` | 0.1331 | 0.0124 | 0.0124 | 0.00 | 1.25 |
| 7 | `deniable_vault.py` | 0.1270 | 0.0158 | 0.0158 | 0.00 | 1.17 |
| 8 | `integrity.py` | 0.1269 | 0.0222 | 0.0222 | 0.00 | 1.12 |
| 9 | `superadmin_audit.py` | 0.1258 | 0.0089 | 0.0089 | 0.00 | 1.20 |
| 10 | `account.py` | 0.1256 | 0.0085 | 0.0085 | 0.00 | 1.20 |

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `app_factory.py` | 48.8 | | 0.0000 |
| `user.py` | 30.7 | | 0.0000 |
| `utils.py` | 28.8 | | 0.0000 |
| `auth.py` | 24.9 | | 0.0000 |
| `admin.py` | 21.9 | | 0.0000 |
| `security.py` | 19.0 | | 0.0513 |
| `qv-crypto.js` | 18.0 | | 0.0000 |
| `auth.py` | 15.4 | | 0.0000 |
| `facade.py` | 14.6 | | 0.0000 |
| `message.py` | 12.4 | | 0.0124 |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### views: auth (Cohesion: 0.44)

**14 files** in this community:

- `auth.py` (py, 14 symbols)
- `plans.py` (py, 10 symbols)
- `user.py` (py, 27 symbols)
- `email_tool.py` (py, 6 symbols)
- `makeadmin.py` (py, 5 symbols)
- `test_utils.py` (py, 3 symbols)
- `mailer.py` (py, 3 symbols)
- `utils.py` (py, 8 symbols)
- `auth.py` (py, 29 symbols)
- `faq.py` (py, 2 symbols)
- `file.py` (py, 3 symbols)
- `message.py` (py, 3 symbols)
- `subscription.py` (py, 4 symbols)
- `views.py` (py, 2 symbols)

### views: facade (Cohesion: 0.41)

**11 files** in this community:

- `app_factory.py` (py, 8 symbols)
- `facade.py` (py, 26 symbols)
- `sync.py` (py, 3 symbols)
- `test_account_facade.py` (py, 6 symbols)
- `test_cover.py` (py, 52 symbols)
- `test_facade.py` (py, 52 symbols)
- `about.py` (py, 1 symbols)
- `facade.py` (py, 6 symbols)
- `privacy.py` (py, 1 symbols)
- `terms.py` (py, 1 symbols)
- `wsgi.py` (py, 0 symbols)

### static/js (Cohesion: 0.89)

**9 files** in this community:

- `account.js` (js, 9 symbols)
- `login.js` (js, 2 symbols)
- `messages.js` (js, 6 symbols)
- `qv-crypto.js` (js, 40 symbols)
- `qv-deniable.js` (js, 7 symbols)
- `qv-padding.js` (js, 5 symbols)
- `recover.js` (js, 3 symbols)
- `register.js` (js, 3 symbols)
- `upload.js` (js, 6 symbols)

### controllers (Cohesion: 0.47)

**8 files** in this community:

- `app.py` (py, 2 symbols)
- `contact.py` (py, 4 symbols)
- `secure_channel.py` (py, 37 symbols)
- `contact.py` (py, 9 symbols)
- `superadmin_audit.py` (py, 5 symbols)
- `test_bloque1.py` (py, 8 symbols)
- `test_secure_channel.py` (py, 67 symbols)
- `admin.py` (py, 19 symbols)

### views: deniable_vault (Cohesion: 0.50)

**8 files** in this community:

- `deniable_vault.py` (py, 22 symbols)
- `deniable_vault.py` (py, 6 symbols)
- `conftest.py` (py, 8 symbols)
- `test_deniable_vault.py` (py, 55 symbols)
- `test_security.py` (py, 8 symbols)
- `security.py` (py, 10 symbols)
- `account.py` (py, 5 symbols)
- `sync.py` (py, 2 symbols)

### utils (Cohesion: 0.47)

**8 files** in this community:

- `file.py` (py, 9 symbols)
- `message.py` (py, 4 symbols)
- `message.py` (py, 6 symbols)
- `test_padding.py` (py, 24 symbols)
- `test_srp.py` (py, 6 symbols)
- `__init__.py` (py, 0 symbols)
- `padding.py` (py, 13 symbols)
- `scheduler.py` (py, 5 symbols)

### tools (Cohesion: 0.67)

**4 files** in this community:

- `test_integrity.py` (py, 6 symbols)
- `generate_sri.py` (py, 5 symbols)
- `verify_build.py` (py, 11 symbols)
- `integrity.py` (py, 8 symbols)

---

## Surprising Connections

Files in different communities connected through 3+ indirect hops.

- `contact.py` <-> `account.js` (9 hops, across 4 communities)
- `contact.py` <-> `account.js` (8 hops, across 4 communities)
- `deniable_vault.py` <-> `account.js` (8 hops, across 4 communities)
- `facade.py` <-> `account.js` (8 hops, across 3 communities)
- `secure_channel.py` <-> `account.js` (8 hops, across 4 communities)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does app_factory.py depend on, and what depends on it? (24 connections)
- What does user.py depend on, and what depends on it? (14 connections)
- What does utils.py depend on, and what depends on it? (14 connections)
- How are the 14 files in 'views: auth' related to each other?
- Why are contact.py and account.js connected through 9 hops across 4 communities?

---

## Taint Propagation Map

Taint analysis traces how dangerous imports propagate through the codebase via transitive dependencies. Source files import dangerous modules directly; sink files receive the danger indirectly.

**Taint Sources:** 5 | **Taint Sinks:** 18 | **Propagation Paths:** 20

- `secure_channel.py` imports `subprocess` (0 hop to `secure_channel.py`) [high]
  Path: secure_channel.py
- `doctor.py` imports `subprocess` (0 hop to `doctor.py`) [high]
  Path: doctor.py
- `doctor.py` imports `urllib.request` (0 hop to `doctor.py`) [medium]
  Path: doctor.py
- `test_secure_channel.py` imports `subprocess` (0 hop to `test_secure_channel.py`) [high]
  Path: test_secure_channel.py
- `test_secure_channel.py` imports `subprocess` (1 hop to `admin.py`) [high]
  Path: test_secure_channel.py -> admin.py
- `test_secure_channel.py` imports `subprocess` (1 hop to `secure_channel.py`) [high]
  Path: test_secure_channel.py -> secure_channel.py
- `test_secure_channel.py` imports `subprocess` (2 hops to `utils.py`) [high]
  Path: test_secure_channel.py -> admin.py -> utils.py
- `test_secure_channel.py` imports `subprocess` (2 hops to `superadmin_audit.py`) [high]
  Path: test_secure_channel.py -> admin.py -> superadmin_audit.py
- `test_secure_channel.py` imports `subprocess` (2 hops to `contact.py`) [high]
  Path: test_secure_channel.py -> admin.py -> contact.py
- `test_secure_channel.py` imports `subprocess` (2 hops to `user.py`) [high]
  Path: test_secure_channel.py -> admin.py -> user.py
- `test_secure_channel.py` imports `subprocess` (2 hops to `auth.py`) [high]
  Path: test_secure_channel.py -> admin.py -> auth.py
- `test_secure_channel.py` imports `subprocess` (2 hops to `plans.py`) [high]
  Path: test_secure_channel.py -> admin.py -> plans.py
- `test_secure_channel.py` imports `subprocess` (3 hops to `contact.py`) [high]
  Path: test_secure_channel.py -> admin.py -> contact.py -> contact.py
- `test_secure_channel.py` imports `subprocess` (3 hops to `mailer.py`) [high]
  Path: test_secure_channel.py -> admin.py -> auth.py -> mailer.py
- `test_secure_channel.py` imports `subprocess` (3 hops to `security.py`) [high]
  Path: test_secure_channel.py -> admin.py -> auth.py -> security.py
- `test_secure_channel.py` imports `subprocess` (3 hops to `auth.py`) [high]
  Path: test_secure_channel.py -> admin.py -> auth.py -> auth.py
- `test_secure_channel.py` imports `subprocess` (4 hops to `__init__.py`) [high]
  Path: test_secure_channel.py -> admin.py -> auth.py -> auth.py -> __init__.py
- `generate_sri.py` imports `urllib.request` (0 hop to `generate_sri.py`) [medium]
  Path: generate_sri.py
- `generate_sri.py` imports `urllib.request` (1 hop to `integrity.py`) [medium]
  Path: generate_sri.py -> integrity.py
- `mutation_test.py` imports `subprocess` (0 hop to `mutation_test.py`) [high]
  Path: mutation_test.py

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `garage-init.sh` | 0.015 | 0.000 | 0.006 | 1 | 0 |
| `mailer.py` | 0.045 | 0.032 | 0.037 | 3 | 7 |
| `padding.py` | 0.194 | 0.055 | 0.111 | 13 | 12 |
| `security.py` | 0.149 | 0.111 | 0.126 | 10 | 24 |
| `test_auth_phone.py` | 0.045 | 0.005 | 0.021 | 3 | 1 |
| `message.py` | 0.060 | 0.069 | 0.065 | 4 | 15 |
| `deniable_vault.py` | 0.090 | 0.032 | 0.055 | 6 | 7 |
| `integrity.py` | 0.119 | 0.051 | 0.078 | 8 | 11 |
| `superadmin_audit.py` | 0.075 | 0.018 | 0.041 | 5 | 4 |
| `account.py` | 0.075 | 0.065 | 0.069 | 5 | 14 |
| `qv-crypto.js` | 0.597 | 1.000 | 0.839 | 40 | 217 |
| `test_secure_channel.py` | 1.000 | 0.115 | 0.469 | 67 | 25 |
| `test_deniable_vault.py` | 0.821 | 0.055 | 0.361 | 55 | 12 |
| `test_facade.py` | 0.776 | 0.046 | 0.338 | 52 | 10 |
| `test_cover.py` | 0.776 | 0.032 | 0.330 | 52 | 7 |

---

## Dataflow Analysis

Procedural intra-function dataflow findings (zero tokens, regex-based heuristics, all INFERRED). Each lead is grounded at file:line for manual review.

**3 findings** (UNCHECKED_ALLOC: 3).

| File | Function | Line | Kind | Variable | Description |
|------|----------|------|------|----------|-------------|
| `tests/test_secure_channel.py` | `test_env_template_documents_channel_keys` | 141 | `UNCHECKED_ALLOC` | `text` | Result of allocator stored in `text` is never checked against NULL. |
| `tests/test_secure_channel.py` | `test_superadmin_channel_section_is_readable` | 687 | `UNCHECKED_ALLOC` | `text` | Result of allocator stored in `text` is never checked against NULL. |
| `tests/test_secure_channel.py` | `test_s3_probe_detects_live_endpoint` | 777 | `UNCHECKED_ALLOC` | `server` | Result of allocator stored in `server` is never checked against NULL. |

---

## Concept Graph

Semantic second-brain layer: nouns are concept nodes, verbs are edges. Each noun maps atomically to a file set (EXTRACTED); each verb aggregates structural imports, calls, and inherits into consumes, invokes, extends, depends_on, or bridges (INFERRED).

**50 concepts, 100 relations.**

| Concept | Files | Mentions |
|---------|-------|----------|
| `never` | 38 | 79 |
| `server` | 37 | 99 |
| `only` | 37 | 76 |
| `user` | 33 | 195 |
| `when` | 31 | 55 |
| `key` | 30 | 157 |
| `return` | 30 | 112 |
| `path` | 30 | 77 |
| `not` | 29 | 82 |
| `every` | 28 | 75 |
| `its` | 28 | 40 |
| `file` | 27 | 81 |
| `page` | 26 | 50 |
| `returns` | 25 | 70 |
| `get` | 25 | 64 |
| `one` | 25 | 62 |
| `which` | 24 | 33 |
| `client` | 23 | 58 |
| `browser` | 23 | 44 |
| `build` | 23 | 41 |
| `without` | 23 | 37 |
| `value` | 22 | 47 |
| `any` | 22 | 34 |
| `code` | 21 | 86 |
| `vault` | 21 | 81 |
| `json` | 21 | 43 |
| `static` | 21 | 28 |
| `zero` | 20 | 32 |
| `args` | 19 | 72 |
| `account` | 19 | 65 |

### Verb Edges

| Source | Verb | Target | Strength | Evidence |
|--------|------|--------|----------|----------|
| `user` | `depends_on` | `never` | 1.00 | 10 |
| `user` | `depends_on` | `one` | 0.92 | 10 |
| `user` | `depends_on` | `only` | 0.92 | 10 |
| `user` | `depends_on` | `return` | 0.92 | 10 |
| `server` | `depends_on` | `never` | 0.91 | 10 |
| `not` | `depends_on` | `never` | 0.88 | 10 |
| `user` | `depends_on` | `when` | 0.88 | 10 |
| `server` | `depends_on` | `one` | 0.86 | 10 |
| `user` | `depends_on` | `path` | 0.86 | 10 |
| `not` | `depends_on` | `return` | 0.85 | 10 |
| `only` | `depends_on` | `never` | 0.85 | 10 |
| `server` | `depends_on` | `only` | 0.85 | 10 |
| `user` | `depends_on` | `server` | 0.85 | 10 |
| `never` | `depends_on` | `one` | 0.82 | 10 |
| `not` | `depends_on` | `only` | 0.82 | 10 |
| `only` | `depends_on` | `one` | 0.82 | 10 |
| `server` | `depends_on` | `return` | 0.82 | 10 |
| `user` | `depends_on` | `used` | 0.82 | 10 |
| `not` | `depends_on` | `one` | 0.80 | 10 |
| `only` | `depends_on` | `return` | 0.80 | 10 |
| `server` | `depends_on` | `when` | 0.80 | 10 |
| `user` | `depends_on` | `returns` | 0.80 | 10 |
| `not` | `depends_on` | `when` | 0.78 | 10 |
| `user` | `depends_on` | `args` | 0.78 | 10 |
| `every` | `depends_on` | `never` | 0.77 | 10 |
| `return` | `depends_on` | `never` | 0.77 | 10 |
| `user` | `depends_on` | `code` | 0.77 | 10 |
| `user` | `depends_on` | `every` | 0.77 | 10 |
| `user` | `depends_on` | `value` | 0.77 | 10 |
| `user` | `depends_on` | `which` | 0.77 | 10 |

### Dialectic Prompts

- Thesis: `accepts` centralizes 18 files; Antithesis: `code` pulls 21 files with 10 shared (Jaccard 0.34); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `accepts` centralizes 18 files; Antithesis: `every` pulls 28 files with 11 shared (Jaccard 0.31); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `accepts` centralizes 18 files; Antithesis: `its` pulls 28 files with 12 shared (Jaccard 0.35); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `accepts` centralizes 18 files; Antithesis: `one` pulls 25 files with 11 shared (Jaccard 0.34); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `accepts` centralizes 18 files; Antithesis: `when` pulls 31 files with 13 shared (Jaccard 0.36); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `accepts` centralizes 18 files; Antithesis: `without` pulls 23 files with 11 shared (Jaccard 0.37); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `account` centralizes 19 files; Antithesis: `can` pulls 17 files with 10 shared (Jaccard 0.38); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `account` centralizes 19 files; Antithesis: `code` pulls 21 files with 12 shared (Jaccard 0.43); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `account` centralizes 19 files; Antithesis: `controller` pulls 18 files with 9 shared (Jaccard 0.32); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `account` centralizes 19 files; Antithesis: `database` pulls 17 files with 9 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?

---

## Dependency Cycles

Circular dependencies detected in the resolved import graph. Cycles increase coupling and make refactoring harder.

| Cycle | Length | Files |
|-------|--------|-------|
| `qv-crypto.js -> register.js -> qv-crypto.js` | 2 | 2 |
| `qv-crypto.js -> login.js -> qv-crypto.js` | 2 | 2 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `utils.py` | 14 | 16 | 30 |
| `padding.py` | 5 | 18 | 23 |
| `user.py` | 14 | 8 | 22 |
| `security.py` | 8 | 14 | 22 |
| `__init__.py` | 3 | 14 | 17 |
| `mailer.py` | 4 | 13 | 17 |
| `plans.py` | 4 | 12 | 16 |
| `contact.py` | 1 | 14 | 15 |
| `auth.py` | 1 | 13 | 14 |
| `contact.py` | 2 | 12 | 14 |
| `auth.py` | 5 | 8 | 13 |
| `message.py` | 2 | 10 | 12 |
| `deniable_vault.py` | 3 | 8 | 11 |
| `integrity.py` | 4 | 7 | 11 |
| `deniable_vault.py` | 2 | 8 | 10 |

---

## Architecture Violations

Violations of architectural layer rules detected in the import graph. **24 strict violations, 0 warnings.**

| Source | Source Layer | Target | Target Layer | Description | Severity |
|--------|-------------|--------|-------------|-------------|----------|
| `test_bloque1.py` | testing | `user.py` | presentation | testing must not import presentation | strict |
| `test_bloque1.py` | testing | `admin.py` | presentation | testing must not import presentation | strict |
| `conftest.py` | testing | `app_factory.py` | presentation | testing must not import presentation | strict |
| `conftest.py` | testing | `security.py` | presentation | testing must not import presentation | strict |
| `test_account_facade.py` | testing | `app_factory.py` | presentation | testing must not import presentation | strict |
| `test_account_facade.py` | testing | `facade.py` | presentation | testing must not import presentation | strict |
| `test_account_facade.py` | testing | `user.py` | presentation | testing must not import presentation | strict |
| `test_cover.py` | testing | `app_factory.py` | presentation | testing must not import presentation | strict |
| `test_cover.py` | testing | `facade.py` | presentation | testing must not import presentation | strict |
| `test_deniable_vault.py` | testing | `deniable_vault.py` | presentation | testing must not import presentation | strict |
| `test_deniable_vault.py` | testing | `user.py` | presentation | testing must not import presentation | strict |
| `test_facade.py` | testing | `app_factory.py` | presentation | testing must not import presentation | strict |
| `test_facade.py` | testing | `facade.py` | presentation | testing must not import presentation | strict |
| `test_facade.py` | testing | `user.py` | presentation | testing must not import presentation | strict |
| `test_padding.py` | testing | `file.py` | presentation | testing must not import presentation | strict |
| `test_padding.py` | testing | `message.py` | presentation | testing must not import presentation | strict |
| `test_secure_channel.py` | testing | `secure_channel.py` | presentation | testing must not import presentation | strict |
| `test_secure_channel.py` | testing | `admin.py` | presentation | testing must not import presentation | strict |
| `test_secure_channel.py` | testing | `admin.py` | presentation | testing must not import presentation | strict |
| `test_secure_channel.py` | testing | `admin.py` | presentation | testing must not import presentation | strict |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM006` | error | Hardcoded credential detected | multi | 3 |
| `RM001` | info | Large number of functions in py: 646 total | py | 646 |
| `RM002` | info | Large number of functions in go: 7 total | go | 7 |
| `RM003` | info | Large number of functions in sh: 4 total | sh | 4 |
| `RM004` | info | Large number of functions in js: 84 total | js | 84 |
| `RM005` | info | Print statement found (consider logging instead) | python | 81 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `__init__.py` (0 symbols, no doc)
- `client.go` (1 symbols, no doc)
- `client.py` (0 symbols, no doc)
- `__init__.py` (0 symbols, no doc)
- `enc_dec.go` (4 symbols, no doc)
- `make.sh` (0 symbols, no doc)
- `__init__.py` (0 symbols, no doc)
- `pq_decrypt_password.py` (0 symbols, no doc)
- `server.go` (2 symbols, no doc)
- `server.py` (0 symbols, no doc)
- `test.sh` (0 symbols, no doc)
- `__init__.py` (0 symbols, no doc)
- `__init__.py` (0 symbols, no doc)
- `__init__.py` (0 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    subgraph community_2 ["static/js"]
    static_js_qv_crypto_js["qv-crypto.js (js)"]
    class static_js_qv_crypto_js mod;
    static_js_qv_crypto_js_concatBytes["concatBytes"]
    class static_js_qv_crypto_js_concatBytes fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_concatBytes
    static_js_qv_crypto_js_hexToBytes["hexToBytes"]
    class static_js_qv_crypto_js_hexToBytes fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_hexToBytes
    static_js_qv_crypto_js_bytesToHex["bytesToHex"]
    class static_js_qv_crypto_js_bytesToHex fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_bytesToHex
    static_js_qv_crypto_js_bytesToBase64["bytesToBase64"]
    class static_js_qv_crypto_js_bytesToBase64 fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_bytesToBase64
    static_js_qv_crypto_js_bytesToBase32["bytesToBase32"]
    class static_js_qv_crypto_js_bytesToBase32 fn;
    static_js_qv_crypto_js --> static_js_qv_crypto_js_bytesToBase32
    static_js_account_js["account.js (js)"]
    class static_js_account_js mod;
    end
    subgraph community_1 ["views: facade"]
    app_factory_py["app_factory.py (py)"]
    class app_factory_py mod;
    static_js_upload_js["upload.js (js)"]
    class static_js_upload_js mod;
    static_js_qv_deniable_js["qv-deniable.js (js)"]
    class static_js_qv_deniable_js mod;
    static_js_messages_js["messages.js (js)"]
    class static_js_messages_js mod;
    end
    subgraph community_3 ["controllers"]
    views_admin_py["admin.py (py)"]
    class views_admin_py mod;
    static_js_recover_js["recover.js (js)"]
    class static_js_recover_js mod;
    static_js_register_js["register.js (js)"]
    class static_js_register_js mod;
    tests_test_secure_channel_py["test_secure_channel.py (py)"]
    class tests_test_secure_channel_py mod;
    end
    subgraph community_0 ["views: auth"]
    views_auth_py["auth.py (py)"]
    class views_auth_py mod;
    controllers_auth_py["auth.py (py)"]
    class controllers_auth_py mod;
    static_js_qv_padding_js["qv-padding.js (js)"]
    class static_js_qv_padding_js mod;
    static_js_login_js["login.js (js)"]
    class static_js_login_js mod;
    views_subscription_py["subscription.py (py)"]
    class views_subscription_py mod;
    static_js_coded_text_js["coded-text.js (js)"]
    class static_js_coded_text_js mod;
    end
    subgraph community_4 ["views: deniable_vault"]
    utils_security_py["security.py (py)"]
    class utils_security_py mod;
    controllers_secure_channel_py["secure_channel.py (py)"]
    class controllers_secure_channel_py mod;
    end
    subgraph community_5 ["utils"]
    utils_scheduler_py["scheduler.py (py)"]
    class utils_scheduler_py mod;
    enc_dec_go["enc_dec.go (go)"]
    class enc_dec_go mod;
    scripts_doctor_py["doctor.py (py)"]
    class scripts_doctor_py mod;
    views_account_py["account.py (py)"]
    class views_account_py mod;
    controllers_message_py["message.py (py)"]
    class controllers_message_py mod;
    tests_test_deniable_vault_py["test_deniable_vault.py (py)"]
    class tests_test_deniable_vault_py mod;
    controllers_deniable_vault_py["deniable_vault.py (py)"]
    class controllers_deniable_vault_py mod;
    views_message_py["message.py (py)"]
    class views_message_py mod;
    tests_test_padding_py["test_padding.py (py)"]
    class tests_test_padding_py mod;
    scripts_email_tool_py["email_tool.py (py)"]
    class scripts_email_tool_py mod;
    views_file_py["file.py (py)"]
    class views_file_py mod;
    tests_test_facade_py["test_facade.py (py)"]
    class tests_test_facade_py mod;
    controllers_facade_py["facade.py (py)"]
    class controllers_facade_py mod;
    end
    subgraph community_6 ["tools"]
    tools_verify_build_py["verify_build.py (py)"]
    class tools_verify_build_py mod;
    scripts_test_bloque1_py["test_bloque1.py (py)"]
    class scripts_test_bloque1_py mod;
    tests_conftest_py["conftest.py (py)"]
    class tests_conftest_py mod;
    enc_dec_py["enc_dec.py (py)"]
    class enc_dec_py mod;
    controllers_file_py["file.py (py)"]
    class controllers_file_py mod;
    models_contact_py["contact.py (py)"]
    class models_contact_py mod;
    tools_mutation_test_py["mutation_test.py (py)"]
    class tools_mutation_test_py mod;
    models_message_py["message.py (py)"]
    class models_message_py mod;
    tests_test_account_facade_py["test_account_facade.py (py)"]
    class tests_test_account_facade_py mod;
    tests_test_integrity_py["test_integrity.py (py)"]
    class tests_test_integrity_py mod;
    views_facade_py["facade.py (py)"]
    class views_facade_py mod;
    views_sync_py["sync.py (py)"]
    class views_sync_py mod;
    tools_generate_sri_py["generate_sri.py (py)"]
    class tools_generate_sri_py mod;
    views_views_py["views.py (py)"]
    class views_views_py mod;
    tests_test_cover_py["test_cover.py (py)"]
    class tests_test_cover_py mod;
    models_user_py["user.py (py)"]
    class models_user_py mod;
    utils_padding_py["padding.py (py)"]
    class utils_padding_py mod;
    utils_integrity_py["integrity.py (py)"]
    class utils_integrity_py mod;
    utils_utils_py["utils.py (py)"]
    class utils_utils_py mod;
    client_go["client.go (go)"]
    class client_go mod;
    client_py["client.py (py)"]
    class client_py mod;
    utils_srp6a_py["srp6a.py (py)"]
    class utils_srp6a_py mod;
    tests_test_security_py["test_security.py (py)"]
    class tests_test_security_py mod;
    app_py["app.py (py)"]
    class app_py mod;
    tests_test_doctor_py["test_doctor.py (py)"]
    class tests_test_doctor_py mod;
    tests_test_srp_py["test_srp.py (py)"]
    class tests_test_srp_py mod;
    scripts_makeadmin_py["makeadmin.py (py)"]
    class scripts_makeadmin_py mod;
    server_go["server.go (go)"]
    class server_go mod;
    views_faq_py["faq.py (py)"]
    class views_faq_py mod;
    server_py["server.py (py)"]
    class server_py mod;
    models_deniable_vault_py["deniable_vault.py (py)"]
    class models_deniable_vault_py mod;
    controllers_sync_py["sync.py (py)"]
    class controllers_sync_py mod;
    models_superadmin_audit_py["superadmin_audit.py (py)"]
    class models_superadmin_audit_py mod;
    utils_cache_py["cache.py (py)"]
    class utils_cache_py mod;
    controllers_contact_py["contact.py (py)"]
    class controllers_contact_py mod;
    tests_test_utils_py["test_utils.py (py)"]
    class tests_test_utils_py mod;
    utils_mailer_py["mailer.py (py)"]
    class utils_mailer_py mod;
    wsgi_py["wsgi.py (py)"]
    class wsgi_py mod;
    models_plans_py["plans.py (py)"]
    class models_plans_py mod;
    pq_decrypt_password_py["pq_decrypt_password.py (py)"]
    class pq_decrypt_password_py mod;
    tests_test_auth_phone_py["test_auth_phone.py (py)"]
    class tests_test_auth_phone_py mod;
    utils_plans_py["plans.py (py)"]
    class utils_plans_py mod;
    templates_terms_py["terms.py (py)"]
    class templates_terms_py mod;
    views_about_py["about.py (py)"]
    class views_about_py mod;
    views_privacy_py["privacy.py (py)"]
    class views_privacy_py mod;
    views_terms_py["terms.py (py)"]
    class views_terms_py mod;
    scripts_garage_native_sh["garage-native.sh (sh)"]
    class scripts_garage_native_sh mod;
    scripts_garage_init_sh["garage-init.sh (sh)"]
    class scripts_garage_init_sh mod;
    __init___py["__init__.py (py)"]
    class __init___py mod;
    controllers___init___py["__init__.py (py)"]
    class controllers___init___py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    make_sh["make.sh (sh)"]
    class make_sh mod;
    models___init___py["__init__.py (py)"]
    class models___init___py mod;
    test_sh["test.sh (sh)"]
    class test_sh mod;
    tests___init___py["__init__.py (py)"]
    class tests___init___py mod;
    utils___init___py["__init__.py (py)"]
    class utils___init___py mod;
    views___init___py["__init__.py (py)"]
    class views___init___py mod;
    end
    app_py -- resolved_imports --> app_factory_py
    app_py -- resolved_imports --> utils_utils_py
    app_factory_py -- resolved_imports --> controllers_file_py
    app_factory_py -- resolved_imports --> controllers_sync_py
    app_factory_py -- resolved_imports --> models_user_py
    app_factory_py -- resolved_imports --> utils_integrity_py
    app_factory_py -- resolved_imports --> utils_utils_py
    app_factory_py -- resolved_imports --> views_about_py
    app_factory_py -- resolved_imports --> views_account_py
    app_factory_py -- resolved_imports --> views_admin_py
    app_factory_py -- resolved_imports --> views_auth_py
    app_factory_py -- resolved_imports --> views_faq_py
    app_factory_py -- resolved_imports --> views_file_py
    app_factory_py -- resolved_imports --> views_message_py
    app_factory_py -- resolved_imports --> views_privacy_py
    app_factory_py -- resolved_imports --> views_sync_py
    app_factory_py -- resolved_imports --> views_terms_py
    app_factory_py -- resolved_imports --> views_views_py
    app_factory_py -- resolved_imports --> views_facade_py
    app_factory_py -- resolved_imports --> views_subscription_py
    controllers_auth_py -- resolved_imports --> models_user_py
    controllers_auth_py -- resolved_imports --> models_plans_py
    controllers_auth_py -- resolved_imports --> utils___init___py
    controllers_auth_py -- resolved_imports --> utils_mailer_py
    controllers_auth_py -- resolved_imports --> utils_utils_py
    controllers_auth_py -- resolved_imports --> utils_security_py
    controllers_contact_py -- resolved_imports --> models_contact_py
    controllers_deniable_vault_py -- resolved_imports --> models_deniable_vault_py
    controllers_deniable_vault_py -- resolved_imports --> utils_security_py
    controllers_facade_py -- resolved_imports --> utils_security_py
    controllers_file_py -- resolved_imports --> utils_utils_py
    controllers_file_py -- resolved_imports --> utils_padding_py
    controllers_message_py -- resolved_imports --> models_message_py
    controllers_message_py -- resolved_imports --> models_user_py
    controllers_message_py -- resolved_imports --> utils_utils_py
    controllers_message_py -- resolved_imports --> utils_padding_py
    scripts_email_tool_py -- resolved_imports --> models_user_py
    scripts_email_tool_py -- resolved_imports --> utils_mailer_py
    scripts_email_tool_py -- resolved_imports --> utils_utils_py
    scripts_makeadmin_py -- resolved_imports --> models_user_py
    scripts_test_bloque1_py -- resolved_imports --> app_py
    scripts_test_bloque1_py -- resolved_imports --> models_user_py
    scripts_test_bloque1_py -- resolved_imports --> views_admin_py
    static_js_account_js -- resolved_imports --> static_js_qv_deniable_js
    static_js_login_js -- resolved_imports --> static_js_qv_crypto_js
    static_js_messages_js -- resolved_imports --> static_js_qv_crypto_js
    static_js_qv_crypto_js -- resolved_imports --> static_js_qv_padding_js
    static_js_qv_crypto_js -- resolved_imports --> static_js_register_js
    static_js_qv_crypto_js -- resolved_imports --> static_js_login_js
    static_js_qv_deniable_js -- resolved_imports --> static_js_qv_crypto_js
    static_js_qv_padding_js -- resolved_imports --> utils_padding_py
    static_js_recover_js -- resolved_imports --> static_js_qv_crypto_js
    static_js_register_js -- resolved_imports --> static_js_qv_crypto_js
    static_js_upload_js -- resolved_imports --> static_js_qv_crypto_js
    tests_conftest_py -- resolved_imports --> app_factory_py
    tests_conftest_py -- resolved_imports --> utils_security_py
    tests_test_account_facade_py -- resolved_imports --> app_factory_py
    tests_test_account_facade_py -- resolved_imports --> controllers_facade_py
    tests_test_account_facade_py -- resolved_imports --> models_user_py
    tests_test_cover_py -- resolved_imports --> app_factory_py
    tests_test_cover_py -- resolved_imports --> controllers_facade_py
    tests_test_deniable_vault_py -- resolved_imports --> controllers_deniable_vault_py
    tests_test_deniable_vault_py -- resolved_imports --> models_deniable_vault_py
    tests_test_deniable_vault_py -- resolved_imports --> models_user_py
    tests_test_facade_py -- resolved_imports --> app_factory_py
    tests_test_facade_py -- resolved_imports --> controllers_facade_py
    tests_test_facade_py -- resolved_imports --> models_user_py
    tests_test_integrity_py -- resolved_imports --> utils_integrity_py
    tests_test_integrity_py -- resolved_imports --> tools_verify_build_py
    tests_test_padding_py -- resolved_imports --> controllers_file_py
    tests_test_padding_py -- resolved_imports --> controllers_message_py
    tests_test_padding_py -- resolved_imports --> utils___init___py
    tests_test_padding_py -- resolved_imports --> utils_padding_py
    tests_test_secure_channel_py -- resolved_imports --> controllers_secure_channel_py
    tests_test_secure_channel_py -- resolved_imports --> views_admin_py
    tests_test_secure_channel_py -- resolved_imports --> views_admin_py
    tests_test_secure_channel_py -- resolved_imports --> views_admin_py
    tests_test_secure_channel_py -- resolved_imports --> views_admin_py
    tests_test_secure_channel_py -- resolved_imports --> views_admin_py
    tests_test_security_py -- resolved_imports --> utils_security_py
    tests_test_srp_py -- resolved_imports --> utils___init___py
    tests_test_utils_py -- resolved_imports --> utils_utils_py
    tools_generate_sri_py -- resolved_imports --> utils_integrity_py
    tools_verify_build_py -- resolved_imports --> utils_integrity_py
    tools_verify_build_py -- resolved_imports --> utils_padding_py
    utils_scheduler_py -- resolved_imports --> models_message_py
    utils_scheduler_py -- resolved_imports --> models_user_py
    utils_scheduler_py -- resolved_imports --> utils_mailer_py
    utils_security_py -- resolved_imports --> utils_utils_py
    views_account_py -- resolved_imports --> controllers_deniable_vault_py
    views_account_py -- resolved_imports --> controllers_facade_py
    views_account_py -- resolved_imports --> models_deniable_vault_py
    views_account_py -- resolved_imports --> utils_security_py
    views_admin_py -- resolved_imports --> models_user_py
    views_admin_py -- resolved_imports --> models_plans_py
    views_admin_py -- resolved_imports --> utils_utils_py
    views_admin_py -- resolved_imports --> views_auth_py
    views_admin_py -- resolved_imports --> controllers_contact_py
    views_admin_py -- resolved_imports --> controllers_secure_channel_py
    views_admin_py -- resolved_imports --> models_superadmin_audit_py
    ext_os["os"]
    class ext_os ext;
    app_py -.->|imports| ext_os
    ext_sys["sys"]
    class ext_sys ext;
    app_py -.->|imports| ext_sys
    ext_app_factory["app_factory"]
    class ext_app_factory ext;
    app_py -.->|imports| ext_app_factory
    ext_utils_utils["utils.utils"]
    class ext_utils_utils ext;
    app_py -.->|imports| ext_utils_utils
    ext___future__["__future__"]
    class ext___future__ ext;
    app_factory_py -.->|imports| ext___future__
    ext_json["json"]
    class ext_json ext;
    app_factory_py -.->|imports| ext_json
    ext_logging["logging"]
    class ext_logging ext;
    app_factory_py -.->|imports| ext_logging
    app_factory_py -.->|imports| ext_os
    ext_secrets["secrets"]
    class ext_secrets ext;
    app_factory_py -.->|imports| ext_secrets
    app_factory_py -.->|imports| ext_sys
    ext_datetime["datetime"]
    class ext_datetime ext;
    app_factory_py -.->|imports| ext_datetime
    ext_typing["typing"]
    class ext_typing ext;
    app_factory_py -.->|imports| ext_typing
    ext_boto3["boto3"]
    class ext_boto3 ext;
    app_factory_py -.->|imports| ext_boto3
    ext_botocore_config["botocore.config"]
    class ext_botocore_config ext;
    app_factory_py -.->|imports| ext_botocore_config
    ext_flask["flask"]
    class ext_flask ext;
    app_factory_py -.->|imports| ext_flask
    ext_flask_cors["flask_cors"]
    class ext_flask_cors ext;
    app_factory_py -.->|imports| ext_flask_cors
    ext_flask_limiter["flask_limiter"]
    class ext_flask_limiter ext;
    app_factory_py -.->|imports| ext_flask_limiter
    ext_flask_limiter_util["flask_limiter.util"]
    class ext_flask_limiter_util ext;
    app_factory_py -.->|imports| ext_flask_limiter_util
    ext_flask_login["flask_login"]
    class ext_flask_login ext;
    app_factory_py -.->|imports| ext_flask_login
    ext_flask_mail["flask_mail"]
    class ext_flask_mail ext;
    app_factory_py -.->|imports| ext_flask_mail
    ext_flask_talisman["flask_talisman"]
    class ext_flask_talisman ext;
    app_factory_py -.->|imports| ext_flask_talisman
    ext_flask_wtf_csrf["flask_wtf.csrf"]
    class ext_flask_wtf_csrf ext;
    app_factory_py -.->|imports| ext_flask_wtf_csrf
    ext_werkzeug_middleware_proxy_fix["werkzeug.middleware.proxy_fix"]
    class ext_werkzeug_middleware_proxy_fix ext;
    app_factory_py -.->|imports| ext_werkzeug_middleware_proxy_fix
    ext_controllers_file["controllers.file"]
    class ext_controllers_file ext;
    app_factory_py -.->|imports| ext_controllers_file
    ext_controllers_sync["controllers.sync"]
    class ext_controllers_sync ext;
    app_factory_py -.->|imports| ext_controllers_sync
    ext_models_user["models.user"]
    class ext_models_user ext;
    app_factory_py -.->|imports| ext_models_user
    ext_utils_integrity["utils.integrity"]
    class ext_utils_integrity ext;
    app_factory_py -.->|imports| ext_utils_integrity
    app_factory_py -.->|imports| ext_utils_utils
    ext_views_about["views.about"]
    class ext_views_about ext;
    app_factory_py -.->|imports| ext_views_about
    ext_views_account["views.account"]
    class ext_views_account ext;
    app_factory_py -.->|imports| ext_views_account
    ext_views_admin["views.admin"]
    class ext_views_admin ext;
    app_factory_py -.->|imports| ext_views_admin
    ext_views_auth["views.auth"]
    class ext_views_auth ext;
    app_factory_py -.->|imports| ext_views_auth
    ext_views_faq["views.faq"]
    class ext_views_faq ext;
    app_factory_py -.->|imports| ext_views_faq
    ext_views_file["views.file"]
    class ext_views_file ext;
    app_factory_py -.->|imports| ext_views_file
    ext_views_message["views.message"]
    class ext_views_message ext;
    app_factory_py -.->|imports| ext_views_message
    ext_views_privacy["views.privacy"]
    class ext_views_privacy ext;
    app_factory_py -.->|imports| ext_views_privacy
    ext_views_sync["views.sync"]
    class ext_views_sync ext;
    app_factory_py -.->|imports| ext_views_sync
    ext_views_terms["views.terms"]
    class ext_views_terms ext;
    app_factory_py -.->|imports| ext_views_terms
    ext_views_views["views.views"]
    class ext_views_views ext;
    app_factory_py -.->|imports| ext_views_views
    ext_views_facade["views.facade"]
    class ext_views_facade ext;
    app_factory_py -.->|imports| ext_views_facade
    ext_views_subscription["views.subscription"]
    class ext_views_subscription ext;
    app_factory_py -.->|imports| ext_views_subscription
    ext_crypto_aes["aes"]
    class ext_crypto_aes ext;
    client_go -.->|imports| ext_crypto_aes
    ext_crypto_cipher["cipher"]
    class ext_crypto_cipher ext;
    client_go -.->|imports| ext_crypto_cipher
    ext_crypto_rand["rand"]
    class ext_crypto_rand ext;
    client_go -.->|imports| ext_crypto_rand
    ext_flag["flag"]
    class ext_flag ext;
    client_go -.->|imports| ext_flag
    ext_fmt["fmt"]
    class ext_fmt ext;
    client_go -.->|imports| ext_fmt
    ext_net["net"]
    class ext_net ext;
    client_go -.->|imports| ext_net
    ext_github_com_open_quantum_safe_liboqs_go_oqs["oqs"]
    class ext_github_com_open_quantum_safe_liboqs_go_oqs ext;
    client_go -.->|imports| ext_github_com_open_quantum_safe_liboqs_go_oqs
    ext_argparse["argparse"]
    class ext_argparse ext;
    client_py -.->|imports| ext_argparse
    ext_socket["socket"]
    class ext_socket ext;
    client_py -.->|imports| ext_socket
    ext_oqs["oqs"]
    class ext_oqs ext;
    client_py -.->|imports| ext_oqs
    ext_cryptography_hazmat_primitives_ciphers_aead["cryptography.hazmat.primitives.ciphers.aead"]
    class ext_cryptography_hazmat_primitives_ciphers_aead ext;
    client_py -.->|imports| ext_cryptography_hazmat_primitives_ciphers_aead
    ext_cryptography_hazmat_primitives["cryptography.hazmat.primitives"]
    class ext_cryptography_hazmat_primitives ext;
    client_py -.->|imports| ext_cryptography_hazmat_primitives
    ext_cryptography_hazmat_primitives_kdf_pbkdf2["cryptography.hazmat.primitives.kdf.pbkdf2"]
    class ext_cryptography_hazmat_primitives_kdf_pbkdf2 ext;
    client_py -.->|imports| ext_cryptography_hazmat_primitives_kdf_pbkdf2
    client_py -.->|imports| ext_os
    controllers_auth_py -.->|imports| ext_os
    controllers_auth_py -.->|imports| ext_secrets
    controllers_auth_py -.->|imports| ext_datetime
    controllers_auth_py -.->|imports| ext_typing
    ext_pytz["pytz"]
    class ext_pytz ext;
    controllers_auth_py -.->|imports| ext_pytz
    controllers_auth_py -.->|imports| ext_flask
    controllers_auth_py -.->|imports| ext_flask_mail
    ext_clicksend_client["clicksend_client"]
    class ext_clicksend_client ext;
    controllers_auth_py -.->|imports| ext_clicksend_client
    controllers_auth_py -.->|imports| ext_clicksend_client
    ext_clicksend_client_rest["clicksend_client.rest"]
    class ext_clicksend_client_rest ext;
    controllers_auth_py -.->|imports| ext_clicksend_client_rest
    controllers_auth_py -.->|imports| ext_models_user
    ext_models_plans["models.plans"]
    class ext_models_plans ext;
    controllers_auth_py -.->|imports| ext_models_plans
    ext_utils["utils"]
    class ext_utils ext;
    controllers_auth_py -.->|imports| ext_utils
    ext_utils_mailer["utils.mailer"]
    class ext_utils_mailer ext;
    controllers_auth_py -.->|imports| ext_utils_mailer
    controllers_auth_py -.->|imports| ext_utils_utils
    ext_utils_security["utils.security"]
    class ext_utils_security ext;
    controllers_auth_py -.->|imports| ext_utils_security
    ext_models_contact["models.contact"]
    class ext_models_contact ext;
    controllers_contact_py -.->|imports| ext_models_contact
    controllers_contact_py -.->|imports| ext_flask
    controllers_deniable_vault_py -.->|imports| ext___future__
    ext_binascii["binascii"]
    class ext_binascii ext;
    controllers_deniable_vault_py -.->|imports| ext_binascii
    ext_base64["base64"]
    class ext_base64 ext;
    controllers_deniable_vault_py -.->|imports| ext_base64
    controllers_deniable_vault_py -.->|imports| ext_json
    controllers_deniable_vault_py -.->|imports| ext_os
    controllers_deniable_vault_py -.->|imports| ext_secrets
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    controllers_deniable_vault_py -.->|imports| ext_dataclasses
    controllers_deniable_vault_py -.->|imports| ext_typing
    ext_models_deniable_vault["models.deniable_vault"]
    class ext_models_deniable_vault ext;
    controllers_deniable_vault_py -.->|imports| ext_models_deniable_vault
    controllers_deniable_vault_py -.->|imports| ext_utils_security
    controllers_facade_py -.->|imports| ext___future__
    controllers_facade_py -.->|imports| ext_os
    controllers_facade_py -.->|imports| ext_dataclasses
    ext_enum["enum"]
    class ext_enum ext;
    controllers_facade_py -.->|imports| ext_enum
    controllers_facade_py -.->|imports| ext_typing
    ext_argon2["argon2"]
    class ext_argon2 ext;
    controllers_facade_py -.->|imports| ext_argon2
    ext_argon2_exceptions["argon2.exceptions"]
    class ext_argon2_exceptions ext;
    controllers_facade_py -.->|imports| ext_argon2_exceptions
    ext_itsdangerous["itsdangerous"]
    class ext_itsdangerous ext;
    controllers_facade_py -.->|imports| ext_itsdangerous
    controllers_facade_py -.->|imports| ext_utils_security
    controllers_file_py -.->|imports| ext_os
    controllers_file_py -.->|imports| ext_typing
    controllers_file_py -.->|imports| ext_flask
    ext_werkzeug_utils["werkzeug.utils"]
    class ext_werkzeug_utils ext;
    controllers_file_py -.->|imports| ext_werkzeug_utils
    ext_utils_padding["utils.padding"]
    class ext_utils_padding ext;
    controllers_file_py -.->|imports| ext_utils_padding
    controllers_file_py -.->|imports| ext_boto3
    ext_botocore_exceptions["botocore.exceptions"]
    class ext_botocore_exceptions ext;
    controllers_file_py -.->|imports| ext_botocore_exceptions
    controllers_message_py -.->|imports| ext_typing
    ext_models_message["models.message"]
    class ext_models_message ext;
    controllers_message_py -.->|imports| ext_models_message
    controllers_message_py -.->|imports| ext_models_user
    controllers_message_py -.->|imports| ext_utils_utils
    controllers_message_py -.->|imports| ext_utils_padding
    controllers_message_py -.->|imports| ext_base64
    controllers_message_py -.->|imports| ext_binascii
    ext_uuid["uuid"]
    class ext_uuid ext;
    controllers_message_py -.->|imports| ext_uuid
    controllers_message_py -.->|imports| ext_flask
    controllers_secure_channel_py -.->|imports| ext___future__
    ext_hashlib["hashlib"]
    class ext_hashlib ext;
    controllers_secure_channel_py -.->|imports| ext_hashlib
    controllers_secure_channel_py -.->|imports| ext_json
    controllers_secure_channel_py -.->|imports| ext_os
    ext_re["re"]
    class ext_re ext;
    controllers_secure_channel_py -.->|imports| ext_re
    ext_shutil["shutil"]
    class ext_shutil ext;
    controllers_secure_channel_py -.->|imports| ext_shutil
    ext_signal["signal"]
    class ext_signal ext;
    controllers_secure_channel_py -.->|imports| ext_signal
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    controllers_secure_channel_py -.->|imports| ext_subprocess
    ext_tempfile["tempfile"]
    class ext_tempfile ext;
    controllers_secure_channel_py -.->|imports| ext_tempfile
    controllers_secure_channel_py -.->|imports| ext_dataclasses
    controllers_secure_channel_py -.->|imports| ext_enum
    ext_pathlib["pathlib"]
    class ext_pathlib ext;
    controllers_secure_channel_py -.->|imports| ext_pathlib
    controllers_secure_channel_py -.->|imports| ext_typing
    ext_time["time"]
    class ext_time ext;
    controllers_secure_channel_py -.->|imports| ext_time
    controllers_secure_channel_py -.->|imports| ext_time
    controllers_sync_py -.->|imports| ext_os
    controllers_sync_py -.->|imports| ext_flask
    controllers_sync_py -.->|imports| ext_boto3
    controllers_sync_py -.->|imports| ext_botocore_exceptions
    ext_archive_tar["tar"]
    class ext_archive_tar ext;
    enc_dec_go -.->|imports| ext_archive_tar
    ext_compress_gzip["gzip"]
    class ext_compress_gzip ext;
    enc_dec_go -.->|imports| ext_compress_gzip
    enc_dec_go -.->|imports| ext_crypto_aes
    enc_dec_go -.->|imports| ext_crypto_cipher
    enc_dec_go -.->|imports| ext_crypto_rand
    enc_dec_go -.->|imports| ext_flag
    enc_dec_go -.->|imports| ext_fmt
    ext_io["io"]
    class ext_io ext;
    enc_dec_go -.->|imports| ext_io
    enc_dec_go -.->|imports| ext_os
    ext_path_filepath["filepath"]
    class ext_path_filepath ext;
    enc_dec_go -.->|imports| ext_path_filepath
    ext_strings["strings"]
    class ext_strings ext;
    enc_dec_go -.->|imports| ext_strings
    enc_dec_go -.->|imports| ext_github_com_open_quantum_safe_liboqs_go_oqs
    ext_golang_org_x_crypto_pbkdf2["pbkdf2"]
    class ext_golang_org_x_crypto_pbkdf2 ext;
    enc_dec_go -.->|imports| ext_golang_org_x_crypto_pbkdf2
    ext_crypto_sha256["sha256"]
    class ext_crypto_sha256 ext;
    enc_dec_go -.->|imports| ext_crypto_sha256
    enc_dec_py -.->|imports| ext_argparse
    enc_dec_py -.->|imports| ext_os
    enc_dec_py -.->|imports| ext_io
    enc_dec_py -.->|imports| ext_oqs
    enc_dec_py -.->|imports| ext_cryptography_hazmat_primitives_ciphers_aead
    enc_dec_py -.->|imports| ext_cryptography_hazmat_primitives_kdf_pbkdf2
    enc_dec_py -.->|imports| ext_cryptography_hazmat_primitives
    enc_dec_py -.->|imports| ext_boto3
    enc_dec_py -.->|imports| ext_botocore_exceptions
    enc_dec_py -.->|imports| ext_pathlib
    ext_pydantic["pydantic"]
    class ext_pydantic ext;
    models_contact_py -.->|imports| ext_pydantic
    models_contact_py -.->|imports| ext_typing
    ext_sqlite3["sqlite3"]
    class ext_sqlite3 ext;
    models_contact_py -.->|imports| ext_sqlite3
    models_contact_py -.->|imports| ext_datetime
    models_contact_py -.->|imports| ext_pytz
    models_contact_py -.->|imports| ext_flask
    models_contact_py -.->|imports| ext_flask
    models_contact_py -.->|imports| ext_flask
    models_contact_py -.->|imports| ext_flask
    models_deniable_vault_py -.->|imports| ext___future__
    models_deniable_vault_py -.->|imports| ext_sqlite3
    models_deniable_vault_py -.->|imports| ext_datetime
    models_deniable_vault_py -.->|imports| ext_typing
    models_message_py -.->|imports| ext_pydantic
    models_message_py -.->|imports| ext_typing
    models_message_py -.->|imports| ext_os
    ext_glob["glob"]
    class ext_glob ext;
    models_message_py -.->|imports| ext_glob
    models_message_py -.->|imports| ext_base64
    models_message_py -.->|imports| ext_datetime
    models_message_py -.->|imports| ext_uuid
    models_message_py -.->|imports| ext_json
    models_message_py -.->|imports| ext_flask
    models_plans_py -.->|imports| ext_typing
    models_plans_py -.->|imports| ext_sqlite3
    models_superadmin_audit_py -.->|imports| ext_sqlite3
    models_superadmin_audit_py -.->|imports| ext_datetime
    models_superadmin_audit_py -.->|imports| ext_typing
    models_user_py -.->|imports| ext_pydantic
    models_user_py -.->|imports| ext_typing
    models_user_py -.->|imports| ext_flask_login
    models_user_py -.->|imports| ext_sqlite3
    models_user_py -.->|imports| ext_datetime
    models_user_py -.->|imports| ext_pytz
    models_user_py -.->|imports| ext_flask
    pq_decrypt_password_py -.->|imports| ext_argparse
    ext_utils_crypto["utils.crypto"]
    class ext_utils_crypto ext;
    pq_decrypt_password_py -.->|imports| ext_utils_crypto
    scripts_doctor_py -.->|imports| ext___future__
    scripts_doctor_py -.->|imports| ext_argparse
    ext_importlib["importlib"]
    class ext_importlib ext;
    scripts_doctor_py -.->|imports| ext_importlib
    scripts_doctor_py -.->|imports| ext_os
    ext_platform["platform"]
    class ext_platform ext;
    scripts_doctor_py -.->|imports| ext_platform
    scripts_doctor_py -.->|imports| ext_shutil
    scripts_doctor_py -.->|imports| ext_socket
    scripts_doctor_py -.->|imports| ext_subprocess
    scripts_doctor_py -.->|imports| ext_sys
    ext_urllib_request["urllib.request"]
    class ext_urllib_request ext;
    scripts_doctor_py -.->|imports| ext_urllib_request
    scripts_doctor_py -.->|imports| ext_dataclasses
    scripts_doctor_py -.->|imports| ext_pathlib
    scripts_doctor_py -.->|imports| ext_hashlib
    scripts_email_tool_py -.->|imports| ext_argparse
    scripts_email_tool_py -.->|imports| ext_os
    scripts_email_tool_py -.->|imports| ext_sys
    scripts_email_tool_py -.->|imports| ext_flask
    scripts_email_tool_py -.->|imports| ext_flask_mail
    scripts_email_tool_py -.->|imports| ext_models_user
    scripts_email_tool_py -.->|imports| ext_utils_mailer
    scripts_email_tool_py -.->|imports| ext_utils_utils
    scripts_makeadmin_py -.->|imports| ext_argparse
    scripts_makeadmin_py -.->|imports| ext_os
    scripts_makeadmin_py -.->|imports| ext_sys
    scripts_makeadmin_py -.->|imports| ext_models_user
    scripts_test_bloque1_py -.->|imports| ext_os
    scripts_test_bloque1_py -.->|imports| ext_sys
    scripts_test_bloque1_py -.->|imports| ext_shutil
    scripts_test_bloque1_py -.->|imports| ext_re
    ext_app["app"]
    class ext_app ext;
    scripts_test_bloque1_py -.->|imports| ext_app
    scripts_test_bloque1_py -.->|imports| ext_models_user
    scripts_test_bloque1_py -.->|imports| ext_views_admin
    server_go -.->|imports| ext_crypto_aes
    server_go -.->|imports| ext_crypto_cipher
    server_go -.->|imports| ext_fmt
    server_go -.->|imports| ext_net
    server_go -.->|imports| ext_github_com_open_quantum_safe_liboqs_go_oqs
    server_py -.->|imports| ext_socket
    server_py -.->|imports| ext_oqs
    server_py -.->|imports| ext_cryptography_hazmat_primitives_ciphers_aead
    server_py -.->|imports| ext_cryptography_hazmat_primitives
    server_py -.->|imports| ext_cryptography_hazmat_primitives_kdf_pbkdf2
    ext___qv_deniable_js["qv-deniable.js"]
    class ext___qv_deniable_js ext;
    static_js_account_js -.->|imports| ext___qv_deniable_js
    ext_notes["notes"]
    class ext_notes ext;
    static_js_account_js -.->|imports| ext_notes
    ext_present["present"]
    class ext_present ext;
    static_js_account_js -.->|imports| ext_present
    ext_setStatus["setStatus"]
    class ext_setStatus ext;
    static_js_account_js -.->|imports| ext_setStatus
    ext_getElementById["getElementById"]
    class ext_getElementById ext;
    static_js_account_js -.->|imports| ext_getElementById
    ext_add["add"]
    class ext_add ext;
    static_js_account_js -.->|imports| ext_add
    ext_csrfToken["csrfToken"]
    class ext_csrfToken ext;
    static_js_account_js -.->|imports| ext_csrfToken
    static_js_account_js -.->|imports| ext_getElementById
    ext_apiRequest["apiRequest"]
    class ext_apiRequest ext;
    static_js_account_js -.->|imports| ext_apiRequest
    static_js_account_js -.->|imports| ext_csrfToken
    ext_stringify["stringify"]
    class ext_stringify ext;
    static_js_account_js -.->|imports| ext_stringify
    ext_fetch["fetch"]
    class ext_fetch ext;
    static_js_account_js -.->|imports| ext_fetch
    static_js_account_js -.->|imports| ext_json
    ext_loadState["loadState"]
    class ext_loadState ext;
    static_js_account_js -.->|imports| ext_loadState
    static_js_account_js -.->|imports| ext_apiRequest
    ext_collectSlots["collectSlots"]
    class ext_collectSlots ext;
    static_js_account_js -.->|imports| ext_collectSlots
    static_js_account_js -.->|imports| ext_getElementById
    static_js_account_js -.->|imports| ext_getElementById
    static_js_account_js -.->|imports| ext_getElementById
    static_js_account_js -.->|imports| ext_getElementById
    ext_push["push"]
    class ext_push ext;
    static_js_account_js -.->|imports| ext_push
    ext_handleConfigure["handleConfigure"]
    class ext_handleConfigure ext;
    static_js_account_js -.->|imports| ext_handleConfigure
    ext_preventDefault["preventDefault"]
    class ext_preventDefault ext;
    static_js_account_js -.->|imports| ext_preventDefault
    static_js_account_js -.->|imports| ext_collectSlots
    static_js_account_js -.->|imports| ext_setStatus
    static_js_account_js -.->|imports| ext_setStatus
    static_js_account_js -.->|imports| ext_setStatus
    static_js_account_js -.->|imports| ext_setStatus
    ext_buildDeniableVault["buildDeniableVault"]
    class ext_buildDeniableVault ext;
    static_js_account_js -.->|imports| ext_buildDeniableVault
    static_js_account_js -.->|imports| ext_apiRequest
    static_js_account_js -.->|imports| ext_setStatus
    ext_reset["reset"]
    class ext_reset ext;
    static_js_account_js -.->|imports| ext_reset
    ext_error["error"]
    class ext_error ext;
    static_js_account_js -.->|imports| ext_error
    static_js_account_js -.->|imports| ext_setStatus
    ext_handleOpen["handleOpen"]
    class ext_handleOpen ext;
    static_js_account_js -.->|imports| ext_handleOpen
    static_js_account_js -.->|imports| ext_preventDefault
    static_js_account_js -.->|imports| ext_getElementById
    static_js_account_js -.->|imports| ext_getElementById
    static_js_account_js -.->|imports| ext_setStatus
    ext_openDeniableVault["openDeniableVault"]
    class ext_openDeniableVault ext;
    static_js_account_js -.->|imports| ext_openDeniableVault
    static_js_account_js -.->|imports| ext_setStatus
    static_js_account_js -.->|imports| ext_setStatus
    ext_handleReset["handleReset"]
    class ext_handleReset ext;
    static_js_account_js -.->|imports| ext_handleReset
    static_js_account_js -.->|imports| ext_apiRequest
    static_js_account_js -.->|imports| ext_loadState
    static_js_account_js -.->|imports| ext_setStatus
    static_js_account_js -.->|imports| ext_setStatus
    ext_init["init"]
    class ext_init ext;
    static_js_account_js -.->|imports| ext_init
    static_js_account_js -.->|imports| ext_getElementById
    static_js_account_js -.->|imports| ext_getElementById
    static_js_account_js -.->|imports| ext_getElementById
    ext_addEventListener["addEventListener"]
    class ext_addEventListener ext;
    static_js_account_js -.->|imports| ext_addEventListener
    static_js_account_js -.->|imports| ext_addEventListener
    static_js_account_js -.->|imports| ext_addEventListener
    static_js_account_js -.->|imports| ext_loadState
    static_js_account_js -.->|imports| ext_setStatus
    static_js_account_js -.->|imports| ext_addEventListener
    static_js_account_js -.->|imports| ext_init
    ext_randomChar["randomChar"]
    class ext_randomChar ext;
    static_js_coded_text_js -.->|imports| ext_randomChar
    ext_floor["floor"]
    class ext_floor ext;
    static_js_coded_text_js -.->|imports| ext_floor
    ext_random["random"]
    class ext_random ext;
    static_js_coded_text_js -.->|imports| ext_random
    ext_toUpperCase["toUpperCase"]
    class ext_toUpperCase ext;
    static_js_coded_text_js -.->|imports| ext_toUpperCase
    ext_animateElement["animateElement"]
    class ext_animateElement ext;
    static_js_coded_text_js -.->|imports| ext_animateElement
    ext_split["split"]
    class ext_split ext;
    static_js_coded_text_js -.->|imports| ext_split
    ext_contains["contains"]
    class ext_contains ext;
    static_js_coded_text_js -.->|imports| ext_contains
    ext_map["map"]
    class ext_map ext;
    static_js_coded_text_js -.->|imports| ext_map
    ext_join["join"]
    class ext_join ext;
    static_js_coded_text_js -.->|imports| ext_join
    ext_timeline["timeline"]
    class ext_timeline ext;
    static_js_coded_text_js -.->|imports| ext_timeline
    static_js_coded_text_js -.->|imports| ext_floor
    static_js_coded_text_js -.->|imports| ext_randomChar
    static_js_coded_text_js -.->|imports| ext_init
    ext_querySelectorAll["querySelectorAll"]
    class ext_querySelectorAll ext;
    static_js_coded_text_js -.->|imports| ext_querySelectorAll
    ext_forEach["forEach"]
    class ext_forEach ext;
    static_js_coded_text_js -.->|imports| ext_forEach
    static_js_coded_text_js -.->|imports| ext_addEventListener
    static_js_coded_text_js -.->|imports| ext_init
    ext___qv_crypto_js["qv-crypto.js"]
    class ext___qv_crypto_js ext;
    static_js_login_js -.->|imports| ext___qv_crypto_js
    ext_controller["controller"]
    class ext_controller ext;
    static_js_login_js -.->|imports| ext_controller
    ext_handleLogin["handleLogin"]
    class ext_handleLogin ext;
    static_js_login_js -.->|imports| ext_handleLogin
    static_js_login_js -.->|imports| ext_preventDefault
    ext_querySelector["querySelector"]
    class ext_querySelector ext;
    static_js_login_js -.->|imports| ext_querySelector
    static_js_login_js -.->|imports| ext_getElementById
    static_js_login_js -.->|imports| ext_getElementById
    static_js_login_js -.->|imports| ext_querySelector
    ext_alert["alert"]
    class ext_alert ext;
    static_js_login_js -.->|imports| ext_alert
    ext_login["login"]
    class ext_login ext;
    static_js_login_js -.->|imports| ext_login
    static_js_login_js -.->|imports| ext_error
    static_js_login_js -.->|imports| ext_alert
    static_js_login_js -.->|imports| ext_init
    static_js_login_js -.->|imports| ext_getElementById
    static_js_login_js -.->|imports| ext_addEventListener
    static_js_login_js -.->|imports| ext_addEventListener
    static_js_login_js -.->|imports| ext_init
    static_js_messages_js -.->|imports| ext___qv_crypto_js
    static_js_messages_js -.->|imports| ext_controller
    ext_textContent["textContent"]
    class ext_textContent ext;
    static_js_messages_js -.->|imports| ext_textContent
    ext_getCsrfToken["getCsrfToken"]
    class ext_getCsrfToken ext;
    static_js_messages_js -.->|imports| ext_getCsrfToken
    static_js_messages_js -.->|imports| ext_querySelector
    ext_handleSend["handleSend"]
    class ext_handleSend ext;
    static_js_messages_js -.->|imports| ext_handleSend
    static_js_messages_js -.->|imports| ext_preventDefault
    static_js_messages_js -.->|imports| ext_getElementById
    static_js_messages_js -.->|imports| ext_getElementById
    static_js_messages_js -.->|imports| ext_alert
    ext_sendSecureMessage["sendSecureMessage"]
    class ext_sendSecureMessage ext;
    static_js_messages_js -.->|imports| ext_sendSecureMessage
    static_js_messages_js -.->|imports| ext_error
    static_js_messages_js -.->|imports| ext_alert
    ext_collectEnvelopes["collectEnvelopes"]
    class ext_collectEnvelopes ext;
    static_js_messages_js -.->|imports| ext_collectEnvelopes
    ext_from["from"]
    class ext_from ext;
    static_js_messages_js -.->|imports| ext_from
    ext_parse["parse"]
    class ext_parse ext;
    static_js_messages_js -.->|imports| ext_parse
    static_js_messages_js -.->|imports| ext_push
    ext_envelope["envelope"]
    class ext_envelope ext;
    static_js_messages_js -.->|imports| ext_envelope
    ext_handleDecryptInbox["handleDecryptInbox"]
    class ext_handleDecryptInbox ext;
    static_js_messages_js -.->|imports| ext_handleDecryptInbox
    static_js_messages_js -.->|imports| ext_collectEnvelopes
    static_js_messages_js -.->|imports| ext_alert
    ext_prompt["prompt"]
    class ext_prompt ext;
    static_js_messages_js -.->|imports| ext_prompt
    ext_decryptInbox["decryptInbox"]
    class ext_decryptInbox ext;
    static_js_messages_js -.->|imports| ext_decryptInbox
    static_js_messages_js -.->|imports| ext_forEach
    static_js_messages_js -.->|imports| ext_error
    static_js_messages_js -.->|imports| ext_alert
    ext_initEditor["initEditor"]
    class ext_initEditor ext;
    static_js_messages_js -.->|imports| ext_initEditor
    static_js_messages_js -.->|imports| ext_getElementById
    ext_value["value"]
    class ext_value ext;
    static_js_messages_js -.->|imports| ext_value
    static_js_messages_js -.->|imports| ext_init
    static_js_messages_js -.->|imports| ext_getElementById
    static_js_messages_js -.->|imports| ext_addEventListener
    static_js_messages_js -.->|imports| ext_getElementById
    static_js_messages_js -.->|imports| ext_addEventListener
    static_js_messages_js -.->|imports| ext_handleDecryptInbox
    static_js_messages_js -.->|imports| ext_initEditor
    static_js_messages_js -.->|imports| ext_addEventListener
    static_js_messages_js -.->|imports| ext_init
    ext___vendor_sha2_js["sha2.js"]
    class ext___vendor_sha2_js ext;
    static_js_qv_crypto_js -.->|imports| ext___vendor_sha2_js
    ext___vendor_hkdf_js["hkdf.js"]
    class ext___vendor_hkdf_js ext;
    static_js_qv_crypto_js -.->|imports| ext___vendor_hkdf_js
    ext___vendor_ml_kem_js["ml_kem.js"]
    class ext___vendor_ml_kem_js ext;
    static_js_qv_crypto_js -.->|imports| ext___vendor_ml_kem_js
    ext___vendor_ed25519_js["ed25519.js"]
    class ext___vendor_ed25519_js ext;
    static_js_qv_crypto_js -.->|imports| ext___vendor_ed25519_js
    ext___qv_padding_js["qv-padding.js"]
    class ext___qv_padding_js ext;
    static_js_qv_crypto_js -.->|imports| ext___qv_padding_js
    ext_768["768"]
    class ext_768 ext;
    static_js_qv_crypto_js -.->|imports| ext_768
    ext_bucket["bucket"]
    class ext_bucket ext;
    static_js_qv_crypto_js -.->|imports| ext_bucket
    static_js_qv_crypto_js -.->|imports| ext_768
    ext_concatBytes["concatBytes"]
    class ext_concatBytes ext;
    static_js_qv_crypto_js -.->|imports| ext_concatBytes
    ext_reduce["reduce"]
    class ext_reduce ext;
    static_js_qv_crypto_js -.->|imports| ext_reduce
    ext_set["set"]
    class ext_set ext;
    static_js_qv_crypto_js -.->|imports| ext_set
    ext_hexToBytes["hexToBytes"]
    class ext_hexToBytes ext;
    static_js_qv_crypto_js -.->|imports| ext_hexToBytes
    ext_parseInt["parseInt"]
    class ext_parseInt ext;
    static_js_qv_crypto_js -.->|imports| ext_parseInt
    ext_bytesToHex["bytesToHex"]
    class ext_bytesToHex ext;
    static_js_qv_crypto_js -.->|imports| ext_bytesToHex
    ext_toString["toString"]
    class ext_toString ext;
    static_js_qv_crypto_js -.->|imports| ext_toString
    ext_padStart["padStart"]
    class ext_padStart ext;
    static_js_qv_crypto_js -.->|imports| ext_padStart
    ext_bytesToBase64["bytesToBase64"]
    class ext_bytesToBase64 ext;
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    ext_fromCharCode["fromCharCode"]
    class ext_fromCharCode ext;
    static_js_qv_crypto_js -.->|imports| ext_fromCharCode
    ext_btoa["btoa"]
    class ext_btoa ext;
    static_js_qv_crypto_js -.->|imports| ext_btoa
    ext_bytes["bytes"]
    class ext_bytes ext;
    static_js_qv_crypto_js -.->|imports| ext_bytes
    ext_bytesToBase32["bytesToBase32"]
    class ext_bytesToBase32 ext;
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase32
    ext_base64ToBytes["base64ToBytes"]
    class ext_base64ToBytes ext;
    static_js_qv_crypto_js -.->|imports| ext_base64ToBytes
    ext_atob["atob"]
    class ext_atob ext;
    static_js_qv_crypto_js -.->|imports| ext_atob
    ext_charCodeAt["charCodeAt"]
    class ext_charCodeAt ext;
    static_js_qv_crypto_js -.->|imports| ext_charCodeAt
    ext_bytesToBigInt["bytesToBigInt"]
    class ext_bytesToBigInt ext;
    static_js_qv_crypto_js -.->|imports| ext_bytesToBigInt
    ext_i2osp["i2osp"]
    class ext_i2osp ext;
    static_js_qv_crypto_js -.->|imports| ext_i2osp
    ext_mod["mod"]
    class ext_mod ext;
    static_js_qv_crypto_js -.->|imports| ext_mod
    ext_return["return"]
    class ext_return ext;
    static_js_qv_crypto_js -.->|imports| ext_return
    ext_modPow["modPow"]
    class ext_modPow ext;
    static_js_qv_crypto_js -.->|imports| ext_modPow
    static_js_qv_crypto_js -.->|imports| ext_mod
    static_js_qv_crypto_js -.->|imports| ext_bytes
    ext_randomBytes["randomBytes"]
    class ext_randomBytes ext;
    static_js_qv_crypto_js -.->|imports| ext_randomBytes
    ext_min["min"]
    class ext_min ext;
    static_js_qv_crypto_js -.->|imports| ext_min
    ext_getRandomValues["getRandomValues"]
    class ext_getRandomValues ext;
    static_js_qv_crypto_js -.->|imports| ext_getRandomValues
    ext_sha256["sha256"]
    class ext_sha256 ext;
    static_js_qv_crypto_js -.->|imports| ext_sha256
    static_js_qv_crypto_js -.->|imports| ext_bytesToBigInt
    ext_vault["vault"]
    class ext_vault ext;
    static_js_qv_crypto_js -.->|imports| ext_vault
    ext_deriveKeyFromPassphrase["deriveKeyFromPassphrase"]
    class ext_deriveKeyFromPassphrase ext;
    static_js_qv_crypto_js -.->|imports| ext_deriveKeyFromPassphrase
    ext_importKey["importKey"]
    class ext_importKey ext;
    static_js_qv_crypto_js -.->|imports| ext_importKey
    ext_deriveBits["deriveBits"]
    class ext_deriveBits ext;
    static_js_qv_crypto_js -.->|imports| ext_deriveBits
    ext_deriveMasterKey["deriveMasterKey"]
    class ext_deriveMasterKey ext;
    static_js_qv_crypto_js -.->|imports| ext_deriveMasterKey
    static_js_qv_crypto_js -.->|imports| ext_deriveKeyFromPassphrase
    ext_aesGcmEncrypt["aesGcmEncrypt"]
    class ext_aesGcmEncrypt ext;
    static_js_qv_crypto_js -.->|imports| ext_aesGcmEncrypt
    static_js_qv_crypto_js -.->|imports| ext_importKey
    static_js_qv_crypto_js -.->|imports| ext_randomBytes
    static_js_qv_crypto_js -.->|imports| ext_concatBytes
    ext_aesGcmDecrypt["aesGcmDecrypt"]
    class ext_aesGcmDecrypt ext;
    static_js_qv_crypto_js -.->|imports| ext_aesGcmDecrypt
    static_js_qv_crypto_js -.->|imports| ext_importKey
    ext_slice["slice"]
    class ext_slice ext;
    static_js_qv_crypto_js -.->|imports| ext_slice
    static_js_qv_crypto_js -.->|imports| ext_slice
    static_js_qv_crypto_js -.->|imports| ext_aesGcmEncrypt
    ext_separate["separate"]
    class ext_separate ext;
    static_js_qv_crypto_js -.->|imports| ext_separate
    ext_module["module"]
    class ext_module ext;
    static_js_qv_crypto_js -.->|imports| ext_module
    ext_computeK["computeK"]
    class ext_computeK ext;
    static_js_qv_crypto_js -.->|imports| ext_computeK
    static_js_qv_crypto_js -.->|imports| ext_i2osp
    ext_deriveVerifier["deriveVerifier"]
    class ext_deriveVerifier ext;
    static_js_qv_crypto_js -.->|imports| ext_deriveVerifier
    static_js_qv_crypto_js -.->|imports| ext_bytesToHex
    ext_srpLogin["srpLogin"]
    class ext_srpLogin ext;
    static_js_qv_crypto_js -.->|imports| ext_srpLogin
    static_js_qv_crypto_js -.->|imports| ext_bytesToBigInt
    static_js_qv_crypto_js -.->|imports| ext_modPow
    ext_postJson["postJson"]
    class ext_postJson ext;
    static_js_qv_crypto_js -.->|imports| ext_postJson
    static_js_qv_crypto_js -.->|imports| ext_computeK
    static_js_qv_crypto_js -.->|imports| ext_i2osp
    static_js_qv_crypto_js -.->|imports| ext_modPow
    static_js_qv_crypto_js -.->|imports| ext_map
    static_js_qv_crypto_js -.->|imports| ext_i2osp
    static_js_qv_crypto_js -.->|imports| ext_i2osp
    static_js_qv_crypto_js -.->|imports| ext_postJson
    ext_hybrid["hybrid"]
    class ext_hybrid ext;
    static_js_qv_crypto_js -.->|imports| ext_hybrid
    ext_generateIdentity["generateIdentity"]
    class ext_generateIdentity ext;
    static_js_qv_crypto_js -.->|imports| ext_generateIdentity
    ext_keygen["keygen"]
    class ext_keygen ext;
    static_js_qv_crypto_js -.->|imports| ext_keygen
    static_js_qv_crypto_js -.->|imports| ext_keygen
    static_js_qv_crypto_js -.->|imports| ext_keygen
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    ext_encode["encode"]
    class ext_encode ext;
    static_js_qv_crypto_js -.->|imports| ext_encode
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    ext_parsePublicKey["parsePublicKey"]
    class ext_parsePublicKey ext;
    static_js_qv_crypto_js -.->|imports| ext_parsePublicKey
    static_js_qv_crypto_js -.->|imports| ext_parse
    ext_decode["decode"]
    class ext_decode ext;
    static_js_qv_crypto_js -.->|imports| ext_decode
    static_js_qv_crypto_js -.->|imports| ext_base64ToBytes
    static_js_qv_crypto_js -.->|imports| ext_base64ToBytes
    ext_parsePrivateBlob["parsePrivateBlob"]
    class ext_parsePrivateBlob ext;
    static_js_qv_crypto_js -.->|imports| ext_parsePrivateBlob
    static_js_qv_crypto_js -.->|imports| ext_parse
    static_js_qv_crypto_js -.->|imports| ext_decode
    static_js_qv_crypto_js -.->|imports| ext_base64ToBytes
    static_js_qv_crypto_js -.->|imports| ext_base64ToBytes
    ext_deriveWrapKey["deriveWrapKey"]
    class ext_deriveWrapKey ext;
    static_js_qv_crypto_js -.->|imports| ext_deriveWrapKey
    ext_hkdf["hkdf"]
    class ext_hkdf ext;
    static_js_qv_crypto_js -.->|imports| ext_hkdf
    static_js_qv_crypto_js -.->|imports| ext_encode
    ext_wrapKey["wrapKey"]
    class ext_wrapKey ext;
    static_js_qv_crypto_js -.->|imports| ext_wrapKey
    static_js_qv_crypto_js -.->|imports| ext_parsePublicKey
    ext_encapsulate["encapsulate"]
    class ext_encapsulate ext;
    static_js_qv_crypto_js -.->|imports| ext_encapsulate
    static_js_qv_crypto_js -.->|imports| ext_keygen
    ext_getSharedSecret["getSharedSecret"]
    class ext_getSharedSecret ext;
    static_js_qv_crypto_js -.->|imports| ext_getSharedSecret
    static_js_qv_crypto_js -.->|imports| ext_deriveWrapKey
    static_js_qv_crypto_js -.->|imports| ext_aesGcmEncrypt
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    ext_unwrapKey["unwrapKey"]
    class ext_unwrapKey ext;
    static_js_qv_crypto_js -.->|imports| ext_unwrapKey
    static_js_qv_crypto_js -.->|imports| ext_parsePrivateBlob
    static_js_qv_crypto_js -.->|imports| ext_parse
    static_js_qv_crypto_js -.->|imports| ext_decode
    ext_decapsulate["decapsulate"]
    class ext_decapsulate ext;
    static_js_qv_crypto_js -.->|imports| ext_decapsulate
    static_js_qv_crypto_js -.->|imports| ext_getSharedSecret
    static_js_qv_crypto_js -.->|imports| ext_deriveWrapKey
    static_js_qv_crypto_js -.->|imports| ext_aesGcmDecrypt
    ext_recovery["recovery"]
    class ext_recovery ext;
    static_js_qv_crypto_js -.->|imports| ext_recovery
    static_js_qv_crypto_js -.->|imports| ext_bytes
    ext_generateRecoveryCode["generateRecoveryCode"]
    class ext_generateRecoveryCode ext;
    static_js_qv_crypto_js -.->|imports| ext_generateRecoveryCode
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase32
    static_js_qv_crypto_js -.->|imports| ext_push
    static_js_qv_crypto_js -.->|imports| ext_join
    ext_normalizeRecoveryCode["normalizeRecoveryCode"]
    class ext_normalizeRecoveryCode ext;
    static_js_qv_crypto_js -.->|imports| ext_normalizeRecoveryCode
    ext_trim["trim"]
    class ext_trim ext;
    static_js_qv_crypto_js -.->|imports| ext_trim
    static_js_qv_crypto_js -.->|imports| ext_toUpperCase
    ext_replace["replace"]
    class ext_replace ext;
    static_js_qv_crypto_js -.->|imports| ext_replace
    ext_wrapPrivateKeyForRecovery["wrapPrivateKeyForRecovery"]
    class ext_wrapPrivateKeyForRecovery ext;
    static_js_qv_crypto_js -.->|imports| ext_wrapPrivateKeyForRecovery
    static_js_qv_crypto_js -.->|imports| ext_bytesToHex
    static_js_qv_crypto_js -.->|imports| ext_deriveMasterKey
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    ext_key["key"]
    class ext_key ext;
    static_js_qv_crypto_js -.->|imports| ext_key
    ext_innerSK["innerSK"]
    class ext_innerSK ext;
    static_js_qv_crypto_js -.->|imports| ext_innerSK
    ext_publicKey["publicKey"]
    class ext_publicKey ext;
    static_js_qv_crypto_js -.->|imports| ext_publicKey
    ext_derivePublicKeyFromPrivateBlob["derivePublicKeyFromPrivateBlob"]
    class ext_derivePublicKeyFromPrivateBlob ext;
    static_js_qv_crypto_js -.->|imports| ext_derivePublicKeyFromPrivateBlob
    static_js_qv_crypto_js -.->|imports| ext_parsePrivateBlob
    static_js_qv_crypto_js -.->|imports| ext_slice
    ext_getPublicKey["getPublicKey"]
    class ext_getPublicKey ext;
    static_js_qv_crypto_js -.->|imports| ext_getPublicKey
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    static_js_qv_crypto_js -.->|imports| ext_postJson
    static_js_qv_crypto_js -.->|imports| ext_fetch
    static_js_qv_crypto_js -.->|imports| ext_json
    ext_endpoint["endpoint"]
    class ext_endpoint ext;
    static_js_qv_crypto_js -.->|imports| ext_endpoint
    ext_buildRegistration["buildRegistration"]
    class ext_buildRegistration ext;
    static_js_qv_crypto_js -.->|imports| ext_buildRegistration
    static_js_qv_crypto_js -.->|imports| ext_bytesToHex
    static_js_qv_crypto_js -.->|imports| ext_bytesToHex
    static_js_qv_crypto_js -.->|imports| ext_deriveVerifier
    static_js_qv_crypto_js -.->|imports| ext_generateIdentity
    static_js_qv_crypto_js -.->|imports| ext_deriveMasterKey
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    static_js_qv_crypto_js -.->|imports| ext_generateRecoveryCode
    static_js_qv_crypto_js -.->|imports| ext_wrapPrivateKeyForRecovery
    ext_register["register"]
    class ext_register ext;
    static_js_qv_crypto_js -.->|imports| ext_register
    static_js_qv_crypto_js -.->|imports| ext_buildRegistration
    static_js_qv_crypto_js -.->|imports| ext_postJson
    ext_recoverAccount["recoverAccount"]
    class ext_recoverAccount ext;
    static_js_qv_crypto_js -.->|imports| ext_recoverAccount
    static_js_qv_crypto_js -.->|imports| ext_fetch
    static_js_qv_crypto_js -.->|imports| ext_json
    static_js_qv_crypto_js -.->|imports| ext_json
    static_js_qv_crypto_js -.->|imports| ext_deriveMasterKey
    static_js_qv_crypto_js -.->|imports| ext_aesGcmDecrypt
    static_js_qv_crypto_js -.->|imports| ext_derivePublicKeyFromPrivateBlob
    static_js_qv_crypto_js -.->|imports| ext_bytesToHex
    static_js_qv_crypto_js -.->|imports| ext_deriveVerifier
    static_js_qv_crypto_js -.->|imports| ext_bytesToHex
    static_js_qv_crypto_js -.->|imports| ext_deriveMasterKey
    static_js_qv_crypto_js -.->|imports| ext_bytesToBase64
    static_js_qv_crypto_js -.->|imports| ext_postJson
    static_js_qv_crypto_js -.->|imports| ext_login
    static_js_qv_crypto_js -.->|imports| ext_srpLogin
    ext_encryptAndUpload["encryptAndUpload"]
    class ext_encryptAndUpload ext;
    static_js_qv_crypto_js -.->|imports| ext_encryptAndUpload
    static_js_qv_crypto_js -.->|imports| ext_randomBytes
    ext_padFramed["padFramed"]
    class ext_padFramed ext;
    static_js_qv_crypto_js -.->|imports| ext_padFramed
    static_js_qv_crypto_js -.->|imports| ext_aesGcmEncrypt
    static_js_qv_crypto_js -.->|imports| ext_wrapKey
    ext_append["append"]
    class ext_append ext;
    static_js_qv_crypto_js -.->|imports| ext_append
    static_js_qv_crypto_js -.->|imports| ext_append
    static_js_qv_crypto_js -.->|imports| ext_append
    static_js_qv_crypto_js -.->|imports| ext_fetch
    static_js_qv_crypto_js -.->|imports| ext_json
    static_js_qv_crypto_js -.->|imports| ext_json
    ext_downloadAndDecrypt["downloadAndDecrypt"]
    class ext_downloadAndDecrypt ext;
    static_js_qv_crypto_js -.->|imports| ext_downloadAndDecrypt
    static_js_qv_crypto_js -.->|imports| ext_fetch
    static_js_qv_crypto_js -.->|imports| ext_json
    static_js_qv_crypto_js -.->|imports| ext_json
    static_js_qv_crypto_js -.->|imports| ext_fetch
    static_js_qv_crypto_js -.->|imports| ext_json
    static_js_qv_crypto_js -.->|imports| ext_deriveMasterKey
    static_js_qv_crypto_js -.->|imports| ext_aesGcmDecrypt
    static_js_qv_crypto_js -.->|imports| ext_unwrapKey
    static_js_qv_crypto_js -.->|imports| ext_aesGcmDecrypt
    ext_unframeFramed["unframeFramed"]
    class ext_unframeFramed ext;
    static_js_qv_crypto_js -.->|imports| ext_unframeFramed
    ext_fetchPublicKey["fetchPublicKey"]
    class ext_fetchPublicKey ext;
    static_js_qv_crypto_js -.->|imports| ext_fetchPublicKey
    static_js_qv_crypto_js -.->|imports| ext_fetch
    static_js_qv_crypto_js -.->|imports| ext_json
    static_js_qv_crypto_js -.->|imports| ext_return
    ext_recipient["recipient"]
    class ext_recipient ext;
    static_js_qv_crypto_js -.->|imports| ext_recipient
    static_js_qv_crypto_js -.->|imports| ext_sendSecureMessage
    static_js_qv_crypto_js -.->|imports| ext_randomBytes
    static_js_qv_crypto_js -.->|imports| ext_padFramed
    static_js_qv_crypto_js -.->|imports| ext_aesGcmEncrypt
    static_js_qv_crypto_js -.->|imports| ext_fetchPublicKey
    static_js_qv_crypto_js -.->|imports| ext_wrapKey
    static_js_qv_crypto_js -.->|imports| ext_fetchPublicKey
    static_js_qv_crypto_js -.->|imports| ext_wrapKey
    static_js_qv_crypto_js -.->|imports| ext_postJson
    static_js_qv_crypto_js -.->|imports| ext_decryptInbox
    static_js_qv_crypto_js -.->|imports| ext_fetch
    static_js_qv_crypto_js -.->|imports| ext_json
    static_js_qv_crypto_js -.->|imports| ext_deriveMasterKey
    static_js_qv_crypto_js -.->|imports| ext_aesGcmDecrypt
    static_js_qv_crypto_js -.->|imports| ext_unwrapKey
    static_js_qv_crypto_js -.->|imports| ext_aesGcmDecrypt
    static_js_qv_crypto_js -.->|imports| ext_unframeFramed
    static_js_qv_crypto_js -.->|imports| ext_push
    static_js_qv_crypto_js -.->|imports| ext_push
    static_js_qv_deniable_js -.->|imports| ext___qv_crypto_js
    static_js_qv_deniable_js -.->|imports| ext_vault
    ext_server["server"]
    class ext_server ext;
    static_js_qv_deniable_js -.->|imports| ext_server
    ext_list["list"]
    class ext_list ext;
    static_js_qv_deniable_js -.->|imports| ext_list
    ext_toBytes["toBytes"]
    class ext_toBytes ext;
    static_js_qv_deniable_js -.->|imports| ext_toBytes
    static_js_qv_deniable_js -.->|imports| ext_encode
    ext_len["len"]
    class ext_len ext;
    static_js_qv_deniable_js -.->|imports| ext_len
    ext_frame["frame"]
    class ext_frame ext;
    static_js_qv_deniable_js -.->|imports| ext_frame
    static_js_qv_deniable_js -.->|imports| ext_randomBytes
    ext_setUint32["setUint32"]
    class ext_setUint32 ext;
    static_js_qv_deniable_js -.->|imports| ext_setUint32
    static_js_qv_deniable_js -.->|imports| ext_set
    static_js_qv_deniable_js -.->|imports| ext_frame
    ext_unframe["unframe"]
    class ext_unframe ext;
    static_js_qv_deniable_js -.->|imports| ext_unframe
    ext_getUint32["getUint32"]
    class ext_getUint32 ext;
    static_js_qv_deniable_js -.->|imports| ext_getUint32
    static_js_qv_deniable_js -.->|imports| ext_slice
    ext_sealSlot["sealSlot"]
    class ext_sealSlot ext;
    static_js_qv_deniable_js -.->|imports| ext_sealSlot
    static_js_qv_deniable_js -.->|imports| ext_randomBytes
    static_js_qv_deniable_js -.->|imports| ext_bytesToHex
    static_js_qv_deniable_js -.->|imports| ext_deriveKeyFromPassphrase
    static_js_qv_deniable_js -.->|imports| ext_aesGcmEncrypt
    static_js_qv_deniable_js -.->|imports| ext_slice
    static_js_qv_deniable_js -.->|imports| ext_slice
    static_js_qv_deniable_js -.->|imports| ext_bytesToHex
    static_js_qv_deniable_js -.->|imports| ext_bytesToBase64
    ext_openSlot["openSlot"]
    class ext_openSlot ext;
    static_js_qv_deniable_js -.->|imports| ext_openSlot
    static_js_qv_deniable_js -.->|imports| ext_deriveKeyFromPassphrase
    static_js_qv_deniable_js -.->|imports| ext_base64ToBytes
    static_js_qv_deniable_js -.->|imports| ext_aesGcmDecrypt
    static_js_qv_deniable_js -.->|imports| ext_unframe
    static_js_qv_deniable_js -.->|imports| ext_buildDeniableVault
    static_js_qv_deniable_js -.->|imports| ext_map
    static_js_qv_deniable_js -.->|imports| ext_toBytes
    static_js_qv_deniable_js -.->|imports| ext_push
    static_js_qv_deniable_js -.->|imports| ext_randomBytes
    static_js_qv_deniable_js -.->|imports| ext_frame
    static_js_qv_deniable_js -.->|imports| ext_push
    static_js_qv_deniable_js -.->|imports| ext_openDeniableVault
    static_js_qv_deniable_js -.->|imports| ext_openSlot
    static_js_qv_deniable_js -.->|imports| ext_decode
    ext_padding["padding"]
    class ext_padding ext;
    static_js_qv_padding_js -.->|imports| ext_padding
    static_js_qv_padding_js -.->|imports| ext_len
    ext_tableFor["tableFor"]
    class ext_tableFor ext;
    static_js_qv_padding_js -.->|imports| ext_tableFor
    ext_bucketFor["bucketFor"]
    class ext_bucketFor ext;
    static_js_qv_padding_js -.->|imports| ext_bucketFor
    static_js_qv_padding_js -.->|imports| ext_tableFor
    ext_randomPad["randomPad"]
    class ext_randomPad ext;
    static_js_qv_padding_js -.->|imports| ext_randomPad
    static_js_qv_padding_js -.->|imports| ext_getRandomValues
    static_js_qv_padding_js -.->|imports| ext_padFramed
    static_js_qv_padding_js -.->|imports| ext_bucketFor
    static_js_qv_padding_js -.->|imports| ext_randomPad
    static_js_qv_padding_js -.->|imports| ext_set
    static_js_qv_padding_js -.->|imports| ext_setUint32
    static_js_qv_padding_js -.->|imports| ext_set
    static_js_qv_padding_js -.->|imports| ext_unframeFramed
    static_js_qv_padding_js -.->|imports| ext_tableFor
    static_js_qv_padding_js -.->|imports| ext_getUint32
    static_js_qv_padding_js -.->|imports| ext_slice
    static_js_recover_js -.->|imports| ext___qv_crypto_js
    static_js_recover_js -.->|imports| ext_controller
    static_js_recover_js -.->|imports| ext_recoverAccount
    static_js_recover_js -.->|imports| ext_setStatus
    ext_toggle["toggle"]
    class ext_toggle ext;
    static_js_recover_js -.->|imports| ext_toggle
    static_js_recover_js -.->|imports| ext_toggle
    ext_handleRecover["handleRecover"]
    class ext_handleRecover ext;
    static_js_recover_js -.->|imports| ext_handleRecover
    static_js_recover_js -.->|imports| ext_preventDefault
    static_js_recover_js -.->|imports| ext_querySelector
    static_js_recover_js -.->|imports| ext_getElementById
    static_js_recover_js -.->|imports| ext_getElementById
    static_js_recover_js -.->|imports| ext_trim
    static_js_recover_js -.->|imports| ext_getElementById
    static_js_recover_js -.->|imports| ext_trim
    static_js_recover_js -.->|imports| ext_getElementById
    static_js_recover_js -.->|imports| ext_getElementById
    static_js_recover_js -.->|imports| ext_querySelector
    static_js_recover_js -.->|imports| ext_setStatus
    static_js_recover_js -.->|imports| ext_setStatus
    static_js_recover_js -.->|imports| ext_setStatus
    static_js_recover_js -.->|imports| ext_setStatus
    static_js_recover_js -.->|imports| ext_recoverAccount
    static_js_recover_js -.->|imports| ext_setStatus
    static_js_recover_js -.->|imports| ext_error
    static_js_recover_js -.->|imports| ext_setStatus
    static_js_recover_js -.->|imports| ext_init
    static_js_recover_js -.->|imports| ext_getElementById
    static_js_recover_js -.->|imports| ext_addEventListener
    static_js_recover_js -.->|imports| ext_addEventListener
    static_js_recover_js -.->|imports| ext_init
    static_js_register_js -.->|imports| ext___qv_crypto_js
    static_js_register_js -.->|imports| ext_controller
    ext_showRecoveryCode["showRecoveryCode"]
    class ext_showRecoveryCode ext;
    static_js_register_js -.->|imports| ext_showRecoveryCode
    static_js_register_js -.->|imports| ext_getElementById
    static_js_register_js -.->|imports| ext_getElementById
    static_js_register_js -.->|imports| ext_getElementById
    static_js_register_js -.->|imports| ext_alert
    ext_resolve["resolve"]
    class ext_resolve ext;
    static_js_register_js -.->|imports| ext_resolve
    ext_remove["remove"]
    class ext_remove ext;
    static_js_register_js -.->|imports| ext_remove
    static_js_register_js -.->|imports| ext_addEventListener
    static_js_register_js -.->|imports| ext_add
    static_js_register_js -.->|imports| ext_resolve
    ext_handleRegister["handleRegister"]
    class ext_handleRegister ext;
    static_js_register_js -.->|imports| ext_handleRegister
    static_js_register_js -.->|imports| ext_preventDefault
    ext_fromEntries["fromEntries"]
    class ext_fromEntries ext;
    static_js_register_js -.->|imports| ext_fromEntries
    static_js_register_js -.->|imports| ext_alert
    static_js_register_js -.->|imports| ext_alert
    static_js_register_js -.->|imports| ext_querySelector
    ext_payload["payload"]
    class ext_payload ext;
    static_js_register_js -.->|imports| ext_payload
    static_js_register_js -.->|imports| ext_buildRegistration
    static_js_register_js -.->|imports| ext_fetch
    static_js_register_js -.->|imports| ext_json
    static_js_register_js -.->|imports| ext_showRecoveryCode
    static_js_register_js -.->|imports| ext_error
    static_js_register_js -.->|imports| ext_alert
    static_js_register_js -.->|imports| ext_init
    static_js_register_js -.->|imports| ext_getElementById
    static_js_register_js -.->|imports| ext_addEventListener
    static_js_register_js -.->|imports| ext_addEventListener
    static_js_register_js -.->|imports| ext_init
    static_js_upload_js -.->|imports| ext___qv_crypto_js
    static_js_upload_js -.->|imports| ext_controller
    static_js_upload_js -.->|imports| ext_getCsrfToken
    static_js_upload_js -.->|imports| ext_querySelector
    ext_getUsername["getUsername"]
    class ext_getUsername ext;
    static_js_upload_js -.->|imports| ext_getUsername
    static_js_upload_js -.->|imports| ext_getPublicKey
    static_js_upload_js -.->|imports| ext_fetch
    static_js_upload_js -.->|imports| ext_getCsrfToken
    static_js_upload_js -.->|imports| ext_json
    static_js_upload_js -.->|imports| ext_json
    ext_handleUpload["handleUpload"]
    class ext_handleUpload ext;
    static_js_upload_js -.->|imports| ext_handleUpload
    static_js_upload_js -.->|imports| ext_preventDefault
    static_js_upload_js -.->|imports| ext_alert
    static_js_upload_js -.->|imports| ext_getPublicKey
    static_js_upload_js -.->|imports| ext_encryptAndUpload
    static_js_upload_js -.->|imports| ext_alert
    ext_reload["reload"]
    class ext_reload ext;
    static_js_upload_js -.->|imports| ext_reload
    static_js_upload_js -.->|imports| ext_alert
    ext_handleDownload["handleDownload"]
    class ext_handleDownload ext;
    static_js_upload_js -.->|imports| ext_handleDownload
    static_js_upload_js -.->|imports| ext_preventDefault
    static_js_upload_js -.->|imports| ext_prompt
    static_js_upload_js -.->|imports| ext_downloadAndDecrypt
    ext_createObjectURL["createObjectURL"]
    class ext_createObjectURL ext;
    static_js_upload_js -.->|imports| ext_createObjectURL
    ext_createElement["createElement"]
    class ext_createElement ext;
    static_js_upload_js -.->|imports| ext_createElement
    ext_appendChild["appendChild"]
    class ext_appendChild ext;
    static_js_upload_js -.->|imports| ext_appendChild
    ext_click["click"]
    class ext_click ext;
    static_js_upload_js -.->|imports| ext_click
    ext_revokeObjectURL["revokeObjectURL"]
    class ext_revokeObjectURL ext;
    static_js_upload_js -.->|imports| ext_revokeObjectURL
    static_js_upload_js -.->|imports| ext_remove
    static_js_upload_js -.->|imports| ext_alert
    static_js_upload_js -.->|imports| ext_init
    static_js_upload_js -.->|imports| ext_getElementById
    static_js_upload_js -.->|imports| ext_getElementById
    static_js_upload_js -.->|imports| ext_getElementById
    static_js_upload_js -.->|imports| ext_addEventListener
    static_js_upload_js -.->|imports| ext_handleUpload
    static_js_upload_js -.->|imports| ext_getUsername
    static_js_upload_js -.->|imports| ext_querySelectorAll
    static_js_upload_js -.->|imports| ext_forEach
    static_js_upload_js -.->|imports| ext_addEventListener
    static_js_upload_js -.->|imports| ext_handleDownload
    static_js_upload_js -.->|imports| ext_addEventListener
    static_js_upload_js -.->|imports| ext_init
    templates_terms_py -.->|imports| ext_flask
    tests_conftest_py -.->|imports| ext___future__
    tests_conftest_py -.->|imports| ext_logging
    tests_conftest_py -.->|imports| ext_os
    tests_conftest_py -.->|imports| ext_sys
    ext_pytest["pytest"]
    class ext_pytest ext;
    tests_conftest_py -.->|imports| ext_pytest
    tests_conftest_py -.->|imports| ext_app_factory
    tests_conftest_py -.->|imports| ext_utils_security
    ext_dotenv["dotenv"]
    class ext_dotenv ext;
    tests_conftest_py -.->|imports| ext_dotenv
    tests_test_account_facade_py -.->|imports| ext___future__
    tests_test_account_facade_py -.->|imports| ext_datetime
    tests_test_account_facade_py -.->|imports| ext_pytest
    tests_test_account_facade_py -.->|imports| ext_app_factory
    ext_controllers_facade["controllers.facade"]
    class ext_controllers_facade ext;
    tests_test_account_facade_py -.->|imports| ext_controllers_facade
    tests_test_account_facade_py -.->|imports| ext_models_user
    tests_test_auth_phone_py -.->|imports| ext___future__
    tests_test_cover_py -.->|imports| ext___future__
    tests_test_cover_py -.->|imports| ext_pytest
    tests_test_cover_py -.->|imports| ext_app_factory
    ext_controllers_cover["controllers.cover"]
    class ext_controllers_cover ext;
    tests_test_cover_py -.->|imports| ext_controllers_cover
    tests_test_cover_py -.->|imports| ext_controllers_facade
    tests_test_deniable_vault_py -.->|imports| ext___future__
    tests_test_deniable_vault_py -.->|imports| ext_base64
    ext_copy["copy"]
    class ext_copy ext;
    tests_test_deniable_vault_py -.->|imports| ext_copy
    tests_test_deniable_vault_py -.->|imports| ext_json
    tests_test_deniable_vault_py -.->|imports| ext_datetime
    tests_test_deniable_vault_py -.->|imports| ext_pytest
    ext_controllers_deniable_vault["controllers.deniable_vault"]
    class ext_controllers_deniable_vault ext;
    tests_test_deniable_vault_py -.->|imports| ext_controllers_deniable_vault
    tests_test_deniable_vault_py -.->|imports| ext_models_deniable_vault
    tests_test_deniable_vault_py -.->|imports| ext_models_user
    tests_test_doctor_py -.->|imports| ext___future__
    ext_importlib_util["importlib.util"]
    class ext_importlib_util ext;
    tests_test_doctor_py -.->|imports| ext_importlib_util
    tests_test_doctor_py -.->|imports| ext_sys
    tests_test_doctor_py -.->|imports| ext_pathlib
    tests_test_doctor_py -.->|imports| ext_os
    tests_test_facade_py -.->|imports| ext___future__
    tests_test_facade_py -.->|imports| ext_json
    tests_test_facade_py -.->|imports| ext_datetime
    tests_test_facade_py -.->|imports| ext_pytest
    tests_test_facade_py -.->|imports| ext_app_factory
    tests_test_facade_py -.->|imports| ext_controllers_facade
    tests_test_facade_py -.->|imports| ext_models_user
    tests_test_integrity_py -.->|imports| ext___future__
    tests_test_integrity_py -.->|imports| ext_base64
    tests_test_integrity_py -.->|imports| ext_hashlib
    tests_test_integrity_py -.->|imports| ext_json
    tests_test_integrity_py -.->|imports| ext_pathlib
    tests_test_integrity_py -.->|imports| ext_utils_integrity
    ext_tools_verify_build["tools.verify_build"]
    class ext_tools_verify_build ext;
    tests_test_integrity_py -.->|imports| ext_tools_verify_build
    tests_test_padding_py -.->|imports| ext___future__
    tests_test_padding_py -.->|imports| ext_base64
    tests_test_padding_py -.->|imports| ext_pytest
    tests_test_padding_py -.->|imports| ext_controllers_file
    ext_controllers_message["controllers.message"]
    class ext_controllers_message ext;
    tests_test_padding_py -.->|imports| ext_controllers_message
    tests_test_padding_py -.->|imports| ext_utils
    tests_test_padding_py -.->|imports| ext_utils_padding
    tests_test_secure_channel_py -.->|imports| ext___future__
    tests_test_secure_channel_py -.->|imports| ext_json
    tests_test_secure_channel_py -.->|imports| ext_os
    ext_controllers_secure_channel["controllers.secure_channel"]
    class ext_controllers_secure_channel ext;
    tests_test_secure_channel_py -.->|imports| ext_controllers_secure_channel
    tests_test_secure_channel_py -.->|imports| ext_subprocess
    tests_test_secure_channel_py -.->|imports| ext_json
    tests_test_secure_channel_py -.->|imports| ext_shutil
    ext_errno["errno"]
    class ext_errno ext;
    tests_test_secure_channel_py -.->|imports| ext_errno
    tests_test_secure_channel_py -.->|imports| ext_re
    tests_test_secure_channel_py -.->|imports| ext_time
    tests_test_secure_channel_py -.->|imports| ext_re
    tests_test_secure_channel_py -.->|imports| ext_time
    tests_test_secure_channel_py -.->|imports| ext_views_admin
    tests_test_secure_channel_py -.->|imports| ext_views_admin
    tests_test_secure_channel_py -.->|imports| ext_views_admin
    tests_test_secure_channel_py -.->|imports| ext_views_admin
    tests_test_secure_channel_py -.->|imports| ext_socket
    tests_test_secure_channel_py -.->|imports| ext_views_admin
    tests_test_secure_channel_py -.->|imports| ext_pathlib
    tests_test_security_py -.->|imports| ext___future__
    tests_test_security_py -.->|imports| ext_json
    tests_test_security_py -.->|imports| ext_flask_wtf_csrf
    tests_test_security_py -.->|imports| ext_utils_security
    tests_test_security_py -.->|imports| ext_flask
    tests_test_srp_py -.->|imports| ext___future__
    tests_test_srp_py -.->|imports| ext_hashlib
    tests_test_srp_py -.->|imports| ext_secrets
    tests_test_srp_py -.->|imports| ext_utils
    tests_test_utils_py -.->|imports| ext___future__
    tests_test_utils_py -.->|imports| ext_utils_utils
    tools_generate_sri_py -.->|imports| ext___future__
    tools_generate_sri_py -.->|imports| ext_argparse
    tools_generate_sri_py -.->|imports| ext_json
    tools_generate_sri_py -.->|imports| ext_sys
    tools_generate_sri_py -.->|imports| ext_urllib_request
    tools_generate_sri_py -.->|imports| ext_pathlib
    tools_generate_sri_py -.->|imports| ext_utils_integrity
    tools_mutation_test_py -.->|imports| ext___future__
    tools_mutation_test_py -.->|imports| ext_argparse
    tools_mutation_test_py -.->|imports| ext_io
    tools_mutation_test_py -.->|imports| ext_os
    tools_mutation_test_py -.->|imports| ext_subprocess
    tools_mutation_test_py -.->|imports| ext_sys
    ext_tokenize["tokenize"]
    class ext_tokenize ext;
    tools_mutation_test_py -.->|imports| ext_tokenize
    tools_mutation_test_py -.->|imports| ext_dataclasses
    tools_mutation_test_py -.->|imports| ext_pathlib
    tools_verify_build_py -.->|imports| ext___future__
    tools_verify_build_py -.->|imports| ext_json
    tools_verify_build_py -.->|imports| ext_re
    tools_verify_build_py -.->|imports| ext_sys
    ext_html_parser["html.parser"]
    class ext_html_parser ext;
    tools_verify_build_py -.->|imports| ext_html_parser
    tools_verify_build_py -.->|imports| ext_pathlib
    tools_verify_build_py -.->|imports| ext_utils_integrity
    tools_verify_build_py -.->|imports| ext_utils_padding
    utils_cache_py -.->|imports| ext_typing
    ext_redis["redis"]
    class ext_redis ext;
    utils_cache_py -.->|imports| ext_redis
    utils_cache_py -.->|imports| ext_json
    utils_integrity_py -.->|imports| ext___future__
    utils_integrity_py -.->|imports| ext_base64
    ext_functools["functools"]
    class ext_functools ext;
    utils_integrity_py -.->|imports| ext_functools
    utils_integrity_py -.->|imports| ext_hashlib
    utils_integrity_py -.->|imports| ext_json
    utils_integrity_py -.->|imports| ext_pathlib
    utils_integrity_py -.->|imports| ext_typing
    utils_mailer_py -.->|imports| ext_typing
    utils_mailer_py -.->|imports| ext_flask
    utils_mailer_py -.->|imports| ext_flask_mail
    utils_padding_py -.->|imports| ext___future__
    utils_padding_py -.->|imports| ext_functools
    utils_padding_py -.->|imports| ext_os
    utils_padding_py -.->|imports| ext_secrets
    ext_struct["struct"]
    class ext_struct ext;
    utils_padding_py -.->|imports| ext_struct
    utils_padding_py -.->|imports| ext_dataclasses
    utils_padding_py -.->|imports| ext_typing
    utils_plans_py -.->|imports| ext_typing
    utils_scheduler_py -.->|imports| ext___future__
    utils_scheduler_py -.->|imports| ext_logging
    utils_scheduler_py -.->|imports| ext_datetime
    utils_scheduler_py -.->|imports| ext_typing
    utils_scheduler_py -.->|imports| ext_pytz
    ext_apscheduler_schedulers_background["apscheduler.schedulers.background"]
    class ext_apscheduler_schedulers_background ext;
    utils_scheduler_py -.->|imports| ext_apscheduler_schedulers_background
    utils_scheduler_py -.->|imports| ext_flask
    utils_scheduler_py -.->|imports| ext_flask_mail
    utils_scheduler_py -.->|imports| ext_models_message
    utils_scheduler_py -.->|imports| ext_models_user
    utils_scheduler_py -.->|imports| ext_utils_mailer
    utils_security_py -.->|imports| ext___future__
    utils_security_py -.->|imports| ext_functools
    utils_security_py -.->|imports| ext_hashlib
    ext_hmac["hmac"]
    class ext_hmac ext;
    utils_security_py -.->|imports| ext_hmac
    utils_security_py -.->|imports| ext_json
    utils_security_py -.->|imports| ext_logging
    utils_security_py -.->|imports| ext_os
    utils_security_py -.->|imports| ext_secrets
    utils_security_py -.->|imports| ext_time
    utils_security_py -.->|imports| ext_uuid
    utils_security_py -.->|imports| ext_typing
    utils_security_py -.->|imports| ext_flask
    utils_security_py -.->|imports| ext_flask_wtf_csrf
    ext_wtforms["wtforms"]
    class ext_wtforms ext;
    utils_security_py -.->|imports| ext_wtforms
    utils_security_py -.->|imports| ext_utils_utils
    utils_srp6a_py -.->|imports| ext_hashlib
    utils_srp6a_py -.->|imports| ext_hmac
    utils_srp6a_py -.->|imports| ext_json
    utils_srp6a_py -.->|imports| ext_secrets
    utils_srp6a_py -.->|imports| ext_typing
    utils_srp6a_py -.->|imports| ext_redis
    utils_utils_py -.->|imports| ext_json
    utils_utils_py -.->|imports| ext_typing
    utils_utils_py -.->|imports| ext_re
    utils_utils_py -.->|imports| ext_os
    utils_utils_py -.->|imports| ext_flask
    utils_utils_py -.->|imports| ext_werkzeug_utils
    utils_utils_py -.->|imports| ext_dotenv
    views_about_py -.->|imports| ext_flask
    views_account_py -.->|imports| ext___future__
    views_account_py -.->|imports| ext_flask
    views_account_py -.->|imports| ext_flask_limiter
    views_account_py -.->|imports| ext_flask_limiter_util
    views_account_py -.->|imports| ext_flask_login
    views_account_py -.->|imports| ext_controllers_deniable_vault
    views_account_py -.->|imports| ext_controllers_facade
    views_account_py -.->|imports| ext_models_deniable_vault
    views_account_py -.->|imports| ext_utils_security
    views_admin_py -.->|imports| ext_flask
    views_admin_py -.->|imports| ext_flask_login
    views_admin_py -.->|imports| ext_models_user
    views_admin_py -.->|imports| ext_models_plans
    ext_flask_wtf["flask_wtf"]
    class ext_flask_wtf ext;
    views_admin_py -.->|imports| ext_flask_wtf
    views_admin_py -.->|imports| ext_wtforms
    ext_wtforms_validators["wtforms.validators"]
    class ext_wtforms_validators ext;
    views_admin_py -.->|imports| ext_wtforms_validators
    views_admin_py -.->|imports| ext_flask_limiter
    views_admin_py -.->|imports| ext_flask_limiter_util
    views_admin_py -.->|imports| ext_utils_utils
    ext_auth["auth"]
    class ext_auth ext;
    views_admin_py -.->|imports| ext_auth
    ext_controllers_contact["controllers.contact"]
    class ext_controllers_contact ext;
    views_admin_py -.->|imports| ext_controllers_contact
    views_admin_py -.->|imports| ext_controllers_secure_channel
    ext_models_superadmin_audit["models.superadmin_audit"]
    class ext_models_superadmin_audit ext;
    views_admin_py -.->|imports| ext_models_superadmin_audit
    views_admin_py -.->|imports| ext_os
    views_admin_py -.->|imports| ext_secrets
    views_admin_py -.->|imports| ext_datetime
    views_admin_py -.->|imports| ext_pytz
    views_admin_py -.->|imports| ext_utils_utils
    views_admin_py -.->|imports| ext_sqlite3
    ext_urllib_parse["urllib.parse"]
    class ext_urllib_parse ext;
    views_admin_py -.->|imports| ext_urllib_parse
    views_admin_py -.->|imports| ext_socket
    views_admin_py -.->|imports| ext_pathlib
    views_admin_py -.->|imports| ext_shutil
    views_admin_py -.->|imports| ext_pathlib
    views_auth_py -.->|imports| ext_hmac
    views_auth_py -.->|imports| ext_os
    views_auth_py -.->|imports| ext_functools
    views_auth_py -.->|imports| ext_flask
    views_auth_py -.->|imports| ext_flask_limiter
    views_auth_py -.->|imports| ext_flask_limiter_util
    views_auth_py -.->|imports| ext_flask_login
    views_auth_py -.->|imports| ext_flask_wtf
    views_auth_py -.->|imports| ext_flask_wtf_csrf
    views_auth_py -.->|imports| ext_wtforms
    views_auth_py -.->|imports| ext_wtforms_validators
    ext_controllers_auth["controllers.auth"]
    class ext_controllers_auth ext;
    views_auth_py -.->|imports| ext_controllers_auth
    views_auth_py -.->|imports| ext_controllers_contact
    views_auth_py -.->|imports| ext_models_user
    views_auth_py -.->|imports| ext_utils_mailer
    views_auth_py -.->|imports| ext_utils_security
    views_auth_py -.->|imports| ext_utils_utils
    views_facade_py -.->|imports| ext___future__
    views_facade_py -.->|imports| ext_pathlib
    views_facade_py -.->|imports| ext_typing
    views_facade_py -.->|imports| ext_flask
    views_facade_py -.->|imports| ext_flask_login
    views_facade_py -.->|imports| ext_flask_wtf_csrf
    views_facade_py -.->|imports| ext_controllers_cover
    views_facade_py -.->|imports| ext_controllers_facade
    views_faq_py -.->|imports| ext_flask
    views_faq_py -.->|imports| ext_models_plans
    views_faq_py -.->|imports| ext_utils_utils
    views_file_py -.->|imports| ext_flask
    views_file_py -.->|imports| ext_flask_login
    views_file_py -.->|imports| ext_flask_wtf
    views_file_py -.->|imports| ext_wtforms
    views_file_py -.->|imports| ext_wtforms_validators
    views_file_py -.->|imports| ext_flask_limiter
    views_file_py -.->|imports| ext_flask_limiter_util
    views_file_py -.->|imports| ext_auth
    views_file_py -.->|imports| ext_os
    views_file_py -.->|imports| ext_base64
    views_message_py -.->|imports| ext_flask
    views_message_py -.->|imports| ext_flask_login
    views_message_py -.->|imports| ext_controllers_message
    views_message_py -.->|imports| ext_flask_wtf
    views_message_py -.->|imports| ext_wtforms
    views_message_py -.->|imports| ext_wtforms_validators
    views_message_py -.->|imports| ext_flask_limiter
    views_message_py -.->|imports| ext_flask_limiter_util
    views_message_py -.->|imports| ext_auth
    views_message_py -.->|imports| ext_os
    views_privacy_py -.->|imports| ext_flask
    views_subscription_py -.->|imports| ext_os
    views_subscription_py -.->|imports| ext_flask
    views_subscription_py -.->|imports| ext_flask_login
    views_subscription_py -.->|imports| ext_models_user
    views_subscription_py -.->|imports| ext_models_plans
    ext_paypalrestsdk["paypalrestsdk"]
    class ext_paypalrestsdk ext;
    views_subscription_py -.->|imports| ext_paypalrestsdk
    views_subscription_py -.->|imports| ext_flask_wtf
    views_subscription_py -.->|imports| ext_wtforms
    views_subscription_py -.->|imports| ext_wtforms_validators
    views_subscription_py -.->|imports| ext_flask_limiter
    views_subscription_py -.->|imports| ext_flask_limiter_util
    views_subscription_py -.->|imports| ext_utils_utils
    views_subscription_py -.->|imports| ext_auth
    views_sync_py -.->|imports| ext_os
    views_sync_py -.->|imports| ext_flask
    views_sync_py -.->|imports| ext_flask_limiter
    views_sync_py -.->|imports| ext_flask_limiter_util
    views_sync_py -.->|imports| ext_flask_login
    views_sync_py -.->|imports| ext_werkzeug_utils
    views_sync_py -.->|imports| ext_utils_security
    views_terms_py -.->|imports| ext_flask
    views_views_py -.->|imports| ext_flask
    views_views_py -.->|imports| ext_flask_login
    views_views_py -.->|imports| ext_flask_wtf
    views_views_py -.->|imports| ext_wtforms
    views_views_py -.->|imports| ext_models_user
    views_views_py -.->|imports| ext_utils_utils
    wsgi_py -.->|imports| ext_os
    wsgi_py -.->|imports| ext_app_factory
```

---

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class auth_py_AuthController {
    <<class>>
    +_now_utc()
    +__init__(self, db_path, mail, storage_uri)
    +register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, recovery_salt, encrypted_private_key_recovery)
    +send_confirmation_email(self, email, username, token)
    +srp_hello(self, username, client_a_hex)
    +srp_verify(self, username, client_m1_hex)
    +send_sms_verification(self, phone, code, username)
    +verify_phone_code(self, username, code)
    +resend_phone_code(self, username)
    +_is_code_valid(self, expires_at)
  }
  class contact_py_ContactController {
    <<class>>
    +__init__(self, db_path)
    +create_contact(self, user_id, subject, message)
    +get_user_contacts(self, user_id)
  }
  class deniable_vault_py_EnvelopeValidationError {
    <<class>>
    +_base64_length(byte_length)
    +canonical_json(envelope)
    +_coerce_int(value, default)
    +_coerce_kdf(value, default)
    +from_mapping(cls, mapping, env)
    +expected_ct_b64_length(self)
    +random_container(self)
    +public_parameters(self)
    +__init__(self, config)
    +validate(self, envelope)
  }
  class deniable_vault_py_DeniableVaultConfig {
    <<class>>
    +_base64_length(byte_length)
    +canonical_json(envelope)
    +_coerce_int(value, default)
    +_coerce_kdf(value, default)
    +from_mapping(cls, mapping, env)
    +expected_ct_b64_length(self)
    +random_container(self)
    +public_parameters(self)
    +__init__(self, config)
    +validate(self, envelope)
  }
  class deniable_vault_py_EnvelopeValidator {
    <<class>>
    +_base64_length(byte_length)
    +canonical_json(envelope)
    +_coerce_int(value, default)
    +_coerce_kdf(value, default)
    +from_mapping(cls, mapping, env)
    +expected_ct_b64_length(self)
    +random_container(self)
    +public_parameters(self)
    +__init__(self, config)
    +validate(self, envelope)
  }
  class deniable_vault_py_DeniableVaultController {
    <<class>>
    +_base64_length(byte_length)
    +canonical_json(envelope)
    +_coerce_int(value, default)
    +_coerce_kdf(value, default)
    +from_mapping(cls, mapping, env)
    +expected_ct_b64_length(self)
    +random_container(self)
    +public_parameters(self)
    +__init__(self, config)
    +validate(self, envelope)
  }
  class facade_py_GateOutcome {
    <<class>>
    +_as_bool(value, default)
    +_as_int(value, default)
    +_as_text(value, default)
    +_as_raw_text(value, default)
    +_as_paths(value, default)
    +gate_configured(self)
    +cover_context(self)
    +cover_variables(self)
    +from_mapping(cls, mapping, env)
    +__init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)
  }
  class facade_py_GateDecision {
    <<class>>
    +_as_bool(value, default)
    +_as_int(value, default)
    +_as_text(value, default)
    +_as_raw_text(value, default)
    +_as_paths(value, default)
    +gate_configured(self)
    +cover_context(self)
    +cover_variables(self)
    +from_mapping(cls, mapping, env)
    +__init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)
  }
  class facade_py_FacadeConfig {
    <<class>>
    +_as_bool(value, default)
    +_as_int(value, default)
    +_as_text(value, default)
    +_as_raw_text(value, default)
    +_as_paths(value, default)
    +gate_configured(self)
    +cover_context(self)
    +cover_variables(self)
    +from_mapping(cls, mapping, env)
    +__init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)
  }
  class facade_py_GatePhraseHasher {
    <<class>>
    +_as_bool(value, default)
    +_as_int(value, default)
    +_as_text(value, default)
    +_as_raw_text(value, default)
    +_as_paths(value, default)
    +gate_configured(self)
    +cover_context(self)
    +cover_variables(self)
    +from_mapping(cls, mapping, env)
    +__init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)
  }
  class facade_py_GateTicket {
    <<class>>
    +_as_bool(value, default)
    +_as_int(value, default)
    +_as_text(value, default)
    +_as_raw_text(value, default)
    +_as_paths(value, default)
    +gate_configured(self)
    +cover_context(self)
    +cover_variables(self)
    +from_mapping(cls, mapping, env)
    +__init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)
  }
  class facade_py_FacadeGate {
    <<class>>
    +_as_bool(value, default)
    +_as_int(value, default)
    +_as_text(value, default)
    +_as_raw_text(value, default)
    +_as_paths(value, default)
    +gate_configured(self)
    +cover_context(self)
    +cover_variables(self)
    +from_mapping(cls, mapping, env)
    +__init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)
  }
  class file_py_FileController {
    <<class>>
    +_log_s3_error(operation, error)
    +safe_filename(name)
    +__init__(self, users_path, s3_bucket, s3_client)
    +_key(self, username, filename, suffix)
    +get_storage_usage(self, username)
    +upload_encrypted_file(self, username, file_storage, wrapped_fek)
    +get_encrypted_file_and_key(self, username, filename)
    +list_encrypted_files(self, username)
  }
  class message_py_MessageController {
    <<class>>
    +__init__(self, users_path, users_db_path)
    +send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)
    +get_messages(self, username, page, per_page)
  }
  class secure_channel_py_ChannelMode {
    <<class>>
    +is_cloudflare_url(value)
    +is_onion_url(value)
    +_as_port(value, default)
    +_as_scheme(value, default)
    +_default_launcher(cmd, log_path)
    +_default_killer(pid)
    +_fingerprint(value)
    +_normalize_onion(raw)
    +_wait_for_pattern(path, pattern, timeout_seconds)
    +_wait_for_file(path, timeout_seconds)
  }
  class secure_channel_py_SecureChannelConfig {
    <<class>>
    +is_cloudflare_url(value)
    +is_onion_url(value)
    +_as_port(value, default)
    +_as_scheme(value, default)
    +_default_launcher(cmd, log_path)
    +_default_killer(pid)
    +_fingerprint(value)
    +_normalize_onion(raw)
    +_wait_for_pattern(path, pattern, timeout_seconds)
    +_wait_for_file(path, timeout_seconds)
  }
  class secure_channel_py_ChannelStatus {
    <<class>>
    +is_cloudflare_url(value)
    +is_onion_url(value)
    +_as_port(value, default)
    +_as_scheme(value, default)
    +_default_launcher(cmd, log_path)
    +_default_killer(pid)
    +_fingerprint(value)
    +_normalize_onion(raw)
    +_wait_for_pattern(path, pattern, timeout_seconds)
    +_wait_for_file(path, timeout_seconds)
  }
  class secure_channel_py_SecureChannelManager {
    <<class>>
    +is_cloudflare_url(value)
    +is_onion_url(value)
    +_as_port(value, default)
    +_as_scheme(value, default)
    +_default_launcher(cmd, log_path)
    +_default_killer(pid)
    +_fingerprint(value)
    +_normalize_onion(raw)
    +_wait_for_pattern(path, pattern, timeout_seconds)
    +_wait_for_file(path, timeout_seconds)
  }
  class sync_py_SyncController {
    <<class>>
    +__init__(self, users_path, s3_bucket, s3_client, file_controller)
    +get_storage_usage(self, username)
  }
  class contact_py_ContactModel {
    <<class>>
    +__init__(self, db_path)
    +_init_db(self)
    +create_contact(self, user_id, subject, message)
    +get_user_contacts(self, user_id)
    +_convert_row_to_dict(self, row)
    +get_all_contacts(self, page, per_page)
    +_convert_row_to_dict_with_username(self, row)
  }
  class contact_py_ContactDB {
    <<class>>
    +__init__(self, db_path)
    +_init_db(self)
    +create_contact(self, user_id, subject, message)
    +get_user_contacts(self, user_id)
    +_convert_row_to_dict(self, row)
    +get_all_contacts(self, page, per_page)
    +_convert_row_to_dict_with_username(self, row)
  }
  class deniable_vault_py_DeniableVaultDB {
    <<class>>
    +__init__(self, db_path)
    +_init_db(self)
    +upsert(self, username, envelope)
    +get(self, username)
    +exists(self, username)
  }
  class message_py_MessageModel {
    <<class>>
    +__init__(self, base_path)
    +save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)
    +get_messages(self, recipient, page, per_page)
    +delete_old_messages(self, recipient, days)
  }
  class message_py_MessageDB {
    <<class>>
    +__init__(self, base_path)
    +save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)
    +get_messages(self, recipient, page, per_page)
    +delete_old_messages(self, recipient, days)
  }
  class plans_py_PlanDB {
    <<class>>
    +__init__(self, db_path)
    +_init_db(self)
    +get_plan(self, plan_name)
    +get_all_plans(self)
    +create_plan(self, name, storage_quota, trial_days, price)
    +update_plan(self, name, storage_quota, trial_days, price)
    +delete_plan(self, name)
    +_convert_row_to_dict(self, row)
    +validate_plan_payment(self, plan_name, amount_paid)
  }
  class superadmin_audit_py_SuperadminAuditDB {
    <<class>>
    +__init__(self, db_path)
    +_init_db(self)
    +record(self, actor, action, target_user, ip, details)
    +recent(self, limit)
  }
  class user_py_UserModel {
    <<class>>
    +get_id(self)
    +is_active(self)
    +__init__(self, db_path)
    +_init_db(self)
    +_has_phone_unique_constraint(self)
    +_drop_phone_unique_if_present(self)
    +_migrate_from_v7(self, legacy_columns)
    +create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled, recovery_salt, encrypted_private_key_recovery)
    +update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)
    +update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)
  }
  class user_py_UserDB {
    <<class>>
    +get_id(self)
    +is_active(self)
    +__init__(self, db_path)
    +_init_db(self)
    +_has_phone_unique_constraint(self)
    +_drop_phone_unique_if_present(self)
    +_migrate_from_v7(self, legacy_columns)
    +create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled, recovery_salt, encrypted_private_key_recovery)
    +update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)
    +update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)
  }
  class doctor_py_CheckResult {
    <<class>>
    +load_env_file(path)
    +effective_env()
    +check_python(minimum)
    +check_module(name)
    +check_binary(name, env_override)
    +check_env_file()
    +parse_host_port(uri, default_port)
    +check_tcp(name, host, port, timeout)
    +debian_arch(deb)
    +cloudflared_deb_url(version, arch)
  }
  class doctor_py_DoctorReport {
    <<class>>
    +load_env_file(path)
    +effective_env()
    +check_python(minimum)
    +check_module(name)
    +check_binary(name, env_override)
    +check_env_file()
    +parse_host_port(uri, default_port)
    +check_tcp(name, host, port, timeout)
    +debian_arch(deb)
    +cloudflared_deb_url(version, arch)
  }
  class test_bloque1_py__FakeUser {
    <<class>>
    +_load_user(uid)
    +check(name, ok, detail)
    +__init__(self, row)
    +is_authenticated(self)
    +is_active(self)
    +is_anonymous(self)
    +get_id(self)
  }
  class conftest_py__ListLogHandler {
    <<class>>
    +_hermetic_env(monkeypatch)
    +_push_request_context()
    +app(tmp_path)
    +client(app)
    +audit_records()
    +__init__(self)
    +emit(self, record)
  }
  class test_cover_py_TestCatalog {
    <<class>>
    +fast_hasher()
    +renderer()
    +store(tmp_path, renderer)
    +_facade_overrides(fast_hasher)
    +_client(tmp_path, fast_hasher)
    +test_catalog_ships_five_distinct_templates(self)
    +test_default_template_exists(self)
    +test_every_template_validates_and_renders(self, renderer)
    +test_empty_payload_fills_defaults(self)
    +test_unknown_variable_is_rejected(self)
  }
  class test_cover_py_TestSanitizer {
    <<class>>
    +fast_hasher()
    +renderer()
    +store(tmp_path, renderer)
    +_facade_overrides(fast_hasher)
    +_client(tmp_path, fast_hasher)
    +test_catalog_ships_five_distinct_templates(self)
    +test_default_template_exists(self)
    +test_every_template_validates_and_renders(self, renderer)
    +test_empty_payload_fills_defaults(self)
    +test_unknown_variable_is_rejected(self)
  }
  class test_cover_py_TestRenderer {
    <<class>>
    +fast_hasher()
    +renderer()
    +store(tmp_path, renderer)
    +_facade_overrides(fast_hasher)
    +_client(tmp_path, fast_hasher)
    +test_catalog_ships_five_distinct_templates(self)
    +test_default_template_exists(self)
    +test_every_template_validates_and_renders(self, renderer)
    +test_empty_payload_fills_defaults(self)
    +test_unknown_variable_is_rejected(self)
  }
  class test_cover_py_TestCustomStore {
    <<class>>
    +fast_hasher()
    +renderer()
    +store(tmp_path, renderer)
    +_facade_overrides(fast_hasher)
    +_client(tmp_path, fast_hasher)
    +test_catalog_ships_five_distinct_templates(self)
    +test_default_template_exists(self)
    +test_every_template_validates_and_renders(self, renderer)
    +test_empty_payload_fills_defaults(self)
    +test_unknown_variable_is_rejected(self)
  }
  class test_cover_py_TestCoverService {
    <<class>>
    +fast_hasher()
    +renderer()
    +store(tmp_path, renderer)
    +_facade_overrides(fast_hasher)
    +_client(tmp_path, fast_hasher)
    +test_catalog_ships_five_distinct_templates(self)
    +test_default_template_exists(self)
    +test_every_template_validates_and_renders(self, renderer)
    +test_empty_payload_fills_defaults(self)
    +test_unknown_variable_is_rejected(self)
  }
  class test_cover_py_TestCoverHttp {
    <<class>>
    +fast_hasher()
    +renderer()
    +store(tmp_path, renderer)
    +_facade_overrides(fast_hasher)
    +_client(tmp_path, fast_hasher)
    +test_catalog_ships_five_distinct_templates(self)
    +test_default_template_exists(self)
    +test_every_template_validates_and_renders(self, renderer)
    +test_empty_payload_fills_defaults(self)
    +test_unknown_variable_is_rejected(self)
  }
  class test_deniable_vault_py_TestDeniableVaultConfig {
    <<class>>
    +config()
    +validator(config)
    +_ciphertext(config, length)
    +_valid_envelope(config)
    +_make_user(app, username, role)
    +_login(client, app, username, role)
    +_csrf(client)
    +test_defaults_are_self_consistent(self)
    +test_expected_ct_length_matches_base64_formula(self, config)
    +test_mapping_overrides_defaults(self)
  }
  class test_deniable_vault_py_TestEnvelopeValidator {
    <<class>>
    +config()
    +validator(config)
    +_ciphertext(config, length)
    +_valid_envelope(config)
    +_make_user(app, username, role)
    +_login(client, app, username, role)
    +_csrf(client)
    +test_defaults_are_self_consistent(self)
    +test_expected_ct_length_matches_base64_formula(self, config)
    +test_mapping_overrides_defaults(self)
  }
  class test_deniable_vault_py_TestRandomContainer {
    <<class>>
    +config()
    +validator(config)
    +_ciphertext(config, length)
    +_valid_envelope(config)
    +_make_user(app, username, role)
    +_login(client, app, username, role)
    +_csrf(client)
    +test_defaults_are_self_consistent(self)
    +test_expected_ct_length_matches_base64_formula(self, config)
    +test_mapping_overrides_defaults(self)
  }
  class test_deniable_vault_py_TestDeniableVaultDB {
    <<class>>
    +config()
    +validator(config)
    +_ciphertext(config, length)
    +_valid_envelope(config)
    +_make_user(app, username, role)
    +_login(client, app, username, role)
    +_csrf(client)
    +test_defaults_are_self_consistent(self)
    +test_expected_ct_length_matches_base64_formula(self, config)
    +test_mapping_overrides_defaults(self)
  }
  class test_deniable_vault_py_TestDeniableVaultController {
    <<class>>
    +config()
    +validator(config)
    +_ciphertext(config, length)
    +_valid_envelope(config)
    +_make_user(app, username, role)
    +_login(client, app, username, role)
    +_csrf(client)
    +test_defaults_are_self_consistent(self)
    +test_expected_ct_length_matches_base64_formula(self, config)
    +test_mapping_overrides_defaults(self)
  }
  class test_deniable_vault_py_TestDeniableVaultApi {
    <<class>>
    +config()
    +validator(config)
    +_ciphertext(config, length)
    +_valid_envelope(config)
    +_make_user(app, username, role)
    +_login(client, app, username, role)
    +_csrf(client)
    +test_defaults_are_self_consistent(self)
    +test_expected_ct_length_matches_base64_formula(self, config)
    +test_mapping_overrides_defaults(self)
  }
  class test_facade_py_TestFacadeConfig {
    <<class>>
    +fast_hasher()
    +gate_config(fast_hasher)
    +_facade_overrides(fast_hasher)
    +facade_client(tmp_path, fast_hasher)
    +_make_user(app_or_path, username)
    +_csrf(client)
    +test_defaults_keep_the_facade_off(self)
    +test_defaults_keep_duress_alert_off(self)
    +test_defaults_are_self_consistent(self)
    +test_mapping_overrides_defaults(self)
  }
  class test_facade_py_TestGatePhraseHasher {
    <<class>>
    +fast_hasher()
    +gate_config(fast_hasher)
    +_facade_overrides(fast_hasher)
    +facade_client(tmp_path, fast_hasher)
    +_make_user(app_or_path, username)
    +_csrf(client)
    +test_defaults_keep_the_facade_off(self)
    +test_defaults_keep_duress_alert_off(self)
    +test_defaults_are_self_consistent(self)
    +test_mapping_overrides_defaults(self)
  }
  class test_facade_py_TestGateTicket {
    <<class>>
    +fast_hasher()
    +gate_config(fast_hasher)
    +_facade_overrides(fast_hasher)
    +facade_client(tmp_path, fast_hasher)
    +_make_user(app_or_path, username)
    +_csrf(client)
    +test_defaults_keep_the_facade_off(self)
    +test_defaults_keep_duress_alert_off(self)
    +test_defaults_are_self_consistent(self)
    +test_mapping_overrides_defaults(self)
  }
  class test_facade_py_TestFacadeGate {
    <<class>>
    +fast_hasher()
    +gate_config(fast_hasher)
    +_facade_overrides(fast_hasher)
    +facade_client(tmp_path, fast_hasher)
    +_make_user(app_or_path, username)
    +_csrf(client)
    +test_defaults_keep_the_facade_off(self)
    +test_defaults_keep_duress_alert_off(self)
    +test_defaults_are_self_consistent(self)
    +test_mapping_overrides_defaults(self)
  }
  class test_facade_py_TestFacadeHttp {
    <<class>>
    +fast_hasher()
    +gate_config(fast_hasher)
    +_facade_overrides(fast_hasher)
    +facade_client(tmp_path, fast_hasher)
    +_make_user(app_or_path, username)
    +_csrf(client)
    +test_defaults_keep_the_facade_off(self)
    +test_defaults_keep_duress_alert_off(self)
    +test_defaults_are_self_consistent(self)
    +test_mapping_overrides_defaults(self)
  }
  class test_padding_py__FakeS3 {
    <<class>>
    +test_pad_roundtrip_message_sizes()
    +test_pad_roundtrip_file_kind()
    +test_bucket_boundaries()
    +test_pad_output_length_is_bucketed()
    +test_pad_uses_fresh_randomness()
    +test_pad_rejects_oversize()
    +test_unpad_rejects_non_bucket_length()
    +test_unpad_rejects_corrupt_prefix()
    +test_unpad_rejects_wrong_kind()
    +test_wire_lengths()
  }
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [{"cohesion": 0.442, "id": 0, "label": "views: auth", "size": 14}, {"cohesion": 0.406, "id": 1, "label": "views: facade", "size": 11}, {"cohesion": 0.889, "id": 2, "label": "static/js", "size": 9}, {"cohesion": 0.471, "id": 3, "label": "controllers", "size": 8}, {"cohesion": 0.5, "id": 4, "label": "views: deniable_vault", "size": 8}, {"cohesion": 0.474, "id": 5, "label": "utils", "size": 8}, {"cohesion": 0.667, "id": 6, "label": "tools", "size": 4}], "god_nodes": [{"node_id": "app_factory.py", "score": 48.8}, {"node_id": "models/user.py", "score": 30.7}, {"node_id": "utils/utils.py", "score": 28.8}, {"node_id": "views/auth.py", "score": 24.9}, {"node_id": "views/admin.py", "score": 21.9}, {"node_id": "utils/security.py", "score": 19.0}, {"node_id": "static/js/qv-crypto.js", "score": 18.0}, {"node_id": "controllers/auth.py", "score": 15.4}, {"node_id": "controllers/facade.py", "score": 14.6}, {"node_id": "controllers/message.py", "score": 12.4}], "surprising_connections": [{"hops": 9, "source": "models/contact.py", "target": "static/js/account.js"}, {"hops": 8, "source": "controllers/contact.py", "target": "static/js/account.js"}, {"hops": 8, "source": "controllers/deniable_vault.py", "target": "static/js/account.js"}, {"hops": 8, "source": "controllers/facade.py", "target": "static/js/account.js"}, {"hops": 8, "source": "controllers/secure_channel.py", "target": "static/js/account.js"}]}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "app_factory"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "boto3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "botocore.config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "flask_cors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "flask_limiter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "flask_limiter.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "flask_mail"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "flask_talisman"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "flask_wtf.csrf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "werkzeug.middleware.proxy_fix"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "controllers.file"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "controllers.sync"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "utils.integrity"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.about"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.account"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.admin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.auth"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.faq"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.file"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.message"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.privacy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.sync"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.terms"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.views"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.facade"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_factory.py", "target": "views.subscription"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.go", "target": "crypto/aes"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.go", "target": "crypto/cipher"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.go", "target": "crypto/rand"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.go", "target": "flag"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.go", "target": "fmt"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.go", "target": "net"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.go", "target": "github.com/open-quantum-safe/liboqs-go/oqs"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.py", "target": "socket"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.py", "target": "oqs"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.py", "target": "cryptography.hazmat.primitives.ciphers.aead"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.py", "target": "cryptography.hazmat.primitives"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.py", "target": "cryptography.hazmat.primitives.kdf.pbkdf2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "client.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "pytz"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "flask_mail"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "clicksend_client"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "clicksend_client"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "clicksend_client.rest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "models.plans"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "utils.mailer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/auth.py", "target": "utils.security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/contact.py", "target": "models.contact"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/contact.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "binascii"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "base64"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "models.deniable_vault"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/deniable_vault.py", "target": "utils.security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "argon2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "argon2.exceptions"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "itsdangerous"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/facade.py", "target": "utils.security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/file.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/file.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/file.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/file.py", "target": "werkzeug.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/file.py", "target": "utils.padding"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/file.py", "target": "boto3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/file.py", "target": "botocore.exceptions"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "models.message"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "utils.padding"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "base64"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "binascii"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "uuid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/message.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "signal"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/secure_channel.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/sync.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/sync.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/sync.py", "target": "boto3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "controllers/sync.py", "target": "botocore.exceptions"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "archive/tar"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "compress/gzip"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "crypto/aes"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "crypto/cipher"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "crypto/rand"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "flag"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "fmt"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "io"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "path/filepath"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "strings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "github.com/open-quantum-safe/liboqs-go/oqs"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "golang.org/x/crypto/pbkdf2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.go", "target": "crypto/sha256"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "io"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "oqs"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "cryptography.hazmat.primitives.ciphers.aead"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "cryptography.hazmat.primitives.kdf.pbkdf2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "cryptography.hazmat.primitives"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "boto3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "botocore.exceptions"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "enc_dec.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "pydantic"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "sqlite3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "pytz"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/contact.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/deniable_vault.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/deniable_vault.py", "target": "sqlite3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/deniable_vault.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/deniable_vault.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "pydantic"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "base64"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "uuid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/message.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/plans.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/plans.py", "target": "sqlite3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/superadmin_audit.py", "target": "sqlite3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/superadmin_audit.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/superadmin_audit.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/user.py", "target": "pydantic"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/user.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/user.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/user.py", "target": "sqlite3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/user.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/user.py", "target": "pytz"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "models/user.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "pq_decrypt_password.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "pq_decrypt_password.py", "target": "utils.crypto"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "importlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "platform"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "socket"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "urllib.request"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/doctor.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/email_tool.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/email_tool.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/email_tool.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/email_tool.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/email_tool.py", "target": "flask_mail"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/email_tool.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/email_tool.py", "target": "utils.mailer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/email_tool.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/makeadmin.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/makeadmin.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/makeadmin.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/makeadmin.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/test_bloque1.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/test_bloque1.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/test_bloque1.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/test_bloque1.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/test_bloque1.py", "target": "app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/test_bloque1.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "scripts/test_bloque1.py", "target": "views.admin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.go", "target": "crypto/aes"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.go", "target": "crypto/cipher"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.go", "target": "fmt"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.go", "target": "net"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.go", "target": "github.com/open-quantum-safe/liboqs-go/oqs"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.py", "target": "socket"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.py", "target": "oqs"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.py", "target": "cryptography.hazmat.primitives.ciphers.aead"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.py", "target": "cryptography.hazmat.primitives"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "server.py", "target": "cryptography.hazmat.primitives.kdf.pbkdf2"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/account.js", "target": "./qv-deniable.js"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "notes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "present"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "add"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "csrfToken"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "apiRequest"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "csrfToken"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "stringify"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "loadState"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "apiRequest"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "collectSlots"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "push"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "handleConfigure"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "preventDefault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "collectSlots"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "buildDeniableVault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "apiRequest"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "reset"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "error"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "handleOpen"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "preventDefault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "openDeniableVault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "handleReset"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "apiRequest"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "loadState"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "loadState"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/account.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "randomChar"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "floor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "random"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "toUpperCase"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "animateElement"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "split"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "contains"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "map"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "join"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "timeline"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "floor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "randomChar"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "querySelectorAll"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "forEach"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/coded-text.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/login.js", "target": "./qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "controller"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "handleLogin"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "preventDefault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "querySelector"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "querySelector"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "login"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "error"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/login.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/messages.js", "target": "./qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "controller"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "textContent"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "getCsrfToken"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "querySelector"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "handleSend"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "preventDefault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "sendSecureMessage"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "error"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "collectEnvelopes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "from"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "parse"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "push"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "envelope"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "handleDecryptInbox"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "collectEnvelopes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "prompt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "decryptInbox"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "forEach"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "error"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "initEditor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "value"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "handleDecryptInbox"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "initEditor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/messages.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/qv-crypto.js", "target": "./vendor/sha2.js"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/qv-crypto.js", "target": "./vendor/hkdf.js"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/qv-crypto.js", "target": "./vendor/ml_kem.js"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/qv-crypto.js", "target": "./vendor/ed25519.js"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/qv-crypto.js", "target": "./qv-padding.js"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "768"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bucket"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "768"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "concatBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "reduce"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "set"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "hexToBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parseInt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "toString"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "padStart"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fromCharCode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "btoa"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase32"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "base64ToBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "atob"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "charCodeAt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBigInt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "i2osp"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "mod"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "return"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "modPow"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "mod"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "randomBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "min"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "getRandomValues"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "sha256"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBigInt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "vault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveKeyFromPassphrase"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "importKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveBits"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveMasterKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveKeyFromPassphrase"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmEncrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "importKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "randomBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "concatBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "importKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "slice"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "slice"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmEncrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "separate"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "module"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "computeK"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "i2osp"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveVerifier"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "srpLogin"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBigInt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "modPow"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "postJson"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "computeK"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "i2osp"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "modPow"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "map"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "i2osp"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "i2osp"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "postJson"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "hybrid"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "generateIdentity"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "keygen"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "keygen"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "keygen"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "encode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parsePublicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parse"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "decode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "base64ToBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "base64ToBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parsePrivateBlob"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parse"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "decode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "base64ToBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "base64ToBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveWrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "hkdf"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "encode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "wrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parsePublicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "encapsulate"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "keygen"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "getSharedSecret"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveWrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmEncrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "unwrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parsePrivateBlob"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parse"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "decode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "decapsulate"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "getSharedSecret"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveWrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "recovery"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "generateRecoveryCode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase32"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "push"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "join"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "normalizeRecoveryCode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "trim"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "toUpperCase"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "replace"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "wrapPrivateKeyForRecovery"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveMasterKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "key"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "innerSK"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "publicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "derivePublicKeyFromPrivateBlob"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "parsePrivateBlob"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "slice"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "getPublicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "postJson"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "endpoint"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "buildRegistration"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveVerifier"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "generateIdentity"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveMasterKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "generateRecoveryCode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "wrapPrivateKeyForRecovery"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "register"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "buildRegistration"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "postJson"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "recoverAccount"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveMasterKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "derivePublicKeyFromPrivateBlob"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveVerifier"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveMasterKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "postJson"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "login"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "srpLogin"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "encryptAndUpload"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "randomBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "padFramed"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmEncrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "wrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "append"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "append"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "append"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "downloadAndDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveMasterKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "unwrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "unframeFramed"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetchPublicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "return"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "recipient"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "sendSecureMessage"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "randomBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "padFramed"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmEncrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetchPublicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "wrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetchPublicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "wrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "postJson"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "decryptInbox"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "deriveMasterKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "unwrapKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "aesGcmDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "unframeFramed"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "push"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-crypto.js", "target": "push"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/qv-deniable.js", "target": "./qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "vault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "server"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "list"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "toBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "encode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "len"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "frame"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "randomBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "setUint32"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "set"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "frame"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "unframe"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "getUint32"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "slice"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "sealSlot"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "randomBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "deriveKeyFromPassphrase"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "aesGcmEncrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "slice"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "slice"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "bytesToHex"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "bytesToBase64"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "openSlot"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "deriveKeyFromPassphrase"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "base64ToBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "aesGcmDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "unframe"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "buildDeniableVault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "map"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "toBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "push"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "randomBytes"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "frame"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "push"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "openDeniableVault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "openSlot"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-deniable.js", "target": "decode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "padding"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "len"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "tableFor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "bucketFor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "tableFor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "randomPad"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "getRandomValues"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "padFramed"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "bucketFor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "randomPad"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "set"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "setUint32"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "set"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "unframeFramed"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "tableFor"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "getUint32"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/qv-padding.js", "target": "slice"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/recover.js", "target": "./qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "controller"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "recoverAccount"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "toggle"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "toggle"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "handleRecover"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "preventDefault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "querySelector"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "trim"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "trim"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "querySelector"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "recoverAccount"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "error"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "setStatus"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/recover.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/register.js", "target": "./qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "controller"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "showRecoveryCode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "resolve"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "remove"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "add"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "resolve"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "handleRegister"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "preventDefault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "fromEntries"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "querySelector"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "payload"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "buildRegistration"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "showRecoveryCode"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "error"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/register.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "static/js/upload.js", "target": "./qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "controller"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getCsrfToken"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "querySelector"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getUsername"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getPublicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "fetch"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getCsrfToken"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "json"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "handleUpload"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "preventDefault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getPublicKey"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "encryptAndUpload"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "reload"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "handleDownload"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "preventDefault"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "prompt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "downloadAndDecrypt"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "createObjectURL"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "createElement"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "appendChild"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "click"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "revokeObjectURL"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "remove"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "alert"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getElementById"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "handleUpload"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "getUsername"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "querySelectorAll"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "forEach"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "handleDownload"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "addEventListener"}, {"confidence": "EXTRACTED", "relation": "calls", "source": "static/js/upload.js", "target": "init"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "templates/terms.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/conftest.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/conftest.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/conftest.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/conftest.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/conftest.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/conftest.py", "target": "app_factory"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/conftest.py", "target": "utils.security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/conftest.py", "target": "dotenv"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_account_facade.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_account_facade.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_account_facade.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_account_facade.py", "target": "app_factory"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_account_facade.py", "target": "controllers.facade"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_account_facade.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_auth_phone.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cover.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cover.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cover.py", "target": "app_factory"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cover.py", "target": "controllers.cover"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cover.py", "target": "controllers.facade"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "base64"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "controllers.deniable_vault"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "models.deniable_vault"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_deniable_vault.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_doctor.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_doctor.py", "target": "importlib.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_doctor.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_doctor.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_doctor.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_facade.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_facade.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_facade.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_facade.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_facade.py", "target": "app_factory"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_facade.py", "target": "controllers.facade"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_facade.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integrity.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integrity.py", "target": "base64"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integrity.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integrity.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integrity.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integrity.py", "target": "utils.integrity"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integrity.py", "target": "tools.verify_build"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_padding.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_padding.py", "target": "base64"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_padding.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_padding.py", "target": "controllers.file"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_padding.py", "target": "controllers.message"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_padding.py", "target": "utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_padding.py", "target": "utils.padding"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "controllers.secure_channel"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "errno"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "views.admin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "views.admin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "views.admin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "views.admin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "socket"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "views.admin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_secure_channel.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "flask_wtf.csrf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "utils.security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_srp.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_srp.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_srp.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_srp.py", "target": "utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_utils.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_utils.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/generate_sri.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/generate_sri.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/generate_sri.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/generate_sri.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/generate_sri.py", "target": "urllib.request"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/generate_sri.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/generate_sri.py", "target": "utils.integrity"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "io"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "tokenize"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/mutation_test.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/verify_build.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/verify_build.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/verify_build.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/verify_build.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/verify_build.py", "target": "html.parser"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/verify_build.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/verify_build.py", "target": "utils.integrity"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tools/verify_build.py", "target": "utils.padding"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/cache.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/cache.py", "target": "redis"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/cache.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/integrity.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/integrity.py", "target": "base64"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/integrity.py", "target": "functools"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/integrity.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/integrity.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/integrity.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/integrity.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/mailer.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/mailer.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/mailer.py", "target": "flask_mail"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/padding.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/padding.py", "target": "functools"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/padding.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/padding.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/padding.py", "target": "struct"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/padding.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/padding.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/plans.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "pytz"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "apscheduler.schedulers.background"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "flask_mail"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "models.message"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/scheduler.py", "target": "utils.mailer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "functools"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "hmac"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "uuid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "flask_wtf.csrf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "wtforms"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/security.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/srp6a.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/srp6a.py", "target": "hmac"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/srp6a.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/srp6a.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/srp6a.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/srp6a.py", "target": "redis"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/utils.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/utils.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/utils.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/utils.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/utils.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/utils.py", "target": "werkzeug.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "utils/utils.py", "target": "dotenv"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/about.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "flask_limiter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "flask_limiter.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "controllers.deniable_vault"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "controllers.facade"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "models.deniable_vault"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/account.py", "target": "utils.security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "models.plans"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "flask_wtf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "wtforms"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "wtforms.validators"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "flask_limiter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "flask_limiter.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "auth"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "controllers.contact"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "controllers.secure_channel"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "models.superadmin_audit"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "pytz"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "sqlite3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "urllib.parse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "socket"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/admin.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "hmac"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "functools"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "flask_limiter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "flask_limiter.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "flask_wtf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "flask_wtf.csrf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "wtforms"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "wtforms.validators"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "controllers.auth"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "controllers.contact"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "utils.mailer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "utils.security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/auth.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/facade.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/facade.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/facade.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/facade.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/facade.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/facade.py", "target": "flask_wtf.csrf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/facade.py", "target": "controllers.cover"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/facade.py", "target": "controllers.facade"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/faq.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/faq.py", "target": "models.plans"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/faq.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "flask_wtf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "wtforms"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "wtforms.validators"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "flask_limiter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "flask_limiter.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "auth"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/file.py", "target": "base64"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "controllers.message"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "flask_wtf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "wtforms"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "wtforms.validators"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "flask_limiter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "flask_limiter.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "auth"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/message.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/privacy.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "models.plans"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "paypalrestsdk"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "flask_wtf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "wtforms"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "wtforms.validators"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "flask_limiter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "flask_limiter.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/subscription.py", "target": "auth"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/sync.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/sync.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/sync.py", "target": "flask_limiter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/sync.py", "target": "flask_limiter.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/sync.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/sync.py", "target": "werkzeug.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/sync.py", "target": "utils.security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/terms.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/views.py", "target": "flask"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/views.py", "target": "flask_login"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/views.py", "target": "flask_wtf"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/views.py", "target": "wtforms"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/views.py", "target": "models.user"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "views/views.py", "target": "utils.utils"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wsgi.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "wsgi.py", "target": "app_factory"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app.py", "target": "app_factory.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "controllers/file.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "controllers/sync.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "utils/integrity.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/about.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/account.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/admin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/auth.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/faq.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/file.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/message.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/privacy.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/sync.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/terms.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/views.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/facade.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app_factory.py", "target": "views/subscription.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/auth.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/auth.py", "target": "models/plans.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/auth.py", "target": "utils/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/auth.py", "target": "utils/mailer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/auth.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/auth.py", "target": "utils/security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/contact.py", "target": "models/contact.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/deniable_vault.py", "target": "models/deniable_vault.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/deniable_vault.py", "target": "utils/security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/facade.py", "target": "utils/security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/file.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/file.py", "target": "utils/padding.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/message.py", "target": "models/message.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/message.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/message.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "controllers/message.py", "target": "utils/padding.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "scripts/email_tool.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "scripts/email_tool.py", "target": "utils/mailer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "scripts/email_tool.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "scripts/makeadmin.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "scripts/test_bloque1.py", "target": "app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "scripts/test_bloque1.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "scripts/test_bloque1.py", "target": "views/admin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/account.js", "target": "static/js/qv-deniable.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/login.js", "target": "static/js/qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/messages.js", "target": "static/js/qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/qv-crypto.js", "target": "static/js/qv-padding.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/qv-crypto.js", "target": "static/js/register.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/qv-crypto.js", "target": "static/js/login.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/qv-deniable.js", "target": "static/js/qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/qv-padding.js", "target": "utils/padding.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/recover.js", "target": "static/js/qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/register.js", "target": "static/js/qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "static/js/upload.js", "target": "static/js/qv-crypto.js"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/conftest.py", "target": "app_factory.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/conftest.py", "target": "utils/security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_account_facade.py", "target": "app_factory.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_account_facade.py", "target": "controllers/facade.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_account_facade.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cover.py", "target": "app_factory.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cover.py", "target": "controllers/facade.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_deniable_vault.py", "target": "controllers/deniable_vault.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_deniable_vault.py", "target": "models/deniable_vault.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_deniable_vault.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_facade.py", "target": "app_factory.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_facade.py", "target": "controllers/facade.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_facade.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_integrity.py", "target": "utils/integrity.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_integrity.py", "target": "tools/verify_build.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_padding.py", "target": "controllers/file.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_padding.py", "target": "controllers/message.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_padding.py", "target": "utils/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_padding.py", "target": "utils/padding.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_secure_channel.py", "target": "controllers/secure_channel.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_secure_channel.py", "target": "views/admin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_secure_channel.py", "target": "views/admin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_secure_channel.py", "target": "views/admin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_secure_channel.py", "target": "views/admin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_secure_channel.py", "target": "views/admin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "utils/security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_srp.py", "target": "utils/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_utils.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tools/generate_sri.py", "target": "utils/integrity.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tools/verify_build.py", "target": "utils/integrity.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tools/verify_build.py", "target": "utils/padding.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "utils/scheduler.py", "target": "models/message.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "utils/scheduler.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "utils/scheduler.py", "target": "utils/mailer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "utils/security.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/account.py", "target": "controllers/deniable_vault.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/account.py", "target": "controllers/facade.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/account.py", "target": "models/deniable_vault.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/account.py", "target": "utils/security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/admin.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/admin.py", "target": "models/plans.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/admin.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/admin.py", "target": "views/auth.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/admin.py", "target": "controllers/contact.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/admin.py", "target": "controllers/secure_channel.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/admin.py", "target": "models/superadmin_audit.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/admin.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/auth.py", "target": "controllers/auth.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/auth.py", "target": "controllers/contact.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/auth.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/auth.py", "target": "utils/mailer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/auth.py", "target": "utils/security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/auth.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/facade.py", "target": "controllers/facade.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/faq.py", "target": "models/plans.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/faq.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/file.py", "target": "views/auth.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/message.py", "target": "controllers/message.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/message.py", "target": "views/auth.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/subscription.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/subscription.py", "target": "models/plans.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/subscription.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/subscription.py", "target": "views/auth.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/sync.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/sync.py", "target": "utils/security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/views.py", "target": "models/user.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "views/views.py", "target": "utils/utils.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "wsgi.py", "target": "app_factory.py"}], "generator": "readmenator", "metadata": {"edge_count": 4562, "file_count": 88, "language_count": 4, "symbol_count": 813}, "nodes": [{"id": "__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "d49aa57081b0bd6f", "symbol_count": 0, "symbols": []}, {"doc": "Local development entry point.  This script exists for the ``make run`` workflow: the Werkzeug dev server with SSL on the loopback port. It is the only place in the codebase where the dev server is started. Production deployments use ``wsgi.py`` and gunicorn instead.  The Werkzeug interactive debugger is intentionally NOT enabled: even with ``FLASK_DEBUG=1`` we never want the debug PIN surface exposed on a network-reachable port. To get a debugger for local work, run the app under an IDE debugger against this file.", "id": "app.py", "kind": "module", "label": "app.py", "language": "py", "sha256": "6a1b831f5e9cac11", "symbol_count": 2, "symbols": [{"kind": "function", "line": 21, "name": "main", "signature": "def main()"}, {"doc": "Return True if the runtime looks like a public-facing deployment.\n\nThe heuristic is intentionally conservative: any deployment with a\nnon-loopback bind address is treated as production. The Werkzeug\ndebugger is forbidden on those binds.", "kind": "function", "line": 58, "name": "_is_production_like", "signature": "def _is_production_like()"}]}, {"doc": "Application factory for QuantumVault.  The same ``create_app()`` callable powers:  - ``app.py`` (dev: ``flask run`` or Werkzeug's dev server with debug) - ``wsgi.py`` (prod: gunicorn / uWSGI behind a reverse proxy)  The factory enforces three things that the old ``app.py``-as-script pattern could not:  1. No Werkzeug debug PIN is ever exposed. Debug mode is gated on the ``FLASK_DEBUG`` environment variable and the Werkzeug debugger is disabled regardless. 2. Security headers (CSP, HSTS, X-Frame-Options, etc.) are installed via Flask-Talisman in production. The strict policy is the default; tests can override ``security_overrides`` to relax specific headers. 3. The session cookie is hardened: HttpOnly, SameSite=Lax, Secure when the request is HTTPS. ``PERMANENT_SESSION_LIFETIME`` caps the idle/absolute lifetime so an unattended browser does not retain auth indefinitely.  Keeping every global side-effect (``app.config[...]``, blueprint registration, extension init) inside the factory means importing ``quantumvault.app_factory`` is free of side effects. That property matters because ``gunicorn`` forks workers and a top-level ``app = create_app()`` in a module would import-time-bind the app to the parent process and re-execute initialization in each worker.", "id": "app_factory.py", "kind": "module", "label": "app_factory.py", "language": "py", "sha256": "3448e2cdddec44c5", "symbol_count": 8, "symbols": [{"doc": "Return True unless the operator explicitly opts into dev mode.", "kind": "function", "line": 71, "name": "_is_production", "signature": "def _is_production()"}, {"doc": "Return the strict Content-Security-Policy used in production.\n\nThe policy allows:\n\n- ``'self'`` for everything by default\n- the JSDelivr CDN pinned to the specific packages the SPA needs\n  (Bootstrap CSS, EasyMDE CSS/JS, marked) and the cdnjs CDN pinned to\n  the legacy pages that need it (crypto-js, jsencrypt). Every remote\n  asset is loaded with SRI from the manifest, so a compromised CDN\n  cannot execute swapped bytes.\n- ``'unsafe-inline'`` for styles is required because EasyMDE injects\n  inline styles; for scripts it is forbidden.\n- WebAssembly is allowed (``'wasm-unsafe-eval'``) so the client can\n  later compile liboqs-portable to WASM and avoid pure-JS PQ.\n\nAdding a new third-party origin to this list is a security review\ngate. Do not add origins without updating docs/SECURITY_TODO.md.", "kind": "function", "line": 82, "name": "_build_csp", "signature": "def _build_csp()"}, {"doc": "Return kwargs to pass to ``Talisman`` based on the runtime env.", "kind": "function", "line": 119, "name": "_build_talisman_kwargs", "signature": "def _build_talisman_kwargs()"}, {"doc": "Set ``app.config['SECRET_KEY']`` from env, payload.json, or a random value.\n\nThe previous code set a fresh 24-byte hex on every process start.\nThat is correct for development (sessions reset, no surprises) but\nin production the operator MUST set ``FLASK_SECRET_KEY`` (or\n``SECRET_KEY``) to a stable, 32+ byte value. Otherwise every\ngunicorn worker restart invalidates every session, including\nCSRF tokens, and the audit log will show a flood of CSRF rejections.\n\nFor backward compatibility, ``payload.json``'s ``SECRET_KEY`` is\naccepted as a third source so a project that was bootstrapped by\n``make env`` keeps working without a code change. The env var\nalways wins over ``payload.json`` so an operator can override.", "kind": "function", "line": 160, "name": "_configure_secret_key", "signature": "def _configure_secret_key(app, config)"}, {"doc": "Apply session lifetime and cookie hardening.\n\nThe defaults are deliberately conservative:\n\n- 8 hours of permanent session lifetime (then user must re-login)\n- 30 minutes of idle lifetime (rolling refresh on every request)\n- Cookies are HttpOnly, SameSite=Lax, and Secure in production", "kind": "function", "line": 203, "name": "_configure_session", "signature": "def _configure_session(app)"}, {"doc": "Wire up a structured application logger.\n\nThe Werkzeug access log goes through Flask's default handler at\nINFO. Application errors use the standard ``app.logger``. The\naudit logger (``quantumvault.audit``) is configured separately in\n:mod:`utils.security` and writes one-line JSON to stdout.", "kind": "function", "line": 220, "name": "_configure_logging", "signature": "def _configure_logging(app)"}, {"doc": "Build and return a fully-configured Flask application.\n\nArgs:\n    config_overrides: Values to merge into ``app.config`` after\n        defaults are applied. Useful for tests that need to swap\n        the database path or disable the rate limiter.\n    security_overrides: Values to merge into the Talisman kwargs.\n        Used by tests to disable CSP and the HTTPS redirect without\n        forking the whole factory.\n\nReturns:\n    A Flask application ready to be served by gunicorn or the\n    Werkzeug dev server.", "kind": "function", "line": 237, "name": "create_app", "signature": "def create_app(config_overrides, security_overrides)"}, {"kind": "function", "line": 416, "name": "load_user", "signature": "def load_user(user_id)"}]}, {"id": "client.go", "kind": "module", "label": "client.go", "language": "go", "sha256": "0fa0dc65ccec2be4", "symbol_count": 1, "symbols": [{"kind": "function", "line": 13, "name": "main", "signature": "func main("}]}, {"id": "client.py", "kind": "module", "label": "client.py", "language": "py", "sha256": "12ebaa00b85321ba", "symbol_count": 0, "symbols": []}, {"id": "controllers/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "8e4c24fce4d70f9f", "symbol_count": 0, "symbols": []}, {"doc": "Zero-knowledge authentication controller for QuantumVault.  Registration accepts cryptographic material that the browser generated and stores it verbatim: the SRP salt and verifier, the user's public key, the password-encrypted private key blob, and the KDF salt. The server never sees the password or any private key. Login is a Secure Remote Password (SRP-6a) challenge/response (see :mod:`utils.srp6a`) so the password is never transmitted.  Phone verification codes, MFA codes, and recovery codes are never stored in plaintext. They are hashed with a server-side pepper via :func:`utils.security.hash_secret` so a database leak does not hand the attacker ready-to-use codes.", "id": "controllers/auth.py", "kind": "module", "label": "auth.py", "language": "py", "sha256": "70a9c0a901cb28ba", "symbol_count": 14, "symbols": [{"doc": "Return the current time as a timezone-aware UTC datetime.\n\nAvoids the deprecated ``datetime.utcnow()`` which returns a naive\nvalue and triggers a DeprecationWarning in Python 3.12+.", "kind": "function", "line": 49, "name": "_now_utc", "signature": "def _now_utc()"}, {"doc": "Handles zero-knowledge registration and SRP-6a authentication.", "kind": "class", "line": 58, "name": "AuthController", "signature": "class AuthController"}, {"doc": "Initialize the controller.\n\nArgs:\n    db_path: Path to the SQLite user database.\n    mail: Configured Flask-Mail instance for transactional email.\n    storage_uri: Redis URI backing the ephemeral SRP session store.", "kind": "method", "line": 61, "name": "__init__", "signature": "def __init__(self, db_path, mail, storage_uri)"}, {"doc": "Register a user from client-generated zero-knowledge credentials.\n\nArgs:\n    username: The desired unique username.\n    srp_salt: SRP salt (hex) generated on the client.\n    srp_verifier: SRP verifier (hex) generated on the client.\n    public_key: The user's hybrid public key blob (opaque).\n    encrypted_private_key: The password-encrypted private key blob (opaque).\n    kdf_salt: Salt (hex) for the client-side key derivation function.\n    email: The user's email address.\n    phone: The user's phone number.\n    first_name: The user's first name.\n    last_name: The user's last name.\n    recovery_salt: Optional QV-RECOVERY-1 PBKDF2 salt (hex), generated on the client.\n    encrypted_private_key_recovery: Optional QV-RECOVERY-1 AES-256-GCM\n        wrapping of the same private key blob, keyed by a\n        client-generated recovery code instead of the password.\n\nReturns:\n    True on success, False if validation fails or persistence errors.", "kind": "method", "line": 76, "name": "register", "signature": "def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, recovery_salt, encrypted_private_key_recovery)"}, {"doc": "Email the account-confirmation link to a freshly registered user.\n\nThe link targets :func:`views.auth.confirm_email`. When SMTP is not\nconfigured, or the send fails, the link is logged at WARNING so an\noperator can still verify the account from the server logs; this keeps\nlocal and bare-VPS deployments usable before mail credentials exist.\n\nArgs:\n    email: The recipient address.\n    username: The account username (used for the greeting).\n    token: The single-use confirmation token stored on the account.\n\nReturns:\n    True if the mail server accepted the message, False otherwise.", "kind": "method", "line": 156, "name": "send_confirmation_email", "signature": "def send_confirmation_email(self, email, username, token)"}, {"doc": "Begin an SRP-6a login and return the salt and server challenge B.", "kind": "method", "line": 202, "name": "srp_hello", "signature": "def srp_hello(self, username, client_a_hex)"}, {"doc": "Complete an SRP-6a login and return the authenticated user and proof.", "kind": "method", "line": 221, "name": "srp_verify", "signature": "def srp_verify(self, username, client_m1_hex)"}, {"doc": "Send a verification code via SMS.", "kind": "method", "line": 253, "name": "send_sms_verification", "signature": "def send_sms_verification(self, phone, code, username)"}, {"doc": "Verify a phone verification code for a user.\n\nThe stored value is the peppered hash; the supplied code is\nhashed in the same way and the two digests are compared in\nconstant time.", "kind": "method", "line": 274, "name": "verify_phone_code", "signature": "def verify_phone_code(self, username, code)"}, {"doc": "Issue and send a fresh phone verification code.\n\nGenerates a new one-time code, stores its peppered hash with a\n30-minute expiry (overwriting any previous pending code), and\ndispatches it by SMS. Returns False when the account is unknown,\nhas no phone number, is already verified, or the SMS provider is\nnot configured, so the caller can surface an honest result.\n\nArgs:\n    username: The account requesting a new code.\n\nReturns:\n    True if a new code was generated, stored, and accepted by the\n    SMS provider; False otherwise.", "kind": "method", "line": 310, "name": "resend_phone_code", "signature": "def resend_phone_code(self, username)"}, {"doc": "Return True if a verification code has not yet expired.", "kind": "method", "line": 349, "name": "_is_code_valid", "signature": "def _is_code_valid(self, expires_at)"}, {"doc": "Verify a multi-factor authentication code for a user.", "kind": "method", "line": 369, "name": "verify_mfa_code", "signature": "def verify_mfa_code(self, username, code)"}, {"doc": "Generate, store, and send an MFA code to the user's phone.", "kind": "method", "line": 393, "name": "send_mfa_code", "signature": "def send_mfa_code(self, username)"}, {"doc": "Enable or disable MFA for a user.", "kind": "method", "line": 416, "name": "toggle_mfa", "signature": "def toggle_mfa(self, username, enable)"}]}, {"id": "controllers/contact.py", "kind": "module", "label": "contact.py", "language": "py", "sha256": "2f6924b47953e9cf", "symbol_count": 4, "symbols": [{"doc": "Handles logic related to contact messages.", "kind": "class", "line": 4, "name": "ContactController", "signature": "class ContactController"}, {"doc": "Initialize the ContactController with the database path.\n\nArgs:\n    db_path (str): Path to the SQLite database file.", "kind": "method", "line": 6, "name": "__init__", "signature": "def __init__(self, db_path)"}, {"doc": "Create a new contact message.\n\nArgs:\n    user_id (int): ID of the user sending the message.\n    subject (str): Subject of the message.\n    message (str): Content of the message.\n\nReturns:\n    bool: True if the message was created successfully, False otherwise.", "kind": "method", "line": 14, "name": "create_contact", "signature": "def create_contact(self, user_id, subject, message)"}, {"doc": "Retrieve all contact messages for a user.\n\nArgs:\n    user_id (int): ID of the user.\n\nReturns:\n    list[ContactModel]: List of contact messages.", "kind": "method", "line": 36, "name": "get_user_contacts", "signature": "def get_user_contacts(self, user_id)"}]}, {"doc": "QV-DENIABLE-1 deniable vault: configuration, validation, orchestration.  This module is the server-side core of the deniable vault feature. It is strictly zero-knowledge: it validates the *structure* of the opaque container the browser produces, stores it, and serves it back. It never decrypts a slot, never sees a passphrase, and never learns which slot holds the decoy and which holds the hidden data.  Deniability requires that activation leaves no evidence. Two mechanisms provide that:  * Every account always has exactly one container of a fixed shape. The server can mint a well-formed *random* container itself, because the blob is opaque and AES-GCM ciphertext is indistinguishable from random. An unactivated account therefore looks identical to an activated one: \"has a container\" is universal and so reveals nothing. Activation only overwrites the random blob with one whose slots a passphrase can open. * Every container has the same byte size. Each slot's plaintext is padded to a fixed length, so every slot's ciphertext is the same length and every container is the same size, whether or not it hides data.  Three collaborators, each with a single responsibility:  * :class:`DeniableVaultConfig` is the immutable set of structural limits, sourced from the environment with safe defaults. Nothing about the envelope shape is hard-coded at a call site. * :class:`EnvelopeValidator` enforces those limits, including the fixed slot count and the fixed ciphertext length. * :class:`DeniableVaultController` wires the validator to :class:`models.deniable_vault.DeniableVaultDB`, provisions random", "id": "controllers/deniable_vault.py", "kind": "module", "label": "deniable_vault.py", "language": "py", "sha256": "55e81f6ade0d13ee", "symbol_count": 22, "symbols": [{"doc": "Return the length of the standard base64 encoding of ``byte_length`` bytes.", "kind": "function", "line": 81, "name": "_base64_length", "signature": "def _base64_length(byte_length)"}, {"doc": "Serialize an envelope deterministically for storage and sizing.\n\nKeys are sorted and separators are compact so the same logical\nenvelope always serializes to the same bytes. Both the size check in\n:class:`EnvelopeValidator` and the persistence path in\n:class:`DeniableVaultController` use this single function, so the\nbytes that are measured are exactly the bytes that are stored.\n\nArgs:\n    envelope: The envelope mapping to serialize.\n\nReturns:\n    The canonical JSON string.", "kind": "function", "line": 86, "name": "canonical_json", "signature": "def canonical_json(envelope)"}, {"doc": "Raised when an envelope violates a structural invariant.", "kind": "class", "line": 104, "name": "EnvelopeValidationError", "signature": "class EnvelopeValidationError(ValueError)"}, {"doc": "Return ``value`` coerced to int, falling back to ``default``.", "kind": "method", "line": 108, "name": "_coerce_int", "signature": "def _coerce_int(value, default)"}, {"doc": "Return an allow-list of KDF identifiers from a value.\n\nAccepts a comma-separated string (as found in environment variables)\nor any iterable of strings.", "kind": "method", "line": 118, "name": "_coerce_kdf", "signature": "def _coerce_kdf(value, default)"}, {"doc": "Immutable structural limits for a deniable vault container.", "kind": "class", "line": 134, "name": "DeniableVaultConfig", "signature": "class DeniableVaultConfig"}, {"doc": "Validate the structure of an opaque deniable vault envelope.\n\nThe validator never decrypts. It checks only the shape: the schema\nversion, the KDF identifier and iteration count, the exact slot count,\neach slot's hex and base64 fields, and the fixed ciphertext length\nthat makes every container identical in size.", "kind": "class", "line": 272, "name": "EnvelopeValidator", "signature": "class EnvelopeValidator"}, {"doc": "Coordinate validation, provisioning, persistence, and auditing.", "kind": "class", "line": 393, "name": "DeniableVaultController", "signature": "class DeniableVaultController"}, {"doc": "Build a config from a mapping, with environment overrides.\n\nResolution order for every field is: environment variable, then\n``mapping`` entry (e.g. ``app.config``), then the module default.\nDefaults are intentionally not written to ``payload.json`` so the\nrepository carries no per-deployment hint that the feature exists;\nan operator overrides them per-host via the environment.\n\nArgs:\n    mapping: A mapping such as ``app.config``.\n    env: Environment to read overrides from. Defaults to\n        ``os.environ``; injectable for tests.\n\nReturns:\n    The resolved, immutable configuration.", "kind": "method", "line": 148, "name": "from_mapping", "signature": "def from_mapping(cls, mapping, env)"}, {"doc": "Return the exact base64 length every slot ciphertext must have.\n\nA slot's ciphertext is the fixed plaintext length plus the GCM\ntag, base64-encoded. Fixing it makes every container byte-for-byte\nthe same shape.", "kind": "method", "line": 213, "name": "expected_ct_b64_length", "signature": "def expected_ct_b64_length(self)"}, {"doc": "Return a well-formed container filled with random, unopenable data.\n\nUsed to provision an account that has not activated the feature and\nto reset one. The result is structurally indistinguishable from an\nactivated container: random hex salts and nonces, and random\nbase64 ciphertext of exactly the expected length. No passphrase can\nopen it, which is the correct behavior for an unactivated vault.\n\nReturns:\n    A fresh random envelope dict.", "kind": "method", "line": 222, "name": "random_container", "signature": "def random_container(self)"}, {"doc": "Return the parameters the browser needs to build a container.\n\nThe browser reads these instead of hard-coding them, so a change\nto the server policy propagates to clients without a code change.\nThe values are non-secret: they describe the container shape,\nwhich is identical for every account.", "kind": "method", "line": 250, "name": "public_parameters", "signature": "def public_parameters(self)"}, {"doc": "Bind the validator to a configuration.", "kind": "method", "line": 281, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Validate ``envelope``, raising on the first violation.\n\nArgs:\n    envelope: The decoded JSON envelope to validate.\n\nRaises:\n    EnvelopeValidationError: If any structural invariant is\n        violated. The message names the violated invariant and\n        never echoes ciphertext.", "kind": "method", "line": 285, "name": "validate", "signature": "def validate(self, envelope)"}, {"doc": "Validate a single slot.\n\nArgs:\n    index: The slot's position, used only in error messages.\n    slot: The slot mapping to validate.\n\nRaises:\n    EnvelopeValidationError: If the slot is malformed or its\n        ciphertext is not the fixed expected length.", "kind": "method", "line": 339, "name": "_validate_slot", "signature": "def _validate_slot(self, index, slot)"}, {"doc": "Validate that ``value`` is hex of exactly ``expected_length``.\n\nRaises:\n    EnvelopeValidationError: If the value is not a hex string of\n        the expected length.", "kind": "method", "line": 376, "name": "_validate_hex", "signature": "def _validate_hex(value, expected_length, index, field)"}, {"doc": "Initialize the controller.\n\nArgs:\n    db: The opaque container store.\n    config: The structural limits in force.\n    validator: The validator to use. Defaults to one bound to\n        ``config``; injectable for tests.", "kind": "method", "line": 401, "name": "__init__", "signature": "def __init__(self, db, config, validator)"}, {"doc": "Return ``username``'s container, minting a random one if absent.\n\nThe mint-on-read behavior is what makes \"has a container\"\nuniversal: any account that has ever opened its settings has an\nindistinguishable container, so the mere existence of one is not\nevidence of a hidden vault.\n\nArgs:\n    username: The owning account.\n\nReturns:\n    The decoded envelope, always present.", "kind": "method", "line": 419, "name": "load_or_provision", "signature": "def load_or_provision(self, username)"}, {"doc": "Validate and persist a container for ``username``.\n\nArgs:\n    username: The owning account.\n    envelope: The decoded JSON envelope from the client.\n\nRaises:\n    EnvelopeValidationError: If the envelope is structurally\n        invalid; nothing is persisted in that case.", "kind": "method", "line": 441, "name": "save", "signature": "def save(self, username, envelope)"}, {"doc": "Overwrite ``username``'s container with a fresh random one.\n\nReset replaces rather than deletes: removing the row would leave a\ngap that distinguishes a user who deactivated from one who never\nactivated. A random container keeps existence universal.\n\nArgs:\n    username: The owning account.\n\nReturns:\n    The new random envelope.", "kind": "method", "line": 456, "name": "reset", "signature": "def reset(self, username)"}, {"doc": "Return True if ``username`` already has a stored container.", "kind": "method", "line": 474, "name": "exists", "signature": "def exists(self, username)"}, {"kind": "method", "line": 171, "name": "read", "signature": "def read(key)"}]}, {"doc": "QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.  The facade hides QuantumVault behind an innocuous cover application. A secret phrase typed into the cover's search field is the first gate: a correct phrase issues a short-lived signed ticket and marks the session ``real`` or ``duress``; either way the ordinary login page is revealed, so an onlooker cannot tell which phrase was used.  This module is the server-side core. It never stores a phrase, never echoes one into the audit log, and performs the same Argon2id work for a miss, the real phrase, and the duress phrase so the response is not an oracle. The zero-knowledge guarantees of SRP-6a and the deniable vault do not depend on this layer.", "id": "controllers/facade.py", "kind": "module", "label": "facade.py", "language": "py", "sha256": "3a594472f40ea950", "symbol_count": 26, "symbols": [{"doc": "Classification of a submitted gate phrase.", "kind": "class", "line": 63, "name": "GateOutcome", "signature": "class GateOutcome(Enum)"}, {"doc": "The outcome of evaluating a phrase plus any issued ticket.", "kind": "class", "line": 72, "name": "GateDecision", "signature": "class GateDecision"}, {"doc": "Coerce an environment or mapping value to a boolean.", "kind": "method", "line": 79, "name": "_as_bool", "signature": "def _as_bool(value, default)"}, {"doc": "Coerce an environment or mapping value to an integer.", "kind": "method", "line": 88, "name": "_as_int", "signature": "def _as_int(value, default)"}, {"doc": "Coerce a value to non-empty text, falling back to ``default``.", "kind": "method", "line": 98, "name": "_as_text", "signature": "def _as_text(value, default)"}, {"doc": "Coerce a value to text without substituting an empty default.", "kind": "method", "line": 106, "name": "_as_raw_text", "signature": "def _as_raw_text(value, default)"}, {"doc": "Parse a comma-separated path list into a tuple of stripped paths.", "kind": "method", "line": 111, "name": "_as_paths", "signature": "def _as_paths(value, default)"}, {"doc": "Immutable facade configuration resolved from environment and app config.", "kind": "class", "line": 124, "name": "FacadeConfig", "signature": "class FacadeConfig"}, {"doc": "Argon2id hashing and verification for a human-chosen gate phrase.", "kind": "class", "line": 262, "name": "GatePhraseHasher", "signature": "class GatePhraseHasher"}, {"doc": "Short-lived signed ticket binding a session to a gate mode.", "kind": "class", "line": 305, "name": "GateTicket", "signature": "class GateTicket"}, {"doc": "Evaluate gate phrases and issue tickets with constant observable work.", "kind": "class", "line": 336, "name": "FacadeGate", "signature": "class FacadeGate"}, {"doc": "Return whether the facade is enabled and holds a real gate hash.", "kind": "method", "line": 154, "name": "gate_configured", "signature": "def gate_configured(self)"}, {"doc": "Return the cosmetic cover context, never carrying a gate hash.", "kind": "method", "line": 158, "name": "cover_context", "signature": "def cover_context(self)"}, {"doc": "Return the sanitizable cover variable payload.", "kind": "method", "line": 166, "name": "cover_variables", "signature": "def cover_variables(self)"}, {"doc": "Resolve configuration with environment, mapping, then default order.", "kind": "method", "line": 181, "name": "from_mapping", "signature": "def from_mapping(cls, mapping, env)"}, {"doc": "Bind the hasher to explicit Argon2id cost parameters.", "kind": "method", "line": 265, "name": "__init__", "signature": "def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)"}, {"doc": "Return a salted Argon2id digest of ``phrase``.", "kind": "method", "line": 282, "name": "hash", "signature": "def hash(self, phrase)"}, {"doc": "Return whether ``phrase`` matches ``encoded`` without raising.", "kind": "method", "line": 286, "name": "verify", "signature": "def verify(self, phrase, encoded)"}, {"doc": "Build a hasher using the cost parameters of ``config``.", "kind": "method", "line": 296, "name": "from_config", "signature": "def from_config(cls, config)"}, {"doc": "Bind the ticket signer to the app secret and a lifetime.", "kind": "method", "line": 308, "name": "__init__", "signature": "def __init__(self, secret_key, ttl_seconds)"}, {"doc": "Return a signed ticket for ``mode`` or raise for an unknown mode.", "kind": "method", "line": 316, "name": "issue", "signature": "def issue(self, mode)"}, {"doc": "Return the ticket mode, or ``None`` if expired, tampered, or absent.", "kind": "method", "line": 322, "name": "verify", "signature": "def verify(self, token)"}, {"doc": "Bind the gate to its configuration and collaborators.", "kind": "method", "line": 339, "name": "__init__", "signature": "def __init__(self, config, hasher, ticket)"}, {"doc": "Build a gate from configuration and the application secret.", "kind": "method", "line": 351, "name": "build", "signature": "def build(cls, config, secret_key)"}, {"doc": "Classify a phrase and emit only a generic audit event.", "kind": "method", "line": 359, "name": "evaluate", "signature": "def evaluate(self, phrase)"}, {"kind": "method", "line": 189, "name": "read", "signature": "def read(key)"}]}, {"doc": "Encrypted file persistence layer.  The server is intentionally blind to plaintext: it only ever stores opaque ciphertext plus an opaque \"wrapped file encryption key\" (``wrapped_fek``) produced by the browser. Every filename that flows through this controller is normalized via :func:`safe_filename` so the S3 key the user ends up with cannot contain path separators or control characters.", "id": "controllers/file.py", "kind": "module", "label": "file.py", "language": "py", "sha256": "9586b5dd98270c1a", "symbol_count": 9, "symbols": [{"doc": "Log a failed S3 operation without raising further.", "kind": "function", "line": 28, "name": "_log_s3_error", "signature": "def _log_s3_error(operation, error)"}, {"doc": "Return a filename safe to embed in an S3 key.\n\nApplies :func:`werkzeug.utils.secure_filename` to strip any path\ncomponents and control characters, then rejects any residual\nshell-meta characters and NUL bytes. Returns an empty string\nfor empty/None input.", "kind": "function", "line": 33, "name": "safe_filename", "signature": "def safe_filename(name)"}, {"doc": "Persistence for end-to-end encrypted files and their wrapped FEKs.", "kind": "class", "line": 51, "name": "FileController", "signature": "class FileController"}, {"kind": "method", "line": 54, "name": "__init__", "signature": "def __init__(self, users_path, s3_bucket, s3_client)"}, {"doc": "Build the S3 key for a user's encrypted file or FEK.\n\nThe username is the server's truth (it came from the\nauthenticated session), so it does not need additional\nvalidation. The filename is expected to have been normalized\nvia :func:`safe_filename` by the caller.", "kind": "method", "line": 59, "name": "_key", "signature": "def _key(self, username, filename, suffix)"}, {"doc": "Sum the bytes used by ``username``'s encrypted files in S3.", "kind": "method", "line": 71, "name": "get_storage_usage", "signature": "def get_storage_usage(self, username)"}, {"doc": "Persist an already-encrypted file and its wrapped FEK to S3.\n\nThe ciphertext must already be padded client-side to a configured\nfile bucket plus AES-256-GCM overhead. Unpadded uploads are\nrejected so exact plaintext sizes never reach the wire or storage.", "kind": "method", "line": 85, "name": "upload_encrypted_file", "signature": "def upload_encrypted_file(self, username, file_storage, wrapped_fek)"}, {"doc": "Fetch a user's encrypted file and its wrapped FEK from S3.\n\nReturns:\n    A 3-tuple of ``(ciphertext, wrapped_fek, error)``. On success\n    ``error`` is ``None``; on failure it contains a human-readable\n    reason and the byte values are ``None``.", "kind": "method", "line": 118, "name": "get_encrypted_file_and_key", "signature": "def get_encrypted_file_and_key(self, username, filename)"}, {"doc": "List the encrypted files that belong to ``username``.", "kind": "method", "line": 148, "name": "list_encrypted_files", "signature": "def list_encrypted_files(self, username)"}]}, {"doc": "Server-side controller for end-to-end encrypted messages.  The browser generates the CEK, encrypts the message with AES-256-GCM, and wraps the CEK with the recipient's and sender's hybrid public keys. The server stores only opaque material; it cannot derive plaintext or any key.", "id": "controllers/message.py", "kind": "module", "label": "message.py", "language": "py", "sha256": "0c647f4b86d9d253", "symbol_count": 4, "symbols": [{"doc": "Handles message persistence in the zero-knowledge flow.", "kind": "class", "line": 19, "name": "MessageController", "signature": "class MessageController"}, {"doc": "Initialize the controller.\n\nArgs:\n    users_path: Base directory under which each user has a\n        ``messages/`` subdirectory.\n    users_db_path: Path to the SQLite user database, used to verify\n        that a message recipient is a registered account. Defaults\n        to the configured database path when omitted.", "kind": "method", "line": 22, "name": "__init__", "signature": "def __init__(self, users_path, users_db_path)"}, {"doc": "Persist an opaque message envelope for the recipient.\n\nArgs:\n    sender: Sender's username.\n    recipient: Recipient's username.\n    encrypted_message_b64: AES-256-GCM ciphertext (base64) of the\n        message body, with the IV prepended by the browser.\n    cek_for_recipient: Hybrid-wrapped CEK to the recipient's public\n        key (base64 JSON from qv-crypto).\n    cek_for_sender: Hybrid-wrapped CEK to the sender's public key\n        (so the outbox copy is readable).\n\nReturns:\n    True on success, False otherwise. Envelopes whose decoded\n    ciphertext length is not a configured message bucket plus\n    AES-256-GCM overhead are rejected so unpadded clients cannot\n    leak exact plaintext sizes on the wire.", "kind": "method", "line": 36, "name": "send_encrypted_message", "signature": "def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)"}, {"doc": "Return opaque message envelopes for the user.\n\nThe browser unwraps each CEK with the user's private blob; the\nserver only returns the opaque envelopes.\n\nArgs:\n    username: User whose mailbox to read.\n    page: 1-indexed page number.\n    per_page: Messages per page.\n\nReturns:\n    A tuple ``(messages, total_pages)`` of opaque messages.", "kind": "method", "line": 90, "name": "get_messages", "signature": "def get_messages(self, username, page, per_page)"}]}, {"doc": "QV-TUNNEL disposable secure channels over Cloudflare and Tor.  Inspiration comes from LazyOwn operator practice: a disposable ``cloudflared`` quick tunnel exposing a local port through a ``*.trycloudflare.com`` URL, and a disposable Tor onion service exposing the same port as a ``*.onion`` address. LazyOwn runs both with interactive prompts and host-wide side effects. This module replaces that workflow with an unprivileged deterministic supervisor suited to QuantumVault zero-trust operation.  Contract summary:  - Channel modes are ``disabled``, ``cloudflared``, ``tor``, and ``hybrid``. Hybrid runs both backends so traffic can use either path and rotation disposes both addresses at once. - Cloudflare uses ``cloudflared tunnel --url`` against loopback only. The origin scheme follows ``QV_CHANNEL_LOCAL_SCHEME`` (``http`` or ``https``): an ``https`` origin adds ``--no-tls-verify`` so a self-signed dev listener stays reachable instead of answering Bad Gateway. The public URL is parsed from process output with a closed allow-list pattern. No account token is required for quick tunnels and none is accepted here, which keeps rotation fully disposable. - Tor uses an unprivileged ``tor`` process with a generated data directory under the configured state directory. No system ``torrc`` file is modified and no sudo is required. The onion hostname is read from the disposable data directory. - State persists atomically as owner-only JSON. Audit records carry mode plus short fingerprints, never full URLs.", "id": "controllers/secure_channel.py", "kind": "module", "label": "secure_channel.py", "language": "py", "sha256": "9886bb0bd9d1deeb", "symbol_count": 37, "symbols": [{"doc": "Selectable disposable channel mode.", "kind": "class", "line": 65, "name": "ChannelMode", "signature": "class ChannelMode(Enum)"}, {"doc": "Return whether value is a quick-tunnel HTTPS URL.", "kind": "method", "line": 82, "name": "is_cloudflare_url", "signature": "def is_cloudflare_url(value)"}, {"doc": "Return whether value is a v3 onion HTTP address.", "kind": "method", "line": 89, "name": "is_onion_url", "signature": "def is_onion_url(value)"}, {"doc": "Coerce input to a TCP port, falling back on default.", "kind": "method", "line": 96, "name": "_as_port", "signature": "def _as_port(value, default)"}, {"doc": "Coerce input to an origin scheme, accepting http or https only.", "kind": "method", "line": 107, "name": "_as_scheme", "signature": "def _as_scheme(value, default)"}, {"doc": "Immutable secure channel configuration from env and mapping.", "kind": "class", "line": 116, "name": "SecureChannelConfig", "signature": "class SecureChannelConfig"}, {"doc": "Point-in-time view of disposable channel state.", "kind": "class", "line": 174, "name": "ChannelStatus", "signature": "class ChannelStatus"}, {"doc": "Spawn a backend daemon detached from the web worker.", "kind": "method", "line": 193, "name": "_default_launcher", "signature": "def _default_launcher(cmd, log_path)"}, {"doc": "Terminate one tracked backend process group.", "kind": "method", "line": 207, "name": "_default_killer", "signature": "def _default_killer(pid)"}, {"doc": "Supervise disposable Cloudflare and Tor backends.", "kind": "class", "line": 220, "name": "SecureChannelManager", "signature": "class SecureChannelManager"}, {"doc": "Return a short non-reversible fingerprint for audit records.", "kind": "method", "line": 503, "name": "_fingerprint", "signature": "def _fingerprint(value)"}, {"doc": "Normalize a Tor hostname file payload to a full onion URL.", "kind": "method", "line": 509, "name": "_normalize_onion", "signature": "def _normalize_onion(raw)"}, {"doc": "Poll a log file for the first regex match within a timeout.", "kind": "method", "line": 517, "name": "_wait_for_pattern", "signature": "def _wait_for_pattern(path, pattern, timeout_seconds)"}, {"doc": "Poll for a small text file such as the onion hostname file.", "kind": "method", "line": 535, "name": "_wait_for_file", "signature": "def _wait_for_file(path, timeout_seconds)"}, {"doc": "Parse free-form input into a mode, defaulting to disabled.", "kind": "method", "line": 74, "name": "parse", "signature": "def parse(cls, raw)"}, {"doc": "Return whether a disposible channel mode is selected.", "kind": "method", "line": 129, "name": "configured", "signature": "def configured(self)"}, {"doc": "Resolve configuration with environment, mapping, then default order.", "kind": "method", "line": 134, "name": "from_mapping", "signature": "def from_mapping(cls, mapping, env)"}, {"doc": "Return whether any backend address is currently published.", "kind": "method", "line": 184, "name": "active", "signature": "def active(self)"}, {"doc": "Bind the manager to a state directory and backend binaries.", "kind": "method", "line": 223, "name": "__init__", "signature": "def __init__(self, state_dir, local_port, local_scheme, cloudflared_bin, tor_bin, start_timeout_seconds, launcher, killer)"}, {"doc": "Return the loopback origin URL both backends forward to.", "kind": "method", "line": 247, "name": "origin_url", "signature": "def origin_url(self)"}, {"doc": "Build a manager sharing binary paths and ports with config.", "kind": "method", "line": 252, "name": "from_config", "signature": "def from_config(cls, config, launcher, killer)"}, {"doc": "Return live status, pruning dead pids without side effects.", "kind": "method", "line": 270, "name": "status", "signature": "def status(self)"}, {"doc": "Start backends for mode, replacing any running channel.", "kind": "method", "line": 281, "name": "start", "signature": "def start(self, mode)"}, {"doc": "Terminate tracked backends and remove persisted state.", "kind": "method", "line": 301, "name": "stop", "signature": "def stop(self)"}, {"doc": "Dispose current addresses and start the same mode again.", "kind": "method", "line": 314, "name": "rotate", "signature": "def rotate(self)"}, {"doc": "Return an audit-safe detail string without full addresses.", "kind": "method", "line": 321, "name": "audit_details", "signature": "def audit_details(self, action, mode, cloud_url, onion_url)"}, {"doc": "Build a status after validating backend address shapes.", "kind": "method", "line": 337, "name": "_status_for", "signature": "def _status_for(self, mode, cloud_url, onion_url, pids)"}, {"doc": "Return the persisted state file path.", "kind": "method", "line": 352, "name": "_state_path", "signature": "def _state_path(self)"}, {"doc": "Load persisted state, returning None when absent or corrupt.", "kind": "method", "line": 356, "name": "_read_state", "signature": "def _read_state(self)"}, {"doc": "Persist state atomically with owner-only permissions.", "kind": "method", "line": 371, "name": "_write_state", "signature": "def _write_state(self, current)"}, {"doc": "Remove persisted state when present.", "kind": "method", "line": 396, "name": "_remove_state", "signature": "def _remove_state(self)"}, {"doc": "Remove stale per-boot scratch directories left by Tor.", "kind": "method", "line": 405, "name": "_cleanup_scratch", "signature": "def _cleanup_scratch(self)"}, {"doc": "Launch a disposable quick tunnel and parse its public URL.", "kind": "method", "line": 418, "name": "_start_cloudflared", "signature": "def _start_cloudflared(self)"}, {"doc": "Launch an unprivileged disposable onion service.", "kind": "method", "line": 438, "name": "_start_tor", "signature": "def _start_tor(self)"}, {"doc": "Resolve a backend binary without trusting PATH alone.", "kind": "method", "line": 471, "name": "_resolve_binary", "signature": "def _resolve_binary(self, binary)"}, {"doc": "Return whether a tracked pid still exists.", "kind": "method", "line": 488, "name": "_pid_live", "signature": "def _pid_live(self, pid)"}, {"kind": "method", "line": 142, "name": "read", "signature": "def read(key)"}]}, {"doc": "controllers/sync.py", "id": "controllers/sync.py", "kind": "module", "label": "sync.py", "language": "py", "sha256": "95b000a830b9ff47", "symbol_count": 3, "symbols": [{"kind": "class", "line": 7, "name": "SyncController", "signature": "class SyncController"}, {"kind": "method", "line": 8, "name": "__init__", "signature": "def __init__(self, users_path, s3_bucket, s3_client, file_controller)"}, {"doc": "Calcula el uso de almacenamiento del usuario en S3.", "kind": "method", "line": 14, "name": "get_storage_usage", "signature": "def get_storage_usage(self, username)"}]}, {"id": "enc_dec.go", "kind": "module", "label": "enc_dec.go", "language": "go", "sha256": "392403d8bf14ea26", "symbol_count": 4, "symbols": [{"kind": "function", "line": 20, "name": "deriveAESKey", "signature": "func deriveAESKey("}, {"kind": "function", "line": 24, "name": "encryptFile", "signature": "func encryptFile("}, {"kind": "function", "line": 45, "name": "decryptFile", "signature": "func decryptFile("}, {"kind": "function", "line": 69, "name": "main", "signature": "func main("}]}, {"doc": "Offline admin tool for ML-KEM-512 key-wrap encryption (QuantumVault).  WARNING -------- This script is **not** part of the zero-knowledge user trust path. It is an operator-only CLI used to retroactively wrap/unwrap files that were uploaded before the browser-based hybrid ML-KEM-768 + X25519 KEM replaced this flow. Do not call it from any user-facing route. The browser does the encryption for regular users; the server never sees plaintext passwords or private keys.  The script reads the object-storage endpoint (Garage / S3) from the environment:  S3_ENDPOINT_URL   - http://localhost:3900 for local Garage S3_ACCESS_KEY     - scoped Garage key S3_SECRET_KEY     - scoped Garage secret S3_REGION         - S3 region name (default: garage) S3_BUCKET         - bucket name (default: quantumvault)  When ``S3_ENDPOINT_URL`` is unset, the script falls back to plain AWS S3 using the ambient AWS credentials chain. The ``--aws-region`` flag overrides ``S3_REGION`` for a single invocation.", "id": "enc_dec.py", "kind": "module", "label": "enc_dec.py", "language": "py", "sha256": "89bde689095c84ba", "symbol_count": 5, "symbols": [{"doc": "Derive a 32-byte AES key from an ML-KEM shared secret.\n\nArgs:\n    shared_secret: The raw shared secret bytes from ``KeyEncapsulation``.\n\nReturns:\n    A 32-byte AES-256 key suitable for use with :class:`AESGCM`.", "kind": "function", "line": 36, "name": "derive_aes_key", "signature": "def derive_aes_key(shared_secret)"}, {"doc": "Encrypt ``data`` in memory with AES-256-GCM and return nonce + ciphertext.\n\nArgs:\n    data: The plaintext bytes to encrypt.\n    aes_key: The 32-byte AES key.\n\nReturns:\n    A tuple ``(nonce, ciphertext)`` where ``nonce`` is 12 random bytes.", "kind": "function", "line": 49, "name": "encrypt_file_in_memory", "signature": "def encrypt_file_in_memory(data, aes_key)"}, {"doc": "Decrypt ``ciphertext`` in memory with AES-256-GCM and return the plaintext.\n\nArgs:\n    nonce: The 12-byte nonce from the encrypt step.\n    ciphertext: The encrypted bytes.\n    aes_key: The 32-byte AES key.\n\nReturns:\n    The original plaintext bytes.", "kind": "function", "line": 65, "name": "decrypt_file_in_memory", "signature": "def decrypt_file_in_memory(nonce, ciphertext, aes_key)"}, {"doc": "Build a boto3 S3 client honoring the zero-trust environment convention.\n\nArgs:\n    region: The region name (overrides ``S3_REGION`` for this call).\n\nReturns:\n    A configured ``boto3.client('s3')`` instance.", "kind": "function", "line": 81, "name": "_build_s3_client", "signature": "def _build_s3_client(region)"}, {"doc": "Run the offline admin CLI (encrypt or decrypt a single object).", "kind": "function", "line": 103, "name": "main", "signature": "def main()"}]}, {"doc": "install.sh: Script para instalar prerrequisitos y compilar el proyecto postcuantum Fecha: 26 de junio de 2025 Autor: Grok 3 (xAI)", "id": "install.sh", "kind": "module", "label": "install.sh", "language": "sh", "sha256": "c907d80fd6734993", "symbol_count": 0, "symbols": []}, {"id": "make.sh", "kind": "module", "label": "make.sh", "language": "sh", "sha256": "6b19313760683dc6", "symbol_count": 0, "symbols": []}, {"id": "models/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "95bdfaea458995a4", "symbol_count": 0, "symbols": []}, {"id": "models/contact.py", "kind": "module", "label": "contact.py", "language": "py", "sha256": "e61cfbd31022bbc2", "symbol_count": 9, "symbols": [{"doc": "Pydantic model for a contact message.\n\nAttributes:\n    id: Unique contact ID.\n    user_id: ID of the user who sent the message.\n    subject: Subject of the contact message.\n    message: Content of the contact message.\n    created_at: Timestamp when the message was created.\n    status: Status of the message (e.g. 'pending', 'resolved').", "kind": "class", "line": 8, "name": "ContactModel", "signature": "class ContactModel(BaseModel)"}, {"doc": "Database operations for contact messages.", "kind": "class", "line": 26, "name": "ContactDB", "signature": "class ContactDB"}, {"doc": "Initialize the ContactDB with the database path.\n\nArgs:\n    db_path: Path to the SQLite database file.", "kind": "method", "line": 29, "name": "__init__", "signature": "def __init__(self, db_path)"}, {"doc": "Initialize the contacts table with all required fields.", "kind": "method", "line": 38, "name": "_init_db", "signature": "def _init_db(self)"}, {"doc": "Create a new contact message.\n\nArgs:\n    user_id: ID of the user sending the message.\n    subject: Subject of the message.\n    message: Content of the message.\n\nReturns:\n    True on success, False if validation fails or the DB write fails.", "kind": "method", "line": 52, "name": "create_contact", "signature": "def create_contact(self, user_id, subject, message)"}, {"doc": "Retrieve all contact messages for a user.\n\nArgs:\n    user_id: ID of the user.\n\nReturns:\n    List of contact message dictionaries, newest first. On DB\n    error, returns an empty list and logs the failure.", "kind": "method", "line": 89, "name": "get_user_contacts", "signature": "def get_user_contacts(self, user_id)"}, {"doc": "Convert an SQLite row to a dictionary.\n\nArgs:\n    row: SQLite row.\n\nReturns:\n    Contact data as a dictionary.", "kind": "method", "line": 115, "name": "_convert_row_to_dict", "signature": "def _convert_row_to_dict(self, row)"}, {"doc": "Retrieve all contact messages with pagination.\n\nArgs:\n    page: 1-based page number.\n    per_page: Number of contacts per page.\n\nReturns:\n    ``(rows, total_count)``. ``rows`` may be empty on DB error.", "kind": "method", "line": 139, "name": "get_all_contacts", "signature": "def get_all_contacts(self, page, per_page)"}, {"doc": "Convert an SQLite row to a dictionary, including username.", "kind": "method", "line": 168, "name": "_convert_row_to_dict_with_username", "signature": "def _convert_row_to_dict_with_username(self, row)"}]}, {"doc": "Opaque storage for QV-DENIABLE-1 deniable vault containers.  The server is zero-knowledge: it stores one opaque, client-encrypted container per user and never derives, decrypts, or inspects the plaintext. A container is the JSON envelope produced by the browser (see ``static/js/qv-deniable.js``); from the database's point of view it is just text.  The table is deliberately minimal. It carries only what the server must hold to serve the container back and to bound storage:  * ``username`` (primary key) links the row to the owning account. * ``envelope`` is the opaque container text. * ``updated_at`` records when the row last changed, for operator housekeeping. No per-slot metadata is stored, because storing anything that distinguished one slot from another would undermine the deniability guarantee the feature exists to provide.  It lives in the same SQLite file as ``users`` so an operator backup or restore captures identity and vault state together.", "id": "models/deniable_vault.py", "kind": "module", "label": "deniable_vault.py", "language": "py", "sha256": "21c36a0304dee37e", "symbol_count": 6, "symbols": [{"doc": "Persistence for per-user opaque deniable vault containers.", "kind": "class", "line": 30, "name": "DeniableVaultDB", "signature": "class DeniableVaultDB"}, {"doc": "Initialize the store and ensure its table exists.\n\nArgs:\n    db_path: Path to the SQLite database file, shared with\n        :class:`models.user.UserDB`.", "kind": "method", "line": 33, "name": "__init__", "signature": "def __init__(self, db_path)"}, {"doc": "Create the ``deniable_vaults`` table on first use.", "kind": "method", "line": 43, "name": "_init_db", "signature": "def _init_db(self)"}, {"doc": "Insert or replace the container for ``username``.\n\nThe whole container is replaced atomically: a deniable vault has\nno partial state, so a replace is always a full rewrite of the\nopaque envelope.\n\nArgs:\n    username: The owning account's username.\n    envelope: The opaque container text to store verbatim.", "kind": "method", "line": 57, "name": "upsert", "signature": "def upsert(self, username, envelope)"}, {"doc": "Return the stored container for ``username``, or ``None``.\n\nArgs:\n    username: The account to look up.\n\nReturns:\n    A dict with ``username``, ``envelope``, and ``updated_at``,\n    or ``None`` when the account has no container.", "kind": "method", "line": 82, "name": "get", "signature": "def get(self, username)"}, {"doc": "Return True if ``username`` has a stored container.", "kind": "method", "line": 101, "name": "exists", "signature": "def exists(self, username)"}]}, {"doc": "Persistence layer for end-to-end encrypted messages.  The browser performs all cryptography: it generates a random 32-byte content encryption key (CEK), encrypts the message with AES-256-GCM, and wraps the CEK to the recipient's hybrid public key (and to the sender for the outbox copy). The server stores only opaque ciphertext + wrapped keys; it never sees plaintext or can derive the message.  The on-disk format is a tiny key-value file per message::  <sender>|<encrypted_message_b64>|<cek_for_recipient_b64>|<cek_for_sender_b64>|<iso_timestamp>  The actual decryption happens in the browser via ``static/js/qv-crypto.js`` -- the page that lists messages fetches each opaque record and unwraps the CEK with the recipient's private blob.", "id": "models/message.py", "kind": "module", "label": "message.py", "language": "py", "sha256": "d0c2dcf76191f54c", "symbol_count": 6, "symbols": [{"doc": "Pydantic model for a stored message envelope.\n\nAttributes:\n    id (Optional[str]): Message ID.\n    sender (str): Sender username.\n    message (str): Display text. With ZK messages this is the opaque\n        payload returned to the client (the browser decrypts it).\n    timestamp (Optional[datetime]): When the message was stored.", "kind": "class", "line": 27, "name": "MessageModel", "signature": "class MessageModel(BaseModel)"}, {"doc": "File-based operations for end-to-end encrypted messages.", "kind": "class", "line": 43, "name": "MessageDB", "signature": "class MessageDB"}, {"doc": "Initialize the MessageDB with the base directory for per-user mailboxes.\n\nArgs:\n    base_path (str): Filesystem path under which each user has a\n        ``messages/`` subdirectory.", "kind": "method", "line": 46, "name": "__init__", "signature": "def __init__(self, base_path)"}, {"doc": "Persist an opaque message envelope for the recipient.\n\nArgs:\n    recipient (str): Recipient username.\n    sender (str): Sender username.\n    encrypted_message_b64 (str): AES-256-GCM(CEK, plaintext) as base64\n        (IV prepended by the browser).\n    cek_for_recipient (str): Hybrid-wrapped CEK to the recipient's\n        public key (base64-encoded JSON from qv-crypto).\n    cek_for_sender (str): Hybrid-wrapped CEK to the sender's public\n        key (so the outbox copy is readable).\n    message_id (str): Unique message ID.", "kind": "method", "line": 55, "name": "save_message", "signature": "def save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)"}, {"doc": "Return opaque message envelopes for the recipient.\n\nThe browser unwraps the CEK with the user's private blob. This\nmethod never derives any key material.\n\nArgs:\n    recipient (str): Username whose mailbox to read.\n    page (int): 1-indexed page number.\n    per_page (int): Messages per page.\n\nReturns:\n    A tuple ``(messages, total_pages)`` where each message is\n    opaque; the ``message`` field carries the JSON envelope\n    ``{encrypted_message_b64, cek_for_recipient, cek_for_sender}``\n    so the browser can decrypt it.", "kind": "method", "line": 87, "name": "get_messages", "signature": "def get_messages(self, recipient, page, per_page)"}, {"doc": "Delete messages older than ``days`` days from the recipient's mailbox.\n\nArgs:\n    recipient (str): Username whose mailbox to prune.\n    days (int): Age threshold in days; older messages are removed.", "kind": "method", "line": 172, "name": "delete_old_messages", "signature": "def delete_old_messages(self, recipient, days)"}]}, {"id": "models/plans.py", "kind": "module", "label": "plans.py", "language": "py", "sha256": "b39dfc7604a9fa06", "symbol_count": 10, "symbols": [{"doc": "Database operations for subscription plans.", "kind": "class", "line": 4, "name": "PlanDB", "signature": "class PlanDB"}, {"doc": "Initialize the PlanDB with the database path.\n\nArgs:\n    db_path (str): Path to the SQLite database file.", "kind": "method", "line": 6, "name": "__init__", "signature": "def __init__(self, db_path)"}, {"doc": "Initialize the plans table with required fields.", "kind": "method", "line": 15, "name": "_init_db", "signature": "def _init_db(self)"}, {"doc": "Retrieve a plan by name.\n\nArgs:\n    plan_name (str): Name of the plan to search for.\n\nReturns:\n    Optional[Dict]: Plan data as a dictionary or None if not found.", "kind": "method", "line": 37, "name": "get_plan", "signature": "def get_plan(self, plan_name)"}, {"doc": "Retrieve all plans.\n\nReturns:\n    List[Dict]: List of dictionaries containing plan data.", "kind": "method", "line": 50, "name": "get_all_plans", "signature": "def get_all_plans(self)"}, {"doc": "Create a new plan.\n\nArgs:\n    name (str): Name of the plan.\n    storage_quota (int): Storage quota in bytes.\n    trial_days (int): Number of trial days.\n    price (float): Price of the plan.", "kind": "method", "line": 60, "name": "create_plan", "signature": "def create_plan(self, name, storage_quota, trial_days, price)"}, {"doc": "Update an existing plan.\n\nArgs:\n    name (str): Name of the plan to update.\n    storage_quota (Optional[int]): New storage quota in bytes.\n    trial_days (Optional[int]): New number of trial days.\n    price (Optional[float]): New price of the plan.", "kind": "method", "line": 78, "name": "update_plan", "signature": "def update_plan(self, name, storage_quota, trial_days, price)"}, {"doc": "Delete a plan by name.\n\nArgs:\n    name (str): Name of the plan to delete.", "kind": "method", "line": 113, "name": "delete_plan", "signature": "def delete_plan(self, name)"}, {"doc": "Convert an SQLite row to a dictionary.", "kind": "method", "line": 127, "name": "_convert_row_to_dict", "signature": "def _convert_row_to_dict(self, row)"}, {"doc": "Validate that the paid amount matches the plan price.\n\nArgs:\n    plan_name (str): Name of the plan.\n    amount_paid (float): Amount paid.\n\nReturns:\n    bool: True if the amount matches the plan price within tolerance.", "kind": "method", "line": 139, "name": "validate_plan_payment", "signature": "def validate_plan_payment(self, plan_name, amount_paid)"}]}, {"doc": "Append-only audit log for superadmin actions.  Why a separate table: every privileged action (MFA reset, confirmation token re-issue, account suspension) needs an immutable record of who did what to which user, from which IP, and when. Mixing this into the ``users`` table is wrong on two counts:  1. The audit row is written by the superadmin, not the affected user. Adding ``last_reset_by`` / ``last_reset_at`` columns to ``users`` would let an attacker who pwns the DB forge the trail.  2. Audit history is monotonic: an entry must never be UPDATEd or DELETEd. SQLite has no row-level immutability, but a dedicated table with no application code path that writes UPDATEs is the closest we can get.  The table lives in ``instance/users.db`` (same file as ``users``) to keep operator backup / restore symmetric: one file = one snapshot of identity state. Storage is bounded by the operational tempo of the superadmin role, not user activity, so growth is negligible.  Rows are never pruned by the application. If a future retention policy is needed it should be a documented operator script, not a silent DELETE in the request path.", "id": "models/superadmin_audit.py", "kind": "module", "label": "superadmin_audit.py", "language": "py", "sha256": "304d2be2b4bcb78d", "symbol_count": 5, "symbols": [{"doc": "Database operations for the superadmin audit log.", "kind": "class", "line": 32, "name": "SuperadminAuditDB", "signature": "class SuperadminAuditDB"}, {"doc": "Initialize the audit log and ensure its table exists.\n\nArgs:\n    db_path: Path to the SQLite database file (shared with\n        ``UserDB`` so the two are backed up together).", "kind": "method", "line": 35, "name": "__init__", "signature": "def __init__(self, db_path)"}, {"doc": "Create the audit table on first use; no-op if it already exists.", "kind": "method", "line": 45, "name": "_init_db", "signature": "def _init_db(self)"}, {"doc": "Append one audit row and return its id.\n\nThe timestamp is generated server-side in UTC so two operators\nin different timezones can correlate a single incident. The\nreturn value is the new row's primary key, useful for tests\nand for linking related log lines in the response.\n\nArgs:\n    actor: Username of the superadmin performing the action.\n    action: Short verb-noun identifier (e.g. ``reset_mfa``,\n        ``resend_confirmation``, ``toggle_suspend``).\n    target_user: Username the action was applied to, or None\n        for global actions (none today, kept for future use).\n    ip: Remote address that issued the request. ``None`` when\n        the request did not carry one (e.g. background job).\n    details: Free-text context, kept short. Use it for the\n        state transition (e.g. ``active->inactive``) not for\n        payloads that should never leave the audit log.\n\nReturns:\n    The new row's ``id``.", "kind": "method", "line": 75, "name": "record", "signature": "def record(self, actor, action, target_user, ip, details)"}, {"doc": "Return the most recent ``limit`` audit rows, newest first.\n\nArgs:\n    limit: Maximum rows to return. Capped at 500 to bound\n        template rendering cost on a noisy superadmin.\n\nReturns:\n    List of dicts with keys ``id``, ``ts``, ``actor``,\n    ``action``, ``target_user``, ``ip``, ``details``.", "kind": "method", "line": 119, "name": "recent", "signature": "def recent(self, limit)"}]}, {"id": "models/user.py", "kind": "module", "label": "user.py", "language": "py", "sha256": "108bcc05840884d2", "symbol_count": 27, "symbols": [{"doc": "Pydantic model for a user with Flask-Login support.\n\nAttributes:\n    id: Unique user ID.\n    username: Unique username.\n    role: User role (free, bronze, silver, gold, admin, superadmin).\n    email: User's email address.\n    phone: User's phone number.\n    first_name: User's first name.\n    last_name: User's last name.\n    storage_quota: Storage quota in bytes.\n    trial_start: Trial period start date.\n    trial_end: Trial period end date.\n    subscription_status: Subscription status (active, inactive).\n    email_verified: Whether the email is verified.\n    confirmation_token: Email confirmation token.\n    phone_verified: Whether the phone number is verified.\n    phone_verification_code_hash: Peppered hash of the phone verification code.\n    phone_code_expires: Phone verification code expiration.\n    mfa_code_hash: Peppered hash of the current MFA code.\n    mfa_code_expires: MFA code expiration.\n    mfa_enabled: Whether MFA is enabled for the user.", "kind": "class", "line": 8, "name": "UserModel", "signature": "class UserModel(BaseModel, UserMixin)"}, {"doc": "Database operations for users.", "kind": "class", "line": 83, "name": "UserDB", "signature": "class UserDB"}, {"doc": "Return the user ID as a string (required by Flask-Login).\n\nReturns:\n    str: The user ID as a string, or an empty string when the\n        user is anonymous.", "kind": "method", "line": 52, "name": "get_id", "signature": "def get_id(self)"}, {"doc": "Return True while the user can use the application.\n\nInactive (lapsed-subscription) users can still sign in to renew\nor download their data, so we do NOT tie this to\n``subscription_status``. The previous implementation returned\nFalse for inactive users, which logged them out of every\n@login_required route. Subscription-gated features should\ncheck ``subscription_status`` directly in the view that needs\nthe gate, not via Flask-Login's activation hook.", "kind": "method", "line": 70, "name": "is_active", "signature": "def is_active(self)"}, {"doc": "Initialize the UserDB with the database path.\n\nArgs:\n    db_path (str): Path to the SQLite database file.", "kind": "method", "line": 85, "name": "__init__", "signature": "def __init__(self, db_path)"}, {"doc": "Initialize the users table with all fields for zero-knowledge auth.\n\nThe table stores only zero-knowledge credential material: the SRP salt\nand verifier (the password itself is never received), the user's public\nkey, the password-encrypted private key blob, and the key-derivation\nsalt used to protect that blob. The server can decrypt none of it.\n\nPhone verification codes and MFA codes are stored as peppered\nSHA-256 digests (``*_code_hash`` columns) instead of plaintext so\na database dump does not hand an attacker ready-to-use codes.\n\nThe ``phone`` column is not unique: phone numbers are recycled by\ncarriers and SIM-swap attacks invalidate the uniqueness guarantee\nanyway. ``email`` remains unique because it is the primary\nrecovery identity.\n\nIf the table was created by an older v7 schema (which carried\nNOT NULL KEM blob columns the v8 controller never writes),\nmigrate in place: rebuild the table under the v8 shape and preserve\nthe surviving identity columns. The legacy password blobs are\nintentionally dropped: v7 ciphertexts are useless without the\nmatching v7 KEM code path that has been removed.", "kind": "method", "line": 105, "name": "_init_db", "signature": "def _init_db(self)"}, {"doc": "Return True if the ``users.phone`` column is UNIQUE.\n\nSQLite does not expose UNIQUE column constraints via ``PRAGMA\ntable_info``; the only reliable signal is the auto-index that\nSQLite materialises for any ``UNIQUE`` column (``sqlite_autoindex_users_N``).", "kind": "method", "line": 193, "name": "_has_phone_unique_constraint", "signature": "def _has_phone_unique_constraint(self)"}, {"doc": "Remove the UNIQUE constraint on ``users.phone``.\n\nThe v7 schema declared ``phone TEXT UNIQUE``. Carriers recycle\nnumbers, so the uniqueness guarantee is illusory; it also makes\naccount recovery hostile when a number changes hands.\n\nSQLite forbids ``DROP INDEX`` on an auto-index backing a UNIQUE\ncolumn, so we have to rebuild the table. The rebuild follows\nthe same shape as :meth:`_migrate_from_v7` but copies every\ncolumn by position (the schema is now already v8-shaped thanks\nto the prior migration step, so we know the column order).", "kind": "method", "line": 214, "name": "_drop_phone_unique_if_present", "signature": "def _drop_phone_unique_if_present(self)"}, {"doc": "Rebuild the users table to drop legacy v7 NOT NULL KEM columns.\n\nSQLite cannot drop a column or relax a NOT NULL constraint in place,\nso we rename the old table, create a fresh v8-shaped users table,\ncopy every surviving column, then drop the renamed legacy table.", "kind": "method", "line": 271, "name": "_migrate_from_v7", "signature": "def _migrate_from_v7(self, legacy_columns)"}, {"doc": "Persist a new user from client-provided zero-knowledge credentials.\n\nAll cryptographic material (salt, verifier, public key, encrypted\nprivate key, KDF salt) is generated on the client; this method only\nstores opaque values and never derives or sees the password.\nPhone and MFA codes are stored as the peppered hash supplied by\nthe controller; the plaintext only ever lives in the SMS that\nleaves the building.\n\n``recovery_salt`` and ``encrypted_private_key_recovery`` are the\nQV-RECOVERY-1 fields: an independent PBKDF2 salt and AES-256-GCM\nwrapping of the same ``privateBlob``, keyed by a client-generated\nhigh-entropy recovery code instead of the account password. Both\nare optional so older clients that do not yet generate a recovery\ncode can still register.", "kind": "method", "line": 325, "name": "create_user", "signature": "def create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled, recovery_salt, encrypted_private_key_recovery)"}, {"doc": "Update phone verification status and related fields.\n\nThe ``phone_verification_code_hash`` parameter accepts the\npeppered SHA-256 digest. Passing ``None`` clears the stored\nhash (e.g. after the user verifies successfully).", "kind": "method", "line": 362, "name": "update_user_phone_status", "signature": "def update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)"}, {"doc": "Update MFA code, expiration, and enabled status.\n\nThe ``mfa_code_hash`` parameter accepts the peppered SHA-256\ndigest of the freshly-generated 6-digit code. ``mfa_enabled`` is\na tri-state: ``None`` leaves the value alone.", "kind": "method", "line": 396, "name": "update_user_mfa_status", "signature": "def update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)"}, {"doc": "Update specific user fields.", "kind": "method", "line": 430, "name": "update_user", "signature": "def update_user(self, username, email_verified, confirmation_token)"}, {"doc": "Retrieve a user by username.\n\nArgs:\n    username (str): Username to search for.\n\nReturns:\n    Optional[dict]: User data as a dictionary or None if not found.", "kind": "method", "line": 454, "name": "get_user", "signature": "def get_user(self, username)"}, {"doc": "Retrieve a user by ID.\n\nArgs:\n    user_id (int): ID of the user to search for.\n\nReturns:\n    Optional[dict]: User data as a dictionary or None if not found.", "kind": "method", "line": 468, "name": "get_user_by_id", "signature": "def get_user_by_id(self, user_id)"}, {"doc": "Retrieve a user by email address.\n\nArgs:\n    email (str): Email address to search for.\n\nReturns:\n    Optional[dict]: User data as a dictionary or None if not found.", "kind": "method", "line": 482, "name": "get_user_by_email", "signature": "def get_user_by_email(self, email)"}, {"doc": "Retrieve a user by phone number.\n\nArgs:\n    phone (str): Phone number to search for.\n\nReturns:\n    Optional[dict]: User data as a dictionary or None if not found.", "kind": "method", "line": 496, "name": "get_user_by_phone", "signature": "def get_user_by_phone(self, phone)"}, {"doc": "Retrieve a user by confirmation token.\n\nArgs:\n    token (str): Confirmation token to search for.\n\nReturns:\n    Optional[dict]: User data as a dictionary or None if not found.", "kind": "method", "line": 510, "name": "get_user_by_confirmation_token", "signature": "def get_user_by_confirmation_token(self, token)"}, {"doc": "Return the QV-RECOVERY-1 bundle for a username, if one exists.\n\nArgs:\n    username (str): Username to look up.\n\nReturns:\n    A dict with ``recovery_salt``, ``encrypted_private_key_recovery``,\n    and ``public_key`` if the account has a recovery bundle\n    configured, or ``None`` if the account does not exist or has\n    not generated a recovery code (e.g. accounts created before\n    QV-RECOVERY-1 was added).", "kind": "method", "line": 524, "name": "get_recovery_bundle", "signature": "def get_recovery_bundle(self, username)"}, {"doc": "Replace a user's password-derived credentials after a verified recovery.\n\nCalled only after the caller has verified ``public_key_proof``\nagainst the stored ``public_key`` (proof that the requester\npossesses the recovery code, since it is the only way to recover\nthe matching ``privateBlob`` and re-derive the public key). The\n``public_key`` and the underlying keypair are unchanged; only the\nSRP verifier and the password-wrapping of the existing private key\nblob are replaced.\n\nArgs:\n    username (str): Username whose credentials are being reset.\n    srp_salt (str): New SRP salt, hex-encoded.\n    srp_verifier (str): New SRP verifier, hex-encoded.\n    kdf_salt (str): New PBKDF2 salt for the password-wrapped private key, hex-encoded.\n    encrypted_private_key (str): The same private key blob, re-wrapped under the new password.", "kind": "method", "line": 548, "name": "reset_credentials_with_recovery", "signature": "def reset_credentials_with_recovery(self, username, srp_salt, srp_verifier, kdf_salt, encrypted_private_key)"}, {"doc": "Update a user's role, storage quota, and subscription status.\n\nArgs:\n    username (str): Username of the user to update.\n    role (str): New role for the user.\n    storage_quota (int): New storage quota in bytes (default: 10MB).\n    subscription_status (str): New subscription status (default: 'active').", "kind": "method", "line": 579, "name": "update_role", "signature": "def update_role(self, username, role, storage_quota, subscription_status)"}, {"doc": "Return the total number of users.\n\nImplemented as ``SELECT COUNT(*)`` rather than ``len(get_all_users())``\nso the home page does not materialise the entire table on every\nrequest.", "kind": "method", "line": 592, "name": "count_users", "signature": "def count_users(self)"}, {"doc": "Retrieve all users.\n\nReturns:\n    list[dict]: List of dictionaries containing user data.", "kind": "method", "line": 603, "name": "get_all_users", "signature": "def get_all_users(self)"}, {"doc": "Parse a stored timestamp into a datetime, tolerating the format.\n\nArgs:\n    value: A datetime, an ISO-like timestamp string, or None.\n\nReturns:\n    The parsed datetime, or None when the value is empty or unparseable.", "kind": "method", "line": 615, "name": "_parse_datetime", "signature": "def _parse_datetime(value)"}, {"doc": "Convert a name-keyed SQLite row into a plain dictionary.\n\nReads access columns by name (the connection uses ``sqlite3.Row``), so\nthe mapping is robust to column ordering and additive migrations.\n\nArgs:\n    row: A ``sqlite3.Row`` produced by a read query, or None.\n\nReturns:\n    A dictionary of user fields, or None when the row is empty.", "kind": "method", "line": 638, "name": "_convert_row_to_dict", "signature": "def _convert_row_to_dict(self, row)"}, {"doc": "Execute a query and return the first result as a dictionary.\n\nArgs:\n    query (str): SQL query to execute.\n    params (tuple): Parameters for the query (default: empty tuple).\n\nReturns:\n    Optional[dict]: First row as a dictionary or None if no results or an error occurs.", "kind": "method", "line": 694, "name": "fetch_one", "signature": "def fetch_one(self, query, params)"}, {"kind": "method", "line": 655, "name": "value", "signature": "def value(name, default)"}]}, {"id": "pq_decrypt_password.py", "kind": "module", "label": "pq_decrypt_password.py", "language": "py", "sha256": "f019755bae8bda62", "symbol_count": 0, "symbols": []}, {"doc": "Doctor: verify and repair the QuantumVault operator environment.  Used by ``make doctor`` (check only) and ``make doctor-fix`` (check plus install every missing piece that has an unattended installer).  Stdlib only, so it runs even when no project dependency is installed. Every knob is overridable through the environment; module-level constants are the single source of truth for defaults.  Checks cover Python modules, system binaries (openssl, redis-server, tor, cloudflared, docker, node), the ``.env`` file, and TCP reachability of Redis and the Garage S3 endpoint. ``--fix`` installs Python dependencies from ``requirements.txt``, Debian packages via apt, the cloudflared binary from the official Cloudflare release, and the garage binary from the official release server. Anything that cannot be installed unattended is reported in plain English with the exact command to run or the instruction to contact the server administrator.", "id": "scripts/doctor.py", "kind": "module", "label": "doctor.py", "language": "py", "sha256": "96d20947772f6ebe", "symbol_count": 28, "symbols": [{"doc": "Outcome of one environment check with a repair hint.", "kind": "class", "line": 98, "name": "CheckResult", "signature": "class CheckResult"}, {"doc": "Accumulated check results with derived exit status.", "kind": "class", "line": 108, "name": "DoctorReport", "signature": "class DoctorReport"}, {"doc": "Parse a dotenv file into a dict without third-party imports.", "kind": "method", "line": 128, "name": "load_env_file", "signature": "def load_env_file(path)"}, {"doc": "Return process env overlaid with ``.env`` file values.", "kind": "method", "line": 147, "name": "effective_env", "signature": "def effective_env()"}, {"doc": "Verify the interpreter meets the minimum supported version.", "kind": "method", "line": 154, "name": "check_python", "signature": "def check_python(minimum)"}, {"doc": "Verify one Python module imports cleanly.", "kind": "method", "line": 170, "name": "check_module", "signature": "def check_module(name)"}, {"doc": "Verify one system binary resolves via PATH or an override path.", "kind": "method", "line": 186, "name": "check_binary", "signature": "def check_binary(name, env_override)"}, {"doc": "Verify the operator ``.env`` file exists.", "kind": "method", "line": 210, "name": "check_env_file", "signature": "def check_env_file()"}, {"doc": "Extract a TCP host and port from a Redis or HTTP(S) URL.", "kind": "method", "line": 223, "name": "parse_host_port", "signature": "def parse_host_port(uri, default_port)"}, {"doc": "Verify a TCP endpoint accepts connections.", "kind": "method", "line": 242, "name": "check_tcp", "signature": "def check_tcp(name, host, port, timeout)"}, {"doc": "Map the host CPU to a Cloudflare or Garage release architecture.", "kind": "method", "line": 261, "name": "debian_arch", "signature": "def debian_arch(deb)"}, {"doc": "Build the official cloudflared .deb URL for a version and arch.", "kind": "method", "line": 270, "name": "cloudflared_deb_url", "signature": "def cloudflared_deb_url(version, arch)"}, {"doc": "Build the official garage binary URL for a version and target.", "kind": "method", "line": 283, "name": "garage_bin_url", "signature": "def garage_bin_url(version, target)"}, {"doc": "Build an apt install command, prefixed with sudo outside root.", "kind": "method", "line": 288, "name": "apt_command", "signature": "def apt_command(packages)"}, {"doc": "Run one shell command and capture its outcome.", "kind": "method", "line": 298, "name": "run_command", "signature": "def run_command(cmd)"}, {"doc": "Fetch a URL with curl when present, else urllib.", "kind": "method", "line": 319, "name": "download_file", "signature": "def download_file(url, destination)"}, {"doc": "Set one KEY=value pair in ``.env``, preserving other lines.", "kind": "method", "line": 334, "name": "upsert_env", "signature": "def upsert_env(key, value, path)"}, {"doc": "Install project requirements with the running interpreter.", "kind": "method", "line": 352, "name": "fix_python_deps", "signature": "def fix_python_deps()"}, {"doc": "Install Debian system packages, using sudo outside root.", "kind": "method", "line": 360, "name": "fix_apt", "signature": "def fix_apt(packages)"}, {"doc": "Install the cloudflared binary into a user-writable bin directory.", "kind": "method", "line": 373, "name": "fix_cloudflared", "signature": "def fix_cloudflared(version, bin_dir)"}, {"doc": "Download the garage binary and verify it against its checksum.", "kind": "method", "line": 417, "name": "fix_garage", "signature": "def fix_garage(version, destination)"}, {"doc": "Run every check and return the aggregated report.", "kind": "method", "line": 449, "name": "collect_report", "signature": "def collect_report()"}, {"doc": "Render the report in plain English for operators.", "kind": "method", "line": 476, "name": "print_report", "signature": "def print_report(report)"}, {"doc": "Install every missing piece that has an unattended installer.", "kind": "method", "line": 493, "name": "apply_fixes", "signature": "def apply_fixes(report)"}, {"doc": "Entry point for ``make doctor`` and ``make doctor-fix``.", "kind": "method", "line": 530, "name": "main", "signature": "def main(argv)"}, {"doc": "Append one check result.", "kind": "method", "line": 113, "name": "add", "signature": "def add(self, result)"}, {"doc": "Return every failing check.", "kind": "method", "line": 118, "name": "failures", "signature": "def failures(self)"}, {"doc": "Return 0 when every check passes, 1 otherwise.", "kind": "method", "line": 123, "name": "exit_code", "signature": "def exit_code(self)"}]}, {"doc": "Operator email tooling for QuantumVault.  Three subcommands, all runnable from any Linux host or AWS VPS that has the project checked out and its configuration available (payload.json plus an optional .env):  python scripts/email_tool.py test-smtp you@example.com Send a real test message through the configured SMTP server to prove the transport works from this machine.  python scripts/email_tool.py link <username> Print the account-confirmation URL for a user without sending mail, so an operator can verify an account when SMTP is not yet set up.  python scripts/email_tool.py confirm <username> Mark a user's email as verified directly in the database.  Exit code is 0 on success and 1 on failure so the commands compose in scripts.", "id": "scripts/email_tool.py", "kind": "module", "label": "email_tool.py", "language": "py", "sha256": "1bc02bf7a93dff05", "symbol_count": 6, "symbols": [{"doc": "Build a minimal Flask app that only carries the mail configuration.\n\nIntentionally avoids the full application factory (object storage, Redis,\nsecurity headers) so this tool runs on a bare host with nothing but SMTP\nreachable.", "kind": "function", "line": 40, "name": "_build_mail_app", "signature": "def _build_mail_app(config)"}, {"doc": "Send a test email through the configured SMTP server.", "kind": "function", "line": 63, "name": "cmd_test_smtp", "signature": "def cmd_test_smtp(args)"}, {"doc": "Print the confirmation URL for a user without sending email.", "kind": "function", "line": 91, "name": "cmd_link", "signature": "def cmd_link(args)"}, {"doc": "Mark a user's email as verified directly in the database.", "kind": "function", "line": 114, "name": "cmd_confirm", "signature": "def cmd_confirm(args)"}, {"doc": "Construct the argument parser for the three subcommands.", "kind": "function", "line": 133, "name": "build_parser", "signature": "def build_parser()"}, {"doc": "Parse arguments and dispatch to the selected subcommand.", "kind": "function", "line": 153, "name": "main", "signature": "def main()"}]}, {"doc": "Bootstrap a fresh Garage deployment for QuantumVault.  What this does: 1. Waits for the admin API to respond. 2. Connects the local node to the cluster (single-node layout). 3. Creates the quantumvault bucket. 4. Creates a scoped API key with read+write on that bucket only. 5. Emits the credentials for .env (S3_ACCESS_KEY / S3_SECRET_KEY).  Usage: docker compose up -d garage scripts/garage-init.sh  The script reads GARAGE_RPC_SECRET and GARAGE_ADMIN_TOKEN from the .env file (or the environment) so the admin API can be authenticated.", "id": "scripts/garage-init.sh", "kind": "module", "label": "garage-init.sh", "language": "sh", "sha256": "6e9fe8a9d44648c8", "symbol_count": 1, "symbols": [{"doc": "Insert or update a KEY=value line in .env without disturbing other lines.", "kind": "function", "line": 35, "name": "upsert_env"}]}, {"doc": "Run Garage (S3-compatible object storage) natively, without Docker.  Idempotent: if the S3 API is already reachable on :3900 it does nothing. Otherwise it ensures a local garage binary exists (downloading a pinned release and verifying its checksum when necessary), writes a development config with project-local data directories under .run/garage, starts the server in the background, provisions the bucket and a scoped access key, and writes the resulting S3 credentials into .env so the app picks them up.  Override knobs via the environment: GARAGE_VERSION   release to download                 (default 1.0.1) GARAGE_BIN       path to (or destination for) garage (default .run/garage-bin/garage) GARAGE_SHA256    pin the binary checksum             (optional, recommended)  This script is invoked by `make garage-up`, which `make run` calls as a prerequisite when Docker is not available.", "id": "scripts/garage-native.sh", "kind": "module", "label": "garage-native.sh", "language": "sh", "sha256": "e4e0897859d0f948", "symbol_count": 3, "symbols": [{"doc": "Insert or update a KEY=value line in .env without disturbing other lines.", "kind": "function", "line": 46, "name": "upsert_env"}, {"kind": "function", "line": 56, "name": "s3_reachable"}, {"kind": "function", "line": 141, "name": "gcmd"}]}, {"doc": "Operator tooling to promote QuantumVault users to a privileged role.  Two subcommands, runnable from any Linux host that has the project checked out (no Flask app context required — talks to the SQLite DB directly):  python scripts/makeadmin.py <username> Promote <username> to 'superadmin'. Idempotent: re-running on an already-superadmin user is a no-op that still returns exit code 0.  python scripts/makeadmin.py <username> <role> Set <username>'s role to an arbitrary value from the allowed set (free, bronze, silver, gold, admin, superadmin). Use this for demotions, role audits, or seeding non-superadmin operators.  Exit code is 0 on success and 1 on failure so the commands compose in scripts. The DB path defaults to ``instance/users.db``; override with the ``QV_USERS_DB`` environment variable when running against a non-default deployment (e.g. a staging copy).  The script writes through ``UserDB.update_role`` (models/user.py) so the storage_quota and subscription_status side-effects match what the rest of the application does. It does NOT touch the KEM / SRP credentials — a promotion never invalidates a user's existing login.", "id": "scripts/makeadmin.py", "kind": "module", "label": "makeadmin.py", "language": "py", "sha256": "bf6eee53c78fd78b", "symbol_count": 5, "symbols": [{"doc": "Return the absolute users.db path, anchored at the project root.\n\nA bare ``instance/users.db`` only resolves when the script is run\nfrom the project root. Anchoring at ``_PROJECT_ROOT`` lets an operator\ninvoke it from anywhere (cron, CI, a different cwd) without surprises.", "kind": "function", "line": 51, "name": "_resolve_db_path", "signature": "def _resolve_db_path()"}, {"doc": "Print the post-update user record so the operator can eyeball it.", "kind": "function", "line": 64, "name": "_print_user_summary", "signature": "def _print_user_summary(user)"}, {"doc": "Promote ``args.username`` to the requested role (default: superadmin).", "kind": "function", "line": 75, "name": "cmd_promote", "signature": "def cmd_promote(args)"}, {"doc": "Construct the argument parser for the makeadmin subcommands.", "kind": "function", "line": 126, "name": "build_parser", "signature": "def build_parser()"}, {"doc": "Parse arguments and dispatch to the selected subcommand.", "kind": "function", "line": 152, "name": "main", "signature": "def main()"}]}, {"doc": "Bloque 1 test: superadmin_edit_user endpoint.  Renders the user-edit form via Flask's test client, then verifies GET (200) + POST (200) paths plus the role guard. The DB is backed up before the run and restored afterwards, so a failed test cannot leave dirty state.  Usage:  python3 scripts/test_bloque1.py", "id": "scripts/test_bloque1.py", "kind": "module", "label": "test_bloque1.py", "language": "py", "sha256": "7ecb72997b4f6e91", "symbol_count": 8, "symbols": [{"kind": "class", "line": 48, "name": "_FakeUser", "signature": "class _FakeUser"}, {"kind": "method", "line": 62, "name": "_load_user", "signature": "def _load_user(uid)"}, {"kind": "method", "line": 86, "name": "check", "signature": "def check(name, ok, detail)"}, {"kind": "method", "line": 49, "name": "__init__", "signature": "def __init__(self, row)"}, {"kind": "method", "line": 54, "name": "is_authenticated", "signature": "def is_authenticated(self)"}, {"kind": "method", "line": 56, "name": "is_active", "signature": "def is_active(self)"}, {"kind": "method", "line": 58, "name": "is_anonymous", "signature": "def is_anonymous(self)"}, {"kind": "method", "line": 59, "name": "get_id", "signature": "def get_id(self)"}]}, {"id": "server.go", "kind": "module", "label": "server.go", "language": "go", "sha256": "cd8b3decdbde4a81", "symbol_count": 2, "symbols": [{"kind": "function", "line": 11, "name": "main", "signature": "func main("}, {"kind": "function", "line": 40, "name": "handleConnection", "signature": "func handleConnection("}]}, {"id": "server.py", "kind": "module", "label": "server.py", "language": "py", "sha256": "f38a106bc85e3411", "symbol_count": 0, "symbols": []}, {"doc": "Account settings controller: secure notes (QV-DENIABLE-1).  Loaded as an external ES module to comply with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts. All container building and opening happens in qv-deniable.js, in the browser. The server returns and accepts an opaque container plus the non-secret structural parameters; it never sees a passphrase or any note text, and it never reports whether a second set of notes exists.", "id": "static/js/account.js", "kind": "module", "label": "account.js", "language": "js", "sha256": "7c7df5c7c360b936", "symbol_count": 9, "symbols": [{"kind": "function", "line": 19, "name": "setStatus"}, {"kind": "function", "line": 30, "name": "csrfToken"}, {"kind": "function", "line": 36, "name": "apiRequest"}, {"kind": "function", "line": 54, "name": "loadState"}, {"kind": "function", "line": 59, "name": "collectSlots"}, {"kind": "function", "line": 73, "name": "handleConfigure"}, {"kind": "function", "line": 103, "name": "handleOpen"}, {"kind": "function", "line": 125, "name": "handleReset"}, {"kind": "function", "line": 138, "name": "init"}]}, {"doc": "Decipher animation for elements tagged with the \"codedText\" class.  Extracted from an inline <script> so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts. The effect is purely cosmetic: if the GSAP animation library is not available it degrades gracefully and leaves the text untouched.", "id": "static/js/coded-text.js", "kind": "module", "label": "coded-text.js", "language": "js", "sha256": "104b45f91ee1d335", "symbol_count": 3, "symbols": [{"kind": "function", "line": 12, "name": "randomChar"}, {"kind": "function", "line": 18, "name": "animateElement"}, {"kind": "function", "line": 49, "name": "init"}]}, {"doc": "Login page controller (zero-knowledge SRP-6a flow).  Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts and inline event handlers. The password never leaves the browser: the SRP handshake exchanges only A (client public) and M1 (proof) and verifies the server proof M2.", "id": "static/js/login.js", "kind": "module", "label": "login.js", "language": "js", "sha256": "25ed813cf2cbd1bb", "symbol_count": 2, "symbols": [{"kind": "function", "line": 11, "name": "handleLogin"}, {"kind": "function", "line": 43, "name": "init"}]}, {"doc": "Messages page controller (zero-knowledge end-to-end messaging).  Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'). Sending encrypts the message to the recipient's hybrid public key in the browser; receiving decrypts the opaque envelopes locally after prompting for the password. Decrypted text is rendered with textContent (never innerHTML) so a malicious sender cannot inject HTML/script into the recipient's page.", "id": "static/js/messages.js", "kind": "module", "label": "messages.js", "language": "js", "sha256": "2677199463a17367", "symbol_count": 6, "symbols": [{"kind": "function", "line": 11, "name": "getCsrfToken"}, {"kind": "function", "line": 17, "name": "handleSend"}, {"kind": "function", "line": 43, "name": "collectEnvelopes"}, {"kind": "function", "line": 60, "name": "handleDecryptInbox"}, {"kind": "function", "line": 87, "name": "initEditor"}, {"kind": "function", "line": 108, "name": "init"}]}, {"doc": "QuantumVault zero-knowledge browser crypto.  Single source of truth for all client-side cryptography. The password and every private key are generated, used, and stored encrypted in the browser; only opaque ciphertext, the SRP salt/verifier, the public key, and the password-encrypted private key blob ever reach the server.  Primitives: - Authentication: SRP-6a (RFC 5054 2048-bit group, SHA-256), scheme \"QV-SRP-1\" mirroring utils/srp6a.py byte-for-byte. - Key wrapping: hybrid KEM = ML-KEM-768 (post-quantum) + X25519 (classical), combined via HKDF-SHA256, sealing keys with AES-256-GCM. - Size concealment: every message/file plaintext is padded to a fixed bucket (qv-padding.js, QV-PAD-1) before AES-GCM, so ciphertext lengths reveal only the bucket. Pad bytes are fresh crypto.getRandomValues per envelope and are never cached or reused. - Private-key protection: PBKDF2-SHA256 (600k iterations) derives the master key that encrypts the user's private key blob.  All cryptographic primitives are loaded from the local `vendor/` directory instead of a CDN. The vendored bundles are pinned to specific upstream versions, served as first-party static assets, and benefit from the same SRI / CSP protections as the rest of the application. The version comment on each import is the upstream package version that was vendored.  noble/hashes 1.8.0 — SHA-2, HKDF, utils, browser crypto provider", "id": "static/js/qv-crypto.js", "kind": "module", "label": "qv-crypto.js", "language": "js", "sha256": "9bbe0f3d5badac05", "symbol_count": 40, "symbols": [{"doc": "-- Encoding helpers ---", "kind": "function", "line": 58, "name": "concatBytes"}, {"kind": "function", "line": 69, "name": "hexToBytes"}, {"kind": "function", "line": 78, "name": "bytesToHex"}, {"kind": "function", "line": 84, "name": "bytesToBase64"}, {"kind": "function", "line": 95, "name": "bytesToBase32"}, {"kind": "function", "line": 113, "name": "base64ToBytes"}, {"kind": "function", "line": 120, "name": "bytesToBigInt"}, {"kind": "function", "line": 127, "name": "i2osp"}, {"kind": "function", "line": 137, "name": "mod"}, {"kind": "function", "line": 141, "name": "modPow"}, {"kind": "function", "line": 159, "name": "randomBytes"}, {"kind": "function", "line": 168, "name": "H"}, {"kind": "function", "line": 172, "name": "Hint"}, {"doc": "Derive a 256-bit key from a passphrase with a caller-chosen PBKDF2 iteration count. This is the single PBKDF2 implementation in the client; deriveMasterKey pins it to the account-password iteration count, while the deniable vault (qv-deniable.js) drives it with the server-advertised count so a policy change needs no client edit.", "kind": "function", "line": 184, "name": "deriveKeyFromPassphrase"}, {"kind": "function", "line": 205, "name": "deriveMasterKey"}, {"kind": "function", "line": 209, "name": "aesGcmEncrypt"}, {"kind": "function", "line": 220, "name": "aesGcmDecrypt"}, {"doc": "-- SRP-6a (QV-SRP-1), mirrors utils/srp6a.py ---", "kind": "function", "line": 250, "name": "computeK"}, {"kind": "function", "line": 255, "name": "deriveVerifier"}, {"doc": "Run a full SRP-6a login against the server, verifying the server proof M2.", "kind": "function", "line": 263, "name": "srpLogin"}, {"kind": "function", "line": 315, "name": "generateIdentity"}, {"kind": "function", "line": 343, "name": "parsePublicKey"}, {"kind": "function", "line": 351, "name": "parsePrivateBlob"}, {"kind": "function", "line": 359, "name": "deriveWrapKey"}, {"doc": "Seal a file encryption key to a recipient's hybrid public key.", "kind": "function", "line": 371, "name": "wrapKey"}, {"doc": "Recover a file encryption key using the recipient's hybrid private blob.", "kind": "function", "line": 395, "name": "unwrapKey"}, {"doc": "Generate a QV-RECOVERY-1 code: 20 random bytes (160 bits) Base32-encoded (RFC 4648, no padding) and grouped as XXXX-XXXX-... for readability.", "kind": "function", "line": 417, "name": "generateRecoveryCode"}, {"doc": "Normalize a user-entered recovery code: strip surrounding whitespace, remove group separators, and uppercase, so \"abcd-efgh\" and \"ABCDEFGH\"", "kind": "function", "line": 428, "name": "normalizeRecoveryCode"}, {"doc": "Re-wrap an existing privateBlob under a key derived from a recovery code, using the same PBKDF2-SHA256 + AES-256-GCM scheme as the password path, with its own independent salt.", "kind": "function", "line": 436, "name": "wrapPrivateKeyForRecovery"}, {"doc": "Reconstruct the public key (the same {v, mlkem, x} structure produced by generateIdentity) from a decrypted privateBlob. The noble ML-KEM-768 secretKey is encoded as [innerSK(1152) | publicKey(1184) | H(pk)(32) | z(32)], so the public key is recoverable directly; the X25519 public key is derived from its secret via x25519.getPublicKey. Used as a proof-of-possession when resetting credentials with a recovery code: the server accepts the reset only if this matches the stored public_key.", "kind": "function", "line": 455, "name": "derivePublicKeyFromPrivateBlob"}, {"kind": "function", "line": 473, "name": "postJson"}, {"doc": "Build the zero-knowledge registration payload entirely in the browser.  Returns `{ payload, recoveryCode }`: `payload` is the JSON body to POST to the registration endpoint (it includes the recovery-code-wrapped private key, but never the recovery code itself), and `recoveryCode` is the plaintext QV-RECOVERY-1 code to show the user exactly once. The server never sees `recoveryCode`.", "kind": "function", "line": 496, "name": "buildRegistration"}, {"kind": "function", "line": 530, "name": "register"}, {"doc": "Reset SRP credentials and the password-encrypted private key using a QV-RECOVERY-1 recovery code, without ever exposing the user's keypair to the server. Fetches the recovery-wrapped privateBlob, decrypts it locally with a key derived from the recovery code, proves possession of the resulting keypair by reconstructing its public key, and re-wraps the same privateBlob under the new password.", "kind": "function", "line": 541, "name": "recoverAccount"}, {"kind": "function", "line": 592, "name": "login"}, {"doc": "Generate a fresh file key, encrypt the padded file, wrap the key, and upload. The file plaintext is padded to a fixed file bucket before AES-GCM so the ciphertext length reveals only the bucket, not the exact file size.", "kind": "function", "line": 599, "name": "encryptAndUpload"}, {"doc": "Download an encrypted file and its key, then decrypt it in the browser.", "kind": "function", "line": 629, "name": "downloadAndDecrypt"}, {"doc": "Fetch a user's hybrid public key so the browser can wrap content to them.", "kind": "function", "line": 668, "name": "fetchPublicKey"}, {"doc": "Encrypt a message to a recipient (keeping a sender-readable outbox copy) and POST the opaque envelope. The plaintext and the CEK never leave the browser; the server stores only ciphertext and wrapped keys.", "kind": "function", "line": 683, "name": "sendSecureMessage"}, {"doc": "Decrypt a batch of inbox envelopes with the user's password. The master key and private blob are derived once and reused, so this stays cheap even for a full mailbox. Returns one result per envelope; a record that cannot be decrypted is reported with ``ok: false`` rather than aborting the batch.", "kind": "function", "line": 714, "name": "decryptInbox"}]}, {"doc": "QuantumVault deniable vault (QV-DENIABLE-1) browser crypto.  A deniable vault is an opaque container with a fixed number of slots. Each slot is independently encrypted under a key derived from its own passphrase; only the slot whose passphrase the user enters will authenticate and decrypt. The container is built and opened entirely in the browser. The server stores only the opaque envelope and never sees a passphrase or a plaintext.  Deniability rests on two invariants enforced here and re-checked on the server (controllers/deniable_vault.py):  1. Every container has exactly `slot_count` slots. A container that hides data is structurally identical to one that does not. 2. Every slot's plaintext is padded to the same length before encryption, so every slot's ciphertext is the same length. The byte sizes reveal nothing about which slot, if any, holds real data.  When the user configures no hidden vault, the hidden slot is filled with random bytes under a random, discarded key. It is then indistinguishable from a slot that holds real data the user is simply declining to open.", "id": "static/js/qv-deniable.js", "kind": "module", "label": "qv-deniable.js", "language": "js", "sha256": "bc4b1bd2e57dec56", "symbol_count": 7, "symbols": [{"kind": "function", "line": 47, "name": "toBytes"}, {"doc": "Frame a payload as [len(4) | payload | random padding] of exactly `paddedLength` bytes. `paddedLength` is shared by every slot so the", "kind": "function", "line": 55, "name": "frame"}, {"kind": "function", "line": 64, "name": "unframe"}, {"doc": "Encrypt one slot's framed plaintext under a passphrase, returning the {salt, nonce, ct} object the envelope stores.", "kind": "function", "line": 82, "name": "sealSlot"}, {"doc": "Attempt to open one slot with a passphrase. Returns the payload bytes on success or null when the passphrase does not authenticate this slot.", "kind": "function", "line": 102, "name": "openSlot"}, {"doc": "Build a deniable container from a list of slot specifications.  `slots` is an array of `{ passphrase, data }`; `data` may be a string or a Uint8Array. The array is padded out to `parameters.slot_count` entries with random, unopenable slots so the container always has the fixed slot count. Every slot's plaintext is padded to `parameters.slot_plaintext_bytes`, so every container is exactly the same size regardless of how much data it holds. Throws if more slots are supplied than allowed, or if any slot's data does not fit the fixed slot size.", "kind": "function", "line": 125, "name": "buildDeniableVault"}, {"doc": "Open a container with a passphrase. Tries every slot; only the slot whose passphrase matches will authenticate. Returns `{ index, data, text }` for the opened slot, or throws if no slot opens.", "kind": "function", "line": 170, "name": "openDeniableVault"}]}, {"doc": "QuantumVault fixed-bucket padding (QV-PAD-1), browser mirror of utils/padding.py.  Every plaintext is framed as [len(4 BE) | plaintext | fresh random pad] up to its bucket before AES-GCM. Buckets must stay identical to the server table: an envelope whose ciphertext length is not bucket+GCM overhead is rejected by the server. Pad bytes come from crypto.getRandomValues on every call and are never cached or reused; only the immutable bucket tables below are long-lived.", "id": "static/js/qv-padding.js", "kind": "module", "label": "qv-padding.js", "language": "js", "sha256": "014f123faa9014f0", "symbol_count": 5, "symbols": [{"kind": "function", "line": 15, "name": "tableFor"}, {"kind": "function", "line": 20, "name": "bucketFor"}, {"kind": "function", "line": 33, "name": "randomPad"}, {"kind": "function", "line": 42, "name": "padFramed"}, {"kind": "function", "line": 54, "name": "unframeFramed"}]}, {"doc": "Account recovery page controller (QV-RECOVERY-1 flow).  Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts and inline event handlers. recoverAccount() in qv-crypto.js fetches the account's recovery bundle, decrypts the private key blob entirely in the browser using a key derived from the recovery code, and re-wraps it under the new password. The recovery code and the new password never leave the browser.", "id": "static/js/recover.js", "kind": "module", "label": "recover.js", "language": "js", "sha256": "60cc13330293d771", "symbol_count": 3, "symbols": [{"kind": "function", "line": 14, "name": "setStatus"}, {"kind": "function", "line": 22, "name": "handleRecover"}, {"kind": "function", "line": 79, "name": "init"}]}, {"doc": "Registration page controller (zero-knowledge flow).  This module is loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts and inline event handlers. It reads the profile from the form, runs the browser-side crypto in qv-crypto.js, and POSTs only opaque zero-knowledge material to the server. The password and the private key never leave the browser.", "id": "static/js/register.js", "kind": "module", "label": "register.js", "language": "js", "sha256": "5fc4d15a655a5641", "symbol_count": 3, "symbols": [{"doc": "Display the one-time QV-RECOVERY-1 code in a modal and wait for the user to acknowledge they have saved it before continuing. The code is shown", "kind": "function", "line": 16, "name": "showRecoveryCode"}, {"kind": "function", "line": 42, "name": "handleRegister"}, {"kind": "function", "line": 109, "name": "init"}]}, {"doc": "Upload page controller (zero-knowledge file storage).  Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'). The browser derives a fresh file key, encrypts the file with AES-256-GCM, and wraps the key to the user's hybrid public key. Downloads are decrypted locally after prompting for the password. The server never sees plaintext, the file key, or the password.", "id": "static/js/upload.js", "kind": "module", "label": "upload.js", "language": "js", "sha256": "250c24e170e56ec6", "symbol_count": 6, "symbols": [{"kind": "function", "line": 11, "name": "getCsrfToken"}, {"kind": "function", "line": 16, "name": "getUsername"}, {"kind": "function", "line": 23, "name": "getPublicKey"}, {"kind": "function", "line": 40, "name": "handleUpload"}, {"kind": "function", "line": 74, "name": "handleDownload"}, {"kind": "function", "line": 96, "name": "init"}]}, {"id": "templates/terms.py", "kind": "module", "label": "terms.py", "language": "py", "sha256": "38dd208e64e063a0", "symbol_count": 1, "symbols": [{"doc": "Render the About page.", "kind": "function", "line": 6, "name": "terms", "signature": "def terms()"}]}, {"id": "test.sh", "kind": "module", "label": "test.sh", "language": "sh", "sha256": "2a5a4539c1bfb714", "symbol_count": 0, "symbols": []}, {"id": "tests/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "f813c53b4d1cc74f", "symbol_count": 0, "symbols": []}, {"doc": "Shared pytest fixtures for the QuantumVault test suite.  Builds the Flask app via :func:`app_factory.create_app` in a mode safe for automated tests: development settings (so a missing ``FLASK_SECRET_KEY`` does not abort startup), CSP/HTTPS-redirect disabled, an in-memory rate limiter, and a temporary SQLite database path so the suite never touches ``instance/users.db``.", "id": "tests/conftest.py", "kind": "module", "label": "conftest.py", "language": "py", "sha256": "7150d18802b39b73", "symbol_count": 8, "symbols": [{"doc": "Keep the suite hermetic against the operator's local ``.env`` file.\n\n``load_payload`` calls ``dotenv.load_dotenv()`` at app creation, which\nwould inject the developer's local ``QV_*`` values (often empty facade\nhashes) into ``os.environ`` and shadow the explicit mappings under\ntest. Neutralizing the loader makes every test run against the\nmappings it declares, matching CI where no ``.env`` exists.", "kind": "function", "line": 26, "name": "_hermetic_env", "signature": "def _hermetic_env(monkeypatch)"}, {"doc": "Neutralize pytest-flask's autouse request-context push.\n\npytest-flask installs an autouse ``_push_request_context`` fixture that\nkeeps an application/request context pushed for the whole test. That\nambient context makes Flask-Login's ``current_user`` proxy and\n``client.session_transaction`` resolve against a stale context, so a\ntest that authenticates a second user on the same client still observes\nthe first user's data. This suite drives the app exclusively through the\n``client`` fixture, which manages its own per-request context, so the\nambient push is both unnecessary and a correctness hazard. Overriding\nthe plugin fixture by name (conftest takes precedence over installed\nplugins) replaces it with a no-op.", "kind": "function", "line": 58, "name": "_push_request_context", "signature": "def _push_request_context()"}, {"doc": "Return a QuantumVault Flask app configured for testing.", "kind": "function", "line": 76, "name": "app", "signature": "def app(tmp_path)"}, {"doc": "Return a Flask test client for the test app.", "kind": "function", "line": 101, "name": "client", "signature": "def client(app)"}, {"doc": "Collect emitted log messages in a list for assertions.", "kind": "class", "line": 106, "name": "_ListLogHandler", "signature": "class _ListLogHandler(Handler)"}, {"doc": "Yield a list that is appended with each ``audit_event`` JSON line.\n\nThe audit logger has ``propagate = False`` (by design, so it never\nmixes into the application log), so ``caplog`` cannot see it. This\nfixture attaches a temporary handler directly to the audit logger\ninstead.", "kind": "method", "line": 118, "name": "audit_records", "signature": "def audit_records()"}, {"kind": "method", "line": 109, "name": "__init__", "signature": "def __init__(self)"}, {"kind": "method", "line": 113, "name": "emit", "signature": "def emit(self, record)"}]}, {"doc": "Behaviour contract: the decoy site requires a deniable passphrase.  When the cover facade is enabled, the account page must ask for a deniable (second) passphrase and mark the field required. The server exposes only the instance-level facade flag; it never learns whether a passphrase is set.", "id": "tests/test_account_facade.py", "kind": "module", "label": "test_account_facade.py", "language": "py", "sha256": "5eecd463dda5c24d", "symbol_count": 6, "symbols": [{"kind": "function", "line": 23, "name": "fast_hasher", "signature": "def fast_hasher()"}, {"kind": "function", "line": 27, "name": "_make_user", "signature": "def _make_user(db_path, username)"}, {"kind": "function", "line": 55, "name": "_authenticated_client", "signature": "def _authenticated_client(application, db_path)"}, {"kind": "function", "line": 65, "name": "_build", "signature": "def _build(tmp_path, fast_hasher)"}, {"kind": "function", "line": 88, "name": "test_facade_enabled_requires_a_deniable_passphrase", "signature": "def test_facade_enabled_requires_a_deniable_passphrase(tmp_path, fast_hasher)"}, {"kind": "function", "line": 99, "name": "test_facade_disabled_keeps_it_optional", "signature": "def test_facade_disabled_keeps_it_optional(tmp_path, fast_hasher)"}]}, {"doc": "Regression tests for the phone-verification page and resend route.  The verify-phone template links its \"Resend Verification Code\" button to ``auth.resend_phone_verification``. Before that endpoint existed, simply rendering the page raised a Jinja ``BuildError`` (HTTP 500). These tests pin both the render and the endpoint registration.  The resend POST itself is not invoked here: like every auth route it constructs an ``AuthController``, which opens a Redis-backed SRP session store, and the test environment has no Redis (``STORAGE_URI=memory://``). Confirming the endpoint is registered is enough to prove the template's ``url_for`` resolves, which is the bug under test.", "id": "tests/test_auth_phone.py", "kind": "module", "label": "test_auth_phone.py", "language": "py", "sha256": "47a6a04c7303d5fd", "symbol_count": 3, "symbols": [{"doc": "GET /verify_phone must render without a url_for BuildError.", "kind": "function", "line": 18, "name": "test_verify_phone_page_renders", "signature": "def test_verify_phone_page_renders(client)"}, {"doc": "The resend endpoint the template links to must exist.", "kind": "function", "line": 25, "name": "test_resend_endpoint_is_registered", "signature": "def test_resend_endpoint_is_registered(app)"}, {"doc": "The resend endpoint is POST-only so a GET cannot trigger an SMS.", "kind": "function", "line": 31, "name": "test_resend_route_accepts_only_post", "signature": "def test_resend_route_accepts_only_post(app)"}]}, {"doc": "Specification tests for the QV-FACADE-2 configurable cover templates.  Behaviour is specified per collaborator (catalog, sanitizer, renderer, custom store, service) and end-to-end through the HTTP cover flow, so a regression in any layer fails a focused test rather than only the surface.", "id": "tests/test_cover.py", "kind": "module", "label": "test_cover.py", "language": "py", "sha256": "b6bc09bcb5a2a60a", "symbol_count": 52, "symbols": [{"kind": "function", "line": 42, "name": "fast_hasher", "signature": "def fast_hasher()"}, {"kind": "function", "line": 47, "name": "renderer", "signature": "def renderer()"}, {"kind": "function", "line": 52, "name": "store", "signature": "def store(tmp_path, renderer)"}, {"kind": "function", "line": 56, "name": "_facade_overrides", "signature": "def _facade_overrides(fast_hasher)"}, {"kind": "function", "line": 68, "name": "_client", "signature": "def _client(tmp_path, fast_hasher)"}, {"kind": "class", "line": 83, "name": "TestCatalog", "signature": "class TestCatalog"}, {"kind": "class", "line": 103, "name": "TestSanitizer", "signature": "class TestSanitizer"}, {"kind": "class", "line": 158, "name": "TestRenderer", "signature": "class TestRenderer"}, {"kind": "class", "line": 189, "name": "TestCustomStore", "signature": "class TestCustomStore"}, {"kind": "class", "line": 244, "name": "TestCoverService", "signature": "class TestCoverService"}, {"kind": "class", "line": 280, "name": "TestCoverHttp", "signature": "class TestCoverHttp"}, {"kind": "method", "line": 84, "name": "test_catalog_ships_five_distinct_templates", "signature": "def test_catalog_ships_five_distinct_templates(self)"}, {"kind": "method", "line": 89, "name": "test_default_template_exists", "signature": "def test_default_template_exists(self)"}, {"kind": "method", "line": 92, "name": "test_every_template_validates_and_renders", "signature": "def test_every_template_validates_and_renders(self, renderer)"}, {"kind": "method", "line": 104, "name": "test_empty_payload_fills_defaults", "signature": "def test_empty_payload_fills_defaults(self)"}, {"kind": "method", "line": 109, "name": "test_unknown_variable_is_rejected", "signature": "def test_unknown_variable_is_rejected(self)"}, {"kind": "method", "line": 113, "name": "test_invalid_email_is_rejected", "signature": "def test_invalid_email_is_rejected(self)"}, {"kind": "method", "line": 117, "name": "test_control_characters_are_stripped", "signature": "def test_control_characters_are_stripped(self)"}, {"kind": "method", "line": 121, "name": "test_overlong_value_is_rejected", "signature": "def test_overlong_value_is_rejected(self)"}, {"kind": "method", "line": 125, "name": "test_multiline_body_preserves_line_breaks", "signature": "def test_multiline_body_preserves_line_breaks(self)"}, {"kind": "method", "line": 129, "name": "test_single_line_value_flattens_line_breaks", "signature": "def test_single_line_value_flattens_line_breaks(self)"}, {"kind": "method", "line": 137, "name": "test_multiline_flag_matches_spec", "signature": "def test_multiline_flag_matches_spec(self, spec)"}, {"kind": "method", "line": 144, "name": "test_text_boundary_is_inclusive", "signature": "def test_text_boundary_is_inclusive(self)"}, {"kind": "method", "line": 150, "name": "test_email_boundary_is_inclusive", "signature": "def test_email_boundary_is_inclusive(self)"}, {"kind": "method", "line": 159, "name": "test_variables_are_autoescaped", "signature": "def test_variables_are_autoescaped(self, renderer)"}, {"kind": "method", "line": 164, "name": "test_unknown_variable_is_rejected", "signature": "def test_unknown_variable_is_rejected(self, renderer)"}, {"kind": "method", "line": 168, "name": "test_dunder_access_is_rejected", "signature": "def test_dunder_access_is_rejected(self, renderer)"}, {"kind": "method", "line": 172, "name": "test_inline_script_is_rejected", "signature": "def test_inline_script_is_rejected(self, renderer)"}, {"kind": "method", "line": 176, "name": "test_external_form_action_is_rejected", "signature": "def test_external_form_action_is_rejected(self, renderer)"}, {"kind": "method", "line": 180, "name": "test_template_import_is_rejected", "signature": "def test_template_import_is_rejected(self, renderer)"}, {"kind": "method", "line": 184, "name": "test_blank_source_is_rejected", "signature": "def test_blank_source_is_rejected(self, renderer)"}, {"kind": "method", "line": 190, "name": "test_valid_template_round_trips", "signature": "def test_valid_template_round_trips(self, store)"}, {"kind": "method", "line": 196, "name": "test_bad_extension_is_rejected", "signature": "def test_bad_extension_is_rejected(self, store)"}, {"kind": "method", "line": 200, "name": "test_oversize_template_is_rejected", "signature": "def test_oversize_template_is_rejected(self, store)"}, {"kind": "method", "line": 204, "name": "test_path_traversal_is_neutralized", "signature": "def test_path_traversal_is_neutralized(self, store)"}, {"kind": "method", "line": 209, "name": "test_script_template_is_rejected", "signature": "def test_script_template_is_rejected(self, store)"}, {"kind": "method", "line": 213, "name": "test_missing_template_raises", "signature": "def test_missing_template_raises(self, store)"}, {"kind": "method", "line": 217, "name": "test_non_bytes_payload_is_rejected", "signature": "def test_non_bytes_payload_is_rejected(self, store)"}, {"kind": "method", "line": 221, "name": "test_disallowed_character_filename_is_rejected", "signature": "def test_disallowed_character_filename_is_rejected(self, store)"}, {"kind": "method", "line": 225, "name": "test_exactly_max_size_is_accepted", "signature": "def test_exactly_max_size_is_accepted(self, store)"}, {"kind": "method", "line": 229, "name": "test_nested_directory_is_created", "signature": "def test_nested_directory_is_created(self, tmp_path, renderer)"}, {"kind": "method", "line": 233, "name": "test_two_templates_share_the_store", "signature": "def test_two_templates_share_the_store(self, store)"}, {"kind": "method", "line": 238, "name": "test_directory_with_allowed_suffix_is_ignored", "signature": "def test_directory_with_allowed_suffix_is_ignored(self, store)"}, {"kind": "method", "line": 245, "name": "test_selects_a_builtin_template", "signature": "def test_selects_a_builtin_template(self, renderer, store)"}, {"kind": "method", "line": 250, "name": "test_unknown_template_falls_back_to_default", "signature": "def test_unknown_template_falls_back_to_default(self, renderer, store)"}, {"kind": "method", "line": 255, "name": "test_missing_custom_template_falls_back_to_default", "signature": "def test_missing_custom_template_falls_back_to_default(self, renderer, store)"}, {"kind": "method", "line": 260, "name": "test_custom_template_is_rendered", "signature": "def test_custom_template_is_rendered(self, renderer, store)"}, {"kind": "method", "line": 267, "name": "test_builtin_selection_ignores_a_custom_name", "signature": "def test_builtin_selection_ignores_a_custom_name(self, renderer, store)"}, {"kind": "method", "line": 274, "name": "test_custom_selection_renders_the_custom_marker", "signature": "def test_custom_selection_renders_the_custom_marker(self, renderer, store)"}, {"kind": "method", "line": 281, "name": "test_default_cover_selects_search_portal", "signature": "def test_default_cover_selects_search_portal(self, tmp_path, fast_hasher)"}, {"kind": "method", "line": 287, "name": "test_configured_template_is_served", "signature": "def test_configured_template_is_served(self, tmp_path, fast_hasher)"}, {"kind": "method", "line": 298, "name": "test_gate_still_works_with_configured_template", "signature": "def test_gate_still_works_with_configured_template(self, tmp_path, fast_hasher)"}]}, {"doc": "Specification tests for the QV-DENIABLE-1 deniable vault feature.  The feature is split across layers, each tested in isolation and then end-to-end through the account HTTP API:  * :class:`controllers.deniable_vault.DeniableVaultConfig` and :class:`controllers.deniable_vault.EnvelopeValidator` enforce the structural invariants that make a stored container indistinguishable to the (zero-knowledge) server: an exact slot count and a fixed-length slot ciphertext. The server validates *structure only*; it never decrypts. * :class:`controllers.deniable_vault.DeniableVaultConfig.random_container` lets the server mint a well-formed, unopenable container so that every account has one. \"Has a container\" is therefore universal and reveals nothing about whether a hidden vault exists. * :class:`models.deniable_vault.DeniableVaultDB` stores the opaque envelope verbatim, one row per user. * :class:`controllers.deniable_vault.DeniableVaultController` provisions, validates, persists, and emits generic audit events that name neither the feature nor the contents. * The ``account`` blueprint exposes the settings page and the ``GET/PUT/DELETE /api/account/vault`` endpoints, gated by authentication, CSRF, and rate limiting.", "id": "tests/test_deniable_vault.py", "kind": "module", "label": "test_deniable_vault.py", "language": "py", "sha256": "46e83b6a99584b93", "symbol_count": 55, "symbols": [{"doc": "Return the default deniable-vault configuration.", "kind": "function", "line": 50, "name": "config", "signature": "def config()"}, {"doc": "Return a validator bound to the default configuration.", "kind": "function", "line": 56, "name": "validator", "signature": "def validator(config)"}, {"doc": "Return a base64 ciphertext string of the given (or expected) length.", "kind": "function", "line": 61, "name": "_ciphertext", "signature": "def _ciphertext(config, length)"}, {"doc": "Build a structurally valid envelope for ``config``.\n\nEvery slot carries a ciphertext of the fixed expected length so the\nfixed-size invariant holds. The contents are zero bytes; the validator\nnever inspects plaintext, only structure.", "kind": "function", "line": 71, "name": "_valid_envelope", "signature": "def _valid_envelope(config)"}, {"doc": "Create a minimal user row in the test database and return it.", "kind": "function", "line": 91, "name": "_make_user", "signature": "def _make_user(app, username, role)"}, {"doc": "Create and authenticate a user on ``client``'s session.", "kind": "function", "line": 120, "name": "_login", "signature": "def _login(client, app, username, role)"}, {"doc": "Fetch a CSRF token bound to the client's session.", "kind": "function", "line": 130, "name": "_csrf", "signature": "def _csrf(client)"}, {"kind": "class", "line": 140, "name": "TestDeniableVaultConfig", "signature": "class TestDeniableVaultConfig"}, {"kind": "class", "line": 185, "name": "TestEnvelopeValidator", "signature": "class TestEnvelopeValidator"}, {"kind": "class", "line": 272, "name": "TestRandomContainer", "signature": "class TestRandomContainer"}, {"kind": "class", "line": 293, "name": "TestDeniableVaultDB", "signature": "class TestDeniableVaultDB"}, {"kind": "class", "line": 325, "name": "TestDeniableVaultController", "signature": "class TestDeniableVaultController"}, {"kind": "class", "line": 390, "name": "TestDeniableVaultApi", "signature": "class TestDeniableVaultApi"}, {"kind": "method", "line": 141, "name": "test_defaults_are_self_consistent", "signature": "def test_defaults_are_self_consistent(self)"}, {"kind": "method", "line": 150, "name": "test_expected_ct_length_matches_base64_formula", "signature": "def test_expected_ct_length_matches_base64_formula(self, config)"}, {"kind": "method", "line": 154, "name": "test_mapping_overrides_defaults", "signature": "def test_mapping_overrides_defaults(self)"}, {"kind": "method", "line": 161, "name": "test_environment_overrides_mapping", "signature": "def test_environment_overrides_mapping(self, monkeypatch)"}, {"kind": "method", "line": 166, "name": "test_allowed_kdf_csv_is_parsed", "signature": "def test_allowed_kdf_csv_is_parsed(self, monkeypatch)"}, {"kind": "method", "line": 172, "name": "test_public_parameters_round_trip_to_json", "signature": "def test_public_parameters_round_trip_to_json(self, config)"}, {"kind": "method", "line": 186, "name": "test_accepts_a_well_formed_envelope", "signature": "def test_accepts_a_well_formed_envelope(self, validator, config)"}, {"kind": "method", "line": 189, "name": "test_rejects_non_dict", "signature": "def test_rejects_non_dict(self, validator)"}, {"kind": "method", "line": 194, "name": "test_rejects_wrong_schema_version", "signature": "def test_rejects_wrong_schema_version(self, validator, config)"}, {"kind": "method", "line": 200, "name": "test_rejects_unknown_kdf", "signature": "def test_rejects_unknown_kdf(self, validator, config)"}, {"kind": "method", "line": 206, "name": "test_rejects_iterations_below_minimum", "signature": "def test_rejects_iterations_below_minimum(self, validator, config)"}, {"kind": "method", "line": 212, "name": "test_rejects_iterations_above_maximum", "signature": "def test_rejects_iterations_above_maximum(self, validator, config)"}, {"kind": "method", "line": 218, "name": "test_rejects_wrong_slot_count", "signature": "def test_rejects_wrong_slot_count(self, validator, config)"}, {"kind": "method", "line": 224, "name": "test_rejects_bad_salt_length", "signature": "def test_rejects_bad_salt_length(self, validator, config)"}, {"kind": "method", "line": 230, "name": "test_rejects_non_hex_salt", "signature": "def test_rejects_non_hex_salt(self, validator, config)"}, {"kind": "method", "line": 236, "name": "test_rejects_bad_nonce_length", "signature": "def test_rejects_bad_nonce_length(self, validator, config)"}, {"kind": "method", "line": 242, "name": "test_rejects_ciphertext_of_wrong_length", "signature": "def test_rejects_ciphertext_of_wrong_length(self, validator, config)"}, {"kind": "method", "line": 248, "name": "test_rejects_unequal_slot_ciphertext_lengths", "signature": "def test_rejects_unequal_slot_ciphertext_lengths(self, validator, config)"}, {"kind": "method", "line": 254, "name": "test_rejects_invalid_base64_ciphertext", "signature": "def test_rejects_invalid_base64_ciphertext(self, validator, config)"}, {"kind": "method", "line": 260, "name": "test_rejects_missing_slot_keys", "signature": "def test_rejects_missing_slot_keys(self, validator, config)"}, {"kind": "method", "line": 273, "name": "test_random_container_passes_validation", "signature": "def test_random_container_passes_validation(self, config, validator)"}, {"kind": "method", "line": 276, "name": "test_random_containers_differ", "signature": "def test_random_containers_differ(self, config)"}, {"kind": "method", "line": 281, "name": "test_random_container_has_fixed_shape", "signature": "def test_random_container_has_fixed_shape(self, config)"}, {"kind": "method", "line": 294, "name": "test_upsert_then_get_round_trips_verbatim", "signature": "def test_upsert_then_get_round_trips_verbatim(self, tmp_path)"}, {"kind": "method", "line": 303, "name": "test_upsert_replaces_existing_row", "signature": "def test_upsert_replaces_existing_row(self, tmp_path)"}, {"kind": "method", "line": 309, "name": "test_get_missing_returns_none", "signature": "def test_get_missing_returns_none(self, tmp_path)"}, {"kind": "method", "line": 313, "name": "test_exists", "signature": "def test_exists(self, tmp_path)"}, {"kind": "method", "line": 326, "name": "_controller", "signature": "def _controller(self, tmp_path)"}, {"kind": "method", "line": 331, "name": "test_load_or_provision_mints_when_absent", "signature": "def test_load_or_provision_mints_when_absent(self, app, tmp_path)"}, {"kind": "method", "line": 339, "name": "test_load_or_provision_is_stable", "signature": "def test_load_or_provision_is_stable(self, app, tmp_path)"}, {"kind": "method", "line": 346, "name": "test_save_then_load_round_trips", "signature": "def test_save_then_load_round_trips(self, app, tmp_path)"}, {"kind": "method", "line": 354, "name": "test_save_rejects_invalid_envelope", "signature": "def test_save_rejects_invalid_envelope(self, app, tmp_path)"}, {"kind": "method", "line": 363, "name": "test_reset_replaces_with_a_valid_random_container", "signature": "def test_reset_replaces_with_a_valid_random_container(self, app, tmp_path)"}, {"kind": "method", "line": 373, "name": "test_audit_is_generic_and_never_contains_ciphertext", "signature": "def test_audit_is_generic_and_never_contains_ciphertext(self, app, tmp_path, audit_records)"}, {"kind": "method", "line": 391, "name": "test_settings_page_requires_authentication", "signature": "def test_settings_page_requires_authentication(self, client)"}, {"kind": "method", "line": 395, "name": "test_get_api_requires_authentication", "signature": "def test_get_api_requires_authentication(self, client)"}, {"kind": "method", "line": 399, "name": "test_settings_page_renders_for_authenticated_user", "signature": "def test_settings_page_renders_for_authenticated_user(self, client, app)"}, {"kind": "method", "line": 406, "name": "test_get_always_returns_an_envelope_and_parameters", "signature": "def test_get_always_returns_an_envelope_and_parameters(self, client, app)"}, {"kind": "method", "line": 414, "name": "test_put_without_csrf_is_rejected", "signature": "def test_put_without_csrf_is_rejected(self, client, app)"}, {"kind": "method", "line": 422, "name": "test_put_get_reset_round_trip", "signature": "def test_put_get_reset_round_trip(self, client, app)"}, {"kind": "method", "line": 447, "name": "test_put_rejects_malformed_envelope", "signature": "def test_put_rejects_malformed_envelope(self, client, app)"}, {"kind": "method", "line": 461, "name": "test_vault_is_scoped_to_the_authenticated_user", "signature": "def test_vault_is_scoped_to_the_authenticated_user(self, client, app)"}]}, {"doc": "Behaviour contracts for scripts/doctor.py.  Covers binary and module checks, host/port parsing, release URL builders, apt command construction, and report exit status. No test touches the network, sudo, or package managers.", "id": "tests/test_doctor.py", "kind": "module", "label": "test_doctor.py", "language": "py", "sha256": "e051e55d5ce5a612", "symbol_count": 12, "symbols": [{"doc": "A binary on PATH reports ok with its resolved path.", "kind": "function", "line": 23, "name": "test_check_binary_finds_present_binary", "signature": "def test_check_binary_finds_present_binary()"}, {"doc": "An unknown binary fails and points at doctor-fix in English.", "kind": "function", "line": 30, "name": "test_check_binary_flags_missing_binary", "signature": "def test_check_binary_flags_missing_binary()"}, {"doc": "Absolute override paths resolve without trusting PATH.", "kind": "function", "line": 38, "name": "test_check_binary_honors_absolute_override", "signature": "def test_check_binary_honors_absolute_override(tmp_path)"}, {"doc": "Present stdlib modules pass, unknown ones fail with a remedy.", "kind": "function", "line": 48, "name": "test_check_module_reports_status", "signature": "def test_check_module_reports_status()"}, {"doc": "The running interpreter satisfies its own minimum version.", "kind": "function", "line": 56, "name": "test_check_python_accepts_current_runtime", "signature": "def test_check_python_accepts_current_runtime()"}, {"doc": "Redis and HTTP URLs reduce to host plus port.", "kind": "function", "line": 62, "name": "test_parse_host_port_shapes", "signature": "def test_parse_host_port_shapes()"}, {"doc": "A closed loopback port fails with operator guidance.", "kind": "function", "line": 83, "name": "test_check_tcp_refused_reports_remedy", "signature": "def test_check_tcp_refused_reports_remedy()"}, {"doc": "Release URLs follow the official vendor layouts.", "kind": "function", "line": 90, "name": "test_release_url_builders", "signature": "def test_release_url_builders()"}, {"doc": "Apt installs escalate with sudo unless already root.", "kind": "function", "line": 105, "name": "test_apt_command_uses_sudo_outside_root", "signature": "def test_apt_command_uses_sudo_outside_root()"}, {"doc": "An empty failure set exits zero, any failure exits one.", "kind": "function", "line": 115, "name": "test_report_exit_code_reflects_failures", "signature": "def test_report_exit_code_reflects_failures()"}, {"doc": "Comment and blank lines are skipped, quotes are stripped.", "kind": "function", "line": 129, "name": "test_load_env_file_parses_assignments", "signature": "def test_load_env_file_parses_assignments(tmp_path)"}, {"doc": "Existing keys are replaced in place, new keys are appended.", "kind": "function", "line": 140, "name": "test_upsert_env_replaces_and_appends", "signature": "def test_upsert_env_replaces_and_appends(tmp_path)"}]}, {"doc": "Specification tests for the QV-FACADE-1 cover facade and two-step gate.  The feature is specified behaviorally (given/when/then) and tested in isolation per collaborator, then end-to-end through the HTTP cover flow:  * :class:`controllers.facade.FacadeConfig` resolves every knob from the environment, then ``app.config``, then a code default, and never carries a gate phrase in the repository. * :class:`controllers.facade.GatePhraseHasher` hashes and verifies a gate phrase with Argon2id, so a low-entropy phrase resists offline attack if the config leaks. * :class:`controllers.facade.GateTicket` mints and verifies a short-lived signed ticket keyed by the app secret; expiry, tampering, and a wrong key all verify to ``None``. * :class:`controllers.facade.FacadeGate` classifies a submitted phrase as a miss, the real phrase, or the duress phrase, and emits a single generic audit event that reveals neither the outcome nor the phrase. * The ``facade`` blueprint conceals the app: anonymous visitors see the cover on the protected pages, a correct phrase reveals the ordinary login, an authenticated user bypasses the cover, and a disabled facade changes nothing.", "id": "tests/test_facade.py", "kind": "module", "label": "test_facade.py", "language": "py", "sha256": "eeccd8bd539d0f60", "symbol_count": 52, "symbols": [{"doc": "Return an Argon2id hasher with cheap parameters for fast tests.\n\nArgon2 embeds its cost parameters in the encoded hash, so verification is\nindependent of the verifying hasher's own settings; a cheap hasher can\ntherefore produce fixtures without weakening what production verifies.", "kind": "function", "line": 54, "name": "fast_hasher", "signature": "def fast_hasher()"}, {"doc": "Return an enabled facade config with real and duress phrases set.", "kind": "function", "line": 67, "name": "gate_config", "signature": "def gate_config(fast_hasher)"}, {"doc": "Return ``create_app`` config overrides that enable the facade.", "kind": "function", "line": 78, "name": "_facade_overrides", "signature": "def _facade_overrides(fast_hasher)"}, {"doc": "Return a test client for an app with the facade enabled.", "kind": "function", "line": 93, "name": "facade_client", "signature": "def facade_client(tmp_path, fast_hasher)"}, {"doc": "Create a minimal user row in the given database and return it.", "kind": "function", "line": 109, "name": "_make_user", "signature": "def _make_user(app_or_path, username)"}, {"doc": "Fetch a CSRF token bound to the client's session.", "kind": "function", "line": 138, "name": "_csrf", "signature": "def _csrf(client)"}, {"kind": "class", "line": 148, "name": "TestFacadeConfig", "signature": "class TestFacadeConfig"}, {"kind": "class", "line": 209, "name": "TestGatePhraseHasher", "signature": "class TestGatePhraseHasher"}, {"kind": "class", "line": 250, "name": "TestGateTicket", "signature": "class TestGateTicket"}, {"kind": "class", "line": 288, "name": "TestFacadeGate", "signature": "class TestFacadeGate"}, {"kind": "class", "line": 396, "name": "TestFacadeHttp", "signature": "class TestFacadeHttp"}, {"kind": "method", "line": 149, "name": "test_defaults_keep_the_facade_off", "signature": "def test_defaults_keep_the_facade_off(self)"}, {"kind": "method", "line": 154, "name": "test_defaults_keep_duress_alert_off", "signature": "def test_defaults_keep_duress_alert_off(self)"}, {"kind": "method", "line": 157, "name": "test_defaults_are_self_consistent", "signature": "def test_defaults_are_self_consistent(self)"}, {"kind": "method", "line": 165, "name": "test_mapping_overrides_defaults", "signature": "def test_mapping_overrides_defaults(self)"}, {"kind": "method", "line": 172, "name": "test_environment_overrides_mapping", "signature": "def test_environment_overrides_mapping(self, monkeypatch)"}, {"kind": "method", "line": 177, "name": "test_protected_paths_csv_is_parsed", "signature": "def test_protected_paths_csv_is_parsed(self)"}, {"kind": "method", "line": 183, "name": "test_gate_configured_requires_enabled_and_a_hash", "signature": "def test_gate_configured_requires_enabled_and_a_hash(self)"}, {"kind": "method", "line": 194, "name": "test_cover_context_is_cosmetic_and_json_serializable", "signature": "def test_cover_context_is_cosmetic_and_json_serializable(self)"}, {"kind": "method", "line": 210, "name": "test_hash_then_verify_accepts_the_phrase", "signature": "def test_hash_then_verify_accepts_the_phrase(self, fast_hasher)"}, {"kind": "method", "line": 214, "name": "test_verify_rejects_a_wrong_phrase", "signature": "def test_verify_rejects_a_wrong_phrase(self, fast_hasher)"}, {"kind": "method", "line": 218, "name": "test_hash_is_salted_so_two_hashes_differ", "signature": "def test_hash_is_salted_so_two_hashes_differ(self, fast_hasher)"}, {"kind": "method", "line": 221, "name": "test_verify_rejects_an_empty_stored_hash", "signature": "def test_verify_rejects_an_empty_stored_hash(self, fast_hasher)"}, {"kind": "method", "line": 224, "name": "test_verify_rejects_a_malformed_stored_hash", "signature": "def test_verify_rejects_a_malformed_stored_hash(self, fast_hasher)"}, {"kind": "method", "line": 227, "name": "test_verify_rejects_a_non_string_stored_hash", "signature": "def test_verify_rejects_a_non_string_stored_hash(self, fast_hasher)"}, {"kind": "method", "line": 231, "name": "test_from_config_builds_a_working_hasher", "signature": "def test_from_config_builds_a_working_hasher(self)"}, {"kind": "method", "line": 251, "name": "test_issue_then_verify_round_trips_the_mode", "signature": "def test_issue_then_verify_round_trips_the_mode(self)"}, {"kind": "method", "line": 256, "name": "test_issue_rejects_an_unknown_mode", "signature": "def test_issue_rejects_an_unknown_mode(self)"}, {"kind": "method", "line": 261, "name": "test_verify_rejects_an_expired_ticket", "signature": "def test_verify_rejects_an_expired_ticket(self)"}, {"kind": "method", "line": 267, "name": "test_verify_rejects_a_ticket_signed_with_another_key", "signature": "def test_verify_rejects_a_ticket_signed_with_another_key(self)"}, {"kind": "method", "line": 272, "name": "test_verify_rejects_garbage_and_none", "signature": "def test_verify_rejects_garbage_and_none(self)"}, {"kind": "method", "line": 277, "name": "test_verify_rejects_a_non_string_token", "signature": "def test_verify_rejects_a_non_string_token(self)"}, {"kind": "method", "line": 289, "name": "_gate", "signature": "def _gate(self, config)"}, {"kind": "method", "line": 292, "name": "test_real_phrase_yields_a_real_ticket", "signature": "def test_real_phrase_yields_a_real_ticket(self, app, gate_config)"}, {"kind": "method", "line": 300, "name": "test_duress_phrase_yields_a_duress_ticket", "signature": "def test_duress_phrase_yields_a_duress_ticket(self, app, gate_config)"}, {"kind": "method", "line": 307, "name": "test_wrong_phrase_is_a_miss_with_no_ticket", "signature": "def test_wrong_phrase_is_a_miss_with_no_ticket(self, app, gate_config)"}, {"kind": "method", "line": 314, "name": "test_miss_without_a_duress_hash", "signature": "def test_miss_without_a_duress_hash(self, app, fast_hasher)"}, {"kind": "method", "line": 325, "name": "test_minimum_length_phrase_is_accepted", "signature": "def test_minimum_length_phrase_is_accepted(self, app, fast_hasher)"}, {"kind": "method", "line": 337, "name": "test_maximum_length_phrase_is_accepted", "signature": "def test_maximum_length_phrase_is_accepted(self, app, fast_hasher)"}, {"kind": "method", "line": 349, "name": "test_too_short_phrase_is_a_miss", "signature": "def test_too_short_phrase_is_a_miss(self, app, gate_config)"}, {"kind": "method", "line": 355, "name": "test_too_long_phrase_is_a_miss", "signature": "def test_too_long_phrase_is_a_miss(self, app, gate_config)"}, {"kind": "method", "line": 361, "name": "test_audit_is_generic_and_never_contains_the_phrase", "signature": "def test_audit_is_generic_and_never_contains_the_phrase(self, app, gate_config, audit_records)"}, {"kind": "method", "line": 372, "name": "test_duress_alert_is_opt_in_and_generically_named", "signature": "def test_duress_alert_is_opt_in_and_generically_named(self, app, fast_hasher, audit_records)"}, {"kind": "method", "line": 397, "name": "test_anonymous_login_page_is_replaced_by_the_cover", "signature": "def test_anonymous_login_page_is_replaced_by_the_cover(self, facade_client)"}, {"kind": "method", "line": 403, "name": "test_anonymous_root_is_replaced_by_the_cover", "signature": "def test_anonymous_root_is_replaced_by_the_cover(self, facade_client)"}, {"kind": "method", "line": 409, "name": "test_wrong_phrase_keeps_the_cover_and_does_not_redirect", "signature": "def test_wrong_phrase_keeps_the_cover_and_does_not_redirect(self, facade_client)"}, {"kind": "method", "line": 417, "name": "test_real_phrase_reveals_the_login", "signature": "def test_real_phrase_reveals_the_login(self, facade_client)"}, {"kind": "method", "line": 432, "name": "test_duress_phrase_marks_the_session", "signature": "def test_duress_phrase_marks_the_session(self, facade_client)"}, {"kind": "method", "line": 441, "name": "test_authenticated_user_bypasses_the_cover", "signature": "def test_authenticated_user_bypasses_the_cover(self, tmp_path, fast_hasher)"}, {"kind": "method", "line": 465, "name": "test_gate_endpoint_is_absent_when_facade_disabled", "signature": "def test_gate_endpoint_is_absent_when_facade_disabled(self, client)"}, {"kind": "method", "line": 469, "name": "test_disabled_facade_serves_the_real_login", "signature": "def test_disabled_facade_serves_the_real_login(self, client)"}, {"kind": "method", "line": 474, "name": "test_enabled_without_a_hash_fails_open_to_the_real_app", "signature": "def test_enabled_without_a_hash_fails_open_to_the_real_app(self, tmp_path)"}]}, {"doc": "Contract tests for SRI pins and reproducible builds (QV-SRI-1).", "id": "tests/test_integrity.py", "kind": "module", "label": "test_integrity.py", "language": "py", "sha256": "64986712b63a5759", "symbol_count": 6, "symbols": [{"kind": "function", "line": 19, "name": "test_compute_sri_format", "signature": "def test_compute_sri_format()"}, {"kind": "function", "line": 25, "name": "test_manifest_exists_and_pins_crypto", "signature": "def test_manifest_exists_and_pins_crypto()"}, {"kind": "function", "line": 37, "name": "test_manifest_hashes_match_files", "signature": "def test_manifest_hashes_match_files()"}, {"kind": "function", "line": 44, "name": "test_template_integrity_resolves_both_forms", "signature": "def test_template_integrity_resolves_both_forms()"}, {"kind": "function", "line": 51, "name": "test_jinja_global_registered", "signature": "def test_jinja_global_registered(app)"}, {"kind": "function", "line": 55, "name": "test_verify_build_passes_on_clean_tree", "signature": "def test_verify_build_passes_on_clean_tree()"}]}, {"doc": "Contract tests for fixed-bucket padding (QV-PAD-1) and its enforcement.", "id": "tests/test_padding.py", "kind": "module", "label": "test_padding.py", "language": "py", "sha256": "32785b4e369268ed", "symbol_count": 24, "symbols": [{"kind": "function", "line": 26, "name": "test_pad_roundtrip_message_sizes", "signature": "def test_pad_roundtrip_message_sizes()"}, {"kind": "function", "line": 33, "name": "test_pad_roundtrip_file_kind", "signature": "def test_pad_roundtrip_file_kind()"}, {"kind": "function", "line": 38, "name": "test_bucket_boundaries", "signature": "def test_bucket_boundaries()"}, {"kind": "function", "line": 44, "name": "test_pad_output_length_is_bucketed", "signature": "def test_pad_output_length_is_bucketed()"}, {"kind": "function", "line": 49, "name": "test_pad_uses_fresh_randomness", "signature": "def test_pad_uses_fresh_randomness()"}, {"kind": "function", "line": 56, "name": "test_pad_rejects_oversize", "signature": "def test_pad_rejects_oversize()"}, {"kind": "function", "line": 61, "name": "test_unpad_rejects_non_bucket_length", "signature": "def test_unpad_rejects_non_bucket_length()"}, {"kind": "function", "line": 66, "name": "test_unpad_rejects_corrupt_prefix", "signature": "def test_unpad_rejects_corrupt_prefix()"}, {"kind": "function", "line": 74, "name": "test_unpad_rejects_wrong_kind", "signature": "def test_unpad_rejects_wrong_kind()"}, {"kind": "function", "line": 80, "name": "test_wire_lengths", "signature": "def test_wire_lengths()"}, {"kind": "function", "line": 87, "name": "test_config_from_env_override", "signature": "def test_config_from_env_override(monkeypatch)"}, {"kind": "function", "line": 94, "name": "test_config_from_env_falls_back_on_garbage", "signature": "def test_config_from_env_falls_back_on_garbage(monkeypatch)"}, {"kind": "function", "line": 99, "name": "test_cache_holds_tables_not_pad_bytes", "signature": "def test_cache_holds_tables_not_pad_bytes()"}, {"kind": "function", "line": 105, "name": "test_message_controller_rejects_unpadded_envelope", "signature": "def test_message_controller_rejects_unpadded_envelope(app, tmp_path, monkeypatch)"}, {"kind": "function", "line": 113, "name": "test_message_controller_rejects_malformed_base64", "signature": "def test_message_controller_rejects_malformed_base64(app, tmp_path, monkeypatch)"}, {"kind": "function", "line": 120, "name": "test_message_controller_accepts_bucketed_envelope", "signature": "def test_message_controller_accepts_bucketed_envelope(app, tmp_path, monkeypatch)"}, {"kind": "class", "line": 128, "name": "_FakeS3", "signature": "class _FakeS3"}, {"kind": "class", "line": 136, "name": "_FakeUpload", "signature": "class _FakeUpload"}, {"kind": "method", "line": 146, "name": "test_file_controller_rejects_unpadded_upload", "signature": "def test_file_controller_rejects_unpadded_upload(app)"}, {"kind": "method", "line": 152, "name": "test_file_controller_accepts_bucketed_upload", "signature": "def test_file_controller_accepts_bucketed_upload(app)"}, {"kind": "method", "line": 129, "name": "__init__", "signature": "def __init__(self)"}, {"kind": "method", "line": 132, "name": "put_object", "signature": "def put_object(self, Bucket, Key, Body)"}, {"kind": "method", "line": 139, "name": "__init__", "signature": "def __init__(self, body)"}, {"kind": "method", "line": 142, "name": "read", "signature": "def read(self)"}]}, {"doc": "Behaviour contracts for QV-TUNNEL disposable secure channels.  Covers SecureChannelConfig resolution, URL validation, manager lifecycle with injected process launcher, atomic state redaction in audit details, and superadmin HTTP gating.", "id": "tests/test_secure_channel.py", "kind": "module", "label": "test_secure_channel.py", "language": "py", "sha256": "5a9ee958054bc320", "symbol_count": 67, "symbols": [{"doc": "Unconfigured environment resolves to a disabled channel.", "kind": "function", "line": 30, "name": "test_config_defaults_to_disabled_without_binaries", "signature": "def test_config_defaults_to_disabled_without_binaries()"}, {"doc": "Mode and local port resolve from environment with bounds.", "kind": "function", "line": 37, "name": "test_config_reads_mode_and_port_from_env", "signature": "def test_config_reads_mode_and_port_from_env()"}, {"doc": "Ports outside 1..65535 fall back to the default.", "kind": "function", "line": 47, "name": "test_config_rejects_out_of_range_port", "signature": "def test_config_rejects_out_of_range_port()"}, {"doc": "Validators accept quick-tunnel and v3 onion shapes only.", "kind": "function", "line": 55, "name": "test_url_validators_accept_only_expected_shapes", "signature": "def test_url_validators_accept_only_expected_shapes()"}, {"doc": "Start launches both backends and persists redacted state.", "kind": "function", "line": 64, "name": "test_manager_starts_hybrid_with_injected_launcher", "signature": "def test_manager_starts_hybrid_with_injected_launcher(tmp_path)"}, {"doc": "Disabled mode cannot be started explicitly.", "kind": "function", "line": 90, "name": "test_manager_rejects_invalid_mode", "signature": "def test_manager_rejects_invalid_mode(tmp_path)"}, {"doc": "Stop kills tracked pids and removes persisted state.", "kind": "function", "line": 101, "name": "test_manager_stop_clears_state_with_killer", "signature": "def test_manager_stop_clears_state_with_killer(tmp_path)"}, {"doc": "Audit helper redacts full URLs to mode plus fingerprint.", "kind": "function", "line": 122, "name": "test_audit_details_never_carry_urls", "signature": "def test_audit_details_never_carry_urls()"}, {"doc": "Anonymous POST to channel endpoints redirects to login.", "kind": "function", "line": 133, "name": "test_superadmin_channel_routes_require_superadmin", "signature": "def test_superadmin_channel_routes_require_superadmin(client)"}, {"doc": "Repository env template exposes every channel key.", "kind": "function", "line": 139, "name": "test_env_template_documents_channel_keys", "signature": "def test_env_template_documents_channel_keys()"}, {"doc": "Persisted state is owner-only.", "kind": "function", "line": 153, "name": "test_channel_state_file_permissions", "signature": "def test_channel_state_file_permissions(tmp_path)"}, {"doc": "Non-string values never validate as backend addresses.", "kind": "function", "line": 164, "name": "test_validators_reject_non_string_inputs", "signature": "def test_validators_reject_non_string_inputs()"}, {"doc": "TCP port coercion honors 1 and 65535 as valid edges.", "kind": "function", "line": 175, "name": "test_port_boundaries_accept_edges_and_reject_outside", "signature": "def test_port_boundaries_accept_edges_and_reject_outside()"}, {"doc": "Empty or whitespace binary and dir values resolve to defaults.", "kind": "function", "line": 186, "name": "test_config_blank_values_fall_back_to_defaults", "signature": "def test_config_blank_values_fall_back_to_defaults()"}, {"doc": "Explicit binary and dir values survive resolution.", "kind": "function", "line": 203, "name": "test_config_explicit_values_are_preserved", "signature": "def test_config_explicit_values_are_preserved()"}, {"doc": "Environment takes precedence over the mapping for every key.", "kind": "function", "line": 219, "name": "test_config_env_beats_mapping", "signature": "def test_config_env_beats_mapping()"}, {"doc": "Ephemeral defaults True and either backend alone counts as active.", "kind": "function", "line": 229, "name": "test_channel_status_defaults_and_single_side_active", "signature": "def test_channel_status_defaults_and_single_side_active()"}, {"doc": "Launcher spawns detached daemons with piped stdio.", "kind": "function", "line": 254, "name": "test_default_launcher_detaches_process", "signature": "def test_default_launcher_detaches_process(monkeypatch)"}, {"doc": "Zero and negative pids never reach os.kill.", "kind": "function", "line": 276, "name": "test_default_killer_ignores_non_positive_pid", "signature": "def test_default_killer_ignores_non_positive_pid(monkeypatch)"}, {"doc": "Group kill failure falls back to plain kill before giving up.", "kind": "function", "line": 286, "name": "test_default_killer_falls_back_to_kill", "signature": "def test_default_killer_falls_back_to_kill(monkeypatch)"}, {"doc": "Blank constructor binaries resolve to shipped defaults.", "kind": "function", "line": 302, "name": "test_manager_init_blank_binaries_fall_back", "signature": "def test_manager_init_blank_binaries_fall_back()"}, {"doc": "Rotate with no persisted channel raises instead of crashing.", "kind": "function", "line": 311, "name": "test_rotate_without_state_raises", "signature": "def test_rotate_without_state_raises(tmp_path)"}, {"doc": "Rotate on a disabled record raises instead of starting.", "kind": "function", "line": 322, "name": "test_rotate_disabled_state_raises", "signature": "def test_rotate_disabled_state_raises(tmp_path)"}, {"doc": "Empty action and absent urls still yield a safe detail string.", "kind": "function", "line": 334, "name": "test_audit_details_default_verb_and_empty_urls", "signature": "def test_audit_details_default_verb_and_empty_urls()"}, {"doc": "Pid zero and negatives never survive status construction.", "kind": "function", "line": 348, "name": "test_status_for_drops_non_positive_pids", "signature": "def test_status_for_drops_non_positive_pids()"}, {"doc": "Corrupt pid entries in state are filtered, valid ones kept.", "kind": "function", "line": 357, "name": "test_read_state_filters_bad_pids", "signature": "def test_read_state_filters_bad_pids(tmp_path)"}, {"doc": "Persisted payload is deterministic JSON with ephemeral set.", "kind": "function", "line": 378, "name": "test_write_state_is_sorted_and_ephemeral", "signature": "def test_write_state_is_sorted_and_ephemeral(tmp_path)"}, {"doc": "Repeated writes into an existing directory never raise.", "kind": "function", "line": 397, "name": "test_write_state_twice_in_existing_dir", "signature": "def test_write_state_twice_in_existing_dir(tmp_path)"}, {"doc": "Nested state directories are created recursively.", "kind": "function", "line": 408, "name": "test_write_state_creates_nested_dirs", "signature": "def test_write_state_creates_nested_dirs(tmp_path)"}, {"doc": "Backend start creates nested state dirs recursively.", "kind": "function", "line": 416, "name": "test_start_creates_nested_state_dirs", "signature": "def test_start_creates_nested_state_dirs(tmp_path)"}, {"doc": "Tor-only start creates nested state dirs without prior backend.", "kind": "function", "line": 442, "name": "test_start_tor_only_creates_nested_state_dirs", "signature": "def test_start_tor_only_creates_nested_state_dirs(tmp_path)"}, {"doc": "Unremovable scratch dirs never break stop.", "kind": "function", "line": 463, "name": "test_cleanup_scratch_suppresses_rmtree_errors", "signature": "def test_cleanup_scratch_suppresses_rmtree_errors(tmp_path, monkeypatch)"}, {"doc": "Default launcher resolves bare names through PATH only.", "kind": "function", "line": 480, "name": "test_resolve_binary_with_default_launcher_requires_path", "signature": "def test_resolve_binary_with_default_launcher_requires_path(tmp_path)"}, {"doc": "Injected launchers accept bare names without PATH lookup.", "kind": "function", "line": 497, "name": "test_resolve_binary_with_injected_launcher_skips_which", "signature": "def test_resolve_binary_with_injected_launcher_skips_which(tmp_path)"}, {"doc": "Absolute candidates are accepted only when the file exists.", "kind": "function", "line": 511, "name": "test_resolve_binary_absolute_path_must_exist", "signature": "def test_resolve_binary_absolute_path_must_exist(tmp_path)"}, {"doc": "Pid liveness distinguishes dead, forbidden, broken, and live.", "kind": "function", "line": 527, "name": "test_pid_live_branches", "signature": "def test_pid_live_branches(monkeypatch, tmp_path)"}, {"doc": "Bare hostnames gain a scheme while full urls pass through.", "kind": "function", "line": 555, "name": "test_normalize_onion_shapes", "signature": "def test_normalize_onion_shapes()"}, {"doc": "Pattern and file waiters poll until timeout or content.", "kind": "function", "line": 564, "name": "test_wait_helpers_respect_deadline_and_content", "signature": "def test_wait_helpers_respect_deadline_and_content(tmp_path, monkeypatch)"}, {"doc": "Polling still checks content at the exact deadline instant.", "kind": "function", "line": 597, "name": "test_wait_helpers_include_deadline_instant", "signature": "def test_wait_helpers_include_deadline_instant(tmp_path, monkeypatch)"}, {"doc": "Diagnostics resolve absolute paths and flag missing bare names.", "kind": "function", "line": 636, "name": "test_channel_diagnostics_reports_availability", "signature": "def test_channel_diagnostics_reports_availability(tmp_path)"}, {"doc": "Absolute candidates that do not exist report as missing.", "kind": "function", "line": 656, "name": "test_channel_diagnostics_missing_absolute_path", "signature": "def test_channel_diagnostics_missing_absolute_path(tmp_path)"}, {"doc": "Log tail surfaces backend output and stays empty when absent.", "kind": "function", "line": 671, "name": "test_read_log_tail_returns_trailing_lines", "signature": "def test_read_log_tail_returns_trailing_lines(tmp_path)"}, {"doc": "Channel panel avoids low-contrast muted text and shows diagnostics.", "kind": "function", "line": 685, "name": "test_superadmin_channel_section_is_readable", "signature": "def test_superadmin_channel_section_is_readable()"}, {"doc": "Only http and https survive scheme coercion.", "kind": "function", "line": 696, "name": "test_origin_scheme_parsing", "signature": "def test_origin_scheme_parsing()"}, {"doc": "Origin scheme resolves from env with a safe fallback.", "kind": "function", "line": 706, "name": "test_config_reads_origin_scheme", "signature": "def test_config_reads_origin_scheme()"}, {"doc": "Origin URL always targets loopback with the configured scheme.", "kind": "function", "line": 719, "name": "test_origin_url_points_at_loopback", "signature": "def test_origin_url_points_at_loopback()"}, {"doc": "Plain origins skip TLS flags, https origins verify nothing.", "kind": "function", "line": 733, "name": "test_cloudflared_cmd_matches_origin_scheme", "signature": "def test_cloudflared_cmd_matches_origin_scheme(tmp_path)"}, {"doc": "Unreachable object storage reports down without raising.", "kind": "function", "line": 763, "name": "test_s3_probe_skips_dead_endpoint", "signature": "def test_s3_probe_skips_dead_endpoint(app)"}, {"doc": "A listening socket reports the endpoint as reachable.", "kind": "function", "line": 771, "name": "test_s3_probe_detects_live_endpoint", "signature": "def test_s3_probe_detects_live_endpoint(app)"}, {"kind": "function", "line": 67, "name": "fake_launcher", "signature": "def fake_launcher(cmd, log_path)"}, {"kind": "function", "line": 105, "name": "fake_launcher", "signature": "def fake_launcher(cmd, log_path)"}, {"kind": "class", "line": 260, "name": "_FakeProcess", "signature": "class _FakeProcess"}, {"kind": "method", "line": 263, "name": "_fake_popen", "signature": "def _fake_popen(cmd)"}, {"kind": "method", "line": 290, "name": "_raise_pg", "signature": "def _raise_pg(pid, sig)"}, {"kind": "method", "line": 293, "name": "_record_kill", "signature": "def _record_kill(pid, sig)"}, {"kind": "method", "line": 419, "name": "fake_launcher", "signature": "def fake_launcher(cmd, log_path)"}, {"kind": "method", "line": 445, "name": "fake_launcher", "signature": "def fake_launcher(cmd, log_path)"}, {"kind": "method", "line": 471, "name": "_raise", "signature": "def _raise()"}, {"kind": "method", "line": 536, "name": "_raise_lookup", "signature": "def _raise_lookup(pid, sig)"}, {"kind": "method", "line": 542, "name": "_raise_perm", "signature": "def _raise_perm(pid, sig)"}, {"kind": "method", "line": 548, "name": "_raise_os", "signature": "def _raise_os(pid, sig)"}, {"kind": "method", "line": 573, "name": "_fake_mono", "signature": "def _fake_mono()"}, {"kind": "method", "line": 576, "name": "_fake_sleep", "signature": "def _fake_sleep(secs)"}, {"kind": "method", "line": 606, "name": "_fake_mono", "signature": "def _fake_mono()"}, {"kind": "method", "line": 609, "name": "_fake_sleep", "signature": "def _fake_sleep(secs)"}, {"kind": "method", "line": 627, "name": "_fake_sleep_file", "signature": "def _fake_sleep_file(secs)"}, {"kind": "method", "line": 737, "name": "fake_launcher", "signature": "def fake_launcher(cmd, log_path)"}]}, {"doc": "Tests for utils/security.py: audit log redaction and JSON CSRF protection.", "id": "tests/test_security.py", "kind": "module", "label": "test_security.py", "language": "py", "sha256": "6cd17b97dfc59216", "symbol_count": 8, "symbols": [{"kind": "function", "line": 12, "name": "test_audit_event_includes_ip_and_ua_by_default", "signature": "def test_audit_event_includes_ip_and_ua_by_default(app, audit_records, monkeypatch)"}, {"kind": "function", "line": 29, "name": "test_audit_event_redacts_ip_and_ua_when_disabled", "signature": "def test_audit_event_redacts_ip_and_ua_when_disabled(app, audit_records, monkeypatch)"}, {"kind": "function", "line": 45, "name": "test_json_csrf_protect_rejects_missing_token", "signature": "def test_json_csrf_protect_rejects_missing_token(app)"}, {"kind": "function", "line": 57, "name": "test_json_csrf_protect_accepts_valid_header_token", "signature": "def test_json_csrf_protect_accepts_valid_header_token(app)"}, {"kind": "function", "line": 77, "name": "test_json_csrf_protect_passes_get_through_without_token", "signature": "def test_json_csrf_protect_passes_get_through_without_token(app)"}, {"kind": "function", "line": 47, "name": "view", "signature": "def view()"}, {"kind": "function", "line": 59, "name": "view", "signature": "def view()"}, {"kind": "function", "line": 79, "name": "view", "signature": "def view()"}]}, {"doc": "Pure-Python SRP-6a (QV-SRP-1) roundtrip test.  Mirrors the client-side math in ``static/js/qv-crypto.js`` (``deriveVerifier`` and ``srpLogin``) using only :mod:`utils.srp6a`, so this test exercises the exact server primitives without needing Redis, Flask, or a browser.", "id": "tests/test_srp.py", "kind": "module", "label": "test_srp.py", "language": "py", "sha256": "5209dd5c47dd4e2a", "symbol_count": 6, "symbols": [{"kind": "function", "line": 16, "name": "_h", "signature": "def _h()"}, {"kind": "function", "line": 23, "name": "_hint", "signature": "def _hint()"}, {"doc": "Mirror ``deriveVerifier`` in qv-crypto.js: v = g^x mod N.", "kind": "function", "line": 27, "name": "_client_derive_verifier", "signature": "def _client_derive_verifier(username, password, salt_hex)"}, {"doc": "Mirror ``srpLogin`` in qv-crypto.js: derive M1 and the expected M2.", "kind": "function", "line": 34, "name": "_client_compute_proof", "signature": "def _client_compute_proof(username, password, salt_hex, server_a_secret, server_a, server_b)"}, {"kind": "function", "line": 74, "name": "test_srp6a_full_roundtrip_matches_server_proofs", "signature": "def test_srp6a_full_roundtrip_matches_server_proofs()"}, {"kind": "function", "line": 104, "name": "test_srp6a_wrong_password_produces_mismatched_proof", "signature": "def test_srp6a_wrong_password_produces_mismatched_proof()"}]}, {"doc": "Contract tests for shared utility helpers.", "id": "tests/test_utils.py", "kind": "module", "label": "test_utils.py", "language": "py", "sha256": "f3dcd1fa7caba28a", "symbol_count": 3, "symbols": [{"kind": "function", "line": 8, "name": "test_database_path_prefers_the_configured_path", "signature": "def test_database_path_prefers_the_configured_path(app)"}, {"kind": "function", "line": 13, "name": "test_database_path_honors_env_outside_a_context", "signature": "def test_database_path_honors_env_outside_a_context(monkeypatch)"}, {"kind": "function", "line": 18, "name": "test_database_path_default_outside_a_context", "signature": "def test_database_path_default_outside_a_context(monkeypatch)"}]}, {"doc": "Generate the SRI manifest for first-party assets and pinned CDN URLs.  Regenerating the manifest is the audited step that binds served bytes to served hashes. The output is deterministic: keys are sorted, the JSON uses a fixed indent, and the file ends with a single newline, so two runs over identical inputs produce byte-identical output.  Usage: ./.venv/bin/python tools/generate_sri.py ./.venv/bin/python tools/generate_sri.py --check", "id": "tools/generate_sri.py", "kind": "module", "label": "generate_sri.py", "language": "py", "sha256": "924a4eefe5e7646e", "symbol_count": 5, "symbols": [{"doc": "Hash every first-party script and stylesheet under ``static/``.", "kind": "function", "line": 41, "name": "collect_local_assets", "signature": "def collect_local_assets()"}, {"doc": "Download every pinned CDN URL and hash its exact bytes.", "kind": "function", "line": 56, "name": "fetch_cdn_assets", "signature": "def fetch_cdn_assets()"}, {"doc": "Assemble the deterministic manifest document.", "kind": "function", "line": 66, "name": "build_manifest", "signature": "def build_manifest(cdn, local)"}, {"doc": "Render the manifest deterministically with a trailing newline.", "kind": "function", "line": 76, "name": "render_manifest", "signature": "def render_manifest(manifest)"}, {"doc": "Generate the manifest, or verify it is current with ``--check``.", "kind": "function", "line": 81, "name": "main", "signature": "def main(argv)"}]}, {"doc": "Mutation testing harness for the QuantumVault facade and cover contracts.  Each discovered token mutation is applied in place, the test suite is run, and the mutation is classified as killed (tests fail) or survived (tests pass). A survivor indicates a gap in the tests and yields a non-zero exit status. The harness runs the suite with ``-B`` and purges bytecode caches so a restored source is always reloaded rather than served from a stale ``.pyc`` compiled from a mutant.", "id": "tools/mutation_test.py", "kind": "module", "label": "mutation_test.py", "language": "py", "sha256": "cf6e936a6b84c2c5", "symbol_count": 8, "symbols": [{"doc": "A single token replacement and where it lives.", "kind": "class", "line": 56, "name": "Mutation", "signature": "class Mutation"}, {"kind": "method", "line": 67, "name": "_is_equivalent_bool", "signature": "def _is_equivalent_bool(tokens, index)"}, {"doc": "Return every token-level mutation the harness can apply to a module.", "kind": "method", "line": 79, "name": "discover_mutations", "signature": "def discover_mutations(path, source)"}, {"doc": "Return source with one token replaced at its exact position.", "kind": "method", "line": 109, "name": "apply_mutation", "signature": "def apply_mutation(source, mutation)"}, {"doc": "Gather mutations across targets up to a global cap.", "kind": "method", "line": 121, "name": "collect", "signature": "def collect(targets, limit)"}, {"doc": "Remove compiled caches so restored sources are always reloaded.", "kind": "method", "line": 133, "name": "purge_bytecode", "signature": "def purge_bytecode()"}, {"doc": "Return whether the test suite passed.", "kind": "method", "line": 142, "name": "run_suite", "signature": "def run_suite(python, tests)"}, {"doc": "Run the mutation campaign and report killed versus survived mutants.", "kind": "method", "line": 157, "name": "main", "signature": "def main(argv)"}]}, {"doc": "Verify reproducible builds and the fixed code contracts (QV-SRI-1).  Checks performed, all offline:  1. Every first-party asset in ``static/sri_manifest.json`` recomputes to its pinned hash. A mismatch means the served bytes drifted from the audited bytes. 2. Every ``/static/...`` script or stylesheet referenced by any template carries an ``integrity`` attribute equal to the manifest value. 3. Every ``https://`` script or stylesheet referenced by any template carries an ``integrity`` attribute equal to the manifest CDN pin. 4. The JavaScript bucket tables in ``static/js/qv-padding.js`` equal the Python defaults in ``utils/padding.py``, so the two sides of the padding contract cannot drift apart silently.  Usage: ./.venv/bin/python tools/verify_build.py", "id": "tools/verify_build.py", "kind": "module", "label": "verify_build.py", "language": "py", "sha256": "c94845edad6f82bc", "symbol_count": 11, "symbols": [{"doc": "Collect external script and stylesheet references from one template.", "kind": "class", "line": 34, "name": "AssetReference", "signature": "class AssetReference(HTMLParser)"}, {"doc": "Resolve a ``url_for('static', ...)`` expression to its served path.", "kind": "method", "line": 60, "name": "_normalize_reference", "signature": "def _normalize_reference(ref)"}, {"doc": "Load and return the SRI manifest document.", "kind": "method", "line": 71, "name": "load_manifest", "signature": "def load_manifest()"}, {"doc": "Resolve the pinned integrity value for one template reference.", "kind": "method", "line": 76, "name": "expected_for_reference", "signature": "def expected_for_reference(manifest, ref)"}, {"doc": "Accept a literal pin or the ``sri_integrity`` template expression.", "kind": "method", "line": 85, "name": "integrity_attribute_ok", "signature": "def integrity_attribute_ok(integrity, ref, expected)"}, {"doc": "Recompute every pinned local asset and record mismatches.", "kind": "method", "line": 95, "name": "check_local_hashes", "signature": "def check_local_hashes(manifest, failures)"}, {"doc": "Require manifest-backed integrity on every template reference.", "kind": "method", "line": 110, "name": "check_template_references", "signature": "def check_template_references(manifest, failures)"}, {"doc": "Require identical bucket tables in Python and JavaScript.", "kind": "method", "line": 126, "name": "check_bucket_parity", "signature": "def check_bucket_parity(failures)"}, {"doc": "Run every check and report failures.", "kind": "method", "line": 141, "name": "main", "signature": "def main()"}, {"doc": "Initialize the reference collector.", "kind": "method", "line": 37, "name": "__init__", "signature": "def __init__(self)"}, {"doc": "Record one script or link tag with its integrity attribute.", "kind": "method", "line": 42, "name": "handle_starttag", "signature": "def handle_starttag(self, tag, attrs)"}]}, {"id": "utils/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "b9a6a0a8280963d8", "symbol_count": 0, "symbols": []}, {"doc": "/home/grisun0/src/postcuantum/v1/utils/cache.py", "id": "utils/cache.py", "kind": "module", "label": "cache.py", "language": "py", "sha256": "f889d007721d93ba", "symbol_count": 5, "symbols": [{"doc": "Redis-based caching layer.", "kind": "class", "line": 6, "name": "Cache", "signature": "class Cache"}, {"kind": "method", "line": 8, "name": "__init__", "signature": "def __init__(self)"}, {"doc": "Retrieve a value from the cache.", "kind": "method", "line": 11, "name": "get", "signature": "def get(self, key)"}, {"doc": "Store a value in the cache with an optional TTL (seconds).", "kind": "method", "line": 16, "name": "set", "signature": "def set(self, key, value, ttl)"}, {"doc": "Delete a key from the cache.", "kind": "method", "line": 20, "name": "delete", "signature": "def delete(self, key)"}]}, {"doc": "Subresource Integrity manifest helpers (QV-SRI-1).  The manifest at ``static/sri_manifest.json`` pins the exact bytes of every first-party script and stylesheet plus every pinned CDN URL. It is generated with ``tools/generate_sri.py`` and checked with ``tools/verify_build.py``. Templates read values through :func:`integrity_for` so the served HTML always carries the hash of the audited bytes, and a compromised static file or a swapped CDN payload fails closed in the browser instead of executing.", "id": "utils/integrity.py", "kind": "module", "label": "integrity.py", "language": "py", "sha256": "5100c185cdb52222", "symbol_count": 8, "symbols": [{"doc": "Return the manifest path resolved from this file, never hardcoded.", "kind": "function", "line": 25, "name": "manifest_path", "signature": "def manifest_path()"}, {"doc": "Return the SRI string ``<algorithm>-<base64 digest>`` for ``data``.", "kind": "function", "line": 30, "name": "compute_sri", "signature": "def compute_sri(data, algorithm)"}, {"doc": "Return the SRI string for the bytes stored at ``path``.", "kind": "function", "line": 36, "name": "compute_file_sri", "signature": "def compute_file_sri(path, algorithm)"}, {"doc": "Return the raw manifest text, cached for the process lifetime.", "kind": "function", "line": 42, "name": "_cached_manifest_text", "signature": "def _cached_manifest_text()"}, {"doc": "Return the parsed SRI manifest, or an empty mapping when absent.", "kind": "function", "line": 47, "name": "load_manifest", "signature": "def load_manifest()"}, {"doc": "Return the pinned integrity string for one manifest key.\n\nArgs:\n    key: Either a first-party asset path such as ``js/qv-crypto.js``\n        or a full CDN URL.\n\nReturns:\n    The pinned ``sha384-...`` value, or ``None`` when unpinned.", "kind": "function", "line": 55, "name": "integrity_for", "signature": "def integrity_for(key)"}, {"doc": "Drop the cached manifest text so tests see a regenerated file.", "kind": "function", "line": 72, "name": "clear_manifest_cache", "signature": "def clear_manifest_cache()"}, {"doc": "Return the integrity string for a template asset reference.\n\nAccepts the same reference the template already uses: a ``/static/``\npath is normalized to its manifest key, and a full CDN URL resolves\nto the CDN pin. Returns an empty string when unpinned so a missing\nentry fails closed in ``verify_build`` instead of rendering ``None``.", "kind": "function", "line": 77, "name": "template_integrity", "signature": "def template_integrity(key)"}]}, {"doc": "Transactional email helpers for QuantumVault.  Centralizes how outbound transactional mail is addressed and delivered so the registration flow and the background scheduler share a single implementation instead of each rebuilding absolute URLs and calling Flask-Mail directly.  The public host used for links is taken from ``SERVER_NAME`` and ``PREFERRED_URL_SCHEME`` so the same code produces correct links from a background thread (no request context) and from a request handler.", "id": "utils/mailer.py", "kind": "module", "label": "mailer.py", "language": "py", "sha256": "f29025ec577736d7", "symbol_count": 3, "symbols": [{"doc": "Build an absolute URL for a root-relative path using the public host.\n\nArgs:\n    path: A path such as ``/confirm/<token>``. A leading slash is added\n        if missing.\n\nReturns:\n    The absolute URL, for example ``https://www.quantumvault.pro/confirm/x``.", "kind": "function", "line": 22, "name": "external_url", "signature": "def external_url(path)"}, {"doc": "Return True when SMTP credentials are present so a send can succeed.\n\nA send is only attempted when both a username and password are set,\nwhich lets callers fall back to logging a link in local or bare-VPS\ndeployments that have no mail account yet.", "kind": "function", "line": 38, "name": "mail_is_configured", "signature": "def mail_is_configured()"}, {"doc": "Send a plain-text transactional email through the configured server.\n\nThis never raises: a failure is logged and reported through the boolean\nreturn so callers (registration, scheduler) degrade gracefully instead of\naborting the surrounding operation.\n\nArgs:\n    subject: The email subject line.\n    recipients: One or more destination addresses.\n    body: The plain-text message body.\n\nReturns:\n    True if Flask-Mail accepted the message, False otherwise.", "kind": "function", "line": 51, "name": "send_transactional_email", "signature": "def send_transactional_email(subject, recipients, body)"}]}, {"doc": "Fixed-bucket padding for metadata-size concealment (QV-PAD-1).  An observer who cannot read ciphertext can still read its length. This module groups every plaintext into fixed buckets so the wire reveals only a coarse size class instead of an exact byte count.  Wire format for one padded plaintext of bucket ``B``::  LENGTH_PREFIX || PLAINTEXT || RANDOM_PAD  where ``LENGTH_PREFIX`` is the true plaintext length as a 4-byte big-endian unsigned integer and ``RANDOM_PAD`` is fresh output from :mod:`secrets` filling the remainder ``B - prefix - len(plaintext)``. The padded plaintext is then encrypted with AES-256-GCM, so the stored and transmitted ciphertext length is ``B + GCM_OVERHEAD_BYTES`` for every plaintext inside the same bucket.  Cache safety contract: the only value ever cached is the immutable bucket table itself, keyed by configuration version, never by message content or message length. Padding bytes are drawn fresh from the operating-system CSPRNG on every call and are never stored, reused, or placed in any cache. Reusing pad bytes across envelopes would make equal-length plaintexts produce related padded inputs, so reuse is forbidden by construction: there is no API that accepts caller-supplied pad bytes and no cache entry that holds them.  Bucket lookup always scans the full table so the number of iterations does not depend on which bucket matched.", "id": "utils/padding.py", "kind": "module", "label": "padding.py", "language": "py", "sha256": "5c429d8e6d1a922e", "symbol_count": 13, "symbols": [{"doc": "Raised when data does not fit any bucket or framing is invalid.", "kind": "class", "line": 73, "name": "PaddingError", "signature": "class PaddingError(ValueError)"}, {"doc": "Immutable bucket tables for the two padded payload kinds.", "kind": "class", "line": 78, "name": "PaddingConfig", "signature": "class PaddingConfig"}, {"doc": "Parse a comma-separated bucket list, falling back on any error.", "kind": "method", "line": 95, "name": "_parse_buckets", "signature": "def _parse_buckets(raw, fallback)"}, {"doc": "Build a :class:`PaddingConfig` from the environment.\n\n``QV_PAD_MESSAGE_BUCKETS`` and ``QV_PAD_FILE_BUCKETS`` accept\ncomma-separated byte sizes. Unset or malformed values resolve to the\ncompiled defaults so a misconfigured host fails closed to a known\ntable instead of disabling padding.", "kind": "method", "line": 109, "name": "config_from_env", "signature": "def config_from_env()"}, {"doc": "Return the cached immutable bucket tables for one config version.\n\nThe cache key is the comma-joined bucket lists, so distinct operator\nconfigurations never share an entry. Only the tables are cached.\nPlaintexts, ciphertexts, lengths of individual payloads, and random\npad bytes never enter this cache.", "kind": "method", "line": 128, "name": "_cached_bucket_table", "signature": "def _cached_bucket_table(fingerprint)"}, {"doc": "Return the process-wide cached bucket tables for ``config``.", "kind": "method", "line": 142, "name": "cached_tables", "signature": "def cached_tables(config)"}, {"doc": "Return the smallest bucket holding ``plaintext_len`` plus prefix.\n\nRaises:\n    PaddingError: If the payload plus prefix exceeds every bucket.", "kind": "method", "line": 149, "name": "bucket_for", "signature": "def bucket_for(plaintext_len, kind, config)"}, {"doc": "Pad ``plaintext`` to its bucket with fresh CSPRNG bytes.\n\nRaises:\n    PaddingError: If the payload does not fit any bucket.", "kind": "method", "line": 169, "name": "pad", "signature": "def pad(plaintext, kind, config)"}, {"doc": "Remove bucket framing and return the original plaintext.\n\nRaises:\n    PaddingError: If the length is not a bucket or framing is corrupt.", "kind": "method", "line": 183, "name": "unpad", "signature": "def unpad(padded, kind, config)"}, {"doc": "Return the AES-256-GCM ciphertext length for one padded bucket.", "kind": "method", "line": 209, "name": "wire_ciphertext_len", "signature": "def wire_ciphertext_len(bucket)"}, {"doc": "Return True when ``ciphertext_len`` matches a bucket plus GCM overhead.", "kind": "method", "line": 214, "name": "is_allowed_ciphertext_len", "signature": "def is_allowed_ciphertext_len(ciphertext_len, kind, config)"}, {"doc": "Return the bucket table for ``kind``.", "kind": "method", "line": 84, "name": "buckets_for", "signature": "def buckets_for(self, kind)"}, {"doc": "Return the largest plaintext that fits ``kind``.", "kind": "method", "line": 90, "name": "max_plaintext_bytes", "signature": "def max_plaintext_bytes(self, kind)"}]}, {"id": "utils/plans.py", "kind": "module", "label": "plans.py", "language": "py", "sha256": "00d0254af3eb604f", "symbol_count": 3, "symbols": [{"doc": "Define los planes de suscripción disponibles.", "kind": "class", "line": 3, "name": "SubscriptionPlans", "signature": "class SubscriptionPlans"}, {"doc": "Obtiene los detalles de un plan.\n\nArgs:\n    plan_name (str): Nombre del plan.\n\nReturns:\n    Dict: Detalles del plan.", "kind": "method", "line": 30, "name": "get_plan", "signature": "def get_plan(plan_name)"}, {"doc": "Valida que el monto pagado coincide con el plan.", "kind": "method", "line": 42, "name": "validate_plan_payment", "signature": "def validate_plan_payment(plan_name, amount_paid)"}]}, {"doc": "Background scheduler for trial expiration and inbox cleanup.  Runs two recurring jobs:  - ``check_trial_expiration`` (every 24h): flips ``subscription_status`` to ``inactive`` once the free trial has elapsed, and emails the user with a renewal link. - ``cleanup_old_messages`` (every 24h): drops inbox messages older than 7 days for inactive free users.  Both jobs run in APScheduler's BackgroundScheduler, so they execute on a separate thread from the Flask request workers. Any exception inside a job is logged but does not crash the scheduler process.", "id": "utils/scheduler.py", "kind": "module", "label": "scheduler.py", "language": "py", "sha256": "87c92deed537960c", "symbol_count": 5, "symbols": [{"doc": "Timezone-aware UTC ``now`` (avoids the deprecated ``datetime.utcnow()``).", "kind": "function", "line": 32, "name": "_now_utc", "signature": "def _now_utc()"}, {"doc": "Start the background scheduler with the production job schedule.\n\nThe jobs run in a daemon thread, so they do not block the Flask\nrequest loop. They are added idempotently: re-importing the module\ndoes not register duplicates because :class:`BackgroundScheduler`\nis local to this call.", "kind": "function", "line": 37, "name": "init_scheduler", "signature": "def init_scheduler(app, mail)"}, {"doc": "Return True if the user is on a free plan and the trial has ended.", "kind": "function", "line": 54, "name": "_is_trial_elapsed", "signature": "def _is_trial_elapsed(user)"}, {"kind": "function", "line": 72, "name": "check_trial_expiration", "signature": "def check_trial_expiration()"}, {"kind": "function", "line": 118, "name": "cleanup_old_messages", "signature": "def cleanup_old_messages()"}]}, {"doc": "Centralized security primitives for QuantumVault.  Single source of truth for:  - The structured audit log used by every security-relevant event (registration, login, MFA, lockouts, contact, role changes, etc.). - A JSON-CSRF decorator that protects ``/api/*`` POST/PUT/DELETE routes against cross-origin forgery via the ``X-CSRF-Token`` header (the same token already issued by ``/api/csrf-token``). - Small helpers for constant-time comparison and secret hashing of short-lived codes (phone verification, MFA, recovery codes).  Keeping these in one module makes the threat model auditable: if a new endpoint is added and it touches the audit logger, the call site becomes trivially visible during a security review.", "id": "utils/security.py", "kind": "module", "label": "security.py", "language": "py", "sha256": "63dbd5a67c65da15", "symbol_count": 10, "symbols": [{"doc": "Return the process-wide audit logger, configured on first use.\n\nThe audit logger writes single-line JSON records to stdout. Every\nsecurity-relevant event (login success/failure, registration, MFA,\ncontact message, role change, account lockout, CSRF rejection) must\ncall :func:`audit_event` so that incident response has a single\nstream to correlate against.", "kind": "function", "line": 46, "name": "_get_audit_logger", "signature": "def _get_audit_logger()"}, {"doc": "Return the per-request correlation id, generating one if missing.\n\nThe id is stored on Flask's ``g`` so a single request emits multiple\naudit events that share the same key, which is what an operator needs\nwhen reconstructing a session.", "kind": "function", "line": 72, "name": "_correlation_id", "signature": "def _correlation_id()"}, {"doc": "Emit a structured audit record.\n\nArgs:\n    event: A short, snake_case event name, e.g. ``login_success`` or\n        ``mfa_failure``.\n    **fields: Additional structured fields to record. The keys\n        ``ts`` (unix epoch in milliseconds), ``event``, ``cid``\n        (correlation id), ``ip``, and ``ua`` are added automatically.\n\nThe ``ip`` and ``ua`` fields are recorded as ``None`` when\n``QV_AUDIT_LOG_IP=0`` or ``QV_AUDIT_LOG_UA=0`` respectively, for\noperators running for high-risk users (e.g. behind Tor) who do not\nwant client IP addresses or User-Agent strings persisted to logs.\nBoth default to enabled (``\"1\"``).", "kind": "function", "line": 86, "name": "audit_event", "signature": "def audit_event(event)"}, {"doc": "Return True if the two strings match in constant time.\n\nA regular ``==`` leaks length and content-prefix information via\nshort-circuit evaluation. This wraps :func:`hmac.compare_digest`\nwhich compares the whole input even when lengths differ.", "kind": "function", "line": 123, "name": "constant_time_compare", "signature": "def constant_time_compare(a, b)"}, {"doc": "Hash a short-lived secret (phone code, MFA, recovery code) for storage.\n\nUses SHA-256 with a server-side pepper. The pepper is read from the\n``QV_SECRET_PEPPER`` environment variable and falls back to a value\nderived from ``SECRET_KEY`` so the hash is non-deterministic across\nreinstalls but stable for a given deployment.\n\nThe goal is to avoid storing plaintext codes in the database: a DB\ndump no longer hands an attacker ready-to-use codes. Phone codes\nare 6 digits and MFA codes are 6 digits, so a peppered SHA-256 is\nmore than sufficient: an attacker with the DB but without the\npepper must precompute a 10^6-entry rainbow table per deployment.", "kind": "function", "line": 135, "name": "hash_secret", "signature": "def hash_secret(secret)"}, {"doc": "Verify a short-lived secret against its stored hash.", "kind": "function", "line": 156, "name": "verify_secret", "signature": "def verify_secret(secret, expected_hash)"}, {"doc": "Return a cryptographically random numeric verification code.", "kind": "function", "line": 163, "name": "new_one_time_code", "signature": "def new_one_time_code(length)"}, {"doc": "Return the CSRF token from the request header or body.\n\nMirrors Flask-WTF's own lookup order so a client that sets either\n``X-CSRFToken`` or ``X-CSRF-Token`` (the two spellings Flask-WTF accepts\nin ``WTF_CSRF_HEADERS``), or a ``csrf_token`` form/JSON field, is handled\nuniformly. The browser crypto in ``static/js/qv-crypto.js`` sends the\n``X-CSRFToken`` header.", "kind": "function", "line": 172, "name": "_extract_csrf_token", "signature": "def _extract_csrf_token()"}, {"doc": "Decorator: require a valid CSRF token on JSON state-changing requests.\n\nThe token is the one Flask-WTF issues through ``form.hidden_tag()`` or\n``/api/csrf-token``. It is a *signed* value, so it is validated with\n:func:`flask_wtf.csrf.validate_csrf`, which unsigns it and compares it to\nthe raw token held in the session; a direct string comparison against the\nsession value never matches and must not be used. A missing or invalid\ntoken is rejected with HTTP 403 and recorded in the audit log.\n\nGET, HEAD and OPTIONS pass through unchanged because they are not\nstate-changing. Use this on every ``/api/`` route that mutates state.", "kind": "function", "line": 193, "name": "json_csrf_protect", "signature": "def json_csrf_protect(view)"}, {"kind": "function", "line": 207, "name": "wrapper", "signature": "def wrapper()"}]}, {"doc": "Zero-knowledge SRP-6a authentication primitives for QuantumVault.  This module implements the server side of a Secure Remote Password (SRP-6a) handshake using the RFC 5054 2048-bit group with SHA-256. The user's password never reaches the server: registration stores only ``salt`` and the password verifier ``v = g**x mod N``; authentication is a challenge/response that proves knowledge of the password without transmitting it.  The serialization scheme (\"QV-SRP-1\") is implemented identically in the browser module ``static/js/qv-crypto.js`` so both ends agree byte-for-byte:  - Every group element hashed (N, g, A, B, S) is encoded as a big-endian integer left-padded to the byte length of N (256 bytes) via :func:`i2osp`. - ``H`` is SHA-256 over the concatenation of byte strings. - ``salt`` travels as a hex string; its raw bytes are used inside hashes.  Public functions perform the SRP math; :class:`SRPSessionStore` persists the ephemeral per-login server state in Redis with a short time-to-live.", "id": "utils/srp6a.py", "kind": "module", "label": "srp6a.py", "language": "py", "sha256": "3a9483fd0ce949df", "symbol_count": 14, "symbols": [{"doc": "Encode an integer as a big-endian byte string padded to the length of N.\n\nArgs:\n    value: Non-negative integer to encode (a group element).\n\nReturns:\n    The big-endian representation left-padded with zero bytes to\n    ``N_BYTE_LENGTH``.", "kind": "function", "line": 47, "name": "i2osp", "signature": "def i2osp(value)"}, {"doc": "Return the SHA-256 digest of the concatenated byte chunks.", "kind": "function", "line": 60, "name": "_hash", "signature": "def _hash()"}, {"doc": "Return the SHA-256 digest of the concatenated chunks as an integer.", "kind": "function", "line": 68, "name": "_hash_int", "signature": "def _hash_int()"}, {"doc": "Compute the SRP-6a multiplier parameter ``k = H(N | PAD(g))``.", "kind": "function", "line": 73, "name": "compute_k", "signature": "def compute_k()"}, {"doc": "Compute the random scrambling parameter ``u = H(PAD(A) | PAD(B))``.\n\nArgs:\n    server_a: The client public ephemeral value A.\n    server_b: The server public ephemeral value B.\n\nReturns:\n    The scrambling parameter u as an integer.", "kind": "function", "line": 78, "name": "compute_u", "signature": "def compute_u(server_a, server_b)"}, {"doc": "Generate the server ephemeral key pair (b, B) for a login challenge.\n\nArgs:\n    verifier: The stored password verifier ``v`` for the user.\n\nReturns:\n    A tuple ``(b, B)`` where ``b`` is the secret ephemeral and\n    ``B = (k * v + g**b) mod N`` is the public value sent to the client.", "kind": "function", "line": 91, "name": "generate_server_challenge", "signature": "def generate_server_challenge(verifier)"}, {"doc": "Compute the expected client proof M1 and the server proof M2.\n\nArgs:\n    username: The user identity I.\n    salt_hex: The user salt as a hex string.\n    verifier: The stored password verifier v.\n    server_a: The client public ephemeral A.\n    server_b: The server public ephemeral B.\n    server_b_secret: The server secret ephemeral b.\n\nReturns:\n    A tuple ``(expected_m1, m2)`` of raw digest bytes.", "kind": "function", "line": 107, "name": "compute_proofs", "signature": "def compute_proofs(username, salt_hex, verifier, server_a, server_b, server_b_secret)"}, {"doc": "Redis-backed store for the ephemeral state of an in-flight SRP login.\n\nEach ``hello`` step persists the values needed to verify the subsequent\n``verify`` step. Entries expire after :data:`SESSION_TTL_SECONDS` so an\nabandoned handshake cannot be resumed later.", "kind": "class", "line": 150, "name": "SRPSessionStore", "signature": "class SRPSessionStore"}, {"doc": "Process the SRP ``hello`` step and return the server challenge B.\n\nArgs:\n    store: The ephemeral session store.\n    username: The user identity.\n    client_a_hex: The client public ephemeral A as a hex string.\n    salt_hex: The stored user salt as a hex string.\n    verifier_hex: The stored verifier as a hex string.\n\nReturns:\n    The server public ephemeral B as a hex string, or ``None`` if the\n    client value A is invalid (``A mod N == 0``).", "kind": "method", "line": 224, "name": "hello", "signature": "def hello(store, username, client_a_hex, salt_hex, verifier_hex)"}, {"doc": "Process the SRP ``verify`` step and return the server proof M2.\n\nArgs:\n    store: The ephemeral session store.\n    username: The user identity.\n    client_m1_hex: The client proof M1 as a hex string.\n\nReturns:\n    The server proof M2 as a hex string on success, or ``None`` if no\n    pending session exists or the client proof is invalid.", "kind": "method", "line": 260, "name": "verify", "signature": "def verify(store, username, client_m1_hex)"}, {"doc": "Initialize the store from a Redis connection URI.\n\nArgs:\n    storage_uri: A ``redis://`` connection string (the same one used by\n        the rate limiter).", "kind": "method", "line": 158, "name": "__init__", "signature": "def __init__(self, storage_uri)"}, {"doc": "Return the Redis key for a username's pending SRP session.", "kind": "method", "line": 168, "name": "_key", "signature": "def _key(username)"}, {"doc": "Persist the ephemeral SRP challenge state for a username.\n\nArgs:\n    username: The user identity.\n    salt_hex: The user salt as a hex string.\n    verifier_hex: The stored verifier as a hex string.\n    server_a_hex: The client public ephemeral A as a hex string.\n    server_b_hex: The server public ephemeral B as a hex string.\n    server_b_secret_hex: The server secret ephemeral b as a hex string.", "kind": "method", "line": 172, "name": "save", "signature": "def save(self, username, salt_hex, verifier_hex, server_a_hex, server_b_hex, server_b_secret_hex)"}, {"doc": "Load and consume the ephemeral SRP state for a username.\n\nThe entry is deleted on read so each challenge is single-use.\n\nArgs:\n    username: The user identity.\n\nReturns:\n    The stored session dictionary, or ``None`` if no valid session\n    exists (expired, missing, or already consumed).", "kind": "method", "line": 202, "name": "load", "signature": "def load(self, username)"}]}, {"doc": "utils/utils.py", "id": "utils/utils.py", "kind": "module", "label": "utils.py", "language": "py", "sha256": "dcefa546f93b5ed2", "symbol_count": 8, "symbols": [{"doc": "Return the SQLite database path from config, with a legacy fallback.\n\nRequest-path code must never hard-code a database location: in tests and\nin multi-instance deployments the configured path is the only correct\none, and a hard-coded path silently writes to (or reads from) the wrong\nfile. Outside an application context, for standalone scripts, the\n``QV_USERS_DB`` environment variable or the historical default is used.", "kind": "function", "line": 12, "name": "database_path", "signature": "def database_path()"}, {"doc": "Coerce an environment or payload value into a real boolean.\n\nStrings such as ``\"True\"`` and ``\"False\"`` are both truthy when passed\nstraight to Flask, which silently enables flags that were meant to be\ndisabled. This normalizes them so ``MAIL_USE_TLS=\"False\"`` disables TLS.\n\nArgs:\n    value: The raw value from ``os.environ`` or ``payload.json``.\n    default: The value to return when ``value`` is ``None``.\n\nReturns:\n    The coerced boolean.", "kind": "function", "line": 29, "name": "as_bool", "signature": "def as_bool(value, default)"}, {"doc": "Sanitiza una ruta de archivo para prevenir LFI y path traversal.\n- Elimina caracteres peligrosos\n- Normaliza la ruta\n- Asegura que no contenga '..' o rutas absolutas", "kind": "function", "line": 49, "name": "sanitize_path", "signature": "def sanitize_path(path)"}, {"doc": "Non-secret application configuration loaded from ``payload.json``.", "kind": "class", "line": 80, "name": "Payload", "signature": "class Payload(TypedDict)"}, {"doc": "Application configuration sourced from ``payload.json`` and the environment.\n\nNon-secret defaults come from ``payload.json``; secrets and infrastructure\nendpoints (mail credentials, object storage, Redis) are overlaid from\nenvironment variables so that no credential is committed to the repository.\n\nEvery attribute is declared on the class so static analyzers see the\nfull shape; :meth:`__init__` populates them from the loaded payload.", "kind": "class", "line": 103, "name": "Config", "signature": "class Config"}, {"doc": "Load non-secret application configuration from ``payload.json``.\n\nA local ``.env`` file is loaded first (when ``python-dotenv`` is available)\nso environment-based secrets are populated before :class:`Config` reads them.\n\nReturns:\n    The parsed configuration dictionary.", "kind": "method", "line": 168, "name": "load_payload", "signature": "def load_payload()"}, {"kind": "method", "line": 145, "name": "__init__", "signature": "def __init__(self, config_dict)"}, {"kind": "method", "line": 165, "name": "__getitem__", "signature": "def __getitem__(self, key)"}]}, {"id": "views/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "38b630c560760858", "symbol_count": 0, "symbols": []}, {"id": "views/about.py", "kind": "module", "label": "about.py", "language": "py", "sha256": "09714a0827826987", "symbol_count": 1, "symbols": [{"doc": "Render the About page.", "kind": "function", "line": 6, "name": "about", "signature": "def about()"}]}, {"doc": "Account settings page and the deniable vault JSON API (QV-DENIABLE-1).  The settings page is a normal, universal part of every authenticated account, regardless of role. It deliberately does not advertise the deniable vault as a special feature: the page looks the same for everyone, and the API never tells the caller whether a hidden vault is configured. That is by design. A deniable vault only protects the user if its presence leaves no evidence; an obvious \"you have a hidden vault\" indicator would make coercion more effective, not less.  Routes:  - ``GET    /account``            : render the account settings page - ``GET    /api/account/vault``  : return the user's opaque container, minting an indistinguishable random one if the account has none yet - ``PUT    /api/account/vault``  : validate and store a container - ``DELETE /api/account/vault``  : reset the container to a fresh random one  The server validates container *structure* only; it never decrypts a slot or sees a passphrase (see :mod:`controllers.deniable_vault`).", "id": "views/account.py", "kind": "module", "label": "account.py", "language": "py", "sha256": "0e8290c809d51742", "symbol_count": 5, "symbols": [{"doc": "Build a controller bound to the active app's database and config.\n\nThe database path and structural parameters are read from\n``current_app.config`` so tests (which point the app at a temporary\ndatabase and may override limits) and production share one code path.", "kind": "function", "line": 51, "name": "get_deniable_vault_controller", "signature": "def get_deniable_vault_controller()"}, {"doc": "Render the account settings page.\n\nWhen the cover facade is enabled the decoy feature requires a deniable\npassphrase, so the page asks for one. The server never learns whether a\npassphrase has been set: it only exposes the instance-level facade flag.", "kind": "function", "line": 65, "name": "settings", "signature": "def settings()"}, {"doc": "Return the user's container and the build parameters.\n\nThe response always includes an ``envelope`` (a random one is minted on\nfirst access) and the structural ``parameters``. It never includes a\n\"configured\" flag: whether the container holds real data is exactly\nwhat must stay hidden.", "kind": "function", "line": 85, "name": "get_vault", "signature": "def get_vault()"}, {"doc": "Validate and store a container for the user.", "kind": "function", "line": 107, "name": "put_vault", "signature": "def put_vault()"}, {"doc": "Reset the user's container to a fresh random one.\n\nReset, not delete: removing the row would distinguish an account that\ndeactivated from one that never activated. A random container keeps the\n\"every account has one\" invariant intact.", "kind": "function", "line": 130, "name": "delete_vault", "signature": "def delete_vault()"}]}, {"id": "views/admin.py", "kind": "module", "label": "admin.py", "language": "py", "sha256": "993ac16ea5df1189", "symbol_count": 19, "symbols": [{"doc": "Append one superadmin audit row with a single construction site.", "kind": "function", "line": 31, "name": "_audit_action", "signature": "def _audit_action(actor, action, target_user, ip, details)"}, {"doc": "Build the disposable channel manager from env and app config.", "kind": "function", "line": 48, "name": "_channel_manager", "signature": "def _channel_manager()"}, {"doc": "Return whether the Garage S3 endpoint answers a TCP probe.\n\nThe file inventory below fans out one listing per user, each\nwith its own retry budget. Probing once up front keeps a downed\nobject store from turning every panel view into a retry storm\nin the logs. A closed port means every listing would fail\nanyway, so skipping them loses nothing.", "kind": "function", "line": 54, "name": "_s3_reachable", "signature": "def _s3_reachable(timeout)"}, {"doc": "Return the last lines of backend logs for operator diagnosis.\n\nOnly the superadmin panel sees this, and it never leaves the\nserver: Jinja autoescaping renders it as text. Missing logs\nyield an empty string instead of an error.", "kind": "function", "line": 84, "name": "_read_log_tail", "signature": "def _read_log_tail(state_dir, limit)"}, {"doc": "Collect binary availability and paths without launching anything.", "kind": "function", "line": 116, "name": "_channel_diagnostics", "signature": "def _channel_diagnostics(manager)"}, {"doc": "Form for editing user details.\n\nIntentionally does NOT carry these fields:\n\n* ``confirmation_token`` — rotated by the resend-confirmation\n  endpoint, never hand-edited. A static token cannot expire and\n  would either lock the user out or be reused forever.\n* ``phone_verification_code`` — same reason; the column stores\n  a hash, not the cleartext code, so a superadmin UI input is\n  meaningless.\n* KEM/SRP blob columns (srp_salt, srp_verifier, public_key,\n  encrypted_private_key, kdf_salt) — the server has no UI to\n  rewrite them. Modifying any of them would silently brick the\n  user's login.\n\n``password`` is also absent: the server is zero-knowledge, so a\n\"change password\" UI lives in the user's own profile, not here.", "kind": "class", "line": 141, "name": "UserEditForm", "signature": "class UserEditForm(FlaskForm)"}, {"doc": "Form for creating or editing a subscription plan.", "kind": "class", "line": 174, "name": "PlanForm", "signature": "class PlanForm(FlaskForm)"}, {"doc": "Plan catalog read view.\n\nPlan CRUD lives at ``/admin<token>/plans`` and\n``/admin<token>/plans/edit/<name>`` so a single page is not also\na destructive form. This view is now strictly a list of\navailable plans, with a per-row edit link.\n\nUser identity (list, edit, suspend, MFA reset, confirmation\nrotation) is the superadmin panel's job and lives at\n``/superadmin<token>``.", "kind": "method", "line": 186, "name": "admin", "signature": "def admin()"}, {"doc": "Full profile edit for a single user.\n\nLives under ``/superadmin<token>`` because every field here touches\nidentity directly (role, verifications, quota, subscription). Admin\nrole no longer has access: the superadmin panel is the only place\nthat can rewrite those columns.\n\nFields intentionally NOT editable through this form:\n\n* ``confirmation_token`` — rotated by the resend-confirmation\n  endpoint, never hand-edited (a static token cannot expire).\n* ``phone_verification_code`` — same reason, lives in a hashed\n  column anyway so even a superadmin should not see it.\n* KEM/SRP blob columns (srp_salt, srp_verifier, public_key,\n  encrypted_private_key, kdf_salt) — modifying any of these would\n  silently brick the user's login. The server has no UI to rewrite\n  them and never should.", "kind": "method", "line": 208, "name": "superadmin_edit_user", "signature": "def superadmin_edit_user(username)"}, {"doc": "Handle plan management.", "kind": "method", "line": 313, "name": "manage_plans", "signature": "def manage_plans()"}, {"doc": "Handle editing of plan details.", "kind": "method", "line": 337, "name": "edit_plan", "signature": "def edit_plan(plan_name)"}, {"doc": "Superadmin identity-recovery and inventory panel.\n\nRead-only by design. The server is zero-knowledge, so it can never\ndecrypt user content; instead this view surfaces the actions a\nsuperadmin actually has to perform during incident response:\n\n* inventory of encrypted file names per user (metadata only)\n* last 50 audit log entries (who did what to which account)\n* the user table with per-row privileged action buttons\n\nMutating actions live in the three POST handlers below. The GET\nhandler must never accept a side-effect query string, otherwise an\nattacker could trigger a reset by luring a superadmin to follow a\ncrafted link.", "kind": "method", "line": 373, "name": "superadmin", "signature": "def superadmin()"}, {"doc": "Disable MFA and clear the pending code for ``username``.\n\nUsed when a user loses their authenticator device. We do NOT\ntouch the password, the email, or the KEM material — losing a\nsecond factor should not invalidate the rest of the identity.", "kind": "method", "line": 476, "name": "superadmin_reset_mfa", "signature": "def superadmin_reset_mfa(username)"}, {"doc": "Issue a fresh ``confirmation_token`` for ``username``.\n\nThe token's 24h expiry is recomputed by ``update_user`` (see\nmodels/user.py:337). If the user already verified, we still issue\na new token so the link can be reused as a magic-link login path\n— useful when a user has lost access to their primary device.", "kind": "method", "line": 523, "name": "superadmin_resend_confirmation", "signature": "def superadmin_resend_confirmation(username)"}, {"doc": "Flip ``subscription_status`` between active and inactive.\n\nSuspension is a billing/operational lever (refuse new uploads,\nblock new devices) that does not require touching the KEM\nmaterial. Reactivation brings the user back into the same\nposition they were in before suspension.", "kind": "method", "line": 570, "name": "superadmin_toggle_suspend", "signature": "def superadmin_toggle_suspend(username)"}, {"doc": "Start a disposable secure channel in the requested mode.\n\nAccepts ``cloudflared``, ``tor``, or ``hybrid`` from the panel form.\nAny other value is rejected so a crafted POST cannot smuggle a mode\nthe supervisor does not know. Audit details carry only the mode\nplus address fingerprints, never the addresses themselves.", "kind": "method", "line": 620, "name": "superadmin_channel_start", "signature": "def superadmin_channel_start()"}, {"doc": "Dispose the running channel and remove its addresses.", "kind": "method", "line": 659, "name": "superadmin_channel_stop", "signature": "def superadmin_channel_stop()"}, {"doc": "Dispose current addresses and publish fresh ones in the same mode.", "kind": "method", "line": 682, "name": "superadmin_channel_rotate", "signature": "def superadmin_channel_rotate()"}, {"kind": "method", "line": 705, "name": "admin_contacts", "signature": "def admin_contacts()"}]}, {"doc": "Authentication and account-management views.  Routes:  - ``GET  /register``            : render the registration form - ``POST /register``            : create a new account from a zero-knowledge payload - ``GET  /login``               : render the login form - ``POST /api/srp/hello``       : SRP-6a step 1, returns salt and server challenge B - ``POST /api/srp/verify``      : SRP-6a step 2, returns server proof M2 and starts a session - ``GET  /logout``              : clear the session - ``GET  /confirm/<token>``     : mark an email as verified - ``GET/POST /verify_phone``    : enter the phone verification code - ``GET/POST /verify_mfa``      : enter the MFA code - ``POST /toggle_mfa``          : enable or disable MFA for the current user - ``GET  /contact``             : render and accept the contact form - ``GET  /api/auth/pubkey``     : return a user's hybrid public key - ``GET  /api/auth/user-keys``  : return the current user's keying material - ``GET  /api/csrf-token``      : issue the CSRF token for SPA use  Every state-changing JSON route is decorated with :func:`utils.security.json_csrf_protect` so a cross-origin request without the matching CSRF token is rejected with HTTP 403 and audited.", "id": "views/auth.py", "kind": "module", "label": "auth.py", "language": "py", "sha256": "7b1c598dc2f2c49a", "symbol_count": 29, "symbols": [{"doc": "Restrict a route to authenticated users holding one of the given roles.\n\nThe check is an intersection of ``VALID_ROLES`` and the caller-\nsupplied roles so a typo in a future route (e.g. ``role_required(\"user\")``)\ncannot accidentally grant access because the role never existed.", "kind": "function", "line": 71, "name": "role_required", "signature": "def role_required()"}, {"kind": "class", "line": 98, "name": "PhoneVerificationForm", "signature": "class PhoneVerificationForm(FlaskForm)"}, {"kind": "class", "line": 103, "name": "MFAForm", "signature": "class MFAForm(FlaskForm)"}, {"kind": "class", "line": 108, "name": "ContactForm", "signature": "class ContactForm(FlaskForm)"}, {"kind": "class", "line": 114, "name": "RegisterForm", "signature": "class RegisterForm(FlaskForm)"}, {"kind": "class", "line": 124, "name": "LoginForm", "signature": "class LoginForm(FlaskForm)"}, {"kind": "method", "line": 132, "name": "get_auth_controller", "signature": "def get_auth_controller()"}, {"kind": "method", "line": 143, "name": "show_register", "signature": "def show_register()"}, {"kind": "method", "line": 150, "name": "handle_register", "signature": "def handle_register()"}, {"kind": "method", "line": 234, "name": "login", "signature": "def login()"}, {"doc": "Render the QV-RECOVERY-1 account-recovery page.\n\nAvailable to anonymous visitors: a forgotten password means the\nvisitor cannot authenticate, by definition.", "kind": "method", "line": 242, "name": "recover", "signature": "def recover()"}, {"kind": "method", "line": 255, "name": "_srp_key", "signature": "def _srp_key()"}, {"kind": "method", "line": 266, "name": "_recovery_key", "signature": "def _recovery_key()"}, {"doc": "First SRP-6a step: receive the client public value A, return salt and B.", "kind": "method", "line": 278, "name": "srp_hello", "signature": "def srp_hello()"}, {"doc": "Second SRP-6a step: verify the client proof M1 and return server proof M2.", "kind": "method", "line": 299, "name": "srp_verify", "signature": "def srp_verify()"}, {"kind": "method", "line": 337, "name": "logout", "signature": "def logout()"}, {"kind": "method", "line": 344, "name": "confirm_email", "signature": "def confirm_email(token)"}, {"kind": "method", "line": 367, "name": "verify_phone", "signature": "def verify_phone()"}, {"doc": "Re-send the phone verification code for an account.\n\nThe username is supplied as a query parameter by the verify-phone\ntemplate's resend form. The form carries the CSRF token, so the\napp-wide CSRFProtect guard applies. The handler never reveals whether\nthe account exists: it always redirects back with a neutral message.", "kind": "method", "line": 384, "name": "resend_phone_verification", "signature": "def resend_phone_verification()"}, {"kind": "method", "line": 407, "name": "verify_mfa", "signature": "def verify_mfa()"}, {"kind": "method", "line": 429, "name": "toggle_mfa", "signature": "def toggle_mfa()"}, {"doc": "Render the contact form and persist a message from the current user.\n\nThe page is only meaningful for authenticated users: messages are tied to\na ``user_id`` foreign key in ``contacts``. Anonymous visitors are sent\nto the login page so they can sign in (or register) before contacting.", "kind": "method", "line": 454, "name": "contact", "signature": "def contact()"}, {"doc": "Return a user's hybrid public key so the browser can wrap data to them.", "kind": "method", "line": 485, "name": "get_public_key", "signature": "def get_public_key()"}, {"doc": "Provide the keys a user needs to decrypt their data client-side.\n\nThe caller must already be authenticated and asking for their own\nmaterial; the route refuses to return anyone else's keying data.", "kind": "method", "line": 503, "name": "get_user_keys", "signature": "def get_user_keys()"}, {"doc": "Return the QV-RECOVERY-1 bundle for a username, if one was generated.\n\nNo authentication is required: a forgotten password by definition\nmeans the caller cannot log in. The returned values are opaque to\nanyone without the recovery code: ``encrypted_private_key_recovery``\nis AES-256-GCM ciphertext keyed by a PBKDF2 derivation of the\nrecovery code, so exposing it to an unauthenticated caller does not\nweaken the zero-knowledge guarantees.", "kind": "method", "line": 534, "name": "get_recovery_bundle", "signature": "def get_recovery_bundle()"}, {"doc": "Reset SRP credentials and the password-wrapped private key via QV-RECOVERY-1.\n\nThe browser has already decrypted ``encrypted_private_key_recovery``\nusing a key derived from the recovery code and reconstructed the\naccount's public key from the recovered private key blob (see\n``derivePublicKeyFromPrivateBlob`` in ``static/js/qv-crypto.js``).\nThat reconstruction is supplied as ``public_key_proof``: AES-GCM\nauthentication means a wrong recovery code fails to decrypt at all,\nso only a caller who supplied the correct code can produce a\n``public_key_proof`` that matches the stored ``public_key``\nbyte-for-byte. The underlying keypair and ``public_key`` are not\nchanged; only the SRP verifier and the password-wrapping of the\nexisting private key blob are replaced.", "kind": "method", "line": 559, "name": "reset_with_recovery", "signature": "def reset_with_recovery()"}, {"doc": "Issue the CSRF token used by the SPA for state-changing JSON calls.", "kind": "method", "line": 619, "name": "get_csrf_token", "signature": "def get_csrf_token()"}, {"kind": "method", "line": 85, "name": "decorator", "signature": "def decorator(f)"}, {"kind": "method", "line": 87, "name": "decorated_function", "signature": "def decorated_function()"}]}, {"doc": "Cover facade HTTP integration: before-request cover and the gate endpoint.  When the facade is configured, anonymous visitors to the protected pages see a configurable cover instead of the application, and ``POST /gate`` accepts the secret phrase. A correct phrase stores the signed ticket in the session and redirects to the ordinary login page; a miss keeps the cover. Nothing in the response distinguishes a miss from a hit to an unauthenticated observer.", "id": "views/facade.py", "kind": "module", "label": "facade.py", "language": "py", "sha256": "856880d5209f1616", "symbol_count": 6, "symbols": [{"doc": "Install the facade on ``app`` when it is enabled and configured.", "kind": "function", "line": 33, "name": "register_facade", "signature": "def register_facade(app)"}, {"kind": "function", "line": 71, "name": "_build_cover_service", "signature": "def _build_cover_service(config)"}, {"kind": "function", "line": 86, "name": "_ticket_mode", "signature": "def _ticket_mode(gate)"}, {"kind": "function", "line": 41, "name": "render_cover", "signature": "def render_cover()"}, {"kind": "function", "line": 48, "name": "_facade_cover", "signature": "def _facade_cover()"}, {"kind": "function", "line": 60, "name": "facade_gate", "signature": "def facade_gate()"}]}, {"id": "views/faq.py", "kind": "module", "label": "faq.py", "language": "py", "sha256": "096125e3ccccb193", "symbol_count": 2, "symbols": [{"doc": "Render the About page.", "kind": "function", "line": 7, "name": "faq", "signature": "def faq()"}, {"doc": "Render the About page.", "kind": "function", "line": 12, "name": "landing", "signature": "def landing()"}]}, {"id": "views/file.py", "kind": "module", "label": "file.py", "language": "py", "sha256": "015a705347d3e30c", "symbol_count": 3, "symbols": [{"doc": "Formulario para la subida de archivos cifrados.", "kind": "class", "line": 15, "name": "UploadForm", "signature": "class UploadForm(FlaskForm)"}, {"doc": "Maneja la subida de archivos cifrados desde el cliente.", "kind": "method", "line": 25, "name": "upload", "signature": "def upload()"}, {"doc": "Provide the encrypted file and its key for client-side decryption.\n\nThe filename comes from the URL and is used to look up a key under\nthe authenticated user's S3 prefix. The server never lets the\nfilename escape that prefix: any ``/``, ``\\``, ``..`` or control\ncharacter is rejected before the S3 key is constructed, so a\ncrafted ``filename`` like ``../admin/files/x`` cannot exfiltrate\nanother user's ciphertext.", "kind": "method", "line": 56, "name": "download", "signature": "def download(filename)"}]}, {"id": "views/message.py", "kind": "module", "label": "message.py", "language": "py", "sha256": "d7d4c20dade41493", "symbol_count": 3, "symbols": [{"doc": "Form for sending messages.", "kind": "class", "line": 19, "name": "MessageForm", "signature": "class MessageForm(FlaskForm)"}, {"doc": "Render the messages page; the browser handles all crypto.\n\nSending happens via the JSON API in /api/secure_message below.", "kind": "method", "line": 29, "name": "messages", "signature": "def messages()"}, {"doc": "Accept an opaque end-to-end encrypted message envelope.\n\nThe browser already generated the CEK, encrypted the message body with\nAES-256-GCM, and wrapped the CEK to the recipient's and sender's\nhybrid public keys. The server stores only the opaque material.", "kind": "method", "line": 49, "name": "api_secure_message", "signature": "def api_secure_message()"}]}, {"id": "views/privacy.py", "kind": "module", "label": "privacy.py", "language": "py", "sha256": "1164010b6e6fe5e9", "symbol_count": 1, "symbols": [{"doc": "Render the About page.", "kind": "function", "line": 6, "name": "privacy", "signature": "def privacy()"}]}, {"id": "views/subscription.py", "kind": "module", "label": "subscription.py", "language": "py", "sha256": "4b72ac662ce6ccad", "symbol_count": 4, "symbols": [{"doc": "Formulario para seleccionar un plan de suscripción.", "kind": "class", "line": 24, "name": "SubscriptionForm", "signature": "class SubscriptionForm(FlaskForm)"}, {"doc": "Maneja la selección de planes y el proceso de pago.", "kind": "method", "line": 37, "name": "subscribe", "signature": "def subscribe()"}, {"doc": "Maneja el éxito del pago y actualiza el plan del usuario.", "kind": "method", "line": 86, "name": "payment_success", "signature": "def payment_success()"}, {"kind": "method", "line": 26, "name": "__init__", "signature": "def __init__(self)"}]}, {"doc": "End-to-end encrypted file synchronization views.  ``POST /secure_sync`` accepts an opaque encrypted payload from the SPA and stores it under the authenticated user's prefix in S3. The endpoint is CSRF-protected and rate-limited per (IP, user) pair to prevent the server from being used as a free file storage for an attacker who phished a session cookie.", "id": "views/sync.py", "kind": "module", "label": "sync.py", "language": "py", "sha256": "504b2dcc744639ea", "symbol_count": 2, "symbols": [{"doc": "Receive an already-encrypted file + wrapped FEK and persist them.\n\nThe server never sees the plaintext: the file body and the\nwrapped key are opaque from the server's perspective. We only\nenforce quota and basic input validation.", "kind": "function", "line": 29, "name": "secure_sync", "signature": "def secure_sync()"}, {"kind": "function", "line": 79, "name": "sync_page", "signature": "def sync_page()"}]}, {"id": "views/terms.py", "kind": "module", "label": "terms.py", "language": "py", "sha256": "e11ce529060e0bd5", "symbol_count": 1, "symbols": [{"doc": "Render the About page.", "kind": "function", "line": 6, "name": "terms", "signature": "def terms()"}]}, {"doc": "Top-level non-API views: home page, account preferences, etc.", "id": "views/views.py", "kind": "module", "label": "views.py", "language": "py", "sha256": "780b36d60b668245", "symbol_count": 2, "symbols": [{"kind": "class", "line": 15, "name": "MFAEnableForm", "signature": "class MFAEnableForm(FlaskForm)"}, {"doc": "Render the landing/home page.\n\nThe total user count is fetched with ``SELECT COUNT(*)`` directly\nrather than loading every row into memory, so the cost is O(1)\nregardless of the user table size.", "kind": "method", "line": 21, "name": "home", "signature": "def home()"}]}, {"doc": "WSGI entry point for production deployments.  Run with gunicorn (or any WSGI server) behind a TLS-terminating reverse proxy::  gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 2 \\\\ --access-logfile - --error-logfile - \\\\ wsgi:application  The reverse proxy (nginx, Caddy, ALB) terminates TLS and forwards ``X-Forwarded-Proto``. The factory wires up ProxyFix only when the operator sets ``QV_TRUSTED_PROXY=1`` so the request scheme is reconstructed correctly inside Flask.  The Werkzeug dev server is never reachable through this module; that keeps the public surface small.", "id": "wsgi.py", "kind": "module", "label": "wsgi.py", "language": "py", "sha256": "669ffc1f82fbe4e9", "symbol_count": 0, "symbols": []}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### GO (3 files)

#### `client.go`
**Path:** `client.go`

**Functions:**
- `main` (line 13) `func main(`

#### `enc_dec.go`
**Path:** `enc_dec.go`

**Functions:**
- `deriveAESKey` (line 20) `func deriveAESKey(`
- `encryptFile` (line 24) `func encryptFile(`
- `decryptFile` (line 45) `func decryptFile(`
- `main` (line 69) `func main(`

#### `server.go`
**Path:** `server.go`

**Functions:**
- `main` (line 11) `func main(`
- `handleConnection` (line 40) `func handleConnection(`

### JS (10 files)

#### `account.js`
**Path:** `static/js/account.js`
**File Doc:** *Account settings controller: secure notes (QV-DENIABLE-1).  Loaded as an external ES module to comply with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts. All container building and opening happens in qv-deniable.js, in the browser. The server returns and accepts an opaque container plus the non-secret structural parameters; it never sees a passphrase or any note text, and it never reports whether a second set of notes exists.*

**Functions:**
- `setStatus` (line 19)
- `csrfToken` (line 30)
- `apiRequest` (line 36)
- `loadState` (line 54)
- `collectSlots` (line 59)
- `handleConfigure` (line 73)
- `handleOpen` (line 103)
- `handleReset` (line 125)
- `init` (line 138)

#### `coded-text.js`
**Path:** `static/js/coded-text.js`
**File Doc:** *Decipher animation for elements tagged with the "codedText" class.  Extracted from an inline <script> so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts. The effect is purely cosmetic: if the GSAP animation library is not available it degrades gracefully and leaves the text untouched.*

**Functions:**
- `randomChar` (line 12)
- `animateElement` (line 18)
- `init` (line 49)

#### `login.js`
**Path:** `static/js/login.js`
**File Doc:** *Login page controller (zero-knowledge SRP-6a flow).  Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts and inline event handlers. The password never leaves the browser: the SRP handshake exchanges only A (client public) and M1 (proof) and verifies the server proof M2.*

**Functions:**
- `handleLogin` (line 11)
- `init` (line 43)

#### `messages.js`
**Path:** `static/js/messages.js`
**File Doc:** *Messages page controller (zero-knowledge end-to-end messaging).  Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'). Sending encrypts the message to the recipient's hybrid public key in the browser; receiving decrypts the opaque envelopes locally after prompting for the password. Decrypted text is rendered with textContent (never innerHTML) so a malicious sender cannot inject HTML/script into the recipient's page.*

**Functions:**
- `getCsrfToken` (line 11)
- `handleSend` (line 17)
- `collectEnvelopes` (line 43)
- `handleDecryptInbox` (line 60)
- `initEditor` (line 87)
- `init` (line 108)

#### `qv-crypto.js`
**Path:** `static/js/qv-crypto.js`
**File Doc:** *QuantumVault zero-knowledge browser crypto.  Single source of truth for all client-side cryptography. The password and every private key are generated, used, and stored encrypted in the browser; only opaque ciphertext, the SRP salt/verifier, the public key, and the password-encrypted private key blob ever reach the server.  Primitives: - Authentication: SRP-6a (RFC 5054 2048-bit group, SHA-256), scheme "QV-SRP-1" mirroring utils/srp6a.py byte-for-byte. - Key wrapping: hybrid KEM = ML-KEM-768 (post-quantum) + X25519 (classical), combined via HKDF-SHA256, sealing keys with AES-256-GCM. - Size concealment: every message/file plaintext is padded to a fixed bucket (qv-padding.js, QV-PAD-1) before AES-GCM, so ciphertext lengths reveal only the bucket. Pad bytes are fresh crypto.getRandomValues per envelope and are never cached or reused. - Private-key protection: PBKDF2-SHA256 (600k iterations) derives the master key that encrypts the user's private key blob.  All cryptographic primitives are loaded from the local `vendor/` directory instead of a CDN. The vendored bundles are pinned to specific upstream versions, served as first-party static assets, and benefit from the same SRI / CSP protections as the rest of the application. The version comment on each import is the upstream package version that was vendored.  noble/hashes 1.8.0 — SHA-2, HKDF, utils, browser crypto provider*

**Functions:**
- `concatBytes` (line 58) - *-- Encoding helpers ---*
- `hexToBytes` (line 69)
- `bytesToHex` (line 78)
- `bytesToBase64` (line 84)
- `bytesToBase32` (line 95)
- `base64ToBytes` (line 113)
- `bytesToBigInt` (line 120)
- `i2osp` (line 127)
- `mod` (line 137)
- `modPow` (line 141)
- `randomBytes` (line 159)
- `H` (line 168)
- `Hint` (line 172)
- `deriveKeyFromPassphrase` (line 184) - *Derive a 256-bit key from a passphrase with a caller-chosen PBKDF2 iteration count. This is the single PBKDF2 implementation in the client; deriveMasterKey pins it to the account-password iteration count, while the deniable vault (qv-deniable.js) drives it with the server-advertised count so a policy change needs no client edit.*
- `deriveMasterKey` (line 205)
- `aesGcmEncrypt` (line 209)
- `aesGcmDecrypt` (line 220)
- `computeK` (line 250) - *-- SRP-6a (QV-SRP-1), mirrors utils/srp6a.py ---*
- `deriveVerifier` (line 255)
- `srpLogin` (line 263) - *Run a full SRP-6a login against the server, verifying the server proof M2.*
- `generateIdentity` (line 315)
- `parsePublicKey` (line 343)
- `parsePrivateBlob` (line 351)
- `deriveWrapKey` (line 359)
- `wrapKey` (line 371) - *Seal a file encryption key to a recipient's hybrid public key.*
- `unwrapKey` (line 395) - *Recover a file encryption key using the recipient's hybrid private blob.*
- `generateRecoveryCode` (line 417) - *Generate a QV-RECOVERY-1 code: 20 random bytes (160 bits) Base32-encoded (RFC 4648, no padding) and grouped as XXXX-XXXX-... for readability.*
- `normalizeRecoveryCode` (line 428) - *Normalize a user-entered recovery code: strip surrounding whitespace, remove group separators, and uppercase, so "abcd-efgh" and "ABCDEFGH"*
- `wrapPrivateKeyForRecovery` (line 436) - *Re-wrap an existing privateBlob under a key derived from a recovery code, using the same PBKDF2-SHA256 + AES-256-GCM scheme as the password path, with its own independent salt.*
- `derivePublicKeyFromPrivateBlob` (line 455) - *Reconstruct the public key (the same {v, mlkem, x} structure produced by generateIdentity) from a decrypted privateBlob. The noble ML-KEM-768 secretKey is encoded as [innerSK(1152) | publicKey(1184) | H(pk)(32) | z(32)], so the public key is recoverable directly; the X25519 public key is derived from its secret via x25519.getPublicKey. Used as a proof-of-possession when resetting credentials with a recovery code: the server accepts the reset only if this matches the stored public_key.*
- `postJson` (line 473)
- `buildRegistration` (line 496) - *Build the zero-knowledge registration payload entirely in the browser.  Returns `{ payload, recoveryCode }`: `payload` is the JSON body to POST to the registration endpoint (it includes the recovery-code-wrapped private key, but never the recovery code itself), and `recoveryCode` is the plaintext QV-RECOVERY-1 code to show the user exactly once. The server never sees `recoveryCode`.*
- `register` (line 530)
- `recoverAccount` (line 541) - *Reset SRP credentials and the password-encrypted private key using a QV-RECOVERY-1 recovery code, without ever exposing the user's keypair to the server. Fetches the recovery-wrapped privateBlob, decrypts it locally with a key derived from the recovery code, proves possession of the resulting keypair by reconstructing its public key, and re-wraps the same privateBlob under the new password.*
- `login` (line 592)
- `encryptAndUpload` (line 599) - *Generate a fresh file key, encrypt the padded file, wrap the key, and upload. The file plaintext is padded to a fixed file bucket before AES-GCM so the ciphertext length reveals only the bucket, not the exact file size.*
- `downloadAndDecrypt` (line 629) - *Download an encrypted file and its key, then decrypt it in the browser.*
- `fetchPublicKey` (line 668) - *Fetch a user's hybrid public key so the browser can wrap content to them.*
- `sendSecureMessage` (line 683) - *Encrypt a message to a recipient (keeping a sender-readable outbox copy) and POST the opaque envelope. The plaintext and the CEK never leave the browser; the server stores only ciphertext and wrapped keys.*
- `decryptInbox` (line 714) - *Decrypt a batch of inbox envelopes with the user's password. The master key and private blob are derived once and reused, so this stays cheap even for a full mailbox. Returns one result per envelope; a record that cannot be decrypted is reported with ``ok: false`` rather than aborting the batch.*

#### `qv-deniable.js`
**Path:** `static/js/qv-deniable.js`
**File Doc:** *QuantumVault deniable vault (QV-DENIABLE-1) browser crypto.  A deniable vault is an opaque container with a fixed number of slots. Each slot is independently encrypted under a key derived from its own passphrase; only the slot whose passphrase the user enters will authenticate and decrypt. The container is built and opened entirely in the browser. The server stores only the opaque envelope and never sees a passphrase or a plaintext.  Deniability rests on two invariants enforced here and re-checked on the server (controllers/deniable_vault.py):  1. Every container has exactly `slot_count` slots. A container that hides data is structurally identical to one that does not. 2. Every slot's plaintext is padded to the same length before encryption, so every slot's ciphertext is the same length. The byte sizes reveal nothing about which slot, if any, holds real data.  When the user configures no hidden vault, the hidden slot is filled with random bytes under a random, discarded key. It is then indistinguishable from a slot that holds real data the user is simply declining to open.*

**Functions:**
- `toBytes` (line 47)
- `frame` (line 55) - *Frame a payload as [len(4) | payload | random padding] of exactly `paddedLength` bytes. `paddedLength` is shared by every slot so the*
- `unframe` (line 64)
- `sealSlot` (line 82) - *Encrypt one slot's framed plaintext under a passphrase, returning the {salt, nonce, ct} object the envelope stores.*
- `openSlot` (line 102) - *Attempt to open one slot with a passphrase. Returns the payload bytes on success or null when the passphrase does not authenticate this slot.*
- `buildDeniableVault` (line 125) - *Build a deniable container from a list of slot specifications.  `slots` is an array of `{ passphrase, data }`; `data` may be a string or a Uint8Array. The array is padded out to `parameters.slot_count` entries with random, unopenable slots so the container always has the fixed slot count. Every slot's plaintext is padded to `parameters.slot_plaintext_bytes`, so every container is exactly the same size regardless of how much data it holds. Throws if more slots are supplied than allowed, or if any slot's data does not fit the fixed slot size.*
- `openDeniableVault` (line 170) - *Open a container with a passphrase. Tries every slot; only the slot whose passphrase matches will authenticate. Returns `{ index, data, text }` for the opened slot, or throws if no slot opens.*

#### `qv-padding.js`
**Path:** `static/js/qv-padding.js`
**File Doc:** *QuantumVault fixed-bucket padding (QV-PAD-1), browser mirror of utils/padding.py.  Every plaintext is framed as [len(4 BE) | plaintext | fresh random pad] up to its bucket before AES-GCM. Buckets must stay identical to the server table: an envelope whose ciphertext length is not bucket+GCM overhead is rejected by the server. Pad bytes come from crypto.getRandomValues on every call and are never cached or reused; only the immutable bucket tables below are long-lived.*

**Functions:**
- `tableFor` (line 15)
- `bucketFor` (line 20)
- `randomPad` (line 33)
- `padFramed` (line 42)
- `unframeFramed` (line 54)

#### `recover.js`
**Path:** `static/js/recover.js`
**File Doc:** *Account recovery page controller (QV-RECOVERY-1 flow).  Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts and inline event handlers. recoverAccount() in qv-crypto.js fetches the account's recovery bundle, decrypts the private key blob entirely in the browser using a key derived from the recovery code, and re-wraps it under the new password. The recovery code and the new password never leave the browser.*

**Functions:**
- `setStatus` (line 14)
- `handleRecover` (line 22)
- `init` (line 79)

#### `register.js`
**Path:** `static/js/register.js`
**File Doc:** *Registration page controller (zero-knowledge flow).  This module is loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts and inline event handlers. It reads the profile from the form, runs the browser-side crypto in qv-crypto.js, and POSTs only opaque zero-knowledge material to the server. The password and the private key never leave the browser.*

**Functions:**
- `showRecoveryCode` (line 16) - *Display the one-time QV-RECOVERY-1 code in a modal and wait for the user to acknowledge they have saved it before continuing. The code is shown*
- `handleRegister` (line 42)
- `init` (line 109)

#### `upload.js`
**Path:** `static/js/upload.js`
**File Doc:** *Upload page controller (zero-knowledge file storage).  Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'). The browser derives a fresh file key, encrypts the file with AES-256-GCM, and wraps the key to the user's hybrid public key. Downloads are decrypted locally after prompting for the password. The server never sees plaintext, the file key, or the password.*

**Functions:**
- `getCsrfToken` (line 11)
- `getUsername` (line 16)
- `getPublicKey` (line 23)
- `handleUpload` (line 40)
- `handleDownload` (line 74)
- `init` (line 96)

### PY (70 files)

#### `__init__.py`
**Path:** `__init__.py`

*No symbols extracted*

#### `app.py`
**Path:** `app.py`
**File Doc:** *Local development entry point.  This script exists for the ``make run`` workflow: the Werkzeug dev server with SSL on the loopback port. It is the only place in the codebase where the dev server is started. Production deployments use ``wsgi.py`` and gunicorn instead.  The Werkzeug interactive debugger is intentionally NOT enabled: even with ``FLASK_DEBUG=1`` we never want the debug PIN surface exposed on a network-reachable port. To get a debugger for local work, run the app under an IDE debugger against this file.*

**Functions:**
- `main` (line 21) `def main()`
- `_is_production_like` (line 58) `def _is_production_like()` - *Return True if the runtime looks like a public-facing deployment.

The heuristic is intentionally conservative: any deployment with a
non-loopback bind address is treated as production. The Werkzeug
debugger is forbidden on those binds.*

#### `app_factory.py`
**Path:** `app_factory.py`
**File Doc:** *Application factory for QuantumVault.  The same ``create_app()`` callable powers:  - ``app.py`` (dev: ``flask run`` or Werkzeug's dev server with debug) - ``wsgi.py`` (prod: gunicorn / uWSGI behind a reverse proxy)  The factory enforces three things that the old ``app.py``-as-script pattern could not:  1. No Werkzeug debug PIN is ever exposed. Debug mode is gated on the ``FLASK_DEBUG`` environment variable and the Werkzeug debugger is disabled regardless. 2. Security headers (CSP, HSTS, X-Frame-Options, etc.) are installed via Flask-Talisman in production. The strict policy is the default; tests can override ``security_overrides`` to relax specific headers. 3. The session cookie is hardened: HttpOnly, SameSite=Lax, Secure when the request is HTTPS. ``PERMANENT_SESSION_LIFETIME`` caps the idle/absolute lifetime so an unattended browser does not retain auth indefinitely.  Keeping every global side-effect (``app.config[...]``, blueprint registration, extension init) inside the factory means importing ``quantumvault.app_factory`` is free of side effects. That property matters because ``gunicorn`` forks workers and a top-level ``app = create_app()`` in a module would import-time-bind the app to the parent process and re-execute initialization in each worker.*

**Functions:**
- `_is_production` (line 71) `def _is_production()` - *Return True unless the operator explicitly opts into dev mode.*
- `_build_csp` (line 82) `def _build_csp()` - *Return the strict Content-Security-Policy used in production.

The policy allows:

- ``'self'`` for everything by default
- the JSDelivr CDN pinned to the specific packages the SPA needs
  (Bootstrap CSS, EasyMDE CSS/JS, marked) and the cdnjs CDN pinned to
  the legacy pages that need it (crypto-js, jsencrypt). Every remote
  asset is loaded with SRI from the manifest, so a compromised CDN
  cannot execute swapped bytes.
- ``'unsafe-inline'`` for styles is required because EasyMDE injects
  inline styles; for scripts it is forbidden.
- WebAssembly is allowed (``'wasm-unsafe-eval'``) so the client can
  later compile liboqs-portable to WASM and avoid pure-JS PQ.

Adding a new third-party origin to this list is a security review
gate. Do not add origins without updating docs/SECURITY_TODO.md.*
- `_build_talisman_kwargs` (line 119) `def _build_talisman_kwargs()` - *Return kwargs to pass to ``Talisman`` based on the runtime env.*
- `_configure_secret_key` (line 160) `def _configure_secret_key(app, config)` - *Set ``app.config['SECRET_KEY']`` from env, payload.json, or a random value.

The previous code set a fresh 24-byte hex on every process start.
That is correct for development (sessions reset, no surprises) but
in production the operator MUST set ``FLASK_SECRET_KEY`` (or
``SECRET_KEY``) to a stable, 32+ byte value. Otherwise every
gunicorn worker restart invalidates every session, including
CSRF tokens, and the audit log will show a flood of CSRF rejections.

For backward compatibility, ``payload.json``'s ``SECRET_KEY`` is
accepted as a third source so a project that was bootstrapped by
``make env`` keeps working without a code change. The env var
always wins over ``payload.json`` so an operator can override.*
- `_configure_session` (line 203) `def _configure_session(app)` - *Apply session lifetime and cookie hardening.

The defaults are deliberately conservative:

- 8 hours of permanent session lifetime (then user must re-login)
- 30 minutes of idle lifetime (rolling refresh on every request)
- Cookies are HttpOnly, SameSite=Lax, and Secure in production*
- `_configure_logging` (line 220) `def _configure_logging(app)` - *Wire up a structured application logger.

The Werkzeug access log goes through Flask's default handler at
INFO. Application errors use the standard ``app.logger``. The
audit logger (``quantumvault.audit``) is configured separately in
:mod:`utils.security` and writes one-line JSON to stdout.*
- `create_app` (line 237) `def create_app(config_overrides, security_overrides)` - *Build and return a fully-configured Flask application.

Args:
    config_overrides: Values to merge into ``app.config`` after
        defaults are applied. Useful for tests that need to swap
        the database path or disable the rate limiter.
    security_overrides: Values to merge into the Talisman kwargs.
        Used by tests to disable CSP and the HTTPS redirect without
        forking the whole factory.

Returns:
    A Flask application ready to be served by gunicorn or the
    Werkzeug dev server.*
- `load_user` (line 416) `def load_user(user_id)`

#### `client.py`
**Path:** `client.py`

*No symbols extracted*

#### `__init__.py`
**Path:** `controllers/__init__.py`

*No symbols extracted*

#### `auth.py`
**Path:** `controllers/auth.py`
**File Doc:** *Zero-knowledge authentication controller for QuantumVault.  Registration accepts cryptographic material that the browser generated and stores it verbatim: the SRP salt and verifier, the user's public key, the password-encrypted private key blob, and the KDF salt. The server never sees the password or any private key. Login is a Secure Remote Password (SRP-6a) challenge/response (see :mod:`utils.srp6a`) so the password is never transmitted.  Phone verification codes, MFA codes, and recovery codes are never stored in plaintext. They are hashed with a server-side pepper via :func:`utils.security.hash_secret` so a database leak does not hand the attacker ready-to-use codes.*

**Classes:**
- `AuthController` (line 58) `class AuthController` - *Handles zero-knowledge registration and SRP-6a authentication.*

**Functions:**
- `_now_utc` (line 49) `def _now_utc()` - *Return the current time as a timezone-aware UTC datetime.

Avoids the deprecated ``datetime.utcnow()`` which returns a naive
value and triggers a DeprecationWarning in Python 3.12+.*

**Methods:**
- `__init__` (line 61) `def __init__(self, db_path, mail, storage_uri)` - *Initialize the controller.

Args:
    db_path: Path to the SQLite user database.
    mail: Configured Flask-Mail instance for transactional email.
    storage_uri: Redis URI backing the ephemeral SRP session store.*
- `register` (line 76) `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, recovery_salt, encrypted_private_key_recovery)` - *Register a user from client-generated zero-knowledge credentials.

Args:
    username: The desired unique username.
    srp_salt: SRP salt (hex) generated on the client.
    srp_verifier: SRP verifier (hex) generated on the client.
    public_key: The user's hybrid public key blob (opaque).
    encrypted_private_key: The password-encrypted private key blob (opaque).
    kdf_salt: Salt (hex) for the client-side key derivation function.
    email: The user's email address.
    phone: The user's phone number.
    first_name: The user's first name.
    last_name: The user's last name.
    recovery_salt: Optional QV-RECOVERY-1 PBKDF2 salt (hex), generated on the client.
    encrypted_private_key_recovery: Optional QV-RECOVERY-1 AES-256-GCM
        wrapping of the same private key blob, keyed by a
        client-generated recovery code instead of the password.

Returns:
    True on success, False if validation fails or persistence errors.*
- `send_confirmation_email` (line 156) `def send_confirmation_email(self, email, username, token)` - *Email the account-confirmation link to a freshly registered user.

The link targets :func:`views.auth.confirm_email`. When SMTP is not
configured, or the send fails, the link is logged at WARNING so an
operator can still verify the account from the server logs; this keeps
local and bare-VPS deployments usable before mail credentials exist.

Args:
    email: The recipient address.
    username: The account username (used for the greeting).
    token: The single-use confirmation token stored on the account.

Returns:
    True if the mail server accepted the message, False otherwise.*
- `srp_hello` (line 202) `def srp_hello(self, username, client_a_hex)` - *Begin an SRP-6a login and return the salt and server challenge B.*
- `srp_verify` (line 221) `def srp_verify(self, username, client_m1_hex)` - *Complete an SRP-6a login and return the authenticated user and proof.*
- `send_sms_verification` (line 253) `def send_sms_verification(self, phone, code, username)` - *Send a verification code via SMS.*
- `verify_phone_code` (line 274) `def verify_phone_code(self, username, code)` - *Verify a phone verification code for a user.

The stored value is the peppered hash; the supplied code is
hashed in the same way and the two digests are compared in
constant time.*
- `resend_phone_code` (line 310) `def resend_phone_code(self, username)` - *Issue and send a fresh phone verification code.

Generates a new one-time code, stores its peppered hash with a
30-minute expiry (overwriting any previous pending code), and
dispatches it by SMS. Returns False when the account is unknown,
has no phone number, is already verified, or the SMS provider is
not configured, so the caller can surface an honest result.

Args:
    username: The account requesting a new code.

Returns:
    True if a new code was generated, stored, and accepted by the
    SMS provider; False otherwise.*
- `_is_code_valid` (line 349) `def _is_code_valid(self, expires_at)` - *Return True if a verification code has not yet expired.*
- `verify_mfa_code` (line 369) `def verify_mfa_code(self, username, code)` - *Verify a multi-factor authentication code for a user.*
- `send_mfa_code` (line 393) `def send_mfa_code(self, username)` - *Generate, store, and send an MFA code to the user's phone.*
- `toggle_mfa` (line 416) `def toggle_mfa(self, username, enable)` - *Enable or disable MFA for a user.*

#### `contact.py`
**Path:** `controllers/contact.py`

**Classes:**
- `ContactController` (line 4) `class ContactController` - *Handles logic related to contact messages.*

**Methods:**
- `__init__` (line 6) `def __init__(self, db_path)` - *Initialize the ContactController with the database path.

Args:
    db_path (str): Path to the SQLite database file.*
- `create_contact` (line 14) `def create_contact(self, user_id, subject, message)` - *Create a new contact message.

Args:
    user_id (int): ID of the user sending the message.
    subject (str): Subject of the message.
    message (str): Content of the message.

Returns:
    bool: True if the message was created successfully, False otherwise.*
- `get_user_contacts` (line 36) `def get_user_contacts(self, user_id)` - *Retrieve all contact messages for a user.

Args:
    user_id (int): ID of the user.

Returns:
    list[ContactModel]: List of contact messages.*

#### `deniable_vault.py`
**Path:** `controllers/deniable_vault.py`
**File Doc:** *QV-DENIABLE-1 deniable vault: configuration, validation, orchestration.  This module is the server-side core of the deniable vault feature. It is strictly zero-knowledge: it validates the *structure* of the opaque container the browser produces, stores it, and serves it back. It never decrypts a slot, never sees a passphrase, and never learns which slot holds the decoy and which holds the hidden data.  Deniability requires that activation leaves no evidence. Two mechanisms provide that:  * Every account always has exactly one container of a fixed shape. The server can mint a well-formed *random* container itself, because the blob is opaque and AES-GCM ciphertext is indistinguishable from random. An unactivated account therefore looks identical to an activated one: "has a container" is universal and so reveals nothing. Activation only overwrites the random blob with one whose slots a passphrase can open. * Every container has the same byte size. Each slot's plaintext is padded to a fixed length, so every slot's ciphertext is the same length and every container is the same size, whether or not it hides data.  Three collaborators, each with a single responsibility:  * :class:`DeniableVaultConfig` is the immutable set of structural limits, sourced from the environment with safe defaults. Nothing about the envelope shape is hard-coded at a call site. * :class:`EnvelopeValidator` enforces those limits, including the fixed slot count and the fixed ciphertext length. * :class:`DeniableVaultController` wires the validator to :class:`models.deniable_vault.DeniableVaultDB`, provisions random*

**Classes:**
- `EnvelopeValidationError` (line 104) `class EnvelopeValidationError(ValueError)` - *Raised when an envelope violates a structural invariant.*
- `DeniableVaultConfig` (line 134) `class DeniableVaultConfig` - *Immutable structural limits for a deniable vault container.*
- `EnvelopeValidator` (line 272) `class EnvelopeValidator` - *Validate the structure of an opaque deniable vault envelope.

The validator never decrypts. It checks only the shape: the schema
version, the KDF identifier and iteration count, the exact slot count,
each slot's hex and base64 fields, and the fixed ciphertext length
that makes every container identical in size.*
- `DeniableVaultController` (line 393) `class DeniableVaultController` - *Coordinate validation, provisioning, persistence, and auditing.*

**Functions:**
- `_base64_length` (line 81) `def _base64_length(byte_length)` - *Return the length of the standard base64 encoding of ``byte_length`` bytes.*
- `canonical_json` (line 86) `def canonical_json(envelope)` - *Serialize an envelope deterministically for storage and sizing.

Keys are sorted and separators are compact so the same logical
envelope always serializes to the same bytes. Both the size check in
:class:`EnvelopeValidator` and the persistence path in
:class:`DeniableVaultController` use this single function, so the
bytes that are measured are exactly the bytes that are stored.

Args:
    envelope: The envelope mapping to serialize.

Returns:
    The canonical JSON string.*

**Methods:**
- `_coerce_int` (line 108) `def _coerce_int(value, default)` - *Return ``value`` coerced to int, falling back to ``default``.*
- `_coerce_kdf` (line 118) `def _coerce_kdf(value, default)` - *Return an allow-list of KDF identifiers from a value.

Accepts a comma-separated string (as found in environment variables)
or any iterable of strings.*
- `from_mapping` (line 148) `def from_mapping(cls, mapping, env)` - *Build a config from a mapping, with environment overrides.

Resolution order for every field is: environment variable, then
``mapping`` entry (e.g. ``app.config``), then the module default.
Defaults are intentionally not written to ``payload.json`` so the
repository carries no per-deployment hint that the feature exists;
an operator overrides them per-host via the environment.

Args:
    mapping: A mapping such as ``app.config``.
    env: Environment to read overrides from. Defaults to
        ``os.environ``; injectable for tests.

Returns:
    The resolved, immutable configuration.*
- `expected_ct_b64_length` (line 213) `def expected_ct_b64_length(self)` - *Return the exact base64 length every slot ciphertext must have.

A slot's ciphertext is the fixed plaintext length plus the GCM
tag, base64-encoded. Fixing it makes every container byte-for-byte
the same shape.*
- `random_container` (line 222) `def random_container(self)` - *Return a well-formed container filled with random, unopenable data.

Used to provision an account that has not activated the feature and
to reset one. The result is structurally indistinguishable from an
activated container: random hex salts and nonces, and random
base64 ciphertext of exactly the expected length. No passphrase can
open it, which is the correct behavior for an unactivated vault.

Returns:
    A fresh random envelope dict.*
- `public_parameters` (line 250) `def public_parameters(self)` - *Return the parameters the browser needs to build a container.

The browser reads these instead of hard-coding them, so a change
to the server policy propagates to clients without a code change.
The values are non-secret: they describe the container shape,
which is identical for every account.*
- `__init__` (line 281) `def __init__(self, config)` - *Bind the validator to a configuration.*
- `validate` (line 285) `def validate(self, envelope)` - *Validate ``envelope``, raising on the first violation.

Args:
    envelope: The decoded JSON envelope to validate.

Raises:
    EnvelopeValidationError: If any structural invariant is
        violated. The message names the violated invariant and
        never echoes ciphertext.*
- `_validate_slot` (line 339) `def _validate_slot(self, index, slot)` - *Validate a single slot.

Args:
    index: The slot's position, used only in error messages.
    slot: The slot mapping to validate.

Raises:
    EnvelopeValidationError: If the slot is malformed or its
        ciphertext is not the fixed expected length.*
- `_validate_hex` (line 376) `def _validate_hex(value, expected_length, index, field)` - *Validate that ``value`` is hex of exactly ``expected_length``.

Raises:
    EnvelopeValidationError: If the value is not a hex string of
        the expected length.*
- `__init__` (line 401) `def __init__(self, db, config, validator)` - *Initialize the controller.

Args:
    db: The opaque container store.
    config: The structural limits in force.
    validator: The validator to use. Defaults to one bound to
        ``config``; injectable for tests.*
- `load_or_provision` (line 419) `def load_or_provision(self, username)` - *Return ``username``'s container, minting a random one if absent.

The mint-on-read behavior is what makes "has a container"
universal: any account that has ever opened its settings has an
indistinguishable container, so the mere existence of one is not
evidence of a hidden vault.

Args:
    username: The owning account.

Returns:
    The decoded envelope, always present.*
- `save` (line 441) `def save(self, username, envelope)` - *Validate and persist a container for ``username``.

Args:
    username: The owning account.
    envelope: The decoded JSON envelope from the client.

Raises:
    EnvelopeValidationError: If the envelope is structurally
        invalid; nothing is persisted in that case.*
- `reset` (line 456) `def reset(self, username)` - *Overwrite ``username``'s container with a fresh random one.

Reset replaces rather than deletes: removing the row would leave a
gap that distinguishes a user who deactivated from one who never
activated. A random container keeps existence universal.

Args:
    username: The owning account.

Returns:
    The new random envelope.*
- `exists` (line 474) `def exists(self, username)` - *Return True if ``username`` already has a stored container.*
- `read` (line 171) `def read(key)`

#### `facade.py`
**Path:** `controllers/facade.py`
**File Doc:** *QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.  The facade hides QuantumVault behind an innocuous cover application. A secret phrase typed into the cover's search field is the first gate: a correct phrase issues a short-lived signed ticket and marks the session ``real`` or ``duress``; either way the ordinary login page is revealed, so an onlooker cannot tell which phrase was used.  This module is the server-side core. It never stores a phrase, never echoes one into the audit log, and performs the same Argon2id work for a miss, the real phrase, and the duress phrase so the response is not an oracle. The zero-knowledge guarantees of SRP-6a and the deniable vault do not depend on this layer.*

**Classes:**
- `GateOutcome` (line 63) `class GateOutcome(Enum)` - *Classification of a submitted gate phrase.*
- `GateDecision` (line 72) `class GateDecision` - *The outcome of evaluating a phrase plus any issued ticket.*
- `FacadeConfig` (line 124) `class FacadeConfig` - *Immutable facade configuration resolved from environment and app config.*
- `GatePhraseHasher` (line 262) `class GatePhraseHasher` - *Argon2id hashing and verification for a human-chosen gate phrase.*
- `GateTicket` (line 305) `class GateTicket` - *Short-lived signed ticket binding a session to a gate mode.*
- `FacadeGate` (line 336) `class FacadeGate` - *Evaluate gate phrases and issue tickets with constant observable work.*

**Methods:**
- `_as_bool` (line 79) `def _as_bool(value, default)` - *Coerce an environment or mapping value to a boolean.*
- `_as_int` (line 88) `def _as_int(value, default)` - *Coerce an environment or mapping value to an integer.*
- `_as_text` (line 98) `def _as_text(value, default)` - *Coerce a value to non-empty text, falling back to ``default``.*
- `_as_raw_text` (line 106) `def _as_raw_text(value, default)` - *Coerce a value to text without substituting an empty default.*
- `_as_paths` (line 111) `def _as_paths(value, default)` - *Parse a comma-separated path list into a tuple of stripped paths.*
- `gate_configured` (line 154) `def gate_configured(self)` - *Return whether the facade is enabled and holds a real gate hash.*
- `cover_context` (line 158) `def cover_context(self)` - *Return the cosmetic cover context, never carrying a gate hash.*
- `cover_variables` (line 166) `def cover_variables(self)` - *Return the sanitizable cover variable payload.*
- `from_mapping` (line 181) `def from_mapping(cls, mapping, env)` - *Resolve configuration with environment, mapping, then default order.*
- `__init__` (line 265) `def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)` - *Bind the hasher to explicit Argon2id cost parameters.*
- `hash` (line 282) `def hash(self, phrase)` - *Return a salted Argon2id digest of ``phrase``.*
- `verify` (line 286) `def verify(self, phrase, encoded)` - *Return whether ``phrase`` matches ``encoded`` without raising.*
- `from_config` (line 296) `def from_config(cls, config)` - *Build a hasher using the cost parameters of ``config``.*
- `__init__` (line 308) `def __init__(self, secret_key, ttl_seconds)` - *Bind the ticket signer to the app secret and a lifetime.*
- `issue` (line 316) `def issue(self, mode)` - *Return a signed ticket for ``mode`` or raise for an unknown mode.*
- `verify` (line 322) `def verify(self, token)` - *Return the ticket mode, or ``None`` if expired, tampered, or absent.*
- `__init__` (line 339) `def __init__(self, config, hasher, ticket)` - *Bind the gate to its configuration and collaborators.*
- `build` (line 351) `def build(cls, config, secret_key)` - *Build a gate from configuration and the application secret.*
- `evaluate` (line 359) `def evaluate(self, phrase)` - *Classify a phrase and emit only a generic audit event.*
- `read` (line 189) `def read(key)`

#### `file.py`
**Path:** `controllers/file.py`
**File Doc:** *Encrypted file persistence layer.  The server is intentionally blind to plaintext: it only ever stores opaque ciphertext plus an opaque "wrapped file encryption key" (``wrapped_fek``) produced by the browser. Every filename that flows through this controller is normalized via :func:`safe_filename` so the S3 key the user ends up with cannot contain path separators or control characters.*

**Classes:**
- `FileController` (line 51) `class FileController` - *Persistence for end-to-end encrypted files and their wrapped FEKs.*

**Functions:**
- `_log_s3_error` (line 28) `def _log_s3_error(operation, error)` - *Log a failed S3 operation without raising further.*
- `safe_filename` (line 33) `def safe_filename(name)` - *Return a filename safe to embed in an S3 key.

Applies :func:`werkzeug.utils.secure_filename` to strip any path
components and control characters, then rejects any residual
shell-meta characters and NUL bytes. Returns an empty string
for empty/None input.*

**Methods:**
- `__init__` (line 54) `def __init__(self, users_path, s3_bucket, s3_client)`
- `_key` (line 59) `def _key(self, username, filename, suffix)` - *Build the S3 key for a user's encrypted file or FEK.

The username is the server's truth (it came from the
authenticated session), so it does not need additional
validation. The filename is expected to have been normalized
via :func:`safe_filename` by the caller.*
- `get_storage_usage` (line 71) `def get_storage_usage(self, username)` - *Sum the bytes used by ``username``'s encrypted files in S3.*
- `upload_encrypted_file` (line 85) `def upload_encrypted_file(self, username, file_storage, wrapped_fek)` - *Persist an already-encrypted file and its wrapped FEK to S3.

The ciphertext must already be padded client-side to a configured
file bucket plus AES-256-GCM overhead. Unpadded uploads are
rejected so exact plaintext sizes never reach the wire or storage.*
- `get_encrypted_file_and_key` (line 118) `def get_encrypted_file_and_key(self, username, filename)` - *Fetch a user's encrypted file and its wrapped FEK from S3.

Returns:
    A 3-tuple of ``(ciphertext, wrapped_fek, error)``. On success
    ``error`` is ``None``; on failure it contains a human-readable
    reason and the byte values are ``None``.*
- `list_encrypted_files` (line 148) `def list_encrypted_files(self, username)` - *List the encrypted files that belong to ``username``.*

#### `message.py`
**Path:** `controllers/message.py`
**File Doc:** *Server-side controller for end-to-end encrypted messages.  The browser generates the CEK, encrypts the message with AES-256-GCM, and wraps the CEK with the recipient's and sender's hybrid public keys. The server stores only opaque material; it cannot derive plaintext or any key.*

**Classes:**
- `MessageController` (line 19) `class MessageController` - *Handles message persistence in the zero-knowledge flow.*

**Methods:**
- `__init__` (line 22) `def __init__(self, users_path, users_db_path)` - *Initialize the controller.

Args:
    users_path: Base directory under which each user has a
        ``messages/`` subdirectory.
    users_db_path: Path to the SQLite user database, used to verify
        that a message recipient is a registered account. Defaults
        to the configured database path when omitted.*
- `send_encrypted_message` (line 36) `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)` - *Persist an opaque message envelope for the recipient.

Args:
    sender: Sender's username.
    recipient: Recipient's username.
    encrypted_message_b64: AES-256-GCM ciphertext (base64) of the
        message body, with the IV prepended by the browser.
    cek_for_recipient: Hybrid-wrapped CEK to the recipient's public
        key (base64 JSON from qv-crypto).
    cek_for_sender: Hybrid-wrapped CEK to the sender's public key
        (so the outbox copy is readable).

Returns:
    True on success, False otherwise. Envelopes whose decoded
    ciphertext length is not a configured message bucket plus
    AES-256-GCM overhead are rejected so unpadded clients cannot
    leak exact plaintext sizes on the wire.*
- `get_messages` (line 90) `def get_messages(self, username, page, per_page)` - *Return opaque message envelopes for the user.

The browser unwraps each CEK with the user's private blob; the
server only returns the opaque envelopes.

Args:
    username: User whose mailbox to read.
    page: 1-indexed page number.
    per_page: Messages per page.

Returns:
    A tuple ``(messages, total_pages)`` of opaque messages.*

#### `secure_channel.py`
**Path:** `controllers/secure_channel.py`
**File Doc:** *QV-TUNNEL disposable secure channels over Cloudflare and Tor.  Inspiration comes from LazyOwn operator practice: a disposable ``cloudflared`` quick tunnel exposing a local port through a ``*.trycloudflare.com`` URL, and a disposable Tor onion service exposing the same port as a ``*.onion`` address. LazyOwn runs both with interactive prompts and host-wide side effects. This module replaces that workflow with an unprivileged deterministic supervisor suited to QuantumVault zero-trust operation.  Contract summary:  - Channel modes are ``disabled``, ``cloudflared``, ``tor``, and ``hybrid``. Hybrid runs both backends so traffic can use either path and rotation disposes both addresses at once. - Cloudflare uses ``cloudflared tunnel --url`` against loopback only. The origin scheme follows ``QV_CHANNEL_LOCAL_SCHEME`` (``http`` or ``https``): an ``https`` origin adds ``--no-tls-verify`` so a self-signed dev listener stays reachable instead of answering Bad Gateway. The public URL is parsed from process output with a closed allow-list pattern. No account token is required for quick tunnels and none is accepted here, which keeps rotation fully disposable. - Tor uses an unprivileged ``tor`` process with a generated data directory under the configured state directory. No system ``torrc`` file is modified and no sudo is required. The onion hostname is read from the disposable data directory. - State persists atomically as owner-only JSON. Audit records carry mode plus short fingerprints, never full URLs.*

**Classes:**
- `ChannelMode` (line 65) `class ChannelMode(Enum)` - *Selectable disposable channel mode.*
- `SecureChannelConfig` (line 116) `class SecureChannelConfig` - *Immutable secure channel configuration from env and mapping.*
- `ChannelStatus` (line 174) `class ChannelStatus` - *Point-in-time view of disposable channel state.*
- `SecureChannelManager` (line 220) `class SecureChannelManager` - *Supervise disposable Cloudflare and Tor backends.*

**Methods:**
- `is_cloudflare_url` (line 82) `def is_cloudflare_url(value)` - *Return whether value is a quick-tunnel HTTPS URL.*
- `is_onion_url` (line 89) `def is_onion_url(value)` - *Return whether value is a v3 onion HTTP address.*
- `_as_port` (line 96) `def _as_port(value, default)` - *Coerce input to a TCP port, falling back on default.*
- `_as_scheme` (line 107) `def _as_scheme(value, default)` - *Coerce input to an origin scheme, accepting http or https only.*
- `_default_launcher` (line 193) `def _default_launcher(cmd, log_path)` - *Spawn a backend daemon detached from the web worker.*
- `_default_killer` (line 207) `def _default_killer(pid)` - *Terminate one tracked backend process group.*
- `_fingerprint` (line 503) `def _fingerprint(value)` - *Return a short non-reversible fingerprint for audit records.*
- `_normalize_onion` (line 509) `def _normalize_onion(raw)` - *Normalize a Tor hostname file payload to a full onion URL.*
- `_wait_for_pattern` (line 517) `def _wait_for_pattern(path, pattern, timeout_seconds)` - *Poll a log file for the first regex match within a timeout.*
- `_wait_for_file` (line 535) `def _wait_for_file(path, timeout_seconds)` - *Poll for a small text file such as the onion hostname file.*
- `parse` (line 74) `def parse(cls, raw)` - *Parse free-form input into a mode, defaulting to disabled.*
- `configured` (line 129) `def configured(self)` - *Return whether a disposible channel mode is selected.*
- `from_mapping` (line 134) `def from_mapping(cls, mapping, env)` - *Resolve configuration with environment, mapping, then default order.*
- `active` (line 184) `def active(self)` - *Return whether any backend address is currently published.*
- `__init__` (line 223) `def __init__(self, state_dir, local_port, local_scheme, cloudflared_bin, tor_bin, start_timeout_seconds, launcher, killer)` - *Bind the manager to a state directory and backend binaries.*
- `origin_url` (line 247) `def origin_url(self)` - *Return the loopback origin URL both backends forward to.*
- `from_config` (line 252) `def from_config(cls, config, launcher, killer)` - *Build a manager sharing binary paths and ports with config.*
- `status` (line 270) `def status(self)` - *Return live status, pruning dead pids without side effects.*
- `start` (line 281) `def start(self, mode)` - *Start backends for mode, replacing any running channel.*
- `stop` (line 301) `def stop(self)` - *Terminate tracked backends and remove persisted state.*
- `rotate` (line 314) `def rotate(self)` - *Dispose current addresses and start the same mode again.*
- `audit_details` (line 321) `def audit_details(self, action, mode, cloud_url, onion_url)` - *Return an audit-safe detail string without full addresses.*
- `_status_for` (line 337) `def _status_for(self, mode, cloud_url, onion_url, pids)` - *Build a status after validating backend address shapes.*
- `_state_path` (line 352) `def _state_path(self)` - *Return the persisted state file path.*
- `_read_state` (line 356) `def _read_state(self)` - *Load persisted state, returning None when absent or corrupt.*
- `_write_state` (line 371) `def _write_state(self, current)` - *Persist state atomically with owner-only permissions.*
- `_remove_state` (line 396) `def _remove_state(self)` - *Remove persisted state when present.*
- `_cleanup_scratch` (line 405) `def _cleanup_scratch(self)` - *Remove stale per-boot scratch directories left by Tor.*
- `_start_cloudflared` (line 418) `def _start_cloudflared(self)` - *Launch a disposable quick tunnel and parse its public URL.*
- `_start_tor` (line 438) `def _start_tor(self)` - *Launch an unprivileged disposable onion service.*
- `_resolve_binary` (line 471) `def _resolve_binary(self, binary)` - *Resolve a backend binary without trusting PATH alone.*
- `_pid_live` (line 488) `def _pid_live(self, pid)` - *Return whether a tracked pid still exists.*
- `read` (line 142) `def read(key)`

#### `sync.py`
**Path:** `controllers/sync.py`
**File Doc:** *controllers/sync.py*

**Classes:**
- `SyncController` (line 7) `class SyncController`

**Methods:**
- `__init__` (line 8) `def __init__(self, users_path, s3_bucket, s3_client, file_controller)`
- `get_storage_usage` (line 14) `def get_storage_usage(self, username)` - *Calcula el uso de almacenamiento del usuario en S3.*

#### `enc_dec.py`
**Path:** `enc_dec.py`
**File Doc:** *Offline admin tool for ML-KEM-512 key-wrap encryption (QuantumVault).  WARNING -------- This script is **not** part of the zero-knowledge user trust path. It is an operator-only CLI used to retroactively wrap/unwrap files that were uploaded before the browser-based hybrid ML-KEM-768 + X25519 KEM replaced this flow. Do not call it from any user-facing route. The browser does the encryption for regular users; the server never sees plaintext passwords or private keys.  The script reads the object-storage endpoint (Garage / S3) from the environment:  S3_ENDPOINT_URL   - http://localhost:3900 for local Garage S3_ACCESS_KEY     - scoped Garage key S3_SECRET_KEY     - scoped Garage secret S3_REGION         - S3 region name (default: garage) S3_BUCKET         - bucket name (default: quantumvault)  When ``S3_ENDPOINT_URL`` is unset, the script falls back to plain AWS S3 using the ambient AWS credentials chain. The ``--aws-region`` flag overrides ``S3_REGION`` for a single invocation.*

**Functions:**
- `derive_aes_key` (line 36) `def derive_aes_key(shared_secret)` - *Derive a 32-byte AES key from an ML-KEM shared secret.

Args:
    shared_secret: The raw shared secret bytes from ``KeyEncapsulation``.

Returns:
    A 32-byte AES-256 key suitable for use with :class:`AESGCM`.*
- `encrypt_file_in_memory` (line 49) `def encrypt_file_in_memory(data, aes_key)` - *Encrypt ``data`` in memory with AES-256-GCM and return nonce + ciphertext.

Args:
    data: The plaintext bytes to encrypt.
    aes_key: The 32-byte AES key.

Returns:
    A tuple ``(nonce, ciphertext)`` where ``nonce`` is 12 random bytes.*
- `decrypt_file_in_memory` (line 65) `def decrypt_file_in_memory(nonce, ciphertext, aes_key)` - *Decrypt ``ciphertext`` in memory with AES-256-GCM and return the plaintext.

Args:
    nonce: The 12-byte nonce from the encrypt step.
    ciphertext: The encrypted bytes.
    aes_key: The 32-byte AES key.

Returns:
    The original plaintext bytes.*
- `_build_s3_client` (line 81) `def _build_s3_client(region)` - *Build a boto3 S3 client honoring the zero-trust environment convention.

Args:
    region: The region name (overrides ``S3_REGION`` for this call).

Returns:
    A configured ``boto3.client('s3')`` instance.*
- `main` (line 103) `def main()` - *Run the offline admin CLI (encrypt or decrypt a single object).*

#### `__init__.py`
**Path:** `models/__init__.py`

*No symbols extracted*

#### `contact.py`
**Path:** `models/contact.py`

**Classes:**
- `ContactModel` (line 8) `class ContactModel(BaseModel)` - *Pydantic model for a contact message.

Attributes:
    id: Unique contact ID.
    user_id: ID of the user who sent the message.
    subject: Subject of the contact message.
    message: Content of the contact message.
    created_at: Timestamp when the message was created.
    status: Status of the message (e.g. 'pending', 'resolved').*
- `ContactDB` (line 26) `class ContactDB` - *Database operations for contact messages.*

**Methods:**
- `__init__` (line 29) `def __init__(self, db_path)` - *Initialize the ContactDB with the database path.

Args:
    db_path: Path to the SQLite database file.*
- `_init_db` (line 38) `def _init_db(self)` - *Initialize the contacts table with all required fields.*
- `create_contact` (line 52) `def create_contact(self, user_id, subject, message)` - *Create a new contact message.

Args:
    user_id: ID of the user sending the message.
    subject: Subject of the message.
    message: Content of the message.

Returns:
    True on success, False if validation fails or the DB write fails.*
- `get_user_contacts` (line 89) `def get_user_contacts(self, user_id)` - *Retrieve all contact messages for a user.

Args:
    user_id: ID of the user.

Returns:
    List of contact message dictionaries, newest first. On DB
    error, returns an empty list and logs the failure.*
- `_convert_row_to_dict` (line 115) `def _convert_row_to_dict(self, row)` - *Convert an SQLite row to a dictionary.

Args:
    row: SQLite row.

Returns:
    Contact data as a dictionary.*
- `get_all_contacts` (line 139) `def get_all_contacts(self, page, per_page)` - *Retrieve all contact messages with pagination.

Args:
    page: 1-based page number.
    per_page: Number of contacts per page.

Returns:
    ``(rows, total_count)``. ``rows`` may be empty on DB error.*
- `_convert_row_to_dict_with_username` (line 168) `def _convert_row_to_dict_with_username(self, row)` - *Convert an SQLite row to a dictionary, including username.*

#### `deniable_vault.py`
**Path:** `models/deniable_vault.py`
**File Doc:** *Opaque storage for QV-DENIABLE-1 deniable vault containers.  The server is zero-knowledge: it stores one opaque, client-encrypted container per user and never derives, decrypts, or inspects the plaintext. A container is the JSON envelope produced by the browser (see ``static/js/qv-deniable.js``); from the database's point of view it is just text.  The table is deliberately minimal. It carries only what the server must hold to serve the container back and to bound storage:  * ``username`` (primary key) links the row to the owning account. * ``envelope`` is the opaque container text. * ``updated_at`` records when the row last changed, for operator housekeeping. No per-slot metadata is stored, because storing anything that distinguished one slot from another would undermine the deniability guarantee the feature exists to provide.  It lives in the same SQLite file as ``users`` so an operator backup or restore captures identity and vault state together.*

**Classes:**
- `DeniableVaultDB` (line 30) `class DeniableVaultDB` - *Persistence for per-user opaque deniable vault containers.*

**Methods:**
- `__init__` (line 33) `def __init__(self, db_path)` - *Initialize the store and ensure its table exists.

Args:
    db_path: Path to the SQLite database file, shared with
        :class:`models.user.UserDB`.*
- `_init_db` (line 43) `def _init_db(self)` - *Create the ``deniable_vaults`` table on first use.*
- `upsert` (line 57) `def upsert(self, username, envelope)` - *Insert or replace the container for ``username``.

The whole container is replaced atomically: a deniable vault has
no partial state, so a replace is always a full rewrite of the
opaque envelope.

Args:
    username: The owning account's username.
    envelope: The opaque container text to store verbatim.*
- `get` (line 82) `def get(self, username)` - *Return the stored container for ``username``, or ``None``.

Args:
    username: The account to look up.

Returns:
    A dict with ``username``, ``envelope``, and ``updated_at``,
    or ``None`` when the account has no container.*
- `exists` (line 101) `def exists(self, username)` - *Return True if ``username`` has a stored container.*

#### `message.py`
**Path:** `models/message.py`
**File Doc:** *Persistence layer for end-to-end encrypted messages.  The browser performs all cryptography: it generates a random 32-byte content encryption key (CEK), encrypts the message with AES-256-GCM, and wraps the CEK to the recipient's hybrid public key (and to the sender for the outbox copy). The server stores only opaque ciphertext + wrapped keys; it never sees plaintext or can derive the message.  The on-disk format is a tiny key-value file per message::  <sender>|<encrypted_message_b64>|<cek_for_recipient_b64>|<cek_for_sender_b64>|<iso_timestamp>  The actual decryption happens in the browser via ``static/js/qv-crypto.js`` -- the page that lists messages fetches each opaque record and unwraps the CEK with the recipient's private blob.*

**Classes:**
- `MessageModel` (line 27) `class MessageModel(BaseModel)` - *Pydantic model for a stored message envelope.

Attributes:
    id (Optional[str]): Message ID.
    sender (str): Sender username.
    message (str): Display text. With ZK messages this is the opaque
        payload returned to the client (the browser decrypts it).
    timestamp (Optional[datetime]): When the message was stored.*
- `MessageDB` (line 43) `class MessageDB` - *File-based operations for end-to-end encrypted messages.*

**Methods:**
- `__init__` (line 46) `def __init__(self, base_path)` - *Initialize the MessageDB with the base directory for per-user mailboxes.

Args:
    base_path (str): Filesystem path under which each user has a
        ``messages/`` subdirectory.*
- `save_message` (line 55) `def save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)` - *Persist an opaque message envelope for the recipient.

Args:
    recipient (str): Recipient username.
    sender (str): Sender username.
    encrypted_message_b64 (str): AES-256-GCM(CEK, plaintext) as base64
        (IV prepended by the browser).
    cek_for_recipient (str): Hybrid-wrapped CEK to the recipient's
        public key (base64-encoded JSON from qv-crypto).
    cek_for_sender (str): Hybrid-wrapped CEK to the sender's public
        key (so the outbox copy is readable).
    message_id (str): Unique message ID.*
- `get_messages` (line 87) `def get_messages(self, recipient, page, per_page)` - *Return opaque message envelopes for the recipient.

The browser unwraps the CEK with the user's private blob. This
method never derives any key material.

Args:
    recipient (str): Username whose mailbox to read.
    page (int): 1-indexed page number.
    per_page (int): Messages per page.

Returns:
    A tuple ``(messages, total_pages)`` where each message is
    opaque; the ``message`` field carries the JSON envelope
    ``{encrypted_message_b64, cek_for_recipient, cek_for_sender}``
    so the browser can decrypt it.*
- `delete_old_messages` (line 172) `def delete_old_messages(self, recipient, days)` - *Delete messages older than ``days`` days from the recipient's mailbox.

Args:
    recipient (str): Username whose mailbox to prune.
    days (int): Age threshold in days; older messages are removed.*

#### `plans.py`
**Path:** `models/plans.py`

**Classes:**
- `PlanDB` (line 4) `class PlanDB` - *Database operations for subscription plans.*

**Methods:**
- `__init__` (line 6) `def __init__(self, db_path)` - *Initialize the PlanDB with the database path.

Args:
    db_path (str): Path to the SQLite database file.*
- `_init_db` (line 15) `def _init_db(self)` - *Initialize the plans table with required fields.*
- `get_plan` (line 37) `def get_plan(self, plan_name)` - *Retrieve a plan by name.

Args:
    plan_name (str): Name of the plan to search for.

Returns:
    Optional[Dict]: Plan data as a dictionary or None if not found.*
- `get_all_plans` (line 50) `def get_all_plans(self)` - *Retrieve all plans.

Returns:
    List[Dict]: List of dictionaries containing plan data.*
- `create_plan` (line 60) `def create_plan(self, name, storage_quota, trial_days, price)` - *Create a new plan.

Args:
    name (str): Name of the plan.
    storage_quota (int): Storage quota in bytes.
    trial_days (int): Number of trial days.
    price (float): Price of the plan.*
- `update_plan` (line 78) `def update_plan(self, name, storage_quota, trial_days, price)` - *Update an existing plan.

Args:
    name (str): Name of the plan to update.
    storage_quota (Optional[int]): New storage quota in bytes.
    trial_days (Optional[int]): New number of trial days.
    price (Optional[float]): New price of the plan.*
- `delete_plan` (line 113) `def delete_plan(self, name)` - *Delete a plan by name.

Args:
    name (str): Name of the plan to delete.*
- `_convert_row_to_dict` (line 127) `def _convert_row_to_dict(self, row)` - *Convert an SQLite row to a dictionary.*
- `validate_plan_payment` (line 139) `def validate_plan_payment(self, plan_name, amount_paid)` - *Validate that the paid amount matches the plan price.

Args:
    plan_name (str): Name of the plan.
    amount_paid (float): Amount paid.

Returns:
    bool: True if the amount matches the plan price within tolerance.*

#### `superadmin_audit.py`
**Path:** `models/superadmin_audit.py`
**File Doc:** *Append-only audit log for superadmin actions.  Why a separate table: every privileged action (MFA reset, confirmation token re-issue, account suspension) needs an immutable record of who did what to which user, from which IP, and when. Mixing this into the ``users`` table is wrong on two counts:  1. The audit row is written by the superadmin, not the affected user. Adding ``last_reset_by`` / ``last_reset_at`` columns to ``users`` would let an attacker who pwns the DB forge the trail.  2. Audit history is monotonic: an entry must never be UPDATEd or DELETEd. SQLite has no row-level immutability, but a dedicated table with no application code path that writes UPDATEs is the closest we can get.  The table lives in ``instance/users.db`` (same file as ``users``) to keep operator backup / restore symmetric: one file = one snapshot of identity state. Storage is bounded by the operational tempo of the superadmin role, not user activity, so growth is negligible.  Rows are never pruned by the application. If a future retention policy is needed it should be a documented operator script, not a silent DELETE in the request path.*

**Classes:**
- `SuperadminAuditDB` (line 32) `class SuperadminAuditDB` - *Database operations for the superadmin audit log.*

**Methods:**
- `__init__` (line 35) `def __init__(self, db_path)` - *Initialize the audit log and ensure its table exists.

Args:
    db_path: Path to the SQLite database file (shared with
        ``UserDB`` so the two are backed up together).*
- `_init_db` (line 45) `def _init_db(self)` - *Create the audit table on first use; no-op if it already exists.*
- `record` (line 75) `def record(self, actor, action, target_user, ip, details)` - *Append one audit row and return its id.

The timestamp is generated server-side in UTC so two operators
in different timezones can correlate a single incident. The
return value is the new row's primary key, useful for tests
and for linking related log lines in the response.

Args:
    actor: Username of the superadmin performing the action.
    action: Short verb-noun identifier (e.g. ``reset_mfa``,
        ``resend_confirmation``, ``toggle_suspend``).
    target_user: Username the action was applied to, or None
        for global actions (none today, kept for future use).
    ip: Remote address that issued the request. ``None`` when
        the request did not carry one (e.g. background job).
    details: Free-text context, kept short. Use it for the
        state transition (e.g. ``active->inactive``) not for
        payloads that should never leave the audit log.

Returns:
    The new row's ``id``.*
- `recent` (line 119) `def recent(self, limit)` - *Return the most recent ``limit`` audit rows, newest first.

Args:
    limit: Maximum rows to return. Capped at 500 to bound
        template rendering cost on a noisy superadmin.

Returns:
    List of dicts with keys ``id``, ``ts``, ``actor``,
    ``action``, ``target_user``, ``ip``, ``details``.*

#### `user.py`
**Path:** `models/user.py`

**Classes:**
- `UserModel` (line 8) `class UserModel(BaseModel, UserMixin)` - *Pydantic model for a user with Flask-Login support.

Attributes:
    id: Unique user ID.
    username: Unique username.
    role: User role (free, bronze, silver, gold, admin, superadmin).
    email: User's email address.
    phone: User's phone number.
    first_name: User's first name.
    last_name: User's last name.
    storage_quota: Storage quota in bytes.
    trial_start: Trial period start date.
    trial_end: Trial period end date.
    subscription_status: Subscription status (active, inactive).
    email_verified: Whether the email is verified.
    confirmation_token: Email confirmation token.
    phone_verified: Whether the phone number is verified.
    phone_verification_code_hash: Peppered hash of the phone verification code.
    phone_code_expires: Phone verification code expiration.
    mfa_code_hash: Peppered hash of the current MFA code.
    mfa_code_expires: MFA code expiration.
    mfa_enabled: Whether MFA is enabled for the user.*
- `UserDB` (line 83) `class UserDB` - *Database operations for users.*

**Methods:**
- `get_id` (line 52) `def get_id(self)` - *Return the user ID as a string (required by Flask-Login).

Returns:
    str: The user ID as a string, or an empty string when the
        user is anonymous.*
- `is_active` (line 70) `def is_active(self)` - *Return True while the user can use the application.

Inactive (lapsed-subscription) users can still sign in to renew
or download their data, so we do NOT tie this to
``subscription_status``. The previous implementation returned
False for inactive users, which logged them out of every
@login_required route. Subscription-gated features should
check ``subscription_status`` directly in the view that needs
the gate, not via Flask-Login's activation hook.*
- `__init__` (line 85) `def __init__(self, db_path)` - *Initialize the UserDB with the database path.

Args:
    db_path (str): Path to the SQLite database file.*
- `_init_db` (line 105) `def _init_db(self)` - *Initialize the users table with all fields for zero-knowledge auth.

The table stores only zero-knowledge credential material: the SRP salt
and verifier (the password itself is never received), the user's public
key, the password-encrypted private key blob, and the key-derivation
salt used to protect that blob. The server can decrypt none of it.

Phone verification codes and MFA codes are stored as peppered
SHA-256 digests (``*_code_hash`` columns) instead of plaintext so
a database dump does not hand an attacker ready-to-use codes.

The ``phone`` column is not unique: phone numbers are recycled by
carriers and SIM-swap attacks invalidate the uniqueness guarantee
anyway. ``email`` remains unique because it is the primary
recovery identity.

If the table was created by an older v7 schema (which carried
NOT NULL KEM blob columns the v8 controller never writes),
migrate in place: rebuild the table under the v8 shape and preserve
the surviving identity columns. The legacy password blobs are
intentionally dropped: v7 ciphertexts are useless without the
matching v7 KEM code path that has been removed.*
- `_has_phone_unique_constraint` (line 193) `def _has_phone_unique_constraint(self)` - *Return True if the ``users.phone`` column is UNIQUE.

SQLite does not expose UNIQUE column constraints via ``PRAGMA
table_info``; the only reliable signal is the auto-index that
SQLite materialises for any ``UNIQUE`` column (``sqlite_autoindex_users_N``).*
- `_drop_phone_unique_if_present` (line 214) `def _drop_phone_unique_if_present(self)` - *Remove the UNIQUE constraint on ``users.phone``.

The v7 schema declared ``phone TEXT UNIQUE``. Carriers recycle
numbers, so the uniqueness guarantee is illusory; it also makes
account recovery hostile when a number changes hands.

SQLite forbids ``DROP INDEX`` on an auto-index backing a UNIQUE
column, so we have to rebuild the table. The rebuild follows
the same shape as :meth:`_migrate_from_v7` but copies every
column by position (the schema is now already v8-shaped thanks
to the prior migration step, so we know the column order).*
- `_migrate_from_v7` (line 271) `def _migrate_from_v7(self, legacy_columns)` - *Rebuild the users table to drop legacy v7 NOT NULL KEM columns.

SQLite cannot drop a column or relax a NOT NULL constraint in place,
so we rename the old table, create a fresh v8-shaped users table,
copy every surviving column, then drop the renamed legacy table.*
- `create_user` (line 325) `def create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled, recovery_salt, encrypted_private_key_recovery)` - *Persist a new user from client-provided zero-knowledge credentials.

All cryptographic material (salt, verifier, public key, encrypted
private key, KDF salt) is generated on the client; this method only
stores opaque values and never derives or sees the password.
Phone and MFA codes are stored as the peppered hash supplied by
the controller; the plaintext only ever lives in the SMS that
leaves the building.

``recovery_salt`` and ``encrypted_private_key_recovery`` are the
QV-RECOVERY-1 fields: an independent PBKDF2 salt and AES-256-GCM
wrapping of the same ``privateBlob``, keyed by a client-generated
high-entropy recovery code instead of the account password. Both
are optional so older clients that do not yet generate a recovery
code can still register.*
- `update_user_phone_status` (line 362) `def update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)` - *Update phone verification status and related fields.

The ``phone_verification_code_hash`` parameter accepts the
peppered SHA-256 digest. Passing ``None`` clears the stored
hash (e.g. after the user verifies successfully).*
- `update_user_mfa_status` (line 396) `def update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)` - *Update MFA code, expiration, and enabled status.

The ``mfa_code_hash`` parameter accepts the peppered SHA-256
digest of the freshly-generated 6-digit code. ``mfa_enabled`` is
a tri-state: ``None`` leaves the value alone.*
- `update_user` (line 430) `def update_user(self, username, email_verified, confirmation_token)` - *Update specific user fields.*
- `get_user` (line 454) `def get_user(self, username)` - *Retrieve a user by username.

Args:
    username (str): Username to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_user_by_id` (line 468) `def get_user_by_id(self, user_id)` - *Retrieve a user by ID.

Args:
    user_id (int): ID of the user to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_user_by_email` (line 482) `def get_user_by_email(self, email)` - *Retrieve a user by email address.

Args:
    email (str): Email address to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_user_by_phone` (line 496) `def get_user_by_phone(self, phone)` - *Retrieve a user by phone number.

Args:
    phone (str): Phone number to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_user_by_confirmation_token` (line 510) `def get_user_by_confirmation_token(self, token)` - *Retrieve a user by confirmation token.

Args:
    token (str): Confirmation token to search for.

Returns:
    Optional[dict]: User data as a dictionary or None if not found.*
- `get_recovery_bundle` (line 524) `def get_recovery_bundle(self, username)` - *Return the QV-RECOVERY-1 bundle for a username, if one exists.

Args:
    username (str): Username to look up.

Returns:
    A dict with ``recovery_salt``, ``encrypted_private_key_recovery``,
    and ``public_key`` if the account has a recovery bundle
    configured, or ``None`` if the account does not exist or has
    not generated a recovery code (e.g. accounts created before
    QV-RECOVERY-1 was added).*
- `reset_credentials_with_recovery` (line 548) `def reset_credentials_with_recovery(self, username, srp_salt, srp_verifier, kdf_salt, encrypted_private_key)` - *Replace a user's password-derived credentials after a verified recovery.

Called only after the caller has verified ``public_key_proof``
against the stored ``public_key`` (proof that the requester
possesses the recovery code, since it is the only way to recover
the matching ``privateBlob`` and re-derive the public key). The
``public_key`` and the underlying keypair are unchanged; only the
SRP verifier and the password-wrapping of the existing private key
blob are replaced.

Args:
    username (str): Username whose credentials are being reset.
    srp_salt (str): New SRP salt, hex-encoded.
    srp_verifier (str): New SRP verifier, hex-encoded.
    kdf_salt (str): New PBKDF2 salt for the password-wrapped private key, hex-encoded.
    encrypted_private_key (str): The same private key blob, re-wrapped under the new password.*
- `update_role` (line 579) `def update_role(self, username, role, storage_quota, subscription_status)` - *Update a user's role, storage quota, and subscription status.

Args:
    username (str): Username of the user to update.
    role (str): New role for the user.
    storage_quota (int): New storage quota in bytes (default: 10MB).
    subscription_status (str): New subscription status (default: 'active').*
- `count_users` (line 592) `def count_users(self)` - *Return the total number of users.

Implemented as ``SELECT COUNT(*)`` rather than ``len(get_all_users())``
so the home page does not materialise the entire table on every
request.*
- `get_all_users` (line 603) `def get_all_users(self)` - *Retrieve all users.

Returns:
    list[dict]: List of dictionaries containing user data.*
- `_parse_datetime` (line 615) `def _parse_datetime(value)` - *Parse a stored timestamp into a datetime, tolerating the format.

Args:
    value: A datetime, an ISO-like timestamp string, or None.

Returns:
    The parsed datetime, or None when the value is empty or unparseable.*
- `_convert_row_to_dict` (line 638) `def _convert_row_to_dict(self, row)` - *Convert a name-keyed SQLite row into a plain dictionary.

Reads access columns by name (the connection uses ``sqlite3.Row``), so
the mapping is robust to column ordering and additive migrations.

Args:
    row: A ``sqlite3.Row`` produced by a read query, or None.

Returns:
    A dictionary of user fields, or None when the row is empty.*
- `fetch_one` (line 694) `def fetch_one(self, query, params)` - *Execute a query and return the first result as a dictionary.

Args:
    query (str): SQL query to execute.
    params (tuple): Parameters for the query (default: empty tuple).

Returns:
    Optional[dict]: First row as a dictionary or None if no results or an error occurs.*
- `value` (line 655) `def value(name, default)`

#### `pq_decrypt_password.py`
**Path:** `pq_decrypt_password.py`

*No symbols extracted*

#### `doctor.py`
**Path:** `scripts/doctor.py`
**File Doc:** *Doctor: verify and repair the QuantumVault operator environment.  Used by ``make doctor`` (check only) and ``make doctor-fix`` (check plus install every missing piece that has an unattended installer).  Stdlib only, so it runs even when no project dependency is installed. Every knob is overridable through the environment; module-level constants are the single source of truth for defaults.  Checks cover Python modules, system binaries (openssl, redis-server, tor, cloudflared, docker, node), the ``.env`` file, and TCP reachability of Redis and the Garage S3 endpoint. ``--fix`` installs Python dependencies from ``requirements.txt``, Debian packages via apt, the cloudflared binary from the official Cloudflare release, and the garage binary from the official release server. Anything that cannot be installed unattended is reported in plain English with the exact command to run or the instruction to contact the server administrator.*

**Classes:**
- `CheckResult` (line 98) `class CheckResult` - *Outcome of one environment check with a repair hint.*
- `DoctorReport` (line 108) `class DoctorReport` - *Accumulated check results with derived exit status.*

**Methods:**
- `load_env_file` (line 128) `def load_env_file(path)` - *Parse a dotenv file into a dict without third-party imports.*
- `effective_env` (line 147) `def effective_env()` - *Return process env overlaid with ``.env`` file values.*
- `check_python` (line 154) `def check_python(minimum)` - *Verify the interpreter meets the minimum supported version.*
- `check_module` (line 170) `def check_module(name)` - *Verify one Python module imports cleanly.*
- `check_binary` (line 186) `def check_binary(name, env_override)` - *Verify one system binary resolves via PATH or an override path.*
- `check_env_file` (line 210) `def check_env_file()` - *Verify the operator ``.env`` file exists.*
- `parse_host_port` (line 223) `def parse_host_port(uri, default_port)` - *Extract a TCP host and port from a Redis or HTTP(S) URL.*
- `check_tcp` (line 242) `def check_tcp(name, host, port, timeout)` - *Verify a TCP endpoint accepts connections.*
- `debian_arch` (line 261) `def debian_arch(deb)` - *Map the host CPU to a Cloudflare or Garage release architecture.*
- `cloudflared_deb_url` (line 270) `def cloudflared_deb_url(version, arch)` - *Build the official cloudflared .deb URL for a version and arch.*
- `garage_bin_url` (line 283) `def garage_bin_url(version, target)` - *Build the official garage binary URL for a version and target.*
- `apt_command` (line 288) `def apt_command(packages)` - *Build an apt install command, prefixed with sudo outside root.*
- `run_command` (line 298) `def run_command(cmd)` - *Run one shell command and capture its outcome.*
- `download_file` (line 319) `def download_file(url, destination)` - *Fetch a URL with curl when present, else urllib.*
- `upsert_env` (line 334) `def upsert_env(key, value, path)` - *Set one KEY=value pair in ``.env``, preserving other lines.*
- `fix_python_deps` (line 352) `def fix_python_deps()` - *Install project requirements with the running interpreter.*
- `fix_apt` (line 360) `def fix_apt(packages)` - *Install Debian system packages, using sudo outside root.*
- `fix_cloudflared` (line 373) `def fix_cloudflared(version, bin_dir)` - *Install the cloudflared binary into a user-writable bin directory.*
- `fix_garage` (line 417) `def fix_garage(version, destination)` - *Download the garage binary and verify it against its checksum.*
- `collect_report` (line 449) `def collect_report()` - *Run every check and return the aggregated report.*
- `print_report` (line 476) `def print_report(report)` - *Render the report in plain English for operators.*
- `apply_fixes` (line 493) `def apply_fixes(report)` - *Install every missing piece that has an unattended installer.*
- `main` (line 530) `def main(argv)` - *Entry point for ``make doctor`` and ``make doctor-fix``.*
- `add` (line 113) `def add(self, result)` - *Append one check result.*
- `failures` (line 118) `def failures(self)` - *Return every failing check.*
- `exit_code` (line 123) `def exit_code(self)` - *Return 0 when every check passes, 1 otherwise.*

#### `email_tool.py`
**Path:** `scripts/email_tool.py`
**File Doc:** *Operator email tooling for QuantumVault.  Three subcommands, all runnable from any Linux host or AWS VPS that has the project checked out and its configuration available (payload.json plus an optional .env):  python scripts/email_tool.py test-smtp you@example.com Send a real test message through the configured SMTP server to prove the transport works from this machine.  python scripts/email_tool.py link <username> Print the account-confirmation URL for a user without sending mail, so an operator can verify an account when SMTP is not yet set up.  python scripts/email_tool.py confirm <username> Mark a user's email as verified directly in the database.  Exit code is 0 on success and 1 on failure so the commands compose in scripts.*

**Functions:**
- `_build_mail_app` (line 40) `def _build_mail_app(config)` - *Build a minimal Flask app that only carries the mail configuration.

Intentionally avoids the full application factory (object storage, Redis,
security headers) so this tool runs on a bare host with nothing but SMTP
reachable.*
- `cmd_test_smtp` (line 63) `def cmd_test_smtp(args)` - *Send a test email through the configured SMTP server.*
- `cmd_link` (line 91) `def cmd_link(args)` - *Print the confirmation URL for a user without sending email.*
- `cmd_confirm` (line 114) `def cmd_confirm(args)` - *Mark a user's email as verified directly in the database.*
- `build_parser` (line 133) `def build_parser()` - *Construct the argument parser for the three subcommands.*
- `main` (line 153) `def main()` - *Parse arguments and dispatch to the selected subcommand.*

#### `makeadmin.py`
**Path:** `scripts/makeadmin.py`
**File Doc:** *Operator tooling to promote QuantumVault users to a privileged role.  Two subcommands, runnable from any Linux host that has the project checked out (no Flask app context required — talks to the SQLite DB directly):  python scripts/makeadmin.py <username> Promote <username> to 'superadmin'. Idempotent: re-running on an already-superadmin user is a no-op that still returns exit code 0.  python scripts/makeadmin.py <username> <role> Set <username>'s role to an arbitrary value from the allowed set (free, bronze, silver, gold, admin, superadmin). Use this for demotions, role audits, or seeding non-superadmin operators.  Exit code is 0 on success and 1 on failure so the commands compose in scripts. The DB path defaults to ``instance/users.db``; override with the ``QV_USERS_DB`` environment variable when running against a non-default deployment (e.g. a staging copy).  The script writes through ``UserDB.update_role`` (models/user.py) so the storage_quota and subscription_status side-effects match what the rest of the application does. It does NOT touch the KEM / SRP credentials — a promotion never invalidates a user's existing login.*

**Functions:**
- `_resolve_db_path` (line 51) `def _resolve_db_path()` - *Return the absolute users.db path, anchored at the project root.

A bare ``instance/users.db`` only resolves when the script is run
from the project root. Anchoring at ``_PROJECT_ROOT`` lets an operator
invoke it from anywhere (cron, CI, a different cwd) without surprises.*
- `_print_user_summary` (line 64) `def _print_user_summary(user)` - *Print the post-update user record so the operator can eyeball it.*
- `cmd_promote` (line 75) `def cmd_promote(args)` - *Promote ``args.username`` to the requested role (default: superadmin).*
- `build_parser` (line 126) `def build_parser()` - *Construct the argument parser for the makeadmin subcommands.*
- `main` (line 152) `def main()` - *Parse arguments and dispatch to the selected subcommand.*

#### `test_bloque1.py`
**Path:** `scripts/test_bloque1.py`
**File Doc:** *Bloque 1 test: superadmin_edit_user endpoint.  Renders the user-edit form via Flask's test client, then verifies GET (200) + POST (200) paths plus the role guard. The DB is backed up before the run and restored afterwards, so a failed test cannot leave dirty state.  Usage:  python3 scripts/test_bloque1.py*

**Classes:**
- `_FakeUser` (line 48) `class _FakeUser`

**Methods:**
- `_load_user` (line 62) `def _load_user(uid)`
- `check` (line 86) `def check(name, ok, detail)`
- `__init__` (line 49) `def __init__(self, row)`
- `is_authenticated` (line 54) `def is_authenticated(self)`
- `is_active` (line 56) `def is_active(self)`
- `is_anonymous` (line 58) `def is_anonymous(self)`
- `get_id` (line 59) `def get_id(self)`

#### `server.py`
**Path:** `server.py`

*No symbols extracted*

#### `terms.py`
**Path:** `templates/terms.py`

**Functions:**
- `terms` (line 6) `def terms()` - *Render the About page.*

#### `__init__.py`
**Path:** `tests/__init__.py`

*No symbols extracted*

#### `conftest.py`
**Path:** `tests/conftest.py`
**File Doc:** *Shared pytest fixtures for the QuantumVault test suite.  Builds the Flask app via :func:`app_factory.create_app` in a mode safe for automated tests: development settings (so a missing ``FLASK_SECRET_KEY`` does not abort startup), CSP/HTTPS-redirect disabled, an in-memory rate limiter, and a temporary SQLite database path so the suite never touches ``instance/users.db``.*

**Classes:**
- `_ListLogHandler` (line 106) `class _ListLogHandler(Handler)` - *Collect emitted log messages in a list for assertions.*

**Functions:**
- `_hermetic_env` (line 26) `def _hermetic_env(monkeypatch)` - *Keep the suite hermetic against the operator's local ``.env`` file.

``load_payload`` calls ``dotenv.load_dotenv()`` at app creation, which
would inject the developer's local ``QV_*`` values (often empty facade
hashes) into ``os.environ`` and shadow the explicit mappings under
test. Neutralizing the loader makes every test run against the
mappings it declares, matching CI where no ``.env`` exists.*
- `_push_request_context` (line 58) `def _push_request_context()` - *Neutralize pytest-flask's autouse request-context push.

pytest-flask installs an autouse ``_push_request_context`` fixture that
keeps an application/request context pushed for the whole test. That
ambient context makes Flask-Login's ``current_user`` proxy and
``client.session_transaction`` resolve against a stale context, so a
test that authenticates a second user on the same client still observes
the first user's data. This suite drives the app exclusively through the
``client`` fixture, which manages its own per-request context, so the
ambient push is both unnecessary and a correctness hazard. Overriding
the plugin fixture by name (conftest takes precedence over installed
plugins) replaces it with a no-op.*
- `app` (line 76) `def app(tmp_path)` - *Return a QuantumVault Flask app configured for testing.*
- `client` (line 101) `def client(app)` - *Return a Flask test client for the test app.*

**Methods:**
- `audit_records` (line 118) `def audit_records()` - *Yield a list that is appended with each ``audit_event`` JSON line.

The audit logger has ``propagate = False`` (by design, so it never
mixes into the application log), so ``caplog`` cannot see it. This
fixture attaches a temporary handler directly to the audit logger
instead.*
- `__init__` (line 109) `def __init__(self)`
- `emit` (line 113) `def emit(self, record)`

#### `test_account_facade.py`
**Path:** `tests/test_account_facade.py`
**File Doc:** *Behaviour contract: the decoy site requires a deniable passphrase.  When the cover facade is enabled, the account page must ask for a deniable (second) passphrase and mark the field required. The server exposes only the instance-level facade flag; it never learns whether a passphrase is set.*

**Functions:**
- `fast_hasher` (line 23) `def fast_hasher()`
- `_make_user` (line 27) `def _make_user(db_path, username)`
- `_authenticated_client` (line 55) `def _authenticated_client(application, db_path)`
- `_build` (line 65) `def _build(tmp_path, fast_hasher)`
- `test_facade_enabled_requires_a_deniable_passphrase` (line 88) `def test_facade_enabled_requires_a_deniable_passphrase(tmp_path, fast_hasher)`
- `test_facade_disabled_keeps_it_optional` (line 99) `def test_facade_disabled_keeps_it_optional(tmp_path, fast_hasher)`

#### `test_auth_phone.py`
**Path:** `tests/test_auth_phone.py`
**File Doc:** *Regression tests for the phone-verification page and resend route.  The verify-phone template links its "Resend Verification Code" button to ``auth.resend_phone_verification``. Before that endpoint existed, simply rendering the page raised a Jinja ``BuildError`` (HTTP 500). These tests pin both the render and the endpoint registration.  The resend POST itself is not invoked here: like every auth route it constructs an ``AuthController``, which opens a Redis-backed SRP session store, and the test environment has no Redis (``STORAGE_URI=memory://``). Confirming the endpoint is registered is enough to prove the template's ``url_for`` resolves, which is the bug under test.*

**Functions:**
- `test_verify_phone_page_renders` (line 18) `def test_verify_phone_page_renders(client)` - *GET /verify_phone must render without a url_for BuildError.*
- `test_resend_endpoint_is_registered` (line 25) `def test_resend_endpoint_is_registered(app)` - *The resend endpoint the template links to must exist.*
- `test_resend_route_accepts_only_post` (line 31) `def test_resend_route_accepts_only_post(app)` - *The resend endpoint is POST-only so a GET cannot trigger an SMS.*

#### `test_cover.py`
**Path:** `tests/test_cover.py`
**File Doc:** *Specification tests for the QV-FACADE-2 configurable cover templates.  Behaviour is specified per collaborator (catalog, sanitizer, renderer, custom store, service) and end-to-end through the HTTP cover flow, so a regression in any layer fails a focused test rather than only the surface.*

**Classes:**
- `TestCatalog` (line 83) `class TestCatalog`
- `TestSanitizer` (line 103) `class TestSanitizer`
- `TestRenderer` (line 158) `class TestRenderer`
- `TestCustomStore` (line 189) `class TestCustomStore`
- `TestCoverService` (line 244) `class TestCoverService`
- `TestCoverHttp` (line 280) `class TestCoverHttp`

**Functions:**
- `fast_hasher` (line 42) `def fast_hasher()`
- `renderer` (line 47) `def renderer()`
- `store` (line 52) `def store(tmp_path, renderer)`
- `_facade_overrides` (line 56) `def _facade_overrides(fast_hasher)`
- `_client` (line 68) `def _client(tmp_path, fast_hasher)`

**Methods:**
- `test_catalog_ships_five_distinct_templates` (line 84) `def test_catalog_ships_five_distinct_templates(self)`
- `test_default_template_exists` (line 89) `def test_default_template_exists(self)`
- `test_every_template_validates_and_renders` (line 92) `def test_every_template_validates_and_renders(self, renderer)`
- `test_empty_payload_fills_defaults` (line 104) `def test_empty_payload_fills_defaults(self)`
- `test_unknown_variable_is_rejected` (line 109) `def test_unknown_variable_is_rejected(self)`
- `test_invalid_email_is_rejected` (line 113) `def test_invalid_email_is_rejected(self)`
- `test_control_characters_are_stripped` (line 117) `def test_control_characters_are_stripped(self)`
- `test_overlong_value_is_rejected` (line 121) `def test_overlong_value_is_rejected(self)`
- `test_multiline_body_preserves_line_breaks` (line 125) `def test_multiline_body_preserves_line_breaks(self)`
- `test_single_line_value_flattens_line_breaks` (line 129) `def test_single_line_value_flattens_line_breaks(self)`
- `test_multiline_flag_matches_spec` (line 137) `def test_multiline_flag_matches_spec(self, spec)`
- `test_text_boundary_is_inclusive` (line 144) `def test_text_boundary_is_inclusive(self)`
- `test_email_boundary_is_inclusive` (line 150) `def test_email_boundary_is_inclusive(self)`
- `test_variables_are_autoescaped` (line 159) `def test_variables_are_autoescaped(self, renderer)`
- `test_unknown_variable_is_rejected` (line 164) `def test_unknown_variable_is_rejected(self, renderer)`
- `test_dunder_access_is_rejected` (line 168) `def test_dunder_access_is_rejected(self, renderer)`
- `test_inline_script_is_rejected` (line 172) `def test_inline_script_is_rejected(self, renderer)`
- `test_external_form_action_is_rejected` (line 176) `def test_external_form_action_is_rejected(self, renderer)`
- `test_template_import_is_rejected` (line 180) `def test_template_import_is_rejected(self, renderer)`
- `test_blank_source_is_rejected` (line 184) `def test_blank_source_is_rejected(self, renderer)`
- `test_valid_template_round_trips` (line 190) `def test_valid_template_round_trips(self, store)`
- `test_bad_extension_is_rejected` (line 196) `def test_bad_extension_is_rejected(self, store)`
- `test_oversize_template_is_rejected` (line 200) `def test_oversize_template_is_rejected(self, store)`
- `test_path_traversal_is_neutralized` (line 204) `def test_path_traversal_is_neutralized(self, store)`
- `test_script_template_is_rejected` (line 209) `def test_script_template_is_rejected(self, store)`
- `test_missing_template_raises` (line 213) `def test_missing_template_raises(self, store)`
- `test_non_bytes_payload_is_rejected` (line 217) `def test_non_bytes_payload_is_rejected(self, store)`
- `test_disallowed_character_filename_is_rejected` (line 221) `def test_disallowed_character_filename_is_rejected(self, store)`
- `test_exactly_max_size_is_accepted` (line 225) `def test_exactly_max_size_is_accepted(self, store)`
- `test_nested_directory_is_created` (line 229) `def test_nested_directory_is_created(self, tmp_path, renderer)`
- `test_two_templates_share_the_store` (line 233) `def test_two_templates_share_the_store(self, store)`
- `test_directory_with_allowed_suffix_is_ignored` (line 238) `def test_directory_with_allowed_suffix_is_ignored(self, store)`
- `test_selects_a_builtin_template` (line 245) `def test_selects_a_builtin_template(self, renderer, store)`
- `test_unknown_template_falls_back_to_default` (line 250) `def test_unknown_template_falls_back_to_default(self, renderer, store)`
- `test_missing_custom_template_falls_back_to_default` (line 255) `def test_missing_custom_template_falls_back_to_default(self, renderer, store)`
- `test_custom_template_is_rendered` (line 260) `def test_custom_template_is_rendered(self, renderer, store)`
- `test_builtin_selection_ignores_a_custom_name` (line 267) `def test_builtin_selection_ignores_a_custom_name(self, renderer, store)`
- `test_custom_selection_renders_the_custom_marker` (line 274) `def test_custom_selection_renders_the_custom_marker(self, renderer, store)`
- `test_default_cover_selects_search_portal` (line 281) `def test_default_cover_selects_search_portal(self, tmp_path, fast_hasher)`
- `test_configured_template_is_served` (line 287) `def test_configured_template_is_served(self, tmp_path, fast_hasher)`
- `test_gate_still_works_with_configured_template` (line 298) `def test_gate_still_works_with_configured_template(self, tmp_path, fast_hasher)`

#### `test_deniable_vault.py`
**Path:** `tests/test_deniable_vault.py`
**File Doc:** *Specification tests for the QV-DENIABLE-1 deniable vault feature.  The feature is split across layers, each tested in isolation and then end-to-end through the account HTTP API:  * :class:`controllers.deniable_vault.DeniableVaultConfig` and :class:`controllers.deniable_vault.EnvelopeValidator` enforce the structural invariants that make a stored container indistinguishable to the (zero-knowledge) server: an exact slot count and a fixed-length slot ciphertext. The server validates *structure only*; it never decrypts. * :class:`controllers.deniable_vault.DeniableVaultConfig.random_container` lets the server mint a well-formed, unopenable container so that every account has one. "Has a container" is therefore universal and reveals nothing about whether a hidden vault exists. * :class:`models.deniable_vault.DeniableVaultDB` stores the opaque envelope verbatim, one row per user. * :class:`controllers.deniable_vault.DeniableVaultController` provisions, validates, persists, and emits generic audit events that name neither the feature nor the contents. * The ``account`` blueprint exposes the settings page and the ``GET/PUT/DELETE /api/account/vault`` endpoints, gated by authentication, CSRF, and rate limiting.*

**Classes:**
- `TestDeniableVaultConfig` (line 140) `class TestDeniableVaultConfig`
- `TestEnvelopeValidator` (line 185) `class TestEnvelopeValidator`
- `TestRandomContainer` (line 272) `class TestRandomContainer`
- `TestDeniableVaultDB` (line 293) `class TestDeniableVaultDB`
- `TestDeniableVaultController` (line 325) `class TestDeniableVaultController`
- `TestDeniableVaultApi` (line 390) `class TestDeniableVaultApi`

**Functions:**
- `config` (line 50) `def config()` - *Return the default deniable-vault configuration.*
- `validator` (line 56) `def validator(config)` - *Return a validator bound to the default configuration.*
- `_ciphertext` (line 61) `def _ciphertext(config, length)` - *Return a base64 ciphertext string of the given (or expected) length.*
- `_valid_envelope` (line 71) `def _valid_envelope(config)` - *Build a structurally valid envelope for ``config``.

Every slot carries a ciphertext of the fixed expected length so the
fixed-size invariant holds. The contents are zero bytes; the validator
never inspects plaintext, only structure.*
- `_make_user` (line 91) `def _make_user(app, username, role)` - *Create a minimal user row in the test database and return it.*
- `_login` (line 120) `def _login(client, app, username, role)` - *Create and authenticate a user on ``client``'s session.*
- `_csrf` (line 130) `def _csrf(client)` - *Fetch a CSRF token bound to the client's session.*

**Methods:**
- `test_defaults_are_self_consistent` (line 141) `def test_defaults_are_self_consistent(self)`
- `test_expected_ct_length_matches_base64_formula` (line 150) `def test_expected_ct_length_matches_base64_formula(self, config)`
- `test_mapping_overrides_defaults` (line 154) `def test_mapping_overrides_defaults(self)`
- `test_environment_overrides_mapping` (line 161) `def test_environment_overrides_mapping(self, monkeypatch)`
- `test_allowed_kdf_csv_is_parsed` (line 166) `def test_allowed_kdf_csv_is_parsed(self, monkeypatch)`
- `test_public_parameters_round_trip_to_json` (line 172) `def test_public_parameters_round_trip_to_json(self, config)`
- `test_accepts_a_well_formed_envelope` (line 186) `def test_accepts_a_well_formed_envelope(self, validator, config)`
- `test_rejects_non_dict` (line 189) `def test_rejects_non_dict(self, validator)`
- `test_rejects_wrong_schema_version` (line 194) `def test_rejects_wrong_schema_version(self, validator, config)`
- `test_rejects_unknown_kdf` (line 200) `def test_rejects_unknown_kdf(self, validator, config)`
- `test_rejects_iterations_below_minimum` (line 206) `def test_rejects_iterations_below_minimum(self, validator, config)`
- `test_rejects_iterations_above_maximum` (line 212) `def test_rejects_iterations_above_maximum(self, validator, config)`
- `test_rejects_wrong_slot_count` (line 218) `def test_rejects_wrong_slot_count(self, validator, config)`
- `test_rejects_bad_salt_length` (line 224) `def test_rejects_bad_salt_length(self, validator, config)`
- `test_rejects_non_hex_salt` (line 230) `def test_rejects_non_hex_salt(self, validator, config)`
- `test_rejects_bad_nonce_length` (line 236) `def test_rejects_bad_nonce_length(self, validator, config)`
- `test_rejects_ciphertext_of_wrong_length` (line 242) `def test_rejects_ciphertext_of_wrong_length(self, validator, config)`
- `test_rejects_unequal_slot_ciphertext_lengths` (line 248) `def test_rejects_unequal_slot_ciphertext_lengths(self, validator, config)`
- `test_rejects_invalid_base64_ciphertext` (line 254) `def test_rejects_invalid_base64_ciphertext(self, validator, config)`
- `test_rejects_missing_slot_keys` (line 260) `def test_rejects_missing_slot_keys(self, validator, config)`
- `test_random_container_passes_validation` (line 273) `def test_random_container_passes_validation(self, config, validator)`
- `test_random_containers_differ` (line 276) `def test_random_containers_differ(self, config)`
- `test_random_container_has_fixed_shape` (line 281) `def test_random_container_has_fixed_shape(self, config)`
- `test_upsert_then_get_round_trips_verbatim` (line 294) `def test_upsert_then_get_round_trips_verbatim(self, tmp_path)`
- `test_upsert_replaces_existing_row` (line 303) `def test_upsert_replaces_existing_row(self, tmp_path)`
- `test_get_missing_returns_none` (line 309) `def test_get_missing_returns_none(self, tmp_path)`
- `test_exists` (line 313) `def test_exists(self, tmp_path)`
- `_controller` (line 326) `def _controller(self, tmp_path)`
- `test_load_or_provision_mints_when_absent` (line 331) `def test_load_or_provision_mints_when_absent(self, app, tmp_path)`
- `test_load_or_provision_is_stable` (line 339) `def test_load_or_provision_is_stable(self, app, tmp_path)`
- `test_save_then_load_round_trips` (line 346) `def test_save_then_load_round_trips(self, app, tmp_path)`
- `test_save_rejects_invalid_envelope` (line 354) `def test_save_rejects_invalid_envelope(self, app, tmp_path)`
- `test_reset_replaces_with_a_valid_random_container` (line 363) `def test_reset_replaces_with_a_valid_random_container(self, app, tmp_path)`
- `test_audit_is_generic_and_never_contains_ciphertext` (line 373) `def test_audit_is_generic_and_never_contains_ciphertext(self, app, tmp_path, audit_records)`
- `test_settings_page_requires_authentication` (line 391) `def test_settings_page_requires_authentication(self, client)`
- `test_get_api_requires_authentication` (line 395) `def test_get_api_requires_authentication(self, client)`
- `test_settings_page_renders_for_authenticated_user` (line 399) `def test_settings_page_renders_for_authenticated_user(self, client, app)`
- `test_get_always_returns_an_envelope_and_parameters` (line 406) `def test_get_always_returns_an_envelope_and_parameters(self, client, app)`
- `test_put_without_csrf_is_rejected` (line 414) `def test_put_without_csrf_is_rejected(self, client, app)`
- `test_put_get_reset_round_trip` (line 422) `def test_put_get_reset_round_trip(self, client, app)`
- `test_put_rejects_malformed_envelope` (line 447) `def test_put_rejects_malformed_envelope(self, client, app)`
- `test_vault_is_scoped_to_the_authenticated_user` (line 461) `def test_vault_is_scoped_to_the_authenticated_user(self, client, app)`

#### `test_doctor.py`
**Path:** `tests/test_doctor.py`
**File Doc:** *Behaviour contracts for scripts/doctor.py.  Covers binary and module checks, host/port parsing, release URL builders, apt command construction, and report exit status. No test touches the network, sudo, or package managers.*

**Functions:**
- `test_check_binary_finds_present_binary` (line 23) `def test_check_binary_finds_present_binary()` - *A binary on PATH reports ok with its resolved path.*
- `test_check_binary_flags_missing_binary` (line 30) `def test_check_binary_flags_missing_binary()` - *An unknown binary fails and points at doctor-fix in English.*
- `test_check_binary_honors_absolute_override` (line 38) `def test_check_binary_honors_absolute_override(tmp_path)` - *Absolute override paths resolve without trusting PATH.*
- `test_check_module_reports_status` (line 48) `def test_check_module_reports_status()` - *Present stdlib modules pass, unknown ones fail with a remedy.*
- `test_check_python_accepts_current_runtime` (line 56) `def test_check_python_accepts_current_runtime()` - *The running interpreter satisfies its own minimum version.*
- `test_parse_host_port_shapes` (line 62) `def test_parse_host_port_shapes()` - *Redis and HTTP URLs reduce to host plus port.*
- `test_check_tcp_refused_reports_remedy` (line 83) `def test_check_tcp_refused_reports_remedy()` - *A closed loopback port fails with operator guidance.*
- `test_release_url_builders` (line 90) `def test_release_url_builders()` - *Release URLs follow the official vendor layouts.*
- `test_apt_command_uses_sudo_outside_root` (line 105) `def test_apt_command_uses_sudo_outside_root()` - *Apt installs escalate with sudo unless already root.*
- `test_report_exit_code_reflects_failures` (line 115) `def test_report_exit_code_reflects_failures()` - *An empty failure set exits zero, any failure exits one.*
- `test_load_env_file_parses_assignments` (line 129) `def test_load_env_file_parses_assignments(tmp_path)` - *Comment and blank lines are skipped, quotes are stripped.*
- `test_upsert_env_replaces_and_appends` (line 140) `def test_upsert_env_replaces_and_appends(tmp_path)` - *Existing keys are replaced in place, new keys are appended.*

#### `test_facade.py`
**Path:** `tests/test_facade.py`
**File Doc:** *Specification tests for the QV-FACADE-1 cover facade and two-step gate.  The feature is specified behaviorally (given/when/then) and tested in isolation per collaborator, then end-to-end through the HTTP cover flow:  * :class:`controllers.facade.FacadeConfig` resolves every knob from the environment, then ``app.config``, then a code default, and never carries a gate phrase in the repository. * :class:`controllers.facade.GatePhraseHasher` hashes and verifies a gate phrase with Argon2id, so a low-entropy phrase resists offline attack if the config leaks. * :class:`controllers.facade.GateTicket` mints and verifies a short-lived signed ticket keyed by the app secret; expiry, tampering, and a wrong key all verify to ``None``. * :class:`controllers.facade.FacadeGate` classifies a submitted phrase as a miss, the real phrase, or the duress phrase, and emits a single generic audit event that reveals neither the outcome nor the phrase. * The ``facade`` blueprint conceals the app: anonymous visitors see the cover on the protected pages, a correct phrase reveals the ordinary login, an authenticated user bypasses the cover, and a disabled facade changes nothing.*

**Classes:**
- `TestFacadeConfig` (line 148) `class TestFacadeConfig`
- `TestGatePhraseHasher` (line 209) `class TestGatePhraseHasher`
- `TestGateTicket` (line 250) `class TestGateTicket`
- `TestFacadeGate` (line 288) `class TestFacadeGate`
- `TestFacadeHttp` (line 396) `class TestFacadeHttp`

**Functions:**
- `fast_hasher` (line 54) `def fast_hasher()` - *Return an Argon2id hasher with cheap parameters for fast tests.

Argon2 embeds its cost parameters in the encoded hash, so verification is
independent of the verifying hasher's own settings; a cheap hasher can
therefore produce fixtures without weakening what production verifies.*
- `gate_config` (line 67) `def gate_config(fast_hasher)` - *Return an enabled facade config with real and duress phrases set.*
- `_facade_overrides` (line 78) `def _facade_overrides(fast_hasher)` - *Return ``create_app`` config overrides that enable the facade.*
- `facade_client` (line 93) `def facade_client(tmp_path, fast_hasher)` - *Return a test client for an app with the facade enabled.*
- `_make_user` (line 109) `def _make_user(app_or_path, username)` - *Create a minimal user row in the given database and return it.*
- `_csrf` (line 138) `def _csrf(client)` - *Fetch a CSRF token bound to the client's session.*

**Methods:**
- `test_defaults_keep_the_facade_off` (line 149) `def test_defaults_keep_the_facade_off(self)`
- `test_defaults_keep_duress_alert_off` (line 154) `def test_defaults_keep_duress_alert_off(self)`
- `test_defaults_are_self_consistent` (line 157) `def test_defaults_are_self_consistent(self)`
- `test_mapping_overrides_defaults` (line 165) `def test_mapping_overrides_defaults(self)`
- `test_environment_overrides_mapping` (line 172) `def test_environment_overrides_mapping(self, monkeypatch)`
- `test_protected_paths_csv_is_parsed` (line 177) `def test_protected_paths_csv_is_parsed(self)`
- `test_gate_configured_requires_enabled_and_a_hash` (line 183) `def test_gate_configured_requires_enabled_and_a_hash(self)`
- `test_cover_context_is_cosmetic_and_json_serializable` (line 194) `def test_cover_context_is_cosmetic_and_json_serializable(self)`
- `test_hash_then_verify_accepts_the_phrase` (line 210) `def test_hash_then_verify_accepts_the_phrase(self, fast_hasher)`
- `test_verify_rejects_a_wrong_phrase` (line 214) `def test_verify_rejects_a_wrong_phrase(self, fast_hasher)`
- `test_hash_is_salted_so_two_hashes_differ` (line 218) `def test_hash_is_salted_so_two_hashes_differ(self, fast_hasher)`
- `test_verify_rejects_an_empty_stored_hash` (line 221) `def test_verify_rejects_an_empty_stored_hash(self, fast_hasher)`
- `test_verify_rejects_a_malformed_stored_hash` (line 224) `def test_verify_rejects_a_malformed_stored_hash(self, fast_hasher)`
- `test_verify_rejects_a_non_string_stored_hash` (line 227) `def test_verify_rejects_a_non_string_stored_hash(self, fast_hasher)`
- `test_from_config_builds_a_working_hasher` (line 231) `def test_from_config_builds_a_working_hasher(self)`
- `test_issue_then_verify_round_trips_the_mode` (line 251) `def test_issue_then_verify_round_trips_the_mode(self)`
- `test_issue_rejects_an_unknown_mode` (line 256) `def test_issue_rejects_an_unknown_mode(self)`
- `test_verify_rejects_an_expired_ticket` (line 261) `def test_verify_rejects_an_expired_ticket(self)`
- `test_verify_rejects_a_ticket_signed_with_another_key` (line 267) `def test_verify_rejects_a_ticket_signed_with_another_key(self)`
- `test_verify_rejects_garbage_and_none` (line 272) `def test_verify_rejects_garbage_and_none(self)`
- `test_verify_rejects_a_non_string_token` (line 277) `def test_verify_rejects_a_non_string_token(self)`
- `_gate` (line 289) `def _gate(self, config)`
- `test_real_phrase_yields_a_real_ticket` (line 292) `def test_real_phrase_yields_a_real_ticket(self, app, gate_config)`
- `test_duress_phrase_yields_a_duress_ticket` (line 300) `def test_duress_phrase_yields_a_duress_ticket(self, app, gate_config)`
- `test_wrong_phrase_is_a_miss_with_no_ticket` (line 307) `def test_wrong_phrase_is_a_miss_with_no_ticket(self, app, gate_config)`
- `test_miss_without_a_duress_hash` (line 314) `def test_miss_without_a_duress_hash(self, app, fast_hasher)`
- `test_minimum_length_phrase_is_accepted` (line 325) `def test_minimum_length_phrase_is_accepted(self, app, fast_hasher)`
- `test_maximum_length_phrase_is_accepted` (line 337) `def test_maximum_length_phrase_is_accepted(self, app, fast_hasher)`
- `test_too_short_phrase_is_a_miss` (line 349) `def test_too_short_phrase_is_a_miss(self, app, gate_config)`
- `test_too_long_phrase_is_a_miss` (line 355) `def test_too_long_phrase_is_a_miss(self, app, gate_config)`
- `test_audit_is_generic_and_never_contains_the_phrase` (line 361) `def test_audit_is_generic_and_never_contains_the_phrase(self, app, gate_config, audit_records)`
- `test_duress_alert_is_opt_in_and_generically_named` (line 372) `def test_duress_alert_is_opt_in_and_generically_named(self, app, fast_hasher, audit_records)`
- `test_anonymous_login_page_is_replaced_by_the_cover` (line 397) `def test_anonymous_login_page_is_replaced_by_the_cover(self, facade_client)`
- `test_anonymous_root_is_replaced_by_the_cover` (line 403) `def test_anonymous_root_is_replaced_by_the_cover(self, facade_client)`
- `test_wrong_phrase_keeps_the_cover_and_does_not_redirect` (line 409) `def test_wrong_phrase_keeps_the_cover_and_does_not_redirect(self, facade_client)`
- `test_real_phrase_reveals_the_login` (line 417) `def test_real_phrase_reveals_the_login(self, facade_client)`
- `test_duress_phrase_marks_the_session` (line 432) `def test_duress_phrase_marks_the_session(self, facade_client)`
- `test_authenticated_user_bypasses_the_cover` (line 441) `def test_authenticated_user_bypasses_the_cover(self, tmp_path, fast_hasher)`
- `test_gate_endpoint_is_absent_when_facade_disabled` (line 465) `def test_gate_endpoint_is_absent_when_facade_disabled(self, client)`
- `test_disabled_facade_serves_the_real_login` (line 469) `def test_disabled_facade_serves_the_real_login(self, client)`
- `test_enabled_without_a_hash_fails_open_to_the_real_app` (line 474) `def test_enabled_without_a_hash_fails_open_to_the_real_app(self, tmp_path)`

#### `test_integrity.py`
**Path:** `tests/test_integrity.py`
**File Doc:** *Contract tests for SRI pins and reproducible builds (QV-SRI-1).*

**Functions:**
- `test_compute_sri_format` (line 19) `def test_compute_sri_format()`
- `test_manifest_exists_and_pins_crypto` (line 25) `def test_manifest_exists_and_pins_crypto()`
- `test_manifest_hashes_match_files` (line 37) `def test_manifest_hashes_match_files()`
- `test_template_integrity_resolves_both_forms` (line 44) `def test_template_integrity_resolves_both_forms()`
- `test_jinja_global_registered` (line 51) `def test_jinja_global_registered(app)`
- `test_verify_build_passes_on_clean_tree` (line 55) `def test_verify_build_passes_on_clean_tree()`

#### `test_padding.py`
**Path:** `tests/test_padding.py`
**File Doc:** *Contract tests for fixed-bucket padding (QV-PAD-1) and its enforcement.*

**Classes:**
- `_FakeS3` (line 128) `class _FakeS3`
- `_FakeUpload` (line 136) `class _FakeUpload`

**Functions:**
- `test_pad_roundtrip_message_sizes` (line 26) `def test_pad_roundtrip_message_sizes()`
- `test_pad_roundtrip_file_kind` (line 33) `def test_pad_roundtrip_file_kind()`
- `test_bucket_boundaries` (line 38) `def test_bucket_boundaries()`
- `test_pad_output_length_is_bucketed` (line 44) `def test_pad_output_length_is_bucketed()`
- `test_pad_uses_fresh_randomness` (line 49) `def test_pad_uses_fresh_randomness()`
- `test_pad_rejects_oversize` (line 56) `def test_pad_rejects_oversize()`
- `test_unpad_rejects_non_bucket_length` (line 61) `def test_unpad_rejects_non_bucket_length()`
- `test_unpad_rejects_corrupt_prefix` (line 66) `def test_unpad_rejects_corrupt_prefix()`
- `test_unpad_rejects_wrong_kind` (line 74) `def test_unpad_rejects_wrong_kind()`
- `test_wire_lengths` (line 80) `def test_wire_lengths()`
- `test_config_from_env_override` (line 87) `def test_config_from_env_override(monkeypatch)`
- `test_config_from_env_falls_back_on_garbage` (line 94) `def test_config_from_env_falls_back_on_garbage(monkeypatch)`
- `test_cache_holds_tables_not_pad_bytes` (line 99) `def test_cache_holds_tables_not_pad_bytes()`
- `test_message_controller_rejects_unpadded_envelope` (line 105) `def test_message_controller_rejects_unpadded_envelope(app, tmp_path, monkeypatch)`
- `test_message_controller_rejects_malformed_base64` (line 113) `def test_message_controller_rejects_malformed_base64(app, tmp_path, monkeypatch)`
- `test_message_controller_accepts_bucketed_envelope` (line 120) `def test_message_controller_accepts_bucketed_envelope(app, tmp_path, monkeypatch)`

**Methods:**
- `test_file_controller_rejects_unpadded_upload` (line 146) `def test_file_controller_rejects_unpadded_upload(app)`
- `test_file_controller_accepts_bucketed_upload` (line 152) `def test_file_controller_accepts_bucketed_upload(app)`
- `__init__` (line 129) `def __init__(self)`
- `put_object` (line 132) `def put_object(self, Bucket, Key, Body)`
- `__init__` (line 139) `def __init__(self, body)`
- `read` (line 142) `def read(self)`

#### `test_secure_channel.py`
**Path:** `tests/test_secure_channel.py`
**File Doc:** *Behaviour contracts for QV-TUNNEL disposable secure channels.  Covers SecureChannelConfig resolution, URL validation, manager lifecycle with injected process launcher, atomic state redaction in audit details, and superadmin HTTP gating.*

**Classes:**
- `_FakeProcess` (line 260) `class _FakeProcess`

**Functions:**
- `test_config_defaults_to_disabled_without_binaries` (line 30) `def test_config_defaults_to_disabled_without_binaries()` - *Unconfigured environment resolves to a disabled channel.*
- `test_config_reads_mode_and_port_from_env` (line 37) `def test_config_reads_mode_and_port_from_env()` - *Mode and local port resolve from environment with bounds.*
- `test_config_rejects_out_of_range_port` (line 47) `def test_config_rejects_out_of_range_port()` - *Ports outside 1..65535 fall back to the default.*
- `test_url_validators_accept_only_expected_shapes` (line 55) `def test_url_validators_accept_only_expected_shapes()` - *Validators accept quick-tunnel and v3 onion shapes only.*
- `test_manager_starts_hybrid_with_injected_launcher` (line 64) `def test_manager_starts_hybrid_with_injected_launcher(tmp_path)` - *Start launches both backends and persists redacted state.*
- `test_manager_rejects_invalid_mode` (line 90) `def test_manager_rejects_invalid_mode(tmp_path)` - *Disabled mode cannot be started explicitly.*
- `test_manager_stop_clears_state_with_killer` (line 101) `def test_manager_stop_clears_state_with_killer(tmp_path)` - *Stop kills tracked pids and removes persisted state.*
- `test_audit_details_never_carry_urls` (line 122) `def test_audit_details_never_carry_urls()` - *Audit helper redacts full URLs to mode plus fingerprint.*
- `test_superadmin_channel_routes_require_superadmin` (line 133) `def test_superadmin_channel_routes_require_superadmin(client)` - *Anonymous POST to channel endpoints redirects to login.*
- `test_env_template_documents_channel_keys` (line 139) `def test_env_template_documents_channel_keys()` - *Repository env template exposes every channel key.*
- `test_channel_state_file_permissions` (line 153) `def test_channel_state_file_permissions(tmp_path)` - *Persisted state is owner-only.*
- `test_validators_reject_non_string_inputs` (line 164) `def test_validators_reject_non_string_inputs()` - *Non-string values never validate as backend addresses.*
- `test_port_boundaries_accept_edges_and_reject_outside` (line 175) `def test_port_boundaries_accept_edges_and_reject_outside()` - *TCP port coercion honors 1 and 65535 as valid edges.*
- `test_config_blank_values_fall_back_to_defaults` (line 186) `def test_config_blank_values_fall_back_to_defaults()` - *Empty or whitespace binary and dir values resolve to defaults.*
- `test_config_explicit_values_are_preserved` (line 203) `def test_config_explicit_values_are_preserved()` - *Explicit binary and dir values survive resolution.*
- `test_config_env_beats_mapping` (line 219) `def test_config_env_beats_mapping()` - *Environment takes precedence over the mapping for every key.*
- `test_channel_status_defaults_and_single_side_active` (line 229) `def test_channel_status_defaults_and_single_side_active()` - *Ephemeral defaults True and either backend alone counts as active.*
- `test_default_launcher_detaches_process` (line 254) `def test_default_launcher_detaches_process(monkeypatch)` - *Launcher spawns detached daemons with piped stdio.*
- `test_default_killer_ignores_non_positive_pid` (line 276) `def test_default_killer_ignores_non_positive_pid(monkeypatch)` - *Zero and negative pids never reach os.kill.*
- `test_default_killer_falls_back_to_kill` (line 286) `def test_default_killer_falls_back_to_kill(monkeypatch)` - *Group kill failure falls back to plain kill before giving up.*
- `test_manager_init_blank_binaries_fall_back` (line 302) `def test_manager_init_blank_binaries_fall_back()` - *Blank constructor binaries resolve to shipped defaults.*
- `test_rotate_without_state_raises` (line 311) `def test_rotate_without_state_raises(tmp_path)` - *Rotate with no persisted channel raises instead of crashing.*
- `test_rotate_disabled_state_raises` (line 322) `def test_rotate_disabled_state_raises(tmp_path)` - *Rotate on a disabled record raises instead of starting.*
- `test_audit_details_default_verb_and_empty_urls` (line 334) `def test_audit_details_default_verb_and_empty_urls()` - *Empty action and absent urls still yield a safe detail string.*
- `test_status_for_drops_non_positive_pids` (line 348) `def test_status_for_drops_non_positive_pids()` - *Pid zero and negatives never survive status construction.*
- `test_read_state_filters_bad_pids` (line 357) `def test_read_state_filters_bad_pids(tmp_path)` - *Corrupt pid entries in state are filtered, valid ones kept.*
- `test_write_state_is_sorted_and_ephemeral` (line 378) `def test_write_state_is_sorted_and_ephemeral(tmp_path)` - *Persisted payload is deterministic JSON with ephemeral set.*
- `test_write_state_twice_in_existing_dir` (line 397) `def test_write_state_twice_in_existing_dir(tmp_path)` - *Repeated writes into an existing directory never raise.*
- `test_write_state_creates_nested_dirs` (line 408) `def test_write_state_creates_nested_dirs(tmp_path)` - *Nested state directories are created recursively.*
- `test_start_creates_nested_state_dirs` (line 416) `def test_start_creates_nested_state_dirs(tmp_path)` - *Backend start creates nested state dirs recursively.*
- `test_start_tor_only_creates_nested_state_dirs` (line 442) `def test_start_tor_only_creates_nested_state_dirs(tmp_path)` - *Tor-only start creates nested state dirs without prior backend.*
- `test_cleanup_scratch_suppresses_rmtree_errors` (line 463) `def test_cleanup_scratch_suppresses_rmtree_errors(tmp_path, monkeypatch)` - *Unremovable scratch dirs never break stop.*
- `test_resolve_binary_with_default_launcher_requires_path` (line 480) `def test_resolve_binary_with_default_launcher_requires_path(tmp_path)` - *Default launcher resolves bare names through PATH only.*
- `test_resolve_binary_with_injected_launcher_skips_which` (line 497) `def test_resolve_binary_with_injected_launcher_skips_which(tmp_path)` - *Injected launchers accept bare names without PATH lookup.*
- `test_resolve_binary_absolute_path_must_exist` (line 511) `def test_resolve_binary_absolute_path_must_exist(tmp_path)` - *Absolute candidates are accepted only when the file exists.*
- `test_pid_live_branches` (line 527) `def test_pid_live_branches(monkeypatch, tmp_path)` - *Pid liveness distinguishes dead, forbidden, broken, and live.*
- `test_normalize_onion_shapes` (line 555) `def test_normalize_onion_shapes()` - *Bare hostnames gain a scheme while full urls pass through.*
- `test_wait_helpers_respect_deadline_and_content` (line 564) `def test_wait_helpers_respect_deadline_and_content(tmp_path, monkeypatch)` - *Pattern and file waiters poll until timeout or content.*
- `test_wait_helpers_include_deadline_instant` (line 597) `def test_wait_helpers_include_deadline_instant(tmp_path, monkeypatch)` - *Polling still checks content at the exact deadline instant.*
- `test_channel_diagnostics_reports_availability` (line 636) `def test_channel_diagnostics_reports_availability(tmp_path)` - *Diagnostics resolve absolute paths and flag missing bare names.*
- `test_channel_diagnostics_missing_absolute_path` (line 656) `def test_channel_diagnostics_missing_absolute_path(tmp_path)` - *Absolute candidates that do not exist report as missing.*
- `test_read_log_tail_returns_trailing_lines` (line 671) `def test_read_log_tail_returns_trailing_lines(tmp_path)` - *Log tail surfaces backend output and stays empty when absent.*
- `test_superadmin_channel_section_is_readable` (line 685) `def test_superadmin_channel_section_is_readable()` - *Channel panel avoids low-contrast muted text and shows diagnostics.*
- `test_origin_scheme_parsing` (line 696) `def test_origin_scheme_parsing()` - *Only http and https survive scheme coercion.*
- `test_config_reads_origin_scheme` (line 706) `def test_config_reads_origin_scheme()` - *Origin scheme resolves from env with a safe fallback.*
- `test_origin_url_points_at_loopback` (line 719) `def test_origin_url_points_at_loopback()` - *Origin URL always targets loopback with the configured scheme.*
- `test_cloudflared_cmd_matches_origin_scheme` (line 733) `def test_cloudflared_cmd_matches_origin_scheme(tmp_path)` - *Plain origins skip TLS flags, https origins verify nothing.*
- `test_s3_probe_skips_dead_endpoint` (line 763) `def test_s3_probe_skips_dead_endpoint(app)` - *Unreachable object storage reports down without raising.*
- `test_s3_probe_detects_live_endpoint` (line 771) `def test_s3_probe_detects_live_endpoint(app)` - *A listening socket reports the endpoint as reachable.*
- `fake_launcher` (line 67) `def fake_launcher(cmd, log_path)`
- `fake_launcher` (line 105) `def fake_launcher(cmd, log_path)`

**Methods:**
- `_fake_popen` (line 263) `def _fake_popen(cmd)`
- `_raise_pg` (line 290) `def _raise_pg(pid, sig)`
- `_record_kill` (line 293) `def _record_kill(pid, sig)`
- `fake_launcher` (line 419) `def fake_launcher(cmd, log_path)`
- `fake_launcher` (line 445) `def fake_launcher(cmd, log_path)`
- `_raise` (line 471) `def _raise()`
- `_raise_lookup` (line 536) `def _raise_lookup(pid, sig)`
- `_raise_perm` (line 542) `def _raise_perm(pid, sig)`
- `_raise_os` (line 548) `def _raise_os(pid, sig)`
- `_fake_mono` (line 573) `def _fake_mono()`
- `_fake_sleep` (line 576) `def _fake_sleep(secs)`
- `_fake_mono` (line 606) `def _fake_mono()`
- `_fake_sleep` (line 609) `def _fake_sleep(secs)`
- `_fake_sleep_file` (line 627) `def _fake_sleep_file(secs)`
- `fake_launcher` (line 737) `def fake_launcher(cmd, log_path)`

#### `test_security.py`
**Path:** `tests/test_security.py`
**File Doc:** *Tests for utils/security.py: audit log redaction and JSON CSRF protection.*

**Functions:**
- `test_audit_event_includes_ip_and_ua_by_default` (line 12) `def test_audit_event_includes_ip_and_ua_by_default(app, audit_records, monkeypatch)`
- `test_audit_event_redacts_ip_and_ua_when_disabled` (line 29) `def test_audit_event_redacts_ip_and_ua_when_disabled(app, audit_records, monkeypatch)`
- `test_json_csrf_protect_rejects_missing_token` (line 45) `def test_json_csrf_protect_rejects_missing_token(app)`
- `test_json_csrf_protect_accepts_valid_header_token` (line 57) `def test_json_csrf_protect_accepts_valid_header_token(app)`
- `test_json_csrf_protect_passes_get_through_without_token` (line 77) `def test_json_csrf_protect_passes_get_through_without_token(app)`
- `view` (line 47) `def view()`
- `view` (line 59) `def view()`
- `view` (line 79) `def view()`

#### `test_srp.py`
**Path:** `tests/test_srp.py`
**File Doc:** *Pure-Python SRP-6a (QV-SRP-1) roundtrip test.  Mirrors the client-side math in ``static/js/qv-crypto.js`` (``deriveVerifier`` and ``srpLogin``) using only :mod:`utils.srp6a`, so this test exercises the exact server primitives without needing Redis, Flask, or a browser.*

**Functions:**
- `_h` (line 16) `def _h()`
- `_hint` (line 23) `def _hint()`
- `_client_derive_verifier` (line 27) `def _client_derive_verifier(username, password, salt_hex)` - *Mirror ``deriveVerifier`` in qv-crypto.js: v = g^x mod N.*
- `_client_compute_proof` (line 34) `def _client_compute_proof(username, password, salt_hex, server_a_secret, server_a, server_b)` - *Mirror ``srpLogin`` in qv-crypto.js: derive M1 and the expected M2.*
- `test_srp6a_full_roundtrip_matches_server_proofs` (line 74) `def test_srp6a_full_roundtrip_matches_server_proofs()`
- `test_srp6a_wrong_password_produces_mismatched_proof` (line 104) `def test_srp6a_wrong_password_produces_mismatched_proof()`

#### `test_utils.py`
**Path:** `tests/test_utils.py`
**File Doc:** *Contract tests for shared utility helpers.*

**Functions:**
- `test_database_path_prefers_the_configured_path` (line 8) `def test_database_path_prefers_the_configured_path(app)`
- `test_database_path_honors_env_outside_a_context` (line 13) `def test_database_path_honors_env_outside_a_context(monkeypatch)`
- `test_database_path_default_outside_a_context` (line 18) `def test_database_path_default_outside_a_context(monkeypatch)`

#### `generate_sri.py`
**Path:** `tools/generate_sri.py`
**File Doc:** *Generate the SRI manifest for first-party assets and pinned CDN URLs.  Regenerating the manifest is the audited step that binds served bytes to served hashes. The output is deterministic: keys are sorted, the JSON uses a fixed indent, and the file ends with a single newline, so two runs over identical inputs produce byte-identical output.  Usage: ./.venv/bin/python tools/generate_sri.py ./.venv/bin/python tools/generate_sri.py --check*

**Functions:**
- `collect_local_assets` (line 41) `def collect_local_assets()` - *Hash every first-party script and stylesheet under ``static/``.*
- `fetch_cdn_assets` (line 56) `def fetch_cdn_assets()` - *Download every pinned CDN URL and hash its exact bytes.*
- `build_manifest` (line 66) `def build_manifest(cdn, local)` - *Assemble the deterministic manifest document.*
- `render_manifest` (line 76) `def render_manifest(manifest)` - *Render the manifest deterministically with a trailing newline.*
- `main` (line 81) `def main(argv)` - *Generate the manifest, or verify it is current with ``--check``.*

#### `mutation_test.py`
**Path:** `tools/mutation_test.py`
**File Doc:** *Mutation testing harness for the QuantumVault facade and cover contracts.  Each discovered token mutation is applied in place, the test suite is run, and the mutation is classified as killed (tests fail) or survived (tests pass). A survivor indicates a gap in the tests and yields a non-zero exit status. The harness runs the suite with ``-B`` and purges bytecode caches so a restored source is always reloaded rather than served from a stale ``.pyc`` compiled from a mutant.*

**Classes:**
- `Mutation` (line 56) `class Mutation` - *A single token replacement and where it lives.*

**Methods:**
- `_is_equivalent_bool` (line 67) `def _is_equivalent_bool(tokens, index)`
- `discover_mutations` (line 79) `def discover_mutations(path, source)` - *Return every token-level mutation the harness can apply to a module.*
- `apply_mutation` (line 109) `def apply_mutation(source, mutation)` - *Return source with one token replaced at its exact position.*
- `collect` (line 121) `def collect(targets, limit)` - *Gather mutations across targets up to a global cap.*
- `purge_bytecode` (line 133) `def purge_bytecode()` - *Remove compiled caches so restored sources are always reloaded.*
- `run_suite` (line 142) `def run_suite(python, tests)` - *Return whether the test suite passed.*
- `main` (line 157) `def main(argv)` - *Run the mutation campaign and report killed versus survived mutants.*

#### `verify_build.py`
**Path:** `tools/verify_build.py`
**File Doc:** *Verify reproducible builds and the fixed code contracts (QV-SRI-1).  Checks performed, all offline:  1. Every first-party asset in ``static/sri_manifest.json`` recomputes to its pinned hash. A mismatch means the served bytes drifted from the audited bytes. 2. Every ``/static/...`` script or stylesheet referenced by any template carries an ``integrity`` attribute equal to the manifest value. 3. Every ``https://`` script or stylesheet referenced by any template carries an ``integrity`` attribute equal to the manifest CDN pin. 4. The JavaScript bucket tables in ``static/js/qv-padding.js`` equal the Python defaults in ``utils/padding.py``, so the two sides of the padding contract cannot drift apart silently.  Usage: ./.venv/bin/python tools/verify_build.py*

**Classes:**
- `AssetReference` (line 34) `class AssetReference(HTMLParser)` - *Collect external script and stylesheet references from one template.*

**Methods:**
- `_normalize_reference` (line 60) `def _normalize_reference(ref)` - *Resolve a ``url_for('static', ...)`` expression to its served path.*
- `load_manifest` (line 71) `def load_manifest()` - *Load and return the SRI manifest document.*
- `expected_for_reference` (line 76) `def expected_for_reference(manifest, ref)` - *Resolve the pinned integrity value for one template reference.*
- `integrity_attribute_ok` (line 85) `def integrity_attribute_ok(integrity, ref, expected)` - *Accept a literal pin or the ``sri_integrity`` template expression.*
- `check_local_hashes` (line 95) `def check_local_hashes(manifest, failures)` - *Recompute every pinned local asset and record mismatches.*
- `check_template_references` (line 110) `def check_template_references(manifest, failures)` - *Require manifest-backed integrity on every template reference.*
- `check_bucket_parity` (line 126) `def check_bucket_parity(failures)` - *Require identical bucket tables in Python and JavaScript.*
- `main` (line 141) `def main()` - *Run every check and report failures.*
- `__init__` (line 37) `def __init__(self)` - *Initialize the reference collector.*
- `handle_starttag` (line 42) `def handle_starttag(self, tag, attrs)` - *Record one script or link tag with its integrity attribute.*

#### `__init__.py`
**Path:** `utils/__init__.py`

*No symbols extracted*

#### `cache.py`
**Path:** `utils/cache.py`
**File Doc:** */home/grisun0/src/postcuantum/v1/utils/cache.py*

**Classes:**
- `Cache` (line 6) `class Cache` - *Redis-based caching layer.*

**Methods:**
- `__init__` (line 8) `def __init__(self)`
- `get` (line 11) `def get(self, key)` - *Retrieve a value from the cache.*
- `set` (line 16) `def set(self, key, value, ttl)` - *Store a value in the cache with an optional TTL (seconds).*
- `delete` (line 20) `def delete(self, key)` - *Delete a key from the cache.*

#### `integrity.py`
**Path:** `utils/integrity.py`
**File Doc:** *Subresource Integrity manifest helpers (QV-SRI-1).  The manifest at ``static/sri_manifest.json`` pins the exact bytes of every first-party script and stylesheet plus every pinned CDN URL. It is generated with ``tools/generate_sri.py`` and checked with ``tools/verify_build.py``. Templates read values through :func:`integrity_for` so the served HTML always carries the hash of the audited bytes, and a compromised static file or a swapped CDN payload fails closed in the browser instead of executing.*

**Functions:**
- `manifest_path` (line 25) `def manifest_path()` - *Return the manifest path resolved from this file, never hardcoded.*
- `compute_sri` (line 30) `def compute_sri(data, algorithm)` - *Return the SRI string ``<algorithm>-<base64 digest>`` for ``data``.*
- `compute_file_sri` (line 36) `def compute_file_sri(path, algorithm)` - *Return the SRI string for the bytes stored at ``path``.*
- `_cached_manifest_text` (line 42) `def _cached_manifest_text()` - *Return the raw manifest text, cached for the process lifetime.*
- `load_manifest` (line 47) `def load_manifest()` - *Return the parsed SRI manifest, or an empty mapping when absent.*
- `integrity_for` (line 55) `def integrity_for(key)` - *Return the pinned integrity string for one manifest key.

Args:
    key: Either a first-party asset path such as ``js/qv-crypto.js``
        or a full CDN URL.

Returns:
    The pinned ``sha384-...`` value, or ``None`` when unpinned.*
- `clear_manifest_cache` (line 72) `def clear_manifest_cache()` - *Drop the cached manifest text so tests see a regenerated file.*
- `template_integrity` (line 77) `def template_integrity(key)` - *Return the integrity string for a template asset reference.

Accepts the same reference the template already uses: a ``/static/``
path is normalized to its manifest key, and a full CDN URL resolves
to the CDN pin. Returns an empty string when unpinned so a missing
entry fails closed in ``verify_build`` instead of rendering ``None``.*

#### `mailer.py`
**Path:** `utils/mailer.py`
**File Doc:** *Transactional email helpers for QuantumVault.  Centralizes how outbound transactional mail is addressed and delivered so the registration flow and the background scheduler share a single implementation instead of each rebuilding absolute URLs and calling Flask-Mail directly.  The public host used for links is taken from ``SERVER_NAME`` and ``PREFERRED_URL_SCHEME`` so the same code produces correct links from a background thread (no request context) and from a request handler.*

**Functions:**
- `external_url` (line 22) `def external_url(path)` - *Build an absolute URL for a root-relative path using the public host.

Args:
    path: A path such as ``/confirm/<token>``. A leading slash is added
        if missing.

Returns:
    The absolute URL, for example ``https://www.quantumvault.pro/confirm/x``.*
- `mail_is_configured` (line 38) `def mail_is_configured()` - *Return True when SMTP credentials are present so a send can succeed.

A send is only attempted when both a username and password are set,
which lets callers fall back to logging a link in local or bare-VPS
deployments that have no mail account yet.*
- `send_transactional_email` (line 51) `def send_transactional_email(subject, recipients, body)` - *Send a plain-text transactional email through the configured server.

This never raises: a failure is logged and reported through the boolean
return so callers (registration, scheduler) degrade gracefully instead of
aborting the surrounding operation.

Args:
    subject: The email subject line.
    recipients: One or more destination addresses.
    body: The plain-text message body.

Returns:
    True if Flask-Mail accepted the message, False otherwise.*

#### `padding.py`
**Path:** `utils/padding.py`
**File Doc:** *Fixed-bucket padding for metadata-size concealment (QV-PAD-1).  An observer who cannot read ciphertext can still read its length. This module groups every plaintext into fixed buckets so the wire reveals only a coarse size class instead of an exact byte count.  Wire format for one padded plaintext of bucket ``B``::  LENGTH_PREFIX || PLAINTEXT || RANDOM_PAD  where ``LENGTH_PREFIX`` is the true plaintext length as a 4-byte big-endian unsigned integer and ``RANDOM_PAD`` is fresh output from :mod:`secrets` filling the remainder ``B - prefix - len(plaintext)``. The padded plaintext is then encrypted with AES-256-GCM, so the stored and transmitted ciphertext length is ``B + GCM_OVERHEAD_BYTES`` for every plaintext inside the same bucket.  Cache safety contract: the only value ever cached is the immutable bucket table itself, keyed by configuration version, never by message content or message length. Padding bytes are drawn fresh from the operating-system CSPRNG on every call and are never stored, reused, or placed in any cache. Reusing pad bytes across envelopes would make equal-length plaintexts produce related padded inputs, so reuse is forbidden by construction: there is no API that accepts caller-supplied pad bytes and no cache entry that holds them.  Bucket lookup always scans the full table so the number of iterations does not depend on which bucket matched.*

**Classes:**
- `PaddingError` (line 73) `class PaddingError(ValueError)` - *Raised when data does not fit any bucket or framing is invalid.*
- `PaddingConfig` (line 78) `class PaddingConfig` - *Immutable bucket tables for the two padded payload kinds.*

**Methods:**
- `_parse_buckets` (line 95) `def _parse_buckets(raw, fallback)` - *Parse a comma-separated bucket list, falling back on any error.*
- `config_from_env` (line 109) `def config_from_env()` - *Build a :class:`PaddingConfig` from the environment.

``QV_PAD_MESSAGE_BUCKETS`` and ``QV_PAD_FILE_BUCKETS`` accept
comma-separated byte sizes. Unset or malformed values resolve to the
compiled defaults so a misconfigured host fails closed to a known
table instead of disabling padding.*
- `_cached_bucket_table` (line 128) `def _cached_bucket_table(fingerprint)` - *Return the cached immutable bucket tables for one config version.

The cache key is the comma-joined bucket lists, so distinct operator
configurations never share an entry. Only the tables are cached.
Plaintexts, ciphertexts, lengths of individual payloads, and random
pad bytes never enter this cache.*
- `cached_tables` (line 142) `def cached_tables(config)` - *Return the process-wide cached bucket tables for ``config``.*
- `bucket_for` (line 149) `def bucket_for(plaintext_len, kind, config)` - *Return the smallest bucket holding ``plaintext_len`` plus prefix.

Raises:
    PaddingError: If the payload plus prefix exceeds every bucket.*
- `pad` (line 169) `def pad(plaintext, kind, config)` - *Pad ``plaintext`` to its bucket with fresh CSPRNG bytes.

Raises:
    PaddingError: If the payload does not fit any bucket.*
- `unpad` (line 183) `def unpad(padded, kind, config)` - *Remove bucket framing and return the original plaintext.

Raises:
    PaddingError: If the length is not a bucket or framing is corrupt.*
- `wire_ciphertext_len` (line 209) `def wire_ciphertext_len(bucket)` - *Return the AES-256-GCM ciphertext length for one padded bucket.*
- `is_allowed_ciphertext_len` (line 214) `def is_allowed_ciphertext_len(ciphertext_len, kind, config)` - *Return True when ``ciphertext_len`` matches a bucket plus GCM overhead.*
- `buckets_for` (line 84) `def buckets_for(self, kind)` - *Return the bucket table for ``kind``.*
- `max_plaintext_bytes` (line 90) `def max_plaintext_bytes(self, kind)` - *Return the largest plaintext that fits ``kind``.*

#### `plans.py`
**Path:** `utils/plans.py`

**Classes:**
- `SubscriptionPlans` (line 3) `class SubscriptionPlans` - *Define los planes de suscripción disponibles.*

**Methods:**
- `get_plan` (line 30) `def get_plan(plan_name)` - *Obtiene los detalles de un plan.

Args:
    plan_name (str): Nombre del plan.

Returns:
    Dict: Detalles del plan.*
- `validate_plan_payment` (line 42) `def validate_plan_payment(plan_name, amount_paid)` - *Valida que el monto pagado coincide con el plan.*

#### `scheduler.py`
**Path:** `utils/scheduler.py`
**File Doc:** *Background scheduler for trial expiration and inbox cleanup.  Runs two recurring jobs:  - ``check_trial_expiration`` (every 24h): flips ``subscription_status`` to ``inactive`` once the free trial has elapsed, and emails the user with a renewal link. - ``cleanup_old_messages`` (every 24h): drops inbox messages older than 7 days for inactive free users.  Both jobs run in APScheduler's BackgroundScheduler, so they execute on a separate thread from the Flask request workers. Any exception inside a job is logged but does not crash the scheduler process.*

**Functions:**
- `_now_utc` (line 32) `def _now_utc()` - *Timezone-aware UTC ``now`` (avoids the deprecated ``datetime.utcnow()``).*
- `init_scheduler` (line 37) `def init_scheduler(app, mail)` - *Start the background scheduler with the production job schedule.

The jobs run in a daemon thread, so they do not block the Flask
request loop. They are added idempotently: re-importing the module
does not register duplicates because :class:`BackgroundScheduler`
is local to this call.*
- `_is_trial_elapsed` (line 54) `def _is_trial_elapsed(user)` - *Return True if the user is on a free plan and the trial has ended.*
- `check_trial_expiration` (line 72) `def check_trial_expiration()`
- `cleanup_old_messages` (line 118) `def cleanup_old_messages()`

#### `security.py`
**Path:** `utils/security.py`
**File Doc:** *Centralized security primitives for QuantumVault.  Single source of truth for:  - The structured audit log used by every security-relevant event (registration, login, MFA, lockouts, contact, role changes, etc.). - A JSON-CSRF decorator that protects ``/api/*`` POST/PUT/DELETE routes against cross-origin forgery via the ``X-CSRF-Token`` header (the same token already issued by ``/api/csrf-token``). - Small helpers for constant-time comparison and secret hashing of short-lived codes (phone verification, MFA, recovery codes).  Keeping these in one module makes the threat model auditable: if a new endpoint is added and it touches the audit logger, the call site becomes trivially visible during a security review.*

**Functions:**
- `_get_audit_logger` (line 46) `def _get_audit_logger()` - *Return the process-wide audit logger, configured on first use.

The audit logger writes single-line JSON records to stdout. Every
security-relevant event (login success/failure, registration, MFA,
contact message, role change, account lockout, CSRF rejection) must
call :func:`audit_event` so that incident response has a single
stream to correlate against.*
- `_correlation_id` (line 72) `def _correlation_id()` - *Return the per-request correlation id, generating one if missing.

The id is stored on Flask's ``g`` so a single request emits multiple
audit events that share the same key, which is what an operator needs
when reconstructing a session.*
- `audit_event` (line 86) `def audit_event(event)` - *Emit a structured audit record.

Args:
    event: A short, snake_case event name, e.g. ``login_success`` or
        ``mfa_failure``.
    **fields: Additional structured fields to record. The keys
        ``ts`` (unix epoch in milliseconds), ``event``, ``cid``
        (correlation id), ``ip``, and ``ua`` are added automatically.

The ``ip`` and ``ua`` fields are recorded as ``None`` when
``QV_AUDIT_LOG_IP=0`` or ``QV_AUDIT_LOG_UA=0`` respectively, for
operators running for high-risk users (e.g. behind Tor) who do not
want client IP addresses or User-Agent strings persisted to logs.
Both default to enabled (``"1"``).*
- `constant_time_compare` (line 123) `def constant_time_compare(a, b)` - *Return True if the two strings match in constant time.

A regular ``==`` leaks length and content-prefix information via
short-circuit evaluation. This wraps :func:`hmac.compare_digest`
which compares the whole input even when lengths differ.*
- `hash_secret` (line 135) `def hash_secret(secret)` - *Hash a short-lived secret (phone code, MFA, recovery code) for storage.

Uses SHA-256 with a server-side pepper. The pepper is read from the
``QV_SECRET_PEPPER`` environment variable and falls back to a value
derived from ``SECRET_KEY`` so the hash is non-deterministic across
reinstalls but stable for a given deployment.

The goal is to avoid storing plaintext codes in the database: a DB
dump no longer hands an attacker ready-to-use codes. Phone codes
are 6 digits and MFA codes are 6 digits, so a peppered SHA-256 is
more than sufficient: an attacker with the DB but without the
pepper must precompute a 10^6-entry rainbow table per deployment.*
- `verify_secret` (line 156) `def verify_secret(secret, expected_hash)` - *Verify a short-lived secret against its stored hash.*
- `new_one_time_code` (line 163) `def new_one_time_code(length)` - *Return a cryptographically random numeric verification code.*
- `_extract_csrf_token` (line 172) `def _extract_csrf_token()` - *Return the CSRF token from the request header or body.

Mirrors Flask-WTF's own lookup order so a client that sets either
``X-CSRFToken`` or ``X-CSRF-Token`` (the two spellings Flask-WTF accepts
in ``WTF_CSRF_HEADERS``), or a ``csrf_token`` form/JSON field, is handled
uniformly. The browser crypto in ``static/js/qv-crypto.js`` sends the
``X-CSRFToken`` header.*
- `json_csrf_protect` (line 193) `def json_csrf_protect(view)` - *Decorator: require a valid CSRF token on JSON state-changing requests.

The token is the one Flask-WTF issues through ``form.hidden_tag()`` or
``/api/csrf-token``. It is a *signed* value, so it is validated with
:func:`flask_wtf.csrf.validate_csrf`, which unsigns it and compares it to
the raw token held in the session; a direct string comparison against the
session value never matches and must not be used. A missing or invalid
token is rejected with HTTP 403 and recorded in the audit log.

GET, HEAD and OPTIONS pass through unchanged because they are not
state-changing. Use this on every ``/api/`` route that mutates state.*
- `wrapper` (line 207) `def wrapper()`

#### `srp6a.py`
**Path:** `utils/srp6a.py`
**File Doc:** *Zero-knowledge SRP-6a authentication primitives for QuantumVault.  This module implements the server side of a Secure Remote Password (SRP-6a) handshake using the RFC 5054 2048-bit group with SHA-256. The user's password never reaches the server: registration stores only ``salt`` and the password verifier ``v = g**x mod N``; authentication is a challenge/response that proves knowledge of the password without transmitting it.  The serialization scheme ("QV-SRP-1") is implemented identically in the browser module ``static/js/qv-crypto.js`` so both ends agree byte-for-byte:  - Every group element hashed (N, g, A, B, S) is encoded as a big-endian integer left-padded to the byte length of N (256 bytes) via :func:`i2osp`. - ``H`` is SHA-256 over the concatenation of byte strings. - ``salt`` travels as a hex string; its raw bytes are used inside hashes.  Public functions perform the SRP math; :class:`SRPSessionStore` persists the ephemeral per-login server state in Redis with a short time-to-live.*

**Classes:**
- `SRPSessionStore` (line 150) `class SRPSessionStore` - *Redis-backed store for the ephemeral state of an in-flight SRP login.

Each ``hello`` step persists the values needed to verify the subsequent
``verify`` step. Entries expire after :data:`SESSION_TTL_SECONDS` so an
abandoned handshake cannot be resumed later.*

**Functions:**
- `i2osp` (line 47) `def i2osp(value)` - *Encode an integer as a big-endian byte string padded to the length of N.

Args:
    value: Non-negative integer to encode (a group element).

Returns:
    The big-endian representation left-padded with zero bytes to
    ``N_BYTE_LENGTH``.*
- `_hash` (line 60) `def _hash()` - *Return the SHA-256 digest of the concatenated byte chunks.*
- `_hash_int` (line 68) `def _hash_int()` - *Return the SHA-256 digest of the concatenated chunks as an integer.*
- `compute_k` (line 73) `def compute_k()` - *Compute the SRP-6a multiplier parameter ``k = H(N | PAD(g))``.*
- `compute_u` (line 78) `def compute_u(server_a, server_b)` - *Compute the random scrambling parameter ``u = H(PAD(A) | PAD(B))``.

Args:
    server_a: The client public ephemeral value A.
    server_b: The server public ephemeral value B.

Returns:
    The scrambling parameter u as an integer.*
- `generate_server_challenge` (line 91) `def generate_server_challenge(verifier)` - *Generate the server ephemeral key pair (b, B) for a login challenge.

Args:
    verifier: The stored password verifier ``v`` for the user.

Returns:
    A tuple ``(b, B)`` where ``b`` is the secret ephemeral and
    ``B = (k * v + g**b) mod N`` is the public value sent to the client.*
- `compute_proofs` (line 107) `def compute_proofs(username, salt_hex, verifier, server_a, server_b, server_b_secret)` - *Compute the expected client proof M1 and the server proof M2.

Args:
    username: The user identity I.
    salt_hex: The user salt as a hex string.
    verifier: The stored password verifier v.
    server_a: The client public ephemeral A.
    server_b: The server public ephemeral B.
    server_b_secret: The server secret ephemeral b.

Returns:
    A tuple ``(expected_m1, m2)`` of raw digest bytes.*

**Methods:**
- `hello` (line 224) `def hello(store, username, client_a_hex, salt_hex, verifier_hex)` - *Process the SRP ``hello`` step and return the server challenge B.

Args:
    store: The ephemeral session store.
    username: The user identity.
    client_a_hex: The client public ephemeral A as a hex string.
    salt_hex: The stored user salt as a hex string.
    verifier_hex: The stored verifier as a hex string.

Returns:
    The server public ephemeral B as a hex string, or ``None`` if the
    client value A is invalid (``A mod N == 0``).*
- `verify` (line 260) `def verify(store, username, client_m1_hex)` - *Process the SRP ``verify`` step and return the server proof M2.

Args:
    store: The ephemeral session store.
    username: The user identity.
    client_m1_hex: The client proof M1 as a hex string.

Returns:
    The server proof M2 as a hex string on success, or ``None`` if no
    pending session exists or the client proof is invalid.*
- `__init__` (line 158) `def __init__(self, storage_uri)` - *Initialize the store from a Redis connection URI.

Args:
    storage_uri: A ``redis://`` connection string (the same one used by
        the rate limiter).*
- `_key` (line 168) `def _key(username)` - *Return the Redis key for a username's pending SRP session.*
- `save` (line 172) `def save(self, username, salt_hex, verifier_hex, server_a_hex, server_b_hex, server_b_secret_hex)` - *Persist the ephemeral SRP challenge state for a username.

Args:
    username: The user identity.
    salt_hex: The user salt as a hex string.
    verifier_hex: The stored verifier as a hex string.
    server_a_hex: The client public ephemeral A as a hex string.
    server_b_hex: The server public ephemeral B as a hex string.
    server_b_secret_hex: The server secret ephemeral b as a hex string.*
- `load` (line 202) `def load(self, username)` - *Load and consume the ephemeral SRP state for a username.

The entry is deleted on read so each challenge is single-use.

Args:
    username: The user identity.

Returns:
    The stored session dictionary, or ``None`` if no valid session
    exists (expired, missing, or already consumed).*

#### `utils.py`
**Path:** `utils/utils.py`
**File Doc:** *utils/utils.py*

**Classes:**
- `Payload` (line 80) `class Payload(TypedDict)` - *Non-secret application configuration loaded from ``payload.json``.*
- `Config` (line 103) `class Config` - *Application configuration sourced from ``payload.json`` and the environment.

Non-secret defaults come from ``payload.json``; secrets and infrastructure
endpoints (mail credentials, object storage, Redis) are overlaid from
environment variables so that no credential is committed to the repository.

Every attribute is declared on the class so static analyzers see the
full shape; :meth:`__init__` populates them from the loaded payload.*

**Functions:**
- `database_path` (line 12) `def database_path()` - *Return the SQLite database path from config, with a legacy fallback.

Request-path code must never hard-code a database location: in tests and
in multi-instance deployments the configured path is the only correct
one, and a hard-coded path silently writes to (or reads from) the wrong
file. Outside an application context, for standalone scripts, the
``QV_USERS_DB`` environment variable or the historical default is used.*
- `as_bool` (line 29) `def as_bool(value, default)` - *Coerce an environment or payload value into a real boolean.

Strings such as ``"True"`` and ``"False"`` are both truthy when passed
straight to Flask, which silently enables flags that were meant to be
disabled. This normalizes them so ``MAIL_USE_TLS="False"`` disables TLS.

Args:
    value: The raw value from ``os.environ`` or ``payload.json``.
    default: The value to return when ``value`` is ``None``.

Returns:
    The coerced boolean.*
- `sanitize_path` (line 49) `def sanitize_path(path)` - *Sanitiza una ruta de archivo para prevenir LFI y path traversal.
- Elimina caracteres peligrosos
- Normaliza la ruta
- Asegura que no contenga '..' o rutas absolutas*

**Methods:**
- `load_payload` (line 168) `def load_payload()` - *Load non-secret application configuration from ``payload.json``.

A local ``.env`` file is loaded first (when ``python-dotenv`` is available)
so environment-based secrets are populated before :class:`Config` reads them.

Returns:
    The parsed configuration dictionary.*
- `__init__` (line 145) `def __init__(self, config_dict)`
- `__getitem__` (line 165) `def __getitem__(self, key)`

#### `__init__.py`
**Path:** `views/__init__.py`

*No symbols extracted*

#### `about.py`
**Path:** `views/about.py`

**Functions:**
- `about` (line 6) `def about()` - *Render the About page.*

#### `account.py`
**Path:** `views/account.py`
**File Doc:** *Account settings page and the deniable vault JSON API (QV-DENIABLE-1).  The settings page is a normal, universal part of every authenticated account, regardless of role. It deliberately does not advertise the deniable vault as a special feature: the page looks the same for everyone, and the API never tells the caller whether a hidden vault is configured. That is by design. A deniable vault only protects the user if its presence leaves no evidence; an obvious "you have a hidden vault" indicator would make coercion more effective, not less.  Routes:  - ``GET    /account``            : render the account settings page - ``GET    /api/account/vault``  : return the user's opaque container, minting an indistinguishable random one if the account has none yet - ``PUT    /api/account/vault``  : validate and store a container - ``DELETE /api/account/vault``  : reset the container to a fresh random one  The server validates container *structure* only; it never decrypts a slot or sees a passphrase (see :mod:`controllers.deniable_vault`).*

**Functions:**
- `get_deniable_vault_controller` (line 51) `def get_deniable_vault_controller()` - *Build a controller bound to the active app's database and config.

The database path and structural parameters are read from
``current_app.config`` so tests (which point the app at a temporary
database and may override limits) and production share one code path.*
- `settings` (line 65) `def settings()` - *Render the account settings page.

When the cover facade is enabled the decoy feature requires a deniable
passphrase, so the page asks for one. The server never learns whether a
passphrase has been set: it only exposes the instance-level facade flag.*
- `get_vault` (line 85) `def get_vault()` - *Return the user's container and the build parameters.

The response always includes an ``envelope`` (a random one is minted on
first access) and the structural ``parameters``. It never includes a
"configured" flag: whether the container holds real data is exactly
what must stay hidden.*
- `put_vault` (line 107) `def put_vault()` - *Validate and store a container for the user.*
- `delete_vault` (line 130) `def delete_vault()` - *Reset the user's container to a fresh random one.

Reset, not delete: removing the row would distinguish an account that
deactivated from one that never activated. A random container keeps the
"every account has one" invariant intact.*

#### `admin.py`
**Path:** `views/admin.py`

**Classes:**
- `UserEditForm` (line 141) `class UserEditForm(FlaskForm)` - *Form for editing user details.

Intentionally does NOT carry these fields:

* ``confirmation_token`` — rotated by the resend-confirmation
  endpoint, never hand-edited. A static token cannot expire and
  would either lock the user out or be reused forever.
* ``phone_verification_code`` — same reason; the column stores
  a hash, not the cleartext code, so a superadmin UI input is
  meaningless.
* KEM/SRP blob columns (srp_salt, srp_verifier, public_key,
  encrypted_private_key, kdf_salt) — the server has no UI to
  rewrite them. Modifying any of them would silently brick the
  user's login.

``password`` is also absent: the server is zero-knowledge, so a
"change password" UI lives in the user's own profile, not here.*
- `PlanForm` (line 174) `class PlanForm(FlaskForm)` - *Form for creating or editing a subscription plan.*

**Functions:**
- `_audit_action` (line 31) `def _audit_action(actor, action, target_user, ip, details)` - *Append one superadmin audit row with a single construction site.*
- `_channel_manager` (line 48) `def _channel_manager()` - *Build the disposable channel manager from env and app config.*
- `_s3_reachable` (line 54) `def _s3_reachable(timeout)` - *Return whether the Garage S3 endpoint answers a TCP probe.

The file inventory below fans out one listing per user, each
with its own retry budget. Probing once up front keeps a downed
object store from turning every panel view into a retry storm
in the logs. A closed port means every listing would fail
anyway, so skipping them loses nothing.*
- `_read_log_tail` (line 84) `def _read_log_tail(state_dir, limit)` - *Return the last lines of backend logs for operator diagnosis.

Only the superadmin panel sees this, and it never leaves the
server: Jinja autoescaping renders it as text. Missing logs
yield an empty string instead of an error.*
- `_channel_diagnostics` (line 116) `def _channel_diagnostics(manager)` - *Collect binary availability and paths without launching anything.*

**Methods:**
- `admin` (line 186) `def admin()` - *Plan catalog read view.

Plan CRUD lives at ``/admin<token>/plans`` and
``/admin<token>/plans/edit/<name>`` so a single page is not also
a destructive form. This view is now strictly a list of
available plans, with a per-row edit link.

User identity (list, edit, suspend, MFA reset, confirmation
rotation) is the superadmin panel's job and lives at
``/superadmin<token>``.*
- `superadmin_edit_user` (line 208) `def superadmin_edit_user(username)` - *Full profile edit for a single user.

Lives under ``/superadmin<token>`` because every field here touches
identity directly (role, verifications, quota, subscription). Admin
role no longer has access: the superadmin panel is the only place
that can rewrite those columns.

Fields intentionally NOT editable through this form:

* ``confirmation_token`` — rotated by the resend-confirmation
  endpoint, never hand-edited (a static token cannot expire).
* ``phone_verification_code`` — same reason, lives in a hashed
  column anyway so even a superadmin should not see it.
* KEM/SRP blob columns (srp_salt, srp_verifier, public_key,
  encrypted_private_key, kdf_salt) — modifying any of these would
  silently brick the user's login. The server has no UI to rewrite
  them and never should.*
- `manage_plans` (line 313) `def manage_plans()` - *Handle plan management.*
- `edit_plan` (line 337) `def edit_plan(plan_name)` - *Handle editing of plan details.*
- `superadmin` (line 373) `def superadmin()` - *Superadmin identity-recovery and inventory panel.

Read-only by design. The server is zero-knowledge, so it can never
decrypt user content; instead this view surfaces the actions a
superadmin actually has to perform during incident response:

* inventory of encrypted file names per user (metadata only)
* last 50 audit log entries (who did what to which account)
* the user table with per-row privileged action buttons

Mutating actions live in the three POST handlers below. The GET
handler must never accept a side-effect query string, otherwise an
attacker could trigger a reset by luring a superadmin to follow a
crafted link.*
- `superadmin_reset_mfa` (line 476) `def superadmin_reset_mfa(username)` - *Disable MFA and clear the pending code for ``username``.

Used when a user loses their authenticator device. We do NOT
touch the password, the email, or the KEM material — losing a
second factor should not invalidate the rest of the identity.*
- `superadmin_resend_confirmation` (line 523) `def superadmin_resend_confirmation(username)` - *Issue a fresh ``confirmation_token`` for ``username``.

The token's 24h expiry is recomputed by ``update_user`` (see
models/user.py:337). If the user already verified, we still issue
a new token so the link can be reused as a magic-link login path
— useful when a user has lost access to their primary device.*
- `superadmin_toggle_suspend` (line 570) `def superadmin_toggle_suspend(username)` - *Flip ``subscription_status`` between active and inactive.

Suspension is a billing/operational lever (refuse new uploads,
block new devices) that does not require touching the KEM
material. Reactivation brings the user back into the same
position they were in before suspension.*
- `superadmin_channel_start` (line 620) `def superadmin_channel_start()` - *Start a disposable secure channel in the requested mode.

Accepts ``cloudflared``, ``tor``, or ``hybrid`` from the panel form.
Any other value is rejected so a crafted POST cannot smuggle a mode
the supervisor does not know. Audit details carry only the mode
plus address fingerprints, never the addresses themselves.*
- `superadmin_channel_stop` (line 659) `def superadmin_channel_stop()` - *Dispose the running channel and remove its addresses.*
- `superadmin_channel_rotate` (line 682) `def superadmin_channel_rotate()` - *Dispose current addresses and publish fresh ones in the same mode.*
- `admin_contacts` (line 705) `def admin_contacts()`

#### `auth.py`
**Path:** `views/auth.py`
**File Doc:** *Authentication and account-management views.  Routes:  - ``GET  /register``            : render the registration form - ``POST /register``            : create a new account from a zero-knowledge payload - ``GET  /login``               : render the login form - ``POST /api/srp/hello``       : SRP-6a step 1, returns salt and server challenge B - ``POST /api/srp/verify``      : SRP-6a step 2, returns server proof M2 and starts a session - ``GET  /logout``              : clear the session - ``GET  /confirm/<token>``     : mark an email as verified - ``GET/POST /verify_phone``    : enter the phone verification code - ``GET/POST /verify_mfa``      : enter the MFA code - ``POST /toggle_mfa``          : enable or disable MFA for the current user - ``GET  /contact``             : render and accept the contact form - ``GET  /api/auth/pubkey``     : return a user's hybrid public key - ``GET  /api/auth/user-keys``  : return the current user's keying material - ``GET  /api/csrf-token``      : issue the CSRF token for SPA use  Every state-changing JSON route is decorated with :func:`utils.security.json_csrf_protect` so a cross-origin request without the matching CSRF token is rejected with HTTP 403 and audited.*

**Classes:**
- `PhoneVerificationForm` (line 98) `class PhoneVerificationForm(FlaskForm)`
- `MFAForm` (line 103) `class MFAForm(FlaskForm)`
- `ContactForm` (line 108) `class ContactForm(FlaskForm)`
- `RegisterForm` (line 114) `class RegisterForm(FlaskForm)`
- `LoginForm` (line 124) `class LoginForm(FlaskForm)`

**Functions:**
- `role_required` (line 71) `def role_required()` - *Restrict a route to authenticated users holding one of the given roles.

The check is an intersection of ``VALID_ROLES`` and the caller-
supplied roles so a typo in a future route (e.g. ``role_required("user")``)
cannot accidentally grant access because the role never existed.*

**Methods:**
- `get_auth_controller` (line 132) `def get_auth_controller()`
- `show_register` (line 143) `def show_register()`
- `handle_register` (line 150) `def handle_register()`
- `login` (line 234) `def login()`
- `recover` (line 242) `def recover()` - *Render the QV-RECOVERY-1 account-recovery page.

Available to anonymous visitors: a forgotten password means the
visitor cannot authenticate, by definition.*
- `_srp_key` (line 255) `def _srp_key()`
- `_recovery_key` (line 266) `def _recovery_key()`
- `srp_hello` (line 278) `def srp_hello()` - *First SRP-6a step: receive the client public value A, return salt and B.*
- `srp_verify` (line 299) `def srp_verify()` - *Second SRP-6a step: verify the client proof M1 and return server proof M2.*
- `logout` (line 337) `def logout()`
- `confirm_email` (line 344) `def confirm_email(token)`
- `verify_phone` (line 367) `def verify_phone()`
- `resend_phone_verification` (line 384) `def resend_phone_verification()` - *Re-send the phone verification code for an account.

The username is supplied as a query parameter by the verify-phone
template's resend form. The form carries the CSRF token, so the
app-wide CSRFProtect guard applies. The handler never reveals whether
the account exists: it always redirects back with a neutral message.*
- `verify_mfa` (line 407) `def verify_mfa()`
- `toggle_mfa` (line 429) `def toggle_mfa()`
- `contact` (line 454) `def contact()` - *Render the contact form and persist a message from the current user.

The page is only meaningful for authenticated users: messages are tied to
a ``user_id`` foreign key in ``contacts``. Anonymous visitors are sent
to the login page so they can sign in (or register) before contacting.*
- `get_public_key` (line 485) `def get_public_key()` - *Return a user's hybrid public key so the browser can wrap data to them.*
- `get_user_keys` (line 503) `def get_user_keys()` - *Provide the keys a user needs to decrypt their data client-side.

The caller must already be authenticated and asking for their own
material; the route refuses to return anyone else's keying data.*
- `get_recovery_bundle` (line 534) `def get_recovery_bundle()` - *Return the QV-RECOVERY-1 bundle for a username, if one was generated.

No authentication is required: a forgotten password by definition
means the caller cannot log in. The returned values are opaque to
anyone without the recovery code: ``encrypted_private_key_recovery``
is AES-256-GCM ciphertext keyed by a PBKDF2 derivation of the
recovery code, so exposing it to an unauthenticated caller does not
weaken the zero-knowledge guarantees.*
- `reset_with_recovery` (line 559) `def reset_with_recovery()` - *Reset SRP credentials and the password-wrapped private key via QV-RECOVERY-1.

The browser has already decrypted ``encrypted_private_key_recovery``
using a key derived from the recovery code and reconstructed the
account's public key from the recovered private key blob (see
``derivePublicKeyFromPrivateBlob`` in ``static/js/qv-crypto.js``).
That reconstruction is supplied as ``public_key_proof``: AES-GCM
authentication means a wrong recovery code fails to decrypt at all,
so only a caller who supplied the correct code can produce a
``public_key_proof`` that matches the stored ``public_key``
byte-for-byte. The underlying keypair and ``public_key`` are not
changed; only the SRP verifier and the password-wrapping of the
existing private key blob are replaced.*
- `get_csrf_token` (line 619) `def get_csrf_token()` - *Issue the CSRF token used by the SPA for state-changing JSON calls.*
- `decorator` (line 85) `def decorator(f)`
- `decorated_function` (line 87) `def decorated_function()`

#### `facade.py`
**Path:** `views/facade.py`
**File Doc:** *Cover facade HTTP integration: before-request cover and the gate endpoint.  When the facade is configured, anonymous visitors to the protected pages see a configurable cover instead of the application, and ``POST /gate`` accepts the secret phrase. A correct phrase stores the signed ticket in the session and redirects to the ordinary login page; a miss keeps the cover. Nothing in the response distinguishes a miss from a hit to an unauthenticated observer.*

**Functions:**
- `register_facade` (line 33) `def register_facade(app)` - *Install the facade on ``app`` when it is enabled and configured.*
- `_build_cover_service` (line 71) `def _build_cover_service(config)`
- `_ticket_mode` (line 86) `def _ticket_mode(gate)`
- `render_cover` (line 41) `def render_cover()`
- `_facade_cover` (line 48) `def _facade_cover()`
- `facade_gate` (line 60) `def facade_gate()`

#### `faq.py`
**Path:** `views/faq.py`

**Functions:**
- `faq` (line 7) `def faq()` - *Render the About page.*
- `landing` (line 12) `def landing()` - *Render the About page.*

#### `file.py`
**Path:** `views/file.py`

**Classes:**
- `UploadForm` (line 15) `class UploadForm(FlaskForm)` - *Formulario para la subida de archivos cifrados.*

**Methods:**
- `upload` (line 25) `def upload()` - *Maneja la subida de archivos cifrados desde el cliente.*
- `download` (line 56) `def download(filename)` - *Provide the encrypted file and its key for client-side decryption.

The filename comes from the URL and is used to look up a key under
the authenticated user's S3 prefix. The server never lets the
filename escape that prefix: any ``/``, ``\``, ``..`` or control
character is rejected before the S3 key is constructed, so a
crafted ``filename`` like ``../admin/files/x`` cannot exfiltrate
another user's ciphertext.*

#### `message.py`
**Path:** `views/message.py`

**Classes:**
- `MessageForm` (line 19) `class MessageForm(FlaskForm)` - *Form for sending messages.*

**Methods:**
- `messages` (line 29) `def messages()` - *Render the messages page; the browser handles all crypto.

Sending happens via the JSON API in /api/secure_message below.*
- `api_secure_message` (line 49) `def api_secure_message()` - *Accept an opaque end-to-end encrypted message envelope.

The browser already generated the CEK, encrypted the message body with
AES-256-GCM, and wrapped the CEK to the recipient's and sender's
hybrid public keys. The server stores only the opaque material.*

#### `privacy.py`
**Path:** `views/privacy.py`

**Functions:**
- `privacy` (line 6) `def privacy()` - *Render the About page.*

#### `subscription.py`
**Path:** `views/subscription.py`

**Classes:**
- `SubscriptionForm` (line 24) `class SubscriptionForm(FlaskForm)` - *Formulario para seleccionar un plan de suscripción.*

**Methods:**
- `subscribe` (line 37) `def subscribe()` - *Maneja la selección de planes y el proceso de pago.*
- `payment_success` (line 86) `def payment_success()` - *Maneja el éxito del pago y actualiza el plan del usuario.*
- `__init__` (line 26) `def __init__(self)`

#### `sync.py`
**Path:** `views/sync.py`
**File Doc:** *End-to-end encrypted file synchronization views.  ``POST /secure_sync`` accepts an opaque encrypted payload from the SPA and stores it under the authenticated user's prefix in S3. The endpoint is CSRF-protected and rate-limited per (IP, user) pair to prevent the server from being used as a free file storage for an attacker who phished a session cookie.*

**Functions:**
- `secure_sync` (line 29) `def secure_sync()` - *Receive an already-encrypted file + wrapped FEK and persist them.

The server never sees the plaintext: the file body and the
wrapped key are opaque from the server's perspective. We only
enforce quota and basic input validation.*
- `sync_page` (line 79) `def sync_page()`

#### `terms.py`
**Path:** `views/terms.py`

**Functions:**
- `terms` (line 6) `def terms()` - *Render the About page.*

#### `views.py`
**Path:** `views/views.py`
**File Doc:** *Top-level non-API views: home page, account preferences, etc.*

**Classes:**
- `MFAEnableForm` (line 15) `class MFAEnableForm(FlaskForm)`

**Methods:**
- `home` (line 21) `def home()` - *Render the landing/home page.

The total user count is fetched with ``SELECT COUNT(*)`` directly
rather than loading every row into memory, so the cost is O(1)
regardless of the user table size.*

#### `wsgi.py`
**Path:** `wsgi.py`
**File Doc:** *WSGI entry point for production deployments.  Run with gunicorn (or any WSGI server) behind a TLS-terminating reverse proxy::  gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 2 \\ --access-logfile - --error-logfile - \\ wsgi:application  The reverse proxy (nginx, Caddy, ALB) terminates TLS and forwards ``X-Forwarded-Proto``. The factory wires up ProxyFix only when the operator sets ``QV_TRUSTED_PROXY=1`` so the request scheme is reconstructed correctly inside Flask.  The Werkzeug dev server is never reachable through this module; that keeps the public surface small.*

*No symbols extracted*

### SH (5 files)

#### `install.sh`
**Path:** `install.sh`
**File Doc:** *install.sh: Script para instalar prerrequisitos y compilar el proyecto postcuantum Fecha: 26 de junio de 2025 Autor: Grok 3 (xAI)*

*No symbols extracted*

#### `make.sh`
**Path:** `make.sh`

*No symbols extracted*

#### `garage-init.sh`
**Path:** `scripts/garage-init.sh`
**File Doc:** *Bootstrap a fresh Garage deployment for QuantumVault.  What this does: 1. Waits for the admin API to respond. 2. Connects the local node to the cluster (single-node layout). 3. Creates the quantumvault bucket. 4. Creates a scoped API key with read+write on that bucket only. 5. Emits the credentials for .env (S3_ACCESS_KEY / S3_SECRET_KEY).  Usage: docker compose up -d garage scripts/garage-init.sh  The script reads GARAGE_RPC_SECRET and GARAGE_ADMIN_TOKEN from the .env file (or the environment) so the admin API can be authenticated.*

**Functions:**
- `upsert_env` (line 35) - *Insert or update a KEY=value line in .env without disturbing other lines.*

#### `garage-native.sh`
**Path:** `scripts/garage-native.sh`
**File Doc:** *Run Garage (S3-compatible object storage) natively, without Docker.  Idempotent: if the S3 API is already reachable on :3900 it does nothing. Otherwise it ensures a local garage binary exists (downloading a pinned release and verifying its checksum when necessary), writes a development config with project-local data directories under .run/garage, starts the server in the background, provisions the bucket and a scoped access key, and writes the resulting S3 credentials into .env so the app picks them up.  Override knobs via the environment: GARAGE_VERSION   release to download                 (default 1.0.1) GARAGE_BIN       path to (or destination for) garage (default .run/garage-bin/garage) GARAGE_SHA256    pin the binary checksum             (optional, recommended)  This script is invoked by `make garage-up`, which `make run` calls as a prerequisite when Docker is not available.*

**Functions:**
- `upsert_env` (line 46) - *Insert or update a KEY=value line in .env without disturbing other lines.*
- `s3_reachable` (line 56)
- `gcmd` (line 141)

#### `test.sh`
**Path:** `test.sh`

*No symbols extracted*
