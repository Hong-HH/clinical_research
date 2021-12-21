import streamlit as st
import numpy as np
import pandas as pd
from eda_app import run_eda_app

def main() :
    menu = ['홈', '데이터분석']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == '홈' :
        st.title('임상연구 DB 분석')
        st.markdown('### 질병관리청에서 제공한 데이터를 바탕으로 임상연구 데이터 분석, 기준날짜 2017년6월20일')
        df = pd.read_csv('data/research.csv')
        st.dataframe(df)

    elif choice == '데이터분석' :
        run_eda_app()
    

if __name__ == '__main__' :
    main()