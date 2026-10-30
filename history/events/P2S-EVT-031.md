# Fiche canonique P2S-EVT-031

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

| 2026-10-28 | P2S-EVT-031 | **RED → GREEN** : trois tests ASGI ajoutés sur PR #2 (streaming sans Content-Length, longueur mensongère, petite charge valide), CI api-contract ROUGE sur commit test `b231bd7f4e7874c24cef75e06bb550cfcc706d83` ; middleware ASGI ajoutée pour limiter à **4096 octets réels**, réponses génériques et refus de longueurs malformées/dupliquées. Contrat URL local toujours désactivé par défaut, sans auth/scan/patch/déploiement. PR #3 resynchronisée par merge deux parents **sans force**, trois fichiers S1 originaux préservés. | PR #2 HEAD `227915fda5379200232ec6a2a968351512fb9153`, 164 tests CLI + **12 API**, [#40635830627](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635830627) et [#40635830633](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635830633) SUCCESS ; CI RED [#40635733090](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635733090). PR #3 HEAD `fdc1e87c009eca22a294cc1bfe4b558648df9b77`, **six CI SUCCESS**, dont [#40635894060](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635894060); compare PR #2→#3 `behind=0`, seuls trois fichiers S1. |

## Développement natif associé

Aucune section développée portant cet identifiant dans le journal ; aucun détail additionnel inventé.

## Vérifications et obligations

- Événement P2S-EVT-031 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
