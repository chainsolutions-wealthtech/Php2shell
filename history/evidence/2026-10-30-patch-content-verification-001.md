# Contrôle probatoire des patchs — première tranche vérifiée (2026-10-30)

**Continuité unique :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**PR :** https://github.com/chainsolutions-wealthtech/Php2shell/pull/7  
**HEAD observé avant vérification :** `5aeec9e6d6d001b6e205e4ecdd3658c16c54852d`  
**Objet :** intégrité du contenu des dossiers de diff, et non simple existence du nom de fichier.

## Méthode réellement exécutée

Pour chacun des trois SHA ci-dessous, récupérer depuis GitHub le commit et sa liste de patchs par fichier, récupérer le dossier Markdown de diff au HEAD indiqué, puis vérifier que **chaque chaîne de patch retournée par GitHub** figure textuellement, à l'identique, dans le dossier archivé. Vérifier également le nombre de blocs `diff` et de fichiers retournés. Il s'agit d'une comparaison de chaînes sur les réponses du connecteur, non d'un audit cryptographique indépendant.

## Résultats individuels

| SHA complet | Fichiers/patchs GitHub | Patchs présents à l'identique | Blocs diff | Résultat |
|---|---:|---:|---:|---|
| `0adc473c8b03e37ad7ad3c99ce8b84cc382dbeca` | 2 | 2 | 2 | PASS |
| `03b45fdc2cf40e3276208935b47a785ef320a27d` | 3 | 3 | 3 | PASS |
| `fe3a61f81009657cc2877c627f8862785c747cf5` | 1 | 1 | 1 | PASS |

Sources primaires :
- https://github.com/chainsolutions-wealthtech/Php2shell/commit/0adc473c8b03e37ad7ad3c99ce8b84cc382dbeca
- https://github.com/chainsolutions-wealthtech/Php2shell/commit/03b45fdc2cf40e3276208935b47a785ef320a27d
- https://github.com/chainsolutions-wealthtech/Php2shell/commit/fe3a61f81009657cc2877c627f8862785c747cf5

## Portée et limites

**3 dossiers contrôlés sur les 363 du snapshot historique ; 6 patchs comparés, 6 correspondances exactes.** Les **360 autres dossiers ne sont pas certifiés** par cette opération. Les éléments non exposés par le connecteur, la provenance indépendante des blobs, la vérification exhaustive des jobs CI, les opérations S1/Plesk et la reconstitution des conversations restent `NOT_VERIFIED` tant qu'aucune preuve spécifique ne les atteste.

Ce fichier complète l'archive existante sans modifier les faits historiques ni le code applicatif. Il ne crée aucun nouveau programme, jalon fonctionnel, mandat ou tâche : il conserve simplement la preuve de vérification déjà exécutée pour l'objectif initial de reconstruction intégrale.
