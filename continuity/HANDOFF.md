# HANDOFF — prompt autonome pour une nouvelle conversation

Utiliser ce texte au début d'une nouvelle conversation ChatGPT ou avec tout agent autorisé à lire GitHub. L'agent **ne doit pas se fier** à sa mémoire implicite ni affirmer connaître des événements survenus après le dernier checkpoint sans lecture directe.

## Message à copier

> Reprends intégralement le programme **PHP2SHELL / PHPPATCH** à partir du point d'ancrage GitHub canonique : **https://github.com/chainsolutions-wealthtech/Php2shell/issues/5**, continuity ID `PHP2SHELL-CONT-20261027-ROOT-01`.
>
> **Lis d'abord l'issue #5 et ses derniers checkpoints**, puis les fichiers `00_START_HERE.md`, `continuity/CURRENT_STATE.md`, `continuity/NEXT_ACTION.md`, `continuity/DECISIONS_LOG.md`, `continuity/EVENT_LOG.md`, `continuity/PROTOCOL.md` sur la branche de la **[PR de continuité #6](https://github.com/chainsolutions-wealthtech/Php2shell/pull/6)** si elle n'est pas encore fusionnée dans `main`.
>
> Vérifie l'état **réel** des branches, PR #1 (V0.1), PR #2 (V0.2), PR #3 (préflight S1), des tests/CI, de l'issue #4 (S1) et de l'issue #5, à HEAD exact. Pour toute opération S1, reconnecte le MCP existant, force sa réconciliation puis consulte les sondes autorisées ; ne réutilise pas des caches conversationnels comme preuves.
>
> **Mission inchangée :** plateforme défensive d'analyse des projets PHP explicitement autorisés, catalogue CVE officiel sourcé, propositions de patch/diffs, tests Docker isolés, validation et rollback gouvernés, MCP GitHub → S1, interfaces Web complètes. Plan conservé **V0.1 → V0.2 → V0.3 → V0.4 → V1.0** sans suppression ni régression.
>
> **Deux domaines S1 :** `php2shell.wealthtechinnovations.com` (analyse/supervision), `phppatch.wealthtechinnovations.com` (propositions de remédiation/approbations), **même moteur**, permissions séparées. Les vhosts/DNS/TLS étaient prêts au dernier checkpoint ; **l'application n'était pas déployée**.
>
> Respecte les gouvernances distinctes PHP2SHELL / Patricked-code/MCP / GRT. Pas de Codex/Copilot, pas de second gateway, pas d'écriture directe sur `main`, pas de scan ou patch sur tiers non autorisés, pas de tâche concurrente, pas de suppression de l'existant.
>
> Récupère la **NEXT_ACTION** la plus récente, exécute ce qui est admissible et vérifiable, mets à jour les registres GitHub en PR et publie un **checkpoint daté dans l'issue #5** avec HEAD, actions, preuves, limites, prochaine action et handoff. Ne prétends pas avoir mémorisé automatiquement tous les messages.
>
> Conserve les protections et les travaux déjà validés, complète-les au lieu de les reconstruire.

## Mémoire étendue obligatoire

Le programme initial **comprenait dès l'origine davantage qu'un scanner local de versions**. Après lecture des checkpoints, lire aussi **`continuity/FOUNDING_SPECIFICATION.md`**, **`continuity/REQUIREMENTS_TRACEABILITY.md`** et **`continuity/CVE_SOURCE_REGISTER.md`** depuis la PR de continuité #6 si elle n'est pas fusionnée. La reprise doit conserver : inventaire CSV/JSON/TXT à volume élevé, campagnes, détection passive PHP, deux niveaux d'autorisations stricts, runtime PHP/backports, parseur PHP, dépendances/config, CVE sourcées, génération de patchs Git, tests en laboratoire Docker isolé, PostgreSQL, FastAPI, Redis/workers, PDF/CSV/JSON, les six lots initiaux **et** les cinq jalons V0.1→V1.0. Aucun livrable ne doit être déclaré implémenté sur la seule base de ce cahier des charges.

## Extension de reprise : audit d'URL depuis le frontend

