# Architecture PHP2SHELL

## Objectif
Réduire les risques PHP dans les actifs autorisés, de la qualification des versions jusqu'à une remédiation gouvernée. Le prototype actuel n'effectue que des opérations déterministes hors ligne.

## Flux V0.1
1. L'opérateur fournit un fichier JSON local ou une version PHP.
2. `app/cli.py` analyse les arguments.
3. `app/core.py` valide les noms d'hôte et les portées ou compare les versions.
4. Le résultat est écrit en JSON sur stdout. Aucun stockage ni trafic réseau.

## Modules
- `Target` : validation d'un nom DNS et de la preuve déclarative en portée `owned_source`.
- `load_targets` : chargement de la liste JSON.
- `inventory` : restitution de la portée, sans découverte de sites.
- `parse_version` / `evaluate` : comparaison de versions, avec données de démonstration non certifiées.
- `tests/` : tests de comportement et de rejet d'entrées.

## Frontières de confiance
Les fichiers d'inventaire sont non fiables : ne jamais y interpréter de commandes ou d'URL. La preuve d'autorisation est une simple chaîne, pas un jeton de privilège. Aucun processus distant, scanner réseau ou moteur de patch n'existe dans cette version.

## Architecture cible (non implémentée)
Registre d'actifs et mandats -> catalogue d'avis sourcés -> analyseurs locaux autorisés -> moteur de propositions de patch -> banc de tests -> approbation humaine -> déploiement contrôlé -> audit et rollback. Chaque transition nécessitera des preuves et des permissions minimales.
