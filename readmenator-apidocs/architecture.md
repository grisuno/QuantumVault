# QuantumVault Architecture and Execution Flows

[Back to index](index.md)

## Architecture Overview

14 components stacked in 4 dependency tiers (weighted Eades-Lin-Smyth ordering: arrows point from dependent to dependency, top to bottom). Labels are import counts, thick arrows the top quartile; 2 transitively implied edges are omitted. Dashed red arrows are upward dependencies: the smallest set of imports that closes every cycle and breaks the layering. Cyan components hold entry points. Interactive version: `readmenator-apidocs/index.html#/flows`.

Upward dependencies to fix first: `views: auth` -> `utils` (2 imports); `views: deniable_vault` -> `views: auth` (2 imports); `views: auth` -> `controllers` (1 imports); `controllers` -> `views: facade` (1 imports); `views: deniable_vault` -> `views: facade` (1 imports)

```mermaid
flowchart TB
    classDef cycle fill:#1f1530,stroke:#f472b6,color:#fce7f3,stroke-width:2px;
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    subgraph lane_0["Tier 1 - entry / orchestration"]
        direction LR
        n_c3["quantumvault/static/js<br/>9 files, 81 symbols<br/>Core / utility"]:::default
        n_c1["views: facade<br/>8 files, 47 symbols<br/>Presentation / entry"]:::entry
        n_d_views["views<br/>1 files, 0 symbols<br/>Presentation / entry"]:::default
        n_d_utils["utils<br/>3 files, 22 symbols<br/>Core / utility"]:::default
        n_d_scripts["scripts<br/>3 files, 32 symbols<br/>Core / utility"]:::default
        n_d_quantumvault["quantumvault<br/>2 files, 4 symbols<br/>Presentation / entry"]:::default
        n_d_models["models<br/>1 files, 0 symbols<br/>Business logic"]:::default
        n_d_controllers["controllers<br/>1 files, 0 symbols<br/>Presentation / entry"]:::default
        n_d__root_["(root)<br/>10 files, 12 symbols<br/>Core / utility"]:::entry
        n_c6["quantumvault<br/>2 files, 0 symbols<br/>Core / utility"]:::default
    end
    subgraph lane_1["Tier 2"]
        direction LR
        n_c4["controllers<br/>6 files, 76 symbols<br/>Presentation / entry"]:::entry
        n_c2["utils<br/>7 files, 50 symbols<br/>Core / utility"]:::cycle
    end
    subgraph lane_2["Tier 3"]
        direction LR
        n_c0["views: auth<br/>15 files, 127 symbols<br/>Presentation / entry"]:::cycle
    end
    subgraph lane_3["Tier 4 - foundation"]
        direction LR
        n_c5["views: deniable_vault<br/>5 files, 45 symbols<br/>Presentation / entry"]:::cycle
    end
    n_c0 ==>|"2"| n_c5
    n_c1 ==>|"2"| n_c2
    n_c1 -->|"1"| n_c4
    n_c2 ==>|"4"| n_c0
    n_c3 -->|"1"| n_c2
    n_c4 ==>|"6"| n_c0
    n_c2 <-.-|"2 upward"| n_c0
    n_c4 <-.-|"1 upward"| n_c0
    n_c1 <-.-|"1 upward"| n_c4
    n_c0 <-.-|"2 upward"| n_c5
    n_c1 <-.-|"1 upward"| n_c5
    linkStyle 6,7,8,9,10 stroke:#f87171,stroke-width:2px;
    n_c3 ~~~ n_c4
    n_c4 ~~~ n_c0
    n_c0 ~~~ n_c5
```

---

## Execution Flows

Entry points are scored from `__main__` guards, `main` functions, entry-style names and files, and call-graph sources. Each flow walks resolved calls in call-site order (depth <= 4, <= 40 steps); numbers give the call order, dashed arrows revisit an already expanded callee, red arrows are recursion. Interactive version with zoom and per-node docs: `readmenator-apidocs/index.html#/flows`.

### `server.main`

`server.go:11`, score 13: `main` in a compiled-language file; entry-style name `main`; defined in entry file `server.go`.

Call tree:

```mermaid
flowchart LR
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    n_server_go__main["server.main<br/>server.go:11"]:::entry
    n_server_go__handleConnection["server.handleConnection<br/>server.go:40"]:::default
    n_server_go__main -->|"1"| n_server_go__handleConnection
```

### `enc_dec.main`

`enc_dec.go:69`, score 12: `main` in a compiled-language file; entry-style name `main`; call-graph source with 3 calls.

Call tree:

