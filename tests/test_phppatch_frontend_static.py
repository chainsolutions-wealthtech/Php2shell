"""Fail-closed, offline-only PHPPATCH static preview contract."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "web/phppatch/index.html"


class PhppatchStaticPreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.markup = PAGE.read_text(encoding="utf-8")

    def test_separate_console_is_explicitly_unconnected(self):
        self.assertIn("<h1>PHPPATCH</h1>", self.markup)
        self.assertIn("Aucun dossier importé", self.markup)
        self.assertIn("NON CONNECTÉ", self.markup)
        self.assertIn("non vérifiés", self.markup)
        self.assertIn("non attestés", self.markup)

    def test_all_actions_are_disabled(self):
        from html.parser import HTMLParser
        class Buttons(HTMLParser):
            def __init__(self):
                super().__init__()
                self.buttons = []
            def handle_starttag(self, tag, attrs):
                if tag == "button":
                    self.buttons.append(dict(attrs))
        parsed = Buttons()
        parsed.feed(self.markup)
        self.assertEqual(len(parsed.buttons), 4)
        for button in parsed.buttons:
            self.assertIn("disabled", button)
            self.assertEqual(button.get("aria-disabled"), "true")
            self.assertEqual(button.get("type"), "button")

    def test_no_network_or_active_markup(self):
        for forbidden in ("<script", "<form", "<iframe", "<object", "<embed",
                          "<input", "<a ", "fetch(", "XMLHttpRequest",
                          "WebSocket(", "navigator.sendBeacon"):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, self.markup)
        self.assertIn("connect-src 'none'", self.markup)
        self.assertIn("script-src 'none'", self.markup)
        self.assertIn("form-action 'none'", self.markup)

    def test_patch_gates_cannot_be_mistaken_for_execution(self):
        for required in ("Diff candidat", "non généré", "Docker isolés",
                         "non exécutés", "Revue indépendante", "non demandée",
                         "rollback", "non prouvés", "preuves insuffisantes"):
            with self.subTest(required=required):
                self.assertIn(required, self.markup)

    def test_no_production_or_approval_claim(self):
        self.assertNotIn("APPROVED", self.markup)
        self.assertNotIn("DEPLOYED", self.markup)
        self.assertIn("Elle n'est pas publiée sur S1", self.markup)


if __name__ == "__main__":
    unittest.main()
