# A propos de la configuration de la database

La base de données est configurée dans le fichier `__init__.py` dans le dossier `models`. Les données de la base de données sont transférées à un fichier `config.py` à la racine du dossier `src`. Ce fichier `config.py` a pour but de prendre l'environnement (test pour le moment) et d'en extirper les données contenues dans un autre fichier `.env`, qui n'est pas dans le dépôt car il concerne des données confidentielles de l'application.

À ce stade, une table temporaire a été créée en localhost afin de m'assurer que la connexion à la base de données fonctionne.
