# PHP2SHELL V0.2 — analyse locale en lecture seule

Commande : `python -m app.cli scan-local --path /chemin/vers/projet-autorise`.

## Comportement implémenté

- Analyse hors ligne des fichiers PHP locaux (`.php`, `.phtml`, `.inc`) et des contraintes déclarées dans `composer.json`.
- Signale certains appels sensibles (`eval`, `unserialize`, `shell_exec`, `system`, `passthru`, `exec`) comme **indices à examiner** : un motif lexical ne prouve pas une faille.
- Masque les zones de HTML hors PHP, les commentaires `//`, `#`, `/* ... */`, les chaînes simples/doubles/backticks ainsi que les blocs heredoc/nowdoc courants. Les numéros de ligne sont préservés.
- Exclut les liens symboliques ainsi que les répertoires `vendor`, `node_modules`, `.git`, `.venv`, `__pycache__`. Maximum 5 000 fichiers PHP ; les fichiers de plus de 2 Mo sont ignorés.
- Retourne un rapport JSON avec `schema_version: "0.2"`, `scanned_php_files`, `findings`, `composer_requirements`, `skipped`, `limitations`.
- Ne modifie pas les sources, n'exécute pas de PHP, n'accède pas au réseau, n'installe rien et ne produit aucun patch.

## Autorisation et sécurité

Scanner **exclusivement** des répertoires locaux détenus ou explicitement autorisés par le responsable de l'actif. La CLI ne vérifie pas l'identité du propriétaire : le contrôle d'autorisation doit être effectué en amont. Ne pas publier des analyses de code privé ni les chemins locaux sensibles.

## Limites importantes

Le moteur utilise une analyse lexicale conservative, et **non** un AST PHP complet. Les syntaxes non couvertes ou ambiguës peuvent générer des faux positifs et des faux négatifs. Il n'y a pas d'analyse de flux de données, de configuration runtime, de dépendances résolues, d'exploitabilité ni de confirmation de CVE. Les valeurs de `composer.json` sont des contraintes déclarées, pas des versions installées.

Les identifiants CVE et versions de référence figurant dans la V0.1 sont des **données d'exemple non vérifiées**. Ils ne doivent pas déclencher de remédiation automatique.

## Contrôle

`python -m unittest discover -s tests -v`

La V0.2 ajoute des tests de masquage lexical, d'exclusion des dépendances, de liens symboliques et de conservation des lignes. La CI est obligatoire avant approbation.

## Jalons suivants

1. Analyse syntaxique PHP réelle / vérification des cas limites.
2. Avis de sécurité sourcés, horodatés, versionnés et vérifiés.
3. Preuves d'autorisation et registres de mandats (distincts de la simple mention `--path`).
4. Exports de rapports et revues indépendantes avant toute remédiation.
5. API sécurisée et déploiement gouverné après autorisation de production.
