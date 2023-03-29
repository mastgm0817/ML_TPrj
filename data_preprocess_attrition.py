import streamlit as st
import seaborn as sns
import pandas as pd
import joblib
import plotly.express as px
from PIL import Image
from math import sqrt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
import pre_process

def make_dummies(df):
    X = pd.get_dummies(df, columns=['Gender'], drop_first=True)
    X = X.drop('Attrition', axis=1)
    y = df['Attrition'].apply(lambda x : 1 if x == "Yes" else 0)
    return X,y

def split_dataset_score(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=20)
    return X_train, X_test, y_train, y_test
def random_forest_score(X_train, X_test, y_train, y_test):

    model = RandomForestClassifier(n_estimators=15, random_state=42)
    model.fit(X_train, y_train)
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, test_pred) # 실제 값, 예측 값 # MAE
    rmse = mean_squared_error(y_test, test_pred, squared=False) # RMSE
    r2 = r2_score(y_test, y_pred)
    # 정확도를 계산하여 모델의 성능을 평가합니다.
    accuracy = accuracy_score(y_test, test_pred)


    index = ["RandomForest"]
    total_info = {"Intercept": intercept, "MAE" : mae,"RMSE": rmse, "R2" : r2, "정확도": accuracy}
    total_df = pd.DataFrame([total_info], index=index)