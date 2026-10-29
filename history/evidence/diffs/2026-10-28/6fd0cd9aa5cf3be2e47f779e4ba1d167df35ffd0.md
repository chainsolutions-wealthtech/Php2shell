# Commit exact 6fd0cd9aa5cf3be2e47f779e4ba1d167df35ffd0

Date UTC 2026-10-28T04:49:34Z; source https://github.com/chainsolutions-wealthtech/Php2shell/commit/6fd0cd9aa5cf3be2e47f779e4ba1d167df35ffd0

Parents: 440cdc91920ed3e1ed60639e040f082202d48984, ac0b35588c950d675fe89c70fbc8d434c0594d20

Fichiers 4; +300/-0

## app/cli.py (modified, +8/-0)

Blob ae08826b0cf7f0c3d2e3e4b97fc431c6388f2f8e; https://github.com/chainsolutions-wealthtech/Php2shell/blob/6fd0cd9aa5cf3be2e47f779e4ba1d167df35ffd0/app%2Fcli.py

```diff
@@ -12,6 +12,7 @@
 from .runtime_reporting import export_runtime_review_csv
 from .audit_dossier import build_audit_dossier, render_audit_dossier_markdown
 from .url_intake import preview_url_scope
+from .patch_preview import propose_local_ini_patch
 from .campaign_plan import plan_offline_campaign
 from .report_html import render_dossier_html
 
@@ -70,6 +71,11 @@ def main():
     campaign.add_argument('--shards', type=int, default=4)
     campaign.add_argument('--pages-per-target', type=int, default=20)
     campaign.add_argument('--requests-per-minute', type=int, default=6)
+    patch_proposal = sub.add_parser('propose-config-patch',
+                                    help='Offline php.ini display_errors diff; NEVER applied')
+    patch_proposal.add_argument('--path', required=True, help='Authorized local PHP project directory')
+    patch_proposal.add_argument('--as-of', required=True, help='UTC calendar date YYYY-MM-DD')
+    patch_proposal.add_argument('--evidence-id', required=True, help='One local dossier P2S-EV indicator')
     args = parser.parse_args()
     if args.command == 'check-version':
         result = evaluate(args.php)
@@ -98,6 +104,8 @@ def main():
             pages_per_target=args.pages_per_target,
             requests_per_minute=args.requests_per_minute,
         )
+    elif args.command == 'propose-config-patch':
+        result = propose_local_ini_patch(args.path, args.as_of, args.evidence_id)
     elif args.command == 'scan-local':
         result = scan_project(args.path)
     else:
```

## app/patch_preview.py (added, +124/-0)

Blob e3f2490a6a01280911284f7cba08b0cbf09abf57; https://github.com/chainsolutions-wealthtech/Php2shell/blob/6fd0cd9aa5cf3be2e47f779e4ba1d167df35ffd0/app%2Fpatch_preview.py

