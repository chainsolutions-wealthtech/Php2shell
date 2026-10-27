# Sécurité et limites

PHP2SHELL V0.1 est **strictement hors ligne**. Ne pas utiliser son résultat comme preuve qu'un système est vulnérable ou sûr.

## Règles d'autorisation
- Actifs tiers : seules les données fournies par l'opérateur sont acceptées; aucune sonde, aucun accès au code.
- Actifs possédés : une portée et une autorisation explicites sont nécessaires avant toute analyse de code future.
- L'étiquette `owned_source` et le champ `evidence` ne constituent **pas** une vérification d'identité.
- Aucun exploit, aucune tentative de contournement, aucun patch appliqué à distance.
- Ne jamais placer de jetons, identifiants ou données confidentielles dans les fichiers suivis par Git.

## Risques connus
1. **Faux positifs / faux négatifs :** comparaison de versions seule, rétroportages possibles.
2. **Sources CVE :** les données de démonstration du code doivent être remplacées par des avis authentifiés et vérifiés avant production.
3. **Entrées :** valider les noms DNS, le JSON, les versions; ne pas exécuter de chaînes fournies par l'utilisateur.
4. **Docker :** le lab est facultatif et ne publie pas de port; ne pas l'exposer sans revue.
5. **Dépendances :** vérifier les images de base et les actions CI, et épingler leurs empreintes avant un usage critique.

## Signalement
Ouvrir une issue sans inclure d'informations exploitables sensibles, de secrets ou de détails sur des cibles réelles non autorisées. Pour les incidents critiques, utiliser un canal privé convenu avec les mainteneurs.

## Critères pour une future remédiation
Mandat explicite, provenance de l'avis, diagnostic reproductible, diff limité, tests, approbation humaine, sauvegarde, rollback et journal d'audit.
