# Archives historiques intégrales — PHP2SHELL–PHPPATCH

**Continuité racine immuable :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source canonique :** [issue #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5)
**Nature :** corpus historique cumulatif, non substitutif, sans suppression des journaux originaux.
**Périmètre :** événements antérieurs à la création de la continuité (22–26 octobre 2026) et ensemble des événements, checkpoints, décisions, actions et preuves depuis le 27 octobre.

## Arborescence documentaire

```text
history/
├── README.md                         ← index, règles et navigation
├── TREE.md                           ← arbre des relations historiques
├── 00-SOURCES-AND-METHOD.md          ← sources, authenticité, lacunes, statuts
├── chronology/
│   ├── 2026-10-22-to-2026-10-26.md  ← origine avant ancrage
│   ├── 2026-10-27.md                ← création de la continuité
│   ├── 2026-10-28.md                ← construction et validations
│   └── 2026-10-29.md                ← dernières évolutions
├── events/                          ← fiches détaillées P2S-EVT-001..052, à compléter
├── checkpoints/                     ← fiches #001..#040 et addenda, à compléter
├── decisions/                       ← décisions P2S-DEC et supersessions, à compléter
├── pull-requests/                   ← historiques PR #1, #2, #3, #6, à compléter
├── work-packages/                   ← 61 WP et dépendances, à compléter
├── requirements/                    ← REQ-001..032, à compléter
├── infrastructure/                  ← S1, domaines, déploiement et permissions
└── evidence/                        ← index SHA, CI, GitHub et écarts
```

Les sous-dossiers annoncés sont des **destinations documentaires**, pas des preuves de fiches déjà écrites. Une section n'est déclarée complète que si ses sources et son contenu détaillé ont été vérifiés.

## Autorités documentaires existantes — conservées intégralement

- [EVENT_LOG](../continuity/EVENT_LOG.md) : `P2S-EVT-001` à `P2S-EVT-052` ; ne pas remplacer les entrées par une narration.
- [DECISIONS_LOG](../continuity/DECISIONS_LOG.md) : décisions structurantes, y compris `P2S-DEC-024`.
- [CURRENT_STATE](../continuity/CURRENT_STATE.md) : instantanés datés, **non** état live garanti.
- [NEXT_ACTION](../continuity/NEXT_ACTION.md) : `P2S-NEXT-001` reste prioritaire tant que non résolue.
- [PROTOCOL](../continuity/PROTOCOL.md) : gouvernance et distinction des trois scopes de claims.
- [WORK_PACKAGES](../continuity/WORK_PACKAGES.json) : 61 WP, DAG, gates, statuts.
- [REQUIREMENTS_TRACEABILITY](../continuity/REQUIREMENTS_TRACEABILITY.md) : 32 exigences.
- [INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW](../continuity/INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md) : architecture cible, ne pas confondre avec exécuteur effectif.

## Convention de chaque action

Chaque fiche détaillée doit contenir : `event_id`, date/heure UTC exacte ou fenêtre incertaine, acteur **attesté ou non attesté**, mandat et scope, état avant, opération réellement tentée, fichiers/ressources touchés, branche et SHA avant/après, PR, tests et run CI au SHA, résultat, incidents et corrections, permissions/claims **séparés**, rollback, décisions associées, dépendances WP/REQ, checkpoint et sources primaires.

Étiquettes de preuve obligatoires : `OBSERVED_IN_GITHUB`, `REPORTED_IN_CANONICAL_LOG`, `USER_MANDATE`, `NOT_VERIFIED`, `BLOCKED`. Aucune affirmation d'exécution sur la seule base d'une intention. Les horaires manquants restent `NOT_VERIFIED` et ne sont jamais inventés.

## Contraintes

- Branche documentaire dédiée ; aucune écriture sur `main`, aucun déploiement, aucune fusion implicite.
- Pas de duplication des IDs canoniques, ni suppression ni renumérotation des événements, décisions ou checkpoints.
- Distinguer travail sur PHP2SHELL, développement MCP et utilisation des ressources MCP/S1/Plesk/GitHub ; les claims sont non transférables.
- Aucun raccourci : l'arbre et l'index servent uniquement à **naviguer vers les preuves et descriptions intégrales**, jamais à remplacer ces descriptions.
- Reconstitution progressive et vérifiable : **ce premier commit crée la structure, pas encore l'intégralité des centaines de pages envisagées**.

## Première fiche probatoire rédigée

- [P2S-EVT-053 — vérification hors ligne de fraîcheur DNS, RED→GREEN, 251 tests et limites](events/P2S-EVT-053.md). Cette fiche a été ajoutée après le squelette initial de la PR #7. Les autres fiches restent à construire individuellement, sans les présenter comme achevées.

- [P2S-EVT-055 — déclaration P2 non vérifiée, horodatages de claims, RED→GREEN et CI exact-SHA](events/P2S-EVT-055.md). Deux tranches défensives sur PR #2 et PR #6 ; aucune admission P2 ni claim runtime.

- [P2S-EVT-054 — cycles de redirection et preuves DAG](events/P2S-EVT-054.md), [checkpoint #042](checkpoints/P2S-CP-20261029-042.md), [checkpoint #043](checkpoints/P2S-CP-20261029-043.md) : sources canoniques archivées sans raccourci.
- [P2S-EVT-056 — fusion gouvernée PR #2 vers PR #3 sans force](events/P2S-EVT-056.md) : comparaison des arbres Git, deux parents, CI exacte et limites S1.

- [P2S-CP-20261029-044 — checkpoint de fusion PR #2→#3](checkpoints/P2S-CP-20261029-044.md) : commentaire canonique #6510381410 reproduit intégralement, quatre workflows PR #3 et rollback documentés.

## Preuves individuelles complémentaires — 30 octobre 2026

Ces documents constituent des **preuves d'investigation ajoutées à l'archive**, pas un remplacement des fiches détaillées ni une déclaration de fin de reconstruction.

- [Contrôle des patchs — tranche 001](evidence/2026-10-30-patch-content-verification-001.md) : trois SHA, six patchs comparés à l'identique.
- [Contrôle des patchs — tranche 002](evidence/2026-10-30-patch-content-verification-002.md) : 28 SHA supplémentaires, 65 patchs textuels comparés à l'identique, deux entrées de fichiers sans patch GitHub à contrôler séparément. **Cumul : 31/363 SHA du snapshot ; 71/71 patchs exposés et comparés ; 332 dossiers restant à vérifier individuellement.**
- [Six jobs GitHub Actions et leurs journaux](evidence/actions/2026-10-30-job-log-verification-001.md) : fondation V0.1, redirections RED→GREEN, P2, convergence S1 et DNS/TLS/HTTPS historiques, avec limites de portée.
- [Frontière du snapshot et sept branches](evidence/2026-10-30-post-snapshot-branch-reconciliation.md) : quatre branches ont avancé depuis les SHA de référence ; les 363 SHA du snapshot ne couvrent pas automatiquement les commits postérieurs.

**État de l'objectif historique intégral : `IN_PROGRESS`.** Les preuves absentes et les limites de validité restent visibles ; aucune CI verte, fiche de commit ou réussite DNS/TLS n'atteste à elle seule une application déployée.

- [Vérification complémentaire des deux blobs sans patch](evidence/2026-10-30-empty-blob-verification-001.md) : `app/__init__.py` et `auth_tests/__init__.py` lus aux SHA historiques, contenu vide et blob SHA identique aux dossiers archivés ; les deux exceptions de la tranche 002 sont ainsi levées, sans changer son état historique initial.

- [Contrôle des patchs — tranche 003](evidence/2026-10-30-patch-content-verification-003.md) : 14 SHA supplémentaires et 26 patchs exacts. **Cumul à cette vérification : 45/363 dossiers individuellement contrôlés, 97/97 patchs exposés identiques, 2/2 blobs sans patch contrôlés ; 318 dossiers du snapshot encore à vérifier**, sans compter les commits postérieurs au snapshot.


## Memoire PHP2 — photographie historique reçue le 30 octobre 2026

- [Index de la photographie « Memoire PHP2 »](memoire-php2/2026-10-30/README.md) — source transmise par l'utilisateur, registre JSON complet, 52 événements / 24 décisions / 61 WP / 40 checkpoints tels qu'ils étaient **rapportés dans ce document**.
- Les enregistrements sont rangés sous `history/memoire-php2/2026-10-30/` pour conserver **une source datée, non substitutive**, sans écraser les fiches, les événements postérieurs, les 363 dossiers de diff ni les preuves CI actuelles.
- **Priorité probatoire :** GitHub exact SHA, CI exact run, preuves serveur, registres natifs et commentaires canoniques ; la mémoire utilisateur est une source secondaire de reconstitution, pas une admission ou preuve de déploiement.


## Point d'entrée transversal — registre maître des identifiants (30 octobre 2026)

- [Registre maître et index transversal](master-index/README.md) : objets typés, identifiants GitHub, SHA, exécutions CI, workflow/check suites et références canoniques ; les matrices relationnelles s'y rattachent.
- Les instantanés du 29 octobre et leurs limites sont conservés, sans remplacement des fiches de preuve déjà présentes.


<!-- PHP2SHELL-MASTER-ROOT-ROUTING-V1 -->
## Raccordement canonique de toutes les mémoires, matrices et conversations (30 octobre 2026)

**Une seule continuité racine :** `PHP2SHELL-CONT-20261027-ROOT-01` ; [issue canonique #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5). **Pas de nouvel ID de continuité.**

- [Routage canonique JSON](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CANONICAL_CONTINUITY_MANIFEST.json) (registre unique des autorités, alias, registres et frontières de preuve).
- [Rejoindre le projet depuis une nouvelle conversation](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/JOIN_THIS_PROJECT.md) : lecture, réconciliation, prochaine action, traces de reprise.
- [Protocole anti-collision](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/NO_COLLISION_REJOIN_PROTOCOL.md) et [contrat JSON](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/REJOIN_PROTOCOL.json) : préflight HEAD, claims réels, gate, admission, écriture sans force, contrôle exact-SHA et checkpoint.
- [Arbre des relations de routage](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CONTINUITY_ROUTING_GRAPH.json) et [journal append-only](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CONTINUITY_ACTIVITY_LEDGER.jsonl).
- Les deux registres `MASTER_IDENTIFIERS_REGISTRY.json` et `MASTER_RELATIONSHIPS_REGISTRY.json` partagent la même racine et pointent vers ce manifeste ; les instantanés et 61 WP ne sont pas des autorisations runtime.

**Priorité métier préservée :** `P2S-NEXT-001` tant qu'un changement attesté n'apparaît pas dans l'issue #5 et les registres actualisés. Les nouvelles conversations doivent d'abord recontrôler les HEAD et le dernier checkpoint.
