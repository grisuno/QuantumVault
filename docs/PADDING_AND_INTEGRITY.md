# Metadata-size concealment and code integrity (QV-PAD-1, QV-SRI-1)

Two complementary mitigations for the issues raised against browser-based
encryption: ciphertext lengths no longer reveal exact plaintext sizes, and
the browser refuses to run any script or stylesheet whose bytes drifted from
the audited source.

## QV-PAD-1: fixed-bucket padding

Every message and file plaintext is framed client-side before AES-256-GCM as

    LENGTH_PREFIX || PLAINTEXT || RANDOM_PAD

where `LENGTH_PREFIX` is the true length as a 4-byte big-endian integer and
`RANDOM_PAD` fills the remainder of the bucket. The wire then carries only
`bucket + 28` bytes of ciphertext (12-byte IV plus 16-byte GCM tag), so a
network observer learns the bucket, never the exact size.

### Bucket tables

| Kind    | Buckets (plaintext bytes)                                              | Env override              |
| ------- | ---------------------------------------------------------------------- | ------------------------- |
| Message | 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536                      | `QV_PAD_MESSAGE_BUCKETS`  |
| File    | 65536 … 10485760 (powers of two plus the 10 MiB cap)                   | `QV_PAD_FILE_BUCKETS`     |

Both sides share one table: `utils/padding.py` (Python) and
`static/js/qv-padding.js` (browser). `tools/verify_build.py` fails when the
tables drift apart. Oversized payloads are rejected with `PaddingError` in
Python and an exception in the browser; there is no silent truncation.

### Server enforcement

The server decodes each envelope and accepts only ciphertext lengths equal
to a bucket plus GCM overhead (`controllers/message.py`,
`controllers/file.py`). An unpadded or downgraded client is rejected, so one
careless client cannot re-open the size oracle for everyone else.

### Cache safety

Padding bytes are drawn fresh from the OS CSPRNG (`secrets.token_bytes` /
`crypto.getRandomValues`) on every envelope and are never stored, reused, or
cached: there is no API that accepts caller-supplied pad bytes and no cache
entry that holds them. The only cached value is the immutable bucket table
itself (`functools.lru_cache` keyed by configuration fingerprint), which
reveals at most which operator configuration is active, never any message
content or length. Bucket lookup always scans the full table so the
iteration count is independent of the matched bucket.

## QV-SRI-1: Subresource Integrity and reproducible builds

`static/sri_manifest.json` pins the SHA-384 hash of every first-party script
and stylesheet plus every pinned CDN URL. Templates render integrity
attributes through the `sri_integrity` Jinja global, so hashes update by
regenerating one file instead of editing every template.

Known limitation: ES-module `import` statements (the `vendor/` bundles loaded
by `qv-crypto.js`) cannot carry SRI attributes. They are protected at rest by
same-origin serving, at load by the strict CSP (`script-src 'self'` plus the
pinned CDN list), and at audit time by `verify_build`, which detects any byte
drift. Vendoring a new upstream version is therefore a two-step change: copy
the files, then regenerate the manifest.

Third-party beacons were removed rather than pinned: the Cloudflare beacon
and the metadl plugin on the landing page, and Google Fonts on the auth
pages, sent every visitor's IP to an outside party. No analytics or font CDN
remains; the interface falls back to system fonts.

### Operator workflow

```bash
./.venv/bin/python tools/generate_sri.py   # after any static/ or CDN change
./.venv/bin/python tools/verify_build.py   # offline CI check, fails closed
make sri            # regenerate the manifest (network for CDN pins)
make verify-build   # offline verification gate
```

`generate_sri.py --offline` refreshes local pins while reusing the committed
CDN hashes, for air-gapped builds. `verify_build.py` additionally rejects any
template that references an unpinned script or stylesheet, so a new CDN
dependency cannot slip in without a hash.

## What this does not fix

Padding hides sizes, not endpoints or timing: IP-level anonymity still needs
Tor or a VPN, and interactive timing correlation is out of scope. SRI proves
the browser received the audited bytes; it cannot prove the server is honest
the next time. High-risk deployments should serve the audited bundle from
immutable storage (content-addressed hosting or a locally verified copy) and
re-run `verify_build` on every deploy.