```diff
@@ -0,0 +1,124 @@
+"""Offline PHPPATCH *proposal* for one simple local PHP configuration indicator.
+
+Does not change files, run PHP, inspect servers, create branches, or approve a
+patch. Its diff is a human-review artifact, not a trusted deployment manifest.
+Only a strict, context-free setting line is included to avoid leaking secrets.
+"""
+from hashlib import sha256
+from pathlib import Path
+import re
+
+from .audit_dossier import build_audit_dossier
+from .dossier_handoff import _verify_dossier
+
+_MAX_SOURCE_BYTES = 65_536
+_DISPLAY_ON = re.compile(
+    r"^[ \t]{0,12}display_errors[ \t]{0,12}=[ \t]{0,12}"
+    r"(?:on|1|yes|true)[ \t]{0,12}$", re.I
+)
+_ALLOWED_NAMES = {"php.ini", ".user.ini"}
+
+
+def propose_local_ini_patch(project_path, as_of_utc, evidence_id):
+    """Produce a zero-context unified diff for an observed local ini setting.
+
+    An evidence ID alone is not a mandate; no actual source edit is executed.
+    The caller must separately authenticate the project, approve and test any
+    eventual patch within governed PHPPATCH before integration or release.
+    """
+    if not isinstance(evidence_id, str) or not re.fullmatch(
+        r"P2S-EV-[0-9a-f]{16}", evidence_id
+    ):
+        raise ValueError("Invalid dossier evidence identifier")
+    root = Path(project_path)
+    if root.is_symlink() or not root.is_dir():
+        raise ValueError("Project root must be a local regular directory")
+    root = root.resolve(strict=True)
+    dossier = build_audit_dossier(root, as_of_utc)
+    _verify_dossier(dossier)
+    rows = [
+        item for item in dossier["observations"]
+        if item["evidence_id"] == evidence_id
+    ]
+    if len(rows) != 1:
+        raise ValueError("Evidence ID not found or ambiguous in current audit")
+    row = rows[0]
+    if (row["category"] != "php_config"
+            or row["rule"] != "PHP-CONFIG-DISPLAY-ERRORS"
+            or row["asset_vulnerability_confirmed"] is not False
+            or row["patch_status"] != "NOT_GENERATED"):
+        raise ValueError("No supported, unapproved ini config indicator")
+    rel = row["source_relative_path"]
+    relpath = Path(rel)
+    if (relpath.is_absolute() or ".." in relpath.parts
+            or relpath.name.lower() not in _ALLOWED_NAMES):
+        raise ValueError("Unsupported or unsafe ini path")
+    cursor = root
+    for component in relpath.parts:
+        cursor = cursor / component
+        if cursor.is_symlink():
+            raise ValueError("Symlinked source path is not allowed")
+    path = root / relpath
+    if not path.is_file() or path.stat().st_size > _MAX_SOURCE_BYTES:
+        raise ValueError("Source ini file is unavailable or too large")
+    try:
+        data = path.read_bytes()
+        if b"\x00" in data:
+            raise ValueError("Binary content is not a PHP ini proposal")
+        text = data.decode("utf-8")
+    except (OSError, UnicodeError) as exc:
+        raise ValueError("Source ini file is not safe UTF-8") from exc
+    # Restrict to plain LF or CRLF; refuse mixed endings, Unicode controls
+    # or any content that might need a context-rich and leaky diff.
+    if "\r" in text.replace("\r\n", ""):
+        raise ValueError("Unexpected line endings in ini")
+    lines = text.splitlines(keepends=True)
+    number = row["source_line"]
+    if number > len(lines):
+        raise ValueError("Evidence line is no longer present")
+    original = lines[number - 1]
+    body = original.rstrip("\r\n")
+    if (len(body) > 100 or not body.isascii()
+            or not _DISPLAY_ON.fullmatch(body)):
+        raise ValueError("Ambiguous ini directive; manual review required")
+    new_line = "display_errors=Off"
+    # Do not put surrounding file lines into the diff: nearby settings may
+    # contain session tokens or environment-specific credentials.
+    diff = (
+        f"--- a/{rel}\n"
+        f"+++ b/{rel}\n"
+        f"@@ -{number} +{number} @@\n"
+        f"-{body}\n"
+        f"+{new_line}\n"
+    )
+    return {
+        "schema_version": "0.3-preview",
+        "proposal_type": "LOCAL_PHP_INI_UNAPPLIED_REVIEW_DIFF",
+        "source_evidence_id": evidence_id,
+        "source_dossier_fingerprint_sha256": dossier["report_fingerprint_sha256"],
+        "relative_file": rel,
+        "unified_diff": diff,
+        "diff_sha256": sha256(diff.encode("utf-8")).hexdigest(),
+        "changes_proposed": 1,
+        "files_modified": 0,
+        "patch_applied": False,
+        "mandate_verified": False,
+        "effective_php_configuration_verified": False,
+        "tests_run_on_candidate": False,
+        "independent_approval_received": False,
+        "ready_for_production": False,
+        "next_gates": [
+            "Authenticate source ownership and P2 mandate.",
+            "Confirm effective PHP HTTP SAPI and config precedence.",
+            "Review behavior and compatibility of the proposed setting.",
+            "Apply only in an isolated authorized sandbox and run regression tests.",
+            "Obtain independent approval and a verified rollback before deployment.",
+        ],
+        "limitations": (
+            "Single offline display_errors suggestion only. File bytes were "
+            "read locally but not changed; fingerprint is not authenticated. "
+            "A local ini file may not be the effective runtime configuration. "
+            "The diff does not fix the prioritized PHP CVEs, confirm a "
+            "vulnerability, authorize deployment or constitute a security patch."
+        ),
+    }
```

## docs/V0_3_LOCAL_PATCH_PREVIEW.md (added, +38/-0)

Blob c51ce37473d875c67bee5688a3e8260c71d76d82; https://github.com/chainsolutions-wealthtech/Php2shell/blob/6fd0cd9aa5cf3be2e47f779e4ba1d167df35ffd0/docs%2FV0_3_LOCAL_PATCH_PREVIEW.md

