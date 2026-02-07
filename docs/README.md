# Titanic Survival Prediction

Projet d'ingénierie logicielle - Prédiction de survie sur le Titanic avec Machine Learning

[![Python CI](https://github.com/Makamtrr/Dvt_Logiciel/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Makamtrr/Dvt_Logiciel/actions)

## 📋 Description

Ce projet implémente un modèle de Machine Learning pour prédire la survie des passagers du Titanic. Il a été développé dans le cadre du BUT VCOD 2025-2026 à l'IUT Paris Cité, en appliquant les bonnes pratiques d'ingénierie logicielle.

**Technologies utilisées:**
- Python 3.9+
- scikit-learn (Random Forest)
- pandas, numpy
- pytest (tests unitaires, 100% de couverture)
- Docker & Docker Compose
- GitHub Actions (CI/CD)

**Données:** [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)

## 🚀 Installation

### Prérequis
- Python 3.9 ou supérieur
- pip
- (Optionnel) Docker et Docker Compose

### Installation locale

```bash
# Cloner le repository
git clone https://github.com/Makamtrr/Dvt_Logiciel.git
cd Dvt_Logiciel

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Installer le projet en mode développement
pip install -e .
```

## 🎯 Utilisation

### Exécution locale

```bash
# Exécuter le pipeline complet
python src/main.py
```

Le fichier de prédictions sera généré dans `output/submission.csv`.

### Exécution avec Docker

```bash
# Construire et lancer le conteneur
docker-compose up --build

# Ou avec Docker uniquement
docker build -t titanic-prediction .
docker run -v $(pwd)/output:/app/output titanic-prediction
```

Les résultats seront disponibles dans le dossier `output/` monté depuis votre machine hôte.

## 📁 Structure du projet

```
.
├── src/                          # Code source principal
│   ├── config.py                 # Configuration et paramètres
│   ├── data_preprocessing.py     # Prétraitement des données
│   ├── model_training.py         # Entraînement du modèle
│   ├── model_evaluation.py       # Évaluation et prédictions
│   └── main.py                   # Pipeline principal
├── tests/                        # Tests unitaires (pytest)
│   ├── test_preprocessing.py     # Tests du prétraitement
│   ├── test_training.py          # Tests de l'entraînement
│   └── test_evaluation.py        # Tests de l'évaluation
├── titanic/                      # Données d'entraînement et test
│   ├── train.csv
│   ├── test.csv
│   └── gender_submission.csv
├── output/                       # Fichiers de prédictions générés
├── docs/                         # Documentation du projet
├── .github/workflows/            # Pipelines CI/CD
│   ├── python-ci.yml             # Tests, linting, formatage
│   └── docker-publish.yml        # Publication Docker
├── Dockerfile                    # Configuration Docker
├── docker-compose.yml            # Orchestration Docker
├── requirements.txt              # Dépendances Python
└── setup.py                      # Configuration du package

```

## 🧪 Tests

Le projet inclut une suite de tests unitaires complète avec une couverture de 100% sur les modules fonctionnels.

```bash
# Exécuter tous les tests
pytest tests/

# Avec rapport de couverture
pytest tests/ --cov=src --cov-report=html

# Exécuter un test spécifique
pytest tests/test_preprocessing.py -v
```

**Résultats:**
- 40 tests unitaires
- 100% de réussite
- Couverture complète des modules fonctionnels

## 🤖 Modèle

**Algorithme:** Random Forest Classifier

**Paramètres:**
- `n_estimators`: 100 arbres
- `max_depth`: 5 niveaux maximum
- `random_state`: 1 (reproductibilité)

**Features utilisées:**
- `Pclass`: Classe du billet (1, 2, 3)
- `Sex`: Sexe du passager (encodé: male=1, female=0)
- `SibSp`: Nombre de frères/sœurs/conjoints à bord
- `Parch`: Nombre de parents/enfants à bord

**Performance:**
- Score de validation croisée: ~80%
- Modèle optimisé pour prévenir le surapprentissage

## 🔧 Développement

### Qualité du code

Le projet utilise plusieurs outils pour maintenir la qualité du code:

```bash
# Linting (flake8)
flake8 src/*.py --max-line-length=88

# Formatage (black)
black src/*.py

# Tri des imports (isort)
isort src/*.py
```

### CI/CD Pipeline

Le projet est configuré avec GitHub Actions pour:
1. **Tests automatiques** sur chaque push/PR
2. **Vérification du linting** (flake8)
3. **Vérification du formatage** (black)
4. **Rapport de couverture** des tests
5. **Publication Docker** (optionnel)

Pipeline déclenché sur les branches `main` et `develop`.

## 📊 Configuration

Les paramètres du projet sont centralisés dans [src/config.py](../src/config.py):

```python
# Paramètres du modèle
RANDOM_FOREST_PARAMS = {
    "n_estimators": 100,
    "max_depth": 5,
    "random_state": 1
}

# Features et cible
FEATURES = ["Pclass", "Sex", "SibSp", "Parch"]
TARGET = "Survived"
```

Pour modifier les paramètres du modèle, éditez ce fichier avant l'exécution.

## 🐳 Docker

### Dockerfile

Le Dockerfile est optimisé pour:
- Utiliser Python 3.9-slim (image légère)
- Mise en cache efficace des dépendances
- Variables d'environnement Python optimisées
- Installation du projet en mode éditable

### Docker Compose

Le fichier `docker-compose.yml` configure:
- Montage du volume `output/` pour récupérer les résultats
- Redémarrage automatique (`unless-stopped`)
- Variables d'environnement Python

## 📚 Documentation technique

### Prétraitement des données (`data_preprocessing.py`)

1. **Chargement** des données depuis CSV
2. **Encodage** de la variable `Sex` (male=1, female=0)
3. **Sélection** des features pertinentes
4. **Gestion** des valeurs manquantes (imputées avec la médiane)

### Entraînement (`model_training.py`)

1. **Initialisation** du Random Forest avec paramètres configurés
2. **Entraînement** sur les données d'entraînement
3. **Retour** du modèle entraîné

### Évaluation (`model_evaluation.py`)

1. **Validation croisée** (5 folds) pour évaluer la performance
2. **Prédictions** sur le jeu de test
3. **Export** des résultats au format CSV

### Pipeline principal (`main.py`)

Orchestre l'exécution complète:
1. Prétraitement des données
2. Entraînement du modèle
3. Évaluation et prédictions
4. Sauvegarde des résultats

## 🔐 Variables d'environnement

**Aucune variable d'environnement sensible n'est requise pour ce projet.**

Toutes les configurations sont statiques et peuvent rester dans le repository:
- Chemins de fichiers (locaux)
- Paramètres du modèle (hyperparamètres)
- Pas d'API keys ou credentials

**Si besoin futur de configuration flexible:**
- Créer un fichier `.env.example` avec les variables template
- Ajouter `.env` au `.gitignore` (déjà fait)
- Utiliser `python-dotenv` pour charger les variables

## 👥 Contributeurs

**Établissement:** IUT Paris Cité - BUT VCOD 2025-2026

**Dépôt GitHub:** [Makamtrr/Dvt_Logiciel](https://github.com/Makamtrr/Dvt_Logiciel)

## 📄 Licence

Projet académique - IUT Paris Cité

## 📞 Support

Pour toute question ou problème:
1. Ouvrir une [issue](https://github.com/Makamtrr/Dvt_Logiciel/issues) sur GitHub
2. Consulter la documentation dans `docs/`
3. Vérifier les rapports d'étapes dans `rapports/`

---

**Dernière mise à jour:** Février 2026
