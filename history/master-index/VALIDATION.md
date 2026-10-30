# Contrôles structurels du registre PHP2SHELL

- Rapport : [VALIDATION_REPORT_20261030.json](VALIDATION_REPORT_20261030.json).
- Source du contrôle : lectures GitHub au commit `ae818cae47aef21acbe87400db2742b42e29ac06` ; toutes les relations ont des deux extrémités enregistrées, sans doublons ; aucun cycle dans le DAG de 61 WP.
- Exécution locale facultative : `python3 history/master-index/validate_registry.py` (lecture seule, stdlib, aucun accès réseau).
- `PASS` = structure de l'index cohérente **uniquement**. Pas de conclusion sur revue de tous les SHA, CI jobs, mandats P1/P2 ou déploiement applicatif.
- Écarts : 8 références de liens non admises au snapshot, 76 entrées sans date fiable ; consulter [écarts](matrices/MATRIX_UNVERIFIED_RELATIONS.json).
