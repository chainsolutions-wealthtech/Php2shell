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

## Validation automatisée fondée sur des preuves — P2S-DEC-024 (29/10/2026)

**Continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`. Ce protocole précise la décision utilisateur [P2S-DEC-024](DECISIONS_LOG.md), sans créer de nouvelle autorité.

1. **Admission** : identifier WP/REQ/version/lot, dépendances, ressource, mandat et claim/lock effectifs ; refuser toute collision, scope non autorisé ou contrôle manquant. Un WP `PLANNED` n'est pas une permission d'écriture.
2. **Preuves techniques** : capturer HEAD avant, modifications bornées sur PR existante, tests de non-régression, analyse de sécurité proportionnée, CI au HEAD après, résultats et limitations. Une CI verte ne prouve ni indépendance de la revue ni sécurité absolue.
3. **Contre-revue** : consigner les constats techniques, leur correction ou blocage et l'identité réelle du contrôleur. Une revue par le même agent ou deux comptes du même propriétaire est `SELF_REVIEW`, jamais `INDEPENDENT_APPROVED`.
4. **Décision de fusion** : vérifier les règles de protection et revues requises en vigueur. Si elles imposent un approbateur indépendant absent, garder `BLOCKED_REVIEW` ; une évolution explicite de politique doit être gouvernée et vérifiée séparément, sans bypass. Ne pas modifier `main` directement.
5. **Frontières** : scans P1/P2, exploitation de tiers, patchs appliqués, permissions MCP et déploiement S1 exigent leurs mandats distincts. Aucune approbation de production ne découle d'une CI verte.
6. **Traçabilité** : après un jalon matériel, ajouter un événement distinct `P2S-EVT-xxx`, actualiser `CURRENT_STATE` et `NEXT_ACTION`, publier un checkpoint non redondant dans l'issue #5 avec SHA/CI/preuves/rollback ; préserver `P2S-EVT-048` et l'unique `P2S-NEXT-001` jusqu'à décision attestée.

**États distincts :** `PLANNED`, `ADMITTED`, `IMPLEMENTED`, `TESTED`, `CI_GREEN`, `SELF_REVIEWED`, `INDEPENDENT_APPROVED`, `BLOCKED_REVIEW`, `MERGED`, `DEPLOYED`, `VERIFIED_DONE`. Ne jamais promouvoir un WP au seul motif d'une documentation ou d'un test partiel.

## Séparation des claims MCP / PHP2SHELL–PHPPATCH — P2S-EVT-051 (29/10/2026)

**continuity_id: `PHP2SHELL-CONT-20261027-ROOT-01`.** Les claims ne sont jamais interchangeables entre autorités.

- **Claim de développement MCP** : travail sur `Patricked-code/MCP` (code, API, bridge, orchestration). Il ne donne ni ownership d'un WP PHP2SHELL, ni autorisation de modifier son dépôt.
- **Claim de travail PHP2SHELL–PHPPATCH** : ownership borné d'un des 61 WP, sur des fichiers/branches/PR du dépôt `chainsolutions-wealthtech/Php2shell`, selon la gouvernance propre au projet. Il ne donne aucun droit sur le code MCP ni sur S1.
- **Claim d'exploitation d'une ressource partagée** : mandat distinct du propriétaire de la ressource (MCP, S1/Plesk, GitHub, production) lorsque le WP doit y agir. Il ne remplace pas le claim de projet.
- **Opération traversant les frontières** : exiger cumulativement l'admission du WP PHP2SHELL, l'absence de collision dans le projet, et l'autorisation/claim de la ressource externe concernée ; vérifier leur identité, durée, scope et révocation. Aucun héritage implicite.
- **Sélecteur `select_candidates.py`** : son résultat `READ_ONLY_CANDIDATE` est une proposition sans claim ni assignation ; aucune promotion `ADMITTED` ou `RUNNING` sans contrôle séparé des autorités concernées.
- **Traçabilité** : chaque checkpoint distingue `project_work_package`, `project_claim` (ou `NOT_ATTESTED`), `external_resource_claim` (ou `NOT_REQUIRED`/`NOT_ATTESTED`), `actor`, `scope`, `head_sha`, `tests`, `ci`, `result`. Ne pas appeler un claim MCP générique « claim PHP2SHELL ».

Cette règle est additive ; aucune nouvelle file d'orchestration ou autorité concurrente n'est créée.
