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
