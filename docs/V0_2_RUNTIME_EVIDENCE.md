# V0.2 — Contrat de preuve de runtime PHP (déclaration hors ligne)

**Statut : prototype de validation d'entrée et de comparaison PHP/CVE. Ce module n'est PAS une attestation cryptographique ni une admission d'autorisation P2. Il ne lance aucun programme et ne contacte aucun serveur.**

## Pourquoi cette capacité est nécessaire

La version PHP affichée par une page ou déclarée par une personne ne prouve pas le moteur réellement utilisé par le serveur HTTP. Une conclusion PHP2SHELL doit, à terme, relier : actif autorisé, mandat P2 authentifié, SAPI effectivement active, paquets réellement chargés, configuration, branches et correctifs rétroportés, horodatage, signature ou contrôle de provenance et références PHP/fournisseur.

La présente tranche prépare **uniquement l'enveloppe locale** et refuse de convertir une simple déclaration en preuve vérifiée.

## Usage

Créer un fichier local `runtime.json` pour une **fixture fictive ou un actif administré** :

```json
{
  "schema_version": "0.2",
  "evidence_type": "DECLARED_PHP_RUNTIME",
  "asset_hostname": "portail-demo.example",
  "mandate_reference": "LAB-P2-001",
  "source_channel": "laboratory_fixture",
  "collected_at_utc": "2026-10-28T00:00:00Z",
  "php_version": "8.3.34",
  "sapi": "fpm-fcgi",
  "vendor_backport_status": "not_verified"
}
```

```bash
python -m app.cli review-runtime-evidence --file ./runtime.json --as-of 2026-10-28
```

Le fichier doit rester local, être régulier (aucun symlink), ne pas dépasser 16 384 octets, contenir exactement les champs attendus et respecter les formats version/date/SAPI. Les captures brutes de `phpinfo()`, identifiants et secrets ne sont pas nécessaires et ne doivent pas être ajoutés à ce schéma.

La sortie comporte :
- identifiant d'actif normalisé, référence de mandat **déclarée mais non vérifiée**, version/SAPI fournies ;
- âge et état de fraîcheur de la déclaration (seuil local 30 jours, **pas une preuve d'actualité du runtime**) ;
- empreinte SHA-256 de l'entrée canonique (**pas une signature d'autorité**) ;
- comparaison aux seuils correctifs upstream des deux CVE de l'instantané officiel ;
- **`mandate_authorization_verified=false`**, **`signature_verified=false`**, **`effective_http_runtime_attested=false`** et **`asset_applicability=insufficient_evidence`** même si la version déclarée est inférieure au seuil connu.

**Aucune analyse distante, récupération de code PHP serveur, validation de mandat, déploiement ou patch n'est effectuée.**

## Critères pour une véritable preuve P2 future

1. Reprendre les mandats et claims du MCP existant, sans créer un système parallèle.
2. Authentifier l'identité de l'agent et l'autorisation de l'actif/source en amont.
3. Produire des informations minimisées et signées à partir de la SAPI réellement utilisée par le vhost ou le pool PHP autorisé, avec validation des signatures et de la fraîcheur.
4. Croiser les packages système/builds, extensions, provenance fournisseur et backports documentés ; **ne pas inférer une CVE confirmée sur la seule comparaison semver**.
5. Connecter les preuves vérifiées au diagnostic, aux rapports puis aux propositions de PHPPATCH sous approbation. Prévoir rollback et tests.

## Non-régression

Les commandes existantes `check-version`, `review-version`, `advisories`, `audit-catalog`, `propose-catalog-update`, `fetch-official-advisory`, `scan-local` et `import-targets` restent présentes. Les tests `tests/test_runtime_evidence.py` couvrent version P2 fictive, source déclarée, champ falsifié, extension de privilèges refusée, date future, fichier symbolique, JSON invalide, fraîcheur et absence de réseau. La CI doit réussir au HEAD exact avant tout checkpoint `VERIFIED_DONE`.

Cette tranche complète **REQ-006** mais ne la termine pas : les permissions et l'attestation **effective** sont encore à construire.
