# PHP2SHELL

**Prototype défensif de gestion des risques PHP — version 0.1.**

PHP2SHELL est un projet visant à inventorier des actifs PHP autorisés, rapprocher des versions déclarées d'avis de sécurité, produire des constats vérifiables et, dans des versions futures, proposer des correctifs soumis à revue humaine.

> **État actuel : prototype local, sans réseau.** La V0.1 ne découvre pas les technologies des sites web, ne télécharge pas leur code, n'exploite aucune faille, ne modifie aucun système et ne déploie aucun patch. Un indicateur de version ne prouve jamais qu'un système est vulnérable.

## Démarrage rapide

**Prérequis :** Python 3.10+ (3.13 utilisé par la CI). Aucune dépendance Python externe.

```bash
git clone https://github.com/chainsolutions-wealthtech/Php2shell.git
cd Php2shell
python -m unittest discover -s tests -v
python -m app.cli inventory --file lab/targets.json
python -m app.cli check-version --php 8.3.34
```

Sur Windows, utiliser `py -m ...` si `python` n'est pas disponible.

## Commandes

| Commande | Résultat |
| --- | --- |
| `python -m app.cli inventory --file lab/targets.json` | Affiche l'inventaire JSON des cibles **déclarées**, sans requête réseau |
| `python -m app.cli check-version --php 8.3.34` | Compare une version PHP fournie à des seuils d'exemple, sans attester l'exploitabilité |
| `python -m unittest discover -s tests -v` | Lance les tests de non-régression |
| `docker build -t php2shell .` | Construit l'image CLI (Docker requis) |
| `docker run --rm php2shell` | Affiche l'inventaire fictif intégré |
| `docker compose --profile lab build` | Construit la fixture PHP facultative, sans la démarrer |

**Exemple d'inventaire** (`lab/targets.json`) :

```json
[
  {"hostname": "portail-demo.example", "scope": "owned_source", "evidence": "fictional-local-lab"},
  {"hostname": "public-demo.example", "scope": "public_metadata"}
]
```

- `public_metadata` : uniquement les informations déjà déclarées. Aucun accès au code source.
- `owned_source` : une preuve d'autorisation non vide est obligatoire. Ce champ est **déclaratif**, non une vérification d'identité; la V0.1 ne lit toujours pas le code source.
- `hostname` : nom DNS, sans schéma, port ni chemin.

La sortie est du JSON sur la sortie standard. Le programme ne crée aucun fichier de rapport et n'effectue aucun appel réseau.

## Comprendre le diagnostic de version

`below_reference_fix` signifie uniquement que la version indiquée est inférieure au seuil configuré dans le prototype. `at_or_above_reference_fix` signifie l'inverse. `review_vendor_support` indique qu'aucun seuil n'est configuré pour la branche.

**Les références CVE-2026-109618 et CVE-2026-109619 ainsi que les versions correctives codées dans `app/core.py` sont des données d'exemple non validées contre les avis officiels.** Ne pas les utiliser pour déclarer une vulnérabilité réelle ni prescrire un correctif. Les distributions peuvent appliquer des rétroportages.

## Organisation du dépôt

```text
app/                    CLI et moteur hors ligne
tests/                  Tests unitaires
lab/                    Cibles fictives et fixture PHP non exposée
docs/ARCHITECTURE.md    Architecture, flux et composants
docs/USAGE.md           Guide d'utilisation et interprétation
docs/SECURITY.md        Modèle de menace, limites et autorisations
docs/GOVERNANCE.md      Contrôles de changement
docs/ROADMAP.md         Plan de développement
.github/workflows/ci.yml  Tests automatiques
Dockerfile              Image CLI
docker-compose.yml      Fixture facultative isolée
```

## Sécurité, gouvernance et contributions

Toute analyse de code ou correction future exige une autorisation vérifiable du propriétaire, une portée explicite, des tests, une validation humaine et un plan de retour arrière. Ne jamais soumettre de secrets ni de données sensibles. Consulter [Sécurité](docs/SECURITY.md), [Gouvernance](docs/GOVERNANCE.md) et [Architecture](docs/ARCHITECTURE.md).

## Feuille de route

1. Vérifier les avis officiels et leur provenance, supprimer les seuils non sourcés.
2. Introduire un inventaire versionné et des rapports JSON avec horodatage et traçabilité.
3. Ajouter une analyse **locale** de dépôts explicitement autorisés.
4. Proposer des correctifs sous forme de diff, sans application automatique.
5. Ajouter une validation CI, une approbation humaine et un mécanisme de rollback.
6. Étudier une API, une interface web et des agents déployables avec permissions minimales.

Voir [la feuille de route complète](docs/ROADMAP.md).

**Statut :** V0.1 expérimentale. Aucune garantie de détection exhaustive ou de remédiation.
