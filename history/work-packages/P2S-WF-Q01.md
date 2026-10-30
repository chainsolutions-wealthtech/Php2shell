# P2S-WF-Q01 — Vérifier non-régression des 32 exigences avec CI

**Racine :** `PHP2SHELL-CONT-20261027-ROOT-01`
**Registre source :** [WORK_PACKAGES.json](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/WORK_PACKAGES.json)
**Blob GitHub source :** `560c5590309535ac09b74dbdf543b50bfe11a660`
**Snapshot déclaré :** `2026-10-28` (ne remplace pas l'état réel du travail).
**Lane :** `QUALITY` ; **version :** `Toutes` ; **gate :** `GOVERNED_PR` ; **statut source :** `PLANNED_NOT_ADMITTED`

## Objet, exigences et dépendances

**Titre exact :** Vérifier non-régression des 32 exigences avec CI
**Exigences :** [REQ-020](../requirements/REQ-020.md), [REQ-032](../requirements/REQ-032.md)
**Dépendances bloquantes déclarées :** [P2S-WF-G01](P2S-WF-G01.md)
**Tâches aval dépendant de ce WP :** aucune

## Contrat complet natif (sans modifier son statut)

```json
{
  "id": "P2S-WF-Q01",
  "lane": "QUALITY",
  "phase": "Toutes",
  "title": "Vérifier non-régression des 32 exigences avec CI",
  "depends_on": [
    "P2S-WF-G01"
  ],
  "requirements": [
    "REQ-020",
    "REQ-032"
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
      "limits": "166 historic + 12 API tests; no E2E production proof"
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
      "kind": "SIGNED_PATH_AND_BUDGET_CONTRACT_NO_RUNTIME_ADMISSION",
      "source_pr": 2,
      "source_head": "53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40639125695",
      "limits": "20 offline Ed25519 verification tests, no real identity/mandate/worker/signed issuer or network rights"
    },
    {
      "observation_date": "2026-10-28",
      "kind": "OFFLINE_COMPOSER_CONSISTENCY_PARTIAL_NOT_INSTALLED_OR_CVE_PROOF",
      "source_pr": 2,
      "source_head": "7f6ae451c1129d0b6a1a0c103f2f91659d26e55b",
      "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40639429710",
      "limits": "17 new local-only tests; 188 historical tests, 12 API and 20 auth remain green; no semver solving, installed packages, P2 mandate or CVE applicability"
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