Lire [`URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md`](URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md) avant tout redesign du frontend ou des agents Web. **Obligation de ne pas perdre** : champ URL/campagne, navigation de pages autorisées/quotas/SSRF, observations HTML/JS/headers, analyse code PHP serveur seulement avec connecteur autorisé P2, diagnostic et panneau CVE avec preuves/confiance, dossier PDF/JSON/CSV et passage indépendant à PHPPATCH avec propositions de patch, tests Docker isolés et approbation. **REQ-023→REQ-032** dans la matrice. Conserver les 22 exigences d'origine, les six lots et les cinq versions ; ne pas annoncer le code comme livré.

## Reprise du workflow intelligent et backlog (NE PAS IGNORER)

Lire [`INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md`](INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md) **et** [`WORK_PACKAGES.json`](WORK_PACKAGES.json) : **61 work packages de conception**, huit axes, dépendances acycliques, 32 exigences et gates. **Ne jamais confondre backlog avec tâches runtime admises**, ni créer de second bus/dispatcher, ni lancer une deuxième tâche/PR sur une ressource déjà réclamée. Revalider GitHub et le MCP avant tout claim ; une seule NEXT_ACTION métier active (`P2S-NEXT-001`) jusqu'au prochain checkpoint gouverné. Les agents peuvent élaborer des propositions en lecture seule sur des axes indépendants, jamais s'auto-autoriser des écritures ou le déploiement S1.

## Reprise après absence de connexion

Si GitHub n'est pas connecté, demander ou rétablir la connexion du dépôt ; **ne pas reconstituer une mission comme exécutée** depuis des souvenirs partiels. Si le MCP est bloqué, continuer en lecture seule/GitHub uniquement quand cela relève du mandat, puis signaler la limite. L'issue #5 est l'adresse durable à fournir pour la reprise.

## Sources techniques / statut

- PR #1 https://github.com/chainsolutions-wealthtech/Php2shell/pull/1
- PR #2 https://github.com/chainsolutions-wealthtech/Php2shell/pull/2
- PR #3 https://github.com/chainsolutions-wealthtech/Php2shell/pull/3
- Issue #4 https://github.com/chainsolutions-wealthtech/Php2shell/issues/4
- Issue #5 https://github.com/chainsolutions-wealthtech/Php2shell/issues/5
- PR #6 https://github.com/chainsolutions-wealthtech/Php2shell/pull/6


<!-- PHP2SHELL-MASTER-ROOT-ROUTING-V1 -->
## Raccordement canonique de toutes les mémoires, matrices et conversations (30 octobre 2026)

**Une seule continuité racine :** `PHP2SHELL-CONT-20261027-ROOT-01` ; [issue canonique #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5). **Pas de nouvel ID de continuité.**

- [Routage canonique JSON](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CANONICAL_CONTINUITY_MANIFEST.json) (registre unique des autorités, alias, registres et frontières de preuve).
- [Rejoindre le projet depuis une nouvelle conversation](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/JOIN_THIS_PROJECT.md) : lecture, réconciliation, prochaine action, traces de reprise.
- [Protocole anti-collision](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/NO_COLLISION_REJOIN_PROTOCOL.md) et [contrat JSON](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/REJOIN_PROTOCOL.json) : préflight HEAD, claims réels, gate, admission, écriture sans force, contrôle exact-SHA et checkpoint.
- [Arbre des relations de routage](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CONTINUITY_ROUTING_GRAPH.json) et [journal append-only](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/integral-chronological-history-20261029/history/master-index/CONTINUITY_ACTIVITY_LEDGER.jsonl).
- Les deux registres `MASTER_IDENTIFIERS_REGISTRY.json` et `MASTER_RELATIONSHIPS_REGISTRY.json` partagent la même racine et pointent vers ce manifeste ; les instantanés et 61 WP ne sont pas des autorisations runtime.

**Priorité métier préservée :** `P2S-NEXT-001` tant qu'un changement attesté n'apparaît pas dans l'issue #5 et les registres actualisés. Les nouvelles conversations doivent d'abord recontrôler les HEAD et le dernier checkpoint.
