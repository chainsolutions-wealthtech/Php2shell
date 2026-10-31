# URL_SITE_AUDIT_AND_PATCH_WORKFLOW — audit Web depuis le frontend et passage vers PHPPATCH

**Continuity ID :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Ancre permanente :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5  
**Décision utilisateur :** ajout **complémentaire** au cahier des charges fondateur et aux 5 versions / 6 lots, sans suppression ni régression.  
**Statut : SPÉCIFICATION CIBLE, NON IMPLÉMENTÉE, NON DÉPLOYÉE.**

## 1. Besoin utilisateur principal : URL → audit complet → diagnostic → document → patch proposé

Depuis la console `https://php2shell.wealthtechinnovations.com`, l'utilisateur doit pouvoir :

1. Saisir une **URL HTTPS ou HTTP** de site ou une liste de cibles (campagnes). Choisir un projet et la **portée autorisée** ; aucun crawl n'est démarré avant admission explicite de la cible et du type de collecte.
2. Pour un site relevant d'un mandat d'audit Web : **découvrir et parcourir progressivement les pages autorisées** par la navigation, sitemap.xml, liens et métadonnées publiques, avec quotas (pages, requêtes, bande passante, profondeur, durée, concurrence), suivi d'avancement, pause/arrêt/reprise.
3. Analyser ce qui est réellement accessible via HTTP : URL canoniques, chemins et réponses autorisés, liens, statuts, redirections, en-têtes de sécurité, configuration visible de cookies, contenu HTML public, **scripts JavaScript publics**, formulaires et informations exposées, indicateurs publics de PHP/CMS/framework et éventuelles divulgations de versions. Le rendu JS éventuel utilise un navigateur isolé sans accès à des réseaux ou destinations hors mandat.
4. Fournir un **rapport d'audit Web** : arborescence des pages effectivement visitées, technologies **supposées** avec niveau de confiance, indices, risques et configuration Web visibles, preuves minimisées, sources, incertitude, pages non explorées et raison de l'arrêt. La couverture est bornée : `all_pages_examined` n'est **jamais** affirmé sans garantie vérifiable sur le périmètre ; les pages non découvertes ou protégées peuvent rester inconnues.
5. Évaluer séparément les avis CVE-2026-109618 / CVE-2026-109619 et futurs avis officiels. **Une bannière PHP ou un HTTP 200 n'atteste pas la version du moteur réellement exécuté, sa distribution ni l'applicabilité de la CVE**. Mentionner `evidence_insufficient` / `potential_exposure` si le runtime n'est pas confirmé.
6. Si le responsable de l'actif a délivré une **autorisation de niveau source/environnement (P2)**, raccorder un dépôt Git identifié à un HEAD exact ou une instance administrée via un connecteur borné. Enrichir l'audit Web avec analyse **réelle des fichiers PHP serveur**, `composer.json` / `composer.lock`, configurations PHP/FPM/webserver, paquets, version runtime et corrections fournisseur. **Aucune URL publique ne permet, à elle seule, de lire tout le code PHP exécuté côté serveur.**
7. Produire le **document de remédiation** : projet, URL, périmètre/mandat, dates, méthodes réellement exécutées, niveau de confiance, inventaire, constats triés par sévérité, justificatifs, statut de chaque CVE, correctifs conseillés (runtime/dépendances/config/code), risques résiduels, plan d'essai, étapes et responsable d'approbation, plan de rollback, export PDF/JSON/CSV.
8. Depuis chaque constat admissible, proposer le passage vers **`https://phppatch.wealthtechinnovations.com`** : préparation d'un **patch candidat** (diff Git, package/runtime/config, explication), exécution de tests isolés, revue humaine, génération d'une PR, traçabilité et reprise. Ni l'affichage du patch ni son téléchargement ne valent autorisation d'application.
9. Conserver les résultats d'audit, les erreurs, la progression et les checkpoints dans un stockage privé avec liens de preuve non sensibles dans le registre gouverné. Rejouer seulement dans le périmètre mandaté et aux quotas définis.

