# Audit individuel de six jobs GitHub Actions et de leurs journaux — 2026-10-30

**Continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Archive exclusive :** [PR #7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7), branche `docs/integral-chronological-history-20261029`.  
**Type :** vérification de preuves historiques GitHub, **aucun nouveau test lancé**, aucun scan ni déploiement effectué par cette opération.  
**Provenance :** `OBSERVED_IN_GITHUB` pour les jobs, leurs steps et les journaux décodés ; les rapports de l'issue #5 sont utilisés comme contexte, non comme substituts aux logs.

## Méthode

Pour chacun des six `run_id`, lecture de `fetch_workflow_run_jobs` et vérification de `job_id`, `name`, `status`, `conclusion`, `steps` et des conclusions des étapes. Ensuite lecture distincte de `fetch_workflow_job_logs(job_id)` et inspection des lignes portant le résultat `unittest`, les échecs individuels et, pour S1, les vérifications DNS/TLS/HTTPS. Le rattachement run→commit est recoupé avec le snapshot GitHub pour le run de 2026-10-22 et avec `fetch_commit_workflow_runs(commit_sha)` pour les cinq runs du 29 octobre.

Les journaux ont été **lus et examinés**, mais **ne sont pas reproduits intégralement** ici : leurs contenus bruts, les métadonnées des runners et les lignes sensibles ou transitoires ne doivent pas être recopiés sans nécessité. Le lien vers le run et le `job_id` permettent de les retrouver. Les lignes probatoires exactes sont citées ci-dessous.

## 1. Fondation V0.1 — 22 octobre 2026

**Commit exact :** [`a9d799b008fc65ed5745745bc4ef09e8b889aabe`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/a9d799b008fc65ed5745745bc4ef09e8b889aabe).  
**Run :** [`39816182850`](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/39816182850) ; événement `push` sur `main` selon le snapshot GitHub historique.  
**Job :** `119955229075`, `unit`, `completed/success`.  
**Étapes :** checkout SUCCESS ; setup Python SUCCESS ; `python -m unittest discover -s tests -v` SUCCESS ; finalisation SUCCESS.  
**Lignes de preuve du journal :** `2026-10-22T16:42:32.8101312Z Ran 7 tests in 0.001s` ; `2026-10-22T16:42:32.8102102Z OK`.  
**Portée :** sept tests de la fondation V0.1 au SHA indiqué ; aucune preuve de déploiement ni d'une campagne PHP distante.

## 2. RED — deux cycles de redirection non rejetés — 29 octobre 2026

**Commit exact :** [`38ea2ba214f8cd067333b756c9744a6cba7549c1`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/38ea2ba214f8cd067333b756c9744a6cba7549c1), associé au run par interrogation du SHA exact.  
**Run :** [`40960351574`](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40960351574).  
**Job :** `123751188601`, `unit`, `completed/failure`.  
**Étape en échec :** `Run python -m unittest discover -s tests -v` ; checkout/setup Python SUCCESS.  
**Journal :** `test_offline_redirect_cycle_back_to_start_is_rejected ... FAIL` et `test_offline_redirect_duplicate_hop_is_rejected ... FAIL`. Les deux traces contiennent `AssertionError: ValueError not raised`.  
**Résultat exact :** `Ran 258 tests in 2.012s` puis `FAILED (failures=2)` à 21:44:56 UTC.  
**Portée :** preuve d'échec reproductible de deux attentes sur les redirections **hors ligne** ; ce résultat rouge n'est pas un incident de production ni un scan réel.

## 3. GREEN — refus des cycles de redirection — 29 octobre 2026

**Commit exact :** [`12a31dbdd6ae83d7c9f97909098ca49fd597644e`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/12a31dbdd6ae83d7c9f97909098ca49fd597644e), associé au run par interrogation du SHA exact.  
**Run :** [`40960376137`](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40960376137).  
**Job :** `123751274664`, `unit`, `completed/success`.  
**Étape de test :** SUCCESS.  
**Journal :** `test_offline_redirect_cycle_back_to_start_is_rejected ... ok` ; `test_offline_redirect_duplicate_hop_is_rejected ... ok` ; `test_offline_redirect_unique_hops_remain_compatible ... ok`.  
**Résultat exact :** `Ran 258 tests in 2.384s` puis `OK` à 21:45:10 UTC.  
**Lien probatoire RED→GREEN :** le test initialement défaillant devient vert sur le commit correctif ; les autres tests réussissent à ce SHA. Cela ne prouve pas que la navigation HTTP réelle soit implémentée.

## 4. Sécurisation P2 — 260 tests — 29 octobre 2026

**Commit exact :** [`0c7e999f73f36a98c6c40c676b0d8ec15b47e950`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/0c7e999f73f36a98c6c40c676b0d8ec15b47e950), associé au run par interrogation du SHA exact.  
**Run :** [`40968291425`](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968291425).  
**Job :** `123778281624`, `unit`, `completed/success`.  
**Journal :** `Ran 260 tests in 2.798s` puis `OK` à 22:45:52 UTC. Le test `test_p2_scope_requires_reference_but_does_not_verify_it` apparaît en `ok`, confirmant que le contrat de test distingue la présence d'une référence de la vérification d'une autorité.  
**Portée :** 260 tests locaux réussis, **pas** de preuve que l'autorisation P2 soit authentifiée par un tiers.

## 5. Convergence PR #2 → PR #3 — 260 tests — 29 octobre 2026

**Commit exact :** [`94af4f1b35655c2ba04a41157a08f191ceea4330`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/94af4f1b35655c2ba04a41157a08f191ceea4330), associé au run par interrogation du SHA exact.  
**Run :** [`40968807945`](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807945).  
**Job :** `123780032323`, `unit`, `completed/success`.  
**Journal :** `Ran 260 tests in 2.786s` puis `OK` à 22:50:03 UTC.  
**Portée :** tests réussis sur le commit de convergence des branches ; n'établit pas une fusion sur `main` ni un déploiement S1.

## 6. Préparation S1 — DNS, TLS et HTTPS — 29 octobre 2026

**Commit exact :** [`94af4f1b35655c2ba04a41157a08f191ceea4330`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/94af4f1b35655c2ba04a41157a08f191ceea4330), associé au run par interrogation du SHA exact.  
**Run :** [`40968807991`](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40968807991).  
**Job :** `123780032778`, `s1-readiness`, `completed/success`.  
**Étape :** `Verify authoritative DNS, public origin, TLS and HTTPS redirect` — SUCCESS.  
**Observations textuelles dans le journal historique :**
- Le 29 octobre 2026 à 22:49:58 UTC, les quatre résolveurs autoritaires `ns1029.ui-dns.org`, `ns1059.ui-dns.de`, `ns1094.ui-dns.com`, `ns1119.ui-dns.biz` ont répondu avec l'adresse A `212.227.212.33` pour `php2shell.wealthtechinnovations.com`.
- Le journal porte `S1 direct TLS and redirect validated for php2shell.wealthtechinnovations.com` à 22:49:59 UTC.
- À 22:49:59 UTC, les quatre mêmes résolveurs ont répondu `212.227.212.33` pour `phppatch.wealthtechinnovations.com`.
- Le journal porte `S1 direct TLS and redirect validated for phppatch.wealthtechinnovations.com` à 22:50:01 UTC.
- **Avertissement explicite du workflow lui-même :** `Network and certificates pass. This does NOT prove app/auth/deployment readiness.`

**Interprétation bornée :** ce sont des observations **historiques** de la CI du 29 octobre ; elles ne garantissent pas le DNS/TLS actuel. Ce workflow de préparation ne prouve **ni** la présence des applications PHP2SHELL/PHPPATCH en production, **ni** la validation P1/P2, **ni** une mutation du serveur par la présente mission. Aucun accès S1 n'a été effectué pendant cet audit documentaire.

## Résultats de cette tranche et limites d'exhaustivité

**Six runs, six jobs et six journaux décodés examinés individuellement.** Cinq jobs `unit` et un job `s1-readiness` : cinq succès et un échec RED attendu. Les trois runs de tests à 258/260 tests, ainsi que la préparation S1, sont reliés à leurs commits par interrogation du SHA ; le run V0.1 est relié au SHA dans l'inventaire GitHub du 29 octobre.

L'index [`workflow-runs-snapshot.json`](workflow-runs-snapshot.json) annonçait 1 040 runs à son cutoff, **mais il précède plusieurs des runs du 29 octobre examinés ici**. Il ne faut pas assimiler les six runs de cette tranche à six lignes déjà présentes dans cet index ni annoncer que les 1 040 runs ont été audités. Une réconciliation des runs post-snapshot et l'examen de tous les jobs, tentatives, journaux et éventuels artefacts restent nécessaires.

**Statut de l'archive intégrale : `IN_PROGRESS` ; pas de déclaration `DONE`.**
