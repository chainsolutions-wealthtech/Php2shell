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

## Parcours débutant — écran simplifié, progressif (P2S-UX-001)

L'accueil PHP2SHELL montre désormais **trois étapes sans jargon** : « Indiquez votre site », « Choisissez votre analyse », « Consultez votre résultat ». Les options de portée sont exprimées comme actions compréhensibles : « Vérifier les informations publiques de mon site » et « Analyser le code de mon site (accès autorisé nécessaire) ». Les valeurs de portée, les limites et les validations sont conservées pour éviter toute régression. Les budgets et distinctions P1/P2 restent disponibles dans un panneau de paramètres avancés.

**La première prévisualisation est utilisable sans inscription et sans requête réseau.** Le prototype ne prétend ni connecter un utilisateur ni contrôler ses droits : il n'existe toujours aucun bouton de connexion, de crawl ou de correction actif. Les étapes nécessaires avant une opération réelle sont annoncées clairement, et toutes les opérations sensibles restent désactivées.

### Parcours futur souhaité, non implémenté

1. Visiteur : saisit l'adresse de son site et choisit le type d'analyse en langage courant ; aucun jargon MCP/P1/P2.
2. Pour un audit réel : connexion simple à un fournisseur d'identité approuvé, **une seule session pour les deux consoles**.
3. Vérification des droits : connecter un dépôt GitHub autorisé pour le code, ou fournir une autre preuve/mandat adapté à l'actif. Un domaine public n'est pas automatiquement autorisé ; une case cochée ou la seule connexion ne valent pas preuve.
4. Après contrôle du périmètre exact et de l'autorisation, lancer uniquement l'analyse autorisée, avec quotas et sécurité réseau, puis présenter un rapport en français courant.
5. PHPPATCH : proposer un correctif à partir du dossier admis et, uniquement sous autorisation distincte, faire approuver tests, application et déploiement.

**Objectif : la complexité de l'authentification, des mandats et du MCP doit être gérée par le backend, pas saisie manuellement par le public.** Aucun fournisseur n'est choisi ou déclaré connecté par cette documentation ; aucun endpoint de session, worker réseau, accès source ou déploiement n'est ajouté.
