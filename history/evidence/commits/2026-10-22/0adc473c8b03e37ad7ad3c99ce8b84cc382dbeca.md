# Commit 0adc473c8b03e37ad7ad3c99ce8b84cc382dbeca — fondation du dépôt

**Continuité immuable :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Nature :** fiche individuelle de preuve Git, non action applicative nouvelle.  
**Source primaire :** [commit GitHub exact](https://github.com/chainsolutions-wealthtech/Php2shell/commit/0adc473c8b03e37ad7ad3c99ce8b84cc382dbeca).  
**Date GitHub observée :** 2026-10-22 à **16:40:40 UTC**.  
**Message Git :** `Initial commit`.  
**Auteur GitHub rapporté par le connecteur :** `Patricked-code` ; **committer :** `web-flow`. Les identités GitHub ainsi affichées ne démontrent pas, à elles seules, qui a personnellement rédigé les deux fichiers.  
**Statut de preuve :** `OBSERVED_IN_GITHUB` pour le SHA, la date, le message, les fichiers et les lignes du diff ; `REPORTED_IN_CANONICAL_LOG` pour le contexte d'origine ; `NOT_VERIFIED` pour les opérations hors Git.

## Fichiers introduits et vérification des changements

### 1. `.gitignore` — fichier ajouté ; 149 lignes

Le diff du commit ajoute un fichier d'exclusions génériques pour des journaux, caches, outils Node.js/TypeScript, produits de build, répertoires de dépendances, sorties web, caches frontend, fichiers `.env` et ses variantes, et plusieurs outils d'assemblage. L'exception `!.env.example` est écrite dans ce fichier. Les lignes couvrent des technologies hétérogènes ; ce contenu ne prouve ni installation d'une application Node.js ni fonctionnement d'un service PHP.

**Conséquence vérifiée :** le dépôt possède un mécanisme Git d'exclusion pour certaines familles de fichiers avant l'arrivée du code de la CLI V0.1.  
**Limites :** la présence d'une règle d'ignorance ne prouve pas qu'aucun secret a été commité, ni que toutes les familles de secrets sont protégées.

### 2. `README.md` — fichier ajouté ; une ligne

Le seul contenu du README à cette étape est `# Php2shell`, sans description fonctionnelle, exigences, procédure d'installation, preuves de tests ou modèle d'autorisation. Il faut attribuer la documentation détaillée du prototype à l'étape suivante, et non à ce commit.

## Ce que cette preuve établit et n'établit pas

- **Établi :** deux fichiers introduits, 150 lignes ajoutées au total ; message et identité affichée ; horodatage GitHub à la seconde.
- **Non établi par ce commit :** application opérationnelle, CLI, tests Python, analyse de domaines, catalogue CVE, correctifs, Docker, CI, S1, PHP2SHELL ou PHPPATCH en production.
- **Parent Git :** non reproduit dans la réponse structurée du connecteur utilisée pour cette fiche. La qualité de « commit racine » était rapportée antérieurement ; elle doit encore être attestée par une représentation des parents Git, et ne doit pas être inférée de son titre.
- **CI au SHA :** `NOT_VERIFIED` ; pas de résultat de workflow attribué ici.
- **Mandat :** origine défensive décrite rétrospectivement par [l'issue canonique #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5), créée ultérieurement, le 27/10. Elle n'est pas une autorisation d'auditer des tiers.
- **Claim de WP PHP2SHELL :** `NOT_ATTESTED` à la date historique ; aucun claim actuel n'est induit.
- **Claim de développement MCP :** hors du périmètre de cette preuve.
- **Permission S1 / déploiement :** aucun usage attesté à ce commit.
- **Rollback :** aucune opération de rollback retrouvée à ce jalon ; ne pas considérer l'absence de preuve comme une preuve d'absence.

## Chaîne temporelle et relations

La deuxième opération de la séquence retrouvée est le [commit a8600e6f](https://github.com/chainsolutions-wealthtech/Php2shell/commit/a8600e6f4d702563a0a0ec6f4d935b0d0ddf0409), observé à 16:41:47 UTC. Le comparateur GitHub confirme exactement **un commit d'avance** entre ces deux SHA, et un seul fichier modifié (`README.md`). L'observation de comparaison prouve cette relation d'ascendance, sans prétendre que tous les commits d'autres branches ont déjà été audités.

**Événement associé :** `P2S-EVT-001` (rattachement historique de la fondation, à confronter à la fiche événementielle complète).  
**Décision associée :** `P2S-DEC-001` (documentée postérieurement).  
**REQ/WP :** attribution individuelle `NOT_VERIFIED` pour cette étape, les registres de WP étant postérieurs.  
**Source de rapprochement :** [EVENT_LOG](../../../continuity/EVENT_LOG.md), [DECISIONS_LOG](../../../continuity/DECISIONS_LOG.md) sur branche de continuité.  
**État documentaire :** fiche de commit ouverte à la traçabilité, pas certification d'un déploiement ou d'une totalité d'actions.
