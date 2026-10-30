# Commit exact addd9bcfccfdac7d2ec4e37808b184aa2e397bb7

Date UTC 2026-10-28T03:16:25Z; source https://github.com/chainsolutions-wealthtech/Php2shell/commit/addd9bcfccfdac7d2ec4e37808b184aa2e397bb7

Parents: 3252bfece52612a805b2931940a184bf3c9be4a0

Fichiers 1; +5/-5

## continuity/REQUIREMENTS_TRACEABILITY.md (modified, +5/-5)

Blob 1893735c3675e9f40d4e1627d6c72589b76c21ff; https://github.com/chainsolutions-wealthtech/Php2shell/blob/addd9bcfccfdac7d2ec4e37808b184aa2e397bb7/continuity%2FREQUIREMENTS_TRACEABILITY.md

```diff
@@ -12,8 +12,8 @@ Ce registre traduit **le programme initial (six lots) + son évolution (cinq ver
 | Exigence | Origine / lot initial | Version(s) cible(s) | État daté 27/10/2026 | Acceptation future et preuve attendue |
 | --- | --- | --- | --- | --- |
 | **REQ-001** imports CSV/JSON/TXT | Inventaire / L2 | V0.2/V1.0 | **Partiel** : JSON déclaré CLI V0.1 ; CSV/TXT/campagnes non implémentés | Import des 3 formats, normalisation par DNS-label, déduplication, rejets et pagination testés |
-| **REQ-002** centaines/milliers cibles | Inventaire/campagnes / L2 | V0.2/V1.0 | **Partiel** : prévisualisation hors ligne `preview-url` à budget borné et aucune requête ; campagnes massives, stockage, reprise, crawl et worker NON implémentés | Campagne testée à volume élevé avec budgets, limites, retries, reprise et preuves, sans requête non autorisée |
-| **REQ-003** double niveau d'autorisation | Exigence fondatrice / L1-L2 | Toutes | **Partiel** : `public_metadata` vs `owned_source` déclaratifs, pas de vérification de mandat | Autorité, date/fin/portée et permissions admises ; refus hors périmètre et tests négatifs |
+| **REQ-002** centaines/milliers cibles | Inventaire/campagnes / L2 | V0.2/V1.0 | **Partiel** : `preview-url` et `plan-campaign` hors ligne, déduplication et partitions stables (1000 cibles testées, au plus 10 000 admises au plan) ; ni job créé, ni campagne exécutée, ni base/worker, quotas persistants ou reprise réelle | Campagne testée à volume élevé avec budgets, limites, retries, reprise et preuves, sans requête non autorisée |
+| **REQ-003** double niveau d'autorisation | Exigence fondatrice / L1-L2 | Toutes | **Partiel** : modes P1/P2 et précontrôle local des domaines, dates, scopes et budgets ; toutes les attestations d'identité, signature, autorité et droits restent `false`, aucune admission MCP réelle | Autorité, date/fin/portée et permissions admises ; refus hors périmètre et tests négatifs |
 | **REQ-004** identification PHP passive et framework | Passive Audit / L2 | V0.2 | Non implémenté | Indices publics non intrusifs avec sources et confiance, redirections validées, taux bornés, absence de faux diagnostic |
 | **REQ-005** catalogue officiel CVE sourcé | CVE Intelligence / L3 | V0.2 | **Partiel** : instantané CVE PHP/CERT-FR sourcé, audit âge/SHA-256, comparateur hors ligne et **client HTTP GitHub explicitement opt-in** à allowlist de GHSA pré-admis, TLS/redirections/taille/identité vérifiés ; 81 tests PR #2. Un client testable **ne prouve pas une acquisition réseau réelle, une ingestion périodique, une signature upstream, ni le suivi fournisseurs/backports**. | Provenance datée + avis upstream/fournisseur, branche, score, backport, tests de divergence |
 | **REQ-006** version runtime réelle / SAPI | CVE/runtime / L3 | V0.2/V0.3 | **Partiel** : comparaison semver sourcée + enveloppe JSON déclarative du runtime/SAPI (`review-runtime-evidence`, PR #2, 89 tests) ; preuve de mandat, capture signée, runtime HTTP effectif et backports **NON attestés** | Collecte sous mandat de PHP réellement exécuté, paquets, config, SAPI, extension et état patched |
@@ -29,10 +29,10 @@ Ce registre traduit **le programme initial (six lots) + son évolution (cinq ver
 | **REQ-016** Docker et lab isolé | L1/L5 | V0.3/V0.4 | Prototype Docker CLI/lab présent ; prod non implémentée | Conteneurs non-root, pas de secrets, réseau/volumes/CPU/mémoire restreints, essais reproductibles |
 | **REQ-017** GitHub App/MCP existant/S1 | Déploiement / L6 | V0.4 | Plesk/DNS/TLS/préflight PR #3 ; application non déployée | Autorisation, claim/lock, exact SHA, CI revue, staging, E2E, rollback attestés |
 | **REQ-018** double console Web | Supervision / L6 | V1.0 | Deux DNS/vhosts S1, interfaces non implémentées | PHP2SHELL analyse + PHPPATCH remédiation, même moteur, tests RBAC négatifs |
-| **REQ-019** PDF/CSV/JSON + Git PR | Sorties / L6 | V0.2/V0.3/V1.0 | **Partiel** : JSON/CSV acquis et nouveau dossier d'audit **JSON + Markdown** à constats PHP/config, recommandations soumises à revue, runtime déclaré non attesté (PR #2, 113 tests). Rapports PDF, diagnostic confirmé, génération de diffs/PR PHPPATCH NON livrés | Exports cohérents, tests d'absence de secrets, résultats traçables à une campagne |
+| **REQ-019** PDF/CSV/JSON + Git PR | Sorties / L6 | V0.2/V0.3/V1.0 | **Partiel** : JSON/CSV/Markdown et rendu HTML statique d'un dossier d'audit local avec contrôles anti-injection ; PDF, diagnostic confirmé, backend API, production et vrais diffs/PR PHPPATCH NON livrés | Exports cohérents, tests d'absence de secrets, résultats traçables à une campagne |
 | **REQ-020** audit durable + reprise conversation | Gouvernance transversale | Toutes | Issue #5 + PR #6 documentaire avec CI ; non fusionnée | Dernier checkpoint exact, registres append-only, actions et preuves relues en nouvelle conversation |
 | **REQ-021** simulation `portail-demo.example` PHP 8.3.34 | Lab historique / L5 | V0.2/V0.3 | Scénario défini, aucun test runtime 8.3.34 spécifiquement prouvé | Build image réellement épinglée 8.3.34, analyse uniquement labo, proposition de mise à jour, compatibilité testée |
-| **REQ-022** contrôle SSRF/redirections/concurrence | Collecte / L2 | V0.2/V0.4 | **Partiel (intake uniquement)** : `preview-url` rejette URL IP, credentials, schémas et ports non autorisés ; aucun DNS/IP effectif, contrôle redirect, quotas runtime ni crawl réseaux n'est implémenté | Rejet loopback/privé/hors-scope, revalidation DNS après redirect, quotas, échecs et journaux |
+| **REQ-022** contrôle SSRF/redirections/concurrence | Collecte / L2 | V0.2/V0.4 | **Partiel (sans réseau)** : prévisualisation URL, classification de réponses A/AAAA fournies localement, refus des adresses non globales et redirections hors origine ; DNS réel, pair connecté, rebinding, robots et budgets runtime NON implémentés | Rejet loopback/privé/hors-scope, revalidation DNS après redirect, quotas, échecs et journaux |
 | **REQ-023** URL unique saisie depuis le frontend | Extension explicite de CAP-01 / L2-L6 | V0.2/V1.0 | **Non implémenté** : pas de frontend ni d'API d'audit Web | Saisie URL, projet, type d'audit et mandat, validation et statut de campagne; refus de cible non admise |
 | **REQ-024** découverte/crawl des pages autorisées | CAP-02 / L2 | V0.2/V1.0 | Non implémenté | Parcours sitemap, liens et pages accessibles **uniquement sous mandat**, quotas/profondeur/horodatages/couverture et limites affichés |
 | **REQ-025** analyse des contenus et signaux Web | CAP-02 / L2 | V0.2 | Non implémenté | HTTP/HTML/JS public, headers, cookies, redirections, framework et PHP probable; preuves/confidence et aucune lecture PHP serveur déduite d'une URL |
@@ -41,7 +41,7 @@ Ce registre traduit **le programme initial (six lots) + son évolution (cinq ver
 | **REQ-028** panneau PHP2Shell CVE et statut par actif | CAP-03/CAP-05 / L3 | V0.2/V1.0 | Documents CVE présents, moteur d'applicabilité non implémenté | Source officielle vérifiée distincte de runtime réellement attesté; catégories insuffisant/potentiel/applicable/fournisseur corrigé |
 | **REQ-029** document de remédiation Web→PDF/JSON/CSV | CAP-08/CAP-10 / L6 | V0.2/V1.0 | Non implémenté | Dossier auditable avec périmètre, preuves, sévérité sourcée, incertitude, plan runtime/config/code, tests et rollback, sans secrets |
 | **REQ-030** passage PHP2SHELL→PHPPATCH | CAP-06/CAP-07/CAP-10 / L4-L6 | V0.3/V1.0 | Non implémenté | Finding/mandat transférés, patch candidat/diff, sandbox, test, approbation, PR, jamais déploiement automatique |
-| **REQ-031** sécurité de navigation URL/SSRF | CAP-01/CAP-02 / L2 | V0.2/V0.4 | **Partiel (prévisualisation seulement)** : parsing HTTPS strict et refus IP/local/path traversals, mode offline ; DNS public/rebinding, redirects, peer IP, robots, quotas, annulation et sessions restent à construire | Refus credentials/IP internes/redirections hors scope/rebinding, budgets de requêtes et annulation ; tests négatifs et absence d'exploit |
+| **REQ-031** sécurité de navigation URL/SSRF | CAP-01/CAP-02 / L2 | V0.2/V0.4 | **Partiel (préflight hors ligne)** : validation URL, précontrôle de listes IP et redirections de même origine ; aucune connexion autorisée ni protection d'exécution DNS/rebinding/pair TLS, annulation, quotas et sessions implémentés | Refus credentials/IP internes/redirections hors scope/rebinding, budgets de requêtes et annulation ; tests négatifs et absence d'exploit |
 | **REQ-032** recette bout en bout frontend/audit/rapport/patch | L5-L6 | V0.3/V0.4/V1.0 | Non implémenté | Fixtures fictives, permissions P1/P2, scans arrêtables, rapports vérifiables, patch/CI/rollback en lab, auth/RBAC et tests E2E S1 |
 
 
```

Attention: inspection du diff Git, sans attestation de tests ou d'exploitation.