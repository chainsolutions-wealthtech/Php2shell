# P2S-WF-E09 — Attestation runtime PHP SAPI et paquets sous mandat P2

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Registre source :** [WORK_PACKAGES.json](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/WORK_PACKAGES.json)
**Blob GitHub source :** `560c5590309535ac09b74dbdf543b50bfe11a660`
**Snapshot déclaré :** `2026-10-28` (ne remplace pas l'état réel du travail).
**Lane :** `ANALYSIS` ; **version :** `V0.2` ; **gate :** `MANDATED_TEST_ONLY` ; **statut source :** `PLANNED_NOT_ADMITTED`

## Objet, exigences et dépendances

**Titre exact :** Attestation runtime PHP SAPI et paquets sous mandat P2
**Exigences :** [REQ-006](../requirements/REQ-006.md), [REQ-026](../requirements/REQ-026.md)
**Dépendances bloquantes déclarées :** [P2S-WF-E08](P2S-WF-E08.md), [P2S-WF-S01](P2S-WF-S01.md)
**Tâches aval dépendant de ce WP :** [P2S-WF-E10](P2S-WF-E10.md)

## Contrat complet natif (sans modifier son statut)

```json
{
  "id": "P2S-WF-E09",
  "lane": "ANALYSIS",
  "phase": "V0.2",
  "title": "Attestation runtime PHP SAPI et paquets sous mandat P2",
  "depends_on": [
    "P2S-WF-E08",
    "P2S-WF-S01"
  ],
  "requirements": [
    "REQ-006",
    "REQ-026"
  ],
  "gate": "MANDATED_TEST_ONLY",
  "status": "PLANNED_NOT_ADMITTED",
  "acceptance": "Check exact authority, mandated scope, evidence and matching requirement; update checkpoint before marking DONE."
}
```

## Distinguer planification et achèvement

Le statut `PLANNED_NOT_ADMITTED` est celui du registre au snapshot. Les événements de code peuvent documenter des parties réalisées sans que le gate, les dépendances, le claim, l'acceptation ou la revue soient satisfaits. **Ne pas promouvoir automatiquement à DONE.**

## Preuves requises pour attester l'admission

- Autorité et périmètre exacts de la demande, identité/mandat et claim de WP PHP2SHELL (distinct des claims MCP et S1).
- Contrôles HEAD exact / CI / tests de non-régression / revue autorisée, puis checkpoint sur l'issue #5.
- Si ressource externe : permission/claim de ressource séparé ; aucune autorisation S1 ne découle du présent registre.
- Échec et rollback à conserver ; aucun patch, scan distant ou déploiement inféré du seul statut de planification.
