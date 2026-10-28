# V0.2 — Planificateur de campagnes locales

Le module `app/campaign_plan.py` ajoute une préparation **hors ligne** de campagnes importées en JSON, CSV ou TXT.

Commande :
```
python -m app.cli plan-campaign --file targets.csv --shards 8
```

Il normalise les cibles, supprime les doublons compatibles, refuse les conflits de portées et prépare une répartition reproductible en 1 à 32 partitions pour au plus 10 000 cibles.

Cette opération ne crée aucun traitement dans une file, n'exécute aucun audit et n'admet aucun mandat. Les budgets affichés sont des propositions à valider avant toute utilisation.

**États vérifiables :** `jobs_created=0`, `network_requests_made=false`, `authorization_verified=false`, `safe_to_execute=false`.

Les preuves privées des mandats ne sont pas copiées dans le plan. Les tests couvrent la stabilité des partitions, un corpus de 1000 cibles, les doublons, les conflits et l'absence de permission implicite.

Le véritable ordonnanceur multi-agents, les mécanismes MCP de claims, l'API, le frontend et les workers restent à construire. Le planificateur n'est pas un système de déploiement.
