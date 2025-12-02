# Mini Projet Programmation - Suivi et Analyse de la Consommation Énergétique
## Contexte

Ce mini-projet a pour objectif de simuler un dispositif de suivi et d’analyse de la consommation énergétique.
Il repose sur :
* La programmation orientée objet (POO)
* La simulation de capteurs IoT
* La détection d’anomalies
* L’enregistrement des données dans une base MongoDB
---
## Objectifs  
Le projet permet de :  
1. Mettre en place une architecture orientée objet claire et modulable.
2. Simuler des capteurs IoT générant des mesures aléatoires.
3. Stocker les mesures dans une base de données MongoDB locale.
4. Détecter les anomalies de consommation via un seuil configurable.
5. Assurer la qualité du code grâce à pytest pour les tests unitaires et flake8 pour le respect du style PEP8.
## Structure du projet
Projet/  
├── capteurs/                  # Classes et simulation des capteurs  
│   └── capteur.py  
├── analytics/                 # Détection d’anomalies  
│   └── anomaly_detector.py  
├── database/                  # Gestion de MongoDB  
│   └── mongo_manager.py  
├── tests/                     # Tests unitaires  
│   ├── test_capteur.py  
│   ├── test_anomaly_detector.py  
│   └── test_mongo_manager.py  
├── main.py                    # Script principal de simulation  
├── requirements.txt           # Dépendances du projet  
└── README.md                  # Documentation  


