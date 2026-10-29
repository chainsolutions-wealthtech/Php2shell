"""Scope-contract regression tests; synthetic claims, no network or claim issuance."""
from datetime import datetime, timedelta, timezone
import unittest

from claim_scope import ROOT, PROJECT, inspect_claim_scope

SHA = "a" * 40
NOW = "2026-10-29T19:35:00Z"
FUTURE = "2026-10-29T20:35:00Z"
WP = "P2S-WF-G01"
ACTOR = "agent-project-01"
BRANCH = "docs/canonical-continuity-20261027"


def project_claim(**changes):
    record = {
        "kind": "PROJECT_WP", "authority": PROJECT, "continuity_id": ROOT,
        "work_package": WP, "actor": ACTOR, "branch": BRANCH,
        "head_sha": SHA, "claim_id": "project-claim-001", "expires_at": FUTURE,
    }
    record.update(changes)
    return record


def resource_claim(**changes):
    record = {
        "kind": "EXTERNAL_RESOURCE", "authority": "Patricked-code/MCP",
        "continuity_id": ROOT, "work_package": WP, "actor": ACTOR,
        "branch": BRANCH, "head_sha": SHA, "claim_id": "resource-claim-001",
        "expires_at": FUTURE, "resource": "S1:php2shell",
    }
    record.update(changes)
    return record


def check(**overrides):
    values = {
        "wp_id": WP, "actor": ACTOR, "branch": BRANCH,
        "head_sha": SHA, "observed_at": NOW,
        "project_claim": project_claim(),
    }
    values.update(overrides)
    return inspect_claim_scope(**values)


class ClaimScopeTests(unittest.TestCase):
    def test_project_claim_is_not_execution_permission(self):
        result = check()
        self.assertTrue(result["scope_consistent"])
        self.assertFalse(result["authority_verified"])
        self.assertFalse(result["execution_authorized"])
        self.assertEqual(result["external_resource_claim"], "NOT_REQUIRED")

    def test_mcp_development_claim_cannot_claim_project_wp(self):
        result = check(project_claim=project_claim(kind="MCP_DEVELOPMENT", authority="Patricked-code/MCP"))
        self.assertFalse(result["scope_consistent"])
        self.assertIn("PROJECT_CLAIM_SCOPE_KIND", result["errors"])
        self.assertIn("PROJECT_CLAIM_SCOPE_AUTHORITY", result["errors"])

    def test_missing_project_claim(self):
        self.assertIn("PROJECT_CLAIM_NOT_ATTESTED", check(project_claim=None)["errors"])

    def test_project_claim_wrong_work_package(self):
        self.assertIn("PROJECT_CLAIM_SCOPE_WORK_PACKAGE",
                      check(project_claim=project_claim(work_package="P2S-WF-G02"))["errors"])

    def test_project_claim_wrong_branch(self):
        self.assertIn("PROJECT_CLAIM_SCOPE_BRANCH",
                      check(project_claim=project_claim(branch="main"))["errors"])

    def test_project_claim_wrong_head(self):
        self.assertIn("PROJECT_CLAIM_SCOPE_HEAD_SHA",
                      check(project_claim=project_claim(head_sha="b" * 40))["errors"])

    def test_expired_project_claim(self):
        self.assertIn("PROJECT_CLAIM_EXPIRED",
                      check(project_claim=project_claim(expires_at=NOW))["errors"])

    def test_naive_expiry_is_rejected(self):
        self.assertIn("PROJECT_CLAIM_INVALID_EXPIRY",
                      check(project_claim=project_claim(expires_at="2026-10-29T21:00:00"))["errors"])

    def test_invalid_observation_time(self):
        self.assertIn("INVALID_OBSERVATION_TIME", check(observed_at="invalid")["errors"])

    def test_missing_external_claim(self):
        result = check(external_resource="S1:php2shell")
        self.assertFalse(result["scope_consistent"])
        self.assertIn("RESOURCE_AUTHORITY_NOT_ATTESTED", result["errors"])

    def test_project_claim_is_not_resource_claim(self):
        result = check(external_resource="S1:php2shell", resource_claim=project_claim())
        self.assertIn("RESOURCE_CLAIM_SCOPE_KIND", result["errors"])
        self.assertIn("RESOURCE_CLAIM_SCOPE_RESOURCE", result["errors"])

    def test_matching_external_claim_still_not_verified(self):
        result = check(external_resource="S1:php2shell", resource_claim=resource_claim())
        self.assertTrue(result["scope_consistent"])
        self.assertFalse(result["authority_verified"])
        self.assertFalse(result["execution_authorized"])

    def test_wrong_external_resource_rejected(self):
        result = check(external_resource="S1:phppatch", resource_claim=resource_claim())
        self.assertIn("RESOURCE_CLAIM_SCOPE_RESOURCE", result["errors"])

    def test_unexpected_resource_claim_rejected(self):
        result = check(resource_claim=resource_claim())
        self.assertIn("UNEXPECTED_EXTERNAL_RESOURCE_CLAIM", result["errors"])

    def test_future_issued_project_claim_is_rejected(self):
        result = check(project_claim=project_claim(issued_at="2026-10-29T20:00:00Z"))
        self.assertIn("PROJECT_CLAIM_FUTURE_ISSUED", result["errors"])
        self.assertFalse(result["scope_consistent"])

    def test_invalid_issued_at_is_rejected(self):
        result = check(project_claim=project_claim(issued_at="not-a-time"))
        self.assertIn("PROJECT_CLAIM_INVALID_ISSUED_AT", result["errors"])

    def test_claim_expiry_before_issuance_is_rejected(self):
        result = check(project_claim=project_claim(issued_at="2026-10-29T21:00:00Z"))
        self.assertIn("PROJECT_CLAIM_INVALID_INTERVAL", result["errors"])

    def test_external_resource_claim_future_issuance_is_rejected(self):
        result = check(external_resource="S1:php2shell", resource_claim=resource_claim(
            issued_at="2026-10-29T21:00:00Z"))
        self.assertIn("RESOURCE_CLAIM_FUTURE_ISSUED", result["errors"])
        self.assertFalse(result["execution_authorized"])

    def test_invalid_head_rejected(self):
        self.assertIn("INVALID_HEAD_SHA", check(head_sha="bad")["errors"])

if __name__ == "__main__":
    unittest.main()
