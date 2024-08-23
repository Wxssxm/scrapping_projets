# scraping_projets
Script de Web Scraping des appels à projets de Bpifrance

## Description
Ce script Python permet de scraper les appels à projets disponibles sur la page de Bpifrance. Il extrait les informations pertinentes pour chaque projet et les enregistre dans un fichier JSON.

## Fonctionnalités
-Scraping du site Bpifrance : Le script envoie une requête à la page des appels à projets et extrait les données utiles.

-Extraction des informations : Il récupère le titre, le lien, la description et les dates de chaque appel à projets.

-Génération d'un fichier JSON & CSV: Les informations extraites sont sauvegardées dans un fichier JSON et un CSV.

## Prérequis

Avant d'exécuter le script, installer les dépendances suivantes :

```bash
pip install requests beautifulsoup4 pandas
```

## Instructions d'utilisation
Téléchargement du script :
Copiez le code dans un fichier Python .py (ex: scraping_bpifrance.py)

Exécution du script :
1.Ouvrir un terminal.

2.Naviguer jusqu'au répertoire où se trouve le script.

3.Exécuter le script avec la commande suivante :
```bash
python scraping_bpifrance.py
```
Un fichier JSON et un fichier CSV sont créés dans le même répertoire que le script, respectivement sous les nom "appels_à_projets.json" et "appels_à_projets.csv".