**Règle fondamentale :** un audit Web public ne révèle généralement que HTML/CSS/JS et les informations exposées ; **pas** les fichiers `.php` source de la logique serveur. Un « audit approfondi de tout le code PHP » nécessite un accès explicite au dépôt, aux fichiers ou à la machine autorisée. Le système explique systématiquement cette limite.

## 2. Parcours frontend à conserver (deux consoles, un moteur)

```text
PHP2SHELL FRONTEND /analysis/new
  URL(s) du site + projet + identité du responsable + preuve d'autorisation
      |
      v
  Choix de mode / portée / limites / connecteurs autorisés
      |
      +--- P1 : métadonnées publiques + audit Web non intrusif soumis à admission
      |          (sans accès aux sources PHP, sans requête agressive)
      |
      +--- P2 : audit du site détenu/mandaté
                 audit Web borné + dépôt Git / runtime autorisé
      |
      v
  Campagne (ID, état, budget, couverture réelle, journaux)
      |
      v
  Cartographie Web et constats de risque + indications PHP / CVE
      |
      +--> données insuffisantes : demander preuve/version ou accès autorisé
      |
      v
  PDF/JSON/CSV : rapport et document de remédiation signable/révisable
      |
      v (transfert de constat approuvé, identité et mandat conservés)
PHPPATCH FRONTEND /remediations/<id>
  correctifs candidats runtime/config/dependency/code
      |
      v
  Diffs Git + plan de migration + sandbox Docker
      |
      v
  Lint, CI, tests de non-régression, revue humaine, approbation
      |
      +--> PR GitHub : pas d'écriture directe dans main
      |
      +--> déploiement uniquement via MCP existant, si autorisé
      |
      v
  preuves d'application / supervision / rollback gouverné
```

Les routes ci-dessus sont **proposées**, aucune UI ni API réelle ne les expose encore.

### Champs UI minimums (futurs)
- Projet/mandat existant, URL de départ, URL(s) supplémentaires importées ; type d'actif : tiers-métadonnées / administré avec preuve.
- Cases d'autorisation explicites et vérifiables par **responsable du périmètre** ; une simple case cochée n'est pas une preuve suffisante pour le niveau P2.
- Type d'audit : inventaire de métadonnées / crawl Web borné / audit code+runtime connecté, avec quotas.
- Connecteur de dépôt Git sous autorité GitHub App existante (lecture seule pour audit) ou environnement S1/Plesk gouverné.
- État, pages autorisées explorées, erreurs/limites, progression et bouton arrêter/reprendre, résultats et niveau de confiance.
- Panneau distinct « PHP2Shell / avis prioritaires » montrant *advisory_verified*, *potential_exposure*, *confirmed_applicability*, *insufficient_evidence*, *vendor_patched*, et origine des preuves.
- Export document de remédiation, boutons **Préparer un patch** / **Soumettre une revue** uniquement si permission et mandat suffisants.

## 3. Détection, preuves, prudence du diagnostic

Chaque constat comprend : `finding_id`, `campaign_id`, `asset_id`, URL/chemin ou fichier, date UTC, méthode, source de la preuve, règles versionnées, observations non sensibles, confiance, sévérité **sourcée si applicable**, avis de sécurité, statut de correspondance, correction suggérée et limitations.

Classes de résultat :
- `TECHNOLOGY_INDICATOR` : indice PHP visible, pas de vulnérabilité confirmée.
- `WEB_CONFIGURATION_FINDING` : configuration observable (headers/cookies/redirects) avec contexte et impacts, sans affirmation générale d'exploitabilité.
- `CVE_ADVISORY_VERIFIED` : l'avis CVE est authentique ; ne dit rien du site.
- `POTENTIAL_EXPOSURE` : hypothèse d'exposition, éléments manquants listés.
- `INSUFFICIENT_EVIDENCE` : version/runtime non attesté ou périmètre inaccessible.
- `CONFIRMED_APPLICABILITY` : produit/runtime/version/packaging et backports attestés **dans un environnement P2 autorisé**, corrélés aux avis officiels.
- `VENDOR_PATCHED` : correctif rétroporté attesté, ne pas recommander inutilement une version upstream au même titre.
- `REMEDIATION_PROPOSED`, `PATCH_TESTED`, `APPROVED`, `DEPLOYED`, `ROLLED_BACK` : états séparés et prouvés ; jamais déduits l'un de l'autre.

