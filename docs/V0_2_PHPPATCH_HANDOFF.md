# V0.2 — Handoff PHP2SHELL → PHPPATCH (brouillon hors ligne)

**Statut : contrat local de revue uniquement.** Cette tranche complète partiellement P2S-WF-E12 / P2S-WF-Q01 et prépare P2S-WF-R06 ; elle ne déclare **aucun** de ces work packages terminé, car les dépendances d'autorisation, d'API et de revue restent bloquantes.

Le module \`app/dossier_handoff.py\` consomme uniquement le résultat local de \`build_audit_dossier\` et produit une file **de revue humaine** à champs autorisés. Il refuse les dossiers modifiés, les preuves dupliquées, les statuts de vulnérabilité/approbation élevés et les affirmations de runtime authentifié. Il recalcule l'empreinte SHA-256 du dossier pour la cohérence : **une empreinte peut être recalculée par un attaquant et ne prouve ni identité, ni intégrité authentifiée, ni consentement**. Les règles d'indicateurs sont recalculées pour empêcher qu'une simple réécriture de l'empreinte ne suffise à promouvoir un dossier.

Utilisation locale dans un projet déjà autorisé :

\`\`\`python
from app.audit_dossier import build_audit_dossier
from app.dossier_handoff import prepare_phppatch_handoff

dossier = build_audit_dossier("./projet-autorise", "2026-10-28")
handoff = prepare_phppatch_handoff(dossier)
assert handoff["ready_for_patch_generation"] is False
assert handoff["patches_generated"] == 0
\`\`\`

La sortie ne contient **ni code source, ni chemin relatif de fichier, ni secret de configuration, ni identité ou référence de mandat, ni adresse d'actif** : seulement identifiants d'observation, règles indicatives, gates et statuts de non-exécution. Même une file vide ne vaut pas certificat de sécurité.

**Gates non franchis :** authentification propriétaire/mandat P2 par les autorités existantes, attestation de la provenance et du runtime PHP/SAPI/backports, génération de diffs dans Docker isolé, tests de non-régression, approbation humaine indépendante et rollback. Aucun appel réseau, aucun patch, aucune écriture serveur, aucune interface Web et aucun déploiement S1. Le moteur partagé et les deux destinations \`php2shell.wealthtechinnovations.com\` / \`phppatch.wealthtechinnovations.com\` restent les objectifs de V0.4/V1.0.

Tests : \`python -m unittest discover -s tests -v\`. Contrôler les deux CI GitHub Actions au **SHA exact** avant de considérer cette tranche techniquement validée. Le parcours complet URL → audit autorisé → diagnostic → PHPPATCH, les 32 exigences, six lots et 61 work packages demeurent intacts.
