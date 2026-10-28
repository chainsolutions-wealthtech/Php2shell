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

## V0.2 — mises à jour d'avis PHP proposées, sans écriture (28/10/2026)

- **PR #2** HEAD exact `bf8a8bad37cc370da15706ea5331cb927c666005`, nouveaux `app/catalog_update.py`, `tests/test_catalog_update.py` et `docs/V0_2_CATALOG_UPDATE_PROPOSAL.md`; commande additive `propose-catalog-update`. Les fichiers candidats sont contrôlés localement, les CVE retirées et dates régressives bloquées, les changements de sources, GHSA et seuils upstream isolés pour une revue indépendante. **Rien n'est appliqué au catalogue acquis**.
- **73 tests** au SHA exact ; [GitHub Actions #40611408263](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40611408263) et [#40611412973](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40611412973) : **SUCCESS**.
- **PR #3 S1** : raccordée par commit à deux parents sans réécrire l'historique `318d60e33858be0447540fc08b42a3c14b1d23f0`, puis addendum de runbook en mode PR sur HEAD `4461048c244b60907a0b92a714dc7a59b8add38a`. Quatre exécutions CI/preflight au SHA final : [#40611726538](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40611726538), [#40611726553](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40611726553), [#40611735365](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40611735365), [#40611735409](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40611735409) : **SUCCESS**.
- **Aucune vraie mise à jour de sources officielles en ligne, ni signature, ni collecte runtime, ni application de correctif**, et aucune preuve d'installation applicative sur les deux sous-domaines S1. Les pages Plesk restent le dernier état observé. Les workflows de continuité sont documentés mais le runtime multi-agent complet n'existe pas encore.
- **PR #6** et **PR #1** attendent toujours une revue réellement approuvée au dernier contrôle ; le fait qu'elles soient fusionnables techniquement ne remplace pas cette autorité. Les 61 unités de travail, cinq versions et 32 exigences restent conservées.

## V0.2 — client public borné d'avis PHP via GitHub API (28/10/2026)

- **PR #2 HEAD exact** : `e02ac06fe715ac643313e4d1a0110d56129fb8d6`. Ajouts `app/advisory_fetch.py`, `tests/test_advisory_fetch.py`, `docs/V0_2_OFFICIAL_ADVISORY_FETCH.md`, commande `fetch-official-advisory --ghsa ... --as-of YYYY-MM-DD --permit-official-network`. Autorité de référence : REST GitHub GET `https://api.github.com/advisories/{GHSA}` (point officiel public), **GHSA limité aux deux entrées courantes du catalogue**.
- Réseau **uniquement sur invocation explicite** ; URL/identifiant construits selon la liste admise, aucun paramètre d'URL libre, proxy de l'environnement désactivé, TLS système, redirections bloquées, délai de 8 s, corps JSON limité à 128 000 octets. Identité GHSA/CVE et provenance de l'URL contrôlées, dates UTC, statut revoked/unreviewed et sévérité réconciliés. Données de réponse brutes non exposées, aucun secret, code source ou CVE vulnérable d'actif confirmé.
- **81 tests, OK** au SHA exact ; CI [40613045223](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40613045223) et [40613051184](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40613051184) **SUCCESS**. Tests réseau réalisés **avec doubles simulés** ; **aucune acquisition publique réellement exécutée ou validée end-to-end** dans cette tranche. Le nouvel endpoint GitHub n'est pas un collecteur PHP/CERT-FR complet.
- **PR #3 S1** raccordée par merge deux parents **sans force**, HEAD `708d912ad19b54a4a9410084058d9114396d591c`, 4 CI de tests et préflight **SUCCESS** au SHA exact : [40613158933](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40613158933), [40613159138](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40613159138), [40613165750](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40613165750), [40613165764](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40613165764). **Aucune application déployée ni configuration S1 modifiée**.
- **REQ-005 reste PARTIELLE** : ni ingestion périodique validée sur API réelle, ni avis tiers/fournisseur backport, ni runtime/SAPI attesté, ni promotion automatique. Le test de transport n'est pas une preuve d'authenticité cryptographique. Prochaine étape technique : enrichissement du contrat de récupération sourcée, traitement des réponses live sous supervision/approbation et recoupement PHP/CERT-FR.
- **NEXT_ACTION de gouvernance P2S-NEXT-001 inchangée** : revue indépendante puis décision de fusion des PR #6 et #1. Automatisation horaire existante reste le seul mécanisme de relance entre sessions, pas de daemon permanent construit.

## V0.2 — enveloppe de déclaration runtime/SAPI et preuve non authentifiée (28/10/2026)

- **PR #2 HEAD `424425116f54c353211aae554fc3866c242689b2`** : `app/runtime_evidence.py`, tests `tests/test_runtime_evidence.py`, manuel `docs/V0_2_RUNTIME_EVIDENCE.md`, CLI `review-runtime-evidence`. Le module inspecte un fichier JSON local `DECLARED_PHP_RUNTIME`, date UTC, mandat de laboratoire **déclaré**, SAPI, version PHP et `vendor_backport_status=not_verified`, avec limites de taille, symlinks et refus d'injection de champs `signature_verified`/`asset_applicability`.
- Sorties explicitement `mandate_authorization_verified=false`, `signature_verified=false`, `effective_http_runtime_attested=false` et `asset_applicability=insufficient_evidence`. Les versions inférieures aux correctifs upstream restent **des indices non confirmés** ; aucune signature/autorisation réelle vérifiée.
- GitHub Actions au SHA exact [40614036258](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40614036258) et [40614041127](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40614041127) : **SUCCESS / 89 tests OK**.
- **PR #3 HEAD `199641477f9fbdb3cfdfcb6c98edcaa3f60b2020`** : branche downstream fusionnée avec la dernière PR #2 via un commit à deux parents et `force=false`. Quatre CI au SHA final [40614130584](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40614130584), [40614130764](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40614130764), [40614135727](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40614135727), [40614135746](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40614135746) **SUCCESS**.
- Aucun scan tiers, émission de commande PHP, collecte réelle sur S1, changement DNS/Plesk, patch de code PHP ni déploiement. **REQ-006 reste PARTIELLE**, le backport et les permissions P2 réelles sont bloquants ; roadmap V0.1→V1.0, 6 lots, 32 exigences, 61 work packages intacts.

## V0.2 — dossier d'audit et prévisualisation URL, construction vérifiée (28/10/2026)

- **PR #2 V0.2 HEAD `4ded6646d57af4bb8f6ee11f4a7b73c828962d29`** : module `app/audit_dossier.py` + `tests/test_audit_dossier.py` + `docs/V0_2_AUDIT_DOSSIER.md` ; CLI `audit-dossier --path ... --as-of ... [--runtime-file ...] --format json|markdown`. Produit des observations à IDs de preuve, règles, chemins relatifs, niveaux indicatifs et actions humaines de remédiation, sans contenu PHP brut, secrets de configs/composer, référence de mandat ou chemin absolu. Rapport **brouillon**, `vulnerability_verdict=INSUFFICIENT_EVIDENCE`, `production_safe_to_patch=false` et `patch_status=NOT_GENERATED`. Version déclarée optionnelle, **jamais** runtime attesté.
- Même PR : module `app/url_intake.py` + `tests/test_url_intake.py` + `docs/V0_2_URL_INTAKE_PREVIEW.md` ; CLI `preview-url --url https://... [--scope public_metadata|owned_source] [--mandate-ref ...]`. Prépare seulement la syntaxe HTTPS, portée et budgets (max 100 pages, 30 req/min) ; bloque les IP et hôtes locaux explicites, ports inhabituels, fragments/query, URL credentials, chemins traversons. **`allowed_to_crawl=false`**, **`dns_and_public_ip_validated=false`**, **`mandate_authentication_verified=false`**, aucun crawl ni résolution DNS. Une URL syntaxiquement correcte ne garantit jamais un réseau public : contrôle DNS/rebinding et redirections **à construire**.
- **113 tests au HEAD exact** ; CI GitHub [#40619000385](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40619000385) et [#40619006476](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40619006476) **SUCCESS**. Les tests sont hors ligne, les acquittements de sécurité ne sont pas des autorisations de production.
- **PR #3 S1** : merges successifs sans rebase forcé depuis la dernière PR #2, HEAD final `3739323768ca9b59a87eabe3cd96730a238c0f86` ; quatre tests / préflight au SHA final [#40619142462](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40619142462), [#40619142464](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40619142464), [#40619149871](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40619149871), [#40619149899](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40619149899) **SUCCESS**. Aucune écriture S1, ni vhost/Docker installé.
- **REQ-002/REQ-022/REQ-031 PARTIELLES uniquement à l'entrée**, **REQ-019 PARTIELLE** (dossier Markdown+JSON, pas PDF complet ni Git patch), **REQ-003 NON authentifiée**. Cette tranche prépare le flux URL→audit autorisé→diagnostic→PHPPATCH mais **n'implémente pas** le vrai crawler, la revue de code serveur sans dépôt, l'API FastAPI, PostgreSQL, Redis, les interfaces Web ou le déploiement.
- **P2S-NEXT-001 inchangée** : revue indépendante PR #6 et PR #1 ; la tâche horaire existante `6ae13640aa9c8191b20d3d120bf71ace` assure la recherche des prochains travaux admissibles, sans collision, ni promesse de daemon permanent.

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


## Jalon V0.2 — CSV des comparaisons PHP/SAPI non attestées (28/10/2026)

- **PR #2** HEAD `e5df6bb8761584716a60bab9067c880276b97b14` : module `app/runtime_reporting.py`, `review-runtime-evidence --format csv`, sept tests de reporting, documentation `docs/V0_2_RUNTIME_CSV_REPORT.md`. **96 tests** au HEAD, CI [40616269007](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616269007) et [40616272906](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616272906) SUCCESS.
- **PR #3** HEAD `2d3d2c9107a5b2c9ac2fdfcc6239083bbba8211b` : branche S1 resynchronisée par merge à deux parents, sans force, fichiers propres S1 conservés. CI [40616321539](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616321539), [40616321597](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616321597), [40616327531](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616327531), [40616327538](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616327538) SUCCESS.
- La sortie CSV **n'atteste ni mandat, ni runtime HTTP, ni signature, ni backport, ni applicabilité CVE**. Seuls des champs autorisés sont exportés avec protection anti-formules. JSON historique conservé. **REQ-019 demeure PARTIELLE** : PDF, dossier de remédiation et flux PHPPATCH non livrés.
- **P2S-NEXT-001 inchangée** : revue réellement indépendante PR #6 puis PR #1 avant fusion gouvernée. Les 6 lots, 32 exigences, 61 work packages, V0.1→V1.0, workflow URL→audit autorisé→PHPPATCH, Docker isolé, moteur partagé et les deux sous-domaines S1 demeurent au programme, sans déploiement attesté.
- MCP read-only `ping` a exigé une interaction de connexion indisponible dans cette exécution ; aucune sonde S1 ni claim runtime MCP n'est prétendu vérifié. La construction GitHub s'est appuyée sur le mandat utilisateur explicite, les branches existantes et le contrôle `expected_sha` anti-collision. Aucun nouvel agent/claim/gateway créé.


## Checkpoint technique additionnel — P2S-EVT-025, 28/10/2026

- **PR #2 V0.2** `fc277eb8b8f1a277a606826e48bbf673028f8449` : nouveau handoff local de revue PHP2SHELL→PHPPATCH, 9 tests additionnels, **122 tests SUCCESS** aux CI #40622112932/#40622118348. Aucun patch généré, aucune autorisation élevée, aucun accès réseau, aucun chemin/code/secret exporté vers la file de revue.
- **PR #3** `686e68980c5807ca84bcdf4ef1e8a2f046fe09f8` : merge Git à deux parents avec PR #2, sans rebase forcé, 3 fichiers propres au preflight S1 conservés, **4 CI SUCCESS** au SHA exact #40622188626/#40622188699/#40622194348/#40622194350.
- **PR #1** `c17f0931db2cae659e4301585b0bf3db9078ca09` OPEN ; **PR #6** en attente de CI et revue indépendante ; `main` reste à vérifier en direct à chaque reprise. `Patricked-code` sollicité sur #1/#6, aucun APPROVED observé lors de cette tranche.
- **MCP read-only** ping/reconcile : deux sous-domaines S1 listés sous la même souscription, aucun outil de déploiement spécifique PHP2SHELL/PHPPATCH trouvé dans le catalogue ; pas de mandat runtime PHP ni de déploiement revendiqué. La file MCP n'est pas une autorité de claims du dépôt PHP2SHELL.
- **État métier** : V0.2 toujours PARTIELLE ; REQ-029/030 partiellement préparées, V0.3 diff/sandbox/rollback non implémentée, V0.4 Docker/MCP/S1 non déployée, V1.0 frontend non implémenté. Les 6 lots, 32 exigences, 61 work packages, moteur partagé, workflow URL→audit autorisé→diagnostic→PHPPATCH et les deux sous-domaines sont conservés.

## Jalon complémentaire — sécurité, campagnes et aperçu Web (28/10/2026)

- **PR #2 HEAD `e9533f2adda02ad1dcb254b3d3bba64cb398884b`** : `app/admission_preflight.py`, `app/network_preflight.py`, `app/campaign_plan.py`, `app/report_html.py`, commandes `plan-campaign` et `audit-dossier --format html`, maquette `web/php2shell/index.html` avec prévisualisation locale.
- **148 tests** au HEAD exact, CI [#40625550297](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40625550297) et [#40625555508](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40625555508) **SUCCESS**. Échecs intermédiaires corrigés (budget P1 et champs source de campagne).
- **Statuts PARTIELS** : mandat P1/P2 déclaratif non authentifié ; échantillons DNS/IP précontrôlés sans résolution/connections ; partitions de campagnes non exécutées ; document HTML et frontend statique non déployés. Aucune vulnérabilité confirmée, aucun patch ni admission réseau.
- **PR #3 S1 encore au HEAD `686e68980c5807ca84bcdf4ef1e8a2f046fe09f8`** : la synchronisation a été bloquée par l'outil et **n'a pas été réalisée**. Ses anciens tests ne couvrent pas cette tranche. La maquette statique de la seconde interface n'a pas pu être créée.
- FastAPI, PostgreSQL, Redis, workers, crawler autorisé, vraie vérification DNS de connexion, RBAC, PDF, sandbox, PHPPATCH, déploiement S1 et revue indépendante restent **non terminés**. Les 61 work packages, 32 exigences, six lots, cinq versions, deux sous-domaines S1 et `P2S-NEXT-001` demeurent intacts.


## Actualisation datée — construction des deux prototypes locaux (28/10/2026, après checkpoint #019)

- Dernier HEAD **PR #2** de cette tranche : `daeca8bff5b776f497e7323e0ab92041b895347a`, 153 tests et deux CI SUCCESS (#40627849277, #40627853683). Deux prototypes statiques distincts `web/php2shell/index.html` et `web/phppatch/index.html` sont désormais sur la branche V0.2, **sans backend ni connexion** ; les boutons d'audit/patch restent inactifs.
- Dernier HEAD **PR #3** : `a7d62aae30908533409cf7931f248ab2ae1a489b` ; merge non forcé à deux parents, trois fichiers S1 conservés, quatre CI SUCCESS (#40627886714, #40627886718, #40627892087, #40627892033). La divergence PR #2/#3 du checkpoint #019 est résolue à ce HEAD.
- **PR #1** `c17f0931db2cae659e4301585b0bf3db9078ca09`, `main` `a9d799b008fc65ed5745745bc4ef09e8b889aabe` inchangés pendant cette tranche ; PR #6 en cours de documentation. Reviewer `Patricked-code` demandé sur #1/#6, aucune revue indépendante APPROVED au contrôle.
- Les deux domaines S1 demeurent des destinations **non déployées applicativement** selon la dernière preuve historique. Aucune sonde S1 nouvelle, aucun scan tiers, aucun mandat P2 authentifié ni claim runtime MCP attesté. Les CI ne prouvent que les tests des branches.
- **P2S-NEXT-001** demeure la revue indépendante PR #6 puis #1 ; aucune étape de déploiement ni de patch déclarée DONE.

## Actualisation — précontrôle de périmètre hors ligne (P2S-EVT-028, 2026-10-28)

- PR #2 `fa1332b0d48c9147ce03f48ba3b3783fe623f3c4` : hostname DNS strict, classification conservatrice des IPv6 de transition, garde-fou optionnel de sous-chemin pour redirections simulées ; **157 tests**, CI [#40633403515](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633403515) / [#40633408996](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633408996) SUCCESS.
- PR #3 `11edd0e4b4ca30931d425f26f37ce91e3ee83e42` : intégration par merge à deux parents, `force=false`, trois fichiers propres à S1 préservés ; 4 CI [#40633467853](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633467853), [#40633467926](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633467926), [#40633472052](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633472052), [#40633472066](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633472066) SUCCESS. Comparaison PR #2→PR #3 : behind=0, uniquement 3 fichiers S1.
- PR #1 `c17f0931db2cae659e4301585b0bf3db9078ca09` et `main` `a9d799b008fc65ed5745745bc4ef09e8b889aabe` observés inchangés avant cette construction ; revue `Patricked-code` demandée sur PR #1/#6, aucune APPROVED indépendante à l'observation.
- Aucune sonde S1 ni opération réseau externe, aucune approbation P1/P2 authentifiée, aucun claim serveur MCP, aucun patch ou déploiement. Le résultat ne vaut **pas** admission de scan, protection SSRF d'un worker ou qualification de vulnérabilité d'actif. Les cinq versions, six lots, 32 exigences, 61 work packages, deux consoles/moteur commun et deux destinations S1 restent au programme.

## Jalon API et proposition de diff local (checkpoint #022, 28/10/2026)

- **PR #2 V0.2/V0.3 préparatoire HEAD `ac0b35588c950d675fe89c70fbc8d434c0594d20`** : `service/local_api.py` (FastAPI 0.162.0, client de test HTTPX 0.28.1), `api_tests/test_local_api.py`, `.github/workflows/api-contract.yml`, `requirements-api-contract.txt`, `docs/V0_2_LOCAL_API_CONTRACT.md`. API de contrat **locale, non démarrée ni déployée** : health/capabilities et prévisualisation URL non exécutante. `P2S_ENABLE_LOCAL_API_PREVIEW=1` reste un **interrupteur de développement**, pas une autorisation ; adresse loopback exigée, P2 refusé, aucune route scan/patch, pas d'OpenAPI exposé. **9 tests ASGI en mémoire**, aucune connexion externe.
- **Première tranche V0.3 préparatoire** : `app/patch_preview.py`, `tests/test_patch_preview.py`, `docs/V0_3_LOCAL_PATCH_PREVIEW.md`, commande `propose-config-patch`. À partir d'un constat PHP2SHELL valide, génère une **proposition de diff php.ini à contexte nul**, sans exporter les valeurs voisines ; `files_modified=0`, `patch_applied=false`, `mandate_verified=false`, `independent_approval_received=false`, `ready_for_production=false`. Aucun correctif des CVE prioritaires.
- **Preuves PR #2** : `164` tests Python existants et `9` tests API, CI [#40634400144](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40634400144) / [#40634400187](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40634400187) **SUCCESS** au HEAD exact. Échecs intermédiaires de contrat d'API et commande CLI corrigés avant validation ; tests historiques conservés.
- **PR #3 HEAD `6fd0cd9aa5cf3be2e47f779e4ba1d167df35ffd0`** : synchronisée par merges gouvernés à deux parents, ref `force=false`, fichiers historiques propres à S1 conservés, **6 CI tests/API/préflight en lecture seule SUCCESS** (#40634497746/#40634497718/#40634497818/#40634502515/#40634502522/#40634502549). Aucune installation ni écriture S1/Plesk.
- La vraie authentification P1/P2, l'API publique sécurisée, PostgreSQL/Redis/workers, le crawler anti-SSRF connecté, PDF, sandbox Docker et diffs généralisés PHPPATCH, PR corrective et rollback sont toujours **NON LIVRÉS**. Référence de gouvernance P2S-NEXT-001 inchangée ; aucun accès S1 ni mandat runtime prétendu.


## Actualisation additive — sécurité des corps ASGI et convergence (#023 en préparation, 2026-10-28 UTC)

- **PR #2** HEAD `227915fda5379200232ec6a2a968351512fb9153` : ajout de trois tests négatifs/compatibilité ASGI ; vérification des octets réels des requêtes POST/PUT/PATCH indépendamment de Content-Length via middleware dédiée bornée à **4096 octets**. Aucun changement des contrats GET/URL ou des outils CLI existants ; aucune API de scan ni autorisation P2 ajoutée. Tests RED commit `b231bd7f4e7874c24cef75e06bb550cfcc706d83` (API CI failure attendue), puis GREEN commit `10ca05ed21295a7c4e8364d642eabc0f83addac2` et documentation commit `227915fda5379200232ec6a2a968351512fb9153`.
- **Tests au HEAD final PR #2** : 164 historiques et **12 API**, CI [#40635830633](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635830633) / [#40635830627](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635830627) SUCCESS (push et PR également verts). Pas de scanner réel, pas de processus serveur écoutant sur interface, ni TLS/HTTP E2E production testé.
- **PR #3** HEAD `fdc1e87c009eca22a294cc1bfe4b558648df9b77`, merge à deux parents (ancien PR #3 + nouveau PR #2), `expected_sha`, `force=false` ; comparaison PR #2→#3 : `behind=0` et seuls les 3 fichiers propres à S1. Six CI au HEAD SUCCESS : #40635887703/#40635887789/#40635887800/#40635894041/#40635894059/#40635894060 ; logs : **164 tests CLI et 12 tests API**.
- **GitHub main** `a9d799b008fc65ed5745745bc4ef09e8b889aabe` et PR #1 `c17f0931db2cae659e4301585b0bf3db9078ca09` inchangées à la réconciliation de départ. PR #6 documentaire à valider de nouveau après le commit présent. Revues PR #1/#6 : COMMENTED automatisées uniquement, aucune APPROVED indépendante.
- **Aucun service S1 déployé**, aucun mandat authentifié P1/P2 ni claim runtime MCP vérifié, aucun code PHP distant exécuté, aucun patch appliqué. La CI de readiness S1 prouve uniquement les précontrôles CI ; aucune sonde S1 fraîche durant cette tranche. L'automatisation horaire existante `6ae13640aa9c8191b20d3d120bf71ace` est restée ENABLED au contrôle.
- **P2S-NEXT-001 inchangée** : revue indépendante PR #6 puis #1 ; sous-tranche API n'est pas un accomplissement de l'exigence d'API authentifiée ou du déploiement V1.0. Six lots, 32 exigences, 61 packages et cinq versions conservés.

## Actualisation additive PHPPATCH — P2S-EVT-032 (28/10/2026 UTC)

- **PR #2 HEAD `6a41ef5c15ef78af95afa0aeda3561fd5c33dd8c`** : le candidat de diff `display_errors` refuse maintenant plusieurs affectations actives dans le même php.ini/.user.ini ; commentaires inactifs et indentation par tabulation conservent leur fonctionnement. Deux tests ajoutés, **166 tests historiques + 12 API** au HEAD final, CI #40636274298/#40636274251/#40636281308/#40636281249 **SUCCESS**. Contrôle RED du test seul `c78c10d60e0c38e154376e1f39315fa6a8b955a0` : CI #40636177514/#40636184215 FAILURE ; correction `ffc68374acd2dd640c565a00752a39a018b6acaf`, compatibilité tabulations `96269838bfc97d770f0850328dc7249f6c5b6550`, documentation `6a41ef5c15ef78af95afa0aeda3561fd5c33dd8c`.
- **PR #3 HEAD `3bccdf0b4d776ba399621debbdc48488685e5eb6`** : merge à deux parents, `force=false`, `expected_sha`, trois fichiers S1 historiques préservés. CI push/PR tests, api-contract et S1-readiness en lecture seule **6/6 SUCCESS** (#40636321289/#40636321381/#40636321405/#40636326105/#40636326106/#40636326111) ; journal du job unit PR #40636326106 : **Ran 166 tests**. Préflight S1 ≠ application exécutée.
- Statuts : le diff reste **une proposition locale NON APPLIQUÉE** ; aucun runtime PHP effectif/SAPI/backport ni mandat P2, scan actif, patch en sandbox, approbation humaine, rollback ou production S1 attesté. L'API demeure locale sans authentification réelle. Aucun changement de `main` ou de PR #1 autorisé/rapporté ; les revues indépendantes PR #6/#1 restent à obtenir. Priorité `P2S-NEXT-001` inchangée.


## P2S-EVT-033 — contrat P1/P2 deny-by-default (2026-10-28 UTC)

- PR #2 `2e270c92048ee9725d9d3b3cba3d2d6ec10d2b97` : extension du préflight existant par `evaluate_action_gates`. Cinq opérations `public_crawl`, `source_read`, `patch_propose`, `patch_apply`, `deploy` portent des exigences d'autorité distinctes ; **toutes DENY** en l'absence de vérificateur réel. Cinq tests supplémentaires, 171 tests historiques et 12 API, CI RED #40636921508, puis GREEN #40636985499/#40636985489 au HEAD.
- PR #3 `2da277bbdb0784f2fe73f69ac0db7b96407a7a71` : merge non forcé, 3 fichiers S1 préservés, 6 CI SUCCESS (#40637036489/#40637036497/#40637036500/#40637042972/#40637042983/#40637043035), behind=0. Aucun déploiement.
- MCP WealthTech interrogé **en lecture seule** (ping + réconciliation + inventaire, 2026-10-28 05:17 UTC) : connexion répond et domaines S1 présents, mais **aucun vérificateur scoped PHP2SHELL P1/P2 opérationnel n'est attesté**. Pas de faux jeton/session, claim ou approbation. Le socle demeure préparatoire, jamais un droit d'exécution.
- `main` et PR #1 n'ont pas été modifiées. `P2S-NEXT-001` demeure la vraie revue indépendante PR #6 puis #1. 61 work packages, 32 exigences, 6 lots et 5 versions inchangés.


## P2S-EVT-034 — vérificateur d'attestations externes Ed25519 (2026-10-28 UTC)

- PR #2 HEAD `cb705a82e5a2d0c2bf7193139873b7e7fc210706` : nouveaux `app/signed_attestation.py`, `auth_tests/test_signed_attestation.py`, `requirements-auth-contract.txt`, `.github/workflows/auth-contract.yml`, `docs/V0_2_SIGNED_ATTESTATION_CONTRACT.md`. Vérification **réelle** et hors ligne d'un JWS Ed25519 signé par **une clé de test éphémère** : émetteur et audience attendus, signature, `kid` autorisé, subject/project/asset/action/scope, fenêtres iat/nbf/exp au plus 300 s, révocation fournie par le serveur. Aucune clé privée conservée ni code émetteur de jeton.
- RED workflow auth [#40638089308](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638089308) FAILURE attendu sans module, GREEN [#40638158899](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638158899) SUCCESS (**10 nouveaux tests**). Tests historiques **171** et tests API **12** restent verts au HEAD via #40638163772/#40638163637. Dépendance `cryptography==46.0.3` isolée, sans modifier CI historiques.
- **Toute attestation correcte produit uniquement `VERIFIED_ATTESTATION_NOT_EXECUTION_ADMISSION`** et `authorized=false`, `execution_enabled=false`, `mcp_claim_verified=false`, `user_session_authenticated=false`. Ce module ne connaît aucun IdP/issuer MCP réel ; aucune prise en charge P1/P2 live, scan, patch, déploiement ni nouvelle autorité n'est démontrée.
- PR #3 HEAD `c22ac964e1cbb71d880e8ef828cf7bd96d485960` : convergence de PR #2 avec trois fichiers S1 inchangés, merge à deux parents, force=false, expected SHA, comparaison derrière=0. Les CI au HEAD seront reportées séparément.
- Toutes les données canoniques existantes, 32 REQ, 61 WP, 6 lots, cinq versions V0.1→V1.0 et P2S-NEXT-001 restent préservées.


## P2S-EVT-035 / P2S-EVT-036 — bornage signé au sous-chemin et budgets P1 (2026-10-28 UTC)

- **PR #2 `53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf`**, 2 tranches RED→GREEN sur `app/signed_attestation.py` / `auth_tests/test_signed_attestation.py`. Cinq tests `base_path` plus cinq tests budgets ; **20 tests auth** nouveaux cumulés, 171 historiques + 12 API inchangés. Six CI au HEAD PR #2 SUCCESS (tests / auth / API, push et PR).
- Une attestation avec `base_path` doit être liée exactement au sous-chemin demandé ; la présence d'un seul côté ou les chemins non canoniques sont refusés. Les anciennes attestations hors ligne non liées au chemin sont conservées uniquement comme vérification cryptographique non exécutable.
- Pour `public_crawl` (P1), `base_path` + plafond de pages + plafond de débit **signés** désormais obligatoires. Les valeurs proposées doivent rester ≤ aux plafonds signés et aux limites absolues (100 pages, 30 requêtes par minute). Aucun budget ne déclenche de crawl ; `authorized=false`, `execution_enabled=false`, `mcp_claim_verified=false`.
- **PR #3 `d48f88039e1faeea1246847a982e59bda4e63e5a`** : synchronisation sans force et vérification des trois fichiers readiness S1 conservés. Aucun serveur modifié.
- **Non acquis :** fournisseur d'identité ou d'attestations réel, clés approuvées et revocation live, session utilisateur, ACL projet, mandats/claims MCP scoped PHP2SHELL, protections DNS/worker runtime, approbations et service Web. Statuts de work packages non avancés artificiellement ; `P2S-NEXT-001` reste la revue indépendante PR #6 puis PR #1.

## P2S-EVT-037 — revue locale de cohérence Composer (2026-10-28 UTC)

- **PR #2 HEAD `7f6ae451c1129d0b6a1a0c103f2f91659d26e55b`** : trois fichiers additifs `app/composer_consistency.py`, `tests/test_composer_consistency.py` et `docs/V0_2_COMPOSER_CONSISTENCY.md`. Commande indépendante `python -m app.composer_consistency --path <projet-local-autorise>`. **17 tests nouveaux**, **188 tests historiques au total**, 12 tests API et 20 tests Ed25519 auth inchangés. CI PR #2 exact SHA : tests #40639429710/#40639432662, API #40639429683/#40639432597, auth #40639429745/#40639432767 **6 SUCCESS**. Journal tests #40639429710 : `Ran 188 tests ... OK`.
- **PR #3 HEAD `8a5ba2dee04a93a07a99229b254159c76673b439`** : merge à deux parents (ancien `d48f880` + PR #2 `7f6ae451`), `expected_sha` et `force=false`. Arbre = PR #2 + **exactement** trois blobs S1 inchangés, comparaison `behind=0`. Huit CI tests/API/auth/S1-readiness push+PR SUCCESS : #40639482247/#40639482267/#40639482157/#40639482174/#40639489693/#40639489694/#40639489782/#40639489633. Job unit PR #40639489694 : `Ran 188 tests ... OK`.
- **REQ-008 / P2S-WF-E07 et P2S-WF-Q01 PARTIELS** : détection de cohérence des métadonnées déclarées, sans résolution Composer complète, ni preuve d'installation, ni attestation PHP/SAPI, ni analyse d'un actif distant. Le code ne lit que des fichiers locaux autorisés et n'ouvre aucun socket. Le module n'est pas relié au dossier d'audit ni au frontend et ne change pas les commandes CLI existantes.
- Revue réellement indépendante PR #6 puis PR #1 toujours **NON APPROVED** à la dernière observation. MCP ping/réconciliation/inventaire en lecture seule : les deux sous-domaines S1 figurent dans l'inventaire, mais aucun claim/mandat PHP2SHELL scoped, IdP/ACL de production, admission P1/P2, crawler connecté, patch actif ou déploiement n'a été attesté.
- **Programme intégral préservé** : V0.1→V0.2→V0.3→V0.4→V1.0, 6 lots, 32 REQ, 61 work packages, URL→audit explicitement autorisé→diagnostic sourcé→PHPPATCH, moteur partagé, Docker isolé, destinations `php2shell.wealthtechinnovations.com` et `phppatch.wealthtechinnovations.com`. Aucun write `main` ni S1, aucune nouvelle automation ou gateway. Priorité `P2S-NEXT-001` inchangée.


## P2S-EVT-038 — raccordement attestations externes à l'intake URL (2026-10-28)

- PR #2 HEAD `a14968d1aa4ff842cfd025b118c5ce90d60c55aa` : nouveau `app/scoped_attestation_preflight.py`, ajout de l'option d'égalité exacte de `mandate_id` dans le vérificateur Ed25519 existant, `auth_tests/test_scoped_attestation_preflight.py` (8 tests), docs enrichies. Construction **RED→GREEN** : refus avant implémentation CI auth #40640364068, puis GREEN #40640438069.
- Compatibilité du programme : **188 tests historiques + 12 API + 28 auth** ; six CI push/PR PR #2 au HEAD exact SUCCESS ; PR #3 HEAD `f87eb7e1ecc41f21611aadd5c3029ac6e16f313e`, trois seuls fichiers S1 exclusifs préservés, huit CI exact SHA SUCCESS.
- La preuve signée doit être liée au hostname, sous-chemin normalisé, action/scope, budgets P1, identité/projet attendus et, pour P2, à la référence de mandat exacte. Les tests vérifient les refus. **Aucune autorisation** : `authorized=false`, `execution_enabled=false`, `user_session_authenticated=false`, `project_acl_verified=false`, `mcp_claim_verified=false`.
- MCP réconciliation/inventaire du 28/10 ~05:49 UTC, runtime/S1 healthy et domaines PHP2SHELL/PHPPATCH inventoriés, **aucune capacité exposée de vérification de mandat utilisateur P1/P2 PHP2SHELL**. Les identités OAuth d'agents MCP ne sont pas des sessions utilisateurs PHP2SHELL. Manquent IdP validé, ACL projet et actif, mandat et délégation émis par autorité approuvée, clés publiques/rotation et révocation live, claims runtime, approbations, worker réseau et déploiement.
- Aucun nouvel IdP, gateway, Bus, autorité, repo, PR ou automation ; pas de fusion main ni d'opération S1. **P2S-NEXT-001** reste la revue indépendante PR #6, puis PR #1.


## P2S-EVT-039 — simplicité pour tous, sécurité interne (28/10/2026)

- **Instruction utilisateur nouvelle :** « ça doit être simple pour permettre à n'importe qui de l'utiliser ». Les labels P1/P2/mandats/claims MCP ne doivent pas être imposés aux débutants ; une seule connexion à terme pour PHP2SHELL et PHPPATCH, vérifications de droits et mandats en backend, non pas en formulaires manuels. L'invité doit pouvoir comprendre et prévisualiser sans inscription.
- **Travail GitHub réel :** PR #2 `69cbbc6b13a08d2ce845754d2e9156edc018510d` modifie seulement la présentation de `web/php2shell/index.html`, le texte local du script `web/shared/url-preview.js` et `web/README.md` ; ajoute 2 tests dans `tests/test_frontend_static.py` : novice en 3 étapes, labels compréhensibles, paramètres avancés, aucun faux login/réseau/crawl. 6/6 CI au SHA SUCCESS ; 190 tests historiques cumulés, 12 API et 28 auth.
- **PR #3 `97808da8783abb9625d7aa2b5efdfe7316cba998`** : synchronisée non forcée sans perdre les trois fichiers S1 ; 8/8 CI exact SHA tests/API/auth/S1-readiness SUCCESS.
- **Non réalisé :** aucune connexion réelle, aucun vérificateur d'autorisation P1/P2 live, aucun crawler, aucun rapport de diagnostic réel depuis l'interface, aucun correctif et aucun déploiement. La prévisualisation accessible sans compte ne donne pas droit d'audit sur des sites tiers. Les 32 exigences, 61 work packages, 6 lots et cinq versions ne sont pas reclassés.


## P2S-EVT-040 — première tranche exécutable de réponse courte anonyme (2026-10-28)

- **PR #2 HEAD `dc2a61d900eb8387470b993f0cab02e58123725d`** : `app/public_summary.py` calcule une synthèse courte et bornée à partir d'éléments publics **fournis et non authentifiés** ; sans éléments, retourne honnêtement `NOT_ANALYZED`. Refuse injection de statut, d'accès privé, de propriétés non conformes et de valeurs d'en-têtes. Ne traite que noms d'en-têtes autorisés et statut HTTP déclaré. Aucun CVE, score, vulnérabilité confirmée, réponse complète sauvegardée, accès réseau ou code source.
- **API locale** `POST /api/v0.2/guest/summary` dans `service/local_api.py` : `P2S_ENABLE_LOCAL_GUEST_SUMMARY=1` et client loopback obligatoire, sinon 403 ; 422 générique pour entrée rejetée ; réutilise cache no-store, corps 4 KiB et TrustedHost. **Non exposée au public / non déployée**.
- **Tests RED→GREEN** : 9 tests pour `app/public_summary.py`, 5 tests API ; CI au HEAD PR #2 **6/6 SUCCESS**. PR #3 HEAD `ddc8871c064ef41c4966302ce516527c05d443e0` synchronisée à deux parents, trois fichiers S1 originaux conservés, **8/8 CI exact HEAD SUCCESS**. Totaux : **199 tests historiques**, **17 tests API**, **28 tests auth**.
- **Aucune confusion admise** : l'utilisateur final ne peut **pas encore** cliquer sur « Analyser » et obtenir une véritable mesure du site ; il faut un collecteur P1 réseau admis et prouvé, ensuite une vraie authentification et un stockage privé. Les trois niveaux définis dans [P2S-UX-002](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5#issuecomment-6462119529) sont une cible de construction, pas un état runtime.
- `main` non modifiée ; 32 exigences, 61 work packages, 6 lots, cinq versions et deux consoles maintenus. Pas de serveur S1, de fusion, de domaine modifié, de nouvel outil d'identité ni de tâche parallèle.
