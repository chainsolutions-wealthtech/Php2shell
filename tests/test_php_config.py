"""Safety and interpretation tests for read-only PHP configuration indicators."""
import json
import tempfile
import unittest
from pathlib import Path

from app.php_config import inspect_php_configs
from app.static_analysis import scan_project


class PhpConfigurationTests(unittest.TestCase):
    def test_ini_indicators_only_from_unambiguous_boolean_values(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "php.ini").write_text(
                "; expose_php = On (commented)\n"
                "# display_errors = On (commented)\n"
                "expose_php=On\n"
                "display_errors = 1 ; local development setting\n"
                "allow_url_include = off\n"
                "session.cookie_httponly = Off\n"
                "session.cookie_secure = yes\n"
                "session.use_strict_mode = 0\n"
                "custom_password = TOP_SECRET_DO_NOT_EXPOSE\n"
                "display_errors = UNKNOWN_DYNAMIC_SETTING\n",
                encoding="utf-8",
            )
            result = inspect_php_configs(root)
            self.assertEqual(result["config_files_examined"], 1)
            self.assertEqual(
                [(x["line"], x["rule"]) for x in result["config_indicators"]],
                [
                    (3, "PHP-CONFIG-EXPOSE-PHP"),
                    (4, "PHP-CONFIG-DISPLAY-ERRORS"),
                    (6, "PHP-CONFIG-COOKIE-HTTPONLY"),
                    (8, "PHP-CONFIG-SESSION-STRICT"),
                ],
            )
            self.assertNotIn("TOP_SECRET_DO_NOT_EXPOSE", json.dumps(result))
            self.assertNotIn("UNKNOWN_DYNAMIC_SETTING", json.dumps(result))
            self.assertTrue(all(
                not x["effective_runtime_confirmed"]
                for x in result["config_indicators"]
            ))

    def test_php_fpm_pool_directives_and_user_ini(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            pool = root / "php-fpm.d"
            pool.mkdir()
            (pool / "www.conf").write_text(
                "php_admin_value[display_errors] = On\n"
                "php_value[session.cookie_httponly] = 0\n"
                "php_admin_value[allow_url_include] = 1\n"
                "user = www-data\n",
                encoding="utf-8",
            )
            (root / ".user.ini").write_text("session.cookie_secure=off\n")
            result = inspect_php_configs(root)
            self.assertEqual(result["config_files_examined"], 2)
            self.assertEqual(
                {x["rule"] for x in result["config_indicators"]},
                {
                    "PHP-CONFIG-DISPLAY-ERRORS", "PHP-CONFIG-COOKIE-HTTPONLY",
                    "PHP-CONFIG-COOKIE-SECURE", "PHP-CONFIG-URL-INCLUDE",
                },
            )
            self.assertTrue(all("path" in x and "line" in x for x in result["config_indicators"]))

    def test_restrict_candidates_and_excluded_vendor(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            vendor = root / "vendor"
            vendor.mkdir()
            (vendor / "php.ini").write_text("display_errors=On")
            (root / "unrelated.conf").write_text("display_errors=On")
            (root / "www.conf").write_text("display_errors=On")
            (root / "php.ini").write_text("display_errors=Off")
            result = inspect_php_configs(root)
            self.assertEqual(result["config_files_examined"], 1)
            self.assertEqual(result["config_indicators"], [])

    def test_config_symlinks_never_followed(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            real = root / "secret.ini"
            real.write_text("display_errors=On\nprivate_access_token=sensitive")
            link = root / "php.ini"
            try:
                link.symlink_to(real)
            except (OSError, NotImplementedError):
                self.skipTest("Symlinks unavailable")
            result = inspect_php_configs(root)
            self.assertEqual(result["config_files_examined"], 0)
            self.assertEqual(result["config_indicators"], [])
            self.assertIn(
                {"path": "php.ini", "reason": "unsafe_config_path"},
                result["config_skipped"],
            )

    def test_malformed_encoding_and_oversized_configs_are_skipped(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "php.ini").write_bytes(b"\xff\xfe")
            (root / ".user.ini").write_bytes(b" " * 1_000_001)
            result = inspect_php_configs(root)
            self.assertEqual(
                {x["reason"] for x in result["config_skipped"]},
                {"config_unreadable", "config_too_large"},
            )
            self.assertEqual(result["config_indicators"], [])

    def test_scan_local_retains_old_keys_and_embeds_php_config(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "index.php").write_text("<?php echo 'hello';")
            (root / "php.ini").write_text(
                "display_errors=On\npassword = DO_NOT_LEAK\n")
            result = scan_project(root)
            self.assertEqual(result["schema_version"], "0.2")
            self.assertIn("composer_requirements", result)
            self.assertIn("locked_dependencies", result)
            self.assertEqual(result["scanned_php_files"], 1)
            self.assertEqual(result["php_configuration"]["config_indicators"][0]["rule"],
                             "PHP-CONFIG-DISPLAY-ERRORS")
            self.assertNotIn("DO_NOT_LEAK", json.dumps(result))
            self.assertIn("not effective PHP runtime", result["limitations"])

    def test_file_limit_is_fail_closed(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for index in range(101):
                directory = root / f"dir{index}"
                directory.mkdir()
                (directory / "php.ini").write_text("expose_php=Off\n")
            with self.assertRaisesRegex(ValueError, "config file limit"):
                inspect_php_configs(root)

    def test_input_must_be_directory(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            path = root / "php.ini"
            path.write_text("display_errors=On")
            with self.assertRaises(ValueError):
                inspect_php_configs(path)


if __name__ == "__main__":
    unittest.main()
