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
| **REQ-002** centaines/milliers cibles | Inventaire/campagnes / L2 | V0.2/V1.0 | **Partiel** : prévisualisation hors ligne `preview-url` à budget borné et aucune requête ; campagnes massives, stockage, reprise, crawl et worker NON implémentés | Campagne testée à volume élevé avec budgets, limites, retries, reprise et preuves, sans requête non autorisée |
| **REQ-003** double niveau d'autorisation | Exigence fondatrice / L1-L2 | Toutes | **Partiel** : `public_metadata` vs `owned_source` déclaratifs, pas de vérification de mandat | Autorité, date/fin/portée et permissions admises ; refus hors périmètre et tests négatifs |
| **REQ-004** identification PHP passive et framework | Passive Audit / L2 | V0.2 | Non implémenté | Indices publics non intrusifs avec sources et confiance, redirections validées, taux bornés, absence de faux diagnostic |
| **REQ-005** catalogue officiel CVE sourcé | CVE Intelligence / L3 | V0.2 | **Partiel** : instantané CVE PHP/CERT-FR sourcé, audit âge/SHA-256, comparateur hors ligne et **client HTTP GitHub explicitement opt-in** à allowlist de GHSA pré-admis, TLS/redirections/taille/identité vérifiés ; 81 tests PR #2. Un client testable **ne prouve pas une acquisition réseau réelle, une ingestion périodique, une signature upstream, ni le suivi fournisseurs/backports**. | Provenance datée + avis upstream/fournisseur, branche, score, backport, tests de divergence |
| **REQ-006** version runtime réelle / SAPI | CVE/runtime / L3 | V0.2/V0.3 | **Partiel** : comparaison semver sourcée + enveloppe JSON déclarative du runtime/SAPI (`review-runtime-evidence`, PR #2, 89 tests) ; preuve de mandat, capture signée, runtime HTTP effectif et backports **NON attestés** | Collecte sous mandat de PHP réellement exécuté, paquets, config, SAPI, extension et état patched |
| **REQ-007** analyse fichiers PHP / AST | Source Review / L4 | V0.2 | **Partiel** : scanner lexical local PR #2 | AST, faux positifs négatifs mesurés, chemin/ligne/preuve, limites documentées |
| **REQ-008** Composer et configs | Source Review / L4 | V0.2 | **Partiel** : `composer.json`/`composer.lock`, `php.ini`/`.user.ini` et certaines configurations PHP-FPM lus **hors ligne** sur PR #2 ; pas de runtime/SAPI effectif ni de configuration webserver complète | Lockfile, dépendances installées, php.ini/FPM/webserver analysés depuis sources autorisées |
| **REQ-009** preuves et niveaux de confiance | CVE/rapport / L3-L4 | V0.2/V1.0 | **Partiel** : indice lexical, `review_required`, sans qualification d'applicabilité | Evidence ID, source, ligne, dates, classification et incertitude, rapport révisable |
| **REQ-010** proposition de patch runtime/code/config | Patch Generator / L4 | V0.3 | Non implémenté | Diff minimal, justification, compatibilité, PR candidate et version runtime corrigée si nécessaire |
| **REQ-011** tests patch avant/après | Validation / L5 | V0.3 | Non implémenté (tests de la CLI seulement) | CI/lint/intégration/non-régression sur copie isolée autorisée, résultats signés |
| **REQ-012** rollback/sauvegarde | Validation / L5-L6 | V0.3/V0.4 | Procédure documentée, pas prouvée en exécution | Rollback en labo et en staging approuvé, checkpoint de restauration |
| **REQ-013** Python/FastAPI API commune | Plateforme / L1 | V0.4/V1.0 | Python CLI présent ; FastAPI non implémenté | API authentifiée, tests permissions, OpenAPI/contrats, isolation des consoles |
| **REQ-014** PostgreSQL / artefacts | Control Plane/Store / L1 | V0.4/V1.0 | Non implémenté | Stockage privé des campagnes et preuves, migrations, RBAC, sauvegardes, rétention |
| **REQ-015** Redis & workers bornés | Orchestration / L1-L2 | V0.4/V1.0 | Non implémenté | File robuste, anti-doublons, annulation/retry contrôlés ; ne pas concurrencer l'autorité MCP |
| **REQ-016** Docker et lab isolé | L1/L5 | V0.3/V0.4 | Prototype Docker CLI/lab présent ; prod non implémentée | Conteneurs non-root, pas de secrets, réseau/volumes/CPU/mémoire restreints, essais reproductibles |
| **REQ-017** GitHub App/MCP existant/S1 | Déploiement / L6 | V0.4 | Plesk/DNS/TLS/préflight PR #3 ; application non déployée | Autorisation, claim/lock, exact SHA, CI revue, staging, E2E, rollback attestés |
| **REQ-018** double console Web | Supervision / L6 | V1.0 | Deux DNS/vhosts S1, interfaces non implémentées | PHP2SHELL analyse + PHPPATCH remédiation, même moteur, tests RBAC négatifs |
| **REQ-019** PDF/CSV/JSON + Git PR | Sorties / L6 | V0.2/V0.3/V1.0 | **Partiel** : JSON/CSV acquis et nouveau dossier d'audit **JSON + Markdown** à constats PHP/config, recommandations soumises à revue, runtime déclaré non attesté (PR #2, 113 tests). Rapports PDF, diagnostic confirmé, génération de diffs/PR PHPPATCH NON livrés | Exports cohérents, tests d'absence de secrets, résultats traçables à une campagne |
| **REQ-020** audit durable + reprise conversation | Gouvernance transversale | Toutes | Issue #5 + PR #6 documentaire avec CI ; non fusionnée | Dernier checkpoint exact, registres append-only, actions et preuves relues en nouvelle conversation |
| **REQ-021** simulation `portail-demo.example` PHP 8.3.34 | Lab historique / L5 | V0.2/V0.3 | Scénario défini, aucun test runtime 8.3.34 spécifiquement prouvé | Build image réellement épinglée 8.3.34, analyse uniquement labo, proposition de mise à jour, compatibilité testée |
| **REQ-022** contrôle SSRF/redirections/concurrence | Collecte / L2 | V0.2/V0.4 | **Partiel (intake uniquement)** : `preview-url` rejette URL IP, credentials, schémas et ports non autorisés ; aucun DNS/IP effectif, contrôle redirect, quotas runtime ni crawl réseaux n'est implémenté | Rejet loopback/privé/hors-scope, revalidation DNS après redirect, quotas, échecs et journaux |
| **REQ-023** URL unique saisie depuis le frontend | Extension explicite de CAP-01 / L2-L6 | V0.2/V1.0 | **Non implémenté** : pas de frontend ni d'API d'audit Web | Saisie URL, projet, type d'audit et mandat, validation et statut de campagne; refus de cible non admise |
| **REQ-024** découverte/crawl des pages autorisées | CAP-02 / L2 | V0.2/V1.0 | Non implémenté | Parcours sitemap, liens et pages accessibles **uniquement sous mandat**, quotas/profondeur/horodatages/couverture et limites affichés |
| **REQ-025** analyse des contenus et signaux Web | CAP-02 / L2 | V0.2 | Non implémenté | HTTP/HTML/JS public, headers, cookies, redirections, framework et PHP probable; preuves/confidence et aucune lecture PHP serveur déduite d'une URL |
| **REQ-026** audit approfondi après liaison P2 | CAP-04/CAP-05 / L4 | V0.2/V0.4 | Non implémenté | Dépôt Git exact SHA, source PHP, Composer, configs, runtime installé/SAPI et backports examinés **uniquement après autorisation vérifiée** |
| **REQ-027** diagnostic par page et preuve d'ampleur | CAP-02/CAP-03 / L2-L3 | V0.2/V1.0 | Non implémenté | Synthèse par URL/fichier/constat, horodatage, méthode, pages visitées/non découvertes et niveaux de confiance; ne pas affirmer « toutes les pages » |
| **REQ-028** panneau PHP2Shell CVE et statut par actif | CAP-03/CAP-05 / L3 | V0.2/V1.0 | Documents CVE présents, moteur d'applicabilité non implémenté | Source officielle vérifiée distincte de runtime réellement attesté; catégories insuffisant/potentiel/applicable/fournisseur corrigé |
| **REQ-029** document de remédiation Web→PDF/JSON/CSV | CAP-08/CAP-10 / L6 | V0.2/V1.0 | Non implémenté | Dossier auditable avec périmètre, preuves, sévérité sourcée, incertitude, plan runtime/config/code, tests et rollback, sans secrets |
| **REQ-030** passage PHP2SHELL→PHPPATCH | CAP-06/CAP-07/CAP-10 / L4-L6 | V0.3/V1.0 | Non implémenté | Finding/mandat transférés, patch candidat/diff, sandbox, test, approbation, PR, jamais déploiement automatique |
| **REQ-031** sécurité de navigation URL/SSRF | CAP-01/CAP-02 / L2 | V0.2/V0.4 | **Partiel (prévisualisation seulement)** : parsing HTTPS strict et refus IP/local/path traversals, mode offline ; DNS public/rebinding, redirects, peer IP, robots, quotas, annulation et sessions restent à construire | Refus credentials/IP internes/redirections hors scope/rebinding, budgets de requêtes et annulation ; tests négatifs et absence d'exploit |
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