```diff
@@ -0,0 +1,38 @@
+# V0.3 — Première proposition de diff PHPPATCH (hors ligne)
+
+**Statut : sous-tranche préparatoire de V0.3, développée sur la PR #2 existante. Elle ne constitue pas la livraison de V0.3.**
+
+Le moteur PHP2SHELL produit déjà un dossier d'audit JSON/Markdown/HTML et un handoff vers PHPPATCH sans permissions. La nouvelle capacité `app/patch_preview.py` ajoute une proposition de modification **strictement limitée** au réglage `display_errors` d'un fichier `php.ini` ou `.user.ini` sous le répertoire local explicitement choisi.
+
+## Parcours démontré
+
+1. Préparer le dossier PHP2SHELL avec `audit-dossier --path ... --as-of ...`.
+2. Repérer un identifiant `P2S-EV-...` dont la règle est `PHP-CONFIG-DISPLAY-ERRORS`.
+3. Produire le diff candidat, sans modifier le projet :
+
+```bash
+python -m app.cli propose-config-patch \
+  --path ./projet-local-autorise \
+  --as-of 2026-10-28 \
+  --evidence-id P2S-EV-xxxxxxxxxxxxxxxx
+```
+
+4. Relire le diff, vérifier la configuration PHP réellement active et les effets fonctionnels, puis exiger mandat P2 authentifié, sandbox, tests et revue avant toute application.
+
+La sortie JSON fournit le diff de contexte nul (une seule ligne remplacée), son empreinte, l'identifiant de constat et le fingerprint du dossier. **Aucun contexte adjacent n'est exporté**, car des paramètres ou secrets peuvent se trouver dans le même fichier. Les chemins restent relatifs au projet.
+
+## Restrictions
+
+- Recalcule le dossier local et les identifiants avant toute proposition ; les identifiants forgés ou devenus obsolètes sont refusés.
+- Refuse les chemins symboliques, le parcours hors du projet, les fichiers non attendus, les réglages ambigus, les données non UTF-8 et les fichiers volumineux.
+- Accepte uniquement une affectation simple de `display_errors` sans commentaires ou interpolation pour produire la suggestion `display_errors=Off`.
+- `files_modified=0`, `patch_applied=false`, `mandate_verified=false`, `tests_run_on_candidate=false`, `independent_approval_received=false`, `ready_for_production=false`.
+- Le réglage peut être surchargé par une autre configuration effective et sa modification peut perturber les environnements de développement ; il faut vérifier la SAPI active et la compatibilité.
+- **Cette proposition n'est pas un correctif des CVE PHP prioritaires**, n'authentifie aucun mandat et ne démontre pas une vulnérabilité du site.
+- Le diff est **un brouillon de revue**, pas un ordre d'écriture Git, un patch appliqué, une PR ni un déploiement.
+
+## Preuves et suite
+
+`tests/test_patch_preview.py` couvre diff minimal, non-écriture, absence réseau, absence de secrets, refus des autres règles, fichiers ambigus/symboliques, CRLF et commande CLI.
+
+**Reste à construire** : moteur générique de propositions de correctifs PHP/runtime/config, diagnostics confirmés, sandbox Docker isolée et non-root, tests d'intégration, score de risque et preuve de rollback, émission de PR sous mandat et approbation, restauration effective et l'interface PHPPATCH authentifiée.
```

## tests/test_patch_preview.py (added, +130/-0)

Blob 6397962980b43614322ad83164e9da8d3c6c2e5a; https://github.com/chainsolutions-wealthtech/Php2shell/blob/6fd0cd9aa5cf3be2e47f779e4ba1d167df35ffd0/tests%2Ftest_patch_preview.py

