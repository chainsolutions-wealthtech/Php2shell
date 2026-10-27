# Guide d'utilisation

## Installation
Installer Python 3.10 ou plus récent et cloner le dépôt. Aucun `pip install` n'est nécessaire. Depuis la racine du dépôt, exécuter `python -m unittest discover -s tests -v`.

## Inventaire fictif
`python -m app.cli inventory --file lab/targets.json`

Le fichier doit être un tableau JSON d'objets ayant `hostname` et `scope`, avec `evidence` non vide pour `owned_source`. Les domaines `.example` sont fictifs. Une entrée invalide déclenche une erreur et le programme s'arrête; il ne tente aucune connexion.

## Comparaison de version
`python -m app.cli check-version --php 8.3.34`

La version doit suivre exactement le format numérique `majeure.mineure.correctif`. Les statuts retournés sont `below_reference_fix`, `at_or_above_reference_fix` et `review_vendor_support`. **Ces statuts ne sont pas des diagnostics de vulnérabilité.** Les seuils d'exemple ne sont pas validés.

## Docker
`docker build -t php2shell .` puis `docker run --rm php2shell` pour le CLI. `docker compose --profile lab build` construit la fixture PHP, sans publication de port. Le Dockerfile de fixture utilise `php:8.3-cli`, **une étiquette mouvante qui ne garantit aucune version corrective précise**. Selon le registre ou le cache local, l'image peut correspondre à différentes versions correctives de PHP 8.3. Pour identifier la version réellement utilisée, exécuter `docker compose --profile lab run --rm lab php -v` uniquement sur le laboratoire local (vérifier le nom du service avec `docker compose config --services`). Pour un scénario de validation reproductible, épingler une image par digest et attester `php -v` ; ne jamais interpréter la construction de cette fixture comme une preuve d'absence de vulnérabilité.

## CI
La workflow `.github/workflows/ci.yml` exécute les tests unitaires sur les pushes et pull requests. Elle n'a qu'un accès `contents: read`. Consulter l'onglet Actions du dépôt.

## Limites et dépannage
- `No module named app` : lancer depuis la racine du dépôt.
- Erreur JSON : vérifier le format de `lab/targets.json`.
- `Expected numeric PHP version X.Y.Z` : retirer suffixes et caractères supplémentaires.
- `Owned-source scope requires authorization evidence` : fournir une preuve déclarative, puis faire vérifier l'autorisation hors de l'outil.
- Pas de découverte de PHP, pas de collecte HTTP, pas d'accès SSH, pas de correctif appliqué.
