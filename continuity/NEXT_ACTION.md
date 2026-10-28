# NEXT_ACTION — une priorité à la fois

**Ancre durable :** https://github.com/chainsolutions-wealthtech/Php2shell/issues/5

**Continuity ID :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**Dernière décision matérialisée :** ancrer l'objectif, les décisions et la reprise dans GitHub (issue #5 et PR documentaire indépendante).

## Point opérationnel vérifié — 28 octobre 2026

- PR #6 : tests verts, revue demandée à `Patricked-code`; **approbation encore à constater** avant fusion gouvernée.
- PR #1 : les trois correctifs sont déjà **codés et testés** (HEAD `c17f0931db2cae659e4301585b0bf3db9078ca09`). Ne **pas** les refaire. La prochaine opération est la revue au HEAD et la décision de fusion.
- PR #2 : premiers imports multi-formats CSV/JSON/TXT + tests, HEAD `8c70d5f5af828588d87fd9c70a8a1b39d555de86` ; PR #3 S1 HEAD `5ce8f4ed91068fa6cad3dbd8d7ad8d16116090fa` ; deux branches resynchronisées sans rebase forcé.
- Le compte `Patricked-code` est **sollicité** pour les PR #1 et #6. Une automatisation horaire (id `6ae13640aa9c8191b20d3d120bf71ace`) a été créée pour contrôler et reprendre les travaux admissibles, sans contourner les permissions.
- **NEXT_ACTION unique** : contrôler les revues et conditions de fusion de PR #6 et PR #1, répondre aux observations éventuelles ; en parallèle, poursuivre les fonctionnalités sur les **branches existantes** si absence de collision et CI au HEAD. Aucun déploiement S1 tant qu'un outil MCP réellement autorisé et les prérequis applicatifs ne sont pas prêts.

## Point de continuité construction (28/10/2026)

- PR #2 V0.2 : `scan-local` enrichi d'indicateurs PHP ini/FPM et de l'export CSV hors ligne (JSON préservé) ; HEAD exact `47303c1eea0fc7d454ef5b73ac53d94e5c16875f`, **49 tests et deux CI SUCCESS**. Les nouvelles observations doivent rester des **indices** en l'absence d'attestation runtime.
- PR #3 S1 : intégration des changements V0.2 sans rebase forcé, HEAD `baf7dc9916e117f13ac3d9ce606f72a4e58d38d4`, **quatre CI SUCCESS**. Ne pas modifier les vhosts tant que le pipeline MCP PHP2SHELL n'est pas disponible.
- Le jalon unique `P2S-NEXT-001` demeure **revue indépendante/fusion gouvernée PR #6 puis PR #1**, en parallèle de la construction V0.2 non bloquée ; ne pas attendre les revues pour des études/tests PR indépendants autorisés.
- Automatisation `Continuité PHP2SHELL`, identifiant `6ae13640aa9c8191b20d3d120bf71ace`, **horaire** : reprendre à partir du dernier checkpoint plutôt que du présent snapshot ; pas de scheduler permanent en cours d'exécution attesté par ce fichier.

## Prochaine étape technique admissible — après l'instantané CVE sourcé

- PR #2 V0.2 : nouveau registre local CVE PHP/CERT-FR et `review-version` **codés et testés** au HEAD `4848bff596977595e58b28db01eaebcd1a128e14` (58 tests et 2 CI vertes). **Ne pas réimplémenter cette étape** ; garder la commande legacy `check-version`.
- PR #3 S1 : synchronisation vérifiée au HEAD `e12cb5054d2a7ac9db1829a5da4eb37e6de919f1` avec 4 CI vertes ; **aucun service déployé**.
- Travail V0.2 restant : préparation de l'ingestion officielle datée des avis sous permission réseau bornée, suivi des révisions et backports des distributions, preuve P2 de runtime/SAPI, extension de l'analyse PHP AST, puis dossier de remédiation. Les contrôles P1/P2 et la preuve de mandat précèdent tout audit distant.
- **Action métier unique toujours `P2S-NEXT-001`** : revue indépendante/fusion gouvernée PR #6 puis PR #1. Continuer entre-temps les sous-tranches indépendantes sur PR #2, sans collision, avec CI exact SHA et checkpoint. L'automatisation horaire conserve ce mandat, pas de nouvelle automation.

## Reprise après audit de provenance du catalogue — 28 octobre 2026

- **PR #2 V0.2** : `audit-catalog --as-of YYYY-MM-DD` codé et testé, SHA `2d2d7abee3b33edcc86bb17975cbe8fa5c1c4390`, CI [40610646884](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610646884) **SUCCESS**. Produit âge de revue, empreinte canonique et avertissements permanents ; ne consulte aucune source distante. L'empreinte **n'est pas une signature éditeur**.
- **PR #3 S1** : resynchronisée par merge à deux parents, SHA `58a15991d4218d756f84acbe1d8b1687d4af8bdd`, quatre CI [40610704047](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610704047), [40610704076](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610704076), [40610712317](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610712317), [40610712452](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40610712452) **SUCCESS**. Seuls les fichiers propres à la préparation S1 restent dans son diff ; aucun déploiement.
- **NEXT_ACTION métier inchangée** : `P2S-NEXT-001`, revue indépendante de PR #6 puis PR #1, décision de fusion gouvernée. Pendant l'attente, sélectionner une autre tranche indépendante V0.2 (validation de provenance, tests de sécurité locale, AST, politique de cache et révision des avis) **uniquement après réconciliation des HEAD/CI/claims** ; ne pas refaire la tranche d'empreinte.
- **Blocages conservés** : pas de preuve de revue indépendante `APPROVED` sur #1/#6 ; pas de mandat de scan distant ni de commande MCP scoped de déploiement S1 ; pas de backports/runtime attestés, pas d'interface URL→PHPPATCH déployée.

