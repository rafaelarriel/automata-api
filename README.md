# Automata API (en)

API for handling and simulating automata, including:
- Deterministic Finite Automaton (DFA)
- Pushdown Automaton (PDA)
- Turing Machine (TM)

## 🚀 Technologies Used

- **Python 3.13+**
- **FastAPI** (Web Framework)
- **SQLAlchemy** (ORM for database management)
- **Alembic** (Database migrations)
- **Uvicorn** (ASGI Server)
- **Pydantic** (Data validation)
- **Graphviz / PyGraphviz** (Automata visualization)

## 📦 Installation

### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/rafaelarriel/automata-api.git
cd automata-api
```

### 2️⃣ **Create a virtual environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ **Install dependencies**
```bash
pip install fastapi sqlalchemy alembic uvicorn pydantic psycopg2 automata-lib python-dotenv
pip install graphviz pygraphviz coloraide
```

## 🛠️ Database Configuration

- Create the database, preferably named `automata_db`:

 ```bash
CREATE DATABASE automata_db;
```
- Modify the database connection URL `DATABASE_URL` in the `.env` file.
- By default, the connection URL is set for PostgreSQL with the database name `automata_db`.

### **1️⃣ Create database tables**

```bash
alembic upgrade head
```

## ▶️ Running the Project

```bash
uvicorn main:app --reload
```

## 🧪 Running Tests

```bash
pytest
```

## 📡 Available Endpoints

Access the interactive API documentation via:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 Project Structure

```
automata-api/
│-- controllers/          # Routes organized by automaton type
│-- models/               # SQLAlchemy models
│-- schemas/              # Pydantic schemas
│-- database.py           # Database configuration
│-- alembic.ini           # Alembic configuration
│-- main.py               # FastAPI initialization
│-- alembic/              # Database version control
│-- README.md             # Project documentation
│-- use_examples/         # Usage examples and API testing
```

## 🔧 Troubleshooting

### **Error installing `pygraphviz`**
If `pygraphviz` fails to install, try installing the system dependencies:

#### Ubuntu/Debian:
```bash
sudo apt-get install graphviz graphviz-dev
pip install pygraphviz
```

#### Windows:
Download and install [Graphviz](https://graphviz.gitlab.io/download/), and add it to the `PATH`.

#### macOS:
```bash
brew install graphviz
pip install pygraphviz
```

# Automata API (pt-BR)

API para manipulação e simulação de autômatos, incluindo:
- Autômato Finito Determinístico (DFA)
- Autômato com Pilha (PDA)
- Máquina de Turing (TM)

## 🚀 Tecnologias Utilizadas

- **Python 3.13+**
- **FastAPI** (Framework Web)
- **SQLAlchemy** (ORM para banco de dados)
- **Alembic** (Migrações do banco)
- **Uvicorn** (Servidor ASGI)
- **Pydantic** (Validação de dados)
- **Graphviz / PyGraphviz** (Visualização de autômatos)

## 📦 Instalação

### 1️⃣ **Clone o repositório**
```bash
git clone https://github.com/rafaelarriel/automata-api.git
cd automata-api
```

### 2️⃣ **Criação de ambiente virtual (Recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ **Instalar dependências**
```bash
pip install fastapi sqlalchemy alembic uvicorn pydantic graphviz pygraphviz coloraide python-dotenv
```

## 🛠️ Configuração do Banco de Dados

- Crie o banco de dados de preferencia com o nome de automata_db

 ```bash
CREATE DATABASE automata_db;
```
- Modifique a url de conexão do banco DATABASE_URL, no arquivo .env
- Por padrão está uma url de conexão com o PostgreSQL, com o banco criado com o nome de automata_db 

### **1️⃣ Criar as tabelas no banco**

```bash
alembic upgrade head
```

## ▶️ Executando o Projeto

```bash
uvicorn main:app --reload
```

## 🧪 Executando Testes

```bash
pytest
```

## 📡 Endpoints Disponíveis

Acesse a documentação interativa da API via:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 Estrutura do Projeto

```
automata-api/
│-- controllers/          # Rotas organizadas por tipo de autômato
│-- models/               # Modelos SQLAlchemy
│-- schemas/              # Schemas Pydantic
│-- database.py           # Configuração do banco de dados
│-- alembic.ini           # Configuração do Alembic
│-- main.py               # Inicialização do FastAPI
│-- alembic/              # Controle de versões do banco
│-- README.md             # Documentação do projeto
│-- use_examples/         # Exemplos de como usar/ testar a API
```

## 🔧 Solução de Problemas

### **Erro ao instalar `pygraphviz`**
Se `pygraphviz` falhar na instalação, tente instalar as dependências do sistema:

#### Ubuntu/Debian:
```bash
sudo apt-get install graphviz graphviz-dev
pip install pygraphviz
```

#### Windows:
Baixe e instale [Graphviz](https://graphviz.gitlab.io/download/), e adicione ao `PATH`.

#### macOS:
```bash
brew install graphviz
pip install pygraphviz
```
