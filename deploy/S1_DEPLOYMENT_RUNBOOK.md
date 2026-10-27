# PHP2SHELL + PHPPATCH — S1 deployment admission (NOT deployed)

## Authority and target

- Repository: `chainsolutions-wealthtech/Php2shell` (public; source only)
- S1 IPv4: `212.227.212.33` (verified MCP project context)
- Plesk subscription: `wealthtechinnovations.com`
- Console: `https://php2shell.wealthtechinnovations.com`
- Remediation frontend: `https://phppatch.wealthtechinnovations.com`
- Read-only observed Plesk folders:
  - `/var/www/vhosts/wealthtechinnovations.com/php2shell.wealthtechinnovations.com`
  - `/var/www/vhosts/wealthtechinnovations.com/phppatch.wealthtechinnovations.com`
  - corresponding `/var/www/vhosts/system/<hostname>` directories
- Both current sites show a Plesk placeholder, **not** a deployed application.
- Two hostnames, one future shared engine, separate authorization boundaries. Never create an independent second gateway.

## Live network evidence (2026-10-27)

DNS A on four authoritative IONOS nameservers => `212.227.212.33` for both.
The old IONOS parking AAAA records have been removed; MX still return `mx00.ionos.fr` and `mx01.ionos.fr`.
HTTPS direct with SNI on S1: `200` for both, trusted Let's Encrypt certificates. HTTP redirects to HTTPS with `301`.
PHP2SHELL certificate: 2026-10-27 through 2027-01-25.
PHPPATCH certificate: 2026-10-27 through 2027-01-25.
A stale recursive cache was observed (old parking IPv4 at Google DNS shortly after change).
An *internal S1* curl by hostname still failed after the public DNS fix: `curl (6)` for PHP2SHELL and `curl (35)` for PHPPATCH. Root cause **not yet confirmed**.
Evidence workflow: `.github/workflows/s1-readiness.yml`. It checks current DNS/HTTPS/TLS without credentials or writes.

## Release gates — block until every relevant prerequisite passes

1. Merge PR #1 (V0.1) only after review, verified CI and confirmed target HEAD.
2. Finish and independently review PR #2 (V0.2). Lexical indicators are **not** confirmed vulnerabilities and the demo CVE catalogue is unverified.
3. Implement actual API and web consoles with identity, RBAC, authentication, sessions, CSRF controls, audit log, rate limiting and secret separation.
4. Implement and review a governed, **scoped** GitHub-to-MCP-to-S1 deployment capability. MCP currently has no generic authorized Plesk provisioning, DNS management, or arbitrary SSH command action. Do not repurpose a `legacy_vhost` command for an unrelated target.
5. Restore reliable local DNS diagnostics on S1 via a separate governed MCP PR, with read-only `getent/dig/resolv.conf` and specifically authorized cache invalidation if shown necessary. Never flush global caches indiscriminately.
6. Obtain a deployment authorization identifying release commit SHA, exact target path(s), runtime user and the two subdomain mappings. Do not store credentials in this public repo.
7. Validate network preflight; CI tests, independent security review, artifact attestation, backups/rollback and documented health checks.
8. Only then deploy a locked image as non-root with minimal privileges, and run an end-to-end staging and production smoke test, including both auth boundaries, negative authorization tests and rollback.
9. Confirm PHP2SHELL can **report**; PHPPATCH may only prepare *proposed* patches until explicit approval. No automatic execution/patch on live systems.

## Separate services

| Host | Intended role | Deployment state |
|---|---|---|
| php2shell.wealthtechinnovations.com | Authenticated console, PHP asset inventory, permitted local project scan, evidence | NOT DEPLOYED |
| phppatch.wealthtechinnovations.com | Authenticated review/approval service for suggested diffs and CI reports | NOT DEPLOYED |

No production API or UI is presently implemented in the V0.1/V0.2 CLI repository.
Do **not** publish a remediation API at either address before the release gates are satisfied.

## Verification & rollback policy

- No writes to `main` outside governed PRs; record exact HEAD and CI run.
- `S1 readiness` workflow validates DNS/TLS/redirects but not production readiness.
- GitHub repository changes do not automatically deploy to Plesk.
- Keep existing vhosts in place. Never purge an existing site or alter other subscriptions.
- Prior to a rollout, snapshot the exact target content/config and register a rollback reference.
- On failed smoke test, revert to the last approved artifact through the same governed deployment route; do not modify protected host directories manually.
