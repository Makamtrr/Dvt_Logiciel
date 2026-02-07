# Titanic Survival Prediction

Projet d'ingénierie logicielle - Prédiction de survie sur le Titanic avec Machine Learning

## 🚀 Quick Start

```bash
# Installation
pip install -r requirements.txt

# Exécution
python src/main.py

# Tests
pytest tests/
```

## 📁 Structure

```
src/
├── config.py              # Configuration
├── data_preprocessing.py  # Prétraitement données
├── model_training.py      # Entraînement modèle
├── model_evaluation.py    # Évaluation & prédictions
└── main.py                # Pipeline principal

tests/                     # Tests unitaires (40 tests, 100% réussite)
output/                    # Prédictions CSV
```

## 🎯 Résultats

- **Modèle :** Random Forest (100 arbres, profondeur 5)
- **Features :** Pclass, Sex, SibSp, Parch
- **Couverture tests :** 100% sur modules fonctionnels
- **Sortie :** `output/submission.csv`

## 📊 Projet

- **Établissement :** IUT Paris Cité - BUT VCOD 2025-2026
- **Source données :** [Kaggle Titanic](https://www.kaggle.com/c/titanic)
- **Dépôt :** [GitHub](https://github.com/Makamtrr/Dvt_Logiciel)
