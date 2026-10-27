# CURRENT_STATE — Snapshot contrôlé, non temps réel

**Continuity ID:** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Capture datée:** 2026-10-28, nouvelle réconciliation GitHub/MCP, état documentaire figé après l'observation  
**Source de vérité actuelle :** GitHub API et sondes S1 observées au moment de la reprise, **pas** ce tableau statique ; vérifier avant toute action.  
**Ancre :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5

## GitHub — état vérifié au moment de la rédaction

| Objet | HEAD / identifiant | Statut observé | Autorité |
|---|---|---|---|
| Dépôt source | `chainsolutions-wealthtech/Php2shell` | public | dépôt GitHub |
| `main` | `a9d799b008fc65ed5745745bc4ef09e8b889aabe` | inchangé, CLI expérimentale | ref GitHub |
| PR #1 / V0.1 | `c17f0931db2cae659e4301585b0bf3db9078ca09` | ouverte, base `main` | https://github.com/chainsolutions-wealthtech/Php2shell/pull/1 |
| PR #2 / V0.2 | `664cf5cde8743713053f4799c24b7d05a074441f` | ouverte, DRAFT, base branche PR #1 | https://github.com/chainsolutions-wealthtech/Php2shell/pull/2 |
| PR #3 / S1 | `2d599f48958d54ceefa1454e01a37eb56d86c06d` | ouverte, DRAFT, base branche PR #2 | https://github.com/chainsolutions-wealthtech/Php2shell/pull/3 |
| Issue #4 | — | ouverte, admission S1 | https://github.com/chainsolutions-wealthtech/Php2shell/issues/4 |
| Issue #5 | — | ancre de continuité ouverte | https://github.com/chainsolutions-wealthtech/Php2shell/issues/5 |
| Branche continuité | `docs/canonical-continuity-20261027` | créée sur `main` vérifié ; **PR #6 ouverte, non fusionnée** | https://github.com/chainsolutions-wealthtech/Php2shell/pull/6 |

**CI vérifiées** au HEAD des branches lors de la reprise :
- PR #2 `d7f2b1d...` : runs [40594022774](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40594022774) et [40594015822](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40594015822), `success`.
- PR #3 `84fc090...` : runs [40594201282](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40594201282) (réseau) et [40594201214](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40594201214) (tests), `success`.
- PR #1 : vérifier CI, revue et HEAD **à nouveau avant fusion** ; aucun succès récent certifié ici.

## Branche documentaire indépendante

- **PR #6** https://github.com/chainsolutions-wealthtech/Php2shell/pull/6 : ancre et dossiers de continuité, base `main`, ne touche ni PR #1-3 ni S1. La CI exacte doit être revalidée au **dernier HEAD de cette branche**, car les références internes peuvent évoluer pendant la préparation de la PR.

## Infrastructure S1 — constat daté

- S1 IPv4 connu par contexte MCP : `212.227.212.33`; domaine parent `wealthtechinnovations.com`.
- Plesk : 2 répertoires de sous-domaines et 2 répertoires système observés pour `php2shell` / `phppatch`.
- DNS : 4 serveurs IONOS autoritaires ont publié l'IPv4 S1 pour les deux ; les anciens AAAA de parking ont été retirés.
- TLS direct S1 : deux certificats Let's Encrypt valides au 27/10/2026, échéances 25/01/2027, HTTP→HTTPS 301.
- HTTPS public direct vers S1 : HTTP 200 **page d'attente Plesk (~464 octets)**, **pas** plateforme.
- **Historique** : erreurs locales S1 `curl (6)`/`curl (35)` observées après modification DNS ; au nouveau contrôle du **27/10/2026 à 23:42 UTC**, les requêtes `curl -I https://php2shell.wealthtechinnovations.com` et `curl -I https://phppatch.wealthtechinnovations.com` **réussissent toutes deux depuis S1** (`code 0`, `HTTP 200`, Apache/PleskLin, `Content-Length: 464`). La résolution locale et HTTPS sont donc **opérationnels à cette observation**, sans preuve de purge DNS ni diagnostic rétrospectif de la cause.
- MCP existant : `Patricked-code/MCP`, mécanismes gouvernés séparés ; aucune commande générique autorisée pour déployer ces nouvelles applications n'était attestée.

## Construction fonctionnelle — ce qui est réellement livré

