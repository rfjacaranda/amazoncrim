import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Obtenha os segredos do Streamlit
db_username = st.secrets["db_username"]
db_password = st.secrets["db_password"]
db_name = st.secrets["db_name"]
connection_name = st.secrets["connection_name"]

# Crie uma conexão com o banco de dados usando SQLAlchemy
engine = create_engine(f'postgresql://{db_username}:{db_password}@/{db_name}?host=/cloudsql/{connection_name}')

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
