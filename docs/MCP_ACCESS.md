# Accès gouverné au serveur MCP — architecture cible

**Statut : spécification uniquement, non déployée.** Ce document ne donne aucune autorisation d'accès à un serveur et ne configure aucun secret.

## Objectif
Permettre à PHP2SHELL, pour des actifs possédés ou explicitement autorisés, de demander une opération limitée sur un serveur MCP avec audit, reprise et retour arrière. Le dépôt PHP2SHELL reste indépendant de la gouvernance du dépôt Patricked-code/MCP.

## Ordre des transports et de l'authentification
1. **OIDC de GitHub Actions** : un workflow de dépôt approuvé demande un jeton OIDC de courte durée (`id-token: write` uniquement pour le job concerné). Une passerelle de confiance vérifie obligatoirement l'émetteur, l'audience, le dépôt, la référence Git, l'environnement, l'expiration et la signature. Elle échange ensuite ce jeton contre une autorisation serveur **à portée limitée**. Aucun accès n'est acquis avant validation de la politique côté serveur.
2. **MCP HTTPS OAuth/OIDC** : si le serveur MCP expose une authentification OAuth/OIDC standard, utiliser un client dédié, le flux de connexion supporté et des jetons à courte durée de vie. La GitHub App ne remplace pas ce client.
3. **Fallback SSH** : exclusivement sur serveur appartenant à l'opérateur ou mandaté, avec clé/certificat SSH de courte durée, hôte épinglé dans `known_hosts`, compte non privilégié, commandes autorisées explicitement et journaux d'audit. Pas de `StrictHostKeyChecking=no`, pas de clé privée en dépôt, pas de SSH Bridge obligatoire.
4. **Repli en lecture seule** : si aucune méthode n'est autorisée, générer un rapport et demander une validation humaine. Ne pas contourner les contrôles.

## Séparation des autorités
- L'installation GitHub App `145098929` autorise des opérations GitHub selon ses permissions. Elle **ne constitue pas** un jeton serveur.
- Les permissions de GitHub Actions sont distinctes des permissions de la GitHub App.
- Le rôle d'une identité GitHub doit être mappé à un mandat serveur vérifié, jamais déduit du seul nom du dépôt.
- Aucun jeton, clé SSH ou secret n'est publié dans ce dépôt public.

## Contrôles avant toute exécution
- Enregistrer l'actif, le propriétaire, la preuve d'autorisation, le mandat, l'action, la durée et la fenêtre d'intervention.
- Vérifier la branche/commit immuable, la CI, l'approbation indépendante et les règles d'environnement.
- Refuser les actions non listées, les destinations non autorisées et les commandes arbitraires.
- Commencer par `read-only`; réserver les modifications à un workflow distinct avec approbation explicite, sauvegarde et rollback.
- Journaliser identités, décisions, hash des artefacts et résultats sans exposer de secrets.
- Prévoir expiration, révocation, anti-rejeu, quotas, limitation réseau et procédure d'arrêt d'urgence.

## Plan d'implémentation (non réalisé)
1. Inventorier en lecture seule les capacités réelles du serveur MCP, son fournisseur OIDC et les permissions de la GitHub App.
2. Rédiger une matrice `action × identité × actif × environnement`.
3. Déployer un **laboratoire fictif** de validation des claims OIDC et des refus d'accès.
4. Tester un appel MCP `ping` en lecture seule via HTTPS et identité autorisée.
5. Tester le fallback SSH sur une machine de laboratoire, avec restriction de commandes.
6. Mettre en place des workflows manuels `workflow_dispatch` à permissions minimales et environnement protégé.
7. Soumettre une revue de sécurité indépendante avant toute utilisation sur un serveur réel.

## Critères de réussite
- OIDC fonctionne sans secret statique GitHub et refuse les claims incorrects.
- SSH refuse les hôtes non approuvés et toute commande hors allowlist.
- La perte de tous les canaux d'accès produit un **échec fermé**, pas une élévation de privilège.
- Chaque opération est attribuable à un mandat, un commit et une identité vérifiés.
