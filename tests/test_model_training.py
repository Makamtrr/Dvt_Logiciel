"""Unit tests for model_training module."""

import pandas as pd
import pytest
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from model_training import train_random_forest, get_model_info
from sklearn.ensemble import RandomForestClassifier


class TestTrainRandomForest:
    """Tests for train_random_forest function."""

    @pytest.fixture
    def sample_training_data(self):
        """Create sample training data."""
        X_train = pd.DataFrame(
            {
                "Pclass": [3, 1, 3, 2],
                "SibSp": [1, 0, 0, 1],
                "Parch": [0, 0, 0, 1],
                "Sex_female": [0, 1, 1, 0],
                "Sex_male": [1, 0, 0, 1],
            }
        )

        y_train = pd.Series([0, 1, 1, 0])

        return X_train, y_train

    def test_train_random_forest_returns_model(self, sample_training_data):
        """Test that training returns a RandomForestClassifier."""
        X_train, y_train = sample_training_data
        model_params = {"n_estimators": 10, "max_depth": 3, "random_state": 42}

        model = train_random_forest(X_train, y_train, model_params)

        assert isinstance(model, RandomForestClassifier)

    def test_train_random_forest_parameters(self, sample_training_data):
        """Test that model is trained with correct parameters."""
        X_train, y_train = sample_training_data
        model_params = {"n_estimators": 50, "max_depth": 4, "random_state": 1}

        model = train_random_forest(X_train, y_train, model_params)

        assert model.n_estimators == 50
        assert model.max_depth == 4
        assert model.random_state == 1

    def test_train_random_forest_is_fitted(self, sample_training_data):
        """Test that returned model is fitted."""
        X_train, y_train = sample_training_data
        model_params = {"n_estimators": 10, "max_depth": 3, "random_state": 42}

        model = train_random_forest(X_train, y_train, model_params)

        # Check if model can make predictions (i.e., it's fitted)
        predictions = model.predict(X_train)
        assert len(predictions) == len(y_train)

    def test_train_random_forest_custom_params(self, sample_training_data):
        """Test training with different parameter sets."""
        X_train, y_train = sample_training_data

        # Test with different parameters
        params1 = {"n_estimators": 20, "max_depth": 2, "random_state": 10}
        params2 = {"n_estimators": 30, "max_depth": 5, "random_state": 20}

        model1 = train_random_forest(X_train, y_train, params1)
        model2 = train_random_forest(X_train, y_train, params2)

        assert model1.n_estimators != model2.n_estimators
        assert model1.max_depth != model2.max_depth


class TestGetModelInfo:
    """Tests for get_model_info function."""

    @pytest.fixture
    def trained_model(self):
        """Create a trained model for testing."""
        X_train = pd.DataFrame(
            {
                "feature1": [1, 2, 3, 4],
                "feature2": [5, 6, 7, 8],
                "feature3": [9, 10, 11, 12],
            }
        )
        y_train = pd.Series([0, 1, 0, 1])

        model_params = {"n_estimators": 100, "max_depth": 5, "random_state": 42}
        model = RandomForestClassifier(**model_params)
        model.fit(X_train, y_train)

        return model

    def test_get_model_info_returns_dict(self, trained_model):
        """Test that get_model_info returns a dictionary."""
        info = get_model_info(trained_model)

        assert isinstance(info, dict)

    def test_get_model_info_contains_keys(self, trained_model):
        """Test that returned dict contains expected keys."""
        info = get_model_info(trained_model)

        assert "n_estimators" in info
        assert "max_depth" in info
        assert "n_features" in info
        assert "random_state" in info

    def test_get_model_info_correct_values(self, trained_model):
        """Test that returned values are correct."""
        info = get_model_info(trained_model)

        assert info["n_estimators"] == 100
        assert info["max_depth"] == 5
        assert info["n_features"] == 3
        assert info["random_state"] == 42

    def test_get_model_info_types(self, trained_model):
        """Test that returned values have correct types."""
        info = get_model_info(trained_model)

        assert isinstance(info["n_estimators"], int)
        assert isinstance(info["max_depth"], int)
        assert isinstance(info["n_features"], int)
        assert isinstance(info["random_state"], int)
