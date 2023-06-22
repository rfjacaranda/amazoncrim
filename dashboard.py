#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Crie uma conexão com o banco de dados usando SQLAlchemy
engine = create_engine('postgresql://postgres:0895@localhost:5432/crime_punicao')

# Consulta ao banco de dados para obter os dados da tabela "Amazoncrim"
query = "SELECT * FROM amazoncrim2020"
df = pd.read_sql_query(query, engine)

# Fechar a conexão com o banco de dados
engine.dispose()

# Configurar a página do Streamlit
st.title('Amazoncrim - Dados sobre a violência na Amazônia')
st.write('Dados sobre a violência em todos os municípios da Amazônia Legal em 2020:')

# Exibir a tabela de dados
st.dataframe(df)


# In[ ]:




