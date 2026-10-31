# INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW — orchestration continue gouvernée

**Continuity ID :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Ancre immuable :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5  
**Source de la file de travail :** [`WORK_PACKAGES.json`](WORK_PACKAGES.json), **61 unités de travail définies**, réparties en 8 axes.  
**Statut : ARCHITECTURE ET BACKLOG DÉFINIS, MOTEUR MULTI-AGENTS NON IMPLÉMENTÉ.**
**Règle :** ceci est une projection de tâches ; **pas** une deuxième Task Queue, un nouvel Event Bus, un dispatcher parallèle à `Patricked-code/MCP`, ni un mécanisme exécutant des travaux sans autorisation.

## 1. Pourquoi « multidirectionnel » et pas une simple checklist linéaire

Le programme suit **V0.1 → V0.2 → V0.3 → V0.4 → V1.0** comme jalons d'admission ; mais les travaux indépendants peuvent être **étudiés et documentés en parallèle** lorsqu'aucune dépendance bloquante, ressource partagée ou permission ne s'y oppose.

Les 8 axes permanents sont :
1. **GOVERNANCE** — PR #6, PR #1→#2→#3, exact SHA, CI, revues, identité, checkpoints et décisions.
2. **SECURITY** — autorisations P1/P2, anti-SSRF, RBAC, secret management, revue des risques, approbations.
3. **ANALYSIS** — campagnes CSV/JSON/TXT, observation Web admise, crawling borné, parsing PHP, Composer/config/runtime, intelligence CVE, preuves, diagnostics et rapports.
4. **REMEDIATION** — suggestions de mise à jour du runtime PHP, diffs, tests Docker, rollback, PHPPATCH.
5. **INFRASTRUCTURE** — API FastAPI, PostgreSQL, worker queue, Docker, DNS/Plesk, adaptateur GitHub/MCP vers S1.
6. **FRONTEND** — saisie d'URL, campagnes, cartographie des pages, états CVE, rapports, deux consoles et suivi.
7. **QUALITY** — tests de non-régression, fixtures, charge sur cibles fictives, tests E2E, tests d'autorisation négatifs.
8. **OPERATIONS** — monitoring, alertes, audits, sauvegardes, releases, maintenance et continuité.

**La priorité active reste `P2S-NEXT-001`** : revue indépendante de PR #6 puis correctifs/revue sur la **branche existante** de PR #1. La file ci-dessus n'admet aucune autre tâche concurrente par le seul fait de son existence.

## 2. Visualisation des flux et points de convergence

```text
        ┌─────────────────────────────────────────────────────────┐
        │ Issue #5 : continuité ; PR #6 ; PR #1 → PR #2 → PR #3 │
        │ revue, exact HEAD, CI, preuve, mandat, NEXT_ACTION      │
        └───────────────────────┬─────────────────────────────────┘
                                │ admission gouvernée
             ┌──────────────────┼────────────────────────┐
             ▼                  ▼                        ▼
        Sécurité P1/P2     Moteur analyse          Plateforme API/Docker
             │             /   |   \                /        \
             │       Web passif  PHP/AST CVE       FastAPI   PostgreSQL/workers
             │             \     |     /                \     /
             └──────────────────► Diagnostics ◄──────────────┘
                                  │
                         preuves et rapports
                                  │
                         PHPPATCH (propositions)
                                  │
                     tests isolés / approbations
                                  │
                  PR + revue + CI + preuve de rollback
                                  │
                           MCP existant (S1)
                                  │
                       staging puis go/no-go
                                  │
                           production autorisée
                                  │
                       supervision, retour vers
                       la détection et le backlog
```

**Aucune flèche n'accorde une permission.** Les portes de gouvernance se répètent à chaque jonction sensible. La branche de production ne démarre pas du seul fait de l'existence d'une URL, d'un CVE ou d'une réussite de CI.

## 3. Pipeline événementiel intelligent à construire (réutilisant les capacités existantes)

**Étape A — OBSERVE.** Lire **GitHub réel** (HEAD, PR, CI, reviews, issues), l'issue #5 et le dernier checkpoint ; si pertinent, état S1 via le **MCP déjà installé** et ses commandes bornées. Consommer de préférence événements GitHub, workflows, mandats existants, et bus/continuity éventuellement déjà gouverné **après validation de leur réalité et de leur portée**.

**Étape B — NORMALIZE / DEDUP.** Établir un `event_id`, `continuity_id`, `work_package_id`, ressource cible, exact SHA, provenance, horodatage. Ignorer les événements répétés, anciens, sans preuve ou portant sur un autre dépôt/une autre autorité.

**Étape C — REASON / PROPOSE.** Un agent de planification peut comparer les constats à `REQ-001..032` et `WORK_PACKAGES.json`, identifier dépendances manquantes, suggérer sous-tâches supplémentaires, corriger les priorités selon risques et générer un mandat **proposé**, jamais une permission implicite. Toute nouvelle tâche doit référencer une exigence/source et éviter les doublons.

