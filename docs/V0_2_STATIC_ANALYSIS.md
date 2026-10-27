# PHP2SHELL V0.2 — analyse locale en lecture seule

Commande : `python -m app.cli scan-local --path /chemin/vers/projet-autorise`.

Le moteur inventorie les fichiers PHP locaux et les exigences `composer.json`. Il signale les appels à `eval`, `unserialize` et certaines fonctions de commande système comme **indices à examiner**, sans exécuter le code et sans accéder au réseau.

Limites : analyse par expressions régulières, sans AST, sans analyse de flux de données, sans validation de CVE ni confirmation d'exploitabilité. Les fichiers de plus de 2 Mo sont ignorés et le nombre de fichiers PHP est limité à 5 000. Les répertoires `vendor`, `node_modules`, `.git` et les liens symboliques sont exclus.

Sécurité : ne scanner que des sources détenues ou explicitement autorisées. Les résultats ne doivent pas être interprétés comme une preuve de vulnérabilité. Aucun correctif ni déploiement automatique n'est réalisé.

Prochaines étapes : parser PHP AST, gestion de sources et dépendances versionnées, règles sourcées, analyse des configurations, export SARIF, tests de non-régression et validation indépendante.
