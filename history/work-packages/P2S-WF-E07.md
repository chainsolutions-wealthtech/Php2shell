# P2S-WF-E07 — Analyse composer.lock dépendances configuration PHP/FPM

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Registre source :** [WORK_PACKAGES.json](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/WORK_PACKAGES.json)
**Blob GitHub source :** `560c5590309535ac09b74dbdf543b50bfe11a660`
**Snapshot déclaré :** `2026-10-28` (ne remplace pas l'état réel du travail).
**Lane :** `ANALYSIS` ; **version :** `V0.2` ; **gate :** `GOVERNED_PR` ; **statut source :** `PLANNED_NOT_ADMITTED`

## Objet, exigences et dépendances

**Titre exact :** Analyse composer.lock dépendances configuration PHP/FPM
**Exigences :** [REQ-008](../requirements/REQ-008.md), [REQ-026](../requirements/REQ-026.md)
**Dépendances bloquantes déclarées :** [P2S-WF-E06](P2S-WF-E06.md)
**Tâches aval dépendant de ce WP :** [P2S-WF-E11](P2S-WF-E11.md), [P2S-WF-R02](P2S-WF-R02.md)

## Contrat complet natif (sans modifier son statut)

```json
{
  "id": "P2S-WF-E07",
  "lane": "ANALYSIS",
  "phase": "V0.2",
  "title": "Analyse composer.lock dépendances configuration PHP/FPM",
  "depends_on": [
    "P2S-WF-E06"
  ],
  "requirements": [
    "REQ-008",
    "REQ-026"
  ],
  "gate": "GOVERNED_PR",
  "status": "PLANNED_NOT_ADMITTED",
  "acceptance": "Check exact authority, mandated scope, evidence and matching requirement; update checkpoint before marking DONE.",
  "observed_partial_evidence": [
    {
      "observation_date": "2026-10-28",
      "kind": "OFFLINE_COMPOSER_CONSISTENCY_PARTIAL_NOT_INSTALLED_OR_CVE_PROOF",
      "source_pr": 2,
      "source_head": "7f6ae451c1129d0b6a1a0c103f2f91659d26e55b",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40639429710",
      "limits": "17 new local-only tests; 188 historical tests, 12 API and 20 auth remain green; no semver solving, installed packages, P2 mandate or CVE applicability"
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
