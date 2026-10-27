# CURRENT_STATE — Snapshot contrôlé, non temps réel

**Continuity ID:** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Capture datée:** 2026-10-27, lecture GitHub de la présente intervention  
**Source de vérité actuelle :** GitHub API et sondes S1 observées au moment de la reprise, **pas** ce tableau statique ; vérifier avant toute action.  
**Ancre :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5

## GitHub — état vérifié au moment de la rédaction

| Objet | HEAD / identifiant | Statut observé | Autorité |
|---|---|---|---|
| Dépôt source | `chainsolutions-wealthtech/Php2shell` | public | dépôt GitHub |
| `main` | `a9d799b008fc65ed5745745bc4ef09e8b889aabe` | inchangé, CLI expérimentale | ref GitHub |
| PR #1 / V0.1 | `26287b66ccd6087955ac587d08ff3ca49d340fd8` | ouverte, base `main` | https://github.com/chainsolutions-wealthtech/Php2shell/pull/1 |
| PR #2 / V0.2 | `d7f2b1d21c6e7c8269eab23c5547d738118bae2f` | ouverte, DRAFT, base branche PR #1 | https://github.com/chainsolutions-wealthtech/Php2shell/pull/2 |
| PR #3 / S1 | `84fc090e08ca6e31e965c6bfab90f3556161e2d2` | ouverte, DRAFT, base branche PR #2 | https://github.com/chainsolutions-wealthtech/Php2shell/pull/3 |
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
- Défaillances résolveur local S1 précédemment observées (`curl (6)` et `curl (35)`) ; origine non résolue au checkpoint, non présumer cache purgé.
- MCP existant : `Patricked-code/MCP`, mécanismes gouvernés séparés ; aucune commande générique autorisée pour déployer ces nouvelles applications n'était attestée.

## Construction fonctionnelle — ce qui est réellement livré

- **V0.1** : prototype CLI local (informations de versions démonstratives), tests et documentation sur PR #1.
- **V0.2** : analyse statique lexicale locale et `composer.json` sur PR #2, 22 tests lors du jalon d'analyse, documentation/CI verts. AST, `composer.lock`, parsing configurations, catalogue CVE officiel et preuve d'autorisation technique manquent.
- **V0.3** : pas encore de moteur de génération de patches ni de validation automatique des patches.
- **V0.4** : infrastructure DNS/TLS/Plesk prête et runbooks/CI préflight ; aucune application Docker Web/API déployée, pas d'adaptateur MCP pour PHP2SHELL.
- **V1.0** : pas encore de consoles Web ni de gestion de projets ou workflow d'approbations opérationnels.

## Réconciliation des exigences fondatrices — addendum documentaire 27/10/2026

- Le texte intégral du **cahier des charges reconstitué** est conservé sous `continuity/FOUNDING_SPECIFICATION.md`, avec 10 capacités produit et les six lots historiques.
- Le tableau `continuity/REQUIREMENTS_TRACEABILITY.md` couvre `REQ-001` à `REQ-022` : les campagnes CSV/TXT, la détection PHP passive à grande échelle, les autorisations vérifiées, FastAPI/PostgreSQL/Redis/workers, les tests de patches et les deux interfaces **ne sont pas déclarés livrés** sans tests.
- `continuity/CVE_SOURCE_REGISTER.md` répertorie les **deux CVE officiellement confirmées** et les seuils de correction PHP amont. Le code V0.1 reste un comparateur de versions sans attestation par actif et l'ingestion sourcée n'est pas encore implantée.
- Les documents de continuité restent sur **PR #6** tant qu'ils ne sont pas fusionnés ; toujours interroger GitHub pour le HEAD et la CI exacts après ces ajouts.

## Points bloquants

1. PR #1 non revue/fusionnée ; ne pas contourner les dépendances des PR empilées.
2. V0.2 n'est pas une analyse de vulnérabilité certifiée ; les CVE d'exemple ne sont pas vérifiées.
3. Pipeline MCP autorisé et backend/API sécurisés à construire.
4. DNS local S1 à diagnostiquer à l'aide des seules capacités autorisées.

## Priorité immédiate

Lire `continuity/NEXT_ACTION.md` et vérifier en direct GitHub/MCP les HEAD et éventuels travaux concurrents. Finaliser la PR de continuité indépendante et le protocole de checkpoint, puis **reprendre PR #1**. Ne pas revendiquer une fusion, une mise en production ou une approbation non attestée.

## Fraîcheur et mise à jour

Ce fichier doit être mis à jour **dans une PR dédiée ou la branche légitime en cours**, avec les preuves et les HEAD, après chaque jalon. Les checkpoints de l'issue #5 portent les attestations chronologiques ; si le fichier semble périmé, lire le dernier checkpoint et revalider les sources directes.
