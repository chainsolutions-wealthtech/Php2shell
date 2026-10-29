# Fiche canonique P2S-EVT-035

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

| 2026-10-28 | P2S-EVT-035 | **Ed25519 sous-chemin exact** : dans le vérificateur externe hors ligne, ajout facultatif et signé de `base_path` lié au sous-chemin attendu côté backend. Refus de préfixe trompeur, omission asymétrique, traversal, query/fragment et caractères non canoniques ; contrat historique sans `base_path` préservé, sans permission. 5 tests nouveaux avec RED→GREEN. PR #3 conserve trois fichiers S1 par merge non forcé. | PR #2 RED `56607e8b82b8cef5b90799f4f6f55e695f197734`, CI auth #40638834360 FAILURE attendu ; GREEN `0556bea72f66c81d3f7c89b6f93297ccfcfef592`, CI auth #40638887265 SUCCESS ; documentation et HEAD ultérieur `0503c99b5090433750e8f70f9deade4788cb50dd` ; PR #3 HEAD `3f9e5bc6fa3046d63797f41667a53df081dacdc1`, 8 CI SUCCESS (#40638967295/#40638967296/#40638967302/#40638967372/#40638973537/#40638973541/#40638973544/#40638973611). |

## Développement natif associé

Aucune section développée portant cet identifiant dans le journal ; aucun détail additionnel inventé.

## Vérifications et obligations

- Événement P2S-EVT-035 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
