# REQUIREMENTS_TRACEABILITY — matrice d'exhaustivité et non-régression

**Continuity ID :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Ancre :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5  
**Source normative des objectifs fondateurs :** `continuity/FOUNDING_SPECIFICATION.md`.  
**Sources d'implémentation :** dépôts/branches/commits réels, jamais une simple phrase d'intention.

Ce registre traduit **le programme initial (six lots) + son évolution (cinq versions, deux domaines S1)** en critères vérifiables. Il complète `docs/ROADMAP.md` de la PR #2 sans y supprimer ni renuméroter les étapes.

## Matrice des capacités de la plateforme

| Exigence | Origine / lot initial | Version(s) cible(s) | État daté 27/10/2026 | Acceptation future et preuve attendue |
| --- | --- | --- | --- | --- |
| **REQ-001** imports CSV/JSON/TXT | Inventaire / L2 | V0.2/V1.0 | **Partiel** : JSON déclaré CLI V0.1 ; CSV/TXT/campagnes non implémentés | Import des 3 formats, normalisation par DNS-label, déduplication, rejets et pagination testés |
| **REQ-002** centaines/milliers cibles | Inventaire/campagnes / L2 | V0.2/V1.0 | **Partiel** : `preview-url` et `plan-campaign` hors ligne, déduplication et partitions stables (1000 cibles testées, au plus 10 000 admises au plan) ; ni job créé, ni campagne exécutée, ni base/worker, quotas persistants ou reprise réelle | Campagne testée à volume élevé avec budgets, limites, retries, reprise et preuves, sans requête non autorisée |
| **REQ-003** double niveau d'autorisation | Exigence fondatrice / L1-L2 | Toutes | **Partiel** : modes P1/P2 et précontrôle local des domaines, dates, scopes et budgets ; toutes les attestations d'identité, signature, autorité et droits restent `false`, aucune admission MCP réelle | Autorité, date/fin/portée et permissions admises ; refus hors périmètre et tests négatifs |
| **REQ-004** identification PHP passive et framework | Passive Audit / L2 | V0.2 | Non implémenté | Indices publics non intrusifs avec sources et confiance, redirections validées, taux bornés, absence de faux diagnostic |
| **REQ-005** catalogue officiel CVE sourcé | CVE Intelligence / L3 | V0.2 | **Partiel** : instantané CVE PHP/CERT-FR sourcé, audit âge/SHA-256, comparateur hors ligne et **client HTTP GitHub explicitement opt-in** à allowlist de GHSA pré-admis, TLS/redirections/taille/identité vérifiés ; 81 tests PR #2. Un client testable **ne prouve pas une acquisition réseau réelle, une ingestion périodique, une signature upstream, ni le suivi fournisseurs/backports**. | Provenance datée + avis upstream/fournisseur, branche, score, backport, tests de divergence |
| **REQ-006** version runtime réelle / SAPI | CVE/runtime / L3 | V0.2/V0.3 | **Partiel** : comparaison semver sourcée + enveloppe JSON déclarative du runtime/SAPI (`review-runtime-evidence`, PR #2, 89 tests) ; preuve de mandat, capture signée, runtime HTTP effectif et backports **NON attestés** | Collecte sous mandat de PHP réellement exécuté, paquets, config, SAPI, extension et état patched |
| **REQ-007** analyse fichiers PHP / AST | Source Review / L4 | V0.2 | **Partiel** : scanner lexical local PR #2 | AST, faux positifs négatifs mesurés, chemin/ligne/preuve, limites documentées |
| **REQ-008** Composer et configs | Source Review / L4 | V0.2 | **Partiel** : `composer.json`/`composer.lock`, `php.ini`/`.user.ini` et certaines configurations PHP-FPM lus **hors ligne** sur PR #2 ; pas de runtime/SAPI effectif ni de configuration webserver complète | Lockfile, dépendances installées, php.ini/FPM/webserver analysés depuis sources autorisées |
| **REQ-009** preuves et niveaux de confiance | CVE/rapport / L3-L4 | V0.2/V1.0 | **Partiel** : indice lexical, `review_required`, sans qualification d'applicabilité | Evidence ID, source, ligne, dates, classification et incertitude, rapport révisable |
| **REQ-010** proposition de patch runtime/code/config | Patch Generator / L4 | V0.3 | Non implémenté | Diff minimal, justification, compatibilité, PR candidate et version runtime corrigée si nécessaire |
| **REQ-011** tests patch avant/après | Validation / L5 | V0.3 | Non implémenté (tests de la CLI seulement) | CI/lint/intégration/non-régression sur copie isolée autorisée, résultats signés |
| **REQ-012** rollback/sauvegarde | Validation / L5-L6 | V0.3/V0.4 | Procédure documentée, pas prouvée en exécution | Rollback en labo et en staging approuvé, checkpoint de restauration |
| **REQ-013** Python/FastAPI API commune | Plateforme / L1 | V0.4/V1.0 | **Partiel préparatoire** : API FastAPI locale (GET health/capabilities, POST preview URL désactivé par défaut), 12 tests ASGI et limite réelle de 4096 octets ; **aucun utilisateur authentifié, RBAC, P1/P2 vérifié, PostgreSQL, Redis, worker ni API de production** | API authentifiée, tests permissions, OpenAPI/contrats, isolation des consoles |
| **REQ-014** PostgreSQL / artefacts | Control Plane/Store / L1 | V0.4/V1.0 | Non implémenté | Stockage privé des campagnes et preuves, migrations, RBAC, sauvegardes, rétention |
| **REQ-015** Redis & workers bornés | Orchestration / L1-L2 | V0.4/V1.0 | Non implémenté | File robuste, anti-doublons, annulation/retry contrôlés ; ne pas concurrencer l'autorité MCP |
| **REQ-016** Docker et lab isolé | L1/L5 | V0.3/V0.4 | Prototype Docker CLI/lab présent ; prod non implémentée | Conteneurs non-root, pas de secrets, réseau/volumes/CPU/mémoire restreints, essais reproductibles |
| **REQ-017** GitHub App/MCP existant/S1 | Déploiement / L6 | V0.4 | Plesk/DNS/TLS/préflight PR #3 ; application non déployée | Autorisation, claim/lock, exact SHA, CI revue, staging, E2E, rollback attestés |
| **REQ-018** double console Web | Supervision / L6 | V1.0 | Deux DNS/vhosts S1, interfaces non implémentées | PHP2SHELL analyse + PHPPATCH remédiation, même moteur, tests RBAC négatifs |
| **REQ-019** PDF/CSV/JSON + Git PR | Sorties / L6 | V0.2/V0.3/V1.0 | **Partiel** : JSON/CSV/Markdown/HTML existants ; **prototype FastAPI local contractuel** et **diff candidat minimal php.ini non appliqué** (164 tests historiques + 9 API). PDF, API authentifiée, diagnostic confirmé, vraies PR de correctif et déploiement NON livrés | Exports cohérents, tests d'absence de secrets, résultats traçables à une campagne |
| **REQ-020** audit durable + reprise conversation | Gouvernance transversale | Toutes | Issue #5 + PR #6 documentaire avec CI ; non fusionnée | Dernier checkpoint exact, registres append-only, actions et preuves relues en nouvelle conversation |
| **REQ-021** simulation `portail-demo.example` PHP 8.3.34 | Lab historique / L5 | V0.2/V0.3 | Scénario défini, aucun test runtime 8.3.34 spécifiquement prouvé | Build image réellement épinglée 8.3.34, analyse uniquement labo, proposition de mise à jour, compatibilité testée |
| **REQ-022** contrôle SSRF/redirections/concurrence | Collecte / L2 | V0.2/V0.4 | **Partiel (sans réseau)** : prévisualisation URL, classification de réponses A/AAAA fournies localement, refus des adresses non globales et redirections hors origine ; DNS réel, pair connecté, rebinding, robots et budgets runtime NON implémentés | Rejet loopback/privé/hors-scope, revalidation DNS après redirect, quotas, échecs et journaux |
| **REQ-023** URL unique saisie depuis le frontend | Extension explicite de CAP-01 / L2-L6 | V0.2/V1.0 | **Non implémenté** : pas de frontend ni d'API d'audit Web | Saisie URL, projet, type d'audit et mandat, validation et statut de campagne; refus de cible non admise |
| **REQ-024** découverte/crawl des pages autorisées | CAP-02 / L2 | V0.2/V1.0 | Non implémenté | Parcours sitemap, liens et pages accessibles **uniquement sous mandat**, quotas/profondeur/horodatages/couverture et limites affichés |
| **REQ-025** analyse des contenus et signaux Web | CAP-02 / L2 | V0.2 | Non implémenté | HTTP/HTML/JS public, headers, cookies, redirections, framework et PHP probable; preuves/confidence et aucune lecture PHP serveur déduite d'une URL |
| **REQ-026** audit approfondi après liaison P2 | CAP-04/CAP-05 / L4 | V0.2/V0.4 | Non implémenté | Dépôt Git exact SHA, source PHP, Composer, configs, runtime installé/SAPI et backports examinés **uniquement après autorisation vérifiée** |
| **REQ-027** diagnostic par page et preuve d'ampleur | CAP-02/CAP-03 / L2-L3 | V0.2/V1.0 | Non implémenté | Synthèse par URL/fichier/constat, horodatage, méthode, pages visitées/non découvertes et niveaux de confiance; ne pas affirmer « toutes les pages » |
| **REQ-028** panneau PHP2Shell CVE et statut par actif | CAP-03/CAP-05 / L3 | V0.2/V1.0 | Documents CVE présents, moteur d'applicabilité non implémenté | Source officielle vérifiée distincte de runtime réellement attesté; catégories insuffisant/potentiel/applicable/fournisseur corrigé |
| **REQ-029** document de remédiation Web→PDF/JSON/CSV | CAP-08/CAP-10 / L6 | V0.2/V1.0 | **Partiel préparatoire** : dossier d'audit local JSON/Markdown/HTML sourcé par indices, sans PDF ni vraie campagne Web, absence de verdict confirmé et d'attestation P2 | Dossier auditable avec périmètre, preuves, sévérité sourcée, incertitude, plan runtime/config/code, tests et rollback, sans secrets |
| **REQ-030** passage PHP2SHELL→PHPPATCH | CAP-06/CAP-07/CAP-10 / L4-L6 | V0.3/V1.0 | **Partiel préparatoire** : handoff PHP2SHELL→PHPPATCH hors ligne et diff de configuration `display_errors` candidate localement, aucun test sandbox, approbation, mandat, PR Git ou application | Finding/mandat transférés, patch candidat/diff, sandbox, test, approbation, PR, jamais déploiement automatique |
| **REQ-031** sécurité de navigation URL/SSRF | CAP-01/CAP-02 / L2 | V0.2/V0.4 | **Partiel (préflight hors ligne)** : validation URL, précontrôle de listes IP et redirections de même origine ; aucune connexion autorisée ni protection d'exécution DNS/rebinding/pair TLS, annulation, quotas et sessions implémentés | Refus credentials/IP internes/redirections hors scope/rebinding, budgets de requêtes et annulation ; tests négatifs et absence d'exploit |
| **REQ-032** recette bout en bout frontend/audit/rapport/patch | L5-L6 | V0.3/V0.4/V1.0 | Non implémenté | Fixtures fictives, permissions P1/P2, scans arrêtables, rapports vérifiables, patch/CI/rollback en lab, auth/RBAC et tests E2E S1 |


**Principe de comptabilité :** `Partiel` signifie qu'une sous-capacité est prouvée, pas que la capacité est complète. `Références vérifiées documentalement` signifie que les avis existent, **pas** que le runtime d'un site est affecté.

## Extension URL→audit→remédiation — 27/10/2026

Le mandat **saisie URL frontend, crawl Web borné, analyse approfondie P2, diagnostic CVE et document de remédiation avec patch séparé** complète les REQ-001→022 par **REQ-023→032**. Spécification détaillée : [\`URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md\`](URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md). Les dix nouvelles exigences restent non implémentées. Elles ne déplacent ni la prochaine action ni les jalons V0.1→V1.0.

## Deux classifications complémentaires

- **Versions de produit** : V0.1 fondations ; V0.2 analyse/code/dépendances/config/CVE/campagnes passives ; V0.3 patches/tests/rollback ; V0.4 MCP/S1/Docker ; V1.0 Web/gestion/projets/rapports.
- **Lots initiaux** : L1 socle API/Docker/base/gouvernance ; L2 campagnes/détection passive ; L3 CVE/versions/preuves ; L4 source/patch ; L5 lab/tests ; L6 console/rapports/déploiement.

**Aucune disparition de L1 (FastAPI/PostgreSQL/Redis/workers) sous prétexte que V0.1 actuelle est une CLI** : le livrable L1 reste à compléter dans V0.4/V1.0. L'ordre peut être planifié par dépendances techniques, sans renommer les exigences ni prétendre qu'elles sont déjà implémentées.

## Liens vers les travaux candidats — pas de déclaration d'exécution

Les **32 exigences** ont été reliées au backlog [`WORK_PACKAGES.json`](WORK_PACKAGES.json) (61 work packages, 8 lanes, dépendances et portes de contrôle) et au contrat [`INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md`](INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md). La couverture est **une planification**, pas une preuve d'implémentation : les statuts des exigences dans la matrice restent inchangés tant qu'une PR, une CI au SHA exact et les preuves d'acceptation n'attestent pas le livrable.

## Dépendances et evidence anchoring

- Références initiales : PR #1 `https://github.com/chainsolutions-wealthtech/Php2shell/pull/1`
- Analyse PHP : PR #2 `https://github.com/chainsolutions-wealthtech/Php2shell/pull/2`
- S1 et Docker : PR #3 `https://github.com/chainsolutions-wealthtech/Php2shell/pull/3` + issue #4
- Mémoire/transmission : PR #6 + issue #5 (point canonique)
- Sources PHP/CERT : `continuity/CVE_SOURCE_REGISTER.md`

## Politique d'évolution

Toute nouvelle fonctionnalité doit :
1. se rattacher à **REQ-nnn** existante ou recevoir un nouvel identifiant ;
2. indiquer PR, HEAD, CI et justificatif d'autorisation ;
3. conserver la couverture des scénarios existants et des versions ;
4. faire évoluer la ligne d'état seulement après preuve ;
5. publier un checkpoint dans l'issue #5 pour les jalons importants.

**Pas de modification ni de scan de sites gouvernementaux/bancaires ou de tiers sans mandat opérationnel explicite.**


## Preuve additive V0.2 — handoff PHP2SHELL→PHPPATCH (P2S-EVT-025, 28/10/2026)

- **REQ-029 / P2S-WF-E12 (PARTIEL)** : dossier JSON/Markdown antérieur conservé ; le nouveau contrat local `app/dossier_handoff.py` prépare une file de revue whitelist, **pas** un rapport Web/PDF ni une attestation de sécurité.
- **REQ-030 / P2S-WF-R06 (PARTIEL PRÉPARATOIRE SEULEMENT)** : transfert hors ligne d'identifiants de preuves et de règles indicatives, refus de promouvoir vulnérabilité, mandat, signature, approbation, patch ou production. Aucun diff, aucune sandbox, aucune PR de correctif ni rollback ne sont livrés.
- **REQ-020/032 / P2S-WF-Q01 (PARTIEL)** : neuf tests négatifs supplémentaires, **122 tests** au HEAD PR #2 `fc277eb8b8f1a277a606826e48bbf673028f8449` avec CI #40622112932/#40622118348 SUCCESS ; PR #3 `686e68980c5807ca84bcdf4ef1e8a2f046fe09f8` avec 4 CI SUCCESS.
- Ce jalon ne modifie **aucune** des 32 exigences ni leurs critères d'acceptation ; le DAG de 61 work packages reste une planification, et les dépendances bloquantes ne sont pas réputées franchies. Aucune action S1, scan tiers, correction PHP ou nouvelle gouvernance.


## Preuve additive — deux prototypes statiques séparés (P2S-EVT-026/027, 28/10/2026)

- **REQ-023 / P2S-WF-U01 = PARTIEL** : formulaire URL PHP2SHELL local déjà existant, aucune vérification de mandat, DNS live, crawl ou API ; pas d'audit actif.
- **REQ-030 / P2S-WF-U05 = PARTIEL PRÉPARATOIRE** : nouvelle maquette `web/phppatch/index.html` **non connectée** à `app/dossier_handoff.py`, quatre actions désactivées, affichage des gates P2/runtime/CVE/diff/Docker/revue/rollback. Aucun correctif, aucune approbation, aucun transfert réel.
- **REQ-020/032 / P2S-WF-Q01 = PARTIEL** : cinq tests de sécurité statique ajoutés ; 153 tests au HEAD PR #2 `daeca8bff5b776f497e7323e0ab92041b895347a`, CI #40627849277/#40627853683 SUCCESS ; PR #3 synchronisée `a7d62aae30908533409cf7931f248ab2ae1a489b`, quatre CI SUCCESS.
- Aucun critère d'acceptation ni exigence n'est supprimé ou marqué DONE. **Les 32 exigences, 6 lots, 61 work packages, V0.1→V1.0 et moteur commun / deux destinations S1 sont préservés.**

## Preuve additive V0.2 — durcissement local DNS/redirections (P2S-EVT-028, 2026-10-28)

- **REQ-022 / REQ-031 / P2S-WF-S03 : PARTIEL / précontrôle seulement**. Validation syntaxique conservatrice des hostnames DNS, rejet des IP littérales et noms réservés, classification IPv6 transition, redirections simulées avec sous-chemin optionnel borné par segment. **Aucun** worker réseau, vérification DNS/TLS au moment de la connexion, autorisation de mandat, crawl ou test SSRF E2E.
- **REQ-020 / REQ-032 / P2S-WF-Q01 : PARTIEL**. Quatre tests négatifs supplémentaires ; 157 tests et CI [#40633403515](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633403515) / [#40633408996](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633408996) SUCCESS au HEAD PR #2 `fa1332b0d48c9147ce03f48ba3b3783fe623f3c4` ; PR #3 `11edd0e4b4ca30931d425f26f37ce91e3ee83e42` synchronisée, quatre CI SUCCESS. Aucune exigence ni dépendance n'est promue à DONE.
- Les 32 exigences, six lots historiques, 61 work packages et V0.1→V1.0 restent intégralement préservés, y compris le parcours URL→audit autorisé→diagnostic→PHPPATCH, les deux sous-domaines S1, Docker isolé, revue et rollback.


- **REQ-013 / P2S-WF-I02 : PARTIEL PRÉPARATOIRE, non admis comme version complète** (2026-10-28, P2S-EVT-031). Durcissement fail-closed du prototype local contre les corps HTTP fragmentés/sans `Content-Length` ; trois nouveaux tests (9→12 API), 164 tests historiques conservés, CI PR #2 [#40635830627](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635830627) / [#40635830633](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635830633) SUCCESS au SHA `227915fda5379200232ec6a2a968351512fb9153`. Les gates auth/P1-P2, gouvernance, projet, stockage, production restent non franchis.
- **REQ-020 / P2S-WF-Q01 : PARTIEL** : CI RED #40635733090 conservée, CI GREEN #40635830627, convergence PR #3 `fdc1e87c` validée (trois fichiers S1 exclusifs, six CI SUCCESS) ; aucun test de production ni scan réalisé. Ne pas promouvoir à DONE les work packages aux dépendances non acquises.

- **REQ-030 / P2S-WF-R06 : PARTIEL PRÉPARATOIRE** (P2S-EVT-032) : durcissement du diff local `display_errors` refusant les affectations actives multiples ; commentaires inactifs, indentation et non-écriture préservés. 166 tests historiques et 12 tests API sur PR #2 `6a41ef5c15ef78af95afa0aeda3561fd5c33dd8c` ; 6 CI vertes PR #3 `3bccdf0b4d776ba399621debbdc48488685e5eb6`. Il manque mandat/authentification, validation PHP SAPI, sandbox, approbation, PR corrective et rollback.
- **REQ-020 / REQ-032 / P2S-WF-Q01 : PARTIEL** : deux nouveaux tests RED→GREEN, CI #40636184215 (RED), #40636281308 (GREEN), CI PR #3 #40636326106 SUCCESS (166 tests). Pas de qualification E2E ni de production.


- **REQ-003 / P2S-WF-S01 PARTIEL, pas d'authentification réelle** (P2S-EVT-033) : `evaluate_action_gates` déclare les exigences séparées P1/P2, patch et déploiement, rejette l'élévation forgée et répond toujours `DENY_UNVERIFIED_AUTHORITY`. PR #2 `2e270c92048ee9725d9d3b3cba3d2d6ec10d2b97` ; 171 tests historiques, 12 API ; CI #40636985499/#40636985489 SUCCESS, RED #40636921508 conservée. **Non acquis :** vrai IdP, sessions, ACL, vérificateur de mandat/délégation, révocation, claims runtime, frontend authentifié et exécution.
- **REQ-013/020/032 PARTIELLES** : matrice fail-closed et tests négatifs validés ; PR #3 `2da277bbdb0784f2fe73f69ac0db7b96407a7a71` synchronisée, 6 CI SUCCESS, aucun worker ni API production ni domaine S1 déployé. Statuts des work packages non élevés.


- **REQ-003 / P2S-WF-S01 PARTIEL, preuve crypto hors ligne uniquement** — P2S-EVT-034 : vérification JWS Ed25519 stricte dans `app/signed_attestation.py` (PR #2 HEAD `cb705a82e5a2d0c2bf7193139873b7e7fc210706`) : signature externe, issuer/audience, subject/project/asset/action/scope, TTL court, checker révocation fail-closed ; **10 tests auth / CI #40638158899 SUCCESS**. Aucune connexion à une autorité MCP réelle, aucun droit P1/P2, toujours `authorized=false`. REQ-003 non achevée.
- **REQ-013 / REQ-020 / REQ-032 PARTIELLES** — 171 tests historiques, 12 API et 10 nouveaux tests auth, aucun endpoint d'auth, connexion OAuth ni API prod. PR #3 HEAD `c22ac964e1cbb71d880e8ef828cf7bd96d485960`, **8/8 CI** tests/API/auth/S1-readiness SUCCESS (#40638221952/#40638221955/#40638221974/#40638222001/#40638228958/#40638228960/#40638228979/#40638229699). PR #6 continuity documentaire uniquement.


- **REQ-003 / REQ-022 / REQ-031 / P2S-WF-S01 : PARTIELS** — P2S-EVT-035 : le vérificateur Ed25519 de la PR #2 contrôle désormais `base_path` signé et demandé, sans correspondance par préfixe implicite ; refuse chemins relatifs, traversal et omissions unilatérales. Cinq tests supplémentaires, RED auth #40638834360 → GREEN #40638887265 ; sans droit d'accès au site ni validation DNS/SSRF réelle.
- **REQ-003 / REQ-002 / REQ-022 / P2S-WF-S01 : PARTIELS** — P2S-EVT-036 : pour un futur `public_crawl`, **`base_path`, `max_pages` et `requests_per_minute` sont obligatoirement signés**, demande plafonnée ≤ 100 pages et ≤ 30 req/min et ≤ budget signé ; cinq tests supplémentaires, RED auth #40639055136 → GREEN #40639079768. Aucun crawler ni quotas persistants implémentés ; jamais d'autorisation `ALLOW`.
- **REQ-013 / REQ-020 / REQ-032 / P2S-WF-Q01 : PARTIELS** — PR #2 HEAD `53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf` : **171 tests CLI historiques + 12 tests API + 20 tests auth**, six CI au SHA SUCCESS. PR #3 HEAD `d48f88039e1faeea1246847a982e59bda4e63e5a` : huit CI au SHA exact SUCCESS (#40639157571/#40639157572/#40639157600/#40639157608/#40639163016/#40639163023/#40639163025/#40639163228), aucun serveur modifié.

## Preuve additive P2S-EVT-037 — REQ-008 / REQ-026 / REQ-032 (2026-10-28 UTC)

La PR #2 `7f6ae451c1129d0b6a1a0c103f2f91659d26e55b` ajoute `app/composer_consistency.py`, `tests/test_composer_consistency.py` (17 tests) et `docs/V0_2_COMPOSER_CONSISTENCY.md`. La revue **hors ligne** compare les dépendances directes de `composer.json` à `composer.lock`, détecte les doublons et divergences d'exact pin, traite les packages virtuels avec prudence, refuse les liens symboliques et les fichiers excessifs, et ne reflète pas les URL/secrets des métadonnées. `python -m unittest discover -s tests -v` : **188 tests SUCCESS** au HEAD, CI #40639429710/#40639432662 ; 12 API et 20 auth préexistants restent verts. PR #3 `8a5ba2dee04a93a07a99229b254159c76673b439`, huit CI SUCCESS, trois fichiers S1 inchangés.

**Classification maintenue PARTIELLE** : pas de résolution complète des contraintes Composer, pas de preuve d'installation réelle, pas d'AST PHP, pas d'autorisation P2 authentifiée, pas de connexion réseau, pas de diagnostic CVE applicable, pas de patch. La portée REQ-008/026/032 et le programme de 32 exigences demeurent intacts.


- **REQ-003 / REQ-013 / REQ-020 / REQ-031 / REQ-032 PARTIELLES (P2S-EVT-038)** : `app/scoped_attestation_preflight.py` lie strictement URL canonique et JWS Ed25519 aux identifiants et opérations attendus, et P2 à un `mandate_id` signé exact. 8 tests nouveaux (28 auth cumulés), RED #40640364068 → GREEN #40640438069. PR #2 HEAD `a14968d1aa4ff842cfd025b118c5ce90d60c55aa` 6 CI SUCCESS ; PR #3 HEAD `f87eb7e1ecc41f21611aadd5c3029ac6e16f313e` 8 CI SUCCESS, 188 CLI historiques et 12 API sans régression. **Pas de vrai IdP client, ACL, mandat externe, gouvernance MCP PHP2SHELL ou `ALLOW`**.


- **REQ-003 / REQ-013 / REQ-020 / REQ-022 / REQ-032 PARTIELLES — P2S-EVT-039** : onboarding débutant à trois étapes sans compte pour preview hors ligne ; choix intelligibles pour P1/P2, budgets avancés repliés, aucune fonction live ni vrai login. PR #2 `69cbbc6b13a08d2ce845754d2e9156edc018510d` RED tests #40641715258 → GREEN 6 CI au HEAD ; PR #3 `97808da8783abb9625d7aa2b5efdfe7316cba998` 8 CI SUCCESS, 190 CLI historiques / 12 API / 28 auth. UX améliorée mais **aucune capacité V1.0 authentifiée ou de scan déployée**. Aucune évolution de statut des 61 work packages.


- **REQ-003 / REQ-013 / REQ-020 / REQ-022 / REQ-032 PARTIELLES — P2S-EVT-040** : moteur de synthèse courte `app/public_summary.py` et API locale `/api/v0.2/guest/summary` ajoutés avec refus par défaut et aucun réseau, aucune identité, autorisation de scan ou persistance. RED 9 tests moteur #40642957257, GREEN #40643056790 ; RED 5 API #40643290583, GREEN #40643320032 ; PR #2 `dc2a61d` six CI SUCCESS, PR #3 `ddc8871` huit CI SUCCESS ; 199 historiques, 17 API, 28 auth. **Le vrai scan invité, les comptes, l'historique détaillé et le lien GitHub vérifié restent NON implémentés**.


- **REQ-004 / REQ-020 / REQ-025 / REQ-032 PARTIELLES — P2S-EVT-041** : `app/http_metadata_normalizer.py` et `tests/test_http_metadata_normalizer.py` (12 tests) ajoutent un filtre hors ligne strict des noms d'en-têtes fournis (sans valeurs, cookies, tokens, URL, réseau, stockage ou preuve d'origine), avec raccordement au moteur de synthèse anonyme non vérifiée. PR #2 `6ca140324820b982beb59408bdd29b0edaeb25c2` : **211 tests historiques + 17 API + 28 auth**, six CI exact SHA SUCCESS. PR #3 `92053ae770a1f5d56d817d16e87c3498c5903872` : huit CI SUCCESS, trois fichiers S1 conservés. **P2S-WF-E03/E05/Q01 demeurent PARTIELS / non admis à l'exécution réseau** : pas de collecteur réel, autorisation P1, vérification du site, preuve CVE ou déploiement.

## Preuve additive V0.3 — CI corrigée, paquet de revue non exécutable (P2S-EVT-042/043)

- **REQ-030 / P2S-WF-R06 = PARTIEL** : moteur et CLI `rehearse-config-patch` effectuent le remplacement de configuration et le rollback **en mémoire uniquement**, sans écrire de fichier, jamais un patch Git ou un rollback S1 ; code/CLI cohérents, CI rouge historique #40649601701 corrigée sur commit `57943460c30ca7a5d52ec681a731447cf252c4b4` (218 tests verts).
- **REQ-029/030/032 / P2S-WF-R06/Q01 = PARTIELS** : `prepare-patch-review` lie dossier courant, handoff, diff minimal, SHA-256 et répétition en mémoire, en ne conservant que des champs allowlist (sans code brut ni secrets). PR #2 HEAD `66aed9bdc742b7cb3ca7dfe705606ff58285fcf8`, **226 tests** et 6 CI tests/API/auth **SUCCESS** ; PR #3 `f11be476228573a1760ec6307351f625cffc7ca0`, huit CI SUCCESS tests/API/auth/préflight S1, sans déploiement.
- **Restent NON acquis** : preuve de propriété/mandat P2 authentifiée, runtime PHP actif, applicabilité réelle CVE, workspace isolé, test PHP/Docker, PR de correction, approbation indépendante, véritable rollback, déploiement S1. Aucun changement des 32 exigences, six lots, 61 WP, cinq versions ni de leurs critères d'acceptation.
