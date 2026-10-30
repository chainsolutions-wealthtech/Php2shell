# P2S-WF-U01 — Formulaire URL projets mandats et statut d'audit

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Registre source :** [WORK_PACKAGES.json](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/WORK_PACKAGES.json)
**Blob GitHub source :** `560c5590309535ac09b74dbdf543b50bfe11a660`
**Snapshot déclaré :** `2026-10-28` (ne remplace pas l'état réel du travail).
**Lane :** `FRONTEND` ; **version :** `V1.0` ; **gate :** `GOVERNED_PR` ; **statut source :** `PLANNED_NOT_ADMITTED`

## Objet, exigences et dépendances

**Titre exact :** Formulaire URL projets mandats et statut d'audit
**Exigences :** [REQ-023](../requirements/REQ-023.md)
**Dépendances bloquantes déclarées :** [P2S-WF-I02](P2S-WF-I02.md), [P2S-WF-S04](P2S-WF-S04.md)
**Tâches aval dépendant de ce WP :** [P2S-WF-U02](P2S-WF-U02.md), [P2S-WF-U03](P2S-WF-U03.md), [P2S-WF-U06](P2S-WF-U06.md)

## Contrat complet natif (sans modifier son statut)

```json
{
  "id": "P2S-WF-U01",
  "lane": "FRONTEND",
  "phase": "V1.0",
  "title": "Formulaire URL projets mandats et statut d'audit",
  "depends_on": [
    "P2S-WF-I02",
    "P2S-WF-S04"
  ],
  "requirements": [
    "REQ-023"
  ],
  "gate": "GOVERNED_PR",
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
