# PROTOCOL — mémoire canonique, checkpoints et reprise sans régression

**Identifiant stable du programme :** `PHP2SHELL-CONT-20261027-ROOT-01`.  
**Ancre durable et unique de routage :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5.  
**Autorité des faits techniques :** code, commits, PR, CI, outils MCP/S1 et preuves datées. **Autorité des choix utilisateur :** décisions explicites consignées dans `DECISIONS_LOG.md`.  
**Une seule gouvernance PHP2SHELL** dans ce dépôt. Ne pas importer les autorités runtime de MCP ou GRT en tant que gouvernance parallèle ; utiliser leurs interfaces autorisées.

## 1. Frontières de la mémoire

Les conversations ChatGPT ne sont **pas** une base de données canonique de projet. Une nouvelle conversation peut ne pas retrouver toutes les formulations antérieures. **Ce protocole ne transcrit pas automatiquement les messages**. Il exige l'enregistrement *explicite* des objectifs, décisions significatives, opérations, preuves et points de reprise dans des sources GitHub visibles à tout agent autorisé.

Le dépôt est **public** : ne jamais publier mots de passe, clés, jetons, secrets, identifiants privés, extraits de code client, pièces sensibles ni transcriptions privées. Les preuves sensibles doivent rester dans des autorités sécurisées séparées avec seulement des références non sensibles dans les checkpoints publics.

## Traçabilité du périmètre fondateur et prévention des oublis

Le **contrat produit** comprend `FOUNDING_SPECIFICATION.md` (les six lots historiques et toutes les capacités), `REQUIREMENTS_TRACEABILITY.md` (REQ-001 à REQ-022 avec critères de sortie) et `CVE_SOURCE_REGISTER.md` (sources de sécurité datées). Les agents doivent consulter ces fichiers avec le plan des cinq versions avant de décider d'une suppression, fusion ou requalification de scope.

Une fonctionnalité est dite **programmée** si un besoin est écrit, **développée** si du code existe, **validée** si tests/CI au HEAD + revue réussis, **déployée** si constat runtime/HTTPS E2E existe. L'absence de champ prouvé interdit la promotion de statut.

## Garantie de conservation du parcours URL

Avant toute décision de concevoir ou mettre en ligne un scanner, lire `URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md` et **REQ-023→REQ-032** dans la matrice. Ne jamais qualifier un résultat de « vulnérabilité PHP confirmée » sur la seule base d'un crawl de pages publiques : accès aux sources/runtime P2 et preuves de backport requis pour l'applicabilité. Refuser tout crawl hors scope, toute tentative d'exploit RCE de tiers, et toute proposition de correction appliquée sans admission/approbation. Le frontend PHPPATCH reste un service distinct avec moteur partagé, sans gateway parallèle.

## Workflow multi-axes sans seconde autorité

Les fichiers [`INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md`](INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md) et [`WORK_PACKAGES.json`](WORK_PACKAGES.json) constituent un **backlog de planification** et un modèle d'orchestration, pas une nouvelle Task Queue ni un second agent autonome actif. Chaque nouveau work package doit associer `REQ-xxx`, dépendances, ressource, mandat, gate, preuves et checkpoint. La complétude d'un DAG documentaire ne garantit ni la disponibilité d'exécuteurs, ni l'autorisation, ni la création d'une automatisation récurrente. Réutiliser les identités stables, claims, locks et événements gouvernés réellement disponibles dans MCP, après confirmation de leur interface, ou rester bloqué et l'attester. Les lectures peuvent être concurrentes ; les écritures sur une même ressource ne le sont pas.

## 2. Cycle obligatoire pour chaque nouvelle conversation / session

**REPRISE LECTURE SEULE d'abord :**
1. Lire l'issue #5 (description puis **dernier checkpoint/commentaire**), ensuite `00_START_HERE.md`, `CURRENT_STATE.md`, `NEXT_ACTION.md`, `DECISIONS_LOG.md`, `EVENT_LOG.md` sur **la branche qui les contient**. Si fusionnés, utiliser `main` ; si non fusionnés, suivre la PR de continuité, pas deviner des chemins.
2. Interroger GitHub en direct pour refs/HEAD/main/branches/PR/issues/workflows/reviews/claims/tâches et comparer aux snapshots. Conserver la chaîne PR #1 → PR #2 → PR #3 et les issues #4/#5.
3. Si une action concerne S1/MCP, appeler `ping`, `mcp_reconcile_governed_context`, `mcp_get_current_state_inventory` et les seules sondes autorisées ; distinguer snapshot, sondage frais et configuration réellement active. Ne pas purger des caches DNS sans outil gouverné dédié.
4. Détecter duplication : réutiliser la branche, PR, issue, tâche et identité autorisées existantes ; **pas de nouvelle tâche concurrente**.
5. Classer chaque affirmation : **CONFIRMED_DIRECT**, **CONFIRMED_GITHUB**, **RECORDED_SNAPSHOT**, **USER_DECISION**, **PROPOSED**, **BLOCKED**.

