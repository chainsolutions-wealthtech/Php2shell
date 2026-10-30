# Contrôle de correspondance SHA des dossiers de diff — 2026-10-30

- continuity_id: `PHP2SHELL-CONT-20261027-ROOT-01`
- pull_request: https://github.com/chainsolutions-wealthtech/Php2shell/pull/7
- branch: `docs/integral-chronological-history-20261029`
- observed_head: `3faf01d3cc858b6eccef0420458f1357df1e5855`
- evidence_status: `OBSERVED_IN_GITHUB`

## Méthode

La liste paginée des chemins modifiés dans la PR #7 a été lue au HEAD indiqué. Les chemins `history/evidence/commits/YYYY-MM-DD/<40hex>.md` et `history/evidence/diffs/YYYY-MM-DD/<40hex>.md` ont été filtrés, puis rapprochés par identifiant SHA complet, et non par simple comptage global.

## Résultat

- Fiches de commits : **363**.
- Dossiers de diff : **363**.
- SHA de fiches sans dossier de diff : **0**.
- SHA de dossiers de diff sans fiche de commit : **0**.
- Statut : **PASS pour la correspondance des noms de fichiers du snapshot initial**.

## Limites probatoires explicites

Ce contrôle ne certifie **pas** l'exhaustivité du graphe Git en dehors des 363 SHA inventoriés, l'intégrité byte-à-byte des patchs, l'absence de patchs tronqués, les statuts CI, les auteurs, les horodatages, les permissions, les exécutions S1/Plesk ou les déploiements. Chaque domaine requiert un contrôle indépendant.

Les dossiers ajoutés au fil de la reconstruction reprennent les patchs exposés par le connecteur GitHub ; lorsque les métadonnées de blob, parent, statut ou statistiques n'étaient pas retournées, elles ont été marquées `NOT_VERIFIED` plutôt qu'inventées.

## Contrôles documentaires connexes (comptages de chemins, non audits de contenu)

- `history/events/` : 56 chemins.
- `history/checkpoints/` : 56 chemins.
- `history/decisions/` : 24 chemins.
- `history/pull-requests/` : 10 chemins.
- `history/work-packages/` : 62 chemins.
- `history/requirements/` : 32 chemins.
- `history/infrastructure/` : 0 chemin modifié dans cette PR ; cela n'établit pas l'absence d'informations d'infrastructure ailleurs.

## Prochaines validations

1. Auditer la complétude de chaque patch et distinguer `PATCH_PRESENT`, `PATCH_ABSENT`, `PATCH_TRUNCATED`, `NOT_VERIFIED`.
2. Réconcilier le registre Git multi-branches et vérifier les SHA contre les commits réels.
3. Rattacher les exécutions GitHub Actions aux SHA et vérifier leurs conclusions.
4. Auditer les liens entre événements, décisions, checkpoints, WP, exigences et PR.
5. Rechercher les preuves S1/Plesk sans confondre mandat, rapport et exécution attestée.

Aucune fusion, écriture `main`, action S1/Plesk ou invocation de Codex n'a été effectuée dans le cadre de ce contrôle.
