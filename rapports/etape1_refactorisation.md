# Étape 1 : Refactorisation du code

**Date de début :** 07/02/2026
**Statut :** ✅ Terminé

## Objectifs de cette étape

1. Analyser le notebook Jupyter existant ([titanic-tutorial.ipynb](../titanic-tutorial.ipynb))
2. Diviser le code monolithique en modules Python réutilisables
3. Créer les scripts suivants :
   - `data_preprocessing.py` : Nettoyage et prétraitement des données
   - `model_training.py` : Entraînement et sauvegarde du modèle
   - `model_evaluation.py` : Évaluation des performances
4. Appliquer les bonnes pratiques de code (PEP 8)
5. Gérer les dépendances avec `requirements.txt`

---

## 1. Analyse du notebook existant

### Structure du notebook tutorial

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

### Dépendances identifiées
- numpy
- pandas
- scikit-learn

---

## 2. Architecture proposée

### Modules créés

```
src/
├── __init__.py
├── config.py                 # Configuration centrale ✅
├── data_preprocessing.py     # Chargement et prétraitement ✅
├── model_training.py         # Entraînement du modèle ✅
├── model_evaluation.py       # Évaluation et prédictions ✅
└── main.py                   # Pipeline principal ✅
```

### Flux de données
1. **config.py** : Définit les chemins et paramètres
2. **data_preprocessing.py** : Charge et nettoie les données
3. **model_training.py** : Entraîne le modèle Random Forest
4. **model_evaluation.py** : Génère les prédictions et métriques
5. **main.py** : Orchestre l'ensemble du pipeline

---

## 3. Création des modules

### 3.1 Module [config.py](../src/config.py)

**Objectif :** Configuration centralisée du projet

**Contenu :**
- Chemins des fichiers de données (train.csv, test.csv)
- Chemin du fichier de sortie (submission.csv)
- Paramètres du modèle Random Forest
- Liste des features utilisées
- Nom de la variable cible

**Avantages :**
- Facilite la modification des paramètres
- Évite les valeurs "en dur" dans le code
- Point unique de configuration

### 3.2 Module [data_preprocessing.py](../src/data_preprocessing.py)

**Fonctions créées :**

1. `load_data(train_path, test_path)` :
   - Charge les données depuis les fichiers CSV
   - Gestion des erreurs (FileNotFoundError)
   - Retourne les DataFrames train et test

2. `preprocess_features(train_data, test_data, features, target)` :
   - Extraction de la variable cible
   - Encodage one-hot des variables catégorielles avec `pd.get_dummies()`
   - Retourne X_train, y_train, X_test

3. `calculate_survival_rates(train_data)` :
   - Analyse exploratoire simple
   - Calcul des taux de survie par genre
   - Retourne un dictionnaire avec les taux

**Bonnes pratiques appliquées :**
- Type hints pour tous les paramètres et retours
- Docstrings complètes (Google Style)
- Gestion des exceptions
- Noms de fonctions explicites

### 3.3 Module [model_training.py](../src/model_training.py)

**Fonctions créées :**

1. `train_random_forest(X_train, y_train, model_params)` :
   - Entraîne un modèle RandomForestClassifier
   - Paramètres configurables via dictionnaire
   - Retourne le modèle entraîné

2. `get_model_info(model)` :
   - Extrait les informations du modèle
   - Retourne un dictionnaire avec les paramètres

**Avantages :**
- Modularité : facile de changer de modèle
- Configuration externe des hyperparamètres
- Réutilisabilité du code

### 3.4 Module [model_evaluation.py](../src/model_evaluation.py)

**Fonctions créées :**

1. `generate_predictions(model, X_test)` :
   - Génère les prédictions sur les données test
   - Retourne une Series pandas

2. `create_submission_file(test_data, predictions, output_path)` :
   - Crée le fichier CSV de soumission
   - Format : PassengerId, Survived
   - Message de confirmation

3. `print_prediction_summary(predictions)` :
   - Affiche un résumé des prédictions
   - Statistiques : total, survivants, décédés, pourcentages

**Avantages :**
- Séparation des responsabilités
- Affichage utilisateur clair et informatif
- Export automatique des résultats

### 3.5 Module [main.py](../src/main.py)

**Objectif :** Script principal orchestrant le pipeline

**Structure du pipeline :**
1. Chargement des données
2. Analyse exploratoire (taux de survie)
3. Prétraitement des features
4. Entraînement du modèle
5. Génération des prédictions et export

**Affichage :**
- Progress indicator ([1/5], [2/5], ...)
- Informations à chaque étape
- Résumé final

---

## 4. Gestion des dépendances

### Fichier [requirements.txt](../requirements.txt) créé avec :

