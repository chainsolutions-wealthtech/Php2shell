# Vérification individuelle des diffs — tranche 003 (30 octobre 2026)

**Continuité :** `PHP2SHELL-CONT-20261027-ROOT-01`.  
**PR unique :** [#7](https://github.com/chainsolutions-wealthtech/Php2shell/pull/7).  
**HEAD avant la tranche :** `928a90944613258ee5dc44302529fd5db6194629`.  
**Périmètre :** 14 SHA **non contrôlés dans les tranches 001 et 002**, extraits du snapshot de 363 commits, répartis entre le 27 et le 28 octobre 2026.  
**Provenance :** `OBSERVED_IN_GITHUB` pour les réponses du connecteur, les commits et les dossiers Markdown.

## Méthode appliquée individuellement

Pour chacun des 14 SHA complets : récupération du commit source via `fetch_commit`, lecture du dossier `history/evidence/diffs/YYYY-MM-DD/<SHA>.md` au HEAD de la branche d'archives, extraction de la liste `files[]`, comparaison **textuelle à l'identique** de chaque champ `patch` dans les blocs `diff`, contrôle du nom exact de chaque fichier et égalité du nombre de blocs `diff` et de patchs exposés. Les chemins et les fichiers n'ont pas été reconstruits à partir d'hypothèses : ils ont été comparés aux réponses GitHub au SHA historique.

## Contrôle commit par commit

| Date UTC | Commit source | Dossier archivé | Fichiers exposés | Patchs textuels identiques | Objet de la modification |
|---|---|---|---:|---:|---|
| 2026-10-27 | [`d38521f8c85c4671a89590a005009154e790b93e`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/d38521f8c85c4671a89590a005009154e790b93e) | [dossier](diffs/2026-10-27/d38521f8c85c4671a89590a005009154e790b93e.md) | 1 | 1/1 | Masquage commentaires, chaînes, HTML et heredocs |
| 2026-10-27 | [`c4a12e4bd415e1488819f1c4985acd3783f2bcd8`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/c4a12e4bd415e1488819f1c4985acd3783f2bcd8) | [dossier](diffs/2026-10-27/c4a12e4bd415e1488819f1c4985acd3783f2bcd8.md) | 1 | 1/1 | Création du protocole canonique |
| 2026-10-27 | [`49065783562c995d14ab918b72cee827d95782d1`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/49065783562c995d14ab918b72cee827d95782d1) | [dossier](diffs/2026-10-27/49065783562c995d14ab918b72cee827d95782d1.md) | 1 | 1/1 | Fondation, six lots et provenance CVE |
| 2026-10-27 | [`3baefb27ee0715e2523a82589e49d04b784d5a89`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/3baefb27ee0715e2523a82589e49d04b784d5a89) | [dossier](diffs/2026-10-27/3baefb27ee0715e2523a82589e49d04b784d5a89.md) | 1 | 1/1 | Continuité frontend, P2 et PHPPATCH |
| 2026-10-27 | [`9e1171ece3dd5187547b33dbf8d58959560fffe9`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/9e1171ece3dd5187547b33dbf8d58959560fffe9) | [dossier](diffs/2026-10-27/9e1171ece3dd5187547b33dbf8d58959560fffe9.md) | 1 | 1/1 | Ancrage du DAG des 61 WP |
| 2026-10-27 | [`d8f2e9e01f21cc60216a4ab0bf8f01b2dd146b1c`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/d8f2e9e01f21cc60216a4ab0bf8f01b2dd146b1c) | [dossier](diffs/2026-10-27/d8f2e9e01f21cc60216a4ab0bf8f01b2dd146b1c.md) | 1 | 1/1 | Tests déduplication CSV/JSON/TXT |
| 2026-10-27 | [`8fc0477ec239fa39d484abcf1928fd63020a5b1f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/8fc0477ec239fa39d484abcf1928fd63020a5b1f) | [dossier](diffs/2026-10-27/8fc0477ec239fa39d484abcf1928fd63020a5b1f.md) | 1 | 1/1 | Composer lockfile et dépendances S1 |
| 2026-10-28 | [`4848bff596977595e58b28db01eaebcd1a128e14`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/4848bff596977595e58b28db01eaebcd1a128e14) | [dossier](diffs/2026-10-28/4848bff596977595e58b28db01eaebcd1a128e14.md) | 1 | 1/1 | Provenance avis PHP et limites d'applicabilité |
| 2026-10-28 | [`318d60e33858be0447540fc08b42a3c14b1d23f0`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/318d60e33858be0447540fc08b42a3c14b1d23f0) | [dossier](diffs/2026-10-28/318d60e33858be0447540fc08b42a3c14b1d23f0.md) | 4 | 4/4 | Convergence S1 des propositions d'avis |
| 2026-10-28 | [`1f51c37becc3007d7328494587ca7effbac6c8f5`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/1f51c37becc3007d7328494587ca7effbac6c8f5) | [dossier](diffs/2026-10-28/1f51c37becc3007d7328494587ca7effbac6c8f5.md) | 1 | 1/1 | Rejet d'une preuve runtime non textuelle |
| 2026-10-28 | [`c6d96345cc1f9d0cf7df540a3ead3aaa50a11f06`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/c6d96345cc1f9d0cf7df540a3ead3aaa50a11f06) | [dossier](diffs/2026-10-28/c6d96345cc1f9d0cf7df540a3ead3aaa50a11f06.md) | 1 | 1/1 | Traçabilité URL et rapports |
| 2026-10-28 | [`2b04f03f759148b3e749bdfb354bff6aa5764c24`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/2b04f03f759148b3e749bdfb354bff6aa5764c24) | [dossier](diffs/2026-10-28/2b04f03f759148b3e749bdfb354bff6aa5764c24.md) | 1 | 1/1 | Rapport HTML assaini |
| 2026-10-28 | [`440cdc91920ed3e1ed60639e040f082202d48984`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/440cdc91920ed3e1ed60639e040f082202d48984) | [dossier](diffs/2026-10-28/440cdc91920ed3e1ed60639e040f082202d48984.md) | 5 | 5/5 | Convergence S1 du contrat FastAPI loopback |
| 2026-10-28 | [`81650eb344fa3bfbc2318efffd4458f57c258f4f`](https://github.com/chainsolutions-wealthtech/Php2shell/commit/81650eb344fa3bfbc2318efffd4458f57c258f4f) | [dossier](diffs/2026-10-28/81650eb344fa3bfbc2318efffd4458f57c258f4f.md) | 6 | 6/6 | Continuité garde PHPPATCH ini |

## Constats techniques

- **14/14 dossiers** retrouvés et vérifiés individuellement.
- **26 fichiers** retournés par l'API GitHub pour ces commits.
- **26/26 patchs** textuels retournés par GitHub retrouvés **à l'identique** dans les dossiers correspondants.
- **26/26 noms de fichiers** retrouvés dans les dossiers correspondants.
- **26 blocs Markdown `diff`** au total, correspondant aux 26 patchs.
- Aucun champ `patch=null` dans cette tranche, contrairement aux deux fichiers vides de la tranche 002, qui ont depuis été vérifiés par [lecture de blob exact](2026-10-30-empty-blob-verification-001.md).
- Aucun écart ni troncature **des chaînes de patch exposées par le connecteur** constaté pour les 26 patchs. Cette phrase ne garantit pas que l'API GitHub expose nécessairement toutes les données possibles, ni que chaque patch soit sûr ou testé.

## Cumul des vérifications individuelles

| Tranche | Commits distincts | Patchs textuels exacts | Fichiers sans patch |
|---|---:|---:|---|
| [001](2026-10-30-patch-content-verification-001.md) | 3 | 6 | 0 |
| [002](2026-10-30-patch-content-verification-002.md) | 28 | 65 | 2 — vérifiés par [blobs](2026-10-30-empty-blob-verification-001.md) |
| **003 — présent document** | **14** | **26** | **0** |
| **Cumul** | **45/363** | **97/97** | **2/2 blobs contrôlés** |

Il reste **318 dossiers de diff du snapshot à auditer individuellement**. Les [écarts de branches post-snapshot](2026-10-30-post-snapshot-branch-reconciliation.md) ne sont pas inclus dans ce dénominateur de 363 : le dénombrement des nouveaux SHA distincts et leur vérification restent nécessaires. L'audit complet des 1 040 runs du snapshot et des runs ultérieurs, des jobs, des logs, des claims et des preuves S1/Plesk reste également `NOT_VERIFIED`.

**Aucune opération sur le code applicatif, `main`, S1, Plesk, MCP ou les autorisations n'a été effectuée. Statut global : `IN_PROGRESS`.**
