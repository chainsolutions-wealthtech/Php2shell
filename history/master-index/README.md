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


## Navigation des matrices transversales

- [Répertoire des 2 738 identifiants](MASTER_IDENTIFIERS_REGISTRY.json) et détails [par catégorie](details/)
- [Registre maître des relations sourcées](MASTER_RELATIONSHIPS_REGISTRY.json) — 5 582 liens observés/rapportés ou déclarés, avec séparation des preuves
- [Matrice des dépendances et exigences](matrices/DEPENDENCIES.json)
- [Matrice des liens Git et historique des branches](matrices/GIT_LINEAGE.json)
- [Matrice des corrélations CI↔commits](matrices/CI_CORRELATION/RUN_TARGETS_SHA.json) et index des autres liens CI dans le registre des relations
- [Corrélations multidimensionnelles par exigence et commit](matrices/MATRIX_CORRELATIONS.json)
- [Matrice de continuité événements↔décisions↔checkpoints↔commentaires](matrices/MATRIX_CONTINUITY.json)
- [Matrice d'activités, tâches et actions](matrices/MATRIX_ACTIVITIES_TASKS_ACTIONS.json) : 61 WP et contrats, non confondus avec réalisation
- [Chronologie d'activités complète du snapshot](matrices/MATRIX_WORK_CHRONOLOGY.json) : commits, runs, décisions, événements, checkpoints, commentaires
- [Index chronologique par jour](matrices/MATRIX_CHRONOLOGY_DAY_INDEX.json)
- [Relations encore non vérifiées](matrices/MATRIX_UNVERIFIED_RELATIONS.json)

### Mode de recherche d'un identifiant
1. Rechercher `TYPE:ID` dans `MASTER_IDENTIFIERS_REGISTRY.json`.
2. Ouvrir `details/TYPE.json`, y retrouver la clé et la source primaire.
3. Lire `MASTER_RELATIONSHIPS_REGISTRY.json` et la matrice correspondant à sa famille.
4. Lire `MATRIX_WORK_CHRONOLOGY.json` et la matrice d'activités si l'objet représente une décision, tâche, action ou exécution.
5. Si une relation manque, la classer `NOT_VERIFIED` ; ne jamais affirmer une opération déployée à partir du simple journal.

Les matrices reflètent les instantanés documentés, et non un état runtime actuel garanti. Les liens planifiés n'attestent ni achèvement ni admission. Aucun nouveau moteur, claim, ou workflow récurrent n'a été créé.


### Compléments de provenance (sans promotion de statut)

- [Matrice des mentions explicites entre événements, décisions, commentaires, WP et REQ](matrices/MATRIX_DOCUMENTED_CROSS_REFERENCES.json) : liens textuels **non assimilés à des réalisations** ; distincts des 5 582 relations structurées.
- [Justificatifs des dates documentaires retrouvées](matrices/MATRIX_DATE_PROVENANCE.json) : ajout de dates au jour près depuis les logs et fiches historiques ; horaires non inventés.
- Les tableaux [chronologiques](matrices/MATRIX_WORK_CHRONOLOGY.json) et [par jour](matrices/MATRIX_CHRONOLOGY_DAY_INDEX.json) intègrent les dates recoupées et conservent les commentaires non datés comme `UNKNOWN`.


<!-- PHP2SHELL-MASTER-ROOT-ROUTING-V1 -->
## Raccordement canonique de toutes les mémoires, matrices et conversations (30 octobre 2026)

**Une seule continuité racine :** `PHP2SHELL-CONT-20261027-ROOT-01` ; [issue canonique #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5). **Pas de nouvel ID de continuité.**

- [Routage canonique JSON](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CANONICAL_CONTINUITY_MANIFEST.json) (registre unique des autorités, alias, registres et frontières de preuve).
- [Rejoindre le projet depuis une nouvelle conversation](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/JOIN_THIS_PROJECT.md) : lecture, réconciliation, prochaine action, traces de reprise.
- [Protocole anti-collision](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/NO_COLLISION_REJOIN_PROTOCOL.md) et [contrat JSON](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/REJOIN_PROTOCOL.json) : préflight HEAD, claims réels, gate, admission, écriture sans force, contrôle exact-SHA et checkpoint.
- [Arbre des relations de routage](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CONTINUITY_ROUTING_GRAPH.json) et [journal append-only](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CONTINUITY_ACTIVITY_LEDGER.jsonl).
- Les deux registres `MASTER_IDENTIFIERS_REGISTRY.json` et `MASTER_RELATIONSHIPS_REGISTRY.json` partagent la même racine et pointent vers ce manifeste ; les instantanés et 61 WP ne sont pas des autorisations runtime.

**Priorité métier préservée :** `P2S-NEXT-001` tant qu'un changement attesté n'apparaît pas dans l'issue #5 et les registres actualisés. Les nouvelles conversations doivent d'abord recontrôler les HEAD et le dernier checkpoint.


## Dernier point de reprise documentaire indexé (30 octobre 2026)

- [Checkpoint canonique `P2S-CP-20261030-045`](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5#issuecomment-6512668570) sur l'issue #5.
- [Pointeur de reprise](CURRENT_HANDOFF_POINTER.json) : dernier HEAD **observé**, priorité métier et chemins de réconciliation.
- [Delta d'identifiants postérieurs au snapshot historique](POST_SNAPSHOT_REFERENCE_DELTA.json) : nouvelles références sourcées **sans modifier les 2 738 objets de l'ancien instantané**.
- [Journal append-only](CONTINUITY_ACTIVITY_LEDGER.jsonl) : précontrôle, commit réellement publié et checkpoint. Ces enregistrements sont des traces, pas des locks ni des tâches exécutées automatiquement.

**Reprise :** toujours réinterroger GitHub avant de considérer le pointeur comme actuel. Tout nouvel identifiant vérifié peut être ajouté par un delta suivant, sans détruire les snapshots antérieurs.
