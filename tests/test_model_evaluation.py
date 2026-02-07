"""Unit tests for model_evaluation module."""

import pandas as pd
import pytest
from pathlib import Path
import sys
import tempfile
import os

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from model_evaluation import (
    generate_predictions,
    create_submission_file,
    print_prediction_summary,
)
from sklearn.ensemble import RandomForestClassifier


class TestGeneratePredictions:
    """Tests for generate_predictions function."""

    @pytest.fixture
    def trained_model(self):
        """Create a simple trained model."""
        X_train = pd.DataFrame(
            {
                "feature1": [1, 2, 3, 4],
                "feature2": [5, 6, 7, 8],
            }
        )
        y_train = pd.Series([0, 1, 0, 1])

        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X_train, y_train)

        return model

    def test_generate_predictions_returns_series(self, trained_model):
        """Test that predictions are returned as a Series."""
        X_test = pd.DataFrame(
            {
                "feature1": [5, 6],
                "feature2": [9, 10],
            }
        )

        predictions = generate_predictions(trained_model, X_test)

        assert isinstance(predictions, (pd.Series, type(predictions)))

    def test_generate_predictions_correct_length(self, trained_model):
        """Test that number of predictions matches test data length."""
        X_test = pd.DataFrame(
            {
                "feature1": [5, 6, 7],
                "feature2": [9, 10, 11],
            }
        )

        predictions = generate_predictions(trained_model, X_test)

        assert len(predictions) == 3

    def test_generate_predictions_binary_values(self, trained_model):
        """Test that predictions are binary (0 or 1)."""
        X_test = pd.DataFrame(
            {
                "feature1": [5, 6, 7, 8],
                "feature2": [9, 10, 11, 12],
            }
        )

        predictions = generate_predictions(trained_model, X_test)

        # All predictions should be 0 or 1
        assert all(pred in [0, 1] for pred in predictions)


class TestCreateSubmissionFile:
    """Tests for create_submission_file function."""

    def test_create_submission_file_creates_file(self, capsys):
        """Test that submission file is created."""
        test_data = pd.DataFrame(
            {
                "PassengerId": [1, 2, 3],
                "Pclass": [3, 1, 2],
            }
        )

        predictions = pd.Series([0, 1, 0])

        # Use temporary file
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as temp_file:
            temp_path = Path(temp_file.name)

        try:
            create_submission_file(test_data, predictions, temp_path)

            # Check file exists
            assert temp_path.exists()

            # Check file content
            submission = pd.read_csv(temp_path)
            assert len(submission) == 3
            assert "PassengerId" in submission.columns
            assert "Survived" in submission.columns

        finally:
            # Clean up
            if temp_path.exists():
                os.unlink(temp_path)

    def test_create_submission_file_correct_format(self):
        """Test that submission file has correct format."""
        test_data = pd.DataFrame(
            {
                "PassengerId": [892, 893, 894],
                "Pclass": [3, 1, 2],
            }
        )

        predictions = pd.Series([0, 1, 1])

        # Use temporary file
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as temp_file:
            temp_path = Path(temp_file.name)

        try:
            create_submission_file(test_data, predictions, temp_path)

            # Read and verify
            submission = pd.read_csv(temp_path)

            assert list(submission["PassengerId"]) == [892, 893, 894]
            assert list(submission["Survived"]) == [0, 1, 1]

        finally:
            if temp_path.exists():
                os.unlink(temp_path)

    def test_create_submission_file_prints_message(self, capsys):
        """Test that success message is printed."""
        test_data = pd.DataFrame(
            {
                "PassengerId": [1, 2],
                "Pclass": [3, 1],
            }
        )

        predictions = pd.Series([0, 1])

        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as temp_file:
            temp_path = Path(temp_file.name)

        try:
            create_submission_file(test_data, predictions, temp_path)

            captured = capsys.readouterr()
            assert "saved successfully" in captured.out.lower()

        finally:
            if temp_path.exists():
                os.unlink(temp_path)


class TestPrintPredictionSummary:
    """Tests for print_prediction_summary function."""

    def test_print_prediction_summary_output(self, capsys):
        """Test that summary is printed correctly."""
        predictions = pd.Series([0, 1, 1, 0, 1])

        print_prediction_summary(predictions)

        captured = capsys.readouterr()
        output = captured.out

        assert "Total passengers: 5" in output
        assert "Predicted to survive: 3" in output
        assert "Predicted to die: 2" in output

    def test_print_prediction_summary_percentages(self, capsys):
        """Test that percentages are displayed."""
        predictions = pd.Series([1, 1, 0, 0])

        print_prediction_summary(predictions)

        captured = capsys.readouterr()
        output = captured.out

        assert "50.0%" in output

    def test_print_prediction_summary_all_survived(self, capsys):
        """Test with all passengers surviving."""
        predictions = pd.Series([1, 1, 1])

        print_prediction_summary(predictions)

        captured = capsys.readouterr()
        output = captured.out

        assert "Predicted to survive: 3" in output
        assert "100.0%" in output

    def test_print_prediction_summary_none_survived(self, capsys):
        """Test with no passengers surviving."""
        predictions = pd.Series([0, 0, 0])

        print_prediction_summary(predictions)

        captured = capsys.readouterr()
        output = captured.out

        assert "Predicted to survive: 0" in output
        assert "0.0%" in output
