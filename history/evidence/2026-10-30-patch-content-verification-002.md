# Contrôle individuel de contenu des diffs — tranche 002 (30 octobre 2026)

**Continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`  
**PR unique :** [#7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7) — `docs/integral-chronological-history-20261029`.  
**HEAD vérifié avant l'opération :** `322f579504c87347de32ba27e08e5ef5228e131a`.  
**Périmètre :** 28 commits du snapshot de 363 SHA, distincts des trois déjà contrôlés dans [la tranche 001](2026-10-30-patch-content-verification-001.md).  
**Provenance :** `OBSERVED_IN_GITHUB` pour les réponses du connecteur GitHub et les fichiers de PR #7. Cette comparaison n'est pas une signature cryptographique indépendante.

## Protocole de vérification réellement appliqué à chaque SHA

1. Récupération de `fetch_commit` au SHA complet, avec tableau `files[]` et champs `filename` et `patch` exposés par GitHub.
2. Lecture de `history/evidence/diffs/YYYY-MM-DD/<SHA>.md` **sur la branche PR #7**, et non sur `main`.
3. Pour chaque `files[].patch` de type chaîne : vérification de sa présence **à l'identique**, sans normalisation des espaces ou des sauts de ligne, dans un bloc Markdown `diff` du dossier. L'une des deux délimitations de fin de bloc `\n\`\`\`` ou `\`\`\`` est acceptée selon le caractère final du patch GitHub.
4. Vérification de la présence de chaque `filename` dans le dossier et de l'égalité entre le nombre de blocs `diff` et le nombre de patchs effectivement fournis par GitHub.
5. Conservation explicite des fichiers dont l'API ne retourne **aucun patch** : absence de patch ≠ preuve de contenu comparé. Les fichiers vides peuvent être concernés, sans conclure que le blob est vide sans une autre vérification.
6. Les conventions de titres diffèrent selon les lots historiques : certains dossiers emploient `### \`nom\``, d'autres `## nom (status)`. L'inspection utilise le nom exact du fichier, pas un titre Markdown imposé. Cela évite de signaler à tort des patchs identiques comme divergents.

## Vérification individuelle — 28 commits et 67 entrées de fichiers

