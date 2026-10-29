# V0.2 — Vérification cryptographique d'attestation externe (PR #2)

**État : code vérificateur réel mais contrat hors ligne, non raccordé à un fournisseur d'identité ni au MCP runtime. Aucun service Web, scanner, accès source P2, correction ou déploiement activé.**

Le module `app/signed_attestation.py` valide une attestation **émise à l'extérieur** au format JWS Ed25519 (`alg=EdDSA`), sans créer de signataire, autorité, jeton ni droit. La clé publique de confiance doit provenir de la configuration serveur protégée, **jamais du corps de la requête, d'un JWT `jwk/jku`, ni d'un utilisateur**. L'émetteur et l'audience acceptés doivent également être épinglés côté serveur.

La validation vérifie l'algorithme et le `kid` explicitement autorisés, la signature, les champs stricts et non dupliqués, `iss`, `aud`, `sub`, les identifiants du projet et de l'actif, la portée P1/P2, l'opération exacte, `iat`/`nbf`/`exp` (durée ≤300 secondes) et le statut de révocation fourni par un mécanisme **externe fiable**. Les mutations des claims, expirations, actions inconnues, extra `admin`, signatures malformées, jetons trop longs et checker de révocation absent/indisponible sont rejetés sans exposer les données signées.

**Séparation des portes :**

1. Authentification de session (IdP réel ; actuellement ABSENTE).
2. Vérification cryptographique d'une attestation externe (ce prototype hors ligne, disponible).
3. Admission de projet/ressource et délégation P1/P2, y compris révocation fiable (NON intégrées).
4. Claim MCP runtime, quotas, protections réseau, validation PHPPATCH et approbations (NON intégrés).
5. Exécution de l'opération (toujours interdite).

Le résultat du vérificateur, y compris pour une signature correcte, contient `authorized=false`, `execution_enabled=false`, `mcp_claim_verified=false`, `user_session_authenticated=false` et `project_acl_verified=false`. Il ne remplace pas `evaluate_action_gates` et ne doit **jamais** être transformé en décision `ALLOW` par un frontend ou un worker.

**CI indépendante :** `.github/workflows/auth-contract.yml`, installation isolée de `cryptography==46.0.3` depuis `requirements-auth-contract.txt`, puis `auth_tests`. La CI historique sans dépendance et la CI FastAPI existante restent inchangées. La clé privée dans les tests est éphémère, créée uniquement pour valider les cas nominaux et négatifs ; aucune clé privée n'est ajoutée au dépôt.

**Limite de sécurité majeure :** l'existence du vérificateur ne prouve pas que le MCP actuellement déployé émette de telles attestations ou dispose d'un mécanisme d'autorisation signé compatible. Il faut le vérifier et l'admettre auprès des autorités existantes avant tout raccordement de production. Aucune nouvelle autorité n'est créée.


## Liaison facultative au sous-chemin : prévention des confusions de périmètre (P2S-EVT-035)

Le premier contrat signé lie explicitement l'identité, le projet, le hostname et l'action, mais un domaine peut servir des applications différentes sur `/app1` et `/app2`. La tranche complémentaire ajoute le champ **facultatif signé `base_path`**, qui doit être présent simultanément dans l'attestation signée et dans la liaison attendue côté backend.

- Si `base_path` est demandé, il doit correspondre **octet pour octet** au champ signé : un chemin père, un chemin fils, une variation de suffixe ou `/app` à la place de `/app/` sont refusés. Ce n'est pas une règle d'héritage de droits par préfixe.
- La grammaire autorise uniquement les chemins absolus simples ; rejette les chemins relatifs, `//`, segments `.` et `..`, caractères de requête/fragment, encodages ambigus et valeurs trop longues.
- Les attestations historiques **sans `base_path` continuent de passer leur vérification cryptographique historique**, mais elles ne peuvent pas répondre à un appel exigeant une liaison par sous-chemin. Ce contrat historique n'a jamais permis l'exécution ; il reste `authorized=false`.
- Un JWT avec `base_path` ne peut pas être utilisé en omettant le champ `base_path` du binding serveur ; c'est une vérification symétrique non contournable par omission.
- La liaison doit provenir de l'URL prévisualisée et de l'ACL de l'autorité backend ; un utilisateur ne doit pas pouvoir choisir lui-même la liaison attendue et la clé de confiance à l'exécution. La validation du chemin ne prouve aucune propriété du site ni une délégation effective, et ne constitue pas un contrôle SSRF.

Cinq tests `auth_tests/test_signed_attestation.py` couvrent la nouvelle liaison et le maintien du mode historique. Aucun fournisseur d'identité live, session, claim ou API de scan n'est ajouté.


