# P2S-WF-G01 — Faire relire et admettre la PR #6 de continuité

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Registre source :** [WORK_PACKAGES.json](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/WORK_PACKAGES.json)
**Blob GitHub source :** `560c5590309535ac09b74dbdf543b50bfe11a660`
**Snapshot déclaré :** `2026-10-28` (ne remplace pas l'état réel du travail).
**Lane :** `GOVERNANCE` ; **version :** `V0.1` ; **gate :** `READ_ONLY` ; **statut source :** `AWAITING_INDEPENDENT_REVIEW`

## Objet, exigences et dépendances

**Titre exact :** Faire relire et admettre la PR #6 de continuité
**Exigences :** [REQ-020](../requirements/REQ-020.md)
**Dépendances bloquantes déclarées :** aucune
**Tâches aval dépendant de ce WP :** [P2S-WF-G02](P2S-WF-G02.md), [P2S-WF-G08](P2S-WF-G08.md), [P2S-WF-G09](P2S-WF-G09.md), [P2S-WF-I01](P2S-WF-I01.md), [P2S-WF-Q01](P2S-WF-Q01.md)

## Contrat complet natif (sans modifier son statut)

```json
{
  "id": "P2S-WF-G01",
  "lane": "GOVERNANCE",
  "phase": "V0.1",
  "title": "Faire relire et admettre la PR #6 de continuité",
  "depends_on": [],
  "requirements": [
    "REQ-020"
  ],
  "gate": "READ_ONLY",
  "status": "AWAITING_INDEPENDENT_REVIEW",
  "acceptance": "Check exact authority, mandated scope, evidence and matching requirement; update checkpoint before marking DONE."
}
```

## Distinguer planification et achèvement

Le statut `AWAITING_INDEPENDENT_REVIEW` est celui du registre au snapshot. Les événements de code peuvent documenter des parties réalisées sans que le gate, les dépendances, le claim, l'acceptation ou la revue soient satisfaits. **Ne pas promouvoir automatiquement à DONE.**

## Preuves requises pour attester l'admission

- Autorité et périmètre exacts de la demande, identité/mandat et claim de WP PHP2SHELL (distinct des claims MCP et S1).
- Contrôles HEAD exact / CI / tests de non-régression / revue autorisée, puis checkpoint sur l'issue #5.
- Si ressource externe : permission/claim de ressource séparé ; aucune autorisation S1 ne découle du présent registre.
- Échec et rollback à conserver ; aucun patch, scan distant ou déploiement inféré du seul statut de planification.
