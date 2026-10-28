# NEXT_ACTION — une priorité à la fois

**Ancre durable :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5

**Continuity ID :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Dernière décision matérialisée :** ancrer l'objectif, les décisions et la reprise dans GitHub (issue #5 et PR documentaire indépendante).

## Point opérationnel vérifié — 28 octobre 2026

- PR #6 : tests verts, revue demandée à `Patricked-code`; **approbation encore à constater** avant fusion gouvernée.
- PR #1 : les trois correctifs sont déjà **codés et testés** (HEAD `c17f0931db2cae659e4301585b0bf3db9078ca09`). Ne **pas** les refaire. La prochaine opération est la revue au HEAD et la décision de fusion.
- PR #2 : premiers imports multi-formats CSV/JSON/TXT + tests, HEAD `8c70d5f5af828588d87fd9c70a8a1b39d555de86` ; PR #3 S1 HEAD `5ce8f4ed91068fa6cad3dbd8d7ad8d16116090fa` ; deux branches resynchronisées sans rebase forcé.
- Le compte `Patricked-code` est **sollicité** pour les PR #1 et #6. Une automatisation horaire (id `6ae13640aa9c8191b20d3d120bf71ace`) a été créée pour contrôler et reprendre les travaux admissibles, sans contourner les permissions.
- **NEXT_ACTION unique** : contrôler les revues et conditions de fusion de PR #6 et PR #1, répondre aux observations éventuelles ; en parallèle, poursuivre les fonctionnalités sur les **branches existantes** si absence de collision et CI au HEAD. Aucun déploiement S1 tant qu'un outil MCP réellement autorisé et les prérequis applicatifs ne sont pas prêts.

## Point de continuité construction (28/10/2026)

- PR #2 V0.2 : `scan-local` enrichi d'indicateurs PHP ini/FPM et de l'export CSV hors ligne (JSON préservé) ; HEAD exact `47303c1eea0fc7d454ef5b73ac53d94e5c16875f`, **49 tests et deux CI SUCCESS**. Les nouvelles observations doivent rester des **indices** en l'absence d'attestation runtime.
- PR #3 S1 : intégration des changements V0.2 sans rebase forcé, HEAD `baf7dc9916e117f13ac3d9ce606f72a4e58d38d4`, **quatre CI SUCCESS**. Ne pas modifier les vhosts tant que le pipeline MCP PHP2SHELL n'est pas disponible.
- Le jalon unique `P2S-NEXT-001` demeure **revue indépendante/fusion gouvernée PR #6 puis PR #1**, en parallèle de la construction V0.2 non bloquée ; ne pas attendre les revues pour des études/tests PR indépendants autorisés.
- Automatisation `Continuité PHP2SHELL`, identifiant `6ae13640aa9c8191b20d3d120bf71ace`, **horaire** : reprendre à partir du dernier checkpoint plutôt que du présent snapshot ; pas de scheduler permanent en cours d'exécution attesté par ce fichier.

## Action prioritaire au checkpoint initial

**P2S-NEXT-001 — Finaliser la [PR #6](https://github.com/chainsolutions-wealthtech/Php2shell/pull/6) documentaire de continuité, puis préparer la revue/validation de PR #1 (V0.1).**

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

### Extension de périmètre confirmée — sans nouvelle tâche active

Le besoin utilisateur « saisir l'URL d'un site en frontend → auditer les pages autorisées → détecter les indices PHP et évaluer les CVE avec preuves → produire un dossier de remédiation → soumettre un patch proposé via PHPPATCH » est enregistré dans `continuity/URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md` et les exigences **REQ-023→REQ-032**. Ces étapes enrichissent V0.2/V0.3/V0.4/V1.0, **ne remplacent pas** le prochain geste `P2S-NEXT-001`, et **ne sont pas implémentées** à ce checkpoint.

### Catalogue exécutable-intentionnel (non encore mis en file runtime)

Le backlog [`WORK_PACKAGES.json`](WORK_PACKAGES.json) contient **61 work packages planifiés** avec dépendances et gates, répartis sur huit axes documentés dans [`INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md`](INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md). Cela permet ultérieurement des flux multidirectionnels, le retour des tests et la proposition de nouvelles tâches. **Ce catalogue n'admet et n'exécute aucune tâche** et ne remplace pas le **prochain geste unique P2S-NEXT-001** : revue indépendante PR #6 puis PR #1 V0.1 dans l'ordre gouverné.

### File des jalons ultérieurs (non actifs tant que précédents non admis)
- V0.2 : AST PHP, `composer.lock`, configurations, catalogue CVE officiel et preuves.
- V0.3 : propositions de patches, tests en Docker isolé, approbation et rollback.
- V0.4 : MCP existant, déploiement gouverné sur deux vhosts S1, sécurité et observabilité.
- V1.0 : interface Web PHP2SHELL + PHPPATCH, moteur commun, projets, rapports/historique.

**Règle :** ce fichier est un snapshot de reprise. Le dernier checkpoint GitHub ne remplace pas une observation de la réalité GitHub/S1 avant action.
