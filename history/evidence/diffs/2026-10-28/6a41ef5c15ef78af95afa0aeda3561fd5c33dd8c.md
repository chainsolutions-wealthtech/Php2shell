# Commit exact 6a41ef5c15ef78af95afa0aeda3561fd5c33dd8c

Date UTC 2026-10-28T05:08:49Z; source https://github.com/chainsolutions-wealthtech/Php2shell/commit/6a41ef5c15ef78af95afa0aeda3561fd5c33dd8c

Parents: 96269838bfc97d770f0850328dc7249f6c5b6550

Fichiers 1; +9/-0

## docs/V0_3_LOCAL_PATCH_PREVIEW.md (modified, +9/-0)

Blob df0ba8d6865972c9f4de09bf3ab675806c4da154; https://github.com/chainsolutions-wealthtech/Php2shell/blob/6a41ef5c15ef78af95afa0aeda3561fd5c33dd8c/docs%2FV0_3_LOCAL_PATCH_PREVIEW.md

```diff
@@ -36,3 +36,12 @@ La sortie JSON fournit le diff de contexte nul (une seule ligne remplacée), son
 `tests/test_patch_preview.py` couvre diff minimal, non-écriture, absence réseau, absence de secrets, refus des autres règles, fichiers ambigus/symboliques, CRLF et commande CLI.
 
 **Reste à construire** : moteur générique de propositions de correctifs PHP/runtime/config, diagnostics confirmés, sandbox Docker isolée et non-root, tests d'intégration, score de risque et preuve de rollback, émission de PR sous mandat et approbation, restauration effective et l'interface PHPPATCH authentifiée.
+
+
+## Durcissement additif — affectations actives contradictoires (28/10/2026)
+
+**Affectations multiples de `display_errors` : refus conservateur.** Si un même `php.ini` ou `.user.ini` présente plusieurs affectations actives de `display_errors`, même lorsque les valeurs semblent équivalentes, la fonction `propose_local_ini_patch` ne propose pas de diff uniligne : un tel diff ne justifie pas une configuration effective sans analyse des surcharges et de la SAPI. L'erreur reste générique, sans affichage des valeurs et secrets des lignes voisines. Les commentaires tels que `; display_errors=Off` restent des lignes inactives et n'interdisent pas une proposition lorsque l'unique directive active correspond à la preuve. Les fichiers restent strictement non modifiés.
+
+- Tests négatifs et compatibilité ajoutés dans `tests/test_patch_preview.py` ; vérification RED sur commit tests `c78c10d60e0c38e154376e1f39315fa6a8b955a0` (CI historiques en échec attendu), puis GREEN à partir du correctif `ffc68374acd2dd640c565a00752a39a018b6acaf`.
+- La correction complémentaire `96269838bfc97d770f0850328dc7249f6c5b6550` conserve explicitement les affectations indentées par des tabulations ; les tests existants, les formats de sortie et la commande CLI restent inchangés.
+- Cette vérification est une **cohérence statique locale**, pas une preuve de la configuration chargée par PHP ou d'une remédiation suffisante : mandat P2, revue humaine, tests en sandbox, rollback et validation de production restent nécessaires.
```

Attention: inspection du diff Git, sans attestation de tests ou d'exploitation.