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
| PR #2 / V0.2 | `4848bff596977595e58b28db01eaebcd1a128e14` | ouverte, DRAFT, base branche PR #1 ; 58 tests au HEAD | https://github.com/chainsolutions-wealthtech/Php2shell/pull/2 |
| PR #3 / S1 | `e12cb5054d2a7ac9db1829a5da4eb37e6de919f1` | ouverte, DRAFT, base branche PR #2 ; 4 CI au HEAD | https://github.com/chainsolutions-wealthtech/Php2shell/pull/3 |
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

## V0.2 — audit php.ini/FPM et export CSV (28/10/2026)

- **PR #2** à l'exact HEAD `47303c1eea0fc7d454ef5b73ac53d94e5c16875f` : nouveaux fichiers `app/php_config.py`, `app/reporting.py` ; intégration `scan-local` et `--format csv` sans changer le comportement JSON par défaut. Tests `test_php_config.py` et `test_reporting.py` contre symlinks, fichiers trop grands, valeurs sensibles, formules de tableur, erreurs et régressions.
- **49 tests réussis** à ce SHA : GitHub Actions [40605915430](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40605915430) et [40605924812](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40605924812), `SUCCESS`. Des runs intermédiaires `FAILURE` ont corrigé un message de limite incompatible avec un test existant ; la trace de ces corrections reste dans l'historique.
- Les constats `php.ini`/`.user.ini`/PHP-FPM ne prouvent **ni la configuration active, ni l'exploitabilité, ni l'applicabilité réelle d'une CVE**. Le CSV est un **inventaire de constats** et ne vaut pas encore rapport de remédiation complet.
- **PR #3** resynchronisée avec PR #2 par merge commit à deux parents, HEAD `baf7dc9916e117f13ac3d9ce606f72a4e58d38d4`; quatre runs exact SHA : [40606042548](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40606042548), [40606042566](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40606042566), [40606048514](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40606048514), [40606048599](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40606048599) : tous `SUCCESS`.
- La **prochaine admission métier** demeure la revue/fusion gouvernée PR #6 puis PR #1. Le développement des autres lots peut se poursuivre en parallèle uniquement si la ressource n'est pas déjà revendiquée et que les permissions le permettent. Aucun backend Web, API, scheduler multi-agent ni déploiement réel n'est attesté ici.

## V0.2 — première tranche du catalogue CVE sourcé, testée (28/10/2026)

- **PR #2 HEAD actuel de cette tranche :** `4848bff596977595e58b28db01eaebcd1a128e14`. Nouveaux `app/data/php_security_advisories.json`, `app/security_advisories.py`, `tests/test_security_advisories.py` et commandes CLI `advisories` / `review-version --php X.Y.Z`.
- Les deux CVE fondatrices **CVE-2026-109618 / CVE-2026-109619** figurent dans un instantané local vérifié manuellement à partir des avis officiels PHP et de CERTFR-2026-ALE-014. Références `GHSA-w8hw-w9fx-j79w` et `GHSA-6wmf-4rv5-p3rp`, premières versions corrigées upstream : PHP 8.2.35, 8.3.36, 8.4.27, 8.5.12.
- **58 tests** au HEAD, GitHub Actions [40609678329](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40609678329) et [40609685203](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40609685203) **SUCCESS**.
- `check-version` V0.1 **inchangée**. La nouvelle comparaison `review-version` porte sur une version **fournie par l'opérateur** ; `asset_applicability` reste **insufficient_evidence**, jamais une preuve d'exposition. Le registre n'est PAS alimenté par un feed live ; pas de collecte fournisseur/backports, ni d'attestation de runtime ou de configuration effective.
- **PR #3** S1 a intégré PR #2 par merge non forcé à deux parents, HEAD `e12cb5054d2a7ac9db1829a5da4eb37e6de919f1`, quatre CI tests/préflight [40609811420](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40609811420), [40609811814](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40609811814), [40609818834](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40609818834), [40609818986](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40609818986) : **SUCCESS**. **Aucun déploiement S1**.
- **REQ-005 = PARTIELLE** : données sourcées et validations d'instantané, mais pas de récupération officielle automatisée ni de corrélation avec les versions fournisseur. La prochaine admission métier reste la revue des PR #6 puis #1 selon `P2S-NEXT-001`; les autres développements autonomes restent soumis à mandats et claims.

## Points bloquants

1. PR #1 non revue/fusionnée ; ne pas contourner les dépendances des PR empilées.
2. V0.2 n'est pas une analyse de vulnérabilité certifiée ; les deux CVE prioritaires sont **publiées et vérifiées**, mais leur applicabilité par actif et l'ingestion officielle automatisée **ne sont pas implémentées**.
3. Pipeline MCP autorisé et backend/API sécurisés à construire.
4. Le DNS/HTTPS local S1 répondait à la dernière observation (HTTP 200 Plesk sur les deux hôtes) ; l'ancien incident n'a pas de cause confirmée. Une capacité MCP bornée de déploiement PHP2SHELL reste absente.

## Priorité immédiate

Lire `continuity/NEXT_ACTION.md` et vérifier en direct GitHub/MCP les HEAD et éventuels travaux concurrents. Finaliser la PR de continuité indépendante et le protocole de checkpoint, puis **reprendre PR #1**. Ne pas revendiquer une fusion, une mise en production ou une approbation non attestée.

## Fraîcheur et mise à jour

Ce fichier doit être mis à jour **dans une PR dédiée ou la branche légitime en cours**, avec les preuves et les HEAD, après chaque jalon. Les checkpoints de l'issue #5 portent les attestations chronologiques ; si le fichier semble périmé, lire le dernier checkpoint et revalider les sources directes.


## Jalon supplémentaire V0.2 — empreinte et âge du catalogue local (28/10/2026)

- PR #2 : HEAD `2d2d7abee3b33edcc86bb17975cbe8fa5c1c4390`. Nouveau module `app/catalog_audit.py`, commande `audit-catalog --as-of`, tests de dates/empreintes, documentation `docs/V0_2_CATALOG_AUDIT.md`. CI exact SHA [40610646884](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610646884) **SUCCESS**.
- PR #3 : HEAD `58a15991d4218d756f84acbe1d8b1687d4af8bdd`, intégration sans force des quatre fichiers V0.2, diff propre à S1 conservé. CI exact SHA [40610704047](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610704047), [40610704076](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610704076), [40610712317](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610712317), [40610712452](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610712452) **SUCCESS**.
- Fonctionnalité **partielle** : empreinte du JSON canonique et âge de la revue **ne sont ni une vérification live ni une signature officielle**, et ne valident aucun runtime, backport ou CVE sur un actif. Les deux sous-domaines S1, Docker isolé, moteur partagé, workflow URL→audit autorisé→PHPPATCH, 6 lots, 32 exigences et 61 work packages restent intégralement conservés comme objectifs non déployés.
- Priorité `P2S-NEXT-001` inchangée ; PR #1/#6 attendent revue indépendante. Aucun `main` ni S1 modifié. Vérifier les HEAD/CI et la gouvernance à chaque reprise.
