# Protocole gouverné de reprise, traçabilité et prévention des collisions

**ROOT-ID :** `PHP2SHELL-CONT-20261027-ROOT-01`. **Autorité :** [issue #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5) et `continuity/PROTOCOL.md`; le présent texte les **complète, sans les remplacer**. Machine-readable : [REJOIN_PROTOCOL.json](REJOIN_PROTOCOL.json).

## Chaîne continue obligatoire
`DISCOVER → READ_CANONICAL → RECONCILE_LIVE → MAP_CURRENT_ACTIVITY → DETECT_DUPLICATES → CHECK_MANDATE → VERIFY_CLAIMS_AND_LOCKS → PLAN_MINIMAL_DELTA → WRITE_EXACT_HEAD → VERIFY_RESULTS → APPEND_CHECKPOINT → HANDOFF`.

### Préflight complet
- Lire le plus récent checkpoint de l'issue #5 et toutes les PR impliquées. Comparer à la branche **réelle** et à son SHA complet ; contrôler CI, reviews et discussions non résolues. Lire les obligations REQ, WP, gates et la provenance des faits.
- Documenter l'**objet de travail** (WP/REQ/événement), **ressource** (branch, files, runner, S1), agent, mandat, statut et owner attesté ou inconnu. Ne pas déduire un propriétaire d'un message non confirmé.
- Rechercher les interventions concurrents : PR ouvertes, branches actives, commentaire de claim, verrous MCP effectifs, dernière observation à jour. **GitHub HEAD seul ne constitue pas un verrou exclusif.**
- Si une autre écriture intervient sur la même ressource, ne pas toucher ni changer de branche silencieusement : détecter le conflit, conserver la preuve et réconcilier.
- Les ressources externes MCP/S1/Plesk exigent leurs admissions propres ; un claim de développement MCP n'accorde jamais un droit sur PHP2SHELL et réciproquement.

### Écriture autorisée
- Créer la modification **minimale et additive** sur la branche existante avec le HEAD comme parent. Reprendre le HEAD frais juste avant le déplacement de ref.
- Exiger `expected_sha=<head observé>` et `force=false`. En cas de non-concordance : **STOP**, lire le nouveau HEAD, examiner le diff et recommencer uniquement après réconciliation.
- Aucun force push, aucune modification directe de `main`, aucune fusion implicite et aucun déploiement sans validation.
- Une opération documentaire dans PR #7 ne vaut pas admission de WP et ne doit pas usurper `P2S-NEXT-001`.

### Chaîne de preuve à conserver pour chaque opération
`mandat → décision → WP/REQ → action → branche/PR → SHA avant/après → fichiers/diff → tests/CI → résultat/limites → checkpoint issue #5 → prochaine action`.

Champs nécessaires : `continuity_id`, `actor`, `mandate`, `operation_reference`, `scope`, `claim/lock status`, `HEADs`, `status_before/after`, `evidence`, `remaining_gaps`, `next_action`, `rollback`, `timestamp` (ou `DATE_ONLY`). Les commentaires et transactions sont des **traces**, non des nouveaux Continuity IDs.

### Cadence et journalisation
- Décrire l'état constaté dans un **nouveau checkpoint/addendum de l'issue #5**, sans effacer les précédents. Si la PR concerne l'archive, mettre les artefacts dans PR #7 et lier le commentaire.
- Laisser un pointeur dans [le registre des opérations](CONTINUITY_ACTIVITY_LEDGER.jsonl). Un journal documentaire ne produit **aucun verrou**, aucun déclencheur, aucune mise à jour automatique.
- Réconcilier les sources historiques figées avec les nouveaux SHA/runs/commentaires, au lieu de réécrire l'ancien snapshot.
- Handoff : nom de l'étape en cours, résultats acquis, bloqueurs, mandat, HEAD et source de vérité ; jamais « DONE » sans vérification.

### Sens du résultat
- `INDEXED` : la référence existe dans les registres.
- `REPORTED` : source historique ou commentaire, pas preuve technique indépendante.
- `VERIFIED_GITHUB` : observation GitHub réelle à SHA précis.
- `CI_VERIFIED` : checks exact SHA contrôlés.
- `RUNTIME_ATTESTED` : attestation autorisée de l'environnement ciblé.
- `NOT_VERIFIED`, `BLOCKED` : preuve insuffisante. L'absence n'est jamais convertie en succès.

**Cette méthode ne promet pas de pouvoir exécuter une action ultérieurement sans nouvelle invocation utilisateur/automatisation autorisée. Elle formalise la façon de reprendre correctement le travail quand l'agent est appelé.**
