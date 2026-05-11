# import pandas as pd
# import numpy as np
#
# from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.pipeline import Pipeline
# from sklearn.impute import KNNImputer
# from sklearn.preprocessing import LabelEncoder
#
#
#
# df = pd.read_csv("cleand.csv")
#
#
#
# original_columns = df.columns.tolist()
#
#
#
# class MedianImputer(BaseEstimator, TransformerMixin):
#
#     def __init__(self, column):
#
#         self.column = column
#
#     def fit(self, X, y=None):
#
#         self.median_value = X[self.column].median()
#
#         return self
#
#     def transform(self, X):
#
#         X = X.copy()
#
#         X[self.column] = X[self.column].fillna(
#             self.median_value
#         )
#
#         return X
#
#
#
# class GroupMedianImputer(BaseEstimator, TransformerMixin):
#
#     def __init__(self, group_col, target_col):
#
#         self.group_col = group_col
#         self.target_col = target_col
#
#     def fit(self, X, y=None):
#
#         self.group_medians = (
#             X.groupby(self.group_col)[self.target_col]
#             .median()
#         )
#
#         return self
#
#     def transform(self, X):
#
#         X = X.copy()
#
#         X[self.target_col] = (
#             X.groupby(self.group_col)[self.target_col]
#             .transform(
#                 lambda x: x.fillna(
#                     self.group_medians[x.name]
#                 )
#             )
#         )
#
#         return X
#
#
#
# class KNNColumnImputer(BaseEstimator, TransformerMixin):
#
#     def __init__(self, columns, n_neighbors=5):
#
#         self.columns = columns
#         self.n_neighbors = n_neighbors
#
#         self.imputer = KNNImputer(
#             n_neighbors=n_neighbors
#         )
#
#     def fit(self, X, y=None):
#
#         self.imputer.fit(
#             X[self.columns]
#         )
#
#         return self
#
#     def transform(self, X):
#
#         X = X.copy()
#
#         X[self.columns] = self.imputer.transform(
#             X[self.columns]
#         )
#
#         return X
#
#
#
# class UsageIntensityCreator(BaseEstimator, TransformerMixin):
#
#     def fit(self, X, y=None):
#
#         return self
#
#     def transform(self, X):
#
#         X = X.copy()
#
#         X['usage_intensity'] = (
#             X['app_usage_time'] *
#             X['number_of_apps_installed']
#         )
#
#         return X
#
#
#
# class MultiColumnLabelEncoder(BaseEstimator, TransformerMixin):
#
#     def __init__(self, columns):
#
#         self.columns = columns
#         self.encoders = {}
#
#     def fit(self, X, y=None):
#
#         for col in self.columns:
#
#             le = LabelEncoder()
#
#             le.fit(
#                 X[col].astype(str)
#             )
#
#             self.encoders[col] = le
#
#         return self
#
#     def transform(self, X):
#
#         X = X.copy()
#
#         for col in self.columns:
#
#             X[col] = self.encoders[col].transform(
#                 X[col].astype(str)
#             )
#
#         return X
#
#
#
# preprocessing_pipeline = Pipeline([
#
#
#     (
#         'apps_median_imputer',
#
#         MedianImputer(
#             column='number_of_apps_installed'
#         )
#     ),
#
#
#     (
#         'gaming_time_group_imputer',
#
#         GroupMedianImputer(
#             group_col='user_behavior_class',
#             target_col='gaming_time'
#         )
#     ),
#
#
#     (
#         'addiction_knn_imputer',
#
#         KNNColumnImputer(
#
#             columns=[
#                 'app_usage_time',
#                 'screen_on_time',
#                 'social_media_usage',
#                 'gaming_time',
#                 'notifications',
#                 'sleep_hours',
#                 'addiction_score'
#             ],
#
#             n_neighbors=5
#         )
#     ),
#
#
#     (
#         'usage_intensity_creator',
#
#         UsageIntensityCreator()
#     ),
#
#
#     (
#         'entertainment_dependency_imputer',
#
#         GroupMedianImputer(
#             group_col='user_behavior_class',
#             target_col='entertainment_dependency'
#         )
#     ),
#
#
#     (
#         'wellness_knn_imputer',
#
#         KNNColumnImputer(
#
#             columns=[
#                 'sleep_hours',
#                 'screen_on_time',
#                 'notifications',
#                 'addiction_score',
#                 'digital_wellness_score'
#             ],
#
#             n_neighbors=5
#         )
#     ),
#
#
#     (
#         'categorical_encoder',
#
#         MultiColumnLabelEncoder(
#
#             columns=[
#                 'gender',
#                 'internet_type',
#                 'location_type',
#                 'user_behavior_class'
#             ]
#         )
#     )
#
# ])


import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder


class MedianImputer(BaseEstimator, TransformerMixin):

    def __init__(self, column):

        self.column = column

    def fit(self, X, y=None):

        self.median_value = X[self.column].median()

        return self

    def transform(self, X):

        X = X.copy()

        X[self.column] = X[self.column].fillna(
            self.median_value
        )

        return X


class GroupMedianImputer(BaseEstimator, TransformerMixin):

    def __init__(self, group_col, target_col):

        self.group_col = group_col

        self.target_col = target_col

    def fit(self, X, y=None):

        self.group_medians = (

            X.groupby(self.group_col)[self.target_col]
            .median()
        )

        return self

    def transform(self, X):

        X = X.copy()

        X[self.target_col] = (

            X.groupby(self.group_col)[self.target_col]

            .transform(

                lambda x: x.fillna(
                    self.group_medians[x.name]
                )
            )
        )

        return X


class KNNColumnImputer(BaseEstimator, TransformerMixin):

    def __init__(self, columns, n_neighbors=5):

        self.columns = columns

        self.n_neighbors = n_neighbors

        self.imputer = KNNImputer(
            n_neighbors=n_neighbors
        )

    def fit(self, X, y=None):

        self.imputer.fit(
            X[self.columns]
        )

        return self

    def transform(self, X):

        X = X.copy()

        X[self.columns] = self.imputer.transform(
            X[self.columns]
        )

        return X


class UsageIntensityCreator(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):

        return self

    def transform(self, X):

        X = X.copy()

        X['usage_intensity'] = (

            X['app_usage_time'] *

            X['number_of_apps_installed']
        )

        return X


class MultiColumnLabelEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, columns):

        self.columns = columns

        self.encoders = {}

    def fit(self, X, y=None):

        for col in self.columns:

            le = LabelEncoder()

            le.fit(
                X[col].astype(str)
            )

            self.encoders[col] = le

        return self

    def transform(self, X):

        X = X.copy()

        for col in self.columns:

            X[col] = self.encoders[col].transform(
                X[col].astype(str)
            )

        return X


preprocessing_pipeline = Pipeline([

    (
        'apps_median_imputer',

        MedianImputer(
            column='number_of_apps_installed'
        )
    ),

    (
        'gaming_time_group_imputer',

        GroupMedianImputer(

            group_col='user_behavior_class',

            target_col='gaming_time'
        )
    ),

    (
        'main_knn_imputer',

        KNNColumnImputer(

            columns=[

                'app_usage_time',
                'screen_on_time',
                'social_media_usage',
                'gaming_time',
                'notifications',
                'sleep_hours'
            ],

            n_neighbors=5
        )
    ),

    (
        'usage_intensity_creator',

        UsageIntensityCreator()
    ),

    (
        'categorical_encoder',

        MultiColumnLabelEncoder(

            columns=[

                'gender',
                'internet_type',
                'location_type',
                'user_behavior_class'
            ]
        )
    )

])