**Étape D — ADMIT.** Calculer les candidats dont dépendances sont **VERIFIED_DONE**. Faire les validations suivantes **avant toute prise en charge** : acteur autorisé, scope P1/P2, expiration mandat, rôle, gate requis (`READ_ONLY`, `GOVERNED_PR`, `MANDATED_TEST_ONLY`, `HUMAN_PRODUCTION_APPROVAL`), politique anti-régression, absence de tâches/claims concurrents.

**Étape E — CLAIM / RUN.** Réutiliser exclusivement l'identité stable et le mécanisme de claim/lock/lease du MCP/de la gouvernance actuellement autorisée et vérifiée pour la ressource. Verrouiller **par dépôt/branche/PR, cible S1 ou mandat**, pas globalement pour tout le programme. Exécuter des activités indépendantes en lecture seule en parallèle ; sérialiser les écritures incompatibles. Ne **jamais** exposer un outil d'exécution arbitraire ou importer une autorité de GRT.

**Étape F — VERIFY.** CI au commit exact, validation sécurité/permissions, preuves d'exécution, tests de non-régression, comparaison avant/après ; environnement staging et rollback avant production. Les échecs ne sont pas des succès partiels silencieux : inscrire motif, blocage et action corrective.

**Étape G — RECORD / HANDOFF.** Émettre un checkpoint dans issue #5 selon `PROTOCOL.md`, actualiser `CURRENT_STATE`, `EVENT_LOG`, `DECISIONS_LOG`, `NEXT_ACTION` dans la PR autorisée ; créer l'événement de jalon suivant uniquement **après** validation. Sauvegarder le contexte de reprise sans secrets.

**Étape H — FEEDBACK.** Nouvelles versions PHP/CVE, test de patch rouge, avis corrigé, rollback, nouvelle autorisation ou réponse de review → **réévaluer** les dépendances et priorités. Les suggestions d'amélioration restent `PROPOSED` jusqu'à admission.

## 4. Règles de déclenchement (candidats, pas automations déjà installées)

| Événement constaté | Réponse proposée | Interdiction / condition |
|---|---|---|
| PR #6 approuvée + CI au HEAD | Préparer la suite PR #1 V0.1 | Pas de merge sans gouvernance et compatibilité |
| Test PR #1 échoue | Créer une observation et patch dans sa **branche existante** | Pas de seconde PR/codeur concurrent |
| PR #1 validée/fusionnée | Réconcilier PR #2 sur nouveau HEAD | Pas de rebase forcé sans analyse des dépendances |
| Nouvel avis officiel PHP/CVE | Mettre à jour catalogue/contradictions, ouvrir une proposition de réévaluation | Pas de vulnérabilité déclarée sur un site à partir du seul advisory |
| Nouvelle URL autorisée P1 | Proposer collecte publique bornée et classification | Pas de scan agressif/exploitation ni lecture de source privée |
| Nouvelle preuve P2 sur un projet détenu | Proposer audit code/runtime, puis rapport | Vérifier mandat exact et sécurité des accès |
| Constat avec correction possible | Préparer patch candidat PHPPATCH et tests isolés | Pas de modification de production automatique |
| Tests passés mais revue absente | Attendre autorité de review ; inscrire BLOCKED | Pas de promotion artificielle en DONE |
| Adaptateur MCP et staging validés | Préparer go/no-go, sauvegarde/rollback | Production exige accord humain explicite |
| Échec ou régression en staging/prod | Geler déploiement, collecter preuves, rollback gouverné si mandaté | Pas d'auto-escalade de permissions |
| Fin de conversation / interruption d'agent | Checkpoint et handoff ; nouveau lecteur revalide les sources | Ne pas se fier aux caches ou souvenirs seuls |

## 5. États et invariants

**États futurs (non implémentés) :**

`PLANNED → PROPOSED → SCOPE_VERIFIED → READY → CLAIMED → RUNNING → VERIFYING → VERIFIED_DONE`

Branches possibles : `BLOCKED_DEPENDENCY`, `BLOCKED_AUTHORITY`, `FAILED_WITH_EVIDENCE`, `CANCELLED`, `SUPERSEDED_WITH_TRACE`, `ROLLBACK_REQUESTED`, `ROLLED_BACK_VERIFIED`.

**Les statuts présents dans le JSON sont uniquement des étiquettes de planification** (`PLANNED_NOT_ADMITTED`, `AWAITING_INDEPENDENT_REVIEW`) ; il n'y a **aucune file active PHP2SHELL** attestée par ce document. Ne pas lire `PLANNED` comme `CLAIMED`.

