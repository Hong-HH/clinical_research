import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import wordcloud


def run_eda_app() :
    df = pd.read_csv('data/research.csv')
    st.dataframe(df)