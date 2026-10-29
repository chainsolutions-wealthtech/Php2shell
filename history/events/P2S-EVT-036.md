# Fiche canonique P2S-EVT-036

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

| 2026-10-28 | P2S-EVT-036 | **Budgets P1 signés et bornés** : l'action future `public_crawl` exige une attestation externe Ed25519 portant `base_path`, `max_pages` et `requests_per_minute` ; les budgets demandés ne peuvent dépasser les plafonds signés (100 pages / 30 requêtes par minute maximum). Refus booléens, zéros, omissions asymétriques et dépassements ; P2 historique vérifiable, jamais exécutant. 5 nouveaux tests avec RED→GREEN. | PR #2 RED `9af38e3205c219f6b578d96ee0fb9bb98d2760da` CI auth #40639055136 FAILURE attendu ; GREEN `b81d590b485f0040e7d1208a01d3e280fc8e7902` auth #40639079768 SUCCESS ; final PR #2 HEAD **`53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf`**, 6 CI success #40639118792/#40639118864/#40639118900/#40639125691/#40639125695/#40639125884 ; PR #3 HEAD **`d48f88039e1faeea1246847a982e59bda4e63e5a`**, CI finale à attester. |

## Développement natif associé

Aucune section développée portant cet identifiant dans le journal ; aucun détail additionnel inventé.

## Vérifications et obligations

- Événement P2S-EVT-036 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
