"""Unit tests for data_preprocessing module."""

import pandas as pd
import pytest
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from data_preprocessing import (
    load_data,
    preprocess_features,
    calculate_survival_rates,
)


class TestLoadData:
    """Tests for load_data function."""

    def test_load_data_success(self):
        """Test successful loading of train and test data."""
        train_path = Path("titanic/train.csv")
        test_path = Path("titanic/test.csv")

        train_data, test_data = load_data(train_path, test_path)

        assert isinstance(train_data, pd.DataFrame)
        assert isinstance(test_data, pd.DataFrame)
        assert len(train_data) == 891
        assert len(test_data) == 418

    def test_load_data_file_not_found(self):
        """Test that FileNotFoundError is raised for missing files."""
        train_path = Path("nonexistent/train.csv")
        test_path = Path("nonexistent/test.csv")

        with pytest.raises(FileNotFoundError):
            load_data(train_path, test_path)

    def test_load_data_columns_present(self):
        """Test that required columns are present in loaded data."""
        train_path = Path("titanic/train.csv")
        test_path = Path("titanic/test.csv")

        train_data, test_data = load_data(train_path, test_path)

        # Check train data columns
        assert "PassengerId" in train_data.columns
        assert "Survived" in train_data.columns
        assert "Pclass" in train_data.columns
        assert "Sex" in train_data.columns

        # Check test data columns
        assert "PassengerId" in test_data.columns
        assert "Pclass" in test_data.columns
        assert "Sex" in test_data.columns


class TestPreprocessFeatures:
    """Tests for preprocess_features function."""

    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing."""
        train_data = pd.DataFrame(
            {
                "PassengerId": [1, 2, 3],
                "Survived": [0, 1, 1],
                "Pclass": [3, 1, 3],
                "Sex": ["male", "female", "female"],
                "SibSp": [1, 1, 0],
                "Parch": [0, 0, 0],
            }
        )

        test_data = pd.DataFrame(
            {
                "PassengerId": [4, 5],
                "Pclass": [1, 2],
                "Sex": ["male", "female"],
                "SibSp": [0, 1],
                "Parch": [0, 1],
            }
        )

        return train_data, test_data

    def test_preprocess_features_shapes(self, sample_data):
        """Test that preprocessing returns correct shapes."""
        train_data, test_data = sample_data
        features = ["Pclass", "Sex", "SibSp", "Parch"]
        target = "Survived"

        X_train, y_train, X_test = preprocess_features(
            train_data, test_data, features, target
        )

        assert len(X_train) == 3
        assert len(y_train) == 3
        assert len(X_test) == 2

    def test_preprocess_features_encoding(self, sample_data):
        """Test that categorical features are one-hot encoded."""
        train_data, test_data = sample_data
        features = ["Pclass", "Sex", "SibSp", "Parch"]
        target = "Survived"

        X_train, y_train, X_test = preprocess_features(
            train_data, test_data, features, target
        )

        # Check that Sex is encoded
        assert "Sex_male" in X_train.columns or "Sex_female" in X_train.columns

    def test_preprocess_features_target_extraction(self, sample_data):
        """Test that target variable is correctly extracted."""
        train_data, test_data = sample_data
        features = ["Pclass", "Sex", "SibSp", "Parch"]
        target = "Survived"

        X_train, y_train, X_test = preprocess_features(
            train_data, test_data, features, target
        )

        # Check target values
        assert list(y_train) == [0, 1, 1]
        assert isinstance(y_train, pd.Series)


class TestCalculateSurvivalRates:
    """Tests for calculate_survival_rates function."""

    def test_calculate_survival_rates_basic(self):
        """Test calculation of survival rates."""
        train_data = pd.DataFrame(
            {
                "Sex": ["male", "male", "female", "female"],
                "Survived": [0, 0, 1, 1],
            }
        )

        rates = calculate_survival_rates(train_data)

        assert "women_survival_rate" in rates
        assert "men_survival_rate" in rates
        assert rates["women_survival_rate"] == 1.0
        assert rates["men_survival_rate"] == 0.0

    def test_calculate_survival_rates_mixed(self):
        """Test calculation with mixed survival rates."""
        train_data = pd.DataFrame(
            {
                "Sex": ["male", "male", "female", "female"],
                "Survived": [0, 1, 1, 0],
            }
        )

        rates = calculate_survival_rates(train_data)

        assert rates["women_survival_rate"] == 0.5
        assert rates["men_survival_rate"] == 0.5

    def test_calculate_survival_rates_types(self):
        """Test that return types are correct."""
        train_data = pd.DataFrame(
            {
                "Sex": ["male", "female"],
                "Survived": [0, 1],
            }
        )

        rates = calculate_survival_rates(train_data)

        assert isinstance(rates, dict)
        assert isinstance(rates["women_survival_rate"], float)
        assert isinstance(rates["men_survival_rate"], float)
