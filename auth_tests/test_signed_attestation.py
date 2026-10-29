"""RED tests for an isolated external Ed25519 attestation verifier.

The test signer is ephemeral and test-only; no keys, JWTs, OAuth sessions,
privileges or production service are minted by the application.
"""
import base64
import json
import unittest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

from app.signed_attestation import verify_external_attestation


def b64(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


class SignedAttestationContractTests(unittest.TestCase):
    def setUp(self):
        self.signer = Ed25519PrivateKey.generate()
        self.public_key = self.signer.public_key().public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw
        )
        self.keys = {"mcp-key-01": self.public_key}
        self.expected = {
            "subject": "operator-1", "project_id": "P2S-PROJECT-001",
            "asset_hostname": "site.example.com", "scope": "owned_source",
            "action": "source_read",
        }
        self.claims = {
            "iss": "mcp-trusted-authority",
            "aud": "php2shell-local-attestation-contract",
            "sub": "operator-1",
            "project_id": "P2S-PROJECT-001",
            "asset_hostname": "site.example.com",
            "scope": "owned_source",
            "action": "source_read",
            "mandate_id": "P2S-MANDATE-001",
            "iat": 1793163600, "nbf": 1793163600,
            "exp": 1793163720, "jti": "P2S-ATTEST-001",
        }
        self.now = 1793163650

    def token(self, claims=None, header=None, *, tamper_signature=False):
        head = {"typ": "p2s-mcp-attestation+jwt", "alg": "EdDSA",
                "kid": "mcp-key-01"} if header is None else header
        body = self.claims if claims is None else claims
        signed = (b64(json.dumps(head, separators=(",", ":")).encode())
                  + "." + b64(json.dumps(body, separators=(",", ":")).encode()))
        signature = self.signer.sign(signed.encode("ascii"))
        if tamper_signature:
            signature = signature[:-1] + bytes([signature[-1] ^ 1])
        return signed + "." + b64(signature)

    def verify(self, token=None, expected=None, now=None, *,
               keys=None, revoked=None, issuer=None, audience=None):
        return verify_external_attestation(
            token if token is not None else self.token(),
            trusted_public_keys=self.keys if keys is None else keys,
            expected_issuer=issuer if issuer is not None else self.claims["iss"],
            expected_audience=(audience if audience is not None
                               else self.claims["aud"]),
            request_binding=self.expected if expected is None else expected,
            observed_at_epoch=self.now if now is None else now,
            revocation_checker=(revoked if revoked is not None
                                else lambda jti: False),
        )

    def test_valid_signature_and_binding_are_not_execution_permission(self):
        decision = self.verify()
        self.assertTrue(decision["signature_verified"])
        self.assertTrue(decision["claims_bound_to_request"])
        self.assertTrue(decision["revocation_checked"])
        self.assertEqual(decision["decision"],
                         "VERIFIED_ATTESTATION_NOT_EXECUTION_ADMISSION")
        self.assertFalse(decision["authorized"])
        self.assertFalse(decision["execution_enabled"])
        self.assertFalse(decision["mcp_claim_verified"])
        self.assertNotIn("P2S-MANDATE-001", json.dumps(decision))
        self.assertNotIn("operator-1", json.dumps(decision))

    def test_signature_tamper_unknown_key_and_alg_none_refused(self):
        with self.assertRaises(ValueError):
            self.verify(self.token(tamper_signature=True))
        with self.assertRaises(ValueError):
            self.verify(keys={"different": self.public_key})
        with self.assertRaises(ValueError):
            self.verify(self.token(header={"alg": "none",
                             "typ": "p2s-mcp-attestation+jwt",
                             "kid": "mcp-key-01"}))
        with self.assertRaises(ValueError):
            self.verify(keys={"mcp-key-01": b"x" * 31})

    def test_binding_enforces_subject_project_asset_action_and_scope(self):
        for key in self.expected:
            with self.subTest(key=key):
                changed = dict(self.expected)
                changed[key] = "other" if key != "scope" else "public_metadata"
                with self.assertRaises(ValueError):
                    self.verify(expected=changed)

    def test_expiration_future_issuance_and_long_lifetime_refused(self):
        for observed in (self.claims["nbf"] - 1,
                         self.claims["exp"],
                         self.claims["iat"] - 10):
            with self.subTest(observed=observed), self.assertRaises(ValueError):
                self.verify(now=observed)
        longer = dict(self.claims, exp=self.claims["iat"] + 86400)
        with self.assertRaises(ValueError):
            self.verify(self.token(longer))

    def test_wrong_issuer_and_audience_refused(self):
        with self.assertRaises(ValueError):
            self.verify(issuer="another-authority")
        with self.assertRaises(ValueError):
            self.verify(audience="another-service")

    def test_revocation_check_is_mandatory_and_fails_closed(self):
        with self.assertRaises(ValueError):
            self.verify(revoked=lambda _: True)
        with self.assertRaises(ValueError):
            self.verify(revoked=lambda _: None)
        with self.assertRaises(ValueError):
            self.verify(revoked=lambda _: 0)
        with self.assertRaises(ValueError):
            verify_external_attestation(
                self.token(), trusted_public_keys=self.keys,
                expected_issuer=self.claims["iss"],
                expected_audience=self.claims["aud"],
                request_binding=self.expected, observed_at_epoch=self.now,
                revocation_checker=None
            )

    def test_wrong_action_not_transitively_granted(self):
        for action in ("patch_propose", "patch_apply", "deploy", "public_crawl"):
            with self.subTest(action=action):
                expected = dict(self.expected, action=action)
                with self.assertRaises(ValueError):
                    self.verify(expected=expected)

    def test_malformed_and_oversized_tokens_rejected(self):
        for token in ("", "not.a.jwt", "x" * 5000,
                      self.token() + ".extra", self.token() + "="):
            with self.subTest(sample=token[:10]), self.assertRaises(ValueError):
                self.verify(token)

    def test_duplicate_json_keys_refused_even_if_signed(self):
        header = ('{"alg":"EdDSA","alg":"EdDSA",'
                  '"typ":"p2s-mcp-attestation+jwt","kid":"mcp-key-01"}')
        encoded = b64(header.encode("utf-8")) + "." + b64(
            json.dumps(self.claims).encode("utf-8"))
        token = encoded + "." + b64(self.signer.sign(encoded.encode("ascii")))
        with self.assertRaises(ValueError):
            self.verify(token)

    def test_untrusted_extra_claims_and_boolean_times_refused(self):
        for body in (dict(self.claims, admin=True),
                     dict(self.claims, exp=True),
                     dict(self.claims, scope="admin")):
            with self.assertRaises(ValueError):
                self.verify(self.token(body))


    def test_bound_base_path_exact_match_without_execution_grant(self):
        body = dict(self.claims, base_path="/client/private/")
        binding = dict(self.expected, base_path="/client/private/")
        decision = self.verify(self.token(body), expected=binding)
        self.assertTrue(decision["signature_verified"])
        self.assertFalse(decision["execution_enabled"])
        self.assertFalse(decision["authorized"])

    def test_bound_base_path_rejects_wrong_path_or_prefix_confusion(self):
        body = dict(self.claims, base_path="/client/private/")
        for path in ("/client/", "/client/private", "/client/private-other/",
                     "/client/private/report", "/client/elsewhere/", "/"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.verify(self.token(body),
                            expected=dict(self.expected, base_path=path))

    def test_missing_path_claim_or_request_binding_refused(self):
        binding = dict(self.expected, base_path="/client/private/")
        with self.assertRaises(ValueError):
            self.verify(expected=binding)
        with self.assertRaises(ValueError):
            self.verify(self.token(dict(self.claims, base_path="/")), expected=self.expected)

    def test_invalid_signed_and_request_paths_rejected(self):
        bad = ("", "client/private", "/client//private", "/client/../admin",
               "/client/./private", "/client/%2e%2e/", "/client?x=1",
               "/client\\\\admin", "//host.example.com", "/client/#f")
        for value in bad:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.verify(self.token(dict(self.claims, base_path=value)),
                            expected=dict(self.expected, base_path=value))

    def test_original_legacy_root_contract_still_verifies_but_never_authorizes(self):
        decision = self.verify()
        self.assertFalse(decision["authorized"])
        self.assertEqual(decision["verification_type"],
                         "EXTERNAL_ED25519_ATTESTATION_NOT_ADMISSION")



    def test_signed_p1_budgets_bound_to_request(self):
        body = dict(self.claims, scope="public_metadata", action="public_crawl",
                    base_path="/public/", max_pages=20, requests_per_minute=6)
        binding = dict(self.expected, scope="public_metadata", action="public_crawl",
                       base_path="/public/", max_pages=10, requests_per_minute=4)
        result = self.verify(self.token(body), expected=binding)
        self.assertTrue(result["signature_verified"])
        self.assertFalse(result["authorized"])
        self.assertFalse(result["execution_enabled"])

    def test_p1_requires_path_and_both_signed_budgets(self):
        base = dict(self.claims, scope="public_metadata", action="public_crawl")
        binding = dict(self.expected, scope="public_metadata", action="public_crawl")
        with self.assertRaises(ValueError):
            self.verify(self.token(base), expected=binding)
        for missing in ("base_path", "max_pages", "requests_per_minute"):
            signed = dict(base, base_path="/public/", max_pages=20,
                          requests_per_minute=6)
            request = dict(binding, base_path="/public/", max_pages=10,
                           requests_per_minute=4)
            signed.pop(missing)
            request.pop(missing)
            with self.subTest(missing=missing), self.assertRaises(ValueError):
                self.verify(self.token(signed), expected=request)

    def test_budget_escalation_and_missing_binding_are_refused(self):
        signed = dict(self.claims, max_pages=20, requests_per_minute=6)
        request = dict(self.expected, max_pages=21, requests_per_minute=7)
        with self.assertRaises(ValueError):
            self.verify(self.token(signed), expected=request)
        with self.assertRaises(ValueError):
            self.verify(self.token(signed), expected=self.expected)
        with self.assertRaises(ValueError):
            self.verify(expected=dict(self.expected,
                                      max_pages=20, requests_per_minute=6))

    def test_bool_zero_and_out_of_range_budgets_refused(self):
        for pages, rate in ((True, 6), (20, False), (0, 6), (20, 0),
                            (101, 6), (20, 31), (-1, 5)):
            with self.subTest(pages=pages, rate=rate), self.assertRaises(ValueError):
                self.verify(
                    self.token(dict(self.claims, max_pages=pages,
                                    requests_per_minute=rate)),
                    expected=dict(self.expected, max_pages=pages,
                                  requests_per_minute=rate),
                )

    def test_partial_budget_fields_rejected(self):
        for partial in ({"max_pages": 20}, {"requests_per_minute": 6}):
            with self.subTest(partial=partial), self.assertRaises(ValueError):
                self.verify(self.token(dict(self.claims, **partial)),
                            expected=dict(self.expected, **partial))



if __name__ == "__main__":
    unittest.main()
