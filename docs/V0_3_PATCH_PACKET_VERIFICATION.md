# V0.3 — Revalidation locale d'un paquet PHPPATCH (non autorisante)

Le module `app.patch_packet_verifier` complète le paquet de revue
`app.patch_review_packet` sans exécuter de correctif. Il recalcule le dossier
d'audit local et **compare l'intégralité du paquet** fourni avec la version
reconstruite depuis les fichiers actuels, pas uniquement son empreinte.

## Utilisation hors ligne

```python
from app.patch_packet_verifier import load_and_verify_local_review_packet

result = load_and_verify_local_review_packet(
    "/chemin/local/packet.json",
    "/chemin/local/projet-autorise",
    "2026-10-28",
    "P2S-EV-0123456789abcdef",
)
```

L'identifiant doit provenir du dossier d'audit courant ; l'exemple est fictif.
La fonction accepte également un objet Python via
`verify_local_review_packet(packet, project_path, as_of_utc, evidence_id)`.

## Garde-fous

- Lecture de fichier JSON local uniquement, limite 16 Kio, rejet des liens
  symboliques, des clés JSON dupliquées et des constantes non finies.
- Comparaison canonique des **types et champs complets** : toute modification,
  promotion de drapeau, champ supplémentaire ou dossier obsolète est refusé.
- Les erreurs ne reproduisent ni configuration PHP, ni source, ni secrets.
- Les tests vérifient le refus des altérations, l'absence de réseau et
  l'absence d'écriture sur les fichiers du projet.

## Frontières de confiance

Un paquet correspondant aux fichiers locaux **n'est pas signé** et ne prouve
ni identité, ni mandat P1/P2, ni propriété de domaine, ni approbation, ni
compatibilité PHP/SAPI, ni test Docker, ni correction d'une CVE. La sortie
conserve `ready_for_production=false`, `patch_applied=false` et
`identity_and_mandate_verified=false`. Le contrôle ne contacte aucun
site, ne crée aucune PR, ne modifie ni `main` ni S1.

Cette tranche constitue une preuve **partielle** pour le transfert et la
revue PHPPATCH (REQ-030, P2S-WF-R06) et la non-régression (P2S-WF-Q01).
Elle ne remplace pas les gates réels de la roadmap V0.1→V1.0.

## Renforcement du lecteur local (28 octobre 2026)

Le fichier de paquet est ouvert en lecture seule avec `O_NOFOLLOW` et
`O_NONBLOCK` lorsqu'ils sont disponibles. Le descripteur est contrôlé par
`fstat` : seul un fichier ordinaire de 16 Kio maximum est accepté ; les
répertoires, FIFO et liens symboliques finaux sont refusés. Le lecteur borne
également les octets effectivement lus et refuse un changement observable de
taille ou de métadonnées pendant la lecture. Si `O_NOFOLLOW` n'existe pas,
il échoue en mode fermé plutôt que d'affirmer une lecture protégée.

Ces vérifications réduisent les risques de substitution locale entre le
contrôle du chemin et l'ouverture. Elles ne constituent **pas** une protection
complète contre toutes les mutations concurrentes des répertoires parents,
ni un verrouillage de snapshot, une signature, un mandat ou une preuve de
propriété. Aucune écriture, connexion réseau ou exécution PHP n'est ajoutée.