## Prochaine tranche admise — proposition de mise à jour CVE (28/10/2026)

- La branche V0.2 PR #2 possède maintenant le **comparateur gouverné** `propose-catalog-update --candidate ... --as-of YYYY-MM-DD` ; HEAD exact `bf8a8bad37cc370da15706ea5331cb927c666005` ; [CI #40611408263](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40611408263) et [#40611412973](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40611412973) **SUCCESS (73 tests)**. L'analyse ne modifie jamais le catalogue, aucune autorisation de promotion implicite.
- Branche préparation S1 PR #3 mise à jour sans force : HEAD `4461048c244b60907a0b92a714dc7a59b8add38a` ; 4 CI tests/preflight **SUCCESS**. Le runbook a conservé l'historique des erreurs DNS mais précise les preuves ultérieures de résolution locale/HTTPS S1 et les pages d'attente Plesk.
- **NEXT_ACTION métier inchangée : `P2S-NEXT-001`**, obtenir une revue indépendante des PR #6 puis #1, puis gestion de fusion dans les protections. **Travaux techniques V0.2 indépendants admissibles** : consommation bornée des avis officiels avec vérification des réponses et sources, attestations runtime et backports P2, enrichissement du diagnostic et rapports ; pas de collecte non mandatée, aucune modification S1.
- La cadence horaire existante de continuité PHP2SHELL demeure la seule automatisation du projet ; ne pas ouvrir un nouvel orchestrateur ni réexécuter le comparateur déjà validé.

## Tranche la plus récente — client officiel GitHub limité et opt-in

- PR #2 V0.2 : nouveau `app/advisory_fetch.py`, CLI `fetch-official-advisory` (réseau explicitement autorisé et uniquement pour GHSA déjà validés dans catalogue). **HEAD `e02ac06fe715ac643313e4d1a0110d56129fb8d6` ; 81 tests et deux CI SUCCESS**. Les tests utilisent des réponses GitHub simulées et ne prouvent pas un appel réel au endpoint.
- PR #3 S1 : cette tranche raccordée sans rebase forcé au HEAD `708d912ad19b54a4a9410084058d9114396d591c` ; quatre CI de tests/préflight SUCCESS. Pas de connexion de l'application aux vhosts Plesk ; S1 inchangé.
- La prochaine construction V0.2 peut étendre **sans collision** le recoupement des métadonnées GitHub et des avis PHP/CERT-FR, les contrats d'attestation runtime P2 et les schémas de preuve, sans scan distant arbitraire. Le collecteur ne met jamais à jour le catalogue local automatiquement. Les tâches d'une même ressource nécessitent le claim existant et le contrôle HEAD frais.
- **P2S-NEXT-001 reste la porte de gouvernance** : vraies revues indépendantes PR #6 puis #1, CI exact SHA et décision de fusion gouvernée, sans inventer d'approbation. Récurrence horaire `6ae13640aa9c8191b20d3d120bf71ace` déjà active ; ne pas créer une seconde automation.

## Dernière construction admise — déclaration de runtime PHP/SAPI P2 (28/10/2026)

- **PR #2** : `app/runtime_evidence.py`, `tests/test_runtime_evidence.py`, `docs/V0_2_RUNTIME_EVIDENCE.md` et CLI `review-runtime-evidence --file ... --as-of ...` ajoutés. Validation stricte des fichiers locaux, schéma borné, empreinte, horodatage, version/SAPI et comparaison des deux CVE officielles ; **mandat et identité de collecte non authentifiés, runtime réel non prouvé, `asset_applicability=insufficient_evidence` invariant**. HEAD `424425116f54c353211aae554fc3866c242689b2` ; **89 tests et deux CI SUCCESS**.
- **PR #3 S1** : merge à deux parents sans réécriture de l'historique, HEAD `199641477f9fbdb3cfdfcb6c98edcaa3f60b2020` ; quatre CI de tests/preflight **SUCCESS**. Aucune application installée sur les deux vhosts S1.
- **P2S-NEXT-001 reste l'action de gouvernance prioritaire** : revue réellement indépendante des PR #6 puis #1 avant fusion ; demandes `Patricked-code` existantes ne valent pas APPROVED.
- **Prochaine tranche technique** : modèle d'attestation **authentifiée** via mandats/identités MCP autorisés, vérification effective SAPI/packages PHP et backports fournisseur, puis rapprochement des avis officiels capturés ; aucune promotion depuis un fichier JSON auto-déclaré, aucune modification à distance.
- Automatisation horaire existante `6ae13640aa9c8191b20d3d120bf71ace` conservée, relire le dernier checkpoint et le HEAD au début de chaque reprise pour éviter collisions.

## Point de reprise #017 — prévisualisation URL et dossier de remédiation à valider (28/10/2026)

