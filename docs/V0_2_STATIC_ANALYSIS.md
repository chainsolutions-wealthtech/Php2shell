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

## Analyse locale des configurations PHP / PHP-FPM (ajout V0.2)

La commande existante \`scan-local\` examine maintenant des fichiers de configuration locaux, **sans requête réseau ni lecture de paramètres de production** :

- \`php.ini\`, \`.user.ini\`, \`php-fpm.conf\` ainsi que les \`*.conf\` des répertoires \`pool.d\` et \`php-fpm.d\` sous la racine autorisée.
- Règles heuristiques sur des valeurs booléennes **explicites** pour \`expose_php\`, \`display_errors\`, \`allow_url_include\`, \`session.cookie_httponly\`, \`session.cookie_secure\` et \`session.use_strict_mode\`. Les syntaxes inconnues et valeurs variables ne sont **pas** interprétées.
- Le nouveau champ \`php_configuration\` regroupe \`config_files_examined\`, \`config_indicators\`, \`config_skipped\`, \`limitations\`. Chaque indicateur fournit **le chemin relatif, la ligne, l'identifiant de règle, un niveau de gravité indicatif et \`review_required\`**, jamais une valeur brute de configuration.
- Refus des symlinks, exclusion des dossiers de dépendances, plafond 100 fichiers de configuration et 1 Mo par fichier. Les fichiers invalides ou illisibles sont mentionnés comme ignorés.
- Les **configurations présentes sur disque ne prouvent pas leur chargement par la SAPI PHP active**, et leurs éventuelles surcharges via \`php_admin_value\`, Plesk ou pool FPM ne sont pas résolues automatiquement. Aucun finding ne doit être promu en vulnérabilité confirmée sur ce seul indice.
- Les secrets, mots de passe, URLs d'accès, autres paramètres et commentaires des configurations restent exclus du JSON. Aucun correctif n'est appliqué automatiquement.

**Préparation de REQ-008 uniquement :** le scanner ne remplace pas une attestation de \`php -i\`/\`php-fpm -tt\`, de la configuration effective d'une instance autorisée, ni une revue des règles de sécurité contextuelles.

## Export CSV des constats locaux — étape complémentaire V0.2

```bash
python -m app.cli scan-local --path /chemin/vers/projet-autorise --format json
python -m app.cli scan-local --path /chemin/vers/projet-autorise --format csv
```

- `json` reste **le format par défaut**, avec les anciens champs, `locked_dependencies` et `php_configuration`. Ce comportement n'est pas remplacé.
- `csv` produit un **inventaire des indicateurs uniquement**, composé des champs `finding_type,rule,severity,confidence,path,line,note` ; les constats lexicaux PHP et les réglages PHP ini sont différenciés par `finding_type`. Le CSV est écrit sur **stdout**, sans fichier ajouté au disque.
- La sortie CSV ne contient **ni code source, ni valeurs brutes de configuration, ni secrets, ni chemin absolu du projet**. Les contenus susceptibles d'être interprétés comme une formule par un tableur sont préfixés de manière protectrice.
- Cet export ne représente **pas encore** un dossier de remédiation PDF complet, ne déduit pas l'applicabilité réelle d'une CVE, et n'exécute aucun correctif.

Les vérifications de confidentialité, de compatibilité de la sortie JSON, de validation des formats et d'injection de formules CSV sont couvertes par la CI.

## Catalogue officiel PHP sourcé — instantané hors ligne V0.2

Les identifiants CVE-2026-109618 et CVE-2026-109619, les bulletins PHP du **21 octobre 2026** et l'alerte **CERTFR-2026-ALE-014**, dernière version constatée le **27 octobre 2026**, ont été vérifiés auprès de l'éditeur et du CERT-FR. Cela **corrige la qualification historique** « données d'exemple non vérifiées » qui s'appliquait au prototype V0.1 et à l'absence d'un pipeline de provenance. Ce changement **n'atteste aucun actif**. Les correctifs PHP amont de référence sont 8.2.35, 8.3.36, 8.4.27 et 8.5.12.

Fichiers nouveaux :
- `app/data/php_security_advisories.json` : instantané local daté `2026-10-28`, avec GHSA, CVE, score, source PHP primaire et CERT-FR, et seuils PHP par branche.
- `app/security_advisories.py` : validation stricte de l'identité, des dates, des URLs HTTPS officielles, des seuils, des doublons et des avertissements obligatoires. **Lecture locale uniquement**, pas de réseau ni de synchronisation automatique.
- `tests/test_security_advisories.py` : seuils, versions non couvertes, double provenance, refus d'URLs falsifiées, de doublons et d'entrées invalides, absence de requêtes réseau et compatibilité des commandes historiques.

Commandes ajoutées **sans modifier** `check-version` :

```bash
python -m app.cli advisories
python -m app.cli review-version --php 8.3.34
```

`advisories` expose les références officiellement publiées, mais le fichier local reste un **instantané**, jamais un flux CVE à jour automatiquement. `review-version` retourne `below_reference_fix`, `at_or_above_reference_fix` ou `review_vendor_support` selon une **version déclarée**, avec `asset_applicability: insufficient_evidence` dans tous les cas. Aucune source ni URL publique ne permet à elle seule d'attester le runtime PHP réellement exécuté ou les correctifs rétroportés par un fournisseur.

**Règle de non-régression :** le comportement et la sortie de `python -m app.cli check-version --php ...` restent inchangés. Les anciennes données et commentaires de démonstration restent dans les versions précédentes pour la traçabilité ; le nouveau catalogue sourcé ne doit jamais être confondu avec une validation automatique de toutes les CVE, des nouvelles versions ou d'un serveur public.

Sources :
- [PHP — GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w).
- [PHP — GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp).
- [CERT-FR — CERTFR-2026-ALE-014](https://www.cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-014/).

**Prochain jalon technique :** acquisition automatisée et gouvernée des avis en provenance des sources officielles, réconciliation des versions fournisseur, puis attestation P2 du runtime en production avec permissions vérifiées ; ne jamais utiliser ce snapshot pour établir seul une vulnérabilité exploitable.
