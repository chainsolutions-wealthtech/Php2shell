# P2S-WF-S02 — Concevoir garde-fous URL anti-SSRF DNS redirects robots quotas

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Registre source :** [WORK_PACKAGES.json](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/WORK_PACKAGES.json)
**Blob GitHub source :** `560c5590309535ac09b74dbdf543b50bfe11a660`
**Snapshot déclaré :** `2026-10-28` (ne remplace pas l'état réel du travail).
**Lane :** `SECURITY` ; **version :** `V0.2` ; **gate :** `READ_ONLY` ; **statut source :** `PLANNED_NOT_ADMITTED`

## Objet, exigences et dépendances

**Titre exact :** Concevoir garde-fous URL anti-SSRF DNS redirects robots quotas
**Exigences :** [REQ-022](../requirements/REQ-022.md), [REQ-031](../requirements/REQ-031.md)
**Dépendances bloquantes déclarées :** [P2S-WF-S01](P2S-WF-S01.md)
**Tâches aval dépendant de ce WP :** [P2S-WF-S03](P2S-WF-S03.md)

## Contrat complet natif (sans modifier son statut)

```json
{
  "id": "P2S-WF-S02",
  "lane": "SECURITY",
  "phase": "V0.2",
  "title": "Concevoir garde-fous URL anti-SSRF DNS redirects robots quotas",
  "depends_on": [
    "P2S-WF-S01"
  ],
  "requirements": [
    "REQ-022",
    "REQ-031"
  ],
  "gate": "READ_ONLY",
  "status": "PLANNED_NOT_ADMITTED",
  "acceptance": "Check exact authority, mandated scope, evidence and matching requirement; update checkpoint before marking DONE.",
  "observed_partial_evidence": [
    {
      "observation_date": "2026-10-28",
      "kind": "SIGNED_PATH_AND_BUDGET_CONTRACT_NO_RUNTIME_ADMISSION",
      "source_pr": 2,
      "source_head": "53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40639125695",
      "limits": "20 offline Ed25519 verification tests, no real identity/mandate/worker/signed issuer or network rights"
    }
  ]
}
```

## Distinguer planification et achèvement

Le statut `PLANNED_NOT_ADMITTED` est celui du registre au snapshot. Les événements de code peuvent documenter des parties réalisées sans que le gate, les dépendances, le claim, l'acceptation ou la revue soient satisfaits. **Ne pas promouvoir automatiquement à DONE.**

## Preuves requises pour attester l'admission

- Autorité et périmètre exacts de la demande, identité/mandat et claim de WP PHP2SHELL (distinct des claims MCP et S1).
- Contrôles HEAD exact / CI / tests de non-régression / revue autorisée, puis checkpoint sur l'issue #5.
- Si ressource externe : permission/claim de ressource séparé ; aucune autorisation S1 ne découle du présent registre.
- Échec et rollback à conserver ; aucun patch, scan distant ou déploiement inféré du seul statut de planification.