- **PR #2 HEAD `4ded6646d57af4bb8f6ee11f4a7b73c828962d29`** : `audit-dossier --format json|markdown` offre un **brouillon local** d'audit combinant signaux PHP/config et runtime **déclaré**, sans divulguer secrets ni confirmer l'applicabilité CVE. `preview-url --url ...` réalise une **prévisualisation de l'entrée d'URL uniquement**, sans autorisation P1/P2 attestée, DNS/IP contrôlé ni requête HTTP. Cette étape n'est ni crawler, ni site Web, ni PHPPATCH appliqué. **113 tests / deux CI SUCCESS** [#40619000385](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40619000385) et [#40619006476](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40619006476).
- **PR #3 S1 HEAD `3739323768ca9b59a87eabe3cd96730a238c0f86`** synchronisée sans force, 4 CI tests/préflight **SUCCESS**. Aucun serveur S1 modifié et pages Plesk à la dernière observation historique.
- **P2S-NEXT-001 (unique priorité de gouvernance) inchangée :** approbation indépendante et fusion gouvernée de PR #6 puis PR #1, sans auto-approbation fictive. Les PR #2 et #3 restent draft/stacked tant que le socle n'est pas admis.
- **Tranches techniques suivantes admissibles après nouvelle réconciliation des HEAD/claims** : (1) contrats réels d'autorisation P1/P2 et contrôle URL DNS/IP à chaque connexion, sans exécution intrusive ; (2) API et frontend de campagnes authentifiées utilisant `preview-url`, avec stockage privé des mandats ; (3) moteur de dossier de remédiation PDF/PHPPATCH par diff proposé, tests isolés et approbation ; (4) protocole d'attestation SAPI/backports fournisseur ; (5) intégration Docker/MCP scoped S1 uniquement après infrastructure et mandats approuvés.
- **Reprise autonome horaire existante** `6ae13640aa9c8191b20d3d120bf71ace` conservée. Contrôler le dernier checkpoint issue #5, mandats/claims et tests au HEAD avant toute mutation ; ne créer ni tâche concurrente ni second gateway.

## Action prioritaire au checkpoint initial

