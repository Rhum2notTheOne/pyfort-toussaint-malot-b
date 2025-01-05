# Projet TI101 : Simulateur Fort Boyard

## Introduction
Bonjour ! Voici un projet Python inspiré de Fort Boyard. Le but est de recréer des épreuves amusantes pour gagner des clés et accéder à la salle du trésor.

## Organisation
Le projet est divisé en plusieurs fichiers Python :
- **`epreuves_mathematiques.py`** : Épreuves de maths comme les factorielles.
- **`epreuves_hasard.py`** : Jeux de chance comme le lancer de dés.
- **`epreuves_logiques.py`** : Épreuves de logique (ex. : le jeu de NIM).
- **`enigme_pere_fouras.py`** : Résoudre des énigmes du Père Fouras.
- **`epreuve_finale.py`** : Trouver le mot-code pour la salle du trésor.

Les données comme les énigmes et indices sont dans le dossier `data` en fichiers JSON.

## Fonctionnement
1. **Composer une équipe** : Jusqu'à 3 joueurs avec des rôles différents.
2. **Participer aux épreuves** : Réussissez pour obtenir des clés.
3. **Débloquer la salle du trésor** : Utilisez les indices pour deviner le mot-code.

## Installation
1. Clonez le projet :
   ```bash
   git clone <url_du_projet>
   ```
2. Exécutez le fichier principal :
   ```bash
   python main.py
   ```

## Points d'amélioration
- Ajouter plus d'épreuves.
- Permettre la sauvegarde des parties.

## Remerciements
Merci de jouer et amusez-vous bien avec ce simulateur Fort Boyard !


#### design du code

- nous avons choisi de nommer les fonctions relatives à la selection des epreuves "pick" plutôt que "epreuve_math" par exemple
  en effet, nous avons trouvé que "pick" était plus explicite et respectait le principe de polymorphisme