```diff
@@ -0,0 +1,130 @@
+"""Read-only local PHP configuration patch proposal regression tests."""
+import json
+import socket
+import subprocess
+import sys
+import tempfile
+import unittest
+from hashlib import sha256
+from pathlib import Path
+from unittest.mock import patch
+
+from app.audit_dossier import build_audit_dossier
+from app.patch_preview import propose_local_ini_patch
+
+
+class IniPatchPreviewTests(unittest.TestCase):
+    def setUp(self):
+        self.tmp = tempfile.TemporaryDirectory()
+        self.addCleanup(self.tmp.cleanup)
+        self.root = Path(self.tmp.name)
+        self.config = self.root / "php.ini"
+        self.config.write_text(
+            "display_errors = On\n"
+            "session.secret=DO_NOT_LEAK_SESSION_SECRET\n"
+            "expose_php=Off\n", encoding="utf-8"
+        )
+
+    def evidence(self, rule="PHP-CONFIG-DISPLAY-ERRORS"):
+        dossier = build_audit_dossier(self.root, "2026-10-28")
+        items = [x for x in dossier["observations"] if x["rule"] == rule]
+        self.assertEqual(len(items), 1)
+        return items[0]["evidence_id"]
+
+    def test_proposes_exact_minimal_diff_without_modifying_file(self):
+        evidence = self.evidence()
+        before = sha256(self.config.read_bytes()).hexdigest()
+        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
+            proposal = propose_local_ini_patch(self.root, "2026-10-28", evidence)
+        after = sha256(self.config.read_bytes()).hexdigest()
+        self.assertEqual(before, after)
+        self.assertEqual(proposal["relative_file"], "php.ini")
+        self.assertEqual(proposal["source_evidence_id"], evidence)
+        self.assertEqual(proposal["unified_diff"],
+                         "--- a/php.ini\n+++ b/php.ini\n@@ -1 +1 @@\n"
+                         "-display_errors = On\n+display_errors=Off\n")
+        self.assertEqual(proposal["files_modified"], 0)
+        for key in ("patch_applied", "mandate_verified",
+                    "effective_php_configuration_verified",
+                    "tests_run_on_candidate", "independent_approval_received",
+                    "ready_for_production"):
+            self.assertIs(proposal[key], False)
+        self.assertNotIn("DO_NOT_LEAK_SESSION_SECRET", json.dumps(proposal))
+        self.assertNotIn(str(self.root), json.dumps(proposal))
+        self.assertEqual(len(proposal["diff_sha256"]), 64)
+
+    def test_deterministic_and_rejects_bad_evidence_identifiers(self):
+        id = self.evidence()
+        self.assertEqual(
+            propose_local_ini_patch(self.root, "2026-10-28", id),
+            propose_local_ini_patch(self.root, "2026-10-28", id),
+        )
+        for bad in ("", "unknown", "P2S-EV-" + "0"*16, 7,
+                    "P2S-EV-" + "x"*16):
+            with self.subTest(bad=bad), self.assertRaises(ValueError):
+                propose_local_ini_patch(self.root, "2026-10-28", bad)
+
+    def test_diff_not_generated_for_unsupported_rule(self):
+        self.config.write_text("expose_php=On\n", encoding="utf-8")
+        identifier = self.evidence("PHP-CONFIG-EXPOSE-PHP")
+        with self.assertRaisesRegex(ValueError, "No supported"):
+            propose_local_ini_patch(self.root, "2026-10-28", identifier)
+
+    def test_ambiguous_commented_setting_refused(self):
+        self.config.write_text(
+            "display_errors = On ; SECRET_COMMENT\n", encoding="utf-8"
+        )
+        identifier = self.evidence()
+        with self.assertRaisesRegex(ValueError, "Ambiguous"):
+            propose_local_ini_patch(self.root, "2026-10-28", identifier)
+
+    def test_project_symlink_and_oversize_file_rejected(self):
+        identifier = self.evidence()
+        link = self.root.parent / (self.root.name + "-link")
+        try:
+            link.symlink_to(self.root, target_is_directory=True)
+        except (OSError, NotImplementedError):
+            pass
+        else:
+            self.addCleanup(link.unlink)
+            with self.assertRaises(ValueError):
+                propose_local_ini_patch(link, "2026-10-28", identifier)
+        self.config.write_text(
+            "display_errors=On\n" + "a" * 66_000, encoding="utf-8"
+        )
+        identifier = self.evidence()
+        with self.assertRaisesRegex(ValueError, "too large"):
+            propose_local_ini_patch(self.root, "2026-10-28", identifier)
+
+    def test_nested_ini_file_and_crlf_line_endings(self):
+        self.config.unlink()
+        p = self.root / "settings"
+        p.mkdir()
+        target = p / ".user.ini"
+        target.write_bytes(
+            b"expose_php=Off\r\ndisplay_errors=On\r\npassword=SECRET\r\n"
+        )
+        identifier = self.evidence()
+        result = propose_local_ini_patch(self.root, "2026-10-28", identifier)
+        self.assertEqual(result["relative_file"], "settings/.user.ini")
+        self.assertIn("@@ -2 +2 @@", result["unified_diff"])
+        self.assertNotIn("password", result["unified_diff"])
+
+    def test_cli_does_not_write_source_and_legacy_reports_remain(self):
+        identifier = self.evidence()
+        before = self.config.read_bytes()
+        proc = subprocess.run(
+            [sys.executable, "-m", "app.cli", "propose-config-patch",
+             "--path", str(self.root), "--as-of", "2026-10-28",
+             "--evidence-id", identifier],
+            capture_output=True, text=True, check=True,
+        )
+        result = json.loads(proc.stdout)
+        self.assertEqual(result["proposal_type"], "LOCAL_PHP_INI_UNAPPLIED_REVIEW_DIFF")
+        self.assertFalse(result["ready_for_production"])
+        self.assertEqual(before, self.config.read_bytes())
+        self.assertNotIn("DO_NOT_LEAK_SESSION_SECRET", proc.stdout)
+
+
+if __name__ == "__main__":
+    unittest.main()
```

Attention: inspection du diff Git, sans attestation de tests ou d'exploitation.