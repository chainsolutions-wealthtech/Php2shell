# Fiche canonique P2S-EVT-041

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

| 2026-10-28 | P2S-EVT-041 | **Normalisation locale des métadonnées HTTP fournies** : `app/http_metadata_normalizer.py` transforme un statut déclaré et jusqu'à 64 couples d'en-têtes en noms publics strictement filtrés, sans exporter les valeurs, cookies, secrets ni URL de redirection ; rejet des types ambigus, injections CRLF, surtailles, Unicode malformé. 12 tests de sécurité dans `tests/test_http_metadata_normalizer.py`, raccordement effectif au résumé invité `app/public_summary.py` sans promotion de confiance : `UNVERIFIED_SUPPLIED_EVIDENCE`, `audit_performed=false`, aucun réseau, aucune sauvegarde. Documentation `docs/V0_2_HTTP_METADATA_NORMALIZER.md`. **Ne constitue pas un collecteur HTTP, ni un audit réel, ni une admission P1/P2.** | PR #2 HEAD `6ca140324820b982beb59408bdd29b0edaeb25c2`, 6/6 CI SUCCESS #40644932366/#40644932373/#40644932439/#40644940088/#40644940090/#40644940082, 211 tests CLI + 17 API + 28 auth ; PR #3 HEAD `92053ae770a1f5d56d817d16e87c3498c5903872`, merge deux parents sans force, seuls 3 fichiers S1 conservés, 8/8 CI SUCCESS #40644991601/#40644991602/#40644991676/#40644991678/#40644998991/#40644999007/#40644999024/#40644999255. |

## Développement natif associé

Aucune section développée portant cet identifiant dans le journal ; aucun détail additionnel inventé.

## Vérifications et obligations

- Événement P2S-EVT-041 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
