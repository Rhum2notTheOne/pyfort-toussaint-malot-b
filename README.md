# Projet TI101 : Simulateur Fort Boyard

## Introduction
Un projet Python simple basé sur Fort Boyard. Le but : réussir des épreuves pour obtenir des clés et ouvrir la salle du trésor.

## Organisation
Fichiers principaux :
- **`epreuves_mathematiques.py`** : Jeux mathématiques (factorielles, etc.).
- **`epreuves_hasard.py`** : Jeux de chance (lancer de dés, etc.).
- **`epreuves_logiques.py`** : Jeux logiques comme le NIM.
- **`enigme_pere_fouras.py`** : Énigmes du Père Fouras.
- **`epreuve_finale.py`** : Salle du trésor.

Les fichiers JSON pour les énigmes et indices sont dans le dossier `data`.

## Fonctionnement
1. Créer une équipe (1 à 3 joueurs).
2. Faire les épreuves et gagner des clés.
3. Ouvrir la salle du trésor avec les indices.

## Installation
1. Clonez le projet :
   ```bash
   git clone https://github.com/Rhum2notTheOne/pyfort-toussaint-malot-b
   ```
2. Lancez le jeu :
   ```python
   python main.py
   ```

## Points à Améliorer
- Ajouter des épreuves.
- Sauvegarder les parties.
- 
## Contributeurs
@S3nda
@Rhum2notTheOne

## Notes
Certaines fonctions utilisent le mot "pick" pour choisir les épreuves. Ce choix respecte le principe de polymorphisme en programmation objet.
Amusez-vous bien avec ce jeu Fort Boyard !

