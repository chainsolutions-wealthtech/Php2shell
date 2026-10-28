# Interfaces — prototypes locaux

## PHP2SHELL

`web/php2shell/index.html` constitue une première maquette statique du parcours de saisie d'URL. Le fichier `web/shared/url-preview.js` fournit un retour immédiat sur la syntaxe et le budget demandé.

Ce prototype **ne contacte aucun site**, ne transmet aucune demande à une API et n'authentifie aucun utilisateur ou mandat. Le bouton d'audit reste désactivé ; un champ de portée P2 n'accorde aucun droit.

La validation JavaScript sert uniquement à l'expérience utilisateur. La future API devra refaire toutes les validations côté serveur et les compléter par l'autorité MCP existante, la sécurité de la connexion réseau, les limites de navigation, le suivi des sessions et les autorisations P1/P2.

## PHPPATCH — aperçu statique de revue

`web/phppatch/index.html` est une **seconde console distincte**, ajoutée de façon additive, sans serveur ni API. Elle présente les portes de revue nécessaires pour recevoir un futur dossier de PHP2SHELL : autorisation P2 authentifiée, provenance des preuves, PHP/SAPI et backports vérifiés, pertinence CVE, diff candidat, tests Docker isolés, revue indépendante et rollback.

**Tous les boutons sont désactivés.** La page ne possède ni script, ni formulaire, ni chargement réseau. Elle n'importe pas les dossiers locaux et ne reflète pas l'état d'un projet réel. Le module `app/dossier_handoff.py` reste un contrat de file de revue hors ligne non authentifié, sans liaison Web. Aucun statut de correctif, d'approbation ou de déploiement n'est promu.

## Étapes ultérieures

Le backend FastAPI, l'authentification/RBAC, PostgreSQL, Redis, les workers, le diagnostic Web autorisé, les rapports complets, les diffs candidats et les tests de patches en sandbox restent des tâches distinctes non livrées par ces fichiers HTML.

Les deux destinations S1 restent `php2shell.wealthtechinnovations.com` et `phppatch.wealthtechinnovations.com`, sous Docker isolé et un moteur commun **à construire**. Ne pas confondre ces maquettes avec des interfaces installées sur S1.

## Contrôles

`tests/test_frontend_static.py` et `tests/test_phppatch_frontend_static.py` vérifient l'absence d'action réseau, les boutons inactifs, la CSP et la séparation des deux consoles.

Le parcours URL → audit autorisé → diagnostic → PHPPATCH, les 6 lots, 32 exigences, 61 work packages et V0.1→V1.0 restent intégralement au programme. Le code existant du moteur PHP2SHELL est conservé sans modification de sa gouvernance.
