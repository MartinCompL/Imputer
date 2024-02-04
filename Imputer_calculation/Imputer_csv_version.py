import pandas as pd
import numpy as np

class Strategyfactory:
    def create_imputer(self, strategy, axis=0):
        if strategy == "mean":
            return MeanImputer(axis=axis)
        elif strategy == "median":
            return MedianImputer(axis=axis)
        elif strategy == "mode":
            return ModeImputer(axis=axis)
        else:
            raise ValueError("The imputation strategy is not valid or not implemented")

class HomebrewImputer:
    def __init__(self, Strategyfactory, axis=0):
        self.Strategyfactory = Strategyfactory
        self.axis = axis
        self.imputer = None

    def fit(self, X, rows=None, strategy=""):
        self.imputer = self.Strategyfactory.create_imputer(strategy, axis=self.axis)
        if rows is not None:
            X = X.loc[rows]
        self.imputer.fit(X)

    def transform(self, X):
        if self.imputer is not None:
            return self.imputer.transform(X)

    def set_axis(self, axis):
        self.axis = axis

class MeanImputer:
    def __init__(self, axis=0):
        self.axis = axis

    def fit(self, X):
        self.imputation_values = X.mean(axis=self.axis)

    def transform(self, X):
        return X.fillna(self.imputation_values)

class MedianImputer:
    def __init__(self, axis=0):
        self.axis = axis

    def fit(self, X):
        self.imputation_values = X.median(axis=self.axis)

    def transform(self, X):
        return X.fillna(self.imputation_values)

class ModeImputer:
    def __init__(self, axis=0):
        self.axis = axis

    def fit(self, X):
        self.imputation_values = X.mode(axis=self.axis).iloc[0]

    def transform(self, X):
        return X.fillna(self.imputation_values)

# Read data from CSV file
file_path = "number.csv"  # Replace with the actual path to your CSV file
X = pd.read_csv(file_path)

Strategyfactory = Strategyfactory()
strategy = "median"
imp = [1, 2]
imputer = HomebrewImputer(Strategyfactory, axis=0)
imputer.fit(X, rows=imp, strategy=strategy)
imputed_data = imputer.transform(X)
print("Original Data: \n", X)
print("Imputed Data : \n", imputed_data)
