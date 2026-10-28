# V0.2 — Audit hors ligne de provenance du catalogue d'avis PHP

La commande additive `audit-catalog` calcule une empreinte SHA-256 du **JSON
canonique validé** et l'âge de la dernière revue du catalogue local. Elle ne
contacte aucun site Web, ne consulte aucun flux distant et ne sonde aucun actif.

```bash
python -m app.cli audit-catalog --as-of 2026-10-28
python -m app.cli audit-catalog --as-of 2026-11-28
python -m unittest discover -s tests -v
```

`--as-of` est une date calendaire UTC **explicitement fournie** au format
`YYYY-MM-DD`. Les dates invalides et antérieures à la date de revue sont
refusées. Le résultat JSON contient `snapshot_age_days`,
`catalog_reviewed_on_utc`, `canonical_json_sha256`,
`advisory_count` et `source_freshness: NOT_A_LIVE_FEED`.

L'empreinte permet de comparer deux instantanés valides et de détecter un
changement de contenu, indépendamment des espaces et de l'ordre des clés JSON.
**Elle ne constitue ni une signature de l'éditeur, ni une preuve cryptographique
de provenance upstream, ni une attestation d'authenticité.** Le catalogue
local doit toujours être vérifié contre les avis primaires avant usage de
remédiation, même si son âge est de zéro jour.

`independent_upstream_reverification_required` est toujours vrai et
`asset_applicability` reste `insufficient_evidence`. Un seuil de fraîcheur
arbitraire ne transforme jamais une version déclarée en diagnostic CVE.
Aucune politique de backport fournisseur, d'authentification runtime ou
d'approbation de patch n'est implémentée par ce module.

Les commandes existantes `check-version`, `advisories`, `review-version`,
`scan-local` et `import-targets` restent inchangées. Cette étape prépare
la provenance et la traçabilité V0.2, **sans** ingestion périodique des sources,
sans collecte distante et sans déploiement S1. Le workflow cible
URL → audit explicitement autorisé → diagnostic → PHPPATCH et les deux
interfaces Docker isolées restent des jalons ultérieurs.
