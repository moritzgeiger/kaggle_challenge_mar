## DF AND VISUALIZATION
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

## ML TOOLS
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn import set_config
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_curve
from joblib import dump, load

## INTERNAL
from binance_strategies.data import feat_drop, uniques

## Importing the test set from kaggle

class Predictor:
    def __init__(self, df):
        self.X_test = pd.read_csv(df)

    def preproc_test_data(self):
        # defining cat and cont features
        # col_cat = list(self.X_test.select_dtypes(exclude=['float64', 'int64']).columns)
        # col_num = list(self.X_test.select_dtypes(include=['float64', 'int64']).columns)

        X_test_p = self.X_test.drop(columns=feat_drop).set_index("id")

        for k, v in uniques.items():
            # replacing with 'other' if val not in training set
            X_test_p[k].apply(lambda x: x if x in v else "other")

        # using preprocessor from notebook
        preprocessor = load('binance_strategies/preprocessor.joblib')
        X_test_p = preprocessor.transform(X_test_p)

        return X_test_p
    
    def predict(self):
        model_forest = load('binance_strategies/model_forest.joblib')
        test_data = self.preproc_test_data()
        y_pred_test = pd.DataFrame(model_forest.predict(test_data), index=self.X_test.id).rename(columns={0:"target"})
        
        return y_pred_test






