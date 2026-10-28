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
