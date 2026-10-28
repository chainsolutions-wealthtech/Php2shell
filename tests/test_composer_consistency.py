"""Tests of local-only Composer metadata consistency; never contact an asset."""
import json
import os
import socket
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.composer_consistency import audit_composer_consistency, _read_local_json


class ComposerConsistencyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def put(self, name, obj):
        (self.root / name).write_text(json.dumps(obj), encoding="utf-8")

    def audit(self):
        return audit_composer_consistency(self.root)

    def rules(self):
        return [x["rule"] for x in self.audit()["observations"]]

    def test_missing_both_artifacts_never_claims_verified(self):
        result = self.audit()
        self.assertEqual(result["status"], "insufficient_local_evidence")
        self.assertFalse(result["installed_versions_verified"])
        self.assertFalse(result["authorized_for_patch"])
        self.assertFalse(result["network_requests_made"])

    def test_exact_pin_match_and_platform_requirement(self):
        self.put("composer.json", {"require": {"php": "^8.3", "ext-json": "*", "acme/pkg": "1.2.3"}})
        self.put("composer.lock", {"packages": [{"name": "acme/pkg", "version": "v1.2.3"}]})
        self.assertEqual(self.rules(), [])
        self.assertEqual(self.audit()["counts"]["direct_package_requirements"], 1)

    def test_missing_direct_dependency_is_review_not_vulnerability(self):
        self.put("composer.json", {"require": {"acme/pkg": "^1.2"}})
        self.put("composer.lock", {"packages": []})
        self.assertIn("DECLARED_PACKAGE_ABSENT_FROM_LOCK", self.rules())
        self.assertEqual(self.audit()["vulnerability_applicability"], "insufficient_evidence")

    def test_virtual_provider_does_not_claim_missing_package(self):
        self.put("composer.json", {"require": {"psr/log-implementation": "^1.0"}})
        self.put("composer.lock", {"packages": [{"name": "acme/logger", "version": "2.0.0", "provide": {"psr/log-implementation": "1.0"}}]})
        self.assertEqual(self.rules(), ["VIRTUAL_OR_REPLACED_REQUIREMENT_REVIEW"])

    def test_exact_pin_mismatch_but_no_semver_range_solver(self):
        self.put("composer.json", {"require": {"acme/pkg": "1.2.3", "acme/other": "^3.0"}})
        self.put("composer.lock", {"packages": [{"name": "acme/pkg", "version": "1.2.4"}, {"name": "acme/other", "version": "2.0.0"}]})
        self.assertEqual(self.rules(), ["EXACT_PIN_DIFFERS_FROM_LOCK"])

    def test_duplicate_lock_across_groups(self):
        self.put("composer.json", {})
        self.put("composer.lock", {"packages": [{"name": "acme/pkg", "version": "1.0.0"}], "packages-dev": [{"name": "acme/pkg", "version": "2.0.0"}]})
        self.assertIn("DUPLICATE_LOCK_PACKAGE", self.rules())

    def test_duplicate_direct_requirement(self):
        self.put("composer.json", {"require": {"acme/pkg": "^1"}, "require-dev": {"acme/pkg": "^2"}})
        self.put("composer.lock", {"packages": [{"name": "acme/pkg", "version": "1.0.0"}]})
        self.assertIn("DUPLICATE_DIRECT_REQUIREMENT", self.rules())

    def test_duplicate_json_key_fails_closed(self):
        (self.root / "composer.json").write_text('{"require":{},"require":{}}', encoding="utf-8")
        self.put("composer.lock", {})
        result = self.audit()
        self.assertEqual(result["status"], "insufficient_local_evidence")
        self.assertIn("LOCAL_ARTIFACT_INVALID_OR_UNREADABLE_JSON", self.rules())

    def test_symlink_lock_refused(self):
        self.put("real.lock", {"packages": []})
        try:
            (self.root / "composer.lock").symlink_to(self.root / "real.lock")
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unsupported")
        self.put("composer.json", {})
        self.assertEqual(self.audit()["status"], "insufficient_local_evidence")
        self.assertIn("LOCAL_ARTIFACT_UNSAFE_OR_UNREADABLE", self.rules())

    def test_malformed_lock_group(self):
        self.put("composer.json", {})
        self.put("composer.lock", {"packages": "not-a-list"})
        self.assertEqual(self.audit()["status"], "insufficient_local_evidence")
        self.assertIn("INVALID_LOCK_GROUP", self.rules())

    def test_non_string_requirement_key_is_generic_error(self):
        self.put("composer.json", {"require": {"acme/pkg": "^1", "1": "^2"}})
        self.put("composer.lock", {})
        self.assertIn("INVALID_REQUIREMENT_ENTRY", self.rules())

    def test_invalid_package_identity_not_echoed(self):
        self.put("composer.json", {})
        self.put("composer.lock", {"packages": [{"name": "SECRET_TOKEN", "version": "1.0.0", "dist": {"url": "https://secret.invalid"}}]})
        result = self.audit()
        self.assertEqual(result["status"], "insufficient_local_evidence")
        self.assertNotIn("SECRET_TOKEN", json.dumps(result))
        self.assertNotIn("secret.invalid", json.dumps(result))

    def test_metadata_secrets_not_reflected(self):
        self.put("composer.json", {"repositories": [{"url": "https://token:SECRET@host.invalid"}], "require": {"acme/pkg": "1.0.0"}})
        self.put("composer.lock", {"packages": [{"name": "acme/pkg", "version": "1.0.0", "source": {"url": "https://token:SECRET@host.invalid"}}]})
        self.assertNotIn("SECRET", json.dumps(self.audit()))
        self.assertNotIn("host.invalid", json.dumps(self.audit()))

    def test_oversized_artifact_rejected(self):
        (self.root / "composer.lock").write_bytes(b" " * 2_000_001)
        self.put("composer.json", {})
        self.assertIn("LOCAL_ARTIFACT_UNSAFE_OR_TOO_LARGE", self.rules())

    def test_no_socket_connect(self):
        self.put("composer.json", {})
        self.put("composer.lock", {})
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            self.assertEqual(self.audit()["status"], "review_required")

    def test_deterministic_observations(self):
        self.put("composer.json", {"require": {"z/z": "1.0.0", "a/a": "2.0.0"}})
        self.put("composer.lock", {"packages": []})
        self.assertEqual([x["package"] for x in self.audit()["observations"]], ["a/a", "z/z"])

    def test_root_must_be_directory(self):
        path = self.root / "notdir"
        path.write_text("x")
        with self.assertRaises(ValueError):
            audit_composer_consistency(path)


    def test_missing_nofollow_support_rejects_even_regular_metadata(self):
        self.put("composer.json", {"require": {"acme/pkg": "1.0.0"}})
        self.put("composer.lock", {"packages": [{"name": "acme/pkg", "version": "1.0.0"}]})
        with patch.object(os, "O_NOFOLLOW", 0, create=True):
            result = self.audit()
        self.assertEqual(result["status"], "insufficient_local_evidence")
        self.assertIn("LOCAL_ARTIFACT_UNSAFE_OR_UNREADABLE",
                      [row["rule"] for row in result["observations"]])
        self.assertFalse(result["installed_versions_verified"])
        self.assertFalse(result["authorized_for_patch"])

    def test_mutation_after_read_is_rejected_by_descriptor_metadata(self):
        self.put("composer.json", {"require": {"acme/pkg": "1.0.0"}})
        original_fstat = os.fstat
        calls = 0
        path = self.root / "composer.json"

        def mutate_on_second_stat(fd):
            nonlocal calls
            calls += 1
            if calls == 2:
                with path.open("ab") as output:
                    output.write(b" ")
            return original_fstat(fd)

        with patch("app.composer_consistency.os.fstat",
                   side_effect=mutate_on_second_stat):
            value, error = _read_local_json(self.root, "composer.json")
        self.assertIsNone(value)
        self.assertEqual(error, "UNSAFE_OR_UNREADABLE")
        self.assertEqual(calls, 2)


if __name__ == "__main__":
    unittest.main()
