# Architecture cible Docker / Plesk S1 — PHP2SHELL & PHPPATCH

> **Statut : PLANIFIÉ, NON DÉPLOYÉ.** Contrat complémentaire au plan directeur `docs/ROADMAP.md` sur la PR #2, et au runbook S1. Aucun changement d'architecture de MCP ni de GRT. Les paramètres techniques définitifs restent soumis au préflight et à l'approbation du propriétaire.

## 1. Topologie logique (deux vhosts, une plateforme)

```text
Internet HTTPS
  |-- php2shell.wealthtechinnovations.com
  |      |-- Plesk S1 / certificat Let's Encrypt
  |      \-- reverse proxy -> interface Analyse (port local non public)
  |
  \-- phppatch.wealthtechinnovations.com
         |-- Plesk S1 / certificat Let's Encrypt
         \-- reverse proxy -> interface Remédiation (port local non public)

         Interfaces distinctes + autorisations distinctes
                       |
                  API commune sécurisée
                       |
       +---------------+---------------------+
       |               |                     |
   PostgreSQL       événements          journal d'audit
   privé            / tâches            append-only
                       |
           Workers à mandat explicitement borné
             |                       |
       Analyse PHP locale        Propositions de diff
       source autorisée          / tests isolés / rollback
             |                       |
       CVE sourcées              revue + approbation humaine

Github (source/CI/PR) → chaîne MCP gouvernée existante → S1
```

## 2. Isolation prévue

- **Console Analyse** : conteneur Web frontal non-root, sans accès direct aux sources clients ni aux secrets du moteur de correctifs. API accessible uniquement par réseau interne contrôlé.
- **Console Remédiation** : conteneur Web distinct avec authentification renforcée, RBAC et approbation avant toute opération sensible. Aucun endpoint de patch anonyme ni exécution directe de commandes.
- **API / moteur commun** : service(s) internes non exposés publiquement ; séparation stricte des mandats analyse / proposition / validation / déploiement, quotas et journaux.
- **Workers analyse** : tâches bornées en durée, CPU et mémoire ; aucun réseau sortant par défaut, sources locales autorisées montées en lecture seule, chemins validés hors symlinks, aucune exécution du PHP analysé au stade lexical.
- **Workers tests de correctifs** : conteneurs éphémères isolés, ressources limitées, artefact préparé dans un environnement temporaire et vérifié ; accès réseau seulement si explicitement justifié et autorisé ; pas de montage de secrets de production.
- **Données sensibles** : secrets gérés hors Git ; bases privées chiffrées/contrôlées, sauvegardes testées, journaux sans jetons ni code privé par défaut.
- **Sécurité Docker** : utilisateurs non-root, `read_only` quand possible, `no-new-privileges`, `cap_drop: ALL`, limites de ressources, restrictions de volumes et d'egress, images verrouillées par digest avec analyse préalable.
- **Plesk** : seuls les vhosts et certificats existants font face à Internet. Ports internes sur loopback S1 uniquement ou réseau Docker privé ; leurs numéros seront alloués après inventaire des collisions.
- **Autorité de déploiement** : GitHub PR+CI+revue → pipeline MCP autorisé exact-SHA → préflight S1 → sauvegarde → déploiement réversible → contrôles HTTPS, authentification et logs. Aucun SSH arbitraire ni écriture directe de code sur `main` ou S1.

## 3. Ordre de réalisation sans contournement des versions

| Version | Livrable de cette architecture | État |
|---|---|---|
| V0.1 | CLI, tests, fondamentaux de sécurité | Développé, PR #1 ouverte |
| V0.2 | Analyse statique locale et catalogue CVE fiable | Lexical partiel, PR #2 ouverte |
| V0.3 | Patches proposés et vérifiés en sandbox, diffs, rollback | Non implémenté |
| V0.4 | Pipeline MCP + deux domaines S1 + Docker isolé | Préflight réseau fait, PR #3 ; runtime non déployé |
| V1.0 | Deux interfaces Web avec moteur partagé, gestion de projets, historique, rapports | Non implémenté |

Les vérifications DNS/TLS déjà effectuées sont une **préparation anticipée de V0.4**, pas une déclaration de V0.4 opérationnelle. La séparation des deux interfaces concerne des permissions et des fonctions, jamais la création de deux gouvernances ou moteurs concurrents.

## 4. Conditions non négociables avant mise en service

- Tranche applicative effective, tests, CI et revue indépendante. Une page Plesk ou `HTTP 200` ne constitue **pas** un déploiement de PHP2SHELL.
- Inventaire Plesk, chemins `realpath`, ports, certificats, éventuelles collisions et données déjà présentes attestés au HEAD.
- Implémentation gouvernée autorisée des cibles dans le MCP actuel, sans détourner les outils `legacy_vhost` d'un autre périmètre.
- Preuves d'identité, RBAC, CSRF, protection des sessions et journaux d'audit, tests négatifs d'autorisation, gestion de secrets.
- Exposition réseau limitée et sauvegarde/restauration/rollback testés en staging.
- Zéro scan intrusif de tiers ; remédiation sur une production uniquement après accord explicite et contrôles requis.
