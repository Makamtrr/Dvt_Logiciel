"""Data preprocessing module for Titanic dataset."""

from pathlib import Path
from typing import Tuple

import pandas as pd


def load_data(train_path: Path, test_path: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load training and test datasets from CSV files.

    Args:
        train_path: Path to the training CSV file
        test_path: Path to the test CSV file

    Returns:
        Tuple containing (train_data, test_data) as pandas DataFrames

    Raises:
        FileNotFoundError: If CSV files are not found
    """
    try:
        train_data = pd.read_csv(train_path)
        test_data = pd.read_csv(test_path)
        return train_data, test_data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data file not found: {e}")


def preprocess_features(
    train_data: pd.DataFrame, test_data: pd.DataFrame, features: list, target: str
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
    """
    Preprocess features by encoding categorical variables.

    Uses pandas get_dummies for one-hot encoding of categorical features.

    Args:
        train_data: Training dataset
        test_data: Test dataset
        features: List of feature column names to use
        target: Name of the target column

    Returns:
        Tuple containing (X_train, y_train, X_test):
            - X_train: Processed training features
            - y_train: Training target variable
            - X_test: Processed test features
    """
    # Extract target variable from training data
    y_train = train_data[target]

    # Apply one-hot encoding to categorical features
    X_train = pd.get_dummies(train_data[features])
    X_test = pd.get_dummies(test_data[features])

    return X_train, y_train, X_test


def calculate_survival_rates(train_data: pd.DataFrame) -> dict:
    """
    Calculate survival rates by gender for exploratory analysis.

    Args:
        train_data: Training dataset containing Sex and Survived columns

    Returns:
        Dictionary with survival rates for women and men
    """
    women = train_data.loc[train_data.Sex == "female"]["Survived"]
    men = train_data.loc[train_data.Sex == "male"]["Survived"]

    rate_women = sum(women) / len(women)
    rate_men = sum(men) / len(men)

    return {"women_survival_rate": rate_women, "men_survival_rate": rate_men}
