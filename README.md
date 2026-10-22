# PHP2SHELL — Defensive prototype (v0.1)

An **offline-first** PHP runtime version triage and authorization-scoped inventory prototype. It **does not scan websites, retrieve remote source code, exploit vulnerabilities, or deploy patches**.

## Quick start

```bash
python -m unittest discover -s tests -v
python -m app.cli inventory --file lab/targets.json
python -m app.cli check-version --php 8.3.34
```

## Scope model

- `public_metadata`: declared public asset, no source-code access or active probes.
- `owned_source`: only when authorization evidence is supplied. This release does not perform source inspection.

## Important limits

- CVE-to-version mappings are a **static seed requiring validation against official PHP/vendor advisories before production use**.
- Version comparison is not proof of exploitability; downstream vendor backports may differ.
- The Docker PHP lab image uses a current maintained PHP 8.3 image and **does not reproduce PHP 8.3.34**. The 8.3.34 scenario is simulated as version metadata in the CLI.
- This is a runnable foundation, **not a deployed agent or an autonomous remediation service**.

## Roadmap

1. Advisory ingestion with source provenance and signed review.
2. Authorized local source analyzers and dependency manifests.
3. Dry-run patch proposals with test and approval gates.
4. PDF/JSON reporting and immutable audit events.
5. Authenticated dashboard and worker queue.