- **V0.1** : prototype CLI local (informations de versions démonstratives), tests et documentation sur PR #1.
- **V0.2** : analyse statique lexicale locale et `composer.json` sur PR #2, 22 tests lors du jalon d'analyse, documentation/CI verts. AST, parsing des configurations/runtime réels, catalogue CVE officiel intégré et preuve d'autorisation technique manquent ; `composer.lock` est désormais inspecté **hors ligne** mais ne prouve pas les versions installées.
- **V0.3** : pas encore de moteur de génération de patches ni de validation automatique des patches.
- **V0.4** : infrastructure DNS/TLS/Plesk prête et runbooks/CI préflight ; aucune application Docker Web/API déployée, pas d'adaptateur MCP pour PHP2SHELL.
- **V1.0** : pas encore de consoles Web ni de gestion de projets ou workflow d'approbations opérationnels.

## Réconciliation des exigences fondatrices — addendum documentaire 27/10/2026

- Le texte intégral du **cahier des charges reconstitué** est conservé sous `continuity/FOUNDING_SPECIFICATION.md`, avec 10 capacités produit et les six lots historiques.
- Le tableau `continuity/REQUIREMENTS_TRACEABILITY.md` couvre `REQ-001` à `REQ-022` : les campagnes CSV/TXT, la détection PHP passive à grande échelle, les autorisations vérifiées, FastAPI/PostgreSQL/Redis/workers, les tests de patches et les deux interfaces **ne sont pas déclarés livrés** sans tests.
- `continuity/CVE_SOURCE_REGISTER.md` répertorie les **deux CVE officiellement confirmées** et les seuils de correction PHP amont. Le code V0.1 reste un comparateur de versions sans attestation par actif et l'ingestion sourcée n'est pas encore implantée.
- Les documents de continuité restent sur **PR #6** tant qu'ils ne sont pas fusionnés ; toujours interroger GitHub pour le HEAD et la CI exacts après ces ajouts.

## Extension UX « audit d'URL et remédiation » — ajout au backlog du 27/10/2026

Spécification additive [`URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md`](URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md), exigences **REQ-023→REQ-032** de `REQUIREMENTS_TRACEABILITY.md` : champ URL frontend, crawl Web borné sous autorisation, cartographie et analyse des pages publiques, diagnostic par preuve, panneau CVE PHP2Shell, connecteur source/runtime P2 pour analyse profonde, rapport PDF/JSON/CSV, transfert vers PHPPATCH pour correctifs proposés et validations. **État = planifié/non implémenté.** Aucun audit de cible réelle effectué ni modification S1 par cet ajout. Une URL Web ne livre pas les sources PHP privées.

La **priorité active reste P2S-NEXT-001** : revue PR #6, puis correction/finalisation gouvernée de PR #1 ; aucun changement de l'ordre V0.1→V1.0.

## Work packages et orchestration — extension documentaire au 28/10/2026

Deux nouveaux fichiers sont ajoutés sur la branche **PR #6 non fusionnée** : [`WORK_PACKAGES.json`](WORK_PACKAGES.json) (61 unités de travail candidates, 8 axes, liens aux REQ-001→032, dépendances et permissions) et [`INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md`](INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md) (proposition de fonctionnement event-driven, déduplication, admission via gouvernance existante, priorités et tests). Ces documents **ne sont pas un scheduler actif**, aucune tâche runtime n'a été créée ni aucun agent nouveau provisionné. Les références GitHub/CI doivent être actualisées avant tout statut `VERIFIED_DONE`. **Priorité active inchangée : P2S-NEXT-001**.

## Réconciliation de construction — 28 octobre 2026 (ajout après mise à jour)

- **PR #1** : trois observations corrigées sur sa branche existante (DNS par label, assertion d'avis non vide, documentation Docker), HEAD `c17f0931db2cae659e4301585b0bf3db9078ca09` ; CI [40602856210](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40602856210) et [40602863436](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40602863436) **SUCCESS**.
- **PR #2** : commande hors ligne `import-targets` pour CSV/JSON/TXT (normalisation, déduplication, P1/P2 sans élévation implicite), tests ; **merge commit à deux parents** intégrant les dernières corrections PR #1 sans rebase ni force ; HEAD `664cf5cde8743713053f4799c24b7d05a074441f` ; CI [40603426908](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40603426908) et [40603432495](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40603432495) **SUCCESS (31 tests)**.
- **PR #3** : branche S1 resynchronisée par merge commit à deux parents avec PR #2, HEAD `2d599f48958d54ceefa1454e01a37eb56d86c06d` ; CI S1/DNS/TLS et suite de tests **SUCCESS** (runs [40603599603](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40603599603), [40603599615](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40603599615), [40603607636](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40603607636), [40603607747](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40603607747)).
- **PR #6** : HEAD `1285c8d9a385c0e13a79ecb872b100f88540eea3` au dernier contrôle **avant le présent document** ; tests append-only inclus, 33 tests et CI réussies. Revue demandée au compte **Patricked-code** sur PR #1 et #6 ; **aucune approbation reçue à l'instant d'observation**.
- **S1** : MCP ping/réconciliation réussis, deux sous-domaines reconfirmés, mais **aucun outil borné d'écriture/déploiement PHP2SHELL/PHPPATCH n'est exposé**. Ne pas détourner les outils `legacy_vhost` ou SadiaAF, ne pas toucher aux vhosts hors autorisation.
- **Capacité serveur** : état Docker S1 observé le 27/10 à 23:42 UTC : **seul conteneur actif `wealthtech_mcp_ssh_bridge`**, aucun service PHP2SHELL/PHPPATCH ; disque racine **77 Go, 53 Go utilisés, 21 Go disponibles (72 %)**. La présence Plesk et une réponse HTTP 200 ne signifient pas installation de l'application.
- **Automatisation de continuité** : tâche `6ae13640aa9c8191b20d3d120bf71ace`, récurrence **horaire**, activée. Cette tâche déclenche un nouveau contrôle/éventuelle exécution admissible et checkpoint ; **ce n'est pas le runtime multi-agents final ni une promesse de déploiement automatique**. Ne pas dupliquer les missions Regulatory/MCP existantes.
- La NEXT_ACTION demeure la validation/revue gouvernée des branches existantes ; les développements additionnels indépendants ne valent pas autorisation de fusion ou de mise en production.

## V0.2 — lecture de Composer.lock ajoutée (28/10/2026)

- PR #2 HEAD **`664cf5cde8743713053f4799c24b7d05a074441f`** : l'analyse locale `scan-local` lit désormais `composer.lock` en lecture seule, limite taille/nombre de paquets et n'exporte que noms, versions verrouillées et groupes `packages`/`packages-dev`. Refuse les symlinks ; distingue verrouillage de l'installation réelle sur serveur.
- Nouveaux tests couvrant manifestes invalides, symlinks, absence du lockfile et filtrage des données d'origine potentiellement sensibles. Deux CI au HEAD : [40604158593](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40604158593) et [40604165162](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40604165162), **SUCCESS**.
- PR #3 resynchronisée **sans rebase forcé** au HEAD `2d599f48958d54ceefa1454e01a37eb56d86c06d` ; CI exact SHA à vérifier avant admission. PR #1 et PR #6 inchangées par ce développement.
- **REQ-008 demeure PARTIELLE**, car les configurations complètes et les versions réellement installées ne sont pas attestées. Les CVE ne sont pas confirmées pour un actif d'après un lockfile seul.

## Points bloquants

1. PR #1 non revue/fusionnée ; ne pas contourner les dépendances des PR empilées.
2. V0.2 n'est pas une analyse de vulnérabilité certifiée ; les CVE d'exemple ne sont pas vérifiées.
3. Pipeline MCP autorisé et backend/API sécurisés à construire.
4. DNS local S1 à diagnostiquer à l'aide des seules capacités autorisées.

## Priorité immédiate

Lire `continuity/NEXT_ACTION.md` et vérifier en direct GitHub/MCP les HEAD et éventuels travaux concurrents. Finaliser la PR de continuité indépendante et le protocole de checkpoint, puis **reprendre PR #1**. Ne pas revendiquer une fusion, une mise en production ou une approbation non attestée.

## Fraîcheur et mise à jour

Ce fichier doit être mis à jour **dans une PR dédiée ou la branche légitime en cours**, avec les preuves et les HEAD, après chaque jalon. Les checkpoints de l'issue #5 portent les attestations chronologiques ; si le fichier semble périmé, lire le dernier checkpoint et revalider les sources directes.