**Vulnérabilités PHP2Shell prioritaires :** demander la preuve de version moteur PHP réellement exécutée, SAPI et provenance du paquet/image ; comparer aux seuils correctifs officiels et révisions fournisseur. Le patch recommandé peut être **une mise à niveau du runtime**, pas un patch sur le HTML ou une simple édition `.php`.

## 4. Contrôles obligatoires contre les audits non autorisés et abus réseau

- **Admission avant crawl** : mandat opérationnel, catégorie P1/P2, liste de domaines exacte, modes autorisés, propriétaire/référent, expiration, quotas et audit log. Liste fournie dans un CSV **≠** autorisation.
- Mode P1 : métadonnées publiques déjà disponibles ; si des requêtes HTTP sont nécessaires, exiger leur admission explicite, faible débit et politique de respect de robots/directives applicables. Pas de test d'exploitation ni de brute-force, pas de recherche de chemins sensibles ou contournement.
- **Anti-SSRF** : n'autoriser que schémas HTTP/HTTPS, hôtes et ports expressément admis ; refuser URL credentials, hostnames/IP internes ou hors périmètre, loopback, link-local, multicast, endpoints de métadonnées ; contrôle DNS à chaque connexion et après redirection, protection contre DNS rebinding et changement d'IP.
- **Navigation bornée** : suivre uniquement les redirections et liens qui restent dans la portée exacte ; pas de soumission de formulaires, paiement, changement d'état, appels API non nécessaires, téléversement ni authentification implicite.
- Quotas par domaine et globalement : pages, profondeur, concurrence, requêtes/seconde, bytes, délai, retries et budgets temporels ; temps d'arrêt et annulation immédiate, priorité à la non-perturbation.
- Gestion des contenus malveillants dans des sandboxes sans secrets, stockage prudent des pages/artefacts, protection du navigateur headless éventuel.
- Ne pas confondre anonymat et droit d'audit : un site gouvernemental/bancaire reste tiers si aucun mandat explicite.

## 5. Architecture technique complémentaire (sans seconde plateforme/gateway)

| Composant | Responsabilité | Jalon |
|---|---|---|
| `frontend-url-audit` PHP2SHELL | Saisie URL, campagne, scopes, visualisation de couverture et rapports | V1.0, contrat V0.2 |
| `campaign-inventory` | CSV/JSON/TXT, normalisation/déduplication, validation DNS et quotas | V0.2/V1.0 |
| `passive-web-crawler` | Cartographie Web bornée, collecte de pages publiques uniquement si admises, sans exploit | V0.2 |
| `web-evidence-analyzer` | En-têtes, cookies, contenu visible, framework, confiance, configuration | V0.2 |
| `authorized-source-runtime-connector` | Dépôt Git exact SHA / environnement administré, PHP/Composer/config attestés sous P2 | V0.2/V0.4 |
| `cve-intelligence` | Catalogue PHP et fournisseurs, applicabilité, backports, scores sourcés | V0.2 |
| `report-remediation` | Document PDF/JSON/CSV, annexes de preuves et recommandations | V0.2/V1.0 |
| `frontend-phppatch` | Correctifs candidats, diffs, sandbox validation, workflow d'approbation | V0.3/V1.0 |
| `api-control-plane` + workers | FastAPI/PostgreSQL/Redis proposés, tâches bornées, journalisation, idempotence | V0.4/V1.0 |
| `governed-release-adapter` | GitHub→MCP existant→S1, sauvegarde, exact HEAD, claims/locks | V0.4 |

