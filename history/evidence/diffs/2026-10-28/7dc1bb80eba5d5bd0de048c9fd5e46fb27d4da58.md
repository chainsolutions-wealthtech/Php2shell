# Commit exact 7dc1bb80eba5d5bd0de048c9fd5e46fb27d4da58

Date UTC 2026-10-28T00:37:23Z; source https://github.com/chainsolutions-wealthtech/Php2shell/commit/7dc1bb80eba5d5bd0de048c9fd5e46fb27d4da58

Parents: 4c289b926d62b85e302a37cc30f705225dc05c68

Fichiers 1; +1/-1

## continuity/REQUIREMENTS_TRACEABILITY.md (modified, +1/-1)

Blob 09952b1aa5af6d26615e3c474870376308059954; https://github.com/chainsolutions-wealthtech/Php2shell/blob/7dc1bb80eba5d5bd0de048c9fd5e46fb27d4da58/continuity%2FREQUIREMENTS_TRACEABILITY.md

```diff
@@ -15,7 +15,7 @@ Ce registre traduit **le programme initial (six lots) + son évolution (cinq ver
 | **REQ-002** centaines/milliers cibles | Inventaire/campagnes / L2 | V0.2/V1.0 | Non implémenté | Campagne testée à volume élevé avec budgets, limites, retries, reprise et preuves, sans requête non autorisée |
 | **REQ-003** double niveau d'autorisation | Exigence fondatrice / L1-L2 | Toutes | **Partiel** : `public_metadata` vs `owned_source` déclaratifs, pas de vérification de mandat | Autorité, date/fin/portée et permissions admises ; refus hors périmètre et tests négatifs |
 | **REQ-004** identification PHP passive et framework | Passive Audit / L2 | V0.2 | Non implémenté | Indices publics non intrusifs avec sources et confiance, redirections validées, taux bornés, absence de faux diagnostic |
-| **REQ-005** catalogue officiel CVE sourcé | CVE Intelligence / L3 | V0.2 | **Références publiques vérifiées documentalement**, ingestion/validation de catalogue NON implémentées | Provenance datée + avis upstream/fournisseur, branche, score, backport, tests de divergence |
+| **REQ-005** catalogue officiel CVE sourcé | CVE Intelligence / L3 | V0.2 | **Partiel** : avis PHP/CERT-FR prioritaires stockés dans un instantané local JSON sourcé, daté et validé par tests (PR #2) ; collecte automatisée, fraîcheur temps réel, distributions/backports NON implémentés | Provenance datée + avis upstream/fournisseur, branche, score, backport, tests de divergence |
 | **REQ-006** version runtime réelle / SAPI | CVE/runtime / L3 | V0.2/V0.3 | Comparaison semver démo seulement, non attestation de serveur | Collecte sous mandat de PHP réellement exécuté, paquets, config, SAPI, extension et état patched |
 | **REQ-007** analyse fichiers PHP / AST | Source Review / L4 | V0.2 | **Partiel** : scanner lexical local PR #2 | AST, faux positifs négatifs mesurés, chemin/ligne/preuve, limites documentées |
 | **REQ-008** Composer et configs | Source Review / L4 | V0.2 | **Partiel** : `composer.json`/`composer.lock`, `php.ini`/`.user.ini` et certaines configurations PHP-FPM lus **hors ligne** sur PR #2 ; pas de runtime/SAPI effectif ni de configuration webserver complète | Lockfile, dépendances installées, php.ini/FPM/webserver analysés depuis sources autorisées |
```

Attention: inspection du diff Git, sans attestation de tests ou d'exploitation.