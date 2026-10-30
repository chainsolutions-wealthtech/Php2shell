# Fiche canonique P2S-EVT-047

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

Aucune ligne du tableau ; consulter la section native ci-dessous.

## Développement natif associé

## P2S-EVT-047 — Durcissement du lecteur Composer (28/10/2026)

**2026-10-28T14:44:11.610Z — P2S-EVT-047.** Construction défensive locale Composer sur la PR #2 : HEAD avant `03b45fdc2cf40e3276208935b47a785ef320a27d`, après `e3237e3276b99652f6b0ab955749409d156af537`. Le lecteur `app/composer_consistency.py` refuse maintenant `O_NOFOLLOW` indisponible au lieu de suivre implicitement un symlink et vérifie via `fstat` la stabilité observable (type, identité, taille, mtime/ctime) des métadonnées pendant la lecture ; deux tests négatifs ajoutés dans `tests/test_composer_consistency.py`. **244 tests** réussis au HEAD (job 122887449339, [CI PR tests #40708622545](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40708622545)) ; **6/6 workflows PR #2 SUCCESS** (push #40708612106/#40708612195/#40708612290 ; PR #40708622555/#40708622541/#40708622545). PR #3 synchronisée par commit à deux parents `2790f4e7f0de2511a9f1f3724caa5fec82cc8eca` (`force=false`, `expected_sha`), comparaison PR #2→#3 : `behind=0`, uniquement trois fichiers S1 historiques ; **8/8 workflows SUCCESS** (push #40708753494/#40708753495/#40708753763/#40708753764 ; PR #40708760352/#40708760448/#40708760334/#40708760366). Aucun scan, patch, Docker, écriture `main` ou S1. Mandats/claims runtime MCP/S1 **non authentifiés** : permission GitHub et contrôle de ref exact SHA limités à cette construction locale, sans droit P1/P2 ni serveur. Revues `Patricked-code` demandées PR #1/#6, pas d'approbation indépendante ; **P2S-NEXT-001** inchangée. REQ-008 et P2S-WF-E07 : preuves **PARTIELLES**, aucun WP DONE. Conservation intégrale V0.1→V0.2→V0.3→V0.4→V1.0, six lots, 32 exigences, 61 WP, URL→audit autorisé→diagnostic→PHPPATCH, moteur partagé, Docker isolé, `php2shell.wealthtechinnovations.com` et `phppatch.wealthtechinnovations.com`.



## Vérifications et obligations

- Événement P2S-EVT-047 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
