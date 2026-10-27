# Mission métier et fonctionnement visé de PHP2SHELL / PHPPATCH

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
