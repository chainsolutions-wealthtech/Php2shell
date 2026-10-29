# V0.2 — Contrôle local de cohérence Composer (sans diagnostic CVE)

**Statut :** module autonome de revue hors ligne, non branché à une autorisation P2 ou un scanner réseau. Complète `scan-local` sans modifier sa sortie JSON/CSV, ses tests ou les interfaces PHP2SHELL/PHPPATCH.

```bash
python -m app.composer_consistency --path /chemin/vers/projet-php-explicitement-autorise
```

Le module lit seulement `composer.json` et `composer.lock` sous la racine locale déclarée. Il compare les noms de dépendances directes déclarées aux noms présents dans les deux groupes du lockfile, relève les doublons et compare uniquement les contraintes *exactes* simples (par exemple `1.2.3` ou `v1.2.3`). Les contraintes Composer comme `^1.2`, `~2`, alias, branches et références de développement **ne sont pas résolues**. Les packages de plateforme PHP/extensions sont exclus de la comparaison des noms. Un package virtuel indiqué dans `provide` ou `replace` reste « à examiner », jamais déclaré absent avec certitude.

Les observations sont des **indices `review_required`**, pas des vulnérabilités. La présence du lockfile n'atteste pas l'installation en production. Aucune version runtime PHP, SAPI, backport fournisseur, CVE applicable, autorisation d'accès ou mandat MCP n'est attesté. Aucun paquet n'est installé, aucune commande Composer/PHP n'est exécutée, aucun réseau n'est contacté et aucun patch n'est généré.

## Confidentialité et bornes

- Fichiers locaux réguliers seulement ; liens symboliques finaux refusés (ouverture `O_NOFOLLOW` sur les plateformes compatibles).
- Lecture plafonnée à 2 Mo par fichier et 5 000 entrées verrouillées ; JSON à clés dupliquées refusé.
- Aucune URL `source`/`dist`/`repositories`, aucun identifiant d'accès, aucune contrainte complète ni chemin absolu ne figure dans le rapport.
- Les noms de packages valides sont affichés pour revue ; **ne pas publier de rapport contenant des noms privés de dépendances sans autorisation**.
- Sortie bornée à 200 observations, avec indicateur de troncature. Le contrôle ne remplace pas une sandbox hostile de filesystem, ni une signature d'artefact Composer.

## Tests et intégration

`python -m unittest discover -s tests -v` inclut les tests de cohérence. Cette tranche est **additive** : elle ne change ni `scan-local`, ni le moteur commun, ni les deux consoles, ni la trajectoire URL → audit explicitement autorisé → PHPPATCH. La prochaine étape peut intégrer le rapport au dossier d'audit, **après** décision de contrat, autorisation de lecture locale et revue de confidentialité.
