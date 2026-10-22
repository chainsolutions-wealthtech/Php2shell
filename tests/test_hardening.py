import json
import tempfile
import unittest
from pathlib import Path

from app.core import Scope, Target, evaluate, load_targets, parse_version

class HardeningTests(unittest.TestCase):
    def test_invalid_version_suffix(self):
        for value in ('8.3.34-ubuntu', '8.3', '8.3.34.1', '', ' 8.3.34'):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_version(value)

    def test_hostname_normalization(self):
        self.assertEqual(Target('DEMO.EXAMPLE', Scope.PUBLIC).hostname, 'demo.example')

    def test_hostname_rejects_url(self):
        for value in ('https://demo.example', 'demo.example:443', 'a..b', '-bad.example'):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    Target(value, Scope.PUBLIC)

    def test_inventory_malformed_json(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'targets.json'
            path.write_text('{bad', encoding='utf-8')
            with self.assertRaises(json.JSONDecodeError):
                load_targets(path)

    def test_inventory_must_be_list(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'targets.json'
            path.write_text('{}', encoding='utf-8')
            with self.assertRaises(ValueError):
                load_targets(path)

    def test_scope_rejects_unknown(self):
        with self.assertRaises(ValueError):
            Scope('unauthorized')

    def test_reference_fix_not_proof(self):
        result = evaluate('8.3.34')
        self.assertTrue(all('verify vendor backports' in x['note'] for x in result))

if __name__ == '__main__':
    unittest.main()
