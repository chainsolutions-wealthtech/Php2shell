# Contrat normatif du registre maître

- Clé de jointure unique : `key = TYPE + ":" + id`.
- `type` : namespace fermé dans le snapshot. `id` conserve l'identifiant de l'autorité existante (SHA complet / entier Actions / P2S-* / nom de branche).
- `source` : URL GitHub du fait ou registre source, permettant un contrôle indépendant. `archive_path` est la présence d'une fiche, non un statut d'audit.
- `source_head_sha` : `bed7c218d71743c4175b6b95f43a788105f966a2`, instantané de lecture de la PR préalable à la création du maître.
- Les statuts WP proviennent de `continuity/WORK_PACKAGES.json` et **n'ont pas été promus**.
- `COMMIT` : ensemble des 363 SHA distincts du snapshot de 7 branches du 29/10, pas inventaire live.
- `RUN` : 1 040 runs du snapshot du 29/10 ; inclut succès ET échecs ; le statut enregistré ne prouve pas un examen individuel des logs.
- `CHECK_SUITE`, `WORKFLOW` : identifiants référencés par ces runs et non éléments vérifiés séparément.
- `COMMENT` : commentaires actuellement retournés pour issue #5 et PR #7 ; valeur `created_at_utc=null` lorsque l'API ne fournit pas l'horodatage.
- `EVENT`, `DECISION`, `CHECKPOINT`, `REQUIREMENT` : présence des documents archivés et correspondance de base avec les logs natifs ; liens sémantiques individuels non encore attestés.
- La matrice ultérieure doit marquer `OBSERVED_IN_SNAPSHOT`, `DECLARED_IN_PLANNING`, `REPORTED_IN_CANONICAL_LOG` ou `NOT_VERIFIED` ; ne jamais inférer qu'une PR ou un commit implémente un WP par coïncidence de date.
- Reprises futures : ajouter un snapshot/manifest distinct si les HEAD évoluent, conserver les références historiques plutôt qu'écraser les anciennes.
- Aucun lien avec des dossiers de diff ne démontre la correction ou la non-régression du code applicatif.
