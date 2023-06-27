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
engine = create_engine(f'postgresql+pg8000://postgres:0895@/crime_punicao?unix_sock=/cloudsql/thematic-cursor-390616:southamerica-east1:crimepunicao-aoc/.s.PGSQL.5432')

# Consulta ao banco de dados para obter os dados da tabela "Amazoncrim"
query = "SELECT * FROM amazoncrim2019"
df = pd.read_sql_query(query, engine)

# Fechar a conexão com o banco de dados
engine.dispose()

# Crie uma conexão com o banco de dados usando SQLAlchemy
create_engine('postgresql+pg8000://[db_username]:[db_password]@/[db_name]?unix_sock=/cloudsql/[connection_name]/.s.PGSQL.5432')

# Consulta ao banco de dados para obter os dados da tabela "Amazoncrim"
query = "SELECT * FROM amazoncrim2019"
df = pd.read_sql_query(query, engine)

# Fechar a conexão com o banco de dados
engine.dispose()

# Configurar a página do Streamlit
st.title('Amazoncrim - Dados sobre a violência na Amazônia')
st.write('Dados sobre a violência em todos os municípios da Amazônia Legal em 2019:')

# Exibir a tabela de dados
st.dataframe(df)