**P2S-NEXT-001 — Finaliser la [PR #6](https://github.com/chainsolutions-wealthtech/Php2shell/pull/6) documentaire de continuité, puis préparer la revue/validation de PR #1 (V0.1).**

### Pourquoi cette action ?
Les phases V0.2 et S1 ont été implémentées sur des PR empilées mais les fondations V0.1 ne sont pas encore fusionnées. La mémoire ne doit pas dépendre d'une discussion ChatGPT : il faut rendre le point d'entrée et le checkpoint durables.

### Conditions d'admission
1. Relire l'issue #5 et vérifier HEAD de `main`, PR #1, PR #2 et PR #3 **en direct**, avant tout nouveau changement.
2. Vérifier l'absence d'une PR/branche/mission runtime concurrente couvrant la même action.
3. Contrôler les tests exacts du HEAD de la PR documentaire (et les références des PR concernées).
4. Ne pas écraser ni rebaser arbitrairement les PR #1 → #2 → #3 ; les conserver et vérifier leurs bases.
5. Si une autre session opère sur PR #1, privilégier le constat et le checkpoint au lieu de commencer un deuxième travail concurrent.
6. Revue humaine ou indépendante conforme à la gouvernance ; ne pas fusionner en l'absence des autorisations applicables.

### Définition de réussite
- Le point d'entrée GitHub, la charte, les décisions, l'historique, le protocole et le checkpoint existent avec liens et commits.
- Une PR documentaire autonome depuis `main` présente des tests verts et une revue prévue ; si non fusionnée, l'issue #5 donne le chemin exact de branche.
- La PR #1 a une revue/CI actualisée et un prochain geste précisément établi ; pas de fusion ou déploiement supposés.
- Le dernier commentaire de l'issue #5 contient l'**unique action prioritaire actualisée**, les HEAD et les blocages.

### Extension de périmètre confirmée — sans nouvelle tâche active

Le besoin utilisateur « saisir l'URL d'un site en frontend → auditer les pages autorisées → détecter les indices PHP et évaluer les CVE avec preuves → produire un dossier de remédiation → soumettre un patch proposé via PHPPATCH » est enregistré dans `continuity/URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md` et les exigences **REQ-023→REQ-032**. Ces étapes enrichissent V0.2/V0.3/V0.4/V1.0, **ne remplacent pas** le prochain geste `P2S-NEXT-001`, et **ne sont pas implémentées** à ce checkpoint.

### Catalogue exécutable-intentionnel (non encore mis en file runtime)

Le backlog [`WORK_PACKAGES.json`](WORK_PACKAGES.json) contient **61 work packages planifiés** avec dépendances et gates, répartis sur huit axes documentés dans [`INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md`](INTELLIGENT_MULTIDIRECTIONAL_WORKFLOW.md). Cela permet ultérieurement des flux multidirectionnels, le retour des tests et la proposition de nouvelles tâches. **Ce catalogue n'admet et n'exécute aucune tâche** et ne remplace pas le **prochain geste unique P2S-NEXT-001** : revue indépendante PR #6 puis PR #1 V0.1 dans l'ordre gouverné.

### File des jalons ultérieurs (non actifs tant que précédents non admis)
- V0.2 : AST PHP, `composer.lock`, configurations, catalogue CVE officiel et preuves.
- V0.3 : propositions de patches, tests en Docker isolé, approbation et rollback.
- V0.4 : MCP existant, déploiement gouverné sur deux vhosts S1, sécurité et observabilité.
- V1.0 : interface Web PHP2SHELL + PHPPATCH, moteur commun, projets, rapports/historique.

**Règle :** ce fichier est un snapshot de reprise. Le dernier checkpoint GitHub ne remplace pas une observation de la réalité GitHub/S1 avant action.


## Dernière tranche technique indépendante — reporting runtime déclaré CSV (28/10/2026)

- **PR #2** HEAD `e5df6bb8761584716a60bab9067c880276b97b14` : module `app/runtime_reporting.py`, `review-runtime-evidence --format csv`, sept tests de reporting, documentation `docs/V0_2_RUNTIME_CSV_REPORT.md`. **96 tests** au HEAD, CI [40616269007](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616269007) et [40616272906](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616272906) SUCCESS.
- **PR #3** HEAD `2d3d2c9107a5b2c9ac2fdfcc6239083bbba8211b` : branche S1 resynchronisée par merge à deux parents, sans force, fichiers propres S1 conservés. CI [40616321539](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616321539), [40616321597](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616321597), [40616327531](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616327531), [40616327538](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40616327538) SUCCESS.
- La sortie CSV **n'atteste ni mandat, ni runtime HTTP, ni signature, ni backport, ni applicabilité CVE**. Seuls des champs autorisés sont exportés avec protection anti-formules. JSON historique conservé. **REQ-019 demeure PARTIELLE** : PDF, dossier de remédiation et flux PHPPATCH non livrés.
- **P2S-NEXT-001 inchangée** : revue réellement indépendante PR #6 puis PR #1 avant fusion gouvernée. Les 6 lots, 32 exigences, 61 work packages, V0.1→V1.0, workflow URL→audit autorisé→PHPPATCH, Docker isolé, moteur partagé et les deux sous-domaines S1 demeurent au programme, sans déploiement attesté.
- MCP read-only `ping` a exigé une interaction de connexion indisponible dans cette exécution ; aucune sonde S1 ni claim runtime MCP n'est prétendu vérifié. La construction GitHub s'est appuyée sur le mandat utilisateur explicite, les branches existantes et le contrôle `expected_sha` anti-collision. Aucun nouvel agent/claim/gateway créé.


## Reprise après construction du handoff local PHPPATCH — 28/10/2026 (P2S-EVT-025)

- **PR #2 V0.2** : HEAD `fc277eb8b8f1a277a606826e48bbf673028f8449` ; `app/dossier_handoff.py`, `tests/test_dossier_handoff.py` et `docs/V0_2_PHPPATCH_HANDOFF.md` ajoutés sans modifier les commandes antérieures. **122 tests** au SHA exact, CI [push #40622112932](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40622112932) et [PR #40622118348](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40622118348) SUCCESS.
- **PR #3 S1** : HEAD `686e68980c5807ca84bcdf4ef1e8a2f046fe09f8`, merge à deux parents (PR #3 précédent + PR #2 actuel), `force=false`, trois fichiers spécifiques S1 conservés. Quatre CI exact SHA #40622188626/#40622188699/#40622194348/#40622194350 SUCCESS ; 122 tests sur le job unit vérifiés.
- **PHPPATCH non déployé** : seule une file de revue locale **non authentifiée** existe, sans code source exporté, génération de patch, Docker, revue, application ou autorisation. REQ-029/030 restent **PARTIELLES**, jamais DONE. Empreinte SHA-256 = cohérence, pas signature.
- MCP : ping/réconciliation read-only réussis le 28/10 vers 02:39 UTC, les deux sous-domaines sont inventoriés sous `wealthtechinnovations.com`, mais **aucun outil scoped PHP2SHELL/PHPPATCH n'est exposé** ; inventaire des tâches MCP distinct de l'autorité du dépôt PHP2SHELL. Aucune opération serveur effectuée.
- **P2S-NEXT-001 inchangée** : revue indépendante des PR #6 puis #1 et décision de fusion gouvernée. Sous-tranche technique suivante seulement après nouvelle vérification des HEAD, CI, mandats/claims et absence de collision : corpus de preuves locales et modèle d'autorisation P1/P2 ou validation du contrat de dossier, sans scan ni déploiement. Les 6 lots, 32 exigences, 61 work packages et les versions V0.1→V1.0 demeurent conservés.


## Checkpoint de construction V0.2 — seconde console statique PHPPATCH (28/10/2026)

- **P2S-NEXT-001 demeure l'unique priorité de gouvernance** : obtenir une revue humaine réellement indépendante de PR #6, puis PR #1, vérifier exact HEAD/CI et décider des fusions selon les protections. Les revues historiques COMMENTED et une identité alternative du même propriétaire ne valent pas approbation.
- **PR #2** : `web/phppatch/index.html`, `tests/test_phppatch_frontend_static.py` et `web/README.md` complétés sur HEAD `daeca8bff5b776f497e7323e0ab92041b895347a`. Console **statique sans connexion** et quatre boutons désactivés ; 5 tests supplémentaires, **153 tests** et deux CI SUCCESS [#40627849277](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40627849277) / [#40627853683](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40627853683). Le prototype PHP2SHELL existant est conservé.
- **PR #3** : divergence constatée au checkpoint #019 **résolue** par merge à deux parents `a7d62aae30908533409cf7931f248ab2ae1a489b` (ancien PR #3 + nouveau PR #2), ref contrôlée `expected_sha` / `force=false`. Diff PR #2→#3 = **uniquement** les trois fichiers S1 d'origine. Quatre CI au HEAD exact SUCCESS [#40627886714](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40627886714), [#40627886718](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40627886718), [#40627892087](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40627892087), [#40627892033](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40627892033).
- **Prochaine tranche technique non concurrente**, après nouvelle admission HEAD/claims : backend local de lecture de dossier avec schéma strict et stockage privé des mandats, ou tests négatifs P1/P2 et moteur de rapports, **sans** connexion réelle, scan tiers ni élévation de confiance ; les actions serveur/déploiement attendent des capacités MCP scoped et les approbations applicables.
- **Aucun mandat runtime MCP ni claim d'exécution serveur vérifié ici** : autorisation utilisateur de construction limitée aux PR GitHub existantes et contrôle des références Git. Ni approbation, ni moteur API/Web connecté, ni conteneur Docker, ni patch, ni déploiement S1. Les 6 lots, 32 exigences, 61 packages, V0.1→V1.0, URL→audit autorisé→diagnostic→PHPPATCH, moteur partagé et les deux sous-domaines restent inchangés.

## Construction de sécurité V0.2 — précontrôle DNS/redirects local (P2S-EVT-028, 2026-10-28)

- **PR #2** : `app/network_preflight.py`, `tests/test_network_preflight.py`, `docs/V0_2_URL_INTAKE_PREVIEW.md` enrichis additivement. Les snapshots A/AAAA fournis localement n'acceptent plus de hostname privé/réservé/IP littérale, ni d'URL cachée dans le champ DNS. IPv6 transition (mapped/6to4/Teredo) bloquées par politique conservatrice. `check_same_origin_redirects(..., allowed_base_path="/app")` est une option additive : refuse les échappements `/application` et `/`, tout en préservant les anciens appels sans scope.
- **Tests** : 153 → **157 tests** au HEAD `fa1332b0d48c9147ce03f48ba3b3783fe623f3c4`, CI [#40633403515](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633403515) / [#40633408996](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633408996) **SUCCESS**, journal du job `122634787167` : `Ran 157 tests ... OK`.
- **PR #3** : merge commit à deux parents `11edd0e4b4ca30931d425f26f37ce91e3ee83e42`, parent PR #3 précédent + PR #2 actuel ; mise à jour `force=false`, `expected_sha`, diff PR #2→PR #3 = uniquement les 3 fichiers S1 d'origine ; 4 CI [#40633467853](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633467853), [#40633467926](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633467926), [#40633472052](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633472052), [#40633472066](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40633472066) **SUCCESS**. Aucune modification Plesk/S1.
- **Limites** : analyse purement locale et syntaxique, pas de résolution DNS, validation du pair/TLS, crawl, authentification de mandat P1/P2 ou claim MCP runtime. **P2S-NEXT-001 inchangée** : revue humaine indépendante PR #6 puis PR #1 avant décision de fusion. Les travaux techniques non concurrents V0.2 peuvent continuer après réconciliation ; ne pas promouvoir ce précontrôle en scanner SSRF-safe.
- **Programme inchangé** : V0.1→V0.2→V0.3→V0.4→V1.0, six lots, 32 exigences, 61 work packages, URL→audit explicitement autorisé→diagnostic→PHPPATCH, moteur partagé, Docker isolé et destinations S1 `php2shell.wealthtechinnovations.com` / `phppatch.wealthtechinnovations.com`.

## Reprise après contrat API local et proposition PHPPATCH — 28/10/2026

- PR #2 HEAD `ac0b35588c950d675fe89c70fbc8d434c0594d20` ; `164` tests historiques + `9` tests API **SUCCESS**, quatre CI au SHA exact. Contrat FastAPI uniquement local, désactivé par défaut, sans authentification ni endpoint scan ; nouvelle proposition de diff `display_errors` à partir d'un constat PHP2SHELL validé, **sans écriture fichier**.
- PR #3 HEAD `6fd0cd9aa5cf3be2e47f779e4ba1d167df35ffd0`, intégration additive non forcée du contrat API et du diff local, **six CI tests/API/readiness SUCCESS** au SHA exact ; aucun serveur cible n'a été modifié.
- **Priorité unique de gouvernance `P2S-NEXT-001` inchangée** : revue véritablement indépendante de PR #6 puis #1, puis décision de fusion sans contourner protections ni simuler APPROVED.
- **Tranches techniques suivantes admissibles après vérification HEAD/claims** : vrai RBAC et mandats via les autorités MCP existantes ; storage PostgreSQL avec isolation des projets/secret handling ; worker Redis et contrôle des connexions anti-SSRF sous mandat ; catalogue/résolution fournisseur et véritable preuve PHP SAPI ; génération de patches sur dépôt isolé, lint/tests Docker, validation indépendante, rollback ; deux frontends branchés et HTTPS S1 après intégration approuvée. La simple maquette API ne vaut pas un déploiement V1.0.
- Aucune nouvelle automation : cadence horaire PHP2SHELL existante reste l'unique point de reprise. 61 packages, 32 exigences, cinq versions, six lots, moteur commun et cibles S1 préservés.


## Suite du durcissement FastAPI borné — P2S-EVT-031 (2026-10-28 UTC)

- **PR #2 HEAD `227915fda5379200232ec6a2a968351512fb9153`** ; 164 tests historiques + **12 tests API** et CI push/PR SUCCESS : [#40635830633](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635830633), [#40635830627](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635830627). La limite de taille HTTP de 4 Kio est désormais une limite d'octets ASGI effectivement lus ; la CI RED du commit tests seul a été conservée comme preuve avant correction.
- **PR #3 HEAD `fdc1e87c009eca22a294cc1bfe4b558648df9b77`** : merge à deux parents, force=false, anciens trois fichiers S1 préservés ; 6 CI tests/API/S1-readiness SUCCESS, notamment [#40635894060](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40635894060), comparaison `behind=0`. Aucune action S1 effective.
- **P2S-NEXT-001**, priorité unique de gouvernance, **toujours ouverte** : obtenir une revue indépendante réelle des PR #6 puis #1 et décider des fusions avec vérification des protections/HEAD/CI. Les tests verts ne se substituent pas à cette revue.
- **Prochaines tranches techniques admissibles après nouvelle réconciliation et admission sans collision** : modèle P1/P2 authentifié (pas de token fictif) ; schéma de stockage privé des mandats et isolation projets ; contrats projets/campagnes et exposition Web seulement après auth réelle ; tests E2E de limites sous serveur et reverse proxy, budgets/timeout ; protections DNS-rebinding/pair réel en environnement autorisé ; rapports PDF local anonymisé ; sandbox de patch non exécutante puis tests sous mandat. Ne pas mettre en ligne l'API actuelle.

## P2S-EVT-032 — garde-fou PHPPATCH hors ligne (28/10/2026 UTC)

- PR #2 `6a41ef5c15ef78af95afa0aeda3561fd5c33dd8c` : proposition ini refuse les paramètres `display_errors` dupliqués actifs, commentaires et tabulations préservés, **166 historiques + 12 API**, CI #40636281308/#40636281249 SUCCESS. PR #3 `3bccdf0b4d776ba399621debbdc48488685e5eb6` : fusion deux parents sans force, six CI SUCCESS, fichiers S1 préservés. CI RED du test préalable #40636184215 conservée.
- **Priorité de gouvernance toujours `P2S-NEXT-001` : vraie revue indépendante PR #6 puis PR #1, suivi d'une décision de fusion gouvernée**. Les preuves de test sur PR #2/#3 ne remplacent ni la revue, ni les droits de production.
- Prochain travail indépendant admissible : renforcer la cohérence du dossier local et des preuves des diffs PHPPATCH, contrats de permissions P1/P2 **non exécutants**, et recettes de non-divulgation ; réserver serveur, réseau, sandbox/PR corrective et S1 aux mandats MCP et revues réellement attestés. Ne pas déclencher de seconde automation ou agent concurrent.


## Tranche P1/P2 — P2S-EVT-033 (28/10/2026)

- Construits sur PR #2 : cinq contrôles d'intention distincts, refus par défaut des assertions forgées, cinq tests supplémentaires, 171 tests CLI + 12 API, CI vertes ; PR #3 synchronisée (6 CI vertes). Aucun `ALLOW`, aucune création de compte, aucune activation réseau.
- **P2S-NEXT-001 reste unique** : faire examiner PR #6 puis PR #1 par une véritable identité indépendante, fusion seulement après revue et contrôles.
- **Travail technique suivant** : identifier et raccorder un vrai vérificateur d'identité/mandat P1/P2 à l'autorité existante, contrôler signature/audience/issuer, l'appartenance projet-ressource, révocation/expiration, claims, quotas, et produire tests de refus et d'admission. Le MCP interrogé ne fournit pas encore de capacité PHP2SHELL attestée. Les workers, scans, patches actifs et S1 restent interdits jusqu'à admission effective.


## P2S-EVT-034 — prochain jalon réel après vérificateur Ed25519

- Code et tests : vérificateur externe JWS Ed25519 **local** intégré à PR #2 `cb705a82` (10 tests auth SUCCESS, 171 tests historiques et 12 tests API SUCCESS) ; PR #3 `c22ac964` synchronisée, sans écriture S1.
- **P2S-NEXT-001 inchangée :** obtenir la vraie revue indépendante de PR #6, puis PR #1, avant décision de fusion. Aucune approbation simulée.
- **Dépendance d'authentification réelle à résoudre :** trouver un émetteur d'identité et un mécanisme d'attestation signé déjà admis par le MCP/IdP, définir un trust-store de clés publiques **côté serveur** et rotation, liaison à la session utilisateur et à l'ACL projet, révocation live, claim MCP et contrôles de ressources. Le prototype ne fournit pas ces éléments et ne doit pas être exposé comme une permission d'opérer.
- Toute application/scan/crawl S1 reste interdite sans mandat explicite et mécanisme réellement exécutable.


## P2S-EVT-035 / P2S-EVT-036 — garde-fous avant admission live

- Contrat signé hors ligne désormais compatible avec `base_path` exact ; P1 `public_crawl` exige une portée de chemin et des plafonds signés `max_pages` / `requests_per_minute`. **20 tests auth** cumulés, 171 CLI et 12 API (PR #2 `53e4378`). P1 sans budgets signés est refusé, aucune opération réseau activée.
- Suivi : PR #3 `d48f880` synchronisée sans force, readiness S1 inchangée, ne signifie pas déploiement. **P2S-NEXT-001**, revue indépendante réelle PR #6 puis PR #1, reste la prochaine décision de gouvernance.
- Prochain travail authentification réelle : vérifier l'existence d'une autorité d'identité et de mandats, un magasin de clés publiques et une révocation live réellement gouvernés, puis brancher les décisions sur une ACL projet/asset et claims MCP audités. Aucune de ces opérations ne peut être remplacée par le prototype Ed25519 local ni par un flag frontend.

## P2S-EVT-037 — contrôle Composer local sans régression (2026-10-28 UTC)

- PR #2 `7f6ae451c1129d0b6a1a0c103f2f91659d26e55b` : nouveau module indépendant `python -m app.composer_consistency --path <répertoire autorisé>`, 17 tests nouveaux ; **188 tests historiques + 12 API + 20 auth** au HEAD. Six CI push/PR tests/API/auth SUCCESS ; aucune dépendance ou CLI existante remplacée.
- PR #3 `8a5ba2dee04a93a07a99229b254159c76673b439` : merge non forcé avec `expected_sha`, 3 blobs S1 historiques préservés, comparaison `behind=0`, huit CI exact SHA SUCCESS (tests/API/auth/S1-readiness). **Aucun déploiement S1**.
- **P2S-NEXT-001 demeure la priorité unique** : obtenir une revue réellement indépendante de PR #6 puis #1, vérifier protections et CI exact SHA avant toute décision de fusion. Ne pas utiliser le compte alternatif du même propriétaire pour simuler une indépendance.
- Tranche technique indépendante suivante admissible après réconciliation et contrôle anti-collision : compléter le diagnostic de cohérence Composer sur fixtures locales et proposer une intégration au dossier d'audit **uniquement après revue du contrat et des règles de confidentialité**, ou avancer les tests AST et faux positifs sans toucher à la gouvernance P1/P2 en cours. Aucune connexion réseau, exécution PHP, correctif ni accès S1 sans mandat authentifié et gates MCP.


## P2S-EVT-038 — adoption réelle du contrôle d'identité P1/P2 (après tranche de code)

- **Produit maintenant dans PR #2 `a14968d`** : adaptateur offline reliant les preuves JWS Ed25519 aux cibles HTTPS canoniques, sous-chemins, plafonds P1, référence de mandat P2 exacte et utilisateur/projet attendu du backend ; 8 nouveaux tests et 28 auth cumulés, 188 historiques, 12 API ; PR #3 `f87eb7e` à 8 CI verts, readiness S1 inchangée.
- **Autorité externe absente :** l'inventaire des 138 outils MCP exposés n'offre pas de service attesté de vérification des utilisateurs/mandats PHP2SHELL. Les governed sessions/oauth_subject concernent les agents MCP ; aucune preuve de réutilisation comme IdP client PHP2SHELL. **Ne pas exposer le prototype comme authentification réelle.**
- **Prochaine dépendance concrète** : définir et approuver l'IdP des utilisateurs, le modèle d'ACL projet/actif et le service gouvernemental de délégation, vérifier les permissions des installations GitHub réellement utiles, fournir un trust-store serveur et une révocation live, puis tester une vraie session et un vrai mandat P2 en environnement isolé, avant toute permission réseau.
- La **priorité gouvernée P2S-NEXT-001 ne change pas** : vraie revue indépendante PR #6 puis #1, CI exact SHA avant fusion, sans compte alternatif du même propriétaire en guise de revue indépendante.


## P2S-EVT-039 — prochain jalon simplicité d'usage

- Prévisualisation débutant hors ligne effectivement construite : trois étapes lisibles et réglages avancés repliés ; PR #2 `69cbbc6`, PR #3 `97808da`, CI toutes vertes.
- **Parcours produit cible à construire :** entrée URL sans inscription et sans réseau ; connexion unique via IdP approuvé lorsqu'une analyse réelle est demandée ; vérification self-service de la propriété/délégation sur domaine ou dépôt par mécanisme externe fiable ; mandat P1/P2 et quotas invisibles au débutant mais appliqués côté backend ; rapport clair, PHPPATCH avec autorisation distincte pour patch et déploiement. Ne pas promettre un audit sur n'importe quel site non autorisé.
- **P2S-NEXT-001** reste la revue indépendante réelle PR #6 puis PR #1, sans auto-approbation. En parallèle, définir les capacités d'IdP et de registre d'actifs pour un vrai onboarding et des contrôles d'autorité. Ne pas confondre une maquette compréhensible avec une plateforme utilisable en production.


## P2S-EVT-040 — jalons après premier moteur de réponse courte

- **Acquis réel (hors ligne)** : résumé anonyme sans conservation + API locale non exposée, PR #2 `dc2a61d`, PR #3 `ddc8871` ; 199 CLI/17 API/28 tests auth et CI vertes, aucune fausse autorisation.
- **Prochaine tranche décisive** : un collecteur HTTP P1 réellement gouverné et limité (cadre légal/mandat, protection SSRF à chaque connexion, résolution IP publique, DNS rebinding/redirects, robots, quotas, rate limits, pause/stop, preuve réelle de collecte), qui alimente le moteur de synthèse ; **ne pas utiliser l'API locale comme scanner public**.
- Ensuite, pour respecter `P2S-UX-002` : connexion réelle et simple, stockage de rapport détaillé strictement lié au compte vérifié, preuve de propriété du domaine ou mandat distinct, connexion facultative au dépôt GitHub avec permissions minimales, raccordement privé P2 et autorisations spécifiques pour PHPPATCH.
- **P2S-NEXT-001 demeure l'approbation indépendante PR #6 puis #1 avant fusion** ; préparer les tests des nouvelles tranches en parallèle sans se faire passer pour une revue indépendante.


## P2S-EVT-041 — après normalisation HTTP locale (28/10/2026)

- **Acquis sur PR #2 `6ca14032`** : transformation hors ligne de couples d'en-têtes HTTP fournis vers des indicateurs non vérifiés, sans valeurs de headers, cookies, URL de redirection, secrets, accès réseau ni sauvegarde. 12 tests ajoutés, **211 CLI + 17 API + 28 auth**, six CI SUCCESS au SHA exact. PR #3 `92053ae7` synchronisée sans force, 8 CI SUCCESS, trois fichiers S1 préservés. La chaîne fonctionne uniquement avec des **données déclarées**, pas une collecte réelle.
- **Priorité unique `P2S-NEXT-001` inchangée** : obtenir une revue indépendante réelle PR #6 puis PR #1 et décider des fusions selon protections et HEAD exacts. Aucune approbation alternative du même propriétaire.
- **Prochaines tranches indépendantes admissibles** : tests isolés de collecte HTTP P1 et de refus SSRF, sans réseau réel avant autorité et claim vérifiés ; identité/ACL et rapports privés réels restent à admettre. Ne pas exposer l'API locale, ne pas déployer S1, ne pas reclasser les exigences comme DONE. Vérifier les branches et la concurrence avant chaque écriture.

## Point de reprise après CI V0.3 rétablie — P2S-EVT-042/043

- La CI rouge documentée au checkpoint #033 a été corrigée **sans désactiver le test** : commande CLI `rehearse-config-patch` ajoutée, 218 tests verts. Puis nouveau contrat `prepare-patch-review` avec dossier/handoff/diff/rollback en mémoire, **226 tests verts** sur PR #2 HEAD `66aed9bdc742b7cb3ca7dfe705606ff58285fcf8`, CI [#40650745805](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40650745805). Les tests API et auth conservent leurs contrats acquis.
- PR #3 HEAD `f11be476228573a1760ec6307351f625cffc7ca0`, synchronisée et 8 CI tests/API/auth/readiness au HEAD **SUCCESS**, sans action S1.
- **P2S-NEXT-001 reste la priorité de gouvernance** : revue réellement indépendante PR #6 puis PR #1, sans présenter les comptes du même propriétaire comme deux réviseurs indépendants. Aucune fusion sans approbation requise, HEAD exact, tests et protections.
- **Tranches V0.3 non admises à l'exécution** : mandat/claim P2 réel, workspace isolé et tests PHP/Docker sur candidat, revue humaine du diff et création de PR corrective gouvernée, rollback de fichier/service, déploiement contrôlé. Les simulations de rollback en mémoire ne prouvent pas un rollback opérationnel. Crawler P1 réel et S1 restent également dépendants du vérificateur d'autorité/IdP et des sécurités de connexion au pair.
- Automation horaire existante `6ae13640aa9c8191b20d3d120bf71ace` conservée : reconsulter l'issue #5, HEAD/CI/reviews/claims au déclenchement, puis poursuivre les travaux indépendants admissibles sans dupliquer une PR ni un agent.

## Reprise après P2S-EVT-044 — paquet PHPPATCH revalidé hors ligne (28/10/2026)

- PR #2 `04990f12d6713d601d2421d4c779bf85c42982f7` : nouveau vérificateur local des paquets de revue, 8 tests ajoutés, **234 tests** réussis et six CI tests/API/auth SUCCESS au HEAD. Ne pas refaire cette tranche. Un paquet concordant ne constitue jamais une autorisation ou approbation.
- PR #3 `414863480a076cb22a314a570102135a2a2c128d` : synchronisée sans force, seulement trois fichiers S1 additionnels et inchangés, huit CI exact SHA SUCCESS ; readiness en lecture seule, pas de déploiement.
- **NEXT_ACTION unique `P2S-NEXT-001` inchangée** : obtenir une vraie revue indépendante de PR #6 puis PR #1, contrôler les protections et décider des fusions selon gouvernance. Aucune auto-approbation via le second compte du même propriétaire.
- Tranche technique suivante, uniquement après nouvelle réconciliation des HEAD, mandats et claims : tests isolés du transfert PHPPATCH et contrôle de provenance des données/rapports, ou préparation documentée d'une sandbox Docker non exécutante ; ne pas déclencher d'opération réseau, patch appliqué, PHP exécuté, compte utilisateur, vhost ou S1 sans autorité réelle. L'accès MCP a demandé une interaction non disponible ici.

## Reprise après P2S-EVT-045 — PHPPATCH CLI (28/10/2026 UTC)

- **Ne pas reconstruire** `verify-patch-review` : la commande de revalidation locale est implémentée sur PR #2 HEAD `26121997f175f88cb92f1907296ae2364222c95a`, 5 tests supplémentaires, **239 tests** et six CI SUCCESS au SHA exact. Elle ne confère aucune autorité.
- **PR #3** synchronisée au HEAD `d2d501d78b42ccc579a72f0b7befdbfd90a1d894`, huit CI SUCCESS, trois blobs S1 préservés, aucun déploiement.
- **Action prioritaire unique `P2S-NEXT-001` inchangée** : vraie revue indépendante PR #6 puis #1, ensuite décision de fusion gouvernée au HEAD courant. Aucune auto-approbation avec les deux comptes du même propriétaire.
- **Prochaine tranche indépendante admissible** : renforcer les tests négatifs des preuves locales et préparer les contrats de sandbox Docker **sans exécution, scan, accès S1, changement de source ou promotion de statut** ; vérifier les claims et le HEAD juste avant toute écriture, garder les branches empilées convergentes. Le moteur PHPPATCH reste non opérationnel en production.


## Reprise après P2S-EVT-046 — paquet PHPPATCH, contrôle FD et refus des fichiers spéciaux

**28/10/2026 UTC — P2S-EVT-046 — PR #2 03b45fdc2cf40e3276208935b47a785ef320a27d, PR #3 d2529e6b5c87588fe0192daed8718d9657fda6de.** Renforcement défensif hors ligne de `app/patch_packet_verifier.py` : ouverture du paquet local par descripteur avec `O_NOFOLLOW` et `O_NONBLOCK`, vérification `fstat` du type fichier régulier, borne effective de 16 Kio et détection de changements observables pendant la lecture. Refus conservateur si `O_NOFOLLOW` indisponible. Trois tests ajoutés : FIFO/répertoire, substitution de symlink entre précontrôle et ouverture, croissance pendant lecture ; documentation `docs/V0_3_PATCH_PACKET_VERIFICATION.md` actualisée. **242 tests applicatifs SUCCESS** sur PR #2, six workflows tests/API/auth au SHA exact : #40666411620/#40666411562/#40666411739/#40666419373/#40666419455/#40666419560. PR #3 synchronisée sans force par merge à deux parents, `behind=0` et uniquement trois blobs S1 historiques conservés ; huit workflows SUCCESS : #40666529156/#40666529189/#40666529254/#40666529325/#40666539588/#40666539650/#40666539803/#40666539804. Aucun scan réseau, correctif appliqué, source modifiée, conteneur démarré, fusion main ou déploiement S1. Le lecteur n'est pas une preuve d'atomicité totale face aux mutations des répertoires parents, ni une attestation d'identité/mandat/approbation. La tentative MCP `ping` a demandé une authentification interactive non disponible : aucun claim runtime/S1 authentifié. PR #1 et #6 toujours en attente de revue réellement indépendante ; demandes `Patricked-code` ne valent pas approbation. Programme intégral V0.1→V0.2→V0.3→V0.4→V1.0, six lots, 32 exigences, 61 WP, parcours URL→audit autorisé→diagnostic→PHPPATCH, moteur partagé, Docker isolé et destinations `php2shell.wealthtechinnovations.com` / `phppatch.wealthtechinnovations.com` préservés. **REQ-030 / REQ-032 et P2S-WF-R06 / P2S-WF-Q01 : preuves partielles uniquement, aucun statut DONE.** `P2S-NEXT-001` reste la revue indépendante de PR #6 puis PR #1 avant toute décision de fusion.

**Prochaine tranche indépendante admissible** : corpus de tests négatifs des dossiers et fichiers locaux ou spécification de la future sandbox Docker non exécutante, sur PR #2/#3 uniquement après vérification des HEAD, CI et claims. Aucune exécution PHP/Docker ou opération S1 sans autorité attestée. Ne pas reconstruire la présente tranche.
