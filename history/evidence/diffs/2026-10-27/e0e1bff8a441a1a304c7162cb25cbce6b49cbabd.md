# Fichiers du commit e0e1bff8a441a1a304c7162cb25cbce6b49cbabd

**Date UTC :** 2026-10-27T22:29:52Z
**Source SHA exacte :** https://github.com/chainsolutions-wealthtech/Php2shell/commit/e0e1bff8a441a1a304c7162cb25cbce6b49cbabd
**Parents Git :** a9d799b008fc65ed5745745bc4ef09e8b889aabe
**Statistiques GitHub :** 1 fichiers ; +62 / -0 lignes.

## Changements observés par fichier

### `00_START_HERE.md` — added

- Blob SHA : `b0008a5e7f237409191355382a14ae8bd6ccd6c7`; +62 / -0.
- [Contenu GitHub](https://github.com/chainsolutions-wealthtech/Php2shell/blob/e0e1bff8a441a1a304c7162cb25cbce6b49cbabd/00_START_HERE.md)

```diff
@@ -0,0 +1,62 @@
+# 00_START_HERE — PHP2SHELL / PHPPATCH
+
+> **Point d'entrée officiel pour reprendre le programme dans toute nouvelle conversation ou avec tout agent autorisé.**
+> **Continuity ID stable :** `PHP2SHELL-CONT-20261027-ROOT-01`
+> **Ancre durable de suivi :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5
+> **Attention :** ce document est ajouté sur une branche de travail ; tant que la PR de continuité n'est pas fusionnée, **ne pas rechercher ce fichier sur `main` par défaut**. Utiliser le lien de la branche ou l'issue #5.
+
+## Objectif fondamental (non négociable)
+
+Concevoir puis livrer une **plateforme défensive de gestion des risques PHP, de l'analyse à la remédiation gouvernée** sur des projets **explicitement autorisés**, avec preuves et niveaux de confiance, avis de sécurité sourcés, propositions de correctifs, tests, approbations, historique et rollback. Aucune exploitation de sites tiers non autorisés, aucune inférence de vulnérabilité avérée à partir d'un simple numéro de version ou motif lexical.
+
+## Architecture retenue
+
+- Dépôt applicatif : `chainsolutions-wealthtech/Php2shell` ; **distinct** de `Patricked-code/MCP` et du Governed-Repository-Template.
+- Serveur de destination : **S1** (Plesk / IONOS), même souscription `wealthtechinnovations.com`.
+- `php2shell.wealthtechinnovations.com` : console d'analyse, inventaire, supervision, rapports.
+- `phppatch.wealthtechinnovations.com` : console de remédiation, diffs, tests, approbations et rollback.
+- **Un moteur partagé et deux interfaces à permissions distinctes**, isolés en conteneurs Docker sur S1 à terme.
+- GitHub PR/CI/revue → **MCP gouverné existant** → S1, sans seconde gateway ou dispatcher ; pas de Codex/Copilot.
+
+## Ordre canonique de lecture avant toute opération
+
+1. Cette entrée `00_START_HERE.md` et l'**issue #5** (lire aussi les derniers commentaires/checkpoints).
+2. `continuity/CURRENT_STATE.md` : snapshot daté, limites de fraîcheur, HEAD et état des branches.
+3. `continuity/NEXT_ACTION.md` : action prioritaire et critères d'admission, ne pas supposer qu'elle reste valable sans réconciliation.
+4. `continuity/DECISIONS_LOG.md` puis `continuity/EVENT_LOG.md` : engagements durables, historique et preuves.
+5. `continuity/PROTOCOL.md` : journalisation et procédure de reprise ; `continuity/HANDOFF.md` : gabarit réutilisable de message initial.
+6. Documents techniques de référence (sur leurs **branches actuelles tant que non fusionnés**) : `docs/ROADMAP.md` et `docs/V0_2_STATIC_ANALYSIS.md` sur PR #2 ; `deploy/S1_DEPLOYMENT_RUNBOOK.md` et `deploy/S1_DOCKER_ARCHITECTURE.md` sur PR #3.
+7. **Revalider l'état en direct** : branches/PR/CI/HEAD GitHub, inventaire MCP/S1 par ping + réconciliation gouvernée, état des vhosts/DNS/TLS si la tâche dépend du serveur. Le GitHub courant prime sur un snapshot, qui prime sur la mémoire conversationnelle non sourcée.
+
+## Programme permanent : versions immuables par objectif, évolutives par ajouts
+
+| Version | Mandat | État au 27/10/2026 |
+|---|---|---|
+| **V0.1** | Prototype CLI, documentation, tests ; finaliser PR #1 | PR #1 ouverte |
+| **V0.2** | Analyse PHP locale, Composer / lock / configs, avis CVE officiels, preuves/confiance | PR #2 en brouillon ; analyse lexicale partielle |
+| **V0.3** | Propositions de correctifs, diffs, validation automatique en Docker isolé, rollback | Non implémenté |
+| **V0.4** | GitHub/MCP existant, S1, gouvernance, Docker isolé, déploiement contrôlé | DNS/TLS et CI préflight uniquement ; PR #3 en brouillon |
+| **V1.0** | Plateforme Web, projets, rapports, historique, workflow et supervision | Non implémenté |
+
+**Vérifications infrastructure ≠ déploiement d'application.** Les URL S1 servent encore la page d'attente Plesk ; l'API et les interfaces ne sont pas encore développées.
+
+## Références d'exécution / ancrage
+
+- **PR #1** https://github.com/chainsolutions-wealthtech/Php2shell/pull/1 — V0.1, cible `main`
+- **PR #2** https://github.com/chainsolutions-wealthtech/Php2shell/pull/2 — V0.2, base branche PR #1
+- **PR #3** https://github.com/chainsolutions-wealthtech/Php2shell/pull/3 — préparation S1, base branche PR #2
+- **Issue #4** https://github.com/chainsolutions-wealthtech/Php2shell/issues/4 — admission et déploiement S1
+- **Issue #5** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5 — ancrage unique de continuité et checkpoints
+- **MCP existant** https://github.com/Patricked-code/MCP/issues/349 — travail de provisionnement sous **autorité MCP séparée**
+
+## Reprise opérationnelle (résumé)
+
+- Lire/valider les sources ci-dessus, puis actualiser `CURRENT_STATE` (en PR) et publier un checkpoint dans l'issue #5 au jalon suivant.
+- Dédupliquer les tâches en consultant PR/issue/checkpoints courants. **Ne pas ouvrir une deuxième PR ou créer une nouvelle identité runtime pour un même travail déjà actif.**
+- Garder une **NEXT_ACTION prioritaire** avec critère de réussite et blocage ; ne pas annoncer de travaux de fond réalisés sans preuve de commit/CI/S1.
+- Aucune mise à jour directe de `main`, aucun déploiement, aucune activation de remédiation autonome sans mandat et contrôles de sécurité.
+- **Toute décision importante de l'utilisateur** doit être enregistrée dans le journal des décisions et reliée à un checkpoint GitHub sans divulguer de contenu privé.
+
+## Vérité importante sur la mémoire inter-conversations
+
+GitHub est le **registre durable et vérifiable**. Une autre conversation ne possède pas nécessairement la transcription de toutes les discussions passées, mais peut récupérer les **décisions, les objectifs, les travaux, les preuves et la prochaine action** dans ce dépôt et l'issue #5. L'archivage automatique mot pour mot de toutes les conversations ChatGPT **n'est pas activé par ces fichiers** : ne jamais prétendre le contraire. Les nouvelles décisions doivent être publiées explicitement selon le protocole.
```

Les diffs sont des preuves du changement Git, et non de tests, droits, sécurité ou déploiement.
