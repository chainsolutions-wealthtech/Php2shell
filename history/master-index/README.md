# Registre maître transversal des identifiants — PHP2SHELL–PHPPATCH

**Autorité :** issue [#5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5) ; **PR d'archive :** [#7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7) ; **continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`.

## Entrée unique
- **[MASTER_IDENTIFIERS_REGISTRY.json](MASTER_IDENTIFIERS_REGISTRY.json)** : inventaire déterministe des objets par clé `TYPE:ID`, sans collision inter-catégories.
- **[MASTER_IDENTIFIERS_COUNTS.json](MASTER_IDENTIFIERS_COUNTS.json)** : comptage par famille et frontière des instantanés.
- **[SOURCE_CONTRACT.md](SOURCE_CONTRACT.md)** : schéma, niveaux de preuves, statut de chaque source.
- Les matrices de corrélation, de liens, de dépendances, de continuité, d'activités et de chronologie sont ajoutées dans un **deuxième commit** exclusivement dérivé de ce registre.

## Couverture initiale et limites
- `BRANCH` : 7
- `CHECKPOINT` : 44
- `CHECK_SUITE` : 1040
- `COMMENT` : 56
- `COMMIT` : 363
- `CONTINUITY` : 1
- `DECISION` : 24
- `EVENT` : 56
- `ISSUE` : 2
- `MEMORY` : 1
- `PR` : 5
- `PROGRAM` : 1
- `REQUIREMENT` : 32
- `RUN` : 1040
- `WORKFLOW` : 5
- `WORK_PACKAGE` : 61

Les sources `history/evidence/git/commit-inventory-all-branches.json` et `history/evidence/actions/workflow-runs-snapshot.json` sont **datées du 29 octobre** : les commits/runs ajoutés après leur cutoff ne sont pas ici déclarés inventoriés. Les commentaires de l'issue #5 et PR #7 ont été relus durant la préparation. Les `CHECK_SUITE` sont des références associées aux runs, non une confirmation de jobs/logs audités.

Les objets issus de fichiers de la PR #7 documentent la présence de fiches, sans affirmer la validation de leurs contenus. Les tâches `PLANNED_NOT_ADMITTED` restent telles quelles. Le registre n'opère aucun claim, merge, scan ou déploiement.
