# V0.2 — Entrée d'URL du futur frontend PHP2SHELL (prévisualisation sûre)

**État : normalisation et préparation du mandat uniquement. Aucun crawler, DNS ni analyse PHP distante n'est exécuté.**

Cette première brique rend possible l'entrée d'un site par URL dans le parcours cible PHP2SHELL :

**URL saisie → préparation du périmètre → preuve d'autorisation → validation DNS/IP/réseau → crawl public borné → constat technique → analyse P2 si autorisée → rapport → propositions PHPPATCH.**

Seule **la première étape de parsing/contrat** est implémentée dans ce jalon. Aucun composant d'interface Web n'est encore déployé.

## Utilisation hors ligne

```bash
python -m app.cli preview-url --url https://example.com/ --scope public_metadata

python -m app.cli preview-url \
  --url https://portail-demo.example/ \
  --scope owned_source --mandate-ref LAB-P2-001 \
  --max-pages 20 --requests-per-minute 6
```

- `--scope public_metadata` est une déclaration P1 non vérifiée ; `owned_source` exige une référence de mandat P2 déclarative, **qui n'est ni enregistrée en clair dans le résultat, ni authentifiée**.
- L'URL doit être `https://`, sans identifiants, query string, fragment ni port différent de 443. Les IP explicites, variantes numériques ambiguës, hôtes locaux/réservés, chemins codés/traversals et paramètres hors bornes sont refusés dès l'entrée.
- Les limites proposées, sans exécution : **1 à 100 pages** et **1 à 30 requêtes par minute**. Ces limites seront des plafonds supplémentaires au moment de la création d'un moteur réseau réellement autorisé.
- Sortie `OFFLINE_URL_SCOPE_PREVIEW_NOT_ADMISSION`, avec URL normalisée, portée déclarée, référence de mandat présente ou non (booléen), budget déclaré et étapes de contrôle nécessaires.
- **Invariants obligatoires :** `allowed_to_crawl=false`, `allowed_to_inspect_source=false`, `mandate_authentication_verified=false`, `target_ownership_verified=false`, `dns_and_public_ip_validated=false`, `network_requests_made=false`.

## Prochaines portes avant toute requête

1. Authentifier utilisateur, identités d'agents, mandat P1/P2, consentement, expiration et quotas via la gouvernance existante.
2. Effectuer au moment **de chaque connexion** une résolution DNS contrôlée, validation CNAME/A/AAAA, et vérification des IP effectives publiques (éviter SSRF, réseau privé, IP metadata et DNS rebinding). La validation de la seule chaîne URL **ne protège pas contre la résolution DNS vers un réseau privé**.
3. Épingler l'adresse de connexion effectivement validée et le nom TLS/origine ; refuser les changements d'IP non revalidés. Valider **chaque redirection** et chaque page du crawl contre le périmètre autorisé.
4. Respecter robots/permissions applicables, limiter débit/concurrence, profondeur, volume, annulation et conservation des preuves.
5. S'interdire de présumer un accès au code PHP serveur à partir de la réponse HTML. L'analyse de code et les tests actifs exigent un mandat P2 effectivement validé.

**Ce n'est pas un crawler SSRF-safe opérationnel, ni une licence pour scanner des tiers.** Aucun changement au serveur S1, aux vhosts, à Docker, au moteur de patch ou aux autorisations de production.

## Tests

`tests/test_url_intake.py` : URL HTTPS normale, sous-chemin, URL de laboratoire non exécutable, refus credentials/fragment/ports/IP/hosts internes/chemins suspects, limites et scopes, absence réseau et contrat CLI JSON.

Cette tranche complète **REQ-002, REQ-003, REQ-022 et REQ-031 à l'état PREVIEW/PARTIEL**, sans les considérer implémentées en production. Elle ne remplace pas les 61 work packages et les autres exigences fondatrices.

## Renforcement local du précontrôle DNS et des redirections (V0.2)

Le module `app/network_preflight.py` refuse désormais les hôtes DNS fournis
qui ressemblent à une URL, une IP littérale, un nom local/réservé ou une
variante numérique ambiguë. Il applique les mêmes restrictions de saisie
que `preview-url`, **sans résoudre aucun DNS**. Les adresses IPv6
encapsulant de l'IPv4 (mapped, 6to4, Teredo) sont classées conservativement
comme bloquées dans les réponses A/AAAA **fournies localement**.

La fonction `check_same_origin_redirects` accepte en complément le paramètre
optionnel `allowed_base_path="/app"` : le départ et chaque destination
doivent appartenir à `/app` ou à un sous-chemin séparé par `/`.
`/application` ne satisfait pas `/app`. Sans ce paramètre, la politique
historique *same-origin* est conservée pour les appelants existants.

Les résultats restent `network_requests_made=false`,
`authorized_to_crawl=false`, `peer_connection_authorized=false`.
**Ce précontrôle hors ligne n'est ni une validation de mandat P1/P2, ni
un garde-fou SSRF utilisable seul en production** : un futur worker autorisé
devra revalider CNAME/A/AAAA, IP du pair, TLS, chaque redirection et
l'intégralité du périmètre au moment de la connexion, sous claim MCP valide.
Aucun scan ni déploiement S1 n'est exécuté par ce changement.


## Contrat additionnel de gates P1/P2 — 28 octobre 2026

`app/admission_preflight.py::evaluate_action_gates` est une extension **purement locale et non exécutante** du précontrôle de déclarations. Elle propose une matrice de conditions nécessaires à cinq familles d'actions distinctes : `public_crawl`, `source_read`, `patch_propose`, `patch_apply` et `deploy`.

- **P1** : l'accès aux métadonnées publiques n'est pas une autorisation de crawl. Il exige une identité authentifiée, une admission du périmètre P1, les contrôles réseau anti-SSRF et un claim/budget gouverné.
- **P2** : la lecture des sources privées exige une délégation P2 et une ACL sur le projet/ressource, à laquelle s'ajoutent validité temporelle, révision des droits et claim gouverné. Une simple référence de mandat, même non expirée, ne prouve aucune délégation.
- **PHPPATCH** : proposer un patch, l'appliquer en sandbox et déployer sont trois capacités distinctes. L'application exige validation/régression/rollback/approbation ; le déploiement exige encore son mandat gouverné indépendant.
- L'extension **refuse explicitement** les booléens d'autorité forgés et les actions inconnues ; elle ne renvoie jamais de jeton, de secret, de preuve de propriété, de permis ou de résultat `ALLOW`. `decision=DENY_UNVERIFIED_AUTHORITY`, `authorized=false`, `execution_enabled=false` sont invariants.
- Cette matrice est un **contrat d'intégration en attente de capacités MCP de vérification de l'identité et de l'autorité réellement déléguées**. Elle ne se substitue pas aux vrais droits GitHub/Plesk, au système de mandats, de révocation, de claims, ni aux protections du worker. Aucun endpoint public ou privilège n'est ouvert par cette tranche.

Les tests `AuthorizationGateContractTests` couvrent les cinq opérations, l'absence d'escalade P1→P2, le refus des indicateurs de confiance falsifiés, les expirations et les différences de hostname. Les tests historiques restent conservés. Aucune opération réseau ou serveur n'est exécutée.
