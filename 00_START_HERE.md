# 00_START_HERE — PHP2SHELL / PHPPATCH

> **Point d'entrée officiel pour reprendre le programme dans toute nouvelle conversation ou avec tout agent autorisé.**
> **Continuity ID stable :** `PHP2SHELL-CONT-20261027-ROOT-01`
> **Ancre durable de suivi :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5
> **Attention :** ce document est ajouté sur [PR #6](https://github.com/chainsolutions-wealthtech/Php2shell/pull/6) ; tant que la PR de continuité n'est pas fusionnée, **ne pas rechercher ce fichier sur `main` par défaut**. Utiliser le lien de la branche ou l'issue #5.

## Objectif fondamental (non négociable)

Concevoir puis livrer une **plateforme défensive de gestion des risques PHP, de l'analyse à la remédiation gouvernée** sur des projets **explicitement autorisés**, avec preuves et niveaux de confiance, avis de sécurité sourcés, propositions de correctifs, tests, approbations, historique et rollback. Aucune exploitation de sites tiers non autorisés, aucune inférence de vulnérabilité avérée à partir d'un simple numéro de version ou motif lexical.

## Architecture retenue

- Dépôt applicatif : `chainsolutions-wealthtech/Php2shell` ; **distinct** de `Patricked-code/MCP` et du Governed-Repository-Template.
- Serveur de destination : **S1** (Plesk / IONOS), même souscription `wealthtechinnovations.com`.
- `php2shell.wealthtechinnovations.com` : console d'analyse, inventaire, supervision, rapports.
- `phppatch.wealthtechinnovations.com` : console de remédiation, diffs, tests, approbations et rollback.
- **Un moteur partagé et deux interfaces à permissions distinctes**, isolés en conteneurs Docker sur S1 à terme.
- GitHub PR/CI/revue → **MCP gouverné existant** → S1, sans seconde gateway ou dispatcher ; pas de Codex/Copilot.

## Ordre canonique de lecture avant toute opération

1. Cette entrée `00_START_HERE.md` et l'**issue #5** (lire aussi les derniers commentaires/checkpoints).
2. `continuity/CURRENT_STATE.md` : snapshot daté, limites de fraîcheur, HEAD et état des branches.
3. `continuity/NEXT_ACTION.md` : action prioritaire et critères d'admission, ne pas supposer qu'elle reste valable sans réconciliation.
4. `continuity/DECISIONS_LOG.md` puis `continuity/EVENT_LOG.md` : engagements durables, historique et preuves.
5. `continuity/PROTOCOL.md` : journalisation et procédure de reprise ; `continuity/HANDOFF.md` : gabarit réutilisable de message initial.
6. Documents techniques de référence (sur leurs **branches actuelles tant que non fusionnés**) : `docs/ROADMAP.md` et `docs/V0_2_STATIC_ANALYSIS.md` sur PR #2 ; `deploy/S1_DEPLOYMENT_RUNBOOK.md` et `deploy/S1_DOCKER_ARCHITECTURE.md` sur PR #3.
7. **Revalider l'état en direct** : branches/PR/CI/HEAD GitHub, inventaire MCP/S1 par ping + réconciliation gouvernée, état des vhosts/DNS/TLS si la tâche dépend du serveur. Le GitHub courant prime sur un snapshot, qui prime sur la mémoire conversationnelle non sourcée.

## Réconciliation explicite du mandat fondateur (ajout du 27/10/2026)

**Les cinq versions ne résument pas à elles seules le périmètre fondateur.** Lire obligatoirement :
- [Cahier des charges fondateur](continuity/FOUNDING_SPECIFICATION.md) : agent de cybersécurité PHP, **campagnes à grande échelle**, import CSV/JSON/TXT, identification passive, double niveau d'autorisation (`public_metadata` / `owned_source` avec preuve de mandat), moteur runtime PHP, patch et validation, plateforme Python/FastAPI/PostgreSQL/Redis/workers, Docker et les **six lots de construction historiques**.
- [Matrice d'exhaustivité et de tests d'acceptation](continuity/REQUIREMENTS_TRACEABILITY.md) : exigences `REQ-001` à `REQ-022`, couverture et preuves ; **un lot initial n'est jamais annulé par une version de la roadmap**.
- [Sources CVE vérifiées](continuity/CVE_SOURCE_REGISTER.md) : les CVE-2026-109618/109619 et les versions de correction sont confirmées officiellement en octobre 2026, **mais la fiabilité du catalogue codé, l'applicabilité à une installation et les éventuels backports restent à implémenter/attester**.

**Séparation essentielle :** les besoins d'analyse passive des métadonnées de tiers, de campagnes CSV et de montée en charge restent à développer ; l'analyse approfondie du code/serveur exige une autorisation établie, pas seulement la présence d'un domaine dans une liste. Aucune sonde RCE ni exploitation de tiers n'est autorisée.

## Programme permanent : versions immuables par objectif, évolutives par ajouts

| Version | Mandat | État au 27/10/2026 |
|---|---|---|
| **V0.1** | Prototype CLI, documentation, tests ; finaliser PR #1 | PR #1 ouverte |
| **V0.2** | Analyse PHP locale, Composer / lock / configs, avis CVE officiels, preuves/confiance | PR #2 en brouillon ; analyse lexicale partielle |
| **V0.3** | Propositions de correctifs, diffs, validation automatique en Docker isolé, rollback | Non implémenté |
| **V0.4** | GitHub/MCP existant, S1, gouvernance, Docker isolé, déploiement contrôlé | DNS/TLS et CI préflight uniquement ; PR #3 en brouillon |
| **V1.0** | Plateforme Web, projets, rapports, historique, workflow et supervision | Non implémenté |

**Vérifications infrastructure ≠ déploiement d'application.** Les URL S1 servent encore la page d'attente Plesk ; l'API et les interfaces ne sont pas encore développées.

## Références d'exécution / ancrage

- **PR #1** https://github.com/chainsolutions-wealthtech/Php2shell/pull/1 — V0.1, cible `main`
- **PR #2** https://github.com/chainsolutions-wealthtech/Php2shell/pull/2 — V0.2, base branche PR #1
- **PR #3** https://github.com/chainsolutions-wealthtech/Php2shell/pull/3 — préparation S1, base branche PR #2
- **Issue #4** https://github.com/chainsolutions-wealthtech/Php2shell/issues/4 — admission et déploiement S1
- **Issue #5** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5 — ancrage unique de continuité et checkpoints
- **PR #6** https://github.com/chainsolutions-wealthtech/Php2shell/pull/6 — fichiers canoniques et tests, **non fusionnée**
- **MCP existant** https://github.com/Patricked-code/MCP/issues/349 — travail de provisionnement sous **autorité MCP séparée**

## Reprise opérationnelle (résumé)

- Lire/valider les sources ci-dessus, puis actualiser `CURRENT_STATE` (en PR) et publier un checkpoint dans l'issue #5 au jalon suivant.
- Dédupliquer les tâches en consultant PR/issue/checkpoints courants. **Ne pas ouvrir une deuxième PR ou créer une nouvelle identité runtime pour un même travail déjà actif.**
- Garder une **NEXT_ACTION prioritaire** avec critère de réussite et blocage ; ne pas annoncer de travaux de fond réalisés sans preuve de commit/CI/S1.
- Aucune mise à jour directe de `main`, aucun déploiement, aucune activation de remédiation autonome sans mandat et contrôles de sécurité.
- **Toute décision importante de l'utilisateur** doit être enregistrée dans le journal des décisions et reliée à un checkpoint GitHub sans divulguer de contenu privé.

## Vérité importante sur la mémoire inter-conversations

GitHub est le **registre durable et vérifiable**. Une autre conversation ne possède pas nécessairement la transcription de toutes les discussions passées, mais peut récupérer les **décisions, les objectifs, les travaux, les preuves et la prochaine action** dans ce dépôt et l'issue #5. L'archivage automatique mot pour mot de toutes les conversations ChatGPT **n'est pas activé par ces fichiers** : ne jamais prétendre le contraire. Les nouvelles décisions doivent être publiées explicitement selon le protocole.
