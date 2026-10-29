# Fiche canonique P2S-EVT-038

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

| 2026-10-28 | P2S-EVT-038 | **Raccordement offline des attestations P1/P2 au parcours URL** dans `app/scoped_attestation_preflight.py` : reconstruit URL canonique, lie subject/project/hostname/base_path/scope/action, budgets P1, **mandate_id signé et exact pour P2**, clés publiques/issuer/audience/revocation externes. Refuse mauvais mandat, domaine, chemin, budget ou escalade d'opération. **8 tests** RED→GREEN, aucun endpoint ni worker, refus d'exécution invariant. MCP ping/réconciliation/inventaire inspectés : sessions agent OAuth existantes mais aucun émetteur d'attestations P1/P2 PHP2SHELL ni ACL utilisateur/claim scoped attestés. | PR #2 RED `5b7c7349393b60056a527838007900c5f6829db7`, auth CI #40640364068/#40640370546 FAILURE attendue, GREEN `9f055e5e69d39a22590a6f5c7367460213bb16fd`, 6 CI SUCCESS #40640438032/#40640438044/#40640438069/#40640443817/#40640443894/#40640443898. PR #2 final `a14968d1aa4ff842cfd025b118c5ce90d60c55aa` : 6 CI SUCCESS #40640502054/#40640502127/#40640502201/#40640507523/#40640507524/#40640507556. PR #3 sync `f87eb7e1ecc41f21611aadd5c3029ac6e16f313e` : 8 CI SUCCESS #40640538179/#40640538182/#40640538186/#40640538205/#40640544639/#40640544651/#40640544656/#40640544734. |

## Développement natif associé

Aucune section développée portant cet identifiant dans le journal ; aucun détail additionnel inventé.

## Vérifications et obligations

- Événement P2S-EVT-038 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