| Date UTC | SHA source | Dossier de diff archivé | Fichiers GitHub | Patchs exacts | Résultat | Objet historique |
|---|---|---|---:|---:|---|---|
| 2026-10-22 | [`a8600e6f4d702563a0a0ec6f4d935b0d0ddf0409`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/a8600e6f4d702563a0a0ec6f4d935b0d0ddf0409) | [dossier](diffs/2026-10-22/a8600e6f4d702563a0a0ec6f4d935b0d0ddf0409.md) | 1 | 1/1 | PASS | README V0.1 |
| 2026-10-22 | [`a9d799b008fc65ed5745745bc4ef09e8b889aabe`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/a9d799b008fc65ed5745745bc4ef09e8b889aabe) | [dossier](diffs/2026-10-22/a9d799b008fc65ed5745745bc4ef09e8b889aabe.md) | 12 | 11/11 | PASS pour les patchs exposés ; fichier sans patch API | Fondation CLI/laboratoire/CI ; app/__init__.py sans patch API |
| 2026-10-22 | [`bcc102ed5ba53bfab82067a1bcf3634817c4c87f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/bcc102ed5ba53bfab82067a1bcf3634817c4c87f) | [dossier](diffs/2026-10-22/bcc102ed5ba53bfab82067a1bcf3634817c4c87f.md) | 7 | 7/7 | PASS | Documentation et tests V0.1 |
| 2026-10-27 | [`ee5564960d924257f7f12996d59f1701872395fa`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/ee5564960d924257f7f12996d59f1701872395fa) | [dossier](diffs/2026-10-27/ee5564960d924257f7f12996d59f1701872395fa.md) | 1 | 1/1 | PASS | Inventaire statique PHP/Composer |
| 2026-10-27 | [`733ded954f52a8dbeceafc8886153eb780d81cc9`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/733ded954f52a8dbeceafc8886153eb780d81cc9) | [dossier](diffs/2026-10-27/733ded954f52a8dbeceafc8886153eb780d81cc9.md) | 1 | 1/1 | PASS | Tests de l'inventaire |
| 2026-10-27 | [`ce88a2c457c85458550f85c8aa2b8d8fbba725a7`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/ce88a2c457c85458550f85c8aa2b8d8fbba725a7) | [dossier](diffs/2026-10-27/ce88a2c457c85458550f85c8aa2b8d8fbba725a7.md) | 1 | 1/1 | PASS | CLI scan-local |
| 2026-10-27 | [`d77932b64a1735bb71292c85281851916c31321a`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/d77932b64a1735bb71292c85281851916c31321a) | [dossier](diffs/2026-10-27/d77932b64a1735bb71292c85281851916c31321a.md) | 1 | 1/1 | PASS | Documentation du scanner |
| 2026-10-27 | [`fbf22c060035e0ec5edc99a15714302f74556a3f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/fbf22c060035e0ec5edc99a15714302f74556a3f) | [dossier](diffs/2026-10-27/fbf22c060035e0ec5edc99a15714302f74556a3f.md) | 1 | 1/1 | PASS | Exclusions vendor |
| 2026-10-27 | [`42b095734a5cfc882c0d579b2a1de6ba6e4b9801`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/42b095734a5cfc882c0d579b2a1de6ba6e4b9801) | [dossier](diffs/2026-10-27/42b095734a5cfc882c0d579b2a1de6ba6e4b9801.md) | 1 | 1/1 | PASS | Tests vendor imbriqué |
| 2026-10-28 | [`47303c1eea0fc7d454ef5b73ac53d94e5c16875f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/47303c1eea0fc7d454ef5b73ac53d94e5c16875f) | [dossier](diffs/2026-10-28/47303c1eea0fc7d454ef5b73ac53d94e5c16875f.md) | 1 | 1/1 | PASS | Documentation CSV et confidentialité |
| 2026-10-28 | [`baf7dc9916e117f13ac3d9ce606f72a4e58d38d4`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/baf7dc9916e117f13ac3d9ce606f72a4e58d38d4) | [dossier](diffs/2026-10-28/baf7dc9916e117f13ac3d9ce606f72a4e58d38d4.md) | 7 | 7/7 | PASS | Convergence S1 et audit configuration PHP |
| 2026-10-28 | [`2d95ecfaa4adb2010751c770484b3886300abbc2`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/2d95ecfaa4adb2010751c770484b3886300abbc2) | [dossier](diffs/2026-10-28/2d95ecfaa4adb2010751c770484b3886300abbc2.md) | 1 | 1/1 | PASS | Continuité audit PHP ini |
| 2026-10-28 | [`2b92c5b07a858d41ae50af7328661fec24113ff4`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/2b92c5b07a858d41ae50af7328661fec24113ff4) | [dossier](diffs/2026-10-28/2b92c5b07a858d41ae50af7328661fec24113ff4.md) | 1 | 1/1 | PASS | Continuité audit PHP ini |
| 2026-10-28 | [`b719b4f8182fc5adfbc6a0f5409b8311f9721326`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/b719b4f8182fc5adfbc6a0f5409b8311f9721326) | [dossier](diffs/2026-10-28/b719b4f8182fc5adfbc6a0f5409b8311f9721326.md) | 1 | 1/1 | PASS | Continuité audit PHP ini |
| 2026-10-28 | [`4c289b926d62b85e302a37cc30f705225dc05c68`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/4c289b926d62b85e302a37cc30f705225dc05c68) | [dossier](diffs/2026-10-28/4c289b926d62b85e302a37cc30f705225dc05c68.md) | 1 | 1/1 | PASS | Continuité audit PHP ini |
| 2026-10-28 | [`98b27584005b16606ac74a7d83471cbc755c5239`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/98b27584005b16606ac74a7d83471cbc755c5239) | [dossier](diffs/2026-10-28/98b27584005b16606ac74a7d83471cbc755c5239.md) | 1 | 1/1 | PASS | CLI provenance avis |
| 2026-10-28 | [`708d912ad19b54a4a9410084058d9114396d591c`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/708d912ad19b54a4a9410084058d9114396d591c) | [dossier](diffs/2026-10-28/708d912ad19b54a4a9410084058d9114396d591c.md) | 4 | 4/4 | PASS | Convergence S1 collecteur GHSA |
| 2026-10-28 | [`35953760a0b71511bf3631cc68d47f210a11fd19`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/35953760a0b71511bf3631cc68d47f210a11fd19) | [dossier](diffs/2026-10-28/35953760a0b71511bf3631cc68d47f210a11fd19.md) | 1 | 1/1 | PASS | Dossier d'audit local |
| 2026-10-28 | [`033dbe37e4283291b5ee7812048ab1a0bfcdc635`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/033dbe37e4283291b5ee7812048ab1a0bfcdc635) | [dossier](diffs/2026-10-28/033dbe37e4283291b5ee7812048ab1a0bfcdc635.md) | 1 | 1/1 | PASS | Tests DNS/redirections |
| 2026-10-28 | [`bed8bfc182612c30963f52018d371397eac72e5f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/bed8bfc182612c30963f52018d371397eac72e5f) | [dossier](diffs/2026-10-28/bed8bfc182612c30963f52018d371397eac72e5f.md) | 4 | 4/4 | PASS | Continuité PHPPATCH et S1 |
| 2026-10-28 | [`b231bd7f4e7874c24cef75e06bb550cfcc706d83`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/b231bd7f4e7874c24cef75e06bb550cfcc706d83) | [dossier](diffs/2026-10-28/b231bd7f4e7874c24cef75e06bb550cfcc706d83.md) | 1 | 1/1 | PASS | Tests limites Content-Length |
| 2026-10-28 | [`c22ac964e1cbb71d880e8ef828cf7bd96d485960`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/c22ac964e1cbb71d880e8ef828cf7bd96d485960) | [dossier](diffs/2026-10-28/c22ac964e1cbb71d880e8ef828cf7bd96d485960.md) | 6 | 5/5 | PASS pour les patchs exposés ; fichier sans patch API | Convergence S1 attestation Ed25519 ; auth_tests/__init__.py sans patch API |
| 2026-10-29 | [`973f4dbb0fffbcf256b5813030f625204fc9fa53`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/973f4dbb0fffbcf256b5813030f625204fc9fa53) | [dossier](diffs/2026-10-29/973f4dbb0fffbcf256b5813030f625204fc9fa53.md) | 2 | 2/2 | PASS | Durcissement PHPPATCH O_NOFOLLOW |
| 2026-10-29 | [`5ae7245e9aa4857aca3835546a9a46ebea969d1f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/5ae7245e9aa4857aca3835546a9a46ebea969d1f) | [dossier](diffs/2026-10-29/5ae7245e9aa4857aca3835546a9a46ebea969d1f.md) | 2 | 2/2 | PASS | Convergence S1 PHPPATCH |
| 2026-10-29 | [`96fc1ee6edd88f8743a91aa33407610c75a77474`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/96fc1ee6edd88f8743a91aa33407610c75a77474) | [dossier](diffs/2026-10-29/96fc1ee6edd88f8743a91aa33407610c75a77474.md) | 4 | 4/4 | PASS | P2S-EVT-048 |
| 2026-10-29 | [`86b68bd26ac889ff54b4f04a0746168c34b24909`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/86b68bd26ac889ff54b4f04a0746168c34b24909) | [dossier](diffs/2026-10-29/86b68bd26ac889ff54b4f04a0746168c34b24909.md) | 1 | 1/1 | PASS | Validation technique documentée |
| 2026-10-29 | [`301d443dcbf4e3834980f04c85fceb532b2887e5`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/301d443dcbf4e3834980f04c85fceb532b2887e5) | [dossier](diffs/2026-10-29/301d443dcbf4e3834980f04c85fceb532b2887e5.md) | 1 | 1/1 | PASS | Protocole de validation |
| 2026-10-29 | [`9517abd090c5e7cffed62e4c77c1826f0282310f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/9517abd090c5e7cffed62e4c77c1826f0282310f) | [dossier](diffs/2026-10-29/9517abd090c5e7cffed62e4c77c1826f0282310f.md) | 1 | 1/1 | PASS | Tests limites DNS/TTL |

