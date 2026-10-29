# P2S-UX-002 — Moteur initial de synthèse courte pour visiteur

**État réel :** premier composant opérationnel **purement local**, sans collecteur HTTP, sans endpoint anonyme, sans stockage de rapport ni compte. La fonction `app.public_summary.build_guest_public_summary(url, public_response_evidence=None)` calcule une réponse courte, mais ne prétend jamais avoir audité le site.

## Contrat

- Entrée : URL HTTPS validée par `app.url_intake.preview_url_scope`. Un appel sans preuve retourne `NOT_ANALYZED`, aucun constat et une explication intelligible.
- En option : un **échantillon de métadonnées HTTP fourni, non authentifié**, avec seulement un code de statut HTTP déclaré et la présence déclarée de certains noms d'en-têtes autorisés ; aucune valeur d'en-tête, donnée privée ni contenu arbitraire. Les clés et limites sont contrôlées strictement.
- Sortie : au plus trois points clairs, **tous marqués comme preuves non vérifiées** ; aucun score de sécurité, aucune conclusion CVE, aucun statut de vulnérabilité prouvée. Les avertissements portent sur ce qui n'est pas indiqué dans l'échantillon fourni, pas sur l'état certain du site.
- Aucune requête DNS/HTTP, aucune copie persistante, aucun rapport détaillé, aucun compte utilisateur, aucun accès au code source ou correction. Tous les champs d'exécution restent `false`.
- L'action `SIGN_IN_FOR_PERSISTENT_DETAILED_REPORT` est **un jalon produit futur** : aucun écran de connexion, rapport détaillé ni sauvegarde n'est construit par ce composant.

## Suite nécessaire pour le vrai parcours public

1. Construire un **collecteur P1 public réellement autorisé** et protégé en profondeur (contrôles d'accès et d'abus, DNS SSRF au moment de chaque connexion, robots et restrictions, budgets, redirections, taille des réponses, annulation, journaux minimisés). Ne pas confondre le résumé d'une URL avec un audit.
2. Brancher ce collecteur au moteur de synthèse, en conservant une preuve de provenance que le client ne peut pas forger ; seule une collecte réellement attestée peut être présentée comme réellement effectuée.
3. Implémenter une authentification grand public réelle, des droits de visibilité, un stockage privé durable, et un rapport public détaillé uniquement sur les données effectivement obtenues.
4. Vérifier séparément la propriété du domaine puis, facultativement, connecter GitHub avec permissions minimales pour analyse P2. PHPPATCH et déploiement restent gouvernés distinctement.

**Aucune autorisation sur un site tiers ne se déduit du statut d'invité ou de l'inscription.** Ne pas publier un bouton d'audit actif tant que le collecteur et les contrôles sont absents.

## Contrat API local de validation (P2S-UX-003)

- Route de développement : `POST /api/v0.2/guest/summary` sur `service/local_api.py`. **Désactivée par défaut** ; pour les tests seulement : `P2S_ENABLE_LOCAL_GUEST_SUMMARY=1`, et appel exclusivement depuis un pair loopback. La fonction existante `_is_loopback_peer` et les middlewares de protection FastAPI sont réutilisés, sans route d'audit réel.
- Charge utile : `{"url":"https://example.com/"}` ; facultativement `public_response_evidence` fourni, strictement non vérifié. L'API refuse les champs de privilèges, ne renvoie pas d'URL contenant un secret, limite le corps HTTP à 4 Kio et désactive le cache.
- Sans information collectée, retourne `NOT_ANALYZED` ; avec des en-têtes déclarés, retourne `UNVERIFIED_SUPPLIED_EVIDENCE`, et au plus trois constats **non authentifiés**, sans niveau CVE ni fausse affirmation de scan.
- Tests `api_tests/test_guest_public_summary_api.py` : accès distant refusé, flag absent refusé, réponse courte en local, contrat des preuves fournies, champs malveillants refusés ; la CI API actuelle couvre ce nouveau parcours.
- **Ne jamais publier la route comme un scan public réel**. La prévisualisation pure n'a aucun stockage, aucune session utilisateur et aucun collecteur HTTP admis ; un reverse proxy public ne doit pas activer cette route avant un contrôle de risques complet. Une identité d'utilisateur réel et la persistance d'un rapport détaillé restent des étapes séparées.
