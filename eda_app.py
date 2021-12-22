import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import wordcloud


def run_eda_app() :
    data_menu = ['개요', '임상시험 단계별']
    select_data = st.sidebar.selectbox('세부 메뉴', data_menu)
    df = pd.read_csv('data/research.csv')
    test_level = df.groupby('임상시험단계')['임상시험단계'].count()
    test_level.index = ['Phase0', 'Phase1', 'Phase1/Phase2', 'Phase2', 'Phase2/Phase3','Phase3', 'Phase4', 'Not applicable']
    
    st.title('데이터 분석')

    if select_data == '개요' :
        st.subheader('사이드바에서 세부 메뉴를 선택해주세요')
        st.dataframe(df)
        st.subheader('임상시험 단계별 분포')
        
        fig1 = plt.figure()
        test_level.plot.bar()
        plt.xticks(rotation=90)
        st.pyplot(fig1)     

    elif select_data == '임상시험 단계별' :
        level_menu = ['임상시험 단계','Phase0', 'Phase1', 'Phase1/Phase2', 'Phase2', 'Phase2/Phase3','Phase3', 'Phase4', 'Not applicable']
        
        level_choice = st.sidebar.radio('선택', level_menu)

        st.subheader('임상시험 단계별 데이터 분석')

        if level_choice == '임상시험 단계' :
            st.subheader('임상시험의 단계')
            st.text('1. 비임상시험 : 사람을 대상으로 하기전 실시하는 임상실험 주로 실험동물에게 실시')
            st.text('2. 임상시험 : 1상 ~4상의 임상시험 사람을 대상으로 함, 실험 대상의 상태와 목적이 다름')
            
            #파이 차트
            fig2 = plt.figure()
            plt.pie(test_level,autopct='%1.1f%%', labels= test_level.index, startangle=90, wedgeprops={'width': 0.7 }, pctdistance= 0.83)
            plt.legend(loc='upper left', bbox_to_anchor=(1.04, 1.06))
            st.pyplot(fig2)

            #카운트 플롯
            fig1 = plt.figure()
            test_level.plot.bar()
            plt.xticks(rotation=90)
            st.pyplot(fig1) 
        elif level_choice == 'Phase0' :
            df_p0 = df.loc[df['임상시험단계']=='Phase0',]
            st.text('{} 행의 데이터가 있습니다.'.format(df_p0.shape[0]))
            st.dataframe(df_p0)
        elif level_choice == 'Phase1' :
            df_p1 = df.loc[df['임상시험단계']=='Phase1',]
            st.text('{} 행의 데이터가 있습니다.'.format(df_p1.shape[0]))
            st.dataframe(df_p1)

        elif level_choice == 'Phase1/Phase2' :
            df_p12 = df.loc[df['임상시험단계']=='Phase1/Phase2',]
            st.text('{} 행의 데이터가 있습니다.'.format(df_p12.shape[0]))
            st.dataframe(df_p12)

        elif level_choice == 'Phase2' :
            df_p2 = df.loc[df['임상시험단계']=='Phase2',]
            st.text('{} 행의 데이터가 있습니다.'.format(df_p2.shape[0]))
            st.dataframe(df_p2)
        
        elif level_choice == 'Phase2/Phase3' :
            df_p23 = df.loc[df['임상시험단계']=='Phase2/Phase3',]
            st.text('{} 행의 데이터가 있습니다.'.format(df_p23.shape[0]))
            st.dataframe(df_p23)

        elif level_choice == 'Phase3' :
            df_p3 = df.loc[df['임상시험단계']=='Phase3',]
            st.text('{} 행의 데이터가 있습니다.'.format(df_p3.shape[0]))
            st.dataframe(df_p3)
        elif level_choice == 'Phase4' :
            df_p4 = df.loc[df['임상시험단계']=='Phase4',]
            st.text('{} 행의 데이터가 있습니다.'.format(df_p4.shape[0]))
            st.dataframe(df_p4)
        elif level_choice == 'Not applicable' :
            df_pN = df.loc[df['임상시험단계']=='해당사항없음(Not applicable)',]
            st.text('{} 행의 데이터가 있습니다.'.format(df_pN.shape[0]))
            st.dataframe(df_pN)




        




    
    