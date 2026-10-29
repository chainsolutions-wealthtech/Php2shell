# Fiche probatoire P2S-EVT-056 — Synchronisation de PR #3 avec PR #2

**Continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`. **Source :** [journal canonique](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md). **Statut :** `OBSERVED_IN_GITHUB` pour les comparaisons de commits, parents et CI applicatives ; `NOT_VERIFIED` pour toute action serveur. Aucun déploiement S1.

## Historique source intégral

## P2S-EVT-056 — 2026-10-29 UTC — Fusion de synchronisation gouvernée PR #2 → PR #3 sans force

**Continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`. **Objet :** réconcilier la branche S1 PR #3 avec les changements de code de PR #2, tout en conservant les trois fichiers S1 propres à PR #3. **Source :** [PR #3](https://github.com/chainsolutions-wealthtech/Php2shell/pull/3), [merge commit `94af4f1b35655c2ba04a41157a08f191ceea4330`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/94af4f1b35655c2ba04a41157a08f191ceea4330).

**Contrôle préalable exact :** PR #2 HEAD `0c7e999f73f36a98c6c40c676b0d8ec15b47e950` ; PR #3 HEAD `5ae7245e9aa4857aca3835546a9a46ebea969d1f`. GitHub compare indiquait `diverged` : PR #2 possédait 9 commits non présents sur PR #3, PR #3 en possédait 39 non présents sur PR #2. Diff PR #3 par rapport à PR #2 limité aux **trois fichiers S1** `.github/workflows/s1-readiness.yml`, `deploy/S1_DEPLOYMENT_RUNBOOK.md`, `deploy/S1_DOCKER_ARCHITECTURE.md`. Diff PR #2 par rapport à PR #3 limité à **six fichiers applicatifs/de tests** (`app/core.py`, `app/network_preflight.py`, `tests/test_campaign_import.py`, `tests/test_core.py`, `tests/test_dns_snapshot_freshness.py`, `tests/test_network_preflight.py`).

**Construction de la fusion :** création d'un arbre Git `303ba4ba967bf8954777262a3a03994c839a704d` fondé sur le contenu exact de PR #2 avec les trois blobs S1 inchangés de PR #3 ; création d'un **commit à deux parents**, PR #3 ancien HEAD en premier et PR #2 HEAD en second. Comparaisons du commit non référencé avant déplacement : par rapport à PR #2, uniquement les trois fichiers S1 ajoutés ; par rapport à PR #3, uniquement les six fichiers PR #2 modifiés/ajoutés ; aucun autre fichier. **Déplacement GitHub `update_ref` avec `force=false` et `expected_sha=5ae7245e9aa4857aca3835546a9a46ebea969d1f` : SUCCESS.** PR #3 HEAD final `94af4f1b35655c2ba04a41157a08f191ceea4330`, les deux historiques sont ancêtres, aucun rebase, aucune réécriture.

**CI exact-SHA PR #3 :** [tests #40968807945 SUCCESS](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807945) (**260 tests**, logs consultés), [API #40968807950 SUCCESS](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807950), [auth #40968807814 SUCCESS](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807814), [S1 readiness read-only #40968807991 SUCCESS](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807991). **Statut :** synchronisation de branche achevée, pas de déploiement ni admission de production ; contributions REQ-016/017 et WP I04 restent PARTIELLES. **Claims :** projet `NOT_ATTESTED` ; ressource S1 `NOT_REQUIRED` car aucune écriture serveur ; développement MCP `NOT_USED`. Aucun WP `DONE`, aucune approbation indépendante simulée. **NEXT_ACTION : P2S-NEXT-001** maintenue. **Rollback :** revert gouverné du merge commit sur PR #3 en sélectionnant son premier parent, avec CI au SHA résultant ; aucune opération serveur à annuler.

## Contrôles de non-régression du merge

1. **Parent PR #3 :** `5ae7245e9aa4857aca3835546a9a46ebea969d1f` ; **parent PR #2 :** `0c7e999f73f36a98c6c40c676b0d8ec15b47e950`.
2. **Tree SHA :** `303ba4ba967bf8954777262a3a03994c839a704d` ; GitHub compare du merge avec PR #2 ne retourne que les trois fichiers S1, et avec PR #3 seulement les six fichiers applicatifs/tests. Cette comparaison a été effectuée avant le déplacement de ref.
3. **Mise à jour de ref :** GitHub `force=false`, `expected_sha` égal à l'ancien HEAD PR #3, résultat `success=true`. Aucun rebase ni force push.
4. **CI au merge exact :** [tests 260](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807945), [API](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807950), [auth](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807814), [S1 readiness hors ligne](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807991), tous `completed/success` lors de la vérification.
5. **Limites :** les tests ne constituent ni une approbation indépendante, ni un contrôle réel de Plesk/S1, ni une autorisation de release. Les claims WP et ressources restent non attestés ; `P2S-NEXT-001` demeure.

## Rollback admissible

Un revert gouverné du merge sur la branche PR #3 doit sélectionner son premier parent (`-m 1`) et être validé par une nouvelle CI au SHA résultant ; **ne pas** faire de reset, force push ou réécriture des parents. Aucune opération de production à annuler.
