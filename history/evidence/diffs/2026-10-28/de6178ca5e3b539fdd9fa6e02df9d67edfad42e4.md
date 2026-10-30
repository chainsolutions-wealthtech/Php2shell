# Commit exact de6178ca5e3b539fdd9fa6e02df9d67edfad42e4

Date UTC 2026-10-28T05:39:56Z; source https://github.com/chainsolutions-wealthtech/Php2shell/commit/de6178ca5e3b539fdd9fa6e02df9d67edfad42e4

Parents: a4da81c040dd46bc9204ba57d8f0efb5a7ba7f79

Fichiers 3; +33/-2

## continuity/DECISIONS_LOG.md (modified, +1/-1)

Blob 8afb122495575f07d668faf007c30ab3d4791eb5; https://github.com/chainsolutions-wealthtech/Php2shell/blob/de6178ca5e3b539fdd9fa6e02df9d67edfad42e4/continuity%2FDECISIONS_LOG.md

```diff
@@ -27,7 +27,7 @@
 
 | P2S-DEC-014 | 2026-10-28 | Autoriser la poursuite technique continue sans nouvelle confirmation pour les opérations admissibles ; utiliser `Patricked-code` pour les revues GitHub si nécessaire | Une automatisation horaire PHP2SHELL distincte peut examiner l'état, agir sur branches autorisées et publier les checkpoints ; **ne jamais contourner** les revues exigées, protections `main`, permissions P1/P2, déploiements sensibles ni le MCP existant | Automatisation `6ae13640aa9c8191b20d3d120bf71ace` / PR #1/#6 / issue #5 |
 
-| P2S-DEC-015 | 2026-10-28 | Durcir le prototype FastAPI local par une borne **réelle** d'octets ASGI (4096), indépendamment de l'en-tête `Content-Length` | RED→GREEN, conservation de tous contrats antérieurs, sans prétendre à une limite proxy/production ni fournir auth/scan/patch ; poursuivre les tranches indépendantes seulement sous admission et sans collision | PR #2 `b231bd7`→`10ca05e`→`227915f` ; P2S-EVT-031 ; CI #40635733090 RED / #40635830627 GREEN ; issue #5 |\n\n| P2S-DEC-016 | 2026-10-28 | Bloquer une proposition de diff php.ini/.user.ini lorsque plusieurs directives `display_errors` actives peuvent produire une surcharge ambiguë | Refus conservateur à partir des preuves locales ; conserver commentaires inactifs, tabulations, CLI et absence d'écriture ; exiger évaluation effective de la configuration PHP puis validation indépendante | PR #2 `c78c10d` → `ffc6837` → `9626983` → `6a41ef5`, P2S-EVT-032, CI #40636184215 RED / #40636281308 GREEN |\n\n| P2S-DEC-017 | 2026-10-28 | Séparer authentification d'identité, mandat P1/P2 sur une ressource et approbation d'une opération active ; interdire toute autorisation déduite d'une déclaration locale | Modèle de gates purement non exécutant, refus systématique jusqu'à intégration d'un vérificateur réellement délégué MCP et revues ; aucune seconde autorité ni gateway | PR #2 `2e270c9`, P2S-EVT-033, CI #40636985499 ; MCP lecture seule 28/10 05:17 UTC |\n\n| P2S-DEC-018 | 2026-10-28 | Préparer un **vérificateur de signature externe Ed25519** sans créer d'émetteur, d'IdP ou d'autorité parallèle | Conserver `authorized=false` après vérification ; ne faire confiance qu'à une clé serveur épinglée par autorité existante et une révocation live, absentes à ce stade ; valider au moyen d'une clé éphémère de test et CI distincte | P2S-EVT-034, PR #2 `cb705a82`, auth CI #40638158899, PR #3 `c22ac964` |\n\n## Modèle pour prochaine décision
+| P2S-DEC-015 | 2026-10-28 | Durcir le prototype FastAPI local par une borne **réelle** d'octets ASGI (4096), indépendamment de l'en-tête `Content-Length` | RED→GREEN, conservation de tous contrats antérieurs, sans prétendre à une limite proxy/production ni fournir auth/scan/patch ; poursuivre les tranches indépendantes seulement sous admission et sans collision | PR #2 `b231bd7`→`10ca05e`→`227915f` ; P2S-EVT-031 ; CI #40635733090 RED / #40635830627 GREEN ; issue #5 |\n\n| P2S-DEC-016 | 2026-10-28 | Bloquer une proposition de diff php.ini/.user.ini lorsque plusieurs directives `display_errors` actives peuvent produire une surcharge ambiguë | Refus conservateur à partir des preuves locales ; conserver commentaires inactifs, tabulations, CLI et absence d'écriture ; exiger évaluation effective de la configuration PHP puis validation indépendante | PR #2 `c78c10d` → `ffc6837` → `9626983` → `6a41ef5`, P2S-EVT-032, CI #40636184215 RED / #40636281308 GREEN |\n\n| P2S-DEC-017 | 2026-10-28 | Séparer authentification d'identité, mandat P1/P2 sur une ressource et approbation d'une opération active ; interdire toute autorisation déduite d'une déclaration locale | Modèle de gates purement non exécutant, refus systématique jusqu'à intégration d'un vérificateur réellement délégué MCP et revues ; aucune seconde autorité ni gateway | PR #2 `2e270c9`, P2S-EVT-033, CI #40636985499 ; MCP lecture seule 28/10 05:17 UTC |\n\n| P2S-DEC-018 | 2026-10-28 | Préparer un **vérificateur de signature externe Ed25519** sans créer d'émetteur, d'IdP ou d'autorité parallèle | Conserver `authorized=false` après vérification ; ne faire confiance qu'à une clé serveur épinglée par autorité existante et une révocation live, absentes à ce stade ; valider au moyen d'une clé éphémère de test et CI distincte | P2S-EVT-034, PR #2 `cb705a82`, auth CI #40638158899, PR #3 `c22ac964` |\n\n| P2S-DEC-019 | 2026-10-28 | Une signature limitée à un domaine ne vaut pas délégation pour tous ses sous-chemins | Ajouter `base_path` signé en liaison exacte facultative, avec rejet des omissions et chemins ambigus ; protéger sans supprimer le contrat historique deny-only | P2S-EVT-035, PR #2 `0503c99`, RED #40638834360 / GREEN #40638887265 |\n\n| P2S-DEC-020 | 2026-10-28 | Toute future opération P1 `public_crawl` doit inclure un périmètre de chemin et des budgets signés et bornés, pas seulement une signature d'identité | Exiger `base_path` et deux plafonds Ed25519 ; refuser l'escalade et la non-canonicalité ; ne pas déclencher de réseau, ne pas fabriquer d'autorité | P2S-EVT-036, PR #2 `53e4378`, RED #40639055136 / GREEN #40639079768 |\n\n## Modèle pour prochaine décision
 
 ```text
 ID: P2S-DEC-015 (ou suivant, après contrôle du journal)
