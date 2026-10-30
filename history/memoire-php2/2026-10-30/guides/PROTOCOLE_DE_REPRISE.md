# Protocole de reprise — Memoire PHP2 (photographie historique)

Continuité : `PHP2SHELL-CONT-20261027-ROOT-01`. Autorité : issue #5. Archive : PR #7.

## Sources probatoires (ordre de priorité)
1. GitHub : SHA exact, parent(s), diff et fichiers.
2. GitHub Actions : run ID, head SHA, jobs et journaux, y compris états RED.
3. Infrastructure : preuves S1/DNS/TLS/Plesk au périmètre et à la date de l'action.
4. Issues, PR, autorisations, claims et mandats effectifs.
5. Registres natifs `continuity/` et instantané `Memoire PHP2` daté.

## Structure minimale de vérification individuelle

```yaml
memoire_id: MEMOIRE-PHP2
continuity_id: PHP2SHELL-CONT-20261027-ROOT-01
record_id: null
record_type: null
occurred_at_utc: null
observed_at_utc: null
source_url: null
commit_sha: null
parent_shas: []
head_at_check: null
changed_files: []
diff_reviewed: false
ci_runs: []
requirements: []
work_packages: []
claims_and_permissions: []
server_runtime_proof: null
before_state: null
operation: null
after_state: null
regression_checks: []
failures: []
corrections: []
rollback_evidence: null
evidence_state: NOT_VERIFIED
open_gaps: []
next_action: null
```

`NOT_VERIFIED`, `EVIDENCE_COLLECTED`, `DIFF_REVIEWED`, `CI_VERIFIED`, `ADMITTED`, `DEPLOYED_ATTESTED` sont des **étiquettes proposées pour l'archive** : ne pas les substituer aux statuts officiels des WP. La preuve de déploiement exige un contrôle runtime distinct. Tout contrôle doit être anti-collision, append-only et sans régression.
