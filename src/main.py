"""Main script to run the Titanic survival prediction pipeline."""

import config
from data_preprocessing import (
    calculate_survival_rates,
    load_data,
    preprocess_features,
)
from model_evaluation import (
    create_submission_file,
    generate_predictions,
    print_prediction_summary,
)
from model_training import get_model_info, train_random_forest


def main():
    """Execute the complete ML pipeline."""
    print("=" * 50)
    print("Titanic Survival Prediction Pipeline")
    print("=" * 50)

    # Step 1: Load data
    print("\n[1/5] Loading data...")
    train_data, test_data = load_data(config.TRAIN_DATA_PATH, config.TEST_DATA_PATH)
    print(f"  - Training set: {len(train_data)} passengers")
    print(f"  - Test set: {len(test_data)} passengers")

    # Step 2: Exploratory analysis
    print("\n[2/5] Exploratory analysis...")
    survival_rates = calculate_survival_rates(train_data)
    women_rate = survival_rates["women_survival_rate"]
    men_rate = survival_rates["men_survival_rate"]
    print(f"  - Women survival rate: {women_rate:.1%}")
    print(f"  - Men survival rate: {men_rate:.1%}")

    # Step 3: Preprocess features
    print("\n[3/5] Preprocessing features...")
    X_train, y_train, X_test = preprocess_features(
        train_data, test_data, config.FEATURES, config.TARGET
    )
    print(f"  - Features after encoding: {list(X_train.columns)}")
    print(f"  - Training samples: {len(X_train)}")

    # Step 4: Train model
    print("\n[4/5] Training Random Forest model...")
    model = train_random_forest(X_train, y_train, config.RANDOM_FOREST_PARAMS)
    model_info = get_model_info(model)
    print(f"  - Number of trees: {model_info['n_estimators']}")
    print(f"  - Max depth: {model_info['max_depth']}")
    print(f"  - Features used: {model_info['n_features']}")

    # Step 5: Generate predictions and save submission
    print("\n[5/5] Generating predictions...")
    predictions = generate_predictions(model, X_test)
    create_submission_file(test_data, predictions, config.SUBMISSION_PATH)
    print_prediction_summary(predictions)

    print("\n" + "=" * 50)
    print("Pipeline completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
