"""Configuration module for Titanic Survival Prediction project."""

from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "titanic"
TRAIN_DATA_PATH = DATA_DIR / "train.csv"
TEST_DATA_PATH = DATA_DIR / "test.csv"
GENDER_SUBMISSION_PATH = DATA_DIR / "gender_submission.csv"

# Output directory
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
SUBMISSION_PATH = OUTPUT_DIR / "submission.csv"

# Model parameters
RANDOM_FOREST_PARAMS = {"n_estimators": 100, "max_depth": 5, "random_state": 1}

# Features to use for training
FEATURES = ["Pclass", "Sex", "SibSp", "Parch"]

# Target variable
TARGET = "Survived"
