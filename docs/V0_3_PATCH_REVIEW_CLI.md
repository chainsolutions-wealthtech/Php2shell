# V0.3 — Vérification CLI d'un paquet de revue PHPPATCH (hors ligne)

Cette tranche expose **le vérificateur local existant** via la CLI historique
`app.cli`. Elle ne crée pas de moteur de patch, de nouveau mandat, de
workflow de déploiement, de service réseau ou de seconde gouvernance.

## Utilisation

Après avoir généré un paquet avec `prepare-patch-review` et sauvegardé
localement son JSON (hors de tout dépôt public), exécuter :

```bash
python -m app.cli verify-patch-review \
  --packet-file /chemin/local/review-packet.json \
  --path /chemin/local/projet-autorise \
  --as-of 2026-10-28 \
  --evidence-id P2S-EV-0123456789abcdef
```

L'identifiant d'exemple est fictif : utiliser celui du dossier courant.
La commande relit le fichier JSON local (16 Kio maximum, sans symlink),
recalcule le paquet à partir du projet local, puis compare **l'intégralité**
des champs et types. Elle refuse les données altérées, les preuves périmées,
les clés JSON dupliquées et les tentatives d'élévation d'autorité.

Succès : JSON avec `local_lineage_matches=true` et **tous les indicateurs
d'autorité/exécution à `false`**. Échec : code de sortie 2, message générique
sans contenu du dossier, aucune sortie JSON trompeuse.

## Frontières de sécurité

- La concordance locale **ne vaut pas signature** et ne valide ni identité,
  ni mandat P1/P2, ni propriété de site, ni approbation indépendante.
- Aucun correctif n'est appliqué, aucun fichier source n'est écrit, aucun
  test Docker/PHP n'est exécuté et aucun rollback de production n'est prouvé.
- Pas de requête HTTP, scan, dépôt Git modifié ou déploiement S1.
- Les sorties ne contiennent ni source brute ni secrets. Le projet doit être
  un projet local autorisé ; ne pas passer de données privées dans des logs.
- Les contrôles sont des vérifications locales préliminaires et ne
  remplacent pas les validations runtime, backports, permissions et revue.

La commande est additive ; `prepare-patch-review`, `rehearse-config-patch`,
`scan-local` et les autres commandes préexistantes sont conservées.
Tranche partielle REQ-030 / P2S-WF-R06 et REQ-032 / P2S-WF-Q01 ;
**aucune exigence ni work package déclaré terminé**.