```

## continuity/REQUIREMENTS_TRACEABILITY.md (modified, +5/-0)

Blob f983fbc32ce0e524d4f871243e6478d655c4c58a; https://github.com/chainsolutions-wealthtech/Php2shell/blob/de6178ca5e3b539fdd9fa6e02df9d67edfad42e4/continuity%2FREQUIREMENTS_TRACEABILITY.md

```diff
@@ -117,3 +117,8 @@ Toute nouvelle fonctionnalité doit :
 
 - **REQ-003 / P2S-WF-S01 PARTIEL, preuve crypto hors ligne uniquement** — P2S-EVT-034 : vérification JWS Ed25519 stricte dans `app/signed_attestation.py` (PR #2 HEAD `cb705a82e5a2d0c2bf7193139873b7e7fc210706`) : signature externe, issuer/audience, subject/project/asset/action/scope, TTL court, checker révocation fail-closed ; **10 tests auth / CI #40638158899 SUCCESS**. Aucune connexion à une autorité MCP réelle, aucun droit P1/P2, toujours `authorized=false`. REQ-003 non achevée.
 - **REQ-013 / REQ-020 / REQ-032 PARTIELLES** — 171 tests historiques, 12 API et 10 nouveaux tests auth, aucun endpoint d'auth, connexion OAuth ni API prod. PR #3 HEAD `c22ac964e1cbb71d880e8ef828cf7bd96d485960`, **8/8 CI** tests/API/auth/S1-readiness SUCCESS (#40638221952/#40638221955/#40638221974/#40638222001/#40638228958/#40638228960/#40638228979/#40638229699). PR #6 continuity documentaire uniquement.
+
+
+- **REQ-003 / REQ-022 / REQ-031 / P2S-WF-S01 : PARTIELS** — P2S-EVT-035 : le vérificateur Ed25519 de la PR #2 contrôle désormais `base_path` signé et demandé, sans correspondance par préfixe implicite ; refuse chemins relatifs, traversal et omissions unilatérales. Cinq tests supplémentaires, RED auth #40638834360 → GREEN #40638887265 ; sans droit d'accès au site ni validation DNS/SSRF réelle.
+- **REQ-003 / REQ-002 / REQ-022 / P2S-WF-S01 : PARTIELS** — P2S-EVT-036 : pour un futur `public_crawl`, **`base_path`, `max_pages` et `requests_per_minute` sont obligatoirement signés**, demande plafonnée ≤ 100 pages et ≤ 30 req/min et ≤ budget signé ; cinq tests supplémentaires, RED auth #40639055136 → GREEN #40639079768. Aucun crawler ni quotas persistants implémentés ; jamais d'autorisation `ALLOW`.
+- **REQ-013 / REQ-020 / REQ-032 / P2S-WF-Q01 : PARTIELS** — PR #2 HEAD `53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf` : **171 tests CLI historiques + 12 tests API + 20 tests auth**, six CI au SHA SUCCESS. PR #3 HEAD `d48f88039e1faeea1246847a982e59bda4e63e5a` : huit CI au SHA exact SUCCESS (#40639157571/#40639157572/#40639157600/#40639157608/#40639163016/#40639163023/#40639163025/#40639163228), aucun serveur modifié.
```

## continuity/WORK_PACKAGES.json (modified, +27/-1)

Blob 30d7d59113212ffab08ee47d587d7df2d27be049; https://github.com/chainsolutions-wealthtech/Php2shell/blob/de6178ca5e3b539fdd9fa6e02df9d67edfad42e4/continuity%2FWORK_PACKAGES.json

```diff
@@ -180,6 +180,14 @@
           "source_head": "cb705a82e5a2d0c2bf7193139873b7e7fc210706",
           "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638158899",
           "limits": "10 offline signature/negative tests, ephemeral signer, no issuer MCP identity/ACL/claims or production rights"
+        },
+        {
+          "observation_date": "2026-10-28",
+          "kind": "SIGNED_PATH_AND_BUDGET_CONTRACT_NO_RUNTIME_ADMISSION",
+          "source_pr": 2,
+          "source_head": "53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf",
+          "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40639125695",
+          "limits": "20 offline Ed25519 verification tests, no real identity/mandate/worker/signed issuer or network rights"
         }
       ]
     },
