# Interfaces — prototypes locaux

## PHP2SHELL

`web/php2shell/index.html` constitue une première maquette statique du parcours de saisie d'URL. Le fichier `web/shared/url-preview.js` fournit un retour immédiat sur la syntaxe et le budget demandé.

Ce prototype **ne contacte aucun site**, ne transmet aucune demande à une API et n'authentifie aucun utilisateur ou mandat. Le bouton d'audit reste désactivé ; un champ de portée P2 n'accorde aucun droit.

La validation JavaScript sert uniquement à l'expérience utilisateur. La future API devra refaire toutes les validations côté serveur et les compléter par l'autorité MCP existante, la sécurité de la connexion réseau, les limites de navigation, le suivi des sessions et les autorisations P1/P2.

## Étapes ultérieures

La console de remédiation séparée, le backend FastAPI, l'authentification/RBAC, PostgreSQL, Redis, les workers, le diagnostic Web autorisé et les rapports complets sont des tâches distinctes qui ne sont pas livrées par ces fichiers HTML.

Ne pas confondre cette maquette avec une interface installée sur S1.

## Contrôles

`tests/test_frontend_static.py` vérifie notamment l'absence d'action réseau dans le prototype, les boutons inactifs et les restrictions du document.

Le code existant du moteur PHP2SHELL est conservé sans modification de sa gouvernance.
