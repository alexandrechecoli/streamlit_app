from requests import session
import streamlit as st
import pandas as pd

'''
# Aplicativo de visualização
Selecione um arquivo para começar a visualização. Note que o arquivo pode ser re-selecionado
diversas vezes.
'''


uploaded_file = st.file_uploader("Escolha um arquivo :", key = "file")
if uploaded_file is not None:
    st.session_state["dt"] = pd.read_csv(st.session_state["file"])

if "dt" in st.session_state:
    st.session_state["dt"]

'''
Agora, mostramos todas as colunas como um combobox
'''

if "dt" in st.session_state:
    rdb_disc = st.radio(
        "Qual a sua disciplina favorita na faculdade?",
         [c for c in st.session_state["dt"].columns],
         key = "col")

'''
Agora, criamos um novo dataframe, aplicando o `groupby` na coluna selecionada.
'''

if "dt" in st.session_state:
    st.session_state["dt_grouped"] = st.session_state["dt"].groupby(st.session_state["col"]).sum()
    st.session_state["dt_grouped"]

'''
Finalmente, criamos um gráfico com os valores agrupados no dataframe
'''

if "dt" in st.session_state:
    st.line_chart(st.session_state["dt_grouped"])