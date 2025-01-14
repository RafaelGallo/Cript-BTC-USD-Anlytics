from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Caminho do banco de dados
DATABASE_URL = "sqlite:///c:/Users/rafae/Downloads/Case_cadastra/yahoo_data.db"

# Configuração do engine
engine = create_engine(DATABASE_URL, echo=False)

# Sessão para conexão ao banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)