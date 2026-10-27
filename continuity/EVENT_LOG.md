# EVENT_LOG — historique chronologique vérifiable

**Ancre durable :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5  
**ID de continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Mode :** événements matériels synthétisés, avec liens GitHub et preuves, pas reproduction mot pour mot des échanges de messagerie. Compléter **sans supprimer** les lignes existantes.

| Date UTC / période | ID | Événement attesté ou mandat transmis | Statut et preuve |
|---|---|---|---|
| 2026-10-22 | P2S-EVT-001 | Demande de construction d'un agent d'analyse et de remédiation PHP, laboratoire fictif, deux niveaux d'autorisation ; dépôt GitHub public `Php2shell` créé | dépôt `chainsolutions-wealthtech/Php2shell` |
| 2026-10-22 | P2S-EVT-002 | Prototype V0.1 initial sur `main` ; CLI, tests, Dockerfile/lab. Branche documentaire et PR #1 ouverte | https://github.com/chainsolutions-wealthtech/Php2shell/pull/1 |
| 2026-10-27 | P2S-EVT-003 | Confirmation du plan permanent V0.1-V1.0 ; V0.2 analyseur PHP lexical local, lecture Composer, tests et documentation ajoutés dans une branche empilée | https://github.com/chainsolutions-wealthtech/Php2shell/pull/2 |
| 2026-10-27 | P2S-EVT-004 | Deux sous-domaines S1 `php2shell` et `phppatch` créés dans Plesk ; enregistrements A corrigés vers S1, TLS Let's Encrypt vérifié des deux côtés, tests HTTP/HTTPS | https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40591464440 |
| 2026-10-27 | P2S-EVT-005 | Audit DNS a comparé serveurs autoritaires, récursifs et liaison SNI directe S1 ; mise en évidence d'anciennes adresses IONOS et d'un cache récursif ponctuellement périmé. Anomalie de résolution **locale S1 non résolue** | https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40589996887 |
| 2026-10-27 | P2S-EVT-006 | Documentation du plan S1/Docker + workflow CI preflight ; PR #3 créée. Pas de service Web applicatif déployé | https://github.com/chainsolutions-wealthtech/Php2shell/pull/3 |
| 2026-10-27 | P2S-EVT-007 | Issue de suivi du raccordement gouverné à S1 créée | https://github.com/chainsolutions-wealthtech/Php2shell/issues/4 |
| 2026-10-27 | P2S-EVT-008 | Plan directeur 5 versions consolidé dans `docs/ROADMAP.md` de PR #2 sans supprimer les anciennes phases | https://github.com/chainsolutions-wealthtech/Php2shell/pull/2 |
| 2026-10-27 | P2S-EVT-009 | Demande explicite de mémoire/traces/transmission d'une conversation à une autre ; création de l'issue #5 et de la branche documentaire indépendante | https://github.com/chainsolutions-wealthtech/Php2shell/issues/5 |

## Règles de qualification
- **Observé** : objet GitHub/CI/S1 vérifié avec date/HEAD ; **déclaré** : demande utilisateur ; **prévu** : architecture non livrée.
- Indiquer lorsque des observations anciennes peuvent avoir changé, y compris les DNS/TLS et statuts de PR.
- Un nouvel événement ne doit pas masquer un incident ou une régression antérieure ; conserver les liens des contrôles rouges et verts.
- Ajouter un `P2S-EVT-nnn` seulement si pertinent et relier au commentaire checkpoint exact de l'issue #5.
