# V0.2 — Rapport CSV des déclarations PHP/SAPI (non attestées)

Ce lot complète **P2S-WF-E12** (reporting local) et **P2S-WF-Q01** (non-régression). Il ne réalise ni scan, ni connexion à un serveur, ni vérification de mandat P2.

Exemple sur un fichier de déclaration local autorisé :

```bash
python -m app.cli review-runtime-evidence --file runtime.json --as-of 2026-10-28 --format csv
```

Sans `--format`, la sortie JSON existante reste inchangée. La sortie CSV est déterministe et contient uniquement des champs explicitement autorisés : nom d'actif déclaré, version et SAPI déclarées, âge logique, comparaisons upstream CVE et indicateurs **tous non attestés**. Elle ne divulgue ni référence de mandat, ni hash du document, ni canal de collecte, ni configuration PHP brute.

Les champs `mandate_verified`, `runtime_attested` et `signature_verified` restent obligatoirement `False` ; `asset_applicability` reste `insufficient_evidence` et les backports `not_verified`. Le CSV protège les cellules commençant par une formule de tableur. Toute tentative de transformer une déclaration en preuve de vulnérabilité ou autorisation est rejetée.

**Limites :** ni attestation cryptographique, ni SAPI HTTP vérifiée, ni preuve de backport fournisseur, ni diagnostic d'exploitabilité, ni PDF, ni approbation de patch. Les avis et seuils de version ne prouvent pas qu'un actif est vulnérable. Le futur workflow URL → audit autorisé → diagnostic → PHPPATCH et les deux services Docker S1 demeurent à construire.
