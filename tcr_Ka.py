import numpy as np
import pandas as pd
import streamlit as st
import openpyxl as pyxl
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **Análise exploratória**
## Aplicativo para análise exploratória dos dados da internação em UTI de pacientes com COVID-19
Programado em ***Python*** + ***Streamlit***
---
''')

# Upload CSV data
with st.sidebar.header('1. Faça o upload da planilha (.xlsx)'):
    uploaded_file = st.sidebar.file_uploader("Upload da planilha excel", type=["xlsx"])

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_xlsx():
        a = pd.read_excel(uploaded_file)
        return a
    df = load_xlsx()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Aguardando por planilha xlsx')
    if st.button('Pressione para utilizar planilha demonstrativa'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)