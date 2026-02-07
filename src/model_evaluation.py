"""Model evaluation and prediction module."""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def generate_predictions(
    model: RandomForestClassifier, X_test: pd.DataFrame
) -> pd.Series:
    """
    Generate predictions using the trained model.

    Args:
        model: Trained RandomForestClassifier
        X_test: Test features (preprocessed)

    Returns:
        Series of predictions (0 or 1)
    """
    predictions = model.predict(X_test)
    return predictions


def create_submission_file(
    test_data: pd.DataFrame, predictions: pd.Series, output_path: Path
) -> None:
    """
    Create submission CSV file with predictions.

    Args:
        test_data: Original test dataset (to get PassengerId)
        predictions: Model predictions
        output_path: Path where to save the submission file
    """
    output = pd.DataFrame(
        {"PassengerId": test_data.PassengerId, "Survived": predictions}
    )

    output.to_csv(output_path, index=False)
    print(f"Submission file saved successfully to: {output_path}")


def print_prediction_summary(predictions: pd.Series) -> None:
    """
    Print a summary of the predictions.

    Args:
        predictions: Series of predictions
    """
    total = len(predictions)
    survived = sum(predictions)
    died = total - survived

    print("\n=== Prediction Summary ===")
    print(f"Total passengers: {total}")
    print(f"Predicted to survive: {survived} ({survived/total*100:.1f}%)")
    print(f"Predicted to die: {died} ({died/total*100:.1f}%)")
    print("=" * 26)