**Librairies principales :**
- numpy >= 1.21.0
- pandas >= 1.3.0
- scikit-learn >= 1.0.0

**Outils de qualité de code :**
- flake8 >= 4.0.0 (linting)
- black >= 22.0.0 (formatage)
- isort >= 5.10.0 (organisation des imports)

**Testing :**
- pytest >= 7.0.0
- pytest-cov >= 3.0.0

**Documentation :**
- pydocstyle >= 6.1.0
- sphinx >= 4.5.0

---

## 5. Qualité du code (PEP 8)

### 5.1 Vérification avec flake8

```bash
python -m flake8 src/*.py
```

**Résultat :** ✅ Aucune erreur

**Corrections effectuées :**
- Suppression de l'import inutile `os` dans [config.py:3](../src/config.py#L3)
- Réduction de lignes trop longues (> 79 caractères)
- Formatage correct des fonctions

### 5.2 Formatage avec black

```bash
python -m black src/*.py
```

**Résultat :** 5 fichiers reformatés
- Indentation cohérente
- Espacement standardisé
- Guillemets doubles pour les chaînes

### 5.3 Organisation des imports avec isort

```bash
python -m isort src/*.py
```

**Résultat :** Imports organisés selon PEP 8
- Imports stdlib en premier
- Imports tiers ensuite
- Imports locaux en dernier

---

## 6. Tests et validation

### 6.1 Exécution du pipeline

```bash
python src/main.py
```

**Résultat :** ✅ Pipeline exécuté avec succès

**Sortie :**
- 891 passagers dans le training set
- 418 passagers dans le test set
- Taux de survie : 74.2% femmes, 18.9% hommes
- Modèle entraîné : 100 arbres, profondeur max 5
- Prédictions générées : 148 survivants (35.4%), 270 décédés (64.6%)
- Fichier submission.csv créé dans `output/`

### 6.2 Validation des résultats

✅ Le fichier `output/submission.csv` est créé
✅ Format correct : PassengerId, Survived
✅ 418 prédictions (une par passager test)
✅ Valeurs binaires (0 ou 1)

---

## 7. Améliorations par rapport au notebook

### Structure
- ❌ Notebook monolithique → ✅ Modules séparés et réutilisables
- ❌ Code dans des cellules → ✅ Fonctions avec signatures claires

### Qualité
- ❌ Pas de type hints → ✅ Type hints complets
- ❌ Documentation minimale → ✅ Docstrings détaillées
- ❌ Pas de gestion d'erreurs → ✅ Exceptions gérées

### Maintenabilité
- ❌ Paramètres en dur → ✅ Configuration centralisée
- ❌ Difficulté de test → ✅ Fonctions testables unitairement
- ❌ Pas de vérification PEP 8 → ✅ Code formaté et linté

### Organisation
- ❌ Tout dans un fichier → ✅ Architecture modulaire claire
- ❌ Dépendances non listées → ✅ requirements.txt
- ❌ Pas de versioning → ✅ Git + GitHub

---

## 8. Architecture finale

```
projet/
├── src/
│   ├── __init__.py              # Package marker
│   ├── config.py                # Configuration centrale ✅
│   ├── data_preprocessing.py    # Chargement et prétraitement ✅
│   ├── model_training.py        # Entraînement du modèle ✅
│   ├── model_evaluation.py      # Évaluation et prédictions ✅
│   └── main.py                  # Pipeline principal ✅
│
├── output/
│   └── submission.csv           # Fichier de soumission généré ✅
│
├── requirements.txt             # Dépendances ✅
└── rapports/
    └── etape1_refactorisation.md # Ce rapport ✅
```

---

## Résumé de l'Étape 1

**Statut :** ✅ **TERMINÉ**

**Réalisations :**
- [x] Analyse du notebook original
- [x] Création de 5 modules Python modulaires
- [x] Application stricte de PEP 8
- [x] Configuration centralisée (config.py)
- [x] Gestion des dépendances (requirements.txt)
- [x] Pipeline fonctionnel et testé
- [x] Code formaté (black, isort)
- [x] Code linté (flake8)
- [x] Documentation complète (docstrings)
- [x] Versioning Git (branche feature/refactoring-notebook)

**Outils utilisés :**
- Python 3.13
- pandas, numpy, scikit-learn
- flake8, black, isort
- Git + GitHub

**Bonnes pratiques appliquées :**
- Architecture modulaire
- Séparation des responsabilités (SoC)
- Type hints
- Docstrings Google Style
- Gestion des erreurs
- Configuration externe
- PEP 8 compliance

**Prochaines étapes :**
1. Merger la feature branch dans develop
2. Étape 2 : Ajouter des tests unitaires avec pytest
3. Continuer le projet

---

**Date de fin :** 07/02/2026
