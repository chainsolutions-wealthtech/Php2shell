"""Static PHP2SHELL frontend preview is intentionally non-executing."""
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class FrontendPreviewTests(unittest.TestCase):
    def test_url_form_is_not_a_scan_or_network_client(self):
        markup = (ROOT / "web/php2shell/index.html").read_text(encoding="utf-8")
        js = (ROOT / "web/shared/url-preview.js").read_text(encoding="utf-8")
        self.assertIn('id="url"', markup)
        self.assertIn('id="scope"', markup)
        self.assertIn('id="preview"', markup)
        self.assertIn('type="button" id="preview"', markup)
        self.assertIn('Démarrer un audit — indisponible', markup)
        self.assertIn("disabled", markup)
        self.assertIn("connect-src 'none'", markup)
        self.assertIn("script-src 'self'", markup)
        self.assertIn("aucun", markup.lower())
        self.assertIn('addEventListener("click"', js)
        self.assertIn(".textContent", js)
        self.assertNotIn(".innerHTML", js)
        for term in ("fetch(", "XMLHttpRequest", "navigator.sendBeacon",
                     "WebSocket(", "location.assign("):
            with self.subTest(term=term):
                self.assertNotIn(term, js)

    def test_no_untrusted_external_asset_dependency(self):
        markup = (ROOT / "web/php2shell/index.html").read_text(encoding="utf-8")
        self.assertIn('src="../shared/url-preview.js"', markup)
        self.assertNotIn("https://cdn.", markup)
        self.assertNotIn("<form action=", markup)
        self.assertNotIn('type="submit"', markup)


    def test_beginner_entry_is_plain_language(self):
        html = (ROOT / "web/php2shell/index.html").read_text(encoding="utf-8")
        self.assertIn("En trois étapes, sans jargon", html)
        self.assertIn("1. Indiquez votre site", html)
        self.assertIn("2. Choisissez votre analyse", html)
        self.assertIn("3. Consultez votre résultat", html)
        self.assertIn("Vérifier les informations publiques", html)
        self.assertIn("Analyser le code de mon site", html)
        self.assertIn('value="public_metadata"', html)
        self.assertIn('value="owned_source"', html)
        self.assertIn("Paramètres avancés", html)
        self.assertIn("<details", html)
        self.assertIn("Sans inscription pour la prévisualisation", html)

    def test_real_scan_and_login_are_never_faked_in_demo(self):
        html = (ROOT / "web/php2shell/index.html").read_text(encoding="utf-8")
        js = (ROOT / "web/shared/url-preview.js").read_text(encoding="utf-8")
        self.assertIn("aucun site n'est contacté", html.lower())
        self.assertIn("Connexion et vérification des droits : non disponibles", html)
        self.assertIn("Démarrer un audit — indisponible", html)
        self.assertIn("disabled", html)
        self.assertIn("connect-src 'none'", html)
        self.assertIn("vérification de vos droits", html)
        self.assertNotIn("fetch(", js)
        self.assertNotIn("XMLHttpRequest", js)



if __name__ == "__main__":
    unittest.main()
