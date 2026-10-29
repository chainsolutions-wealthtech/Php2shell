# Méthode et étendue probatoire — archive intégrale PHP2SHELL–PHPPATCH

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01` ; [issue canonique #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5) ; [PR documentaire #7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7).

## Principes de conservation
1. Conserver les documents `continuity/`, leurs 53 événements à ce point de référence, les décisions, checkpoints, addenda et états datés **sans les réécrire**.
2. Chaque fait documentaire doit porter son origine : `OBSERVED_IN_GITHUB` (GET API, lien exact), `REPORTED_IN_CANONICAL_LOG` (journal existant), `USER_MANDATE`, `NOT_VERIFIED`, `BLOCKED`. Ces termes ne sont pas interchangeables.
3. Les données de code au commit historique s'identifient par SHA complet, date UTC auteur/committer, messages, parents, fichiers et différences. Le lien GitHub `/commit/<sha>` fournit le diff source. Un inventaire de fichiers au SHA ne démontre **ni** que le patch est sûr, **ni** que les tests étaient verts, **ni** que le SHA était déployé.
4. Chaque workflow GitHub Actions est indexé par `run_id`, `head_sha`, `event`, `status`, `conclusion`, `created_at` et `html_url`; un workflow rouge/annulé/en attente demeure dans les preuves. Un listing de runs ne remplace pas l'audit de tous les jobs/logs.
5. Historique des 7 branches observées le 29/10/2026 : `main`, `docs/hardening-v0-1-20261022`, `feat/v0-2-offline-php-static-analysis-20261027`, `ops/s1-readiness-php-services-20261027`, `audit/s1-php-dns-20261027`, `docs/canonical-continuity-20261027`, `docs/integral-chronological-history-20261029`. **363 SHA distincts**, **688 appartenances commit/branche** au cutoff de l'inventaire `history/evidence/git/commit-inventory-all-branches.json`. Les commits apparus après ce cutoff ne réécrivent pas le dénombrement.
6. L'API GitHub annonçait **1 036 workflows Actions** à la première interrogation du 29/10. Ce nombre est une photographie mouvante, pas un dénombrement éternel.
7. Toute divergence de branches, de documentation, de signature, de statut WP ou de portée d'autorisation doit apparaître sans modification rétroactive du fait antérieur.
8. Les SHA des écritures de cette archive ne doivent jamais être interprétés comme des commits applicatifs validés.
9. Le maintien de **claims distincts** est obligatoire : développement du dépôt `Patricked-code/MCP` ; tâches `P2S-WF-*` du dépôt PHP2SHELL ; permissions/claims des ressources MCP, GitHub, Plesk et S1. Aucun passage d'un périmètre à un autre n'est automatique.
10. Une URL publique, une déclaration d'appartenance, une signature locale ou des tests hors ligne ne suffisent pas à autoriser le scan actif, l'accès source, un patch ou le déploiement.
11. Pas de Codex/Copilot, pas de seconde gateway, de nouvelle tâche récurrente, de branche d'archives concurrente ni de mutation directe sur `main` ou S1 ; ne pas fusionner PR #7 pour la seule raison que des fiches documentaires y sont publiées.
12. L'exhaustivité s'évalue couche par couche : (A) inventaire de références accessibles ; (B) détail technique individuel des commits ; (C) index de toutes les CI ; (D) inspection des jobs/logs ; (E) preuves Plesk/S1 ; (F) correspondances décision→WP→REQ→commit→tests→checkpoint ; (G) réconciliation des conversations non publiées. Ne pas déclarer `DONE` à l'échelle du programme si une couche demeure `NOT_VERIFIED`.

## Sources primaires
- [Commits et branches GitHub](https://github.com/chainsolutions-wealthtech/Php2shell/branches)
- [Actions](https://github.com/chainsolutions-wealthtech/Php2shell/actions)
- [Issues et PR](https://github.com/chainsolutions-wealthtech/Php2shell/issues)
- [Ancrage #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5)
- [PR #1](https://github.com/chainsolutions-wealthtech/Php2shell/pull/1) ; [#2](https://github.com/chainsolutions-wealthtech/Php2shell/pull/2) ; [#3](https://github.com/chainsolutions-wealthtech/Php2shell/pull/3) ; [#6](https://github.com/chainsolutions-wealthtech/Php2shell/pull/6) ; [#7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7)
- [Work packages](../continuity/WORK_PACKAGES.json), [journal](../continuity/EVENT_LOG.md), [décisions](../continuity/DECISIONS_LOG.md), [exigences](../continuity/REQUIREMENTS_TRACEABILITY.md)

## Contrôle des limites
Les données présentes sur GitHub peuvent établir le contenu d'un commit ou le statut d'un run. Elles ne prouvent pas à elles seules le déroulement de toutes les actions dans une conversation antérieure ni les changements réellement opérés sur S1, Docker et Plesk. Les bornes de ces observations sont consignées dans chaque dossier individuel.
