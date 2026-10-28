# V0.2 — Acquisition publique bornée d'avis PHP via GitHub

**État : client GitHub API développé sur la PR #2, validation CI avec réponses simulées. Aucune requête réelle à l'API officielle n'est attestée par les tests. Aucune cible externe n'est auditée. Aucune mise à jour de catalogue n'est appliquée.**

## Contrat de sécurité et source de vérité

L'interface `app/advisory_fetch.py` interroge, **uniquement sur invocation explicite**, le point REST documenté par GitHub :

```text
GET https://api.github.com/advisories/{GHSA_EXACT}
```

Source de contrat : [GitHub REST — Get a global security advisory](https://docs.github.com/en/rest/security-advisories/global-advisories).

- Seuls les **identifiants GHSA déjà admis** dans l'instantané local `app/data/php_security_advisories.json` sont acceptés. Aucune URL libre, aucun hôte, chemin, paramètre de requête ou en-tête de connexion fourni par l'opérateur.
- Requête `GET` HTTPS vers `api.github.com` uniquement, délai maximum 8 secondes, **proxy de l'environnement désactivé**, redirections refusées, certificat TLS vérifié par les racines du système.
- Réponse `HTTP 200` au format JSON, au plus 128 000 octets ; longueur déclarée vérifiée avant lecture ; lecture bornée ; identifiants `ghsa_id`/`cve_id`, `html_url` public et `url` API comparés au GHSA/CVE préexistant ; dates UTC, sévérité et type vérifiés.
- **Métadonnées minimales seulement** : GHSA, CVE, URL officielle, dates, type, sévérité, état retiré, empreinte SHA-256 des octets bruts ; **pas de description brute, de contenu non filtré ni de credential** dans les résultats.
- Toute divergence de sévérité, état de revue ou retrait est signalée sous `metadata_drift_fields` et exige une revue indépendante. L'acquisition ne vérifie pas la configuration PHP, les versions rétroportées ni une vulnérabilité d'un actif.
- **Pas d'écriture** : catalogue canonique inchangé, aucun patch, aucun déploiement. L'empreinte représente les données reçues, **pas une signature éditeur**.

## Commande CLI explicitement opt-in

```bash
python -m app.cli fetch-official-advisory \
  --ghsa GHSA-w8hw-w9fx-j79w \
  --as-of 2026-10-28 \
  --permit-official-network
```

La présence du flag `--permit-official-network` autorise **seulement cette lecture REST GitHub** ; les mandats P1/P2 de toute collecte concernant un actif Web, les futures sources externes et les autres permissions ne sont pas affectés. La date fournie est un **repère calendaire** explicite, pas un horodatage serveur indépendant ni un cache effectivement actualisé. Un avis `unreviewed` ou `withdrawn` bloque toute promotion automatique.

Le client ne contacte pas CERT-FR ni un site tiers. La validation des avis PHP/CERT-FR déjà conservés est indépendante du format JSON de GitHub et reste nécessaire avant toute décision de remédiation.

## Tests et preuves

`tests/test_advisory_fetch.py` couvre les réponses GitHub **simulées** : identité GHSA/CVE, métadonnées non copiées, absence de requête sur un identifiant hors catalogue, URL usurpée, sévérité divergente, avis retiré/non revu, redirections, erreurs HTTP, type MIME invalide, réponse trop volumineuse, dates futures/incorrectes et exigence du flag CLI.

Exécuter `python -m unittest discover -s tests -v` ; vérifier le **HEAD exact** et la CI GitHub avant d'affirmer la réussite. Aucun test ne déclenche un appel réseau réel.

## Étapes suivantes du programme

1. Mettre en place un **flux de vérification d'avis** fondé sur cette acquisition, en conservant une trace d'observation/publisher, la politique de fraîcheur et les revues avant admission d'un nouveau GHSA/CVE.
2. Ajouter la réconciliation CERT-FR/PHP et les fournisseurs de distributions, puis une proposition de modification **sans suppression silencieuse**, en réutilisant `catalog_update.py`.
3. Développer une **attestation P2** du runtime/SAPI et des correctifs rétroportés sur des systèmes effectivement administrés avant toute conclusion d'applicabilité CVE.
4. Intégrer le diagnostic sourcé, les rapports et PHPPATCH à l'API/frontends protégés et aux tests Docker isolés.

**Ce document est un complément additif à `docs/V0_2_CATALOG_AUDIT.md` et `docs/V0_2_CATALOG_UPDATE_PROPOSAL.md`.** Il ne transforme pas un prototype CLI en plateforme déployée.
