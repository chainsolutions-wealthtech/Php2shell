# Réconciliation de la frontière du snapshot Git — 30 octobre 2026

**Continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`.  
**PR exclusive :** [#7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7).  
**Source ancienne :** [`commit-inventory-all-branches.json`](git/commit-inventory-all-branches.json), snapshot daté du 29 octobre 2026, 363 SHA uniques, 688 appartenances commit/branche.  
**Source fraîche :** interrogation de `search_branches` jusqu'à `cursor=null`, puis comparaison `compare_commits(base=<SHA du snapshot>, head=<nom de branche>)` pour chaque branche.  
**HEAD de la PR #7 immédiatement avant la rédaction de ce constat :** `f0e4958453b2ec68c0a32aa912c96feece1fec0c`.

## Constat exhaustif des noms de branches actuellement accessibles

La recherche GitHub a retourné les sept noms ci-dessous, puis une page suivante vide avec `cursor=null`. L'exhaustivité ici concerne **les noms de branches retournés à cet instant**, et non les branches supprimées ou les commits orphelins.

| Branche | SHA de référence du snapshot | Relation GitHub snapshot→branche observée | Commits devant | Commits derrière | Fichiers agrégés dans la comparaison |
|---|---|---|---:|---:|---:|
| `audit/s1-php-dns-20261027` | `02a4f1d6592a8d5ada59a1959bb8f4e0c591c4c2` | `identical` | 0 | 0 | 0 |
| `docs/canonical-continuity-20261027` | `69e15bebd588de08f9658769d812cb6c639c1739` | `ahead` | 16 | 0 | 8 |
| `docs/hardening-v0-1-20261022` | `c17f0931db2cae659e4301585b0bf3db9078ca09` | `identical` | 0 | 0 | 0 |
| `docs/integral-chronological-history-20261029` | `26f98c08a05ab865087da1ebdf02df87d49230c3` | `ahead` | 121 | 0 | 300 |
| `feat/v0-2-offline-php-static-analysis-20261027` | `9517abd090c5e7cffed62e4c77c1826f0282310f` | `ahead` | 5 | 0 | 5 |
| `main` | `a9d799b008fc65ed5745745bc4ef09e8b889aabe` | `identical` | 0 | 0 | 0 |
| `ops/s1-readiness-php-services-20261027` | `5ae7245e9aa4857aca3835546a9a46ebea969d1f` | `ahead` | 10 | 0 | 6 |

## Interprétation strictement bornée

1. **Le snapshot des 363 SHA est désormais historiquement figé et incomplet pour les branches actuelles.** Quatre branches ont avancé depuis leur SHA de référence. Les nouvelles preuves archivées doivent porter leur propre date et leur propre base de comparaison, sans réécrire le snapshot.
2. **Les valeurs `ahead_by` ne sont pas additionnables pour calculer des SHA uniques.** Les branches sont empilées, peuvent partager des commits et la PR #7 hérite de la branche documentaire #6. La somme arithmétique `16+121+5+10=152` est uniquement un total de **comptages de différences par branche**, pas un nombre de nouveaux SHA distincts.
3. **Les 121 commits devant le snapshot sur la PR #7 incluent les écritures de l'archive elle-même** (notamment les deux dossiers de preuve ajoutés pendant la présente intervention). Ils ne constituent pas 121 commits de construction applicative.
4. Les `ahead_by` observés sont des résultats à un instant de lecture, **pas des locks ni des HEAD futurs garantis**. Une autre écriture d'agent peut modifier ces valeurs.
5. L'absence de `behind_by` à cet instant indique une relation d'ascendance sur les branches comparées. Elle ne certifie ni l'absence de collision ultérieure, ni la validité des claims, ni l'intégralité des conversations ou des logs serveur.
6. La comparaison GitHub renvoie des statistiques de fichiers agrégées. Elle **ne livre pas la liste complète des nouveaux SHA dans cette réponse** : l'identification et l'audit individuels de tous les commits post-snapshot restent `NOT_VERIFIED` jusqu'à récupération d'un inventaire paginé actualisé.
7. La branche `main` est `identical` à son SHA de référence historique dans cette observation ; cela ne signifie pas que les PR applicatives ou documentaires ont été fusionnées.

## Conséquence sur la reconstruction intégrale

La couverture documentaire `363 fiches de commits + 363 dossiers de diff` est **exacte pour son périmètre historique**, mais ne couvre pas automatiquement les commits intervenus après le cutoff. Les dossiers de contrôle [patchs tranche 001](2026-10-30-patch-content-verification-001.md) et [patchs tranche 002](2026-10-30-patch-content-verification-002.md) ne doivent pas être confondus avec un audit de ces nouveaux SHA.

La prochaine réconciliation doit obtenir les listes paginées de commits de chacune des sept branches à un HEAD figé, dédupliquer par SHA, construire les fiches/diffs **manquants uniquement** dans PR #7, puis vérifier individuellement leur contenu, leurs CI, leurs liens aux décisions et aux checkpoints. Aucune suppression, force push, écriture `main`, action S1/Plesk ni nouvelle PR ne découle de ce constat.

**État : `IN_PROGRESS` ; l'archive n'est pas intégralement auditée.**
