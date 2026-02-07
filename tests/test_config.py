"""Unit tests for config module."""

import pytest
from pathlib import Path

import config


class TestConfigPaths:
    """Tests for configuration paths."""

    def test_project_root_exists(self):
        """Test that project root directory exists."""
        assert config.PROJECT_ROOT.exists()
        assert config.PROJECT_ROOT.is_dir()

    def test_data_dir_configuration(self):
        """Test that data directory is correctly configured."""
        assert config.DATA_DIR == config.PROJECT_ROOT / "titanic"

    def test_train_data_path(self):
        """Test that train data path is correct."""
        assert config.TRAIN_DATA_PATH == config.DATA_DIR / "train.csv"
        assert config.TRAIN_DATA_PATH.exists()

    def test_test_data_path(self):
        """Test that test data path is correct."""
        assert config.TEST_DATA_PATH == config.DATA_DIR / "test.csv"
        assert config.TEST_DATA_PATH.exists()

    def test_output_dir_created(self):
        """Test that output directory is created."""
        assert config.OUTPUT_DIR.exists()
        assert config.OUTPUT_DIR.is_dir()


class TestModelParameters:
    """Tests for model parameters configuration."""

    def test_random_forest_params_type(self):
        """Test that model parameters are a dictionary."""
        assert isinstance(config.RANDOM_FOREST_PARAMS, dict)

    def test_random_forest_params_keys(self):
        """Test that required parameter keys exist."""
        assert "n_estimators" in config.RANDOM_FOREST_PARAMS
        assert "max_depth" in config.RANDOM_FOREST_PARAMS
        assert "random_state" in config.RANDOM_FOREST_PARAMS

    def test_random_forest_params_values(self):
        """Test that parameter values are valid."""
        assert config.RANDOM_FOREST_PARAMS["n_estimators"] > 0
        assert config.RANDOM_FOREST_PARAMS["max_depth"] > 0
        assert isinstance(config.RANDOM_FOREST_PARAMS["random_state"], int)

    def test_random_forest_params_default_values(self):
        """Test default parameter values."""
        assert config.RANDOM_FOREST_PARAMS["n_estimators"] == 100
        assert config.RANDOM_FOREST_PARAMS["max_depth"] == 5
        assert config.RANDOM_FOREST_PARAMS["random_state"] == 1


class TestFeaturesConfiguration:
    """Tests for features configuration."""

    def test_features_type(self):
        """Test that FEATURES is a list."""
        assert isinstance(config.FEATURES, list)

    def test_features_not_empty(self):
        """Test that features list is not empty."""
        assert len(config.FEATURES) > 0

    def test_features_content(self):
        """Test that expected features are present."""
        assert "Pclass" in config.FEATURES
        assert "Sex" in config.FEATURES
        assert "SibSp" in config.FEATURES
        assert "Parch" in config.FEATURES

    def test_target_variable(self):
        """Test that target variable is correctly set."""
        assert config.TARGET == "Survived"
        assert isinstance(config.TARGET, str)
