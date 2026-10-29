# Décision canonique P2S-DEC-024

**Continuity ID :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Source primaire documentaire :** [DECISIONS_LOG](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/DECISIONS_LOG.md)
**Source blob :** `2b29694e071446792f9fffc8741a89047b9e0fa9`
**Type d'élément :** décision déclarée dans le registre ; réalisation technique à attester séparément.

## Texte exact du registre

Décision non située dans la table ; voir développement natif.

## Développement natif

## P2S-DEC-024 — 2026-10-29 — Validation automatisée fondée sur des preuves (mandat utilisateur)

**Continuity ID racine unique :** `PHP2SHELL-CONT-20261027-ROOT-01`. **Autorité :** décision explicite du propriétaire du programme dans la conversation du 29 octobre 2026 ; ancrage issue #5. **Statut :** décision approuvée, implémentation complète du workflow NON ATTESTÉE.

- Adopter comme politique cible une **validation technique automatisée fondée sur des preuves** : tests de non-régression, contrôles de sécurité, CI verte liée au HEAD exact, revue technique automatisée documentée, conservation des résultats et checkpoints dans l'issue #5. Permettre la progression des constructions admissibles sur les PR/branches existantes sans attendre une confirmation humaine répétitive.
- L'utilisateur ne dispose pas d'un réviseur humain indépendant et demande de ne pas bloquer inutilement les constructions sur cette attente. **Une auto-revue, deux comptes contrôlés par la même personne ou une CI verte ne constituent jamais une approbation indépendante.** Les exigences existantes de revue indépendante, règles de protection de branche ou permissions ne sont **pas** réputées levées par cette décision : vérifier la configuration effective et, si nécessaire, soumettre une modification de politique explicite et traçable avant toute fusion concernée.
- Conserver les gates d'autorisation sur actifs P1/P2, les preuves de propriété/mandat, la sécurité des opérations sensibles, les autorisations de production, la possibilité de rollback, les claims/locks existants et les restrictions de non-régression. Ne pas scanner de tiers ni exécuter de patch/déploiement S1 sans permission applicable.
- Préserver V0.1→V0.2→V0.3→V0.4→V1.0, six lots, REQ-001→REQ-032, les 61 work packages, le moteur commun, URL→audit autorisé→diagnostic→PHPPATCH, Docker isolé et les deux sous-domaines S1. Aucun nouvel orchestrateur/gateway/automation ni écriture directe sur `main`.
- **NEXT_ACTION `P2S-NEXT-001` :** réconcilier les règles de revue/fusion réelles des PR #6 et #1 avec cette décision, puis définir sur PR existante les critères d'admission et de preuve d'une voie automatisée, sans fusion ni fausse approbation. Pendant ce temps poursuivre les constructions indépendantes admissibles avec HEAD/CI/claims vérifiés.

**Trace de publication :** issue #5 (commentaire de décision à publier séparément). **Cette décision ne marque aucun work package `DONE` et n'atteste aucun déploiement.**


## Relations d'exécution

Le registre P2S-DEC-024 fait autorité pour la décision rapportée, mais sa matérialisation en commit, CI, tâche et déploiement exige des preuves distinctes. Aucun statut DONE, claim ou autorisation n'est ajouté par l'archive.
