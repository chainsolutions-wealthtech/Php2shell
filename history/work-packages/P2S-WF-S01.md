# P2S-WF-S01 — Définir modèle P1/P2 autorisations preuves périmètres expirations

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Registre source :** [WORK_PACKAGES.json](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/WORK_PACKAGES.json)
**Blob GitHub source :** `560c5590309535ac09b74dbdf543b50bfe11a660`
**Snapshot déclaré :** `2026-10-28` (ne remplace pas l'état réel du travail).
**Lane :** `SECURITY` ; **version :** `V0.2` ; **gate :** `READ_ONLY` ; **statut source :** `PLANNED_NOT_ADMITTED`

## Objet, exigences et dépendances

**Titre exact :** Définir modèle P1/P2 autorisations preuves périmètres expirations
**Exigences :** [REQ-003](../requirements/REQ-003.md)
**Dépendances bloquantes déclarées :** [P2S-WF-G09](P2S-WF-G09.md)
**Tâches aval dépendant de ce WP :** [P2S-WF-S02](P2S-WF-S02.md), [P2S-WF-S04](P2S-WF-S04.md), [P2S-WF-S06](P2S-WF-S06.md), [P2S-WF-E09](P2S-WF-E09.md), [P2S-WF-I02](P2S-WF-I02.md)

## Contrat complet natif (sans modifier son statut)

```json
{
  "id": "P2S-WF-S01",
  "lane": "SECURITY",
  "phase": "V0.2",
  "title": "Définir modèle P1/P2 autorisations preuves périmètres expirations",
  "depends_on": [
    "P2S-WF-G09"
  ],
  "requirements": [
    "REQ-003"
  ],
  "gate": "READ_ONLY",
  "status": "PLANNED_NOT_ADMITTED",
  "acceptance": "Check exact authority, mandated scope, evidence and matching requirement; update checkpoint before marking DONE.",
  "observed_partial_evidence": [
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
      "kind": "SIGNED_PATH_AND_BUDGET_CONTRACT_NO_RUNTIME_ADMISSION",
      "source_pr": 2,
      "source_head": "53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40639125695",
      "limits": "20 offline Ed25519 verification tests, no real identity/mandate/worker/signed issuer or network rights"
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
