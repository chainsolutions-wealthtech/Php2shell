# P2S-EVT-055 — Déclaration P2 non vérifiée et validité temporelle des claims

**Continuité racine :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Date :** 2026-10-29 UTC. **Périmètre :** modifications locales sur PR #2 et PR #6, sans réseau, scan, patch, S1, MCP ni `main`.  
**Source canonique :** [EVENT_LOG sur PR #6](https://github.com/chainsolutions-wealthtech/Php2shell/blob/docs/canonical-continuity-20261027/continuity/EVENT_LOG.md), [issue #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5).  
**Statut de preuve :** `OBSERVED_IN_GITHUB` pour commits et workflows ; `NOT_VERIFIED` pour claims externes et permissions runtime.  
**Exigences :** REQ-003, REQ-020. **WP :** P2S-WF-S01 et P2S-WF-G09, tous deux **partiels**, non admis, non terminés.

## 1. État initial attesté — fail-open P2 dans l'inventaire hors ligne

Dans `app/core.py`, `Target` exigeait seulement que le champ `evidence` d'un scope `owned_source` soit non vide. La fonction `inventory()` produisait ensuite `source_access_allowed=True` pour ce scope, sans vérification d'identité, propriété du site, validité du mandat ni révocation. Cette sortie était incohérente avec la déclaration du module `app/campaign_import.py` selon laquelle l'import de campagne ne valide pas les mandats et n'effectue aucun réseau. Il s'agit d'un **risque de confusion d'autorisation** dans la représentation des données, et non d'une preuve d'exploitation réelle ou d'accès source exécuté.

**État GitHub avant modification :** [PR #2](https://github.com/chainsolutions-wealthtech/Php2shell/pull/2) au commit `12a31dbdd6ae83d7c9f97909098ca49fd597644e`, trois workflows de tests précédemment réussis.

## 2. Cycle RED — tests de refus P2

[Commit de tests `ac57457e45fd0562f07c1697caaab061afb6c58f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/ac57457e45fd0562f07c1697caaab061afb6c58f), fichier `tests/test_core.py`. Deux scénarios ont été ajoutés : un objet `owned_source` muni d'une simple chaîne d'évidence doit rester non autorisé ; un inventaire mixte public/owned ne doit élever aucun de ses membres.

[Run tests RED #40968190003](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968190003) : `completed/failure`, **260 tests exécutés, deux échecs attendus** confirmés dans les logs. Les workflows API et authentification associés ont réussi. Ce run n'est pas présenté comme une régression de production ; c'est un test volontaire de l'ancien comportement.

## 3. Premier GREEN partiel et découverte d'une attente héritée

[Commit `ee3aa5ee2fe255c648e03e934c892c747eaacafa`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/ee3aa5ee2fe255c648e03e934c892c747eaacafa), fichier `app/core.py`. L'inventaire renvoie désormais `source_access_allowed=False` et `authorization_verified=False` pour toute déclaration, avec `mandate_reference_supplied` séparé pour préserver l'information déclarative sans élever les droits.

[Run intermédiaire #40968207139](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968207139) : `completed/failure`, **un échec** dans `tests/test_campaign_import.py::test_json_campaign_deduplicates_normalized_hostnames`. Le test héritait de l'hypothèse incorrecte selon laquelle un texte d'évidence P2 conférait un accès source.

[Commit de compatibilité de contrat `0c7e999f73f36a98c6c40c676b0d8ec15b47e950`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/0c7e999f73f36a98c6c40c676b0d8ec15b47e950) : le test de campagne conserve ses contrôles de déduplication et de scope mais exige désormais l'absence d'autorisation P2 implicite.

**HEAD final de code PR #2 :** `0c7e999f73f36a98c6c40c676b0d8ec15b47e950`. [Tests #40968291425](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968291425) : `completed/success`, **260 tests** selon les logs ; [API #40968291429](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968291429) et [auth #40968291631](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968291631) : `completed/success`.

## 4. Deuxième tranche — contrôle temporel des claims (PR #6)

État initial : `continuity/claim_scope.py` vérifiait la correspondance de scope et `expires_at`, mais ne vérifiait pas le champ facultatif `issued_at` lorsqu'il était fourni.

[Commit de tests RED `312d6a24d38ad88addbd4be93a81a81b0ad4db2c`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/312d6a24d38ad88addbd4be93a81a81b0ad4db2c) : quatre cas (date d'émission future projet, format invalide, émission après expiration, émission future ressource externe). [CI RED #40968312927](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968312927) : `completed/failure`, **4 échecs sur 29 tests**.

[Commit GREEN `8cab675d13bdba6b5204716a9b98e4792834b9a8`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/8cab675d13bdba6b5204716a9b98e4792834b9a8) : validation `issued_at` uniquement si présent, refus d'une date future ou égale/supérieure à `expires_at`. [CI #40968324981](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968324981) : `completed/success`, **29 tests**.

**Limites importantes :** les horodatages sont déclaratifs et non signés ; une cohérence temporelle ne prouve ni autorité ni révocation ni exclusivité du claim. Le champ `issued_at` demeure optionnel pour les anciens appels ; `authority_verified=False` et `execution_authorized=False` restent inchangés.

## 5. Séparation des autorités, impacts et rollback

- **Claims PHP2SHELL WP :** `NOT_ATTESTED`. Aucune admission ni affectation du WP S01/G09.
- **Claims de développement MCP :** non utilisés et non hérités.
- **Claims de ressources externes S1/Plesk/GitHub :** `NOT_REQUIRED` pour ces travaux de code local, aucune permission d'exploitation invoquée.
- **PR #3 :** reste à réconcilier avec PR #2 sans écrasement des fichiers S1, sans rebase destructeur.
- **PR #6 :** les modifications de code ci-dessus précèdent les commits append-only de continuité, qui exigent leur CI propre au HEAD documentaire final.
- **Production :** aucun accès source, scan, correctif, déploiement ni mutation `main` attesté.
- **Rollback :** revert gouverné des commits de code et tests de PR #2 ou #6 sur leurs branches respectives, puis revalidation de tous les workflows au nouveau SHA. Aucun rollback S1.
- **NEXT_ACTION :** `P2S-NEXT-001` inchangée ; vérifier les autorités de claims et la synchronisation gouvernée de PR #3.

Cette fiche conserve les deux échecs RED et l'échec de compatibilité intermédiaire au lieu de les masquer ; elle ne déclare aucun WP terminé.
