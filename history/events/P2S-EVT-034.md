# Fiche canonique P2S-EVT-034

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

| 2026-10-28 | P2S-EVT-034 | Tranche **vérification cryptographique hors ligne** des attestations externes P1/P2 : JWS Ed25519 strict, vérification signature, key-id connu, issuer/audience, identités projet/asset/opération, expiration ≤300s et callback révocation fail-closed. Aucune autorité privée/clé/signataire créée, aucune admission réelle ou serveur. 10 nouveaux tests de signature/altération/rejeu temporel/revocation/escalade ; CI dédiée isolée, tests historiques inchangés. PR #3 synchronisée sans force et trois fichiers S1 préservés. | PR #2 RED `f3851a5c40bef6e957ce7608d6d5019f33be3537` CI [#40638089308](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638089308) FAILURE attendu ; GREEN `cb705a82e5a2d0c2bf7193139873b7e7fc210706` CI auth [#40638158899](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638158899) SUCCESS (10 tests), tests/API historiques CI [#40638163772](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638163772)/[#40638163637](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638163637) SUCCESS. PR #3 `c22ac964e1cbb71d880e8ef828cf7bd96d485960` ; CI synchronisée suivie dans checkpoint. |

## Développement natif associé

Aucune section développée portant cet identifiant dans le journal ; aucun détail additionnel inventé.

## Vérifications et obligations

- Événement P2S-EVT-034 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
