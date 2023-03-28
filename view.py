import streamlit as st
import pandas as pd
import model1, model2
import pre_process

def view_model1():

    st.title("다중선형회귀 vs 다항선형회귀")
    tab1, tab2 = st.tabs(["LinearRegression", "Polynomial Regression"])
    df = pre_process.load_data(1)
    with tab1:
            st.header("LinearRegression")
            model1.linear_model()
    with tab2:
            st.header("Polynomial Regression")
            st.write("## 전처리 후 데이터의 모습")
            model1.poly_model(df)


def view_model2():
    st.title("회사퇴사 예측 모델")
    tab1, tab2, tab3 = st.tabs(["RandomForest", "XGBoost", 'LightGBM'])
    df = pre_process.load_data(2)
    with tab1:
            st.header("RandomForest")
            model2.random_forest_model(df)
    with tab2:
            st.header("XGBoost")
            model2.xgBoost_model(df)
    with tab3:
            st.header("LightGBM")
            model2.lightGBM_model(df)
            