import streamlit as st
import pandas as pd
import data_preprocess_score, data_preprocess_attrition, visualization_process_score, visualization_process_attrition, models
import pre_process
import decision_tree

def view_model1():
    st.title("다중선형회귀 vs 다항선형회귀(Lasso)")
    tab1, tab2, tab3 = st.tabs(["성적 예측","데이터셋 지표분석","시각화"])
    df = pre_process.load_data(1)
    with tab1:
            st.header("성적 예측 모델")
            models.linear_model()
    with tab2:
            st.header("원본 데이터")
            st.write(df)
            st.header("데이터셋 통계자료 ")
            processed_df = pre_process.s_pre_processing(df)
            visualization_process_score.describe_linear_model(df)
            st.header("데이터셋 Drop & One-Hot Enconding")
            st.write(processed_df)
            st.header("Min-Max Scaling")
            data_frame2 = data_preprocess_score.linear_process(df)
            s_df, comparison, data_frame1 = data_preprocess_score.poly_model(df)
            data_preprocess_score.draw_table(data_frame1, data_frame2 )
    with tab3:
            st.header("시각화")
            visualization_process_score.visualization(df, s_df, comparison)



def view_model2():
    st.title("회사퇴사 예측 모델")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["RandomForest", "XGBoost", 'LightGBM','데이터셋', '결정트리 시각화'])
    df = pre_process.load_data(2)
    with tab1:
            # RandomForest Model
            models.random_forest_model(df)
    with tab2:
            # XGBoost Model
            models.xgBoost_model(df)
    with tab3:
            # LightGBM Model
            models.lightGBM_model(df)
    with tab4:
            st.header("원본 데이터")
            st.write(df)
            st.header("데이터셋 통계자료 ")
            visualization_process_attrition.describe_attrition_model(df)
            df1 = pre_process.a_pre_processing(df)
            st.header("데이터셋 Drop & One-Hot Enconding")
            X,y = data_preprocess_attrition.make_dummies(df1)
            st.write(X)
            st.header("모델별 지표 분석")
    with tab5:
            df = pre_process.load_data(2)
            decision_tree.decision_tree_preprocessing(df)
            data_preprocess_attrition.create_table()

            