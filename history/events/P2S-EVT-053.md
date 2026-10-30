# P2S-EVT-053 — Vérification locale de la fraîcheur des instantanés DNS

**Continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Date des opérations :** 29 octobre 2026 (UTC, heure précise des opérations non garantie par cette fiche).  
**Dépôt :** `chainsolutions-wealthtech/Php2shell`  
**Branche applicative :** `feat/v0-2-offline-php-static-analysis-20261027`  
**PR applicative :** [#2](https://github.com/chainsolutions-wealthtech/Php2shell/pull/2)  
**Événement canonique :** [EVENT_LOG / P2S-EVT-053](../../continuity/EVENT_LOG.md) sur la branche documentaire PR #6 après sa mise à jour.  
**REQ / WP :** `REQ-031`, `P2S-WF-S03` — travail **partiel**, sans admission ni clôture du WP.

## 1. Situation constatée avant l'intervention

La PR #2 était ouverte en brouillon, sur le HEAD `973f4dbb0fffbcf256b5813030f625204fc9fa53`, avec pour base la branche V0.1 `docs/hardening-v0-1-20261022`. La PR #3 de préparation S1 était empilée sur PR #2, au HEAD `5ae7245e9aa4857aca3835546a9a46ebea969d1f`. La PR #6 documentaire était distincte, au HEAD `27e6205b61ad5bbb75edb457b10ae74ffcfabf3f`. Ces identifiants ont été lus via le connecteur GitHub avant les écritures.

La fonction `check_public_address_answers` dans `app/network_preflight.py` contrôlait déjà la syntaxe de l'horodatage déclaré, les IP publiques, les IP de transition IPv6, les doublons et les bornes TTL. Elle **ne comparait pas encore** la date de l'instantané DNS fourni à une date d'évaluation fournie. Il était donc possible qu'un instantané périmé continue à produire des adresses candidates **hors ligne**. Le module ne réalisait aucune résolution DNS ni connexion réseau et refusait toujours d'autoriser le pair.

## 2. Construction des tests — phase RED

Nouveau fichier : `tests/test_dns_snapshot_freshness.py`, créé par le commit [`ce49384abc40614d98609b44090944219a25355a`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/ce49384abc40614d98609b44090944219a25355a).

Les six tests introduisent les scénarios suivants, sans contacter de réseau :

1. Un instantané DNS déclaré à `03:00:00Z`, évalué à `03:00:30Z` avec TTL de 60 secondes, conserve une adresse candidate publique, mais **ne devient pas une autorisation réseau**.
2. À `03:01:00Z` (frontière TTL), les candidats sont retirés et le bloqueur `STALE_OR_FUTURE_DNS_SNAPSHOT` est ajouté.
3. Une évaluation antérieure à l'instantané est rejetée comme donnée future.
4. Une date d'évaluation vide, invalide, impossible ou de type non autorisé provoque un refus explicite.
5. Une adresse privée reste bloquée même si la comparaison temporelle est favorable.
6. Un appel historique ne fournissant pas `evaluated_at_utc` conserve son contrat de retour et n'affirme pas une vérification de fraîcheur.

**Preuve RED :** [workflow tests #40950801488 — FAILURE](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40950801488). Les workflows API et auth-contract de ce commit ont réussi ; leur réussite n'efface pas l'échec attendu du nouveau contrat.

## 3. Implémentation — phase GREEN

Commit [`aba5640ee24a73f01623d5e4e2dba0a342baf888`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/aba5640ee24a73f01623d5e4e2dba0a342baf888) : ajout du paramètre optionnel `evaluated_at_utc=None` à `check_public_address_answers`.

Lorsqu'une date d'évaluation est fournie, la fonction compare `evaluated_at_utc - observed_at_utc` au TTL. Seul un âge compris dans `[0, ttl_seconds[` conserve les adresses candidates. Les instantanés futurs et périmés perdent leurs candidats et produisent le bloqueur dédié. Les contrôles existants d'adresses non globales continuent à s'appliquer indépendamment.

Commit [`c8226776c9430b34d595db9654092d0c02814ce3`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/c8226776c9430b34d595db9654092d0c02814ce3) : ajustement du test de compatibilité, afin que la valeur optionnelle `None` conserve le comportement historique au lieu d'être traitée comme une date malformée.

**HEAD applicatif final vérifié :** `c8226776c9430b34d595db9654092d0c02814ce3`.

## 4. Preuves d'exécution des tests

- [Workflow tests #40950840727 — SUCCESS](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40950840727), job `unit` #123718222494 : commande `python -m unittest discover -s tests -v`, **251 tests exécutés en 2,752 secondes**, dont les six nouveaux tests de fraîcheur DNS.
- [Workflow api-contract #40950840600 — SUCCESS](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40950840600).
- [Workflow auth-contract #40950840934 — SUCCESS](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40950840934).

Ces preuves concernent le SHA de PR #2 mentionné ci-dessus. Elles ne prouvent ni l'intégration dans `main`, ni un test S1, ni une autorisation de scanner.

## 5. Autorités, limitations et absence de régression

**Claim WP PHP2SHELL :** `NOT_ATTESTED`.  
**Claim de développement MCP :** `NOT_REQUIRED` pour cette modification de code dans le dépôt PHP2SHELL.  
**Claim/permission S1 :** `NOT_REQUIRED` car aucune action S1 n'a été entreprise.  
**Droit d'exécuter un crawl :** `FALSE`.  
**Droit d'appliquer un patch :** `FALSE`.  
**Work package `P2S-WF-S03` :** `PARTIEL`, non déclaré `DONE`.

La comparaison temporelle repose sur **deux dates fournies par l'appelant**, pas sur une horloge attestée. Elle n'authentifie ni DNS, ni CNAME, ni IP du pair, ni certificat TLS, ni identité, ni consentement. Un futur worker réseau devra contrôler de nouveau ces propriétés au moment de chaque connexion et de chaque redirection.

Les appels historiques qui omettent le nouveau paramètre ne changent pas leur contrat. Aucun fichier de déploiement, branche `main`, service MCP ou vhost S1 n'a été modifié.

## 6. Conséquence sur les PR empilées

PR #3 était toujours au HEAD `5ae7245e9aa4857aca3835546a9a46ebea969d1f` après la validation de PR #2. Une comparaison de l'ancien HEAD PR #2 avec PR #3 a confirmé que les trois fichiers spécifiques S1 sont `.github/workflows/s1-readiness.yml`, `deploy/S1_DEPLOYMENT_RUNBOOK.md` et `deploy/S1_DOCKER_ARCHITECTURE.md`. **Aucune synchronisation PR #2 → PR #3 n'a été exécutée pendant cette tranche.** Elle doit faire l'objet d'une opération gouvernée, sans force et avec contrôle du HEAD/CI.

## 7. Rollback et continuité

Rollback possible uniquement par revert gouverné, sur la branche PR #2, des trois commits `c822677`, `aba5640` et `ce49384`, puis tests et CI au nouveau SHA. Aucun rollback de production n'est requis, puisqu'aucune production n'a été touchée.

**NEXT_ACTION canonique :** `P2S-NEXT-001` demeure inchangée. La prochaine action indépendante est la convergence gouvernée de PR #3 après validation des écarts, sans confusion avec les claims du MCP.

**Statut de cette fiche :** les actions et résultats ci-dessus sont corroborés par les commits, les workflows et les lectures GitHub cités. Les claims d'exécution de WP et les autorisations de production ne sont pas attestés.
