# Gouvernance et non-régression

## Autorités
Le dépôt `chainsolutions-wealthtech/Php2shell` est indépendant des dépôts MCP/GRT. Ne pas confondre leurs permissions ni leurs règles d'administration.

## Cycle de changement
1. Lire README, architecture, sécurité, tests et état GitHub.
2. Créer une branche dédiée à partir du HEAD vérifié.
3. Limiter le diff au mandat; ne pas modifier de sites tiers.
4. Exécuter les tests, vérifier la CI et analyser le diff.
5. Publier une PR avec justification, risques et plan de rollback.
6. Faire approuver avant fusion si les règles du dépôt le requièrent.
7. Enregistrer les résultats et prochaines actions dans la PR.

## Limites
Pas de tests actifs sur sites tiers, pas de collecte de code distant, pas d'exploitation ni de patch distant en V0.1. Les avis CVE de démonstration ne sont pas des renseignements de sécurité validés. La CI utilise des permissions GitHub minimales. Aucun secret dans Git.
