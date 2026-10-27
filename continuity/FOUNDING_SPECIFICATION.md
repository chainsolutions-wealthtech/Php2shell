# PHP2SHELL — cahier des charges fondateur réconcilié (sans régression)

**Continuity ID :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Ancre :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5  
**Périmètre :** spécification cible/mandats déclarés, PAS déclaration d'implémentation.
**Date de consolidation :** 2026-10-27.

## 1. Mission de départ — NE PAS RÉDUIRE À UN SCRIPT DE VERSION

Construire un **agent autonome d'audit défensif, de détection, de qualification et de remédiation des vulnérabilités PHP**, en mesure de gérer des centaines ou milliers de noms de domaine **dans des campagnes bornées et autorisées**, avec traçabilité de bout en bout, et une plateforme Web de supervision. L'autonomie concerne l'inventaire autorisé, la planification, l'analyse passive et locale, la collecte des preuves, les propositions et les tests isolés. Elle **n'autorise pas** les accès intrusifs, les exploits ni les modifications de systèmes réels sans mandat et admission.

La plateforme doit reconnaître et hiérarchiser les deux risques initiaux CVE-2026-109618 et CVE-2026-109619, avec une intelligence des vulnérabilités **extensible et non figée à deux CVE**. Le besoin primordial porte sur le **runtime PHP installé**, la SAPI et les correctifs du fournisseur ; un correctif dans un fichier applicatif ne suffit pas pour corriger une faille du moteur.

## 2. Deux niveaux opérationnels d'autorisation (règle fondamentale)

| Niveau | Type d'actif | Collecte et action admissibles | Contrôles |
| --- | --- | --- | --- |
| **P1 — Métadonnées publiques** | Domaine tiers ou site non administré | Import / déduplication de listes fournies, analyse des données publiques documentées et des indices HTTP **uniquement via une campagne de collecte non intrusive explicitement admise et limitée** ; rapport d'indices avec confiance ; PAS de code PHP interne, pas de vulnérabilité confirmée, pas de scanning agressif, pas d'exploit, pas de patch | Scope et origine, limites de débit/concurrence, restrictions de destinations et redirections, journal des observations, option "aucune requête réseau" |
| **P2 — Source et environnement possédés/autorisés** | Dépôt ou serveur détenu, autorisation explicite du responsable | Accès borné aux sources et configurations, versions runtime attestées, analyse statique, validation de patch en clone/lab, propositions Git/PR, tests ; déploiement ultérieur seulement avec mandat distinct et approbation | Preuve d'autorisation, portée exacte, expiration, identités/mandats, RBAC, accès minimal et revue séparée |

**Correspondance aux types de portée déjà présents dans la CLI V0.1 (compatibilité obligatoire) :** `P1 → public_metadata` et `P2 → owned_source`. Ces labels sont pour l'instant déclaratifs : une future version doit contrôler une preuve d'autorisation et un mandat avant toute lecture de sources ou requête réseau. Aucune promotion implicite P1→P2.

Un nom dans un CSV ou un DNS public n'est **jamais** une preuve suffisante pour scanner intensivement un site. L'identification passive de technologie n'est pas une preuve de vulnérabilité. Une page Web publique renvoie généralement du HTML généré et **non le code PHP côté serveur**.

## 3. Chaîne complète de 10 capacités de produit

**CAP-01 — Campaign & Domain Inventory.** Imports CSV/JSON/TXT, centaines/milliers de cibles, validation domaines, normalisation, déduplication, campagnes, propriétaires/scope, permissions, refus automatiques des cibles hors périmètre, pagination, suivi et statut par cible.

**CAP-02 — Passive Audit Agent.** Recherche de signaux HTTP/headers déjà exposés, indices publics de framework/CMS et versions publiquement visibles, collecte de métadonnées de manière non intrusive, statut `php_possible` / `non_determine` avec provenance, horodatage et confiance. Aucune interprétation de signature comme exploitabilité. Le code source PHP serveur n'est pas accessible via une simple requête HTTP.

**CAP-03 — CVE Intelligence.** Catalogue officiel actualisable (PHP Security Advisories, avis des éditeurs et distributions, CERT-FR/CERT-EU, CVE/NVD), dates/version/source, scores sourcés, branches, SAPI, backports, statut de vérification. Classification distincte `confirmed_applicability`, `potential_exposure`, `insufficient_evidence`, `not_applicable`, `vendor_patched`.

