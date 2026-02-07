# Étape 1 : Refactorisation du code

**Date de début :** 07/02/2026
**Statut :** En cours

## Objectifs de cette étape

1. Analyser le notebook Jupyter existant ([titanic-tutorial.ipynb](titanic-tutorial.ipynb))
2. Diviser le code monolithique en modules Python réutilisables
3. Créer les scripts suivants :
   - `data_preprocessing.py` : Nettoyage et prétraitement des données
   - `model_training.py` : Entraînement et sauvegarde du modèle
   - `model_evaluation.py` : Évaluation des performances
4. Appliquer les bonnes pratiques de code (PEP 8)
5. Gérer les dépendances avec `requirements.txt`

---

## 1. Analyse du notebook existant

### Structure du notebook tutorial :

Le notebook `titanic-tutorial.ipynb` contient :

#### Partie 1 : Chargement des données
- Import des bibliothèques (numpy, pandas)
- Lecture des fichiers CSV (train.csv, test.csv)
- Affichage des premières lignes

#### Partie 2 : Analyse exploratoire simple
- Calcul du taux de survie par genre
- Constatation : 74% des femmes survivent vs 19% des hommes

#### Partie 3 : Machine Learning (Random Forest)
- Import de sklearn.ensemble.RandomForestClassifier
- Sélection des features : Pclass, Sex, SibSp, Parch
- Encodage des variables catégorielles avec pd.get_dummies()
- Entraînement du modèle (100 arbres, profondeur max 5)
- Génération des prédictions
- Sauvegarde dans submission.csv

### Dépendances identifiées :
- numpy
- pandas
- scikit-learn

---

## 2. Architecture proposée

### Modules à créer :

```
src/
├── __init__.py
├── data_preprocessing.py    # Chargement et prétraitement des données
├── model_training.py         # Entraînement du modèle ML
├── model_evaluation.py       # Évaluation et prédictions
├── config.py                 # Configuration (chemins, paramètres)
└── main.py                   # Script principal d'exécution
```

### Flux de données :
1. **config.py** : Définit les chemins et paramètres
2. **data_preprocessing.py** : Charge et nettoie les données
3. **model_training.py** : Entraîne le modèle Random Forest
4. **model_evaluation.py** : Génère les prédictions et métriques
5. **main.py** : Orchestre l'ensemble du pipeline

---

## 3. Création des modules

### En cours...

_Cette section sera mise à jour au fur et à mesure de la création des modules._
