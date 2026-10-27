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
| **REQ-002** centaines/milliers cibles | Inventaire/campagnes / L2 | V0.2/V1.0 | Non implémenté | Campagne testée à volume élevé avec budgets, limites, retries, reprise et preuves, sans requête non autorisée |
| **REQ-003** double niveau d'autorisation | Exigence fondatrice / L1-L2 | Toutes | **Partiel** : `public_metadata` vs `owned_source` déclaratifs, pas de vérification de mandat | Autorité, date/fin/portée et permissions admises ; refus hors périmètre et tests négatifs |
| **REQ-004** identification PHP passive et framework | Passive Audit / L2 | V0.2 | Non implémenté | Indices publics non intrusifs avec sources et confiance, redirections validées, taux bornés, absence de faux diagnostic |
| **REQ-005** catalogue officiel CVE sourcé | CVE Intelligence / L3 | V0.2 | **Références publiques vérifiées documentalement**, ingestion/validation de catalogue NON implémentées | Provenance datée + avis upstream/fournisseur, branche, score, backport, tests de divergence |
| **REQ-006** version runtime réelle / SAPI | CVE/runtime / L3 | V0.2/V0.3 | Comparaison semver démo seulement, non attestation de serveur | Collecte sous mandat de PHP réellement exécuté, paquets, config, SAPI, extension et état patched |
| **REQ-007** analyse fichiers PHP / AST | Source Review / L4 | V0.2 | **Partiel** : scanner lexical local PR #2 | AST, faux positifs négatifs mesurés, chemin/ligne/preuve, limites documentées |
| **REQ-008** Composer et configs | Source Review / L4 | V0.2 | **Partiel** : `composer.json` lu, pas `composer.lock` ni runtime/config complète | Lockfile, dépendances installées, php.ini/FPM/webserver analysés depuis sources autorisées |
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
| **REQ-019** PDF/CSV/JSON + Git PR | Sorties / L6 | V0.2/V0.3/V1.0 | JSON CLI présent ; PDF/CSV, Git patches à construire | Exports cohérents, tests d'absence de secrets, résultats traçables à une campagne |
| **REQ-020** audit durable + reprise conversation | Gouvernance transversale | Toutes | Issue #5 + PR #6 documentaire avec CI ; non fusionnée | Dernier checkpoint exact, registres append-only, actions et preuves relues en nouvelle conversation |
| **REQ-021** simulation `portail-demo.example` PHP 8.3.34 | Lab historique / L5 | V0.2/V0.3 | Scénario défini, aucun test runtime 8.3.34 spécifiquement prouvé | Build image réellement épinglée 8.3.34, analyse uniquement labo, proposition de mise à jour, compatibilité testée |
| **REQ-022** contrôle SSRF/redirections/concurrence | Collecte / L2 | V0.2/V0.4 | Non implémenté (scanner CLI sans réseau) | Rejet loopback/privé/hors-scope, revalidation DNS après redirect, quotas, échecs et journaux |

**Principe de comptabilité :** `Partiel` signifie qu'une sous-capacité est prouvée, pas que la capacité est complète. `Références vérifiées documentalement` signifie que les avis existent, **pas** que le runtime d'un site est affecté.

## Deux classifications complémentaires

- **Versions de produit** : V0.1 fondations ; V0.2 analyse/code/dépendances/config/CVE/campagnes passives ; V0.3 patches/tests/rollback ; V0.4 MCP/S1/Docker ; V1.0 Web/gestion/projets/rapports.
- **Lots initiaux** : L1 socle API/Docker/base/gouvernance ; L2 campagnes/détection passive ; L3 CVE/versions/preuves ; L4 source/patch ; L5 lab/tests ; L6 console/rapports/déploiement.

**Aucune disparition de L1 (FastAPI/PostgreSQL/Redis/workers) sous prétexte que V0.1 actuelle est une CLI** : le livrable L1 reste à compléter dans V0.4/V1.0. L'ordre peut être planifié par dépendances techniques, sans renommer les exigences ni prétendre qu'elles sont déjà implémentées.

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