**CAP-04 — Authorized Source Review Agent.** Lecture locale de dépôts approuvés, AST PHP, `composer.json` et `composer.lock`, configurations PHP/FPM/Apache/Nginx, analyse des dépendances effectivement résolues, localisation symboles/fichiers/lignes, preuves contextuelles et confiance. Les empreintes et extraits sensibles restent dans stockage privé.

**CAP-05 — Runtime & Environment Agent.** Attestation de `php -v` / paquets installés / image digests/SAPI/configuration **sur machines explicitement autorisées** ; distinction version upstream et correctif fournisseur rétroporté, extensions et reprise de workers. Pour CVE PHP runtime, proposer une montée de version PHP plutôt que seulement modifier des sources applicatives.

**CAP-06 — Patch Generator.** Propose changements minimaux runtime/dépendances/configuration/code avec justification, risques, diffs, plan de compatibilité, métadonnées avant/après, PR candidate. Ne jamais appliquer une modification silencieuse sur la production.

**CAP-07 — Validation Agent / Lab.** Docker isolé, fixtures `portail-demo.example`, contrôle de versions et configurations, lint/statique/unitaires/intégration/compatibilité, non-régression, preuves, simulation de rollback. Aucun payload RCE sur sites publics ; tests de sécurité actifs exclusivement en laboratoires explicitement autorisés.

**CAP-08 — Evidence & Remediation Store.** PostgreSQL pour campagnes, actifs, décisions, faits sourcés, observations, identité/mandats, états de remédiation, artefacts, horodatages, checkpoints et journaux d'audit append-only logiques. Secrets et données privées **hors dépôt public**.

**CAP-09 — Governed Orchestration & Deployment.** Workers asynchrones, files Redis (ou équivalent validé), quotas, annulation/reprise, anti-doublons, retries bornés, supervision des erreurs, audit ; pipeline GitHub→MCP existant→S1 exact SHA, séparation des permissions, sauvegarde et rollback.

**CAP-10 — Dual Web Consoles & Outputs.** Contrôle utilisateur central/authentifié, campagnes/projets/historique/alertes ; `php2shell.wealthtechinnovations.com` pour inventaire/analyses, `phppatch.wealthtechinnovations.com` pour diffs/tests/approbations ; API partagée, export PDF/CSV/JSON, patches Git/PR et rapports d'exécution.

## 4. Architecture cible initiale (choix proposés, pas toutes technologies déjà acquises)

