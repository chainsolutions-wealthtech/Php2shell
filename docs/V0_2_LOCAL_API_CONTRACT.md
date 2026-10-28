# V0.2 — Contrat API FastAPI local (sans crawler ni production)

**Statut : prototype FastAPI local, testable via ASGI, non déployé.**
Cette extension conserve tous les outils CLI et les deux maquettes statiques déjà acquis.

## Routes exposées

- `GET /health` — état du prototype, toujours `ready_for_production=false`.
- `GET /api/v0.2/capabilities` — tableau de capacités ; crawl, correction, authentification, mandat, déploiement sont toujours **false**.
- `POST /api/v0.2/url/preview` — prévisualisation *hors ligne* du seul périmètre P1 déclaré. Désactivée par défaut ; nécessite `P2S_ENABLE_LOCAL_API_PREVIEW=1` **et** une connexion provenant de l'adresse loopback. Refuse toute portée P2 en absence de validation externe de mandat.

Le service n'effectue **ni DNS, ni HTTP externe, ni crawl, ni collecte de code, ni exploitation, ni écriture de fichiers, ni patch**. L'activation locale n'est pas un jeton de sécurité, un compte utilisateur ou un mandat.

## Mesures locales

- Contrat strict d'entrée ; champs supplémentaires et types ambigus refusés.
- Rejet des origines `Host` non locales ; contrôle complémentaire de l'adresse du pair ASGI.
- En-têtes `Cache-Control: no-store`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`.
- Erreurs de validation génériques qui ne réaffichent ni mot de passe ni URL saisie.
- Pages de documentation/OpenAPI, endpoints de scan et de correction **absents**.
- Refus préliminaire des corps dont `Content-Length` dépasse 4 KiB. Cette limite ne remplace pas une future borne sur les *octets effectivement lus* par le proxy/serveur.
- Refus des corps HTTP dont les **octets effectivement lus** dépassent 4 Kio, même si `Content-Length` est absent, trompeur ou inférieur à la charge réelle ; rejet des déclarations de longueur dupliquées, malformées ou supérieures à la borne. Aucun contenu excessif n'est remis à Pydantic.
- L'adaptateur ASGI met en mémoire au maximum 4 Kio par requête POST/PUT/PATCH ; en cas de dépassement, réponse générique `413 REQUEST_TOO_LARGE` avec en-têtes de confidentialité. Ce contrôle applicatif local **n'est ni un rate limiter, ni une protection HTTP de production, ni une authentification** : tout futur serveur exposé devra avoir des limites indépendantes au reverse proxy et des tests end-to-end.
- Aucun lanceur de serveur ou fichier d'environnement de production ajouté ; l'API ne démarre **pas** simplement parce qu'elle est importée.

## Tests et dépendances

- `requirements-api-contract.txt` isole les dépendances de démonstration (FastAPI, HTTPX), pour ne pas altérer les CLI standard.
- `api_tests/test_local_api.py` valide uniquement les appels ASGI **en mémoire**, sans ouvrir de connexion sur le réseau. Le workflow `api-contract.yml` exécute cette suite sur les commits/PR GitHub.
- La CI existante `ci.yml` continue de protéger les tests Python historiques.

## Non-acquis

Ce prototype ne remplace pas l'architecture cible **FastAPI + PostgreSQL + Redis + workers**, l'authentification réelle, le RBAC, les claims MCP, la gestion des secrets et de la rétention, le crawler autorisé anti-SSRF, le reporting PDF, PHPPATCH ou les deux domaines S1. Ne pas publier cette API sur Internet ni y injecter de données clients.

**Prochaines dépendances :** identité réelle et contrôle de mandat P1/P2 via les autorités existantes, stockage de campagnes et isolation des projets, quotas et annulation côté workers, tests réseau isolés, puis intégration aux interfaces en PR gouvernée.

## Complément de validation RED → GREEN — 28 octobre 2026

- Trois tests ASGI sont ajoutés dans `api_tests/test_local_api.py` : corps HTTP fragmenté sans `Content-Length` ; longueur déclarée volontairement trompeuse ; requête valide fragmentée qui doit conserver le fonctionnement acquis.
- Le commit de tests `b231bd7f4e7874c24cef75e06bb550cfcc706d83` a provoqué l'échec attendu de la CI `api-contract`. Le correctif `10ca05ed21295a7c4e8364d642eabc0f83addac2` a fait passer la CI `api-contract` #40635761978 (SUCCESS au SHA exact).
- L'API est toujours un prototype de contrats local uniquement ; aucune cible réseau ni installation S1 testée par ce jalon.