**EXÉCUTION :**
6. N'intervenir qu'en branche/PR revue et avec permissions propres au dépôt/serveur. Appliquer l'ajout minimal et exécuter tests/CI; pas d'écriture directe dans `main`, pas de seconde gateway, pas de détournement des outils de projet S1.
7. Journaliser toute décision significative `DECISIONS_LOG`, tout événement matériel `EVENT_LOG`, le snapshot `CURRENT_STATE` et une `NEXT_ACTION` unique dans une PR légitime (ou la PR documentaire de continuité si aucun autre support adapté).
8. Publier un **commentaire checkpoint dans l'issue #5 après chaque jalon significatif** : rôle/intervenant, mandat, exact HEAD, PR, CI, action réellement exécutée, preuves, résultat/limites, décision, handoff et NEXT_ACTION.
9. Si un write GitHub est indisponible, **ne pas prétendre que l'information est enregistrée** ; livrer le checkpoint à publier et indiquer le blocage d'accès. Si l'utilisateur veut de la persistance automatique hors conversation, une automatisation/connexion dédiée doit être créée et autorisée séparément.

**REPRISE / HANDOFF :**
10. Terminer avec les liens directs vers issue/PR/commit/CI et le prochain geste ; ne pas demander à l'utilisateur de répéter les informations déjà écrites.
11. Si la prochaine conversation observe un HEAD différent, **réconcilier le conflit** avant toute écriture ; ne pas forcer un rebase ni réécrire l'histoire.
12. Pour abandon/rollback, documenter l'approbation, les artefacts concernés, la restauration et la preuve, sans suppression de checkpoints.

## 3. Format obligatoire du checkpoint (commentaire de l'issue #5)

```yaml
continuity_id: PHP2SHELL-CONT-20261027-ROOT-01
checkpoint_id: P2S-CP-YYYYMMDD-NNN
timestamp_utc: YYYY-MM-DDTHH:MM:SSZ
actor: ChatGPT / humain / agent autorisé (avec contexte du rôle)
intent_and_authorization: mandat explicite + périmètre
repository: chainsolutions-wealthtech/Php2shell
branch: branche existante exacte
head_before: SHA ou NOT_APPLICABLE
head_after: SHA ou NOT_CHANGED
pr: URL ou NONE
ci: run URLs et résultats exacts
server_target: S1 / none
actions_completed: [actions réellement attestées]
evidence: [URLs GitHub, logs sécurisés, sources et timestamp]
limitations_and_blockers: [manques et doutes]
decisions_recorded: [P2S-DEC-nnn ou NONE]
next_action: UNE action déterminée, avec condition de réussite
rollback: référence ou NOT_APPLICABLE
```

Les valeurs sont des exemples de champs, pas un registre informatique exécutable. Le **dernier checkpoint n'efface pas l'historique**.

## 4. Ordre des autorités

**En cas de conflit :** (1) état GitHub/S1 direct vérifié et mandats en cours ; (2) décisions utilisateur explicites les plus récentes compatibles avec les protections ; (3) journal canonique vérifié ; (4) checkpoint daté ; (5) résumé de conversation ; (6) supposition, jamais utilisée comme preuve.

Les informations historiques restent utiles mais ne doivent **jamais** être présentées comme actuelles sans nouvelles sondes.

## 5. Conditions de non-régression

- Ne supprimer ni règles, ni tests, ni protections, ni décisions acquises ; enregistrer les éventuelles exceptions explicitement approuvées.
- Chaque changement doit identifier impact, tests, sécurité, plan de rollback et preuve CI au SHA exact.
- Toute analyse de projet PHP nécessite un mandat explicite ; aucun scan actif de tiers non autorisés.
- Les avis non vérifiés ne sont pas des CVE confirmées ; les propositions de patch ne sont jamais appliquées automatiquement à une production.
- Aucun Codex/Copilot requis ou utilisé ; outils GitHub/MCP existants uniquement selon portée.
- Les sous-domaines S1 et conteneurs Docker restent des éléments d'un moteur partagé, pas des gouvernances indépendantes.
