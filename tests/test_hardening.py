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
        invalid = (
            'https://demo.example', 'demo.example:443', 'a..b',
            '-bad.example', 'ok.-bad.example', 'ok.bad-.example',
            'bad-.example', 'a' * 64 + '.example', 'ok.' + 'a' * 64,
            'example.', '.example', 'name_with_underscore.example',
            'hello/example', 'a' * 63 + '.' + 'b' * 63 + '.' +
            'c' * 63 + '.' + 'd' * 62,
        )
        for value in invalid:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    Target(value, Scope.PUBLIC)

    def test_dns_label_length_boundaries(self):
        long_valid = '.'.join(['a' * 63, 'b' * 63, 'c' * 63, 'd' * 61])
        self.assertEqual(len(long_valid), 253)
        self.assertEqual(Target(long_valid, Scope.PUBLIC).hostname, long_valid)
        self.assertEqual(Target('a-b.example', Scope.PUBLIC).hostname, 'a-b.example')
        self.assertEqual(Target('LOCALHOST', Scope.PUBLIC).hostname, 'localhost')

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
        self.assertTrue(result, 'evaluate() must return at least one cautionary note')
        self.assertTrue(all('verify vendor backports' in x['note'] for x in result))

if __name__ == '__main__':
    unittest.main()
