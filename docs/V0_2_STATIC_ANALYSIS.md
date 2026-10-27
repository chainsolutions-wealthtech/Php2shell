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

## Import de campagnes local V0.2 (ajout non intrusif)

Le prototype expose maintenant **une prévisualisation hors ligne** de listes de domaines, sans DNS, HTTP ni audit de site :

```bash
python -m app.cli import-targets --file ./targets.json
python -m app.cli import-targets --file ./targets.csv
python -m app.cli import-targets --file ./targets.txt
```

- JSON : tableau d'objets `{"hostname":"demo.example","scope":"public_metadata"}` ou `{"hostname":"owned.example","scope":"owned_source","evidence":"declaration"}`.
- CSV : en-têtes obligatoires `hostname,scope` ; colonne `evidence` optionnelle, requise avec une valeur non vide pour `owned_source`.
- TXT : **un domaine par ligne**, lignes vides et commentaires `#` ignorés ; attribue uniquement `public_metadata`, jamais de promotion implicite P2.
- Normalisation DNS cohérente avec `Target` ; doublons exacts fusionnés ; doublons avec scopes ou preuves divergents rejetés ; entrée non valide rejetée.
- Maximum 10 000 lignes et 5 Mo ; refus des fichiers de saisie symboliques. La commande `inventory --file` originale reste inchangée (JSON).
- Retour JSON : `rows_received`, `unique_targets`, `duplicates_removed`, `targets`, limites et origine du format. **Les `scope` et `evidence` sont déclaratifs, PAS une preuve d'autorisation vérifiée.**
- Les imports constituent une préparation de **REQ-001** : ni stockage durable de campagnes, ni crawler, ni scanner distant, ni ordonnanceur ne sont encore construits. Toute collecte Web future requiert admission réelle de mandat/portée avant une requête.

Tests : `python -m unittest discover -s tests -v`.

## Versions verrouillées Composer (ajout V0.2)

`scan-local` examine désormais également `composer.lock`, **uniquement dans le répertoire de projet local autorisé** : extraction des noms et versions verrouillées pour `packages` et `packages-dev`, sans installation, exécution PHP, DNS ou réseau. Les URL Git privées, informations d'origine des paquets, dist/source, références potentiellement sensibles et secrets présents dans le lockfile **ne sont pas recopiés** dans le résultat JSON.

Les nouveaux champs sont `composer_lock_present` et `locked_dependencies` (objets `name`, `locked_version`, `dependency_group`). Les fichiers symboliques, manifestes mal formés, plus de 2 Mo ou plus de 5 000 paquets sont refusés ou ignorés avec indication dans `skipped`. Les règles lexicales PHP et la lecture antérieure de `composer.json` sont conservées.

**Une version verrouillée dans `composer.lock` n'atteste ni une installation effective en production, ni l'applicabilité d'une CVE.** Un diagnostic de vulnérabilité sur l'environnement réel exigera la preuve des versions réellement installées, des backports fournisseurs et des configurations d'exécution sous mandat P2.
