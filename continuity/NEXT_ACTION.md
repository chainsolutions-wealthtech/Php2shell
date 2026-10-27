# NEXT_ACTION — une priorité à la fois

**Continuity ID :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Dernière décision matérialisée :** ancrer l'objectif, les décisions et la reprise dans GitHub (issue #5 et PR documentaire indépendante).

## Action prioritaire au checkpoint initial

**P2S-NEXT-001 — Finaliser la PR documentaire de continuité, puis préparer la revue/validation de PR #1 (V0.1).**

### Pourquoi cette action ?
Les phases V0.2 et S1 ont été implémentées sur des PR empilées mais les fondations V0.1 ne sont pas encore fusionnées. La mémoire ne doit pas dépendre d'une discussion ChatGPT : il faut rendre le point d'entrée et le checkpoint durables.

### Conditions d'admission
1. Relire l'issue #5 et vérifier HEAD de `main`, PR #1, PR #2 et PR #3 **en direct**, avant tout nouveau changement.
2. Vérifier l'absence d'une PR/branche/mission runtime concurrente couvrant la même action.
3. Contrôler les tests exacts du HEAD de la PR documentaire (et les références des PR concernées).
4. Ne pas écraser ni rebaser arbitrairement les PR #1 → #2 → #3 ; les conserver et vérifier leurs bases.
5. Si une autre session opère sur PR #1, privilégier le constat et le checkpoint au lieu de commencer un deuxième travail concurrent.
6. Revue humaine ou indépendante conforme à la gouvernance ; ne pas fusionner en l'absence des autorisations applicables.

### Définition de réussite
- Le point d'entrée GitHub, la charte, les décisions, l'historique, le protocole et le checkpoint existent avec liens et commits.
- Une PR documentaire autonome depuis `main` présente des tests verts et une revue prévue ; si non fusionnée, l'issue #5 donne le chemin exact de branche.
- La PR #1 a une revue/CI actualisée et un prochain geste précisément établi ; pas de fusion ou déploiement supposés.
- Le dernier commentaire de l'issue #5 contient l'**unique action prioritaire actualisée**, les HEAD et les blocages.

### File des jalons ultérieurs (non actifs tant que précédents non admis)
- V0.2 : AST PHP, `composer.lock`, configurations, catalogue CVE officiel et preuves.
- V0.3 : propositions de patches, tests en Docker isolé, approbation et rollback.
- V0.4 : MCP existant, déploiement gouverné sur deux vhosts S1, sécurité et observabilité.
- V1.0 : interface Web PHP2SHELL + PHPPATCH, moteur commun, projets, rapports/historique.

**Règle :** ce fichier est un snapshot de reprise. Le dernier checkpoint GitHub ne remplace pas une observation de la réalité GitHub/S1 avant action.