- **Moteur Python** : cœur d'analyse (existant en V0.1/V0.2 locale).
- **FastAPI** : API du control plane, futur jalon d'application sécurisée, **non implémentée**.
- **PostgreSQL** : conservation canonique privée des campagnes, preuves et historique, **non implémenté**.
- **Redis + workers** : orchestration des campagnes sous quotas et sans doublons, **non implémentés**, choix à valider selon les mécanismes MCP déjà disponibles (ne pas recréer une Task Queue d'autorité concurrente).
- **Docker / Docker Compose** : prototype CLI/lab déjà présent ; topologie production isolée, non-root, ressources bornées, ports internes et Plesk TLS **encore à construire**.
- **MCP GitHub / S1** : réutiliser la gouvernance et les déploiements existants de `Patricked-code/MCP` ; aucune deuxième gateway ni fusion d'autorités.
- **Control Plane + agents spécialisés** : modules d'un même produit, non des identités ou dispatchers indépendants ; adapter aux mécanismes d'autorisation réels avant tout runtime.

## 5. Sécurité de la collecte multi-domaines — critères de conception

- Liste explicite des domaines autorisés pour l'opération et du **type de collecte** permis ; mandats horodatés.
- Refuser les schémas/ports/destinations hors autorisation, les IP privées, loopback, link-local et endpoints de métadonnées cloud si non expressément prévus ; validation DNS/URL et revalidation après résolution et redirection (risque SSRF/dérive DNS).
- Rate limits par domaine, budgets globaux, limites de concurrence, délais, délais d'expiration, circuit breakers, gestion des erreurs et arrêt immédiat.
- Aucune énumération agressive, contournement d'authentification, exploitation RCE, écriture distante ni collecte de code source de tiers.
- Contrôler la confidentialité des en-têtes, cookies et URLs ; supprimer les secrets des rapports et journaliser **les décisions/permissions, pas des données personnelles inutiles**.
- Preuve d'accès à une source/serveur != autorisation de publier des artefacts contenant son contenu : la publication publique GitHub est restreinte à du code non sensible et des constats fictifs.

## 6. Six lots historiques — complémentaires aux cinq versions, PAS remplacés

| Lot initial | Livrable initial | Correspondance progressive |
|---|---|---|
| **L1** — Socle API, Docker, base, gouvernance | Plateforme initiale | V0.1 (CLI/tests) + extensions V0.4/V1.0 (API/base Docker prod) |
| **L2** — Import domaine et détection PHP passive | Moteur inventaire | V0.2 (imports/campagnes/sondes consenties), interface V1.0 |
| **L3** — CVE, versions et preuves | Rapport de vulnérabilité | V0.2 intelligence CVE + données attestées |
| **L4** — Audit sources + génération patchs | Patch Git | V0.2 analyse locale → V0.3 patch |
| **L5** — Laboratoire + validations | Artefacts de tests | V0.3 sandbox → V0.4 Docker/runtime |
| **L6** — Interface, rapports, déploiement | Plateforme opérationnelle | V0.4 MCP/S1 → V1.0 consoles + rapports |

Cette table est une **traçabilité des deux découpages complémentaires** : les travaux d'infrastructure anticipés ne sont pas un changement du plan métier ni une annonce de livraison de V0.4 ou V1.0.

## 7. Exemple du scénario de référence

Actif fictif `portail-demo.example`, version locale déclarée **PHP 8.3.34** ; demande de vérification de CVE-2026-109618/109619. **Le cas illustratif historique utilise une version en-dessous de l'upstream PHP 8.3.36, mais un diagnostic réel exige la confirmation du runtime et des correctifs rétroportés.** Remédiation candidate : mise à jour vers 8.3.36 ou version maintenue plus récente, révision extensions/SAPI et compatibilité, redémarrage contrôlé des workers, tests applicatifs. Rapport proposé PDF/JSON; statut `SCENARIO_DEFINED_NOT_EXECUTED` tant qu'aucune exécution n'est prouvée.

## Extension additive : parcours URL → pages autorisées → diagnostic → rapport → correctif proposé

Mandat utilisateur du 27/10/2026 : le **frontend PHP2SHELL** doit proposer un champ d'URL déclenchant un audit de bout en bout avec navigation bornée, inventaire des pages et vulnérabilités apparentes, rapport et document de remédiation. Le **frontend PHPPATCH** reçoit ensuite les corrections **proposées** (moteur PHP, dépendances, configuration, code Git) accompagnées de diffs, tests, approbation et rollback.

Le **mode URL/P1**, limité aux métadonnées publiquement accessibles et aux requêtes Web explicitement admises, **n'expose pas la source PHP interne** : le serveur retourne habituellement le rendu HTML/JS public. Le **mode approfondi P2** exige en complément un accès autorisé au code Git/fichiers et aux informations du runtime PHP installé (y compris correctifs fournisseur) avant de prétendre confirmer une exposition CVE. Les résultats distinguent **indices**, **exposition potentielle**, **preuves insuffisantes** et **applicabilité effectivement attestée** ; les zones non parcourues restent signalées.

Conserver cette fonctionnalité dans les dix capacités existantes **CAP-01, CAP-02, CAP-03, CAP-04, CAP-05, CAP-06, CAP-07, CAP-10** sans créer un onzième agent/gateway concurrent, et dans les six lots L2–L6. **Contrat fonctionnel détaillé :** [`URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md`](URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md) ; **exigences : REQ-023→REQ-032**. Aucun crawler ni UI produit à ce stade.

## 8. Préservation de l'existant

PR #1 (V0.1) → PR #2 (V0.2) → PR #3 (S1) ; issue #4 (S1) ; PR #6 (continuité), issue #5 (ancre).
Les **implémentations** restent des preuves distinctes des **objectifs** : les 10 capacités ci-dessus décrivent la cible, pas un logiciel déjà installé ou un accès universel aux sites listés.
