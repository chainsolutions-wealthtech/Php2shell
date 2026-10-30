# P2S-WF-I02 — Construire contrat API FastAPI commun sécurisé

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Registre source :** [WORK_PACKAGES.json](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/WORK_PACKAGES.json)
**Blob GitHub source :** `560c5590309535ac09b74dbdf543b50bfe11a660`
**Snapshot déclaré :** `2026-10-28` (ne remplace pas l'état réel du travail).
**Lane :** `INFRASTRUCTURE` ; **version :** `V0.4` ; **gate :** `GOVERNED_PR` ; **statut source :** `PLANNED_NOT_ADMITTED`

## Objet, exigences et dépendances

**Titre exact :** Construire contrat API FastAPI commun sécurisé
**Exigences :** [REQ-013](../requirements/REQ-013.md)
**Dépendances bloquantes déclarées :** [P2S-WF-G05](P2S-WF-G05.md), [P2S-WF-S01](P2S-WF-S01.md)
**Tâches aval dépendant de ce WP :** [P2S-WF-S04](P2S-WF-S04.md), [P2S-WF-I03](P2S-WF-I03.md), [P2S-WF-I04](P2S-WF-I04.md), [P2S-WF-U01](P2S-WF-U01.md)

## Contrat complet natif (sans modifier son statut)

```json
{
  "id": "P2S-WF-I02",
  "lane": "INFRASTRUCTURE",
  "phase": "V0.4",
  "title": "Construire contrat API FastAPI commun sécurisé",
  "depends_on": [
    "P2S-WF-G05",
    "P2S-WF-S01"
  ],
  "requirements": [
    "REQ-013"
  ],
  "gate": "GOVERNED_PR",
  "status": "PLANNED_NOT_ADMITTED",
  "acceptance": "Check exact authority, mandated scope, evidence and matching requirement; update checkpoint before marking DONE.",
  "observed_partial_evidence": [
    {
      "observation_date": "2026-10-28",
      "kind": "PARTIAL_CODE_EVIDENCE_NOT_WP_COMPLETION",
      "source_pr": 2,
      "source_head": "6a41ef5c15ef78af95afa0aeda3561fd5c33dd8c",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40636281308",
      "limits": "API contract-only; authentication/project gate not acquired"
    },
    {
      "observation_date": "2026-10-28",
      "kind": "OFFLINE_DENY_BY_DEFAULT_ONLY_NOT_APPROVAL",
      "source_pr": 2,
      "source_head": "2e270c92048ee9725d9d3b3cba3d2d6ec10d2b97",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40636985499",
      "limits": "No authenticated identity, delegated mandate, governed claim or production operation"
    },
    {
      "observation_date": "2026-10-28",
      "kind": "EXTERNAL_ED25519_CRYPTO_CONTRACT_NOT_AUTHENTICATION_OR_ADMISSION",
      "source_pr": 2,
      "source_head": "cb705a82e5a2d0c2bf7193139873b7e7fc210706",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638158899",
      "limits": "10 offline signature/negative tests, ephemeral signer, no issuer MCP identity/ACL/claims or production rights"
    },
    {
      "observation_date": "2026-10-28",
      "kind": "SIGNED_URL_SCOPE_AND_P2_MANDATE_EXACT_BINDING_NOT_AUTHORIZATION",
      "source_pr": 2,
      "source_head": "a14968d1aa4ff842cfd025b118c5ce90d60c55aa",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40640507524",
      "limits": "8 new auth tests; 28 auth total; no approved issuer, IdP session, ACL, claim, network scanning or deployment"
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
