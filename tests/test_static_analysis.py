import json
import tempfile
import unittest
from pathlib import Path
from app.static_analysis import scan_project

class StaticAnalysisTests(unittest.TestCase):
    def test_detects_indicators_and_composer(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "index.php").write_text("<?php\neval($input);\nsystem($cmd);\n", encoding="utf-8")
            (root / "composer.json").write_text(json.dumps({"require": {"php": "^8.3", "vendor/pkg": "^1.0"}}))
            result = scan_project(root)
            self.assertEqual(result["scanned_php_files"], 1)
            self.assertEqual({f["rule"] for f in result["findings"]}, {"PHP-DYNAMIC-EVAL", "PHP-SHELL-EXEC"})
            self.assertEqual(result["composer_requirements"]["require"]["php"], "^8.3")

    def test_ignores_vendor_and_symlinks(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            vendor = root / "vendor"
            vendor.mkdir()
            (vendor / "test.php").write_text("<?php eval($x);")
            (root / "safe.php").write_text("<?php echo 'safe';")
            (root / "linked.php").symlink_to(vendor / "test.php")
            result = scan_project(root)
            self.assertEqual(result["scanned_php_files"], 1)
            self.assertEqual(result["findings"], [])

    def test_nested_vendor_directory_is_pruned(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            nested = root / "src" / "vendor"
            nested.mkdir(parents=True)
            (nested / "bad.php").write_text("<?php eval($x);")
            (root / "src" / "ok.php").write_text("<?php echo 1;")
            result = scan_project(root)
            self.assertEqual(result["scanned_php_files"], 1)
            self.assertEqual(result["findings"], [])

    def test_ignores_strings_comments_html_and_heredocs(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            code = (
                '<p>eval($web)</p>\n'
                '<?php\n'
                '// eval($comment);\n'
                '/* system($comment); */\n'
                '$a = "shell_exec($quoted)";\n'
                '$b = \'unserialize($quoted)\';\n'
                "$c = <<<'DATA'\\n"
                'eval($heredoc);\n'
                'DATA;\n'
                'eval($real);\n'
                '?>\n'
                '<div>system($html)</div>\n'
                '<?php unserialize($data);\n'
            )
            (root / "mixed.php").write_text(code, encoding="utf-8")
            result = scan_project(root)
            self.assertEqual([(f["line"], f["rule"]) for f in result["findings"]],
                             [(10, "PHP-DYNAMIC-EVAL"), (13, "PHP-UNSERIALIZE")])
            self.assertEqual(result["schema_version"], "0.2")

    def test_php_line_comment_terminates_on_closing_tag(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "mixed.php").write_text(
                "<?php // echo 1; ?> eval($html) <?php system($real);", encoding="utf-8"
            )
            findings = scan_project(root)["findings"]
            self.assertEqual([f["rule"] for f in findings], ["PHP-SHELL-EXEC"])

    def test_unterminated_php_string_does_not_leak_indicators(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "unterminated.php").write_text(
                '<?php $a = "not closed \\n eval($x);', encoding="utf-8"
            )
            self.assertEqual(scan_project(root)["findings"], [])

    def test_invalid_manifest_is_not_fatal(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "composer.json").write_text("{broken")
            self.assertEqual(scan_project(root)["skipped"][0]["reason"], "invalid_manifest")

    def test_requires_directory(self):
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / "file.php"
            file.write_text("<?php")
            with self.assertRaises(ValueError):
                scan_project(file)

if __name__ == "__main__":
    unittest.main()
