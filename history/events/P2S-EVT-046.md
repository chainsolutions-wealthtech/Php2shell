# Fiche canonique P2S-EVT-046

**Identifiant racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source versionnée :** [EVENT_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md)
**Blob source :** `6368168136e22a2162b5f8821ce7e508387ddf1c`
**Fiabilité :** `REPORTED_IN_CANONICAL_LOG` (déclaration canonique, non certification de chaque opération).

## Ligne chronologique native

Aucune ligne du tableau ; consulter la section native ci-dessous.

## Développement natif associé

## P2S-EVT-046 — Lecture bornée du paquet PHPPATCH via descripteur

**28/10/2026 UTC — P2S-EVT-046 — PR #2 03b45fdc2cf40e3276208935b47a785ef320a27d, PR #3 d2529e6b5c87588fe0192daed8718d9657fda6de.** Renforcement défensif hors ligne de `app/patch_packet_verifier.py` : ouverture du paquet local par descripteur avec `O_NOFOLLOW` et `O_NONBLOCK`, vérification `fstat` du type fichier régulier, borne effective de 16 Kio et détection de changements observables pendant la lecture. Refus conservateur si `O_NOFOLLOW` indisponible. Trois tests ajoutés : FIFO/répertoire, substitution de symlink entre précontrôle et ouverture, croissance pendant lecture ; documentation `docs/V0_3_PATCH_PACKET_VERIFICATION.md` actualisée. **242 tests applicatifs SUCCESS** sur PR #2, six workflows tests/API/auth au SHA exact : #40666411620/#40666411562/#40666411739/#40666419373/#40666419455/#40666419560. PR #3 synchronisée sans force par merge à deux parents, `behind=0` et uniquement trois blobs S1 historiques conservés ; huit workflows SUCCESS : #40666529156/#40666529189/#40666529254/#40666529325/#40666539588/#40666539650/#40666539803/#40666539804. Aucun scan réseau, correctif appliqué, source modifiée, conteneur démarré, fusion main ou déploiement S1. Le lecteur n'est pas une preuve d'atomicité totale face aux mutations des répertoires parents, ni une attestation d'identité/mandat/approbation. La tentative MCP `ping` a demandé une authentification interactive non disponible : aucun claim runtime/S1 authentifié. PR #1 et #6 toujours en attente de revue réellement indépendante ; demandes `Patricked-code` ne valent pas approbation. Programme intégral V0.1→V0.2→V0.3→V0.4→V1.0, six lots, 32 exigences, 61 WP, parcours URL→audit autorisé→diagnostic→PHPPATCH, moteur partagé, Docker isolé et destinations `php2shell.wealthtechinnovations.com` / `phppatch.wealthtechinnovations.com` préservés. **REQ-030 / REQ-032 et P2S-WF-R06 / P2S-WF-Q01 : preuves partielles uniquement, aucun statut DONE.** `P2S-NEXT-001` reste la revue indépendante de PR #6 puis PR #1 avant toute décision de fusion.



## Vérifications et obligations

- Événement P2S-EVT-046 conservé sans modification de l'entrée source.
- Les URL citées dans l'entrée ou le développement constituent les points de contrôle pour la vérification individuelle ; une déclaration seule ne prouve pas la CI, le déploiement ou un claim.
- Pour une opération serveur, demander un élément primaire d'inventaire/log/provisioning correspondant à la date, qui n'est pas nécessairement présent dans GitHub.
- Date/heure exacte, acteur effectif, SHA initial/final, job/log, droits, statut d'admission et rollback : NOT_VERIFIED lorsqu'ils ne figurent pas explicitement dans le texte source.
