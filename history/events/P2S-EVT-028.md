# Fiche canonique P2S-EVT-028

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

| 2026-10-28 | P2S-EVT-028 | Renforcement **hors ligne** des précontrôles réseau : hôtes DNS soumis à la politique de saisie URL publique (IP littérale/hôte interne/URL cachée rejetés), IPv6 transition conservativement bloquées, portée de sous-chemin optionnelle pour la chaîne de redirections (segments entiers, sans changement du mode same-origin existant). **Quatre tests nouveaux, 157 tests au total**. PR #3 synchronisée sans force et ses 3 fichiers S1 conservés. **Aucun DNS live, scan, mandat authentifié, patch ou déploiement.** | PR #2 `fa1332b0d48c9147ce03f48ba3b3783fe623f3c4` (CI [#40633403515](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633403515) / [#40633408996](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633408996), 157 tests SUCCESS) ; PR #3 `11edd0e4b4ca30931d425f26f37ce91e3ee83e42` (4 CI [#40633467853](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633467853), [#40633467926](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633467926), [#40633472052](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633472052), [#40633472066](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633472066) SUCCESS). Issue #5 checkpoint #021. |

## Développement natif associé

Aucune section développée portant cet identifiant dans le journal ; aucun détail additionnel inventé.

## Vérifications et obligations

- Événement P2S-EVT-028 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