```mermaid
flowchart LR
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    n_enc_dec_go__main["enc_dec.main<br/>enc_dec.go:69"]:::entry
    n_enc_dec_go__deriveAESKey["enc_dec.deriveAESKey<br/>enc_dec.go:20"]:::default
    n_enc_dec_go__encryptFile["enc_dec.encryptFile<br/>enc_dec.go:24"]:::default
    n_enc_dec_go__decryptFile["enc_dec.decryptFile<br/>enc_dec.go:45"]:::default
    n_enc_dec_go__main -->|"1"| n_enc_dec_go__deriveAESKey
    n_enc_dec_go__main -->|"2"| n_enc_dec_go__encryptFile
    n_enc_dec_go__main -->|"3"| n_enc_dec_go__decryptFile
```

### `app.main`

`app.py:21`, score 9: entry-style name `main`; defined in entry file `app.py`; called from the `__main__` guard.

Control flow:

```mermaid
flowchart TB
    classDef decision fill:#1e1b4b,stroke:#a78bfa,color:#ede9fe;
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    n_s1(["start app.main"]):::entry
    n_s2["Config(), load_payload(), get(), _is_production_like()<br/>Application configuration sourced from #96;#96;payl..."]:::default
    n_s3{"not (os.path.exists(cert) and os.path.exists(key))?"}:::decision
    n_s4["get(), create_app()<br/>Build and return a fully-configured Flask app..."]:::default
    n_s5(["end"]):::entry
    n_s1 --> n_s2
    n_s2 --> n_s3
    n_s3 -->|"yes"| n_s4
    n_s3 -->|"no"| n_s4
    n_s4 --> n_s5
```

Call tree:

```mermaid
flowchart LR
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef external fill:#1a1530,stroke:#a78bfa,color:#ede9fe;
    n_app_py__main["app.main<br/>app.py:21"]:::entry
    n_utils_utils_py__Config["utils.Config<br/>Application configuration sourced from #96;#96;payl...<br/>utils.py:103"]:::external
    n_utils_utils_py__load_payload["utils.load_payload<br/>Load non-secret application configuration fro...<br/>utils.py:168"]:::external
    n_app_py___is_production_like["app._is_production_like<br/>Return True if the runtime looks like a publi...<br/>app.py:58"]:::default
    n_quantumvault_app_factory_py__create_app["app_factory.create_app<br/>Build and return a fully-configured Flask app...<br/>app_factory.py:237"]:::external
    n_quantumvault_app_factory_py___configure_secret_key["app_factory._configure_secret_key<br/>Set #96;#96;app.config['SECRET_KEY']#96;#96; from env, pa...<br/>app_factory.py:160"]:::external
    n_quantumvault_app_factory_py___is_production["app_factory._is_production<br/>Return True unless the operator explicitly op...<br/>app_factory.py:71"]:::external
    n_quantumvault_app_factory_py___configure_session["app_factory._configure_session<br/>Apply session lifetime and cookie hardening.<br/>app_factory.py:203"]:::external
    n_quantumvault_app_factory_py___configure_logging["app_factory._configure_logging<br/>Wire up a structured application logger.<br/>app_factory.py:220"]:::external
    n_quantumvault_app_factory_py___build_talisman_kwargs["app_factory._build_talisman_kwargs<br/>Return kwargs to pass to #96;#96;Talisman#96;#96; based o...<br/>app_factory.py:119"]:::external
    n_quantumvault_app_factory_py___build_csp["app_factory._build_csp<br/>Return the strict Content-Security-Policy use...<br/>app_factory.py:82"]:::external
    n_controllers_file_py__FileController["file.FileController<br/>Persistence for end-to-end encrypted files an...<br/>file.py:51"]:::external
    n_controllers_sync_py__SyncController["sync.SyncController<br/>sync.py:7"]:::external
    n_views_facade_py__register_facade["facade.register_facade<br/>Install the facade on #96;#96;app#96;#96; when it is enab...<br/>facade.py:33"]:::external
    n_controllers_facade_py__from_mapping["facade.FacadeConfig.from_mapping<br/>Resolve configuration with environment, mappi...<br/>facade.py:181"]:::external
    n_controllers_facade_py___as_bool["facade._as_bool<br/>Coerce an environment or mapping value to a b...<br/>facade.py:79"]:::external
    n_controllers_facade_py__read["facade.FacadeConfig.read<br/>facade.py:189"]:::external
    n_controllers_facade_py___as_raw_text["facade._as_raw_text<br/>Coerce a value to text without substituting a...<br/>facade.py:106"]:::external
    n_controllers_facade_py___as_text["facade._as_text<br/>Coerce a value to non-empty text, falling bac...<br/>facade.py:98"]:::external
    n_controllers_facade_py___as_int["facade._as_int<br/>Coerce an environment or mapping value to an...<br/>facade.py:88"]:::external
    n_controllers_facade_py___as_paths["facade._as_paths<br/>Parse a comma-separated path list into a tupl...<br/>facade.py:111"]:::external
    n_controllers_facade_py__build["facade.FacadeGate.build<br/>Build a gate from configuration and the appli...<br/>facade.py:351"]:::external
    n_controllers_facade_py__from_config["facade.GatePhraseHasher.from_config<br/>Build a hasher using the cost parameters of #96;...<br/>facade.py:296"]:::external
    n_controllers_facade_py__GateTicket["facade.GateTicket<br/>Short-lived signed ticket binding a session t...<br/>facade.py:305"]:::external
    n_views_facade_py___build_cover_service["facade._build_cover_service<br/>facade.py:71"]:::external
    n_controllers_facade_py__cover_variables["facade.FacadeConfig.cover_variables<br/>Return the sanitizable cover variable payload.<br/>facade.py:166"]:::external
    n_app_py__main -->|"1"| n_utils_utils_py__Config
    n_app_py__main -->|"2"| n_utils_utils_py__load_payload
    n_app_py__main -->|"3"| n_app_py___is_production_like
    n_app_py__main -->|"4"| n_quantumvault_app_factory_py__create_app
    n_quantumvault_app_factory_py__create_app -.-> n_utils_utils_py__Config
    n_quantumvault_app_factory_py__create_app -.-> n_utils_utils_py__load_payload
    n_quantumvault_app_factory_py__create_app -->|"1"| n_quantumvault_app_factory_py___configure_secret_key
    n_quantumvault_app_factory_py___configure_secret_key -->|"1"| n_quantumvault_app_factory_py___is_production
    n_quantumvault_app_factory_py__create_app -->|"2"| n_quantumvault_app_factory_py___configure_session
    n_quantumvault_app_factory_py___configure_session -.-> n_quantumvault_app_factory_py___is_production
    n_quantumvault_app_factory_py__create_app -->|"3"| n_quantumvault_app_factory_py___configure_logging
    n_quantumvault_app_factory_py___configure_logging -.-> n_quantumvault_app_factory_py___is_production
    n_quantumvault_app_factory_py__create_app -->|"4"| n_quantumvault_app_factory_py___build_talisman_kwargs
    n_quantumvault_app_factory_py___build_talisman_kwargs -.-> n_quantumvault_app_factory_py___is_production
    n_quantumvault_app_factory_py___build_talisman_kwargs -->|"1"| n_quantumvault_app_factory_py___build_csp
    n_quantumvault_app_factory_py__create_app -->|"5"| n_controllers_file_py__FileController
    n_quantumvault_app_factory_py__create_app -->|"6"| n_controllers_sync_py__SyncController
    n_quantumvault_app_factory_py__create_app -->|"7"| n_views_facade_py__register_facade
    n_views_facade_py__register_facade -->|"1"| n_controllers_facade_py__from_mapping
    n_controllers_facade_py__from_mapping -->|"1"| n_controllers_facade_py___as_bool
    n_controllers_facade_py__from_mapping -->|"2"| n_controllers_facade_py__read
    n_controllers_facade_py__from_mapping -->|"3"| n_controllers_facade_py___as_raw_text
    n_controllers_facade_py__from_mapping -->|"4"| n_controllers_facade_py___as_text
    n_controllers_facade_py__from_mapping -->|"5"| n_controllers_facade_py___as_int
    n_controllers_facade_py__from_mapping -->|"6"| n_controllers_facade_py___as_paths
    n_views_facade_py__register_facade -->|"2"| n_controllers_facade_py__build
    n_controllers_facade_py__build -->|"1"| n_controllers_facade_py__from_config
    n_controllers_facade_py__build -->|"2"| n_controllers_facade_py__GateTicket
    n_views_facade_py__register_facade -->|"3"| n_views_facade_py___build_cover_service
    n_views_facade_py___build_cover_service -->|"1"| n_controllers_facade_py__cover_variables
```

Cross-file sequence:

```mermaid
sequenceDiagram
    autonumber
    participant p_app_py as app.py
    participant p_utils_utils_py as utils.py
    participant p_quantumvault_app_factory_py as app_factory.py
    participant p_controllers_file_py as file.py
    participant p_controllers_sync_py as sync.py
    participant p_views_facade_py as facade.py
    participant p_controllers_facade_py as facade.py
    p_app_py->>p_utils_utils_py: Config()
    p_app_py->>p_utils_utils_py: load_payload()
    p_app_py->>p_quantumvault_app_factory_py: create_app()
    p_quantumvault_app_factory_py->>p_controllers_file_py: FileController()
    p_quantumvault_app_factory_py->>p_controllers_sync_py: SyncController()
    p_quantumvault_app_factory_py->>p_views_facade_py: register_facade()
    p_views_facade_py->>p_controllers_facade_py: FacadeConfig.from_mapping()
    p_views_facade_py->>p_controllers_facade_py: FacadeGate.build()
    p_views_facade_py->>p_controllers_facade_py: FacadeConfig.cover_variables()
```

---
