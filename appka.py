import numpy as np
import pandas as pd
import streamlit as st 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# Título do aplicativo
st.markdown('''
# **Análise exploratória TCR: Grau de mobilidade de pacientes com COVID-19
internados em UTI**

Análise realizada em **Python**, utilizando ***streamlit*** e ***pandas***.
''')

# Import excel file
with st.sidebar.header('Faça o upload da versão mais recente do arquivo execel contendo os dodos'):
    uploaded_file = st.sidebar.file_uploader("Upload arquivo excel")


# Pandas profiling report
if uploaded_file is not None:
    @st.cache
    def load_excel():
        xlsx = pd.read_excel(uploaded_file)
        return xlsx
    df = load_excel()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Aguardando o envio da planilha excel')
    if st.button('Pressione para usar dados como exemplo'):
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
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)