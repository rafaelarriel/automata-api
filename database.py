import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# URL de conexão com o PostgreSQL
SQLALCHEMY_DATABASE_URL =  os.getenv("DATABASE_URL")

# Cria a engine do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()