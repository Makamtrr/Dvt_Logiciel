"""Model training module for Titanic survival prediction."""

from typing import Any, Dict

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_random_forest(
    X_train: pd.DataFrame, y_train: pd.Series, model_params: Dict[str, Any]
) -> RandomForestClassifier:
    """
    Train a Random Forest Classifier model.

    Args:
        X_train: Training features (preprocessed)
        y_train: Training target variable
        model_params: Dictionary of Random Forest parameters
            - n_estimators: Number of trees
            - max_depth: Maximum depth of trees
            - random_state: Random seed for reproducibility

    Returns:
        Trained RandomForestClassifier model
    """
    model = RandomForestClassifier(**model_params)
    model.fit(X_train, y_train)

    return model


def get_model_info(model: RandomForestClassifier) -> dict:
    """
    Get information about the trained model.

    Args:
        model: Trained RandomForestClassifier

    Returns:
        Dictionary containing model information
    """
    return {
        "n_estimators": model.n_estimators,
        "max_depth": model.max_depth,
        "n_features": model.n_features_in_,
        "random_state": model.random_state,
    }
