# Governance and non-regression

No code changes to third-party systems. No remote active tests in v0.1. Public assets are metadata-only. Ownership must be evidenced for source-level operations. Any future patch requires a reviewed diff, tests, explicit approval, rollback plan and audit trail. CI has read-only GitHub permissions. No secrets in repository. Treat remote headers as untrusted; do not infer vulnerability solely from a technology fingerprint.