Les agents sont des **modules spécialisés de la plateforme PHP2SHELL** ; leur existence ne justifie ni une deuxième file d'autorité MCP, ni une seconde gateway, ni un accès SSH arbitraire.

## 6. Document de remédiation : contrat minimal de sortie

Rapport :
- Identité du projet, mandat, niveau et périmètre, horodatage, version des règles, algorithmes, nombre de pages **effectivement** visitées et pages exclues.
- Synthèse exécutive, risques par preuve et confiance, détails Web, technologies présumées vs attestées, présence ou absence de sources PHP autorisées, résumé CVE avec backports et niveau de certitude.
- Tableau des constats (ID, URL/fichier, impact, gravité sourcée, preuve, limites), diagnostic applicable/incertain, mesures de réduction du risque et urgence recommandée.
- Plan de remédiation classé (runtime PHP, paquets, configs, code), versions correctives officielles et prérequis opérationnels.
- Proposition de patch Git/diff **si accès P2 et revue**, tests de compatibilité/non-régression, sauvegarde et rollback.
- Annexe d'audit (empreintes et références privées aux preuves, succès/échecs de collecte, dates) sans code privé ni credentials dans un dépôt public.
- Export PDF/JSON/CSV ; signatures ou approbations et historique via outil gouverné.

## 7. Acceptation future / cas de tests obligatoires

1. **URL admise P2** : les pages découvertes restent sous périmètre, les résultats distinguent web vs code serveur et ne prétendent pas « toutes les pages » sans preuve.
2. **URL publique sans mandat** : pas de crawl actif ni de scan d'exploit ; possibilité d'enregistrer des métadonnées publiques déjà obtenues selon règle de portée.
3. **Redirection hors périmètre, DNS rebinding, IP privée/cloud metadata, URL avec credentials** : refus, arrêt et preuve; pas de connexion réalisée vers la destination interdite.
4. **Campagne volumineuse** : milliers de domaines fictifs et données synthétiques ; quotas/rate limits, pause, reprise, anti-doublons, arrêt et couverture documentée.
5. **Site PHP sans source/runtime** : `PHP_POSSIBLE` + `INSUFFICIENT_EVIDENCE`, jamais `CONFIRMED_APPLICABILITY` sur signature.
6. **Site P2 avec accès source et version runtime** : corrélation GHSA/CVE version corrigée/backport, justificatifs de pertinence, classification traçable.
7. **Site non-PHP / protections/403** : aucune vulnérabilité inventée ; zones non explorées signalées.
8. **Patch moteur PHP** : proposition de montée de version/runtime avec test de compatibilité et rollback, aucune mutation système sans approbation.
9. **Rapport PDF/JSON/CSV** : chiffres cohérents avec les preuves, pas de fuite d'identifiants, distinction hypothèse/constat.
10. **Passage PHP2SHELL → PHPPATCH** : mandat et finding ID conservés, droits indépendants et test négatif des privilèges.
11. **Échec partiel/reprise** : rapport incomplet explicitement marqué, tentatives et budget enregistrés, pas de succès fictif.
12. **Deux hôtes S1** : readiness DNS/TLS distincte de l'E2E fonctionnel ; les pages Plesk ne valident pas un déploiement.

## 8. Liens d'autorité

- Cahier des charges complet : `FOUNDING_SPECIFICATION.md`
- Matrice des exigences : `REQUIREMENTS_TRACEABILITY.md`
- Registre des sources officielles PHP/CERT : `CVE_SOURCE_REGISTER.md`
- Feuille de route à 5 versions : `docs/ROADMAP.md` sur PR #2
- Architecture Docker cible : `deploy/S1_DOCKER_ARCHITECTURE.md` sur PR #3
- Reprise et checkpoints : issue #5 / PR #6

**Cette spécification est additive et doit être intégrée dans les futures tranches d'implémentation avec ses tests ; elle ne déclare aucun crawler, backend, patch ou interface déjà opérationnel.**
