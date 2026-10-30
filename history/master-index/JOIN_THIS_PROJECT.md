# REJOINDRE CE PROJET DEPUIS N'IMPORTE QUELLE CONVERSATION

**IDENTIFIANT CANONIQUE RACINE UNIQUE :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Mandat :** Programme Directeur Intégral PHP2SHELL–PHPPATCH ; **pas** le chantier universel MCP ni GRT.  
**Autorité durable :** [issue #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5).  
**Registre de routage :** [CANONICAL_CONTINUITY_MANIFEST.json](CANONICAL_CONTINUITY_MANIFEST.json).  
**Archive et traces :** [PR #7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7), branche `docs/integral-chronological-history-20261029`.

## Comment rejoindre
1. À partir du seul ID `PHP2SHELL-CONT-20261027-ROOT-01`, ouvrir l'issue #5, lire ses commentaires les plus récents puis `00_START_HERE.md` et `continuity/HANDOFF.md` depuis une branche existante **non supposée être main**.
2. Lire [le registre maître des identifiants](MASTER_IDENTIFIERS_REGISTRY.json) : clé `TYPE:ID` et fichier `details/TYPE.json`. Il indexe au dernier snapshot 2 738 clés dans 16 catégories, pas tous les faits du futur.
3. Lire [le registre maître des relations](MASTER_RELATIONSHIPS_REGISTRY.json) : 5 582 liens structurés historisés + [213 références textuelles non probatoires](matrices/MATRIX_DOCUMENTED_CROSS_REFERENCES.json).
4. Lire les matrices [activités/tâches/actions](matrices/MATRIX_ACTIVITIES_TASKS_ACTIONS.json), [décisions/continuité](matrices/MATRIX_CONTINUITY.json), [corrélations](matrices/MATRIX_CORRELATIONS.json), [chronologie](matrices/MATRIX_WORK_CHRONOLOGY.json), [relations non vérifiées](matrices/MATRIX_UNVERIFIED_RELATIONS.json) et les sources natives `continuity/`.
5. **Réconcilier à l'instant de la reprise** les branches et HEAD des PR #1/#2/#3/#6/#7, les commentaires de l'issue #5, statuts de revue, CI exact-SHA, les 61 work packages et les claims/locks effectifs dans leur périmètre. Les nombres de commits/runs de 2026-10-29 ne constituent pas le live.
6. Utiliser [NO_COLLISION_REJOIN_PROTOCOL.md](NO_COLLISION_REJOIN_PROTOCOL.md). Les travaux en lecture seule peuvent être parallèles ; les écritures sur un même fichier, branche, WP, instance S1 ou ressource exigent admission/coordination réelle. Ne **jamais** considérer cet index comme un verrou.
7. Exécuter seulement la tranche mandatée et admissible, vérifier le résultat, produire une trace append-only dans la même PR légitime et un checkpoint ancré à l'issue #5. Mentionner tous les éléments `NOT_VERIFIED` ; ne pas passer un WP à DONE sans critères et preuves.
8. Remettre à la prochaine conversation le même `PHP2SHELL-CONT-20261027-ROOT-01`, les liens des nouvelles preuves, la dernière ref vérifiée, les ressources encore occupées et le `P2S-NEXT-001` métier tant qu'il n'a pas été remplacé par une décision canonique étayée.

## Règles de priorité et anti-collision
- **Une seule continuité racine**, sans ID de remplacement ni seconde source d'autorité.
- **Une seule priorité métier active** à un instant donné selon la source actualisée. `P2S-NEXT-001` n'est pas réputée terminée par une action documentaire sur la PR #7.
- **PR #7 = archive documentaire** ; PR #6 = continuité ; PR #1 = V0.1 ; PR #2 = V0.2 ; PR #3 = préparation S1. Leurs scopes, bases et HEAD doivent être vérifiés avant chaque opération.
- **Aucune régression** : pas d'écriture directe `main`, pas de force push, pas de réécriture des faits historiques ni de fusion non mandatée.
- **Pas de Codex/Copilot**, pas de second orchestrateur, pas de nouvelle automatisation implicite.
- **Autorisations séparées** : PHP2SHELL, développement du MCP, accès aux ressources S1/Plesk/GitHub.
- **Pas de secrets dans le dépôt public.** Si un accès, une preuve ou un claim manque, écrire `NOT_VERIFIED` ou `BLOCKED`.

## Prompt de reprise autonome

> Rejoins le programme PHP2SHELL–PHPPATCH par le Continuity ID racine `PHP2SHELL-CONT-20261027-ROOT-01`. Commence par l'issue #5 et par `history/master-index/CANONICAL_CONTINUITY_MANIFEST.json` sur la branche actuelle de la PR #7 ; lis le point d'entrée `JOIN_THIS_PROJECT.md`, les registres maîtres d'identifiants et de relations, les matrices de continuité, corrélations et chronologie, puis `continuity/HANDOFF.md`, `PROTOCOL.md` et `NEXT_ACTION.md`. Réconcilie les HEAD/CI/permissions/claims/locks et les checkpoints les plus récents avant toute action. Ne crée pas de continuité ni de PR concurrente. Conserve la priorité métier et les 61 work packages, ajoute sans régression sur les ressources autorisées, contrôle les résultats et publie un checkpoint sourcé dans l'issue #5 avec lien vers la PR et un handoff. Aucune supposition de déploiement, scan ou patch. N'utilise pas Codex/Copilot.

## Limites honnêtes
Une URL issue #5 + ces fichiers rend la reprise **reconstructible**, mais ne donne pas à ChatGPT une mémoire verbatim automatique, ni une réservation de ressource, ni une permission runtime. Les mises à jour des registres devront être explicites. Les 2 738 objets et 5 582 relations sont ceux des snapshots documentés.
