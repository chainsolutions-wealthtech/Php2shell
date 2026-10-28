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
