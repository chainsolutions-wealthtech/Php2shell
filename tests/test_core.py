import unittest
from app.core import Target, Scope, evaluate, inventory, parse_version

class CoreTests(unittest.TestCase):
    def test_affected_example(self):
        self.assertTrue(all(x['status'] == 'below_reference_fix' for x in evaluate('8.3.34')))
    def test_fixed_example(self):
        self.assertTrue(all(x['status'] == 'at_or_above_reference_fix' for x in evaluate('8.3.36')))
    def test_unknown_branch(self):
        self.assertTrue(all(x['status'] == 'review_vendor_support' for x in evaluate('8.1.1')))
    def test_invalid_version(self):
        with self.assertRaises(ValueError): parse_version('8.3.34;cmd')
    def test_owned_requires_evidence(self):
        with self.assertRaises(ValueError): Target('demo.example', Scope.OWNED)
    def test_public_has_no_source_access(self):
        self.assertFalse(inventory([Target('demo.example', Scope.PUBLIC)])[0]['source_access_allowed'])
    def test_unverified_owned_source_declaration_cannot_grant_source_access(self):
        target = Target('demo.example', Scope.OWNED, evidence='user-supplied-reference')
        result = inventory([target])[0]
        self.assertEqual(result['scope'], Scope.OWNED.value)
        self.assertFalse(result['source_access_allowed'])
        self.assertFalse(result['authorization_verified'])
        self.assertTrue(result['mandate_reference_supplied'])

    def test_mixed_inventory_does_not_elevate_owned_declarations(self):
        targets = [Target('public.example', Scope.PUBLIC),
                   Target('owned.example', Scope.OWNED, evidence='unverified')]
        rows = inventory(targets)
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(row['source_access_allowed'] is False for row in rows))
        self.assertTrue(all(row['authorization_verified'] is False for row in rows))

    def test_invalid_hostname(self):
        with self.assertRaises(ValueError): Target('localhost/path', Scope.PUBLIC)

if __name__ == '__main__':
    unittest.main()
