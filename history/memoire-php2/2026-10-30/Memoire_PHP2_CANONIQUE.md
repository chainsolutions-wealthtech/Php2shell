# Memoire PHP2 — Registre canonique exploitable

> **Qualification :** transcription structurée du document fourni par l’utilisateur (historique établi dans sa source). Aucune vérification GitHub/S1 supplémentaire n’a été exécutée pour constituer cette édition. Les preuves absentes restent absentes.

## 1. Identité et autorités

- Nom de la mémoire : **Memoire PHP2** (`MEMOIRE-PHP2`).
- Programme : **Programme Directeur Intégral PHP2SHELL–PHPPATCH**.
- Continuity ID : `PHP2SHELL-CONT-20261027-ROOT-01`.
- Point de départ historique : **22/10/2026** ; création de la continuité canonique : **27/10/2026**.
- Dépôt : [https://github.com/chainsolutions-wealthtech/Php2shell](https://github.com/chainsolutions-wealthtech/Php2shell).
- Ancrage des décisions et checkpoints : [issue #5](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5).
- Archivage historique progressif : [PR #7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7).
- Continuité documentaire : [PR #6](https://github.com/chainsolutions-wealthtech/Php2shell/pull/6).
- Source du présent paquet : `sources/SOURCE_20261029_reconstitution_integrale.txt`, SHA-256 `9154b71a3e0bc408d742bce6f29990811f6cc96b64d456beffd1a8b870374de4`.

## 2. Règles de vérité et de qualification

1. Une **décision** n’est pas une preuve de réalisation.
2. Un **commit** prouve un changement versionné, pas une admission, une exécution CI réussie ni un déploiement.
3. Un **test local rapporté**, une **CI verte**, une **approbation** et une **preuve runtime S1** sont quatre états distincts.
4. Les champs manquants restent `null`, `non_precise_dans_le_document_fourni` ou `a_reconcilier` ; ils ne sont jamais complétés par présomption.
5. L’issue #5 et les registres natifs GitHub demeurent les autorités canoniques du projet ; cette mémoire est une **copie structurée**, sans substitution de source.
6. Toute évolution future doit être **additive**, éviter les collisions inter-agents et préserver les gouvernances distinctes MCP, GRT et PHP2SHELL ; pas de Codex/Copilot.

## 3. Données quantifiées : photographie historique, pas état live

| Mesure | Valeur rapportée | Qualification |
|---|---:|---|
| Événements canoniques | 52 | EVT-001 à EVT-052 dans le document |
| Décisions | 24 | P2S-DEC-001 à P2S-DEC-024 |
| Work packages | 61 | 8 axes, 60 PLANNED_NOT_ADMITTED et G01 AWAITING_INDEPENDENT_REVIEW |
| Checkpoints numérotés | 40 | #001 à #040, avec addenda non renumérotés |
| Exigences mentionnées | 32 | REQ-001 à REQ-032 ; liste/mapping individuels non reproduits |
| Branches | 6 puis 7 | 7 après détection de la PR #7 |
| Commits uniques | 346 puis ≥ 348 | Inventaires successifs du document, non revérifiés ici |
| Entrées de commits multi-branches | 515 | Inventaire initial avant PR #7 |
| GitHub Actions runs | 988 | Inventaire initial ; journaux non tous vérifiés |
| Pull requests | 4 puis 5 | Avant/après PR #7, photographie documentaire |
| Issues, PR incluses | 6 | Inventaire initial |
| Commentaires issue #5 | 48 | Inventaire initial |

## 4. Arbre hiérarchique de reconstitution

```text
Programme Directeur Intégral PHP2SHELL–PHPPATCH
└── PHP2SHELL-CONT-20261027-ROOT-01
    ├── Autorités (dépôt / issue #5 / PR #6 / PR #7)
    ├── Mandats et périmètre initial (depuis 22/10/2026)
    ├── Décisions P2S-DEC-001..024
    ├── Exigences REQ-001..032 [mapping source natif requis]
    ├── Work packages P2S-WF-... (61 ; dépendances et statuts)
    │   ├── G Gouvernance (9)
    │   ├── S Sécurité et autorisations (8)
    │   ├── E Analyse / campagnes / CVE (12)
    │   ├── R Remédiation PHPPATCH (7)
    │   ├── I Infrastructure / backend / MCP (8)
    │   ├── U Interfaces (6)
    │   ├── Q Qualité / recette (5)
    │   └── O Exploitation / supervision (6)
    ├── Événements EVT-001..052
    ├── Branches / PR / commits (dossiers de diff individuels à compléter)
    ├── Tests et GitHub Actions (preuves exact SHA à compléter)
    ├── Checkpoints #001..040 et addenda
    ├── Périmètres / claims / admissions / décisions d’approbation
    ├── Preuves DNS, TLS, Docker, Plesk et runtime S1
    └── Dossiers de contrôle, écarts et prochaines actions
```

## 5. Chronologie exhaustive des événements retrouvés (52)

Chaque ligne reproduit les formulations de la source ; l’identifiant et la date proviennent du document fourni.

| ID | Date | Construction / opération décrite | Résultat / limite |
|---|---|---|---|
| `EVT-001` | 2026-10-22 | Demande de création d’un agent d’audit et de remédiation PHP. Création du dépôt public `Php2shell`, avec laboratoire fictif et périmètre défensif. | Dépôt créé ; analyse de tiers non autorisée. |
| `EVT-002` | 2026-10-22 | Construction initiale V0.1 : CLI Python, fonctions de diagnostic, tests, Dockerfile, laboratoire PHP, CI et documentation. Ouverture de la PR #1. | Prototype local, non déployé. |
| `EVT-003` | 2026-10-27 | Confirmation des cinq versions du programme. Construction initiale du scanner lexical PHP local, inventaire Composer, exclusions de parcours, tests et documentation V0.2. | Développé hors ligne, sans AST complet ni audit réseau. |
| `EVT-004` | 2026-10-27 | Création des deux sous-domaines `php2shell.wealthtechinnovations.com` et `phppatch.wealthtechinnovations.com` sur S1 ; vérifications DNS, TLS et HTTPS. | Préparation d'hébergement, pas déploiement des applications. |
| `EVT-005` | 2026-10-27 | Audit DNS : comparaison des serveurs autoritaires, récursifs et de la connexion directe S1 avec SNI ; identification d'anciens enregistrements et de caches. | Anomalie de résolution locale S1 encore signalée. |
| `EVT-006` | 2026-10-27 | Création du workflow S1 de précontrôle DNS/TLS/redirections, du plan Docker isolé et ouverture de la PR #3. | Readiness uniquement, sans publication applicative. |
| `EVT-007` | 2026-10-27 | Ouverture de l'issue #4 pour les prérequis et preuves du déploiement gouverné S1. | Suivi créé, déploiement non exécuté. |
| `EVT-008` | 2026-10-27 | Consolidation de `docs/ROADMAP.md` : V0.1 à V1.0, sans suppression des capacités historiques. | Décision matérialisée dans la documentation. |
| `EVT-009` | 2026-10-27 | Décision de traçabilité inter-conversations ; création de l'issue canonique #5. | Ancrage durable créé. |
| `EVT-010` | 2026-10-27 | Création des fichiers de continuité, de leurs tests et de la PR #6 indépendante. | Infrastructure documentaire, `main` inchangée. |
| `EVT-011` | 2026-10-27 | Réconciliation de la mission fondatrice : six lots, campagnes à grande échelle, P1/P2, analyse passive, CVE, source/runtime, API, base, workers et supervision. Création de la première matrice REQ-001 à REQ-022 et du registre CVE. | Périmètre rétabli, fonctionnalités non toutes réalisées. |
| `EVT-012` | 2026-10-27 | Décision d'ajouter le parcours URL → analyse des pages autorisées → diagnostic PHP/CVE → dossier de remédiation → PHPPATCH. Création des exigences REQ-023 à REQ-032. | Contrat cible rédigé, pas de scan actif. |
| `EVT-013` | 2026-10-28 | Création du DAG de 61 work packages, répartis sur huit axes de suivi. Écriture du contrat de workflow intelligent et multidirectionnel, avec tests documentaires. | Planification ; aucun moteur d'exécution autonome créé. |
| `EVT-014` | 2026-10-28 | Corrections V0.1 DNS/tests/Docker, premier import CSV/JSON/TXT V0.2, synchronisation des PR empilées, demandes de revue et création de l'automatisation horaire. | Branches modifiées ; fusion et déploiement non réalisés. |
| `EVT-015` | 2026-10-28 | Lecture locale bornée de `composer.lock`, contrôle des entrées malformées, des liens symboliques et des divulgations ; nouvelle convergence PR #3. | Fonction locale testée. |
| `EVT-016` | 2026-10-28 | Analyse hors ligne de `php.ini`, `.user.ini` et PHP-FPM ; intégration au scanner et export CSV protégeant contre l'injection de formules. | 49 tests au jalon enregistré. |
| `EVT-017` | 2026-10-28 | Ajout d'un catalogue PHP/CERT-FR sourcé et daté, consultation CLI et comparaison prudente de versions. | 58 tests ; aucune vulnérabilité d'actif confirmée. |
| `EVT-018` | 2026-10-28 | Audit hors ligne du catalogue : SHA-256 canonique, âge du snapshot, validation des dates et commande `audit-catalog`. | 63 tests au checkpoint associé ; pas de flux CVE périodique. |
| `EVT-019` | 2026-10-28 | Proposition contrôlée de mise à jour des données CVE : refus des suppressions non examinées, dates régressives et changements silencieux de sources ou seuils. | 73 tests ; aucune mise à jour automatique en production. |
| `EVT-020` | 2026-10-28 | Client GHSA GitHub borné, explicitement activable, avec contrôles de transport, limites de réponse et refus des redirections non autorisées. | 81 tests ; collecte testée notamment avec mocks, non preuve de flux live opérationnel. |
| `EVT-021` | 2026-10-28 | Lecture d'une déclaration de runtime PHP/SAPI, comparaison aux références de versions et prise en compte explicite de l'absence de preuve de backport. | 89 tests ; environnement réel non attesté. |
| `EVT-022` | 2026-10-28 | Export CSV des observations de runtime déclaré, avec liste de champs autorisés et prévention des injections CSV. | 96 tests ; CSV non assimilable à une attestation. |
| `EVT-023` | 2026-10-28 | Création d'un dossier d'audit local JSON/Markdown, combinant indicateurs PHP, configuration et éventuellement déclaration runtime, avec recommandations à examiner. | Analyse hors ligne ; aucun patch exécuté. |
| `EVT-024` | 2026-10-28 | Prévisualisation d'URL HTTPS : rejet de nombreuses formes d'URL dangereuses, d'adresses privées et de déclarations insuffisantes. | 113 tests ; aucune visite réseau ni admission P1/P2. |
| `EVT-025` | 2026-10-28 | Construction du transfert PHP2SHELL → PHPPATCH, avec contrôle de cohérence des preuves, identifiants et règles, sans exposer de secrets ou sources brutes. | 122 tests ; transfert préparatoire, pas de correction appliquée. |
| `EVT-026` | 2026-10-28 | Ajouts successifs : précontrôles P1/P2, DNS et redirections hors ligne, campagnes partitionnées, rapport HTML et maquette PHP2SHELL. | 148 tests ; synchronisation de PR #3 alors encore incomplète. |
| `EVT-027` | 2026-10-28 | Deuxième console statique PHPPATCH, séparée de PHP2SHELL et conservant une posture sans action active. | 153 tests ; console non authentifiée et non déployée. |
| `EVT-028` | 2026-10-28 | Renforcement des contrôles de noms DNS, URL, IPv6 de transition et redirections limitées à un sous-chemin. | 157 tests ; vérification syntaxique, pas connexion réseau. |
| `EVT-029` | 2026-10-28 | Première API FastAPI locale : santé, capacités, prévisualisation URL, accès loopback, opérations de scan/patch désactivées et tests ASGI. | Contrat de développement uniquement. |
| `EVT-030` | 2026-10-28 | Première proposition PHPPATCH de diff local minimal pour `display_errors=Off`, liée à un constat et à un identifiant de preuve. | 164 tests applicatifs et 9 API ; aucun fichier modifié par le patch. |
| `EVT-031` | 2026-10-28 | Séquence RED→GREEN pour une véritable limite de corps ASGI de 4 Kio, indépendante de `Content-Length`, y compris trafic découpé. | 164 tests applicatifs + 12 API ; limite de prototype, non du reverse proxy de production. |
| `EVT-032` | 2026-10-28 | Séquence RED→GREEN : rejet des propositions de diff lorsque plusieurs directives `display_errors` actives rendent la modification ambiguë. | 166 tests applicatifs + 12 API ; absence d'écriture conservée. |
| `EVT-033` | 2026-10-28 | Modèle de cinq contrôles séparés : lecture publique, lecture source, proposition de patch, application de patch et déploiement. | Refus par défaut ; identité et mandat réels absents. |
| `EVT-034` | 2026-10-28 | Vérificateur cryptographique hors ligne Ed25519 : signature, émetteur, audience, projet, actif, opération, expiration et révocation fournie. | Tests cryptographiques ; aucune autorité réelle accordée. |
| `EVT-035` | 2026-10-28 | Liaison exacte d'un sous-chemin `base_path` signé pour éviter les confusions de périmètre entre tenants. | RED→GREEN ; contrat historique conservé. |
| `EVT-036` | 2026-10-28 | Plafonds de pages et de débit signés pour les futurs crawls P1, avec contrôle des budgets demandés. | RED→GREEN ; aucune opération réseau activée. |
| `EVT-037` | 2026-10-28 | Vérification de cohérence locale `composer.json` / `composer.lock` : versions, doublons, divergences et cas particuliers. | 17 nouveaux tests ; analyse toujours locale. |
| `EVT-038` | 2026-10-28 | Liaison de la preuve Ed25519 à l'URL canonique, aux identités externes et au mandat exact P2. | 188 tests applicatifs, 12 API et 28 sécurité au jalon ; accès réel toujours refusé. |
| `EVT-039` | 2026-10-28 | Simplification de l'interface : trois étapes compréhensibles, langage courant, réglages techniques repliés. | 190 tests applicatifs au jalon ; interface sans véritable analyse live. |
| `EVT-040` | 2026-10-28 | Moteur de synthèse courte anonyme et API locale, à partir d'une URL et éventuellement de métadonnées HTTP fournies. | 199 tests applicatifs, 17 API et 28 sécurité ; `NOT_ANALYZED` si aucune collecte, pas de faux audit. |
| `EVT-041` | 2026-10-28 | Normaliseur local de métadonnées HTTP : noms d'en-têtes autorisés, valeurs sensibles exclues, contrôles des tailles et caractères. | 211 tests applicatifs, 17 API et 28 sécurité ; aucune collecte distante. |
| `EVT-042` | 2026-10-28 | Correction de la CI rouge de la répétition PHPPATCH : ajout de la commande `rehearse-config-patch` manquante. | 218 tests ; échec précédent conservé dans l'historique. |
| `EVT-043` | 2026-10-28 | Paquet de revue PHPPATCH : dossier, transfert, diff et simulation de rollback liés par des empreintes et métadonnées contrôlées. | 226 tests ; paquet non exécutable. |
| `EVT-044` | 2026-10-28 | Vérification d'un paquet PHPPATCH à partir d'un dossier recalculé, avec refus des données altérées, périmées ou non canoniques. | 234 tests ; aucune promotion de droits. |
| `EVT-045` | 2026-10-28 | Commande CLI de revalidation du paquet de revue et tests de refus des paquets falsifiés. | 239 tests ; toujours sans exécution de patch. |
| `EVT-046` | 2026-10-28 | Lecture sécurisée du paquet PHPPATCH par descripteur : `O_NOFOLLOW`, `O_NONBLOCK`, `fstat`, fichier régulier et limite de 16 Kio. | 242 tests ; protège plusieurs substitutions, sans garantir un snapshot atomique total. |
| `EVT-047` | 2026-10-28 | Durcissement de la lecture Composer contre les liens symboliques et changements observables pendant la lecture. | 244 tests ; contrat source/local préservé. |
| `EVT-048` | 2026-10-29 | PHPPATCH refuse les valeurs invalides ou inefficaces de `O_NOFOLLOW` avant d'ouvrir un paquet. Convergence de la PR #3 et réconciliation MCP en lecture seule. | 245 tests applicatifs ; aucun patch ou déploiement. |
| `EVT-049` | 2026-10-29 | Formalisation de la validation technique automatisée sur preuves, sans confondre auto-revue, CI verte et approbation indépendante. | Règle documentaire, pas admission automatique. |
| `EVT-050` | 2026-10-29 | Création de `continuity/select_candidates.py` et de tests : lecture des dépendances du DAG de 61 unités, contrôle des identifiants et sélection conservatrice des candidats. | Sélecteur sans exécuteur ni attribution de claim. |
| `EVT-051` | 2026-10-29 | Séparation explicite des claims de développement MCP, des claims des work packages PHP2SHELL et des permissions de ressources partagées. | Gouvernance clarifiée, aucun droit transféré. |
| `EVT-052` | 2026-10-29 | Création du garde de périmètre des claims, tests négatifs et intégration des tests de continuité dans la CI. Exclusion des tâches bloquées par une revue. | CI de continuité réussie ; toujours aucun claim d'exécution créé. |

## 6. Décisions structurantes retrouvées (24)

| ID | Date | Décision / conséquence / restriction |
|---|---|---|
| `P2S-DEC-001` | 2026-10-22 | Créer `chainsolutions-wealthtech/Php2shell` comme dépôt public d'un outil défensif, avec laboratoire fictif et analyses limitées aux actifs autorisés. |
| `P2S-DEC-002` | 2026-10-22 | Construire la chaîne analyse → vulnérabilités prouvées → proposition de patch → tests → validation. Interdire l'assimilation d'un simple indicateur à une vulnérabilité confirmée. |
| `P2S-DEC-003` | 2026-10-27 | Maintenir V0.1 → V0.2 → V0.3 → V0.4 → V1.0 ; évolutions additives et critères de sortie documentés. |
| `P2S-DEC-004` | 2026-10-27 | Utiliser deux sous-domaines S1 distincts, PHP2SHELL et PHPPATCH, avec un moteur partagé et des permissions séparées. |
| `P2S-DEC-005` | 2026-10-27 | Viser Docker isolé et GitHub/MCP gouverné, sans nouveau gateway concurrent ni écriture directe sur `main` ou S1. |
| `P2S-DEC-006` | 2026-10-27 | Conserver cinq capacités essentielles : analyse PHP, avis CVE officiels, génération de patch, tests de patch, interface Web. Les manques doivent rester visibles. |
| `P2S-DEC-007` | 2026-10-27 | Instituer la mémoire canonique inter-conversations : issue #5, documents de référence, checkpoints par jalon et traçabilité des blocages. |
| `P2S-DEC-008` | 2026-10-27 | Ne pas utiliser Codex/Copilot, éviter les régressions et préserver les gouvernances séparées de PHP2SHELL, MCP et GRT. |
| `P2S-DEC-009` | 2026-10-27 | Restaurer le périmètre intégral de départ : centaines/milliers de domaines, CSV/JSON/TXT, analyse passive, sources privées autorisées, CVE, remédiation et supervision. |
| `P2S-DEC-010` | 2026-10-27 | Faire coexister les six lots historiques et les cinq versions ; conserver FastAPI, PostgreSQL, Redis/workers, Docker, rapports PDF/CSV/JSON et campagnes dans l'architecture cible. |
| `P2S-DEC-011` | 2026-10-27 | Distinguer les références officielles des CVE PHP et leur applicabilité réelle aux actifs ; prendre en compte le runtime et les backports fournisseurs. |
| `P2S-DEC-012` | 2026-10-27 | Ajouter le parcours d'audit déclenché par URL, l'exploration bornée et autorisée, l'analyse PHP profonde P2, le dossier de diagnostic et la remise à PHPPATCH. |
| `P2S-DEC-013` | 2026-10-28 | Organiser 61 work packages dans un workflow intelligent multidirectionnel, fondé sur dépendances, gates, coordination des agents et prévention des collisions. |
| `P2S-DEC-014` | 2026-10-28 | Autoriser la progression technique récurrente des actions admissibles par une automatisation horaire, sans lever les validations et permissions sensibles. |
| `P2S-DEC-015` | 2026-10-28 | Introduire une limite ASGI réelle de 4 096 octets, même lorsque `Content-Length` est absent ou mensonger, par tests RED→GREEN. |
| `P2S-DEC-016` | 2026-10-28 | Interdire une proposition de correction `display_errors` lorsqu'il existe plusieurs directives actives ambiguës ; conserver la compatibilité des fichiers et commandes historiques. |
| `P2S-DEC-017` | 2026-10-28 | Séparer la vérification d'identité, les droits/mandats P1/P2 et l'approbation d'une opération ; refus par défaut tant que les autorités réelles ne sont pas vérifiées. |
| `P2S-DEC-018` | 2026-10-28 | Préparer la vérification de signatures Ed25519 externes, sans créer d'émetteur d'identité parallèle ni accorder de permissions sur la seule signature. |
| `P2S-DEC-019` | 2026-10-28 | Exiger un sous-chemin exact signé lorsque l'attestation porte sur une partie du site ; éviter qu'une autorisation de domaine soit élargie à tort. |
| `P2S-DEC-020` | 2026-10-28 | Lier les futurs crawls publics à des budgets et périmètres signés, bornés et non dépassables. |
| `P2S-DEC-021` | 2026-10-28 | Raccorder l'attestation signée à l'URL canonique et à un mandat P2 exact ; maintenir `deny-only` sans IdP, ACL, révocation et claims MCP effectifs. |
| `P2S-DEC-022` | 2026-10-28 | Simplifier PHP2SHELL/PHPPATCH pour les non-techniciens : trois étapes, aperçu sans compte, jargon masqué, connexion unique à terme. |
| `P2S-DEC-023` | 2026-10-28 | Préparer la réponse courte anonyme, en séparant URL seule, métadonnées fournies non vérifiées et véritable analyse du site. Ne pas stocker de rapport complet sans compte réel. |
| `P2S-DEC-024` | 2026-10-29 | Adopter la validation technique automatisée fondée sur des preuves exact-HEAD, tests, CI et contre-revue documentée. Une auto-revue ou deux comptes d'un même propriétaire ne deviennent pas une approbation indépendante ; les protections effectives doivent être respectées ou modifiées explicitement selon les procédures applicables. |

## 7. Work packages intégraux (61)

Statuts du registre source : **G01 = `AWAITING_INDEPENDENT_REVIEW` ; tous les autres = `PLANNED_NOT_ADMITTED`**. La présence de fonctions partielles dans la branche ne change pas le statut officiel des WP.

Les quatre catégories de gates rapportées dans le document sont `READ_ONLY`, `GOVERNED_PR`, `MANDATED_TEST_ONLY` et `HUMAN_PRODUCTION_APPROVAL` ; leur attribution individuelle est à importer du fichier natif plutôt qu’à inventer.

### Gouvernance (9)

| WP | Version | Tâche source | Dépendances | Statut |
|---|---|---|---|---|
| `P2S-WF-G01` | V0.1 | Faire relire et admettre la PR #6 de continuité. | Aucune | `AWAITING_INDEPENDENT_REVIEW` |
| `P2S-WF-G02` | V0.1 | Corriger les observations de PR #1 sur DNS, tests et Docker. Correctifs codés, mais statut WP non promu. | P2S-WF-G01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-G03` | V0.1 | Revue sécurité et finalisation gouvernée de PR #1. | P2S-WF-G02 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-G04` | V0.2 | Réconcilier PR #2 avec HEAD et tests V0.1. Synchronisations techniques réalisées, finalisation non admise. | P2S-WF-G03 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-G05` | V0.2 | Revue et finalisation de PR #2. | P2S-WF-G04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-G06` | V0.4 | Réconcilier PR #3 S1 avec V0.2. Plusieurs convergences testées, sans finalisation de phase. | P2S-WF-G05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-G07` | V0.4 | Revue et finalisation PR #3 sans déployer. | P2S-WF-G06 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-G08` | Toutes | Réconcilier HEAD, PR, CI, checkpoints et NEXT_ACTION à chaque jalon. | P2S-WF-G01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-G09` | Toutes | Cartographier identités, mandats, claims, locks et BUS MCP existants. | P2S-WF-G01 | `PLANNED_NOT_ADMITTED` |

### Sécurité et autorisations (8)

| WP | Version | Tâche source | Dépendances | Statut |
|---|---|---|---|---|
| `P2S-WF-S01` | V0.2 | Modèle P1/P2 : autorisations, preuves, périmètres et expiration. Contrats offline partiels déjà construits. | P2S-WF-G09 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-S02` | V0.2 | Concevoir les protections URL/SSRF, DNS, redirections, robots et quotas. | P2S-WF-S01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-S03` | V0.2 | Implémenter et tester les contrôles SSRF, quotas, annulation et refus négatifs pour une véritable collecte. | P2S-WF-S02, P2S-WF-G05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-S04` | V0.4 | Authentification réelle, RBAC et sessions sécurisées. | P2S-WF-I02, P2S-WF-S01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-S05` | V0.4 | Secrets hors Git, preuves privées, journaux append-only et conservation. | P2S-WF-G09 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-S06` | V0.3 | Politique des tests en sandbox et approbation avant patch. | P2S-WF-S01, P2S-WF-S05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-S07` | V1.0 | Modèle de menaces Web/API/workers/Docker/Plesk. | P2S-WF-S03, P2S-WF-S04, P2S-WF-I04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-S08` | V1.0 | Revue sécurité indépendante et acceptation des risques avant production. | P2S-WF-S07, P2S-WF-Q05 | `PLANNED_NOT_ADMITTED` |

### Analyse, campagnes et CVE (12)

| WP | Version | Tâche source | Dépendances | Statut |
|---|---|---|---|---|
| `P2S-WF-E01` | V0.2 | Importer CSV/JSON/TXT, normaliser, valider les domaines et dédupliquer. Des composants locaux existent. | P2S-WF-G05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E02` | V0.2 | Campagnes à grande échelle, inventaire, reprise et stockage. Partitionnement hors ligne existant ; workers réels absents. | P2S-WF-E01, P2S-WF-I03 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E03` | V0.2 | Détection PHP passive sur des réponses publiques collectées avec autorisation. | P2S-WF-S03 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E04` | V0.2 | Crawler sitemap/liens, limites de profondeur, budgets et reprise. | P2S-WF-E03 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E05` | V0.2 | Analyse HTML, JavaScript public, headers, cookies et redirections. | P2S-WF-E04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E06` | V0.2 | Parser PHP AST et corpus de faux positifs/négatifs. Scanner lexical partiel déjà présent. | P2S-WF-G05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E07` | V0.2 | Analyser Composer, dépendances et configuration PHP/FPM. Plusieurs modules locaux et durcissements existent. | P2S-WF-E06 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E08` | V0.2 | Catalogue GHSA/PHP/CERT/fournisseurs/backports. Snapshot et clients préparatoires existants. | P2S-WF-G05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E09` | V0.2 | Attestation réelle du runtime PHP, SAPI et paquets sous mandat P2. | P2S-WF-E08, P2S-WF-S01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E10` | V0.2 | Déterminer la pertinence des CVE et le niveau de confiance par actif. | P2S-WF-E08, P2S-WF-E09 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E11` | V0.2 | Corréler observations Web, code, runtime et preuves. | P2S-WF-E05, P2S-WF-E07, P2S-WF-E10 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-E12` | V0.2 | Produire un dossier de remédiation PDF/CSV/JSON sans secrets. Rendus locaux partiels existants. | P2S-WF-E11 | `PLANNED_NOT_ADMITTED` |

### Remédiation PHPPATCH (7)

| WP | Version | Tâche source | Dépendances | Statut |
|---|---|---|---|---|
| `P2S-WF-R01` | V0.3 | Définir les stratégies de correction du runtime, extensions et backports PHP. | P2S-WF-E10 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-R02` | V0.3 | Générer des diffs candidats sur code, configuration et dépendances. Une proposition ini limitée existe. | P2S-WF-E07, P2S-WF-S06 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-R03` | V0.3 | Exécuter un laboratoire Docker isolé, non-root, sans secrets. | P2S-WF-S06, P2S-WF-I04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-R04` | V0.3 | Exécuter les tests lint, compatibilité et intégration avant/après patch. | P2S-WF-R02, P2S-WF-R03 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-R05` | V0.3 | Sauvegarde et simulation de rollback attestée. Une répétition en mémoire existe mais ne suffit pas. | P2S-WF-R03 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-R06` | V0.3 | Transfert PHPPATCH, approbation et PR candidate. Les paquets de revue locaux existent ; approbation réelle absente. | P2S-WF-R04, P2S-WF-S04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-R07` | V0.3 | Fixture `portail-demo.example` PHP 8.3.34 validée. | P2S-WF-R01, P2S-WF-R03 | `PLANNED_NOT_ADMITTED` |

### Infrastructure, backend et MCP (8)

| WP | Version | Tâche source | Dépendances | Statut |
|---|---|---|---|---|
| `P2S-WF-I01` | V0.4 | Diagnostiquer DNS local et configuration Plesk S1 en lecture seule. | P2S-WF-G01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-I02` | V0.4 | Construire l'API FastAPI commune sécurisée. Premier contrat local présent, backend de production absent. | P2S-WF-G05, P2S-WF-S01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-I03` | V0.4 | PostgreSQL, modèle de données, migrations, sécurité et sauvegardes. | P2S-WF-I02, P2S-WF-S05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-I04` | V0.4 | Images et réseau Docker isolés compatibles Plesk. | P2S-WF-I02, P2S-WF-S05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-I05` | V0.4 | Cartographier l'adaptateur de déploiement MCP existant. | P2S-WF-G07, P2S-WF-G09 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-I06` | V0.4 | Adaptateur MCP ciblé avec exact SHA et rollback. | P2S-WF-I05, P2S-WF-I04, P2S-WF-R05 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-I07` | V0.4 | Staging S1 authentifié, préflight et contrôle du rollback. | P2S-WF-I06, P2S-WF-S04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-I08` | V0.4 | Workers idempotents, files bornées et anti-doublons. | P2S-WF-I03, P2S-WF-G09 | `PLANNED_NOT_ADMITTED` |

### Interfaces PHP2SHELL et PHPPATCH (6)

| WP | Version | Tâche source | Dépendances | Statut |
|---|---|---|---|---|
| `P2S-WF-U01` | V1.0 | Formulaire URL, projets, mandats et statut d'audit. Maquette statique partielle présente. | P2S-WF-I02, P2S-WF-S04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-U02` | V1.0 | Cartographie des pages réellement visitées et couverture des audits. | P2S-WF-U01, P2S-WF-E04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-U03` | V1.0 | Panneau PHP2Shell/CVE, preuves, incertitudes et diagnostics contextualisés. | P2S-WF-U01, P2S-WF-E10 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-U04` | V1.0 | Rapports téléchargeables et historique privé des preuves. | P2S-WF-U02, P2S-WF-E12 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-U05` | V1.0 | Console PHPPATCH : diff, tests, approbations et rollback. Maquette présente, actions réelles absentes. | P2S-WF-R06, P2S-WF-S04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-U06` | V1.0 | Supervision multi-projets et tâches. | P2S-WF-U01, P2S-WF-I03 | `PLANNED_NOT_ADMITTED` |

### Qualité et recette (5)

| WP | Version | Tâche source | Dépendances | Statut |
|---|---|---|---|---|
| `P2S-WF-Q01` | Toutes | Vérifier la non-régression de toutes les 32 exigences par CI. Des suites existent, pas la recette finale complète. | P2S-WF-G01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-Q02` | V0.2 | Simuler des campagnes de 1, 100 puis 1 000 domaines fictifs. Simulation de partitionnement déjà réalisée. | P2S-WF-E02, P2S-WF-S03 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-Q03` | V0.3 | Corpus PHP de versions corrigées et de backports, avec cas de compatibilité. | P2S-WF-E10, P2S-WF-R04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-Q04` | V1.0 | Tests E2E URL → rapport → PHPPATCH → PR fictive. | P2S-WF-U04, P2S-WF-U05, P2S-WF-I07 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-Q05` | V1.0 | Recette staging négative, authentification, performance et rollback. | P2S-WF-Q04, P2S-WF-S07 | `PLANNED_NOT_ADMITTED` |

### Exploitation et supervision (6)

| WP | Version | Tâche source | Dépendances | Statut |
|---|---|---|---|---|
| `P2S-WF-O01` | Toutes | Observer PR, CI et checkpoints via les événements du BUS MCP existant. | P2S-WF-G09 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-O02` | Toutes | Définir une supervision périodique sans duplication ni spam. | P2S-WF-O01 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-O03` | V1.0 | Observabilité, métriques, journaux, sauvegardes et alertes. | P2S-WF-I08, P2S-WF-I07 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-O04` | V1.0 | Préparer go/no-go et release de production autorisée. | P2S-WF-S08, P2S-WF-G07, P2S-WF-O03 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-O05` | V1.0 | Déployer les deux applications sur S1 via une chaîne gouvernée. | P2S-WF-O04 | `PLANNED_NOT_ADMITTED` |
| `P2S-WF-O06` | V1.0 | Maintenance récurrente : avis CVE, certificats et sauvegardes. | P2S-WF-O05 | `PLANNED_NOT_ADMITTED` |

## 8. Checkpoints numérotés retrouvés (40)

| Checkpoint | Objet inscrit dans l’issue #5 |
|---|---|
| `#001` | Création de l'ancrage canonique, PR #6, documents et premiers tests de continuité. |
| `#002` | Vérification de l'amont V0.1 avant poursuite. |
| `#003` | Réconciliation du cahier des charges initial et des six lots. |
| `#004` | Formalisation du parcours URL → Web autorisé → PHP profond → PHPPATCH. |
| `#005` | Création du backlog multidirectionnel de 61 unités. |
| `#006` | Correction documentaire append-only et revue PR #6 toujours attendue. |
| `#007` | Corrections PR #1, imports V0.2, synchronisation S1 et automatisation horaire. |
| `#008` | Contrôle S1 des deux vhosts et diagnostic DNS local. |
| `#009` | Inspection Composer.lock et nouvelle synchronisation PR #3. |
| `#010` | Audit ini/FPM, export CSV, synchronisation et renforcement de l'automatisation. |
| `#011` | Catalogue officiel PHP/CERT-FR et CLI de consultation. |
| `#012` | Audit hors ligne du catalogue et provenance. |
| `#013` | Propositions contrôlées de mise à jour CVE. |
| `#014` | Client GHSA officiel borné et tests de transport. |
| `#015` | Enveloppe de déclaration PHP/SAPI, mandat non attesté. |
| `#016` | Export CSV runtime déclaré et convergence des branches. |
| `#017` | Dossier d'audit JSON/Markdown et prévisualisation URL sécurisée. |
| `#018` | Transfert préparatoire PHP2SHELL → PHPPATCH, 122 tests. |
| `#019` | Précontrôles P1/P2, campagnes, rapport HTML et aperçu URL, 148 tests. |
| `#020` | Deuxième console PHPPATCH statique, 153 tests. |
| `#021` | Contrôles DNS/redirections hors ligne, 157 tests. |
| `#022` | Contrat FastAPI local et proposition PHPPATCH, 164 tests applicatifs + 9 API. |
| `#023` | Limite ASGI réelle de 4 Kio, 164 + 12 tests. |
| `#024` | Refus des directives ini actives dupliquées, 166 + 12 tests. |
| `#025` | Matrice P1/P2 fail-closed et vérifications MCP en lecture seule. |
| `#026` | Attestation Ed25519 externe hors ligne, 171 + 12 + 10 tests. |
| `#027` | Sous-chemin et budgets signés, collision concurrente détectée. |
| `#028` | Cohérence Composer, 188 + 12 + 20 tests. |
| `#029` | Liaison P1/P2 signée au parcours URL, 188 + 12 + 28 tests. |
| `#030` | UX grand public à trois étapes, aucun scan réel. |
| `#031` | Synthèse courte anonyme et API locale, 199 + 17 + 28 tests. |
| `#032` | Normalisation des métadonnées HTTP, 211 + 17 + 28 tests. |
| `#033` | Répétition PHPPATCH V0.3, avec une CI rouge constatée. |
| `#034` | Correction de la répétition, paquet de revue PHPPATCH, 226 tests. |
| `#035` | Vérification du paquet de revue, 234 tests. |
| `#036` | Commande CLI de revalidation, 239 tests. |
| `#037` | Ouverture sécurisée du paquet par descripteur, 242 tests. |
| `#038` | Durcissement Composer, 244 tests. |
| `#039` | Refus des drapeaux `O_NOFOLLOW` inefficaces, 245 tests. |
| `#040` | Séparation technique des claims et tests de continuité dans la CI. |

Les addenda des 48 commentaires initialement recensés ne sont pas tous individualisés dans le document transmis. Ils ne doivent pas être effacés ni devenir de faux checkpoints.

## 9. Preuves, SHA, branches et CI mentionnés

### Commits ponctuellement cités par la source

| SHA | Déclaration dans le document source |
|---|---|
| [`0adc473c8b03`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/0adc473c8b03e37ad7ad3c99ce8b84cc382dbeca) | initialisation dépôt main 2026-10-22 16:40:40 UTC |
| [`a8600e6f4d70`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/a8600e6f4d702563a0a0ec6f4d935b0d0ddf0409) | périmètre défensif 2026-10-22 16:41:47 UTC |
| [`a9d799b008fc`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/a9d799b008fc65ed5745745bc4ef09e8b889aabe) | CLI V0.1, laboratoire Docker et CI 2026-10-22 16:42:16 UTC |
| [`973f4dbb0fff`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/973f4dbb0fffbcf256b5813030f625204fc9fa53) | durcissement paquet PHPPATCH |
| [`b355299f1b33`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/b355299f1b338b22c13546a802144d0050e01026) | HEAD archive PR #7 lors du contrôle historique |
| [`33b5c7389339`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/33b5c7389339855795ac2fd81c0525927cc74402) | EVT-052, garde de périmètre claims et CI continuité |

- HEAD archive PR #7 selon la source : `b355299f1b338b22c13546a802144d0050e01026` (historique, non nécessairement HEAD actuel).
- CI associée à EVT-052 selon la source : [run #40941805840](https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40941805840).
- Les historiques de `main`, PR #1, PR #2, PR #3, audit DNS/S1, PR #6 et PR #7 sont décrits dans le document original (section 7).
- La source précise que la vérification individuelle de chaque diff des au moins 348 commits et de chacun des 988 runs **n’a pas été achevée**.

## 10. Registre des vérifications non closes

| Contrôle demandé | État constaté dans la source |
|---|---|
| Identifier l'origine et l'ordre chronologique des commits présents sur les branches | Inventaire Git effectué sur les branches initiales ; nouvelle PR #7 identifiée séparément |
| Ouvrir individuellement chaque commit et contrôler parents, fichiers, ajouts et suppressions | Partiel |
| Vérifier toutes les CI et leurs journaux au SHA exact, y compris les échecs RED | Partiel |
| Recenser les 52 événements canoniques et leur ordre | Effectué dans le registre |
| Recenser les 24 décisions canoniques et leur ordre | Effectué dans le registre |
| Recenser les 61 work packages, leurs versions, dépendances et statuts | Effectué dans le registre |
| Recenser les 40 checkpoints numérotés et les addenda de l'issue #5 | Effectué au niveau des entrées retrouvées |
| Vérifier chaque checkpoint contre les commits, CI et opérations réellement exécutées | Partiel |
| Vérifier indépendamment les opérations DNS, Plesk, Docker et S1 historiques | Non exhaustif ; certaines preuves proviennent de checkpoints rétrospectifs |
| Réconcilier les décisions prises dans les conversations avant leur publication sur GitHub | Non exhaustif |
| Vérifier les claims, mandats, approbations et droits exacts à chaque date historique | Non exhaustif |
| Constituer les fiches d'action individuelles avec avant/après, incidents, corrections et rollback | À compléter |
| Attester la correspondance de chaque WP avec des preuves d'exécution et critères d'acceptation complets | Non réalisé intégralement |

## 11. Périmètre produit et distinction entre construit et projeté

- Versions : V0.1 → V0.2 → V0.3 → V0.4 → V1.0, évolutions additives.
- Séparation fonctionnelle PHP2SHELL (analyse) / PHPPATCH (revue/remédiation), deux sous-domaines préparés sur S1 ; ni déploiement applicatif ni patch effectif attestés dans la source.
- Parcours cible URL → exploration autorisée et bornée → diagnostic PHP/CVE → dossier de preuve → proposition PHPPATCH → tests → approbation → exécution éventuelle sous mandat.
- P1/P2 et accès anonymes : spécification additionnelle [P2S-UX-002](https://github.com/chainsolutions-wealthtech/Php2shell/issues/5#issuecomment-6462119529) pour réponse courte sans compte, rapport privé après inscription, analyse approfondie après vérification du propriétaire et mandat.
- Les attestations Ed25519 hors ligne, les budgets signés, le `base_path` et les règles `deny-only` ne créent pas de droits réels.
- Docker, FastAPI, PostgreSQL, Redis/workers et déploiement MCP restent à qualifier selon chaque work package ; des prototypes locaux ne sont pas un service opérationnel.

## 12. Règles de reprise non régressive

1. Consulter d’abord les registres GitHub canoniques ; ne pas utiliser ce fichier pour déduire un HEAD actuel.
2. Vérifier l’identité, le mandat, les gates, les conflits de claims et les dépendances avant tout changement de statut.
3. Créer des fiches individuelles pour les commits/runs à examiner avec SHA, parents, diff, fichiers, tests, résultat, horodatage et sources primaires.
4. Conserver l’échec puis son correctif, notamment les CI rouges historiques et tests RED→GREEN ; ne jamais réécrire l’historique.
5. Garder les statuts des work packages tant que les exigences d’admission et preuves d’acceptation ne sont pas réunies.
6. Préserver les périmètres MCP, GRT et PHP2SHELL ; ne jamais fusionner leurs pouvoirs ou claims.
7. Ne pas activer scan distant, patch, déploiement ou mutation de ressources sans admission et autorisation correspondantes.
8. Écrire les suites en append-only, avec checkpoint lisible et `NEXT_ACTION` conditionnée par les preuves.

## 13. Emplacement des données structurées

| Fichier | Emploi |
|---|---|
| `MANIFEST.json` | Identité, sources, date, réserves, volumes et liens stables |
| `registres/EVENEMENTS.json` et `.csv` | 52 événements, dates et restrictions |
| `registres/DECISIONS.json` et `.csv` | 24 décisions datées |
| `registres/WORK_PACKAGES.json` et `.csv` | 61 tâches, axes, dépendances, statuts et champs de preuves vides |
| `registres/CHECKPOINTS.json` et `.csv` | 40 points de reprise, sans SHA imaginé |
| `registres/VERIFICATIONS_EN_ATTENTE.json` et `.csv` | Contrôles dont l’exhaustivité n’est pas établie |
| `tracabilite/INDEX_PREUVES_REFERENCES.json` | SHA et CI explicitement mentionnés |
| `sources/SOURCE_20261029_reconstitution_integrale.txt` | Document original intégral, non modifié |
| `guides/PROTOCOLE_DE_REPRISE.md` | Procédure et champs d’une nouvelle preuve |

## 14. Registre d’intégrité

- Document original SHA-256 : `9154b71a3e0bc408d742bce6f29990811f6cc96b64d456beffd1a8b870374de4`.
- Nombre d’entrées extraites automatiquement : **52 événements + 24 décisions + 61 WP + 40 checkpoints + 13 vérifications à réconcilier**.
- Dépendances : tous les identifiants de dépendance pointent vers un WP de ce paquet.
- Les dates de checkpoints, les HEAD exacts à chaque jalon et l’affectation individuelle des gates sont **non présents dans le document transmis** : ces champs restent vacants.

Cette édition ne modifie ni les branches GitHub, ni les PR #6/#7, ni S1. Elle n’atteste aucune finalisation du projet.