**Invariants :**
- Chaque tâche a un **ID unique**, une exigence, un lane, un jalon, une porte d'autorisation et des dépendances existantes dans un DAG **sans cycle**.
- Chaque action critique fournit `actor`, `authority`, `mandate_id`, `resource_id`, `source_head`, `target_head`, `risk`, `evidence`, `rollback`, `checkpoint` ; utiliser la structure existante des autorités MCP si disponible.
- **Un seul claim d'écriture actif par ressource**, lectures indépendantes concurrentes possibles. Les limites de concurrency et leases viennent des gouvernances existantes, pas d'un second lock manager.
- Un agent ne peut pas s'auto-accorder une autorisation P2 ni une permission de déploiement en production.
- Les mentions « DONE » doivent être appuyées par preuves vérifiables ; aucune suggestion d'IA n'est une validation de sécurité.
- Un dépôt public n'accueille que métadonnées non sensibles ; logs/artefacts privés restent dans des stockages protégés.
- Aucune PR directe `main` ; pas de seconde gateway, pas de Codex/Copilot, pas de suppression de protections.
- La convergence PR #1→#2→#3 concerne **l'ordre des fusions de fond**, pas une interdiction de préparer d'autres dossiers en lecture seule.

## 6. Ordonnancement : une priorité métier, plusieurs axes éligibles

- **P0 gouvernance** : revue PR #6 puis correction de PR #1 (point d'entrée `P2S-NEXT-001`).
- **Préparation sans écriture concurrente** : recherche d'avis PHP officiels, modèles de menaces, définition des contrats d'API, jeu de données fictif, modèles de rapports, revue des capacités MCP. Ces études ne changent pas l'ordre de fusion.
- **P1 fonctionnalité** : V0.2 complète analyse/mandats/imports/crawl autorisé/intelligence CVE.
- **P1 correctifs** : V0.3 patch/rollback/validation avec preuve ; dépend de la qualification des risques et des capacités sandbox.
- **P1 infrastructure** : V0.4 MCP existant, Docker, stockage, API, staging puis chaîne de déploiement gouvernée.
- **P1 interface** : V1.0 deux consoles, rapports, historiques, tests E2E, go/no-go et exploitation.
- **Entretien continu** : veille CVE, logs, sauvegardes, vérification des certificats, supervision des CI ; les mécanismes récurrents ne sont pas encore créés.

## 7. Exemples de parallélisme utile mais gouverné

**Après admissibilité V0.1/V0.2 :** une équipe peut travailler en PR distincte sur l'AST PHP, une autre documenter le catalogue officiel, une troisième concevoir l'anti-SSRF/crawler et une quatrième construire des fixtures offline. Elles ne deviennent pas quatre codeurs concurrents sur une même branche.

**Convergence :** code PHP/AST + avis CVE + preuves runtime + analyse Web admise → moteur de constats → document de remédiation → correctif proposé + sandbox → approbation → interface PHPPATCH → staging → release. Les branches sans preuves attendent.

**Après incident :** nouvelle preuve/CI rouge ⇒ priorité sécurité/régression ; ne pas lancer en parallèle un déploiement indépendant de la correction. Relire les locks, figer les écritures incompatibles et conserver le checkpoint.

## 8. Workflows livrables à concevoir, pas encore actifs

1. **Observation** : PR, reviews et CI GitHub ; événement normalisé, freshness et exact HEAD.
2. **Admission** : permissions et scope, raison du blocage, identités/claims existants.
3. **Exécution code** : PR, tests, revue, audit et checkpoint.
4. **Campagnes Web** : uniquement URL admises, budget, anti-SSRF, preuve et rapport.
5. **Avis sécurité** : ingestion des avis officiels + vérification d'applicabilité P2.
6. **Remédiation** : proposition, approbation, tests Docker, diff et rollback.
7. **Livraison** : GitHub/MCP/S1, staging, go/no-go, monitoring/retour.
8. **Continuité** : dernier checkpoint et revalidation de l'état en conversation suivante.

Le modèle doit être testé sur des fixtures simulant concurrence, échecs CI, retards de review, dépendances non satisfaites, récupération après interruption, claims expirés, conflit HEAD, et demandes hors permission. **Le runtime orchestrateur n'existe pas encore.**

## 9. Ce que ce document ne promet pas

Aucune IA ne peut prédire **exhaustivement toutes les tâches futures** (bugs, demandes, avis CVE, changements d'environnement, contraintes légales). Le backlog de 61 tâches identifie les **travaux actuellement connus** ; toute tâche émergente sera ajoutée sans effacer l'historique, avec justification, test, coût/risque et admission.

**Critère d'acceptation de ce contrat documentaire** : fichier JSON de tâches cohérent et acyclique ; huit lanes et cinq versions préservés, trente-deux exigences conservées, tests CI verts, checkpoint GitHub. Cela **ne vaut pas** validation de fonctionnement multi-agents en temps réel.