@@ -197,7 +205,17 @@
       ],
       "gate": "READ_ONLY",
       "status": "PLANNED_NOT_ADMITTED",
-      "acceptance": "Check exact authority, mandated scope, evidence and matching requirement; update checkpoint before marking DONE."
+      "acceptance": "Check exact authority, mandated scope, evidence and matching requirement; update checkpoint before marking DONE.",
+      "observed_partial_evidence": [
+        {
+          "observation_date": "2026-10-28",
+          "kind": "SIGNED_PATH_AND_BUDGET_CONTRACT_NO_RUNTIME_ADMISSION",
+          "source_pr": 2,
+          "source_head": "53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf",
+          "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40639125695",
+          "limits": "20 offline Ed25519 verification tests, no real identity/mandate/worker/signed issuer or network rights"
+        }
+      ]
     },
     {
       "id": "P2S-WF-S03",
@@ -901,6 +919,14 @@
           "source_head": "cb705a82e5a2d0c2bf7193139873b7e7fc210706",
           "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40638158899",
           "limits": "10 offline signature/negative tests, ephemeral signer, no issuer MCP identity/ACL/claims or production rights"
+        },
+        {
+          "observation_date": "2026-10-28",
+          "kind": "SIGNED_PATH_AND_BUDGET_CONTRACT_NO_RUNTIME_ADMISSION",
+          "source_pr": 2,
+          "source_head": "53e4378e6f95b28a1c93c2a6061a84fb3fe4ebaf",
+          "check": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40639125695",
+          "limits": "20 offline Ed25519 verification tests, no real identity/mandate/worker/signed issuer or network rights"
         }
       ]
     },
```

Attention: inspection du diff Git, sans attestation de tests ou d'exploitation.