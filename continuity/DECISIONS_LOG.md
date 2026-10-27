# DECISIONS_LOG — décisions structurantes immuables

**Continuity ID:** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Ancre durable:** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5

**Ancre :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5  
**Politique :** journal **append-only logique** : ne pas réécrire silencieusement ni supprimer une décision ; ajouter une décision supersédante explicitement référencée si l'utilisateur modifie un choix. Conserver date, autorité, raison, impact et lien de preuve. Ne jamais publier de secrets ou de verbatim privé.

| ID | Date | Décision ou mandat utilisateur consolidé | Impact / règle | Source durable |
|---|---|---|---|---|
| P2S-DEC-001 | 2026-10-22 | Créer un dépôt public `Php2shell` dans l'organisation `chainsolutions-wealthtech`, avec laboratoire fictif et outils défensifs | Sources locales autorisées uniquement ; aucune exploitation de tiers | dépôt et PR #1 |
| P2S-DEC-002 | 2026-10-22 | Construire l'agent suivant un cycle analyse → vulnérabilités prouvées → proposition de patch → tests → validations | Ne pas confondre indicateur et vulnérabilité avérée ; correctif toujours revu | PR #1 / PR #2 |
| P2S-DEC-003 | 2026-10-27 | Respecter intégralement le plan **V0.1 → V0.2 → V0.3 → V0.4 → V1.0**, sans suppression ni régression | Chaque phase additive, critères de sortie documentés | PR #2 `docs/ROADMAP.md` |
| P2S-DEC-004 | 2026-10-27 | Conserver **les deux sous-domaines sur S1** : PHP2SHELL pour l'analyse, PHPPATCH pour la remédiation | **Un moteur partagé**, interfaces à permissions séparées, pas deux plateformes concurrentes | PR #3 / issue #4 |
| P2S-DEC-005 | 2026-10-27 | Architecture cible avec **conteneurs Docker isolés**, GitHub/MCP existants et déploiement gouverné | Pas de serveur de commande/gateway parallèle ; pas d'écriture directe main/S1 | PR #3 Docker architecture |
| P2S-DEC-006 | 2026-10-27 | Maintenir les 5 capacités fondamentales : analyse PHP ; avis CVE officiels ; génération patch ; tests de patch ; interface Web | Les composants non implémentés doivent être clairement identifiés | PR #2 plan directeur |
| P2S-DEC-007 | 2026-10-27 | Exiger une **traçabilité durable** des conversations de travail, décisions, travaux, preuves, objectifs, blocages et reprise depuis toute nouvelle conversation | Issue #5 ancre unique + fichiers canoniques + checkpoint obligatoire par jalon ; pas de garantie de transcription automatique intégrale | issue #5 / PR de continuité |
| P2S-DEC-008 | 2026-10-27 | Éviter Codex/Copilot, les régressions, la fusion des autorités MCP/GRT, les écritures directes sur `main` et les opérations non autorisées | Préserver tests, protections, revues, historique, fonctionnement existant | règles du programme / `docs/GOVERNANCE.md` sur PR #1 |

| P2S-DEC-009 | 2026-10-27 | Confirmer **l'intégralité de la mission fondatrice** : campagnes de centaines/milliers de domaines, CSV/JSON/TXT, identification PHP passive, code autorisé, CVE/intelligence, patch/validation, supervision et rapports | Conserver le scope global au-delà du seul comparateur de versions ; ne jamais convertir un domaine public en autorisation d'audit actif | `continuity/FOUNDING_SPECIFICATION.md` / issue #5 |
| P2S-DEC-010 | 2026-10-27 | Les **six lots historiques** et les cinq versions V0.1→V1.0 sont **deux vues complémentaires** d'un même programme | Conserver FastAPI, PostgreSQL, Redis/workers, Docker isolé, PDF/CSV/JSON et campagnes passives même si ces éléments n'existent pas encore dans le code | `continuity/REQUIREMENTS_TRACEABILITY.md` / PR #6 |
| P2S-DEC-011 | 2026-10-27 | Les CVE-2026-109618 et CVE-2026-109619 ainsi que les correctifs amont sont **documentés par le projet PHP et le CERT-FR** ; leur applicabilité à chaque actif n'est pas attestée par la CLI actuelle | Distinguer sources officielles vérifiées et catalogue/diagnostic effectif à implémenter ; priorité aux correctifs du moteur PHP, en tenant compte des backports | `continuity/CVE_SOURCE_REGISTER.md` / GHSA PHP / CERTFR-2026-ALE-014 |

| P2S-DEC-012 | 2026-10-27 | Ajouter à PHP2SHELL un **audit de site déclenché par URL dans le frontend**, parcours et analyse des pages autorisées, diagnostic PHP/CVE et document de remédiation ; permettre dans PHPPATCH le correctif proposé, les tests et la validation séparée | Ne pas confondre HTTP/HTML/JS public et code PHP serveur ; P2 source/runtime mandaté requis pour l'analyse en profondeur ; crawl borné, anti-SSRF, sans exploit ni patch automatique de tiers ; exigences REQ-023 à REQ-032 | `continuity/URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md` / issue #5 / PR #6 |

| P2S-DEC-013 | 2026-10-28 | Organiser **toutes les prochaines actions identifiables** dans un workflow continu, **multidirectionnel et intelligent**, en préservant la priorité actuelle et la reprise inter-conversations | **61 work packages planifiés / 8 axes / DAG sans cycle / gates** ; détection de dépendances, proposition d'actions, parallélisme lecture seule et anti-doublon par les autorités MCP existantes ; aucun moteur runtime ou autorisation implicite créé | `continuity/WORK_PACKAGES.json` et `continuity/INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md` ; PR #6 / issue #5 |

## Modèle pour prochaine décision

```text
ID: P2S-DEC-014 (ou suivant, après contrôle du journal)
Date UTC:
Source de décision: mandat explicite de l'utilisateur / décision technique argumentée
Texte:
Portée / comptes / dépôts:
Conséquences et non-régression:
Décision remplacée (si applicable):
Preuve GitHub: issue/PR/commentaire/commit
```

**Ne pas prétendre que chaque mot de chaque chat est archivé.** Ce registre capture les décisions **matérielles**, avec liens vers les travaux et les checkpoints publiés.
