# V0.3 — Première proposition de diff PHPPATCH (hors ligne)

**Statut : sous-tranche préparatoire de V0.3, développée sur la PR #2 existante. Elle ne constitue pas la livraison de V0.3.**

Le moteur PHP2SHELL produit déjà un dossier d'audit JSON/Markdown/HTML et un handoff vers PHPPATCH sans permissions. La nouvelle capacité `app/patch_preview.py` ajoute une proposition de modification **strictement limitée** au réglage `display_errors` d'un fichier `php.ini` ou `.user.ini` sous le répertoire local explicitement choisi.

## Parcours démontré

1. Préparer le dossier PHP2SHELL avec `audit-dossier --path ... --as-of ...`.
2. Repérer un identifiant `P2S-EV-...` dont la règle est `PHP-CONFIG-DISPLAY-ERRORS`.
3. Produire le diff candidat, sans modifier le projet :

```bash
python -m app.cli propose-config-patch \
  --path ./projet-local-autorise \
  --as-of 2026-10-28 \
  --evidence-id P2S-EV-xxxxxxxxxxxxxxxx
```

4. Relire le diff, vérifier la configuration PHP réellement active et les effets fonctionnels, puis exiger mandat P2 authentifié, sandbox, tests et revue avant toute application.

La sortie JSON fournit le diff de contexte nul (une seule ligne remplacée), son empreinte, l'identifiant de constat et le fingerprint du dossier. **Aucun contexte adjacent n'est exporté**, car des paramètres ou secrets peuvent se trouver dans le même fichier. Les chemins restent relatifs au projet.

## Restrictions

- Recalcule le dossier local et les identifiants avant toute proposition ; les identifiants forgés ou devenus obsolètes sont refusés.
- Refuse les chemins symboliques, le parcours hors du projet, les fichiers non attendus, les réglages ambigus, les données non UTF-8 et les fichiers volumineux.
- Accepte uniquement une affectation simple de `display_errors` sans commentaires ou interpolation pour produire la suggestion `display_errors=Off`.
- `files_modified=0`, `patch_applied=false`, `mandate_verified=false`, `tests_run_on_candidate=false`, `independent_approval_received=false`, `ready_for_production=false`.
- Le réglage peut être surchargé par une autre configuration effective et sa modification peut perturber les environnements de développement ; il faut vérifier la SAPI active et la compatibilité.
- **Cette proposition n'est pas un correctif des CVE PHP prioritaires**, n'authentifie aucun mandat et ne démontre pas une vulnérabilité du site.
- Le diff est **un brouillon de revue**, pas un ordre d'écriture Git, un patch appliqué, une PR ni un déploiement.

## Preuves et suite

`tests/test_patch_preview.py` couvre diff minimal, non-écriture, absence réseau, absence de secrets, refus des autres règles, fichiers ambigus/symboliques, CRLF et commande CLI.

**Reste à construire** : moteur générique de propositions de correctifs PHP/runtime/config, diagnostics confirmés, sandbox Docker isolée et non-root, tests d'intégration, score de risque et preuve de rollback, émission de PR sous mandat et approbation, restauration effective et l'interface PHPPATCH authentifiée.


## Durcissement additif — affectations actives contradictoires (28/10/2026)

**Affectations multiples de `display_errors` : refus conservateur.** Si un même `php.ini` ou `.user.ini` présente plusieurs affectations actives de `display_errors`, même lorsque les valeurs semblent équivalentes, la fonction `propose_local_ini_patch` ne propose pas de diff uniligne : un tel diff ne justifie pas une configuration effective sans analyse des surcharges et de la SAPI. L'erreur reste générique, sans affichage des valeurs et secrets des lignes voisines. Les commentaires tels que `; display_errors=Off` restent des lignes inactives et n'interdisent pas une proposition lorsque l'unique directive active correspond à la preuve. Les fichiers restent strictement non modifiés.

- Tests négatifs et compatibilité ajoutés dans `tests/test_patch_preview.py` ; vérification RED sur commit tests `c78c10d60e0c38e154376e1f39315fa6a8b955a0` (CI historiques en échec attendu), puis GREEN à partir du correctif `ffc68374acd2dd640c565a00752a39a018b6acaf`.
- La correction complémentaire `96269838bfc97d770f0850328dc7249f6c5b6550` conserve explicitement les affectations indentées par des tabulations ; les tests existants, les formats de sortie et la commande CLI restent inchangés.
- Cette vérification est une **cohérence statique locale**, pas une preuve de la configuration chargée par PHP ou d'une remédiation suffisante : mandat P2, revue humaine, tests en sandbox, rollback et validation de production restent nécessaires.
