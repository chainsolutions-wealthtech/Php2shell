# Fiche canonique P2S-EVT-039

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

| 2026-10-28 | P2S-EVT-039 | **Décision produit : tout le monde doit comprendre et pouvoir prévisualiser sans jargon et sans compte.** Sur PHP2SHELL prototype statique, accueil en trois étapes (site → type d'analyse → résultat futur), options en français courant au lieu des labels techniques P1/P2, paramétrage avancé repliable. Vérifications et interdits inchangés : aucun réseau ni scan, pas de connexion/ACL simulée, bouton audit désactivé, PHPPATCH distinct inchangé. 2 tests supplémentaires RED→GREEN, JS local textContent uniquement et CSP connect-src none préservés. Le parcours futur prévoit **une session utilisateur pour deux consoles**, mais nécessite une véritable autorité de droits par projet/cible pour toute opération réelle. | PR #2 RED `be36a08c07defe79ffb1a295ad209ab37e12b095`, tests #40641715258/#40641721811 FAILURE attendue ; GREEN `69cbbc6b13a08d2ce845754d2e9156edc018510d`, CI 6/6 SUCCESS #40641850954/#40641851013/#40641851020/#40641856621/#40641856693/#40641856698. PR #3 sync `97808da8783abb9625d7aa2b5efdfe7316cba998`, 8/8 CI SUCCESS #40641908837/#40641908840/#40641908841/#40641909074/#40641914531/#40641914555/#40641914557/#40641914718. |

## Développement natif associé

Aucune section développée portant cet identifiant dans le journal ; aucun détail additionnel inventé.

## Vérifications et obligations

- Événement P2S-EVT-039 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