## Budgets P1 obligatoires et signés — tranche complémentaire P2S-EVT-036

Un crawler public peut multiplier les requêtes ; une attestation contenant uniquement un nom de site n'impose pas encore de budget. Le contrat `app/signed_attestation.py` accepte désormais un couple **facultatif pour les autres actions**, mais **obligatoire pour `public_crawl`**, de champs signés `max_pages` et `requests_per_minute` en plus du `base_path` exact signé. Le backend fournit séparément le budget demandé, dérivé de la demande initiale admise.

- Le plafond signé de pages doit être un entier strict compris entre 1 et 100, le débit signé entre 1 et 30 requêtes par minute.
- Le budget demandé par l'appelant doit lui-même être un entier strict, strictement positif, et **inférieur ou égal** au plafond signé, jamais plus élevé.
- Un seul des deux champs présent dans le token, des champs présents uniquement dans la demande, des booléens substitués à des entiers, des valeurs nulles/négatives et les dépassements de budget sont refusés.
- Pour l'opération `public_crawl` (P1), le sous-chemin signé et **les deux champs de budget signés** sont désormais obligatoires dans ce nouveau contrat. Les attestations P1 incomplètes sont refusées, même si leur signature Ed25519 est valable.
- Les anciennes attestations hors ligne de type P2 `source_read` sans champs de budget restent vérifiables pour préserver la non-régression. **Aucune** attestation n'accorde le droit d'exécuter un crawler.
- Ce contrôle ne crée ni quota persistant, ni ordonnanceur, ni vraie admission réseau. Le futur worker devra appliquer ses propres quotas et revalider les mandats et les IP au moment de chaque opération.

Cinq tests de budget, en plus des cinq tests de sous-chemin, couvrent les cas nominaux et les refus. Les 171 tests CLI historiques et 12 tests API restent distincts. Le résultat du contrat signé demeure `authorized=false`, `execution_enabled=false` et `mcp_claim_verified=false`.


## Raccordement effectif au parcours URL — contrat offline P2S-EVT-038

La fonction `app/scoped_attestation_preflight.py::verify_scoped_attestation_preflight` relie **réellement dans le code** les trois fondations existantes :

1. `preview_url_scope` produit un hostname, un sous-chemin et des budgets **recalculés à partir de l'URL HTTPS**, sans se fier à une sérialisation client de preview.
2. `verify_external_attestation` contrôle la signature Ed25519 externe contre une liste de clés publiques épinglées, l'émetteur/audience autorisés, l'ID de sujet et le projet fournis par le **backend de confiance**, le hostname/sous-chemin, l'action/scope, les budgets P1, l'expiration et le callback de révocation.
3. **P2 exige l'égalité exacte du `mandate_id` signé et de la référence requise** ; les autres opérations P2 (lecture/proposition/application/déploiement) restent indépendantes : une preuve signée pour `source_read` ne peut jamais être utilisée pour `patch_apply` ou `deploy`.

La sortie est *exclusivement* `SIGNED_URL_SCOPE_PREFLIGHT_NOT_ADMISSION`, sans URL, identité, référence de mandat ou jeton. Elle retourne `authorized=false`, `execution_enabled=false`, `user_session_authenticated=false`, `project_acl_verified=false`, `mcp_claim_verified=false`. Il n'existe **aucun endpoint d'auth** ni de scanner mis en route par ce module.

**Préconditions encore absentes pour la vraie authentification P1/P2** : fournisseur OIDC/OAuth de sessions utilisateur et preuve d'identité ; registre de projets/actifs et droits du propriétaire ; mandat réellement signé par une autorité existante reconnue (et ses clés publiques gérées/rotées côté serveur) ; révocation live ; claim MCP runtime spécifique à la tâche ; quota/enforcement réseau et contrôle SSRF ; validation indépendante des correctifs et de la production. Les identités OAuth d'agents MCP ne deviennent **pas automatiquement** des identités utilisateurs de PHP2SHELL.

Les tests `auth_tests/test_scoped_attestation_preflight.py` emploient des clés **éphémères de laboratoire**, prouvent les refus (faux périmètres, chemin, budgets, mandat, sujet/projet, délégation de type d'opération, clé absente, révocation, URL risquée), et ne fournissent aucune autorisation réelle.

**Recommandation de raccordement prod :** adopter un IdP connu et autorisé par les propriétaires du projet, exposer une interface backend **contrôlée** pour ses sessions ; obtenir une délégation scopée d'actif via la gouvernance existante ; ne brancher les attestations Ed25519 qu'après avoir vérifié que l'émetteur officiel est effectivement capable de les délivrer et révoquer. Sinon, conserver systématiquement DENY. Ne créer aucune seconde autorité parallèle au MCP.
