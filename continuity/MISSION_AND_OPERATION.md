# Mission métier et fonctionnement visé de PHP2SHELL / PHPPATCH

**Continuity ID:** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Ancre durable:** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5

**Mandat permanent :** protéger des applications PHP sur lesquelles l'opérateur dispose d'une autorisation explicite. La plateforme doit produire des analyses reproductibles, expliquer ses constats, préparer des propositions de correction et aider à valider leur sécurité **sans appliquer de correctif en production de façon autonome**.

## Cycle métier fonctionnel attendu

1. **Enregistrer les projets** : actifs, dépôt/source autorisée, propriétaire, autorisation et portée, date de validité et responsable de décision. Des listes publiques de noms de domaine peuvent être documentées passivement, mais **n'autorisent jamais à scanner du code distant ni à exploiter un tiers**.
2. **Inventorier l'environnement** : identifier dans les sources détenues la présence de PHP, versions déclarées, `composer.json` et `composer.lock`, dépendances et configurations `php.ini`, `.user.ini`, Apache/Nginx, etc. Un inventaire de versions ne constitue pas un test d'exploitation.
3. **Analyser localement** : règles déterministes + parseur PHP solide/AST + analyse des dépendances/configurations, puis recherche de preuves contextualisées (fichier/ligne/symbole, niveau de confiance, limites, origine). V0.2 actuelle : seulement **indicateurs lexicaux**, non une analyse complète.
4. **Rapprocher les avis officiels** : sources PHP/fournisseurs de paquets/NVD/CVE pertinentes, dates, versions, branche/distribution et correctifs rétroportés ; absence de vérification = `non_verifie`, pas de déclaration de CVE confirmée. Les CVE d'exemple du prototype restent non vérifiées.
5. **Qualifier le risque** : preuve, gravité *sourcée*, incertitude, faux positifs et contexte, décision humaine de qualification.
6. **Préparer des remédiations** : correctifs proposés sous forme de diff minimal et explicable, sans écriture silencieuse sur le dépôt ou la production ; versions de bibliothèque, réglages et code avec procédures de migration si justifiées.
7. **Valider en environnement isolé** : lint, unitaires, intégration, non-régression, analyse sécurité et vérification avant/après ; conteneurs Docker éphémères, sans secrets prod, rollback préparé.
8. **Faire approuver et publier** : séparation auteur/réviseur, mandat et autorité, PR GitHub sous branche dédiée, CI au HEAD et contrôle de non-régression.
9. **Déployer seulement si autorisé** : GitHub → MCP *existant* (session/claim/lock/permission/trace) → S1 ; sauvegarde, test de santé, observation et rollback. Pas de second gateway ni reprise d'autorité GRT.
10. **Superviser et archiver** : tableau de bord, historique des décisions, rapports JSON/PDF, preuves, interventions, alertes et suivi jusqu'à résolution.

## Contrat fondateur conservé dans son intégralité

Ce cycle à dix étapes **n'abolit pas** les besoins initiaux plus détaillés : campagnes de **centaines à milliers de domaines**, imports `CSV/JSON/TXT`, normalisation/déduplication, **identification PHP passive** et détection de frameworks avec preuves/confiance, niveaux séparés `public_metadata` et `owned_source`/mandats, CVE Intelligence, analyse locale approfondie `composer.lock`/configs, attestation du runtime et SAPI, propositions de mises à jour de PHP et correctifs Git, validation Docker isolée, **Python/FastAPI/PostgreSQL/Redis/workers**, rapports PDF/CSV/JSON, historique et supervision.

Ces besoins et les **six lots historiques** sont conservés dans [`FOUNDING_SPECIFICATION.md`](FOUNDING_SPECIFICATION.md), chacun relié aux cinq versions et à une preuve de livraison par [`REQUIREMENTS_TRACEABILITY.md`](REQUIREMENTS_TRACEABILITY.md). Le code existant ne prétend pas encore réaliser les composants non implémentés.

**CVE prioritaires** : CVE-2026-109618 et CVE-2026-109619 sont officiellement décrites par PHP/CERT-FR depuis le 21/10/2026 ; référence et seuils amont documentés dans [`CVE_SOURCE_REGISTER.md`](CVE_SOURCE_REGISTER.md). L'ancien texte de prototype qualifiant ses seuils de « démonstration/non vérifiés » décrit **l'absence de source automatisée et de qualification par actif dans le logiciel**, et non l'inexistence des CVE. Un statut réel d'exposition nécessite version runtime, paquet/distribution, SAPI, config et backports.

## Parcours utilisateur supplémentaire : saisie URL → audit Web → dossier → PHPPATCH

À conserver intégralement en complément : depuis la console PHP2SHELL, saisir une URL, choisir un projet/mandat, explorer les pages **autorisées** selon des budgets et suivre la couverture réelle ; analyser les observations Web (HTML, JS public, headers, cookies, redirections, indices PHP) et la correspondance avec les CVE officiellement documentées, **sans annoncer de vulnérabilité confirmée d'après une URL seule**. Lorsque le propriétaire a autorisé la lecture du dépôt ou du serveur, enrichir avec les sources PHP, Composer, configs, version runtime réelle et backports. Produire un rapport PDF/JSON/CSV et passer dans **PHPPATCH** pour un patch candidat et ses tests/approbations sans installation automatique.

**Spécification :** [`URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md`](URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md), **REQ-023→REQ-032**. Il n'existe pas encore d'interface ni de crawler opérationnel.

## Deux interfaces, une plateforme

- **php2shell.wealthtechinnovations.com** : analyse, inventaire, projet, risque, preuves, rapports et supervision.
- **phppatch.wealthtechinnovations.com** : proposition de patch/diff, CI, revue, approbation, validation isolée et rollback.
- Tous deux sont prévus sur **S1 / Plesk** ; un moteur API, un registre de mandats et un audit communs. Les conteneurs/frontends et permissions sont séparés. Le DNS et les certificats existent mais l'application n'est pas déployée.

## Roadmap non régressive

- V0.1 **Fondations** : CLI, tests, documentation (PR #1).
- V0.2 **Analyseur PHP** : source, Composer, dépendances réelles/config, preuves/confiance et avis officiels (PR #2 partielle).
- V0.3 **Remédiation** : propositions de patch, tests automatiques isolés, diff et rollback (à construire).
- V0.4 **MCP/S1/Docker** : contrôles d'accès, connecteurs et déploiement gouverné, conteneurs isolés (PR #3 = préparation uniquement).
- V1.0 **Plateforme Web complète** : projets, rapports, historique, supervision, approbations (à construire).

L'architecture technique détaillée existante réside dans les docs des PR #2 et #3, et ce dossier de continuité ne doit pas devenir une deuxième spécification contradictoire.

## Règles de sûreté durables

- Autorisation forte, périmètre local vérifiable ; aucun test actif sur sites tiers non mandatés.
- Toujours distinguer : motif ≠ vulnérabilité ; seuil de version ≠ CVE vérifiée ; HTTP 200 ≠ application ; CI ≠ revue sécurité ; proposition ≠ correctif appliqué.
- Zéro secrets, tokens, clefs ou source privée dans ce dépôt **public**, dans les issues et dans les logs de reprise.
- Aucune régression : conserver les protections, tests, décisions et historique ; préférer extensions compatibles + PR revue plutôt que remplacement destructeur.
- Journaliser décisions, activités, révisions, preuves et NEXT_ACTION dans les fichiers de `continuity/` et l'issue #5.
