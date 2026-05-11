import pandas as pd
import numpy as np
import joblib
import mlflow
import mlflow.sklearn
import os

from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor

from preprocessing import preprocessing_pipeline


def adjusted_r2(r2, n, p):

    return 1 - (
        ((1 - r2) * (n - 1)) /
        (n - p - 1)
    )


df = pd.read_csv("cleand.csv")

df = preprocessing_pipeline.fit_transform(df)

df = pd.DataFrame(df)

TARGET = 'screen_on_time'

selected_features = [

    'age',

    'gender',

    'app_usage_time',

    'number_of_apps_installed',

    'battery_drain',

    'data_usage',

    'sleep_hours',

    'notifications',

    'social_media_usage',

    'gaming_time',

    'study_work_time',

    'weekend_usage',

    'data_per_hour',

    'battery_drain_per_hour',

    'device_stress_score',

    'heavy_gamer'
]

X = df[selected_features]

y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42
)

models = {

    'Linear Regression':
        LinearRegression(),

    'Random Forest':
        RandomForestRegressor(
            random_state=42
        ),

    'XGBoost':
        XGBRegressor(
            random_state=42
        ),

    'LightGBM':
        LGBMRegressor(
            random_state=42
        ),

    'CatBoost':
        CatBoostRegressor(
            verbose=0,
            random_state=42
        )
}

os.makedirs("mlruns", exist_ok=True)

mlflow.set_tracking_uri(
    "file:./mlruns"
)

mlflow.set_experiment(
    "Mobile Addiction Prediction"
)

results = []

with mlflow.start_run():

    for name, model in models.items():

        model.fit(X_train, y_train)

        y_train_pred = model.predict(X_train)

        y_test_pred = model.predict(X_test)

        train_r2 = r2_score(
            y_train,
            y_train_pred
        )

        test_r2 = r2_score(
            y_test,
            y_test_pred
        )

        train_adj_r2 = adjusted_r2(
            train_r2,
            X_train.shape[0],
            X_train.shape[1]
        )

        test_adj_r2 = adjusted_r2(
            test_r2,
            X_test.shape[0],
            X_test.shape[1]
        )

        mae = mean_absolute_error(
            y_test,
            y_test_pred
        )

        mse = mean_squared_error(
            y_test,
            y_test_pred
        )

        rmse = np.sqrt(mse)

        difference = abs(
            train_r2 - test_r2
        )

        mlflow.log_metric(
            f"{name}_Train_R2",
            train_r2
        )

        mlflow.log_metric(
            f"{name}_Test_R2",
            test_r2
        )

        mlflow.log_metric(
            f"{name}_Train_Adjusted_R2",
            train_adj_r2
        )

        mlflow.log_metric(
            f"{name}_Test_Adjusted_R2",
            test_adj_r2
        )

        mlflow.log_metric(
            f"{name}_MAE",
            mae
        )

        mlflow.log_metric(
            f"{name}_RMSE",
            rmse
        )

        results.append({

            'Model': name,

            'Train R2':
                round(train_r2, 4),

            'Train Adjusted R2':
                round(train_adj_r2, 4),

            'Test R2':
                round(test_r2, 4),

            'Test Adjusted R2':
                round(test_adj_r2, 4),

            'Difference':
                round(difference, 4),

            'MAE':
                round(mae, 4),

            'RMSE':
                round(rmse, 4)
        })

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(

        by='Test R2',

        ascending=False
    )

    print(results_df)

    best_model_name = results_df.iloc[0]['Model']

    print(f"\nBest Model : {best_model_name}")

    param_grids = {

        'Random Forest': {

            'n_estimators': [100, 200, 300],

            'max_depth': [None, 10, 20],

            'min_samples_split': [2, 5, 10]
        },

        'XGBoost': {

            'n_estimators': [100, 200, 300],

            'max_depth': [3, 5, 7],

            'learning_rate': [0.01, 0.05, 0.1]
        },

        'LightGBM': {

            'n_estimators': [100, 200, 300],

            'learning_rate': [0.01, 0.05, 0.1],

            'num_leaves': [31, 50, 100]
        },

        'CatBoost': {

            'iterations': [100, 200, 300],

            'depth': [4, 6, 8],

            'learning_rate': [0.01, 0.05, 0.1]
        }
    }

    if best_model_name == 'Linear Regression':

        final_model = models[best_model_name]

        final_model.fit(X_train, y_train)

    else:

        best_model = models[best_model_name]

        random_search = RandomizedSearchCV(

            estimator=best_model,

            param_distributions=
                param_grids[best_model_name],

            n_iter=10,

            scoring='r2',

            cv=3,

            verbose=2,

            random_state=42,

            n_jobs=-1
        )

        random_search.fit(X_train, y_train)

        final_model = random_search.best_estimator_

        print("\nBest Parameters:\n")

        print(random_search.best_params_)

        y_train_pred = final_model.predict(X_train)

        y_test_pred = final_model.predict(X_test)

        train_r2 = r2_score(
            y_train,
            y_train_pred
        )

        test_r2 = r2_score(
            y_test,
            y_test_pred
        )

        train_adj_r2 = adjusted_r2(
            train_r2,
            X_train.shape[0],
            X_train.shape[1]
        )

        test_adj_r2 = adjusted_r2(
            test_r2,
            X_test.shape[0],
            X_test.shape[1]
        )

        print("\nTUNED MODEL RESULTS\n")

        print(f"Train R2          : {round(train_r2,4)}")

        print(f"Train Adjusted R2 : {round(train_adj_r2,4)}")

        print(f"Test R2           : {round(test_r2,4)}")

        print(f"Test Adjusted R2  : {round(test_adj_r2,4)}")

        mlflow.log_metric(
            "Final_Train_R2",
            train_r2
        )

        mlflow.log_metric(
            "Final_Test_R2",
            test_r2
        )

        mlflow.log_metric(
            "Final_Train_Adjusted_R2",
            train_adj_r2
        )

        mlflow.log_metric(
            "Final_Test_Adjusted_R2",
            test_adj_r2
        )
    joblib.dump(final_model, "best_model.pkl")

    try:

        mlflow.sklearn.log_model(
            sk_model=final_model,
            artifact_path="best_model"
        )

    except Exception as e:

        print("\nMLFLOW LOGGING ERROR\n")

        print(e)

    print("\nModel Saved Successfully")