## Contrôle des totaux et anomalies

- **28/28 dossiers** retrouvés et inspectés individuellement dans cette tranche.
- **67 entrées de fichiers** retournées par les commits source.
- **65 patchs textuels** retournés par GitHub, **65/65 reproduits textuellement à l'identique** dans les dossiers archivés.
- **65 blocs `diff`** présents dans les dossiers pour ces 65 patchs : aucun bloc manquant ni bloc supplémentaire constaté dans ce périmètre.
- **67/67 noms de fichiers** retrouvés dans les dossiers respectifs.
- **Deux fichiers sans `patch` dans la réponse GitHub**, donc sans contenu de patch contrôlable par cette méthode : `app/__init__.py` au SHA `a9d799b008fc65ed5745745bc4ef09e8b889aabe`, et `auth_tests/__init__.py` au SHA `c22ac964e1cbb71d880e8ef828cf7bd96d485960`. **Statut du contenu de ces deux fichiers : `NOT_VERIFIED`**, même si leur nom est présent.
- Aucun écart textuel observé pour les patchs effectivement exposés. Cela ne prouve ni l'absence d'omission du côté de l'API GitHub, ni l'intégrité indépendante des blobs, ni la correction fonctionnelle du code.

## Cumul strict avec la tranche 001

La [tranche 001](2026-10-30-patch-content-verification-001.md) avait vérifié **3 commits, 6 patchs, 6 correspondances**. Les 28 SHA de la présente tranche ne sont pas ceux de la tranche 001.

**Cumul observé : 31/363 dossiers individuellement comparés, 71/71 patchs textuels exposés et comparés à l'identique, 332 dossiers du snapshot restant à contrôler.** Deux entrées de fichiers sans patch nécessitent un contrôle de blob distinct. Les 363 dossiers du snapshot ne prouvent toujours pas la couverture des commits apparus ensuite sur les branches.

## Suites probatoires nécessaires

Continuer sur les **332 SHA non encore audités individuellement**, puis traiter les deux entrées sans patch par récupération des blobs exacts. Vérifier ensuite les SHA postérieurs au snapshot, la totalité des jobs/logs CI, les attestations de déploiement éventuelles et les liens de provenance `décision → WP/REQ → commit → CI → checkpoint`. Les couches non vérifiées restent `NOT_VERIFIED` ; l'archive n'est pas `DONE`.

**Aucune modification applicative, aucun claim, aucun déploiement, aucune fusion et aucune écriture hors PR #7 n'ont été réalisés pour cette vérification.**
