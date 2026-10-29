# V0.2 — Admission P1/P2 et précontrôles réseau

**Implémentation actuelle : validation hors ligne uniquement.**

## Autorisations

Le module `app/admission_preflight.py` compare une déclaration locale de mandat au résultat de `preview-url`, en vérifiant cohérence du domaine, portée, dates et quotas. Il ne délivre aucune autorisation : `authorized_to_crawl=false`, `authorized_to_inspect_source=false`, `mcp_claim_verified=false`. Les déclarations de l'opérateur ne sont pas des attestations de propriété ou d'identité.

L'intégration future devra utiliser les mandats, identités et claims du MCP existant, sans créer de gouvernance concurrente.

## Précontrôle réseau

Le module `app/network_preflight.py` classe des réponses DNS **fournies en entrée**, distingue les adresses globalement routables des adresses non publiques et prévisualise les chaînes de redirection HTTPS sur une même origine.

Il n'effectue aucune requête DNS/HTTP. Il ne vérifie ni les réponses du résolveur, ni la connexion physique. Les résultats ne donnent jamais l'autorisation de contacter un site.

## Exigences de suite

Le moteur réseau devra valider effectivement le domaine autorisé, les destinations, les limites de navigation et la session, sans se fier aux seuls résultats de ces fonctions. Les accès P2 aux sources nécessitent une admission indépendante. Un audit ne peut pas confirmer une CVE depuis un numéro de version ou un indice lexical.

Tests : `tests/test_admission_preflight.py` et `tests/test_network_preflight.py`.

**Statut : P2S-WF-S01/S02 préparatoires ; S03, les API, les deux frontends, PHPPATCH et S1 restent des chantiers non terminés.**
