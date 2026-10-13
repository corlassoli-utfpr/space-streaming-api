import mysql.connector
from flask import g
import os # Permite acessar variáveis com os dados que usaremos na conexão
from getpass import getpass # Permite inputs de dados sensíveis

senha = getpass("Digite a senha do MySQL: ") # Recebe a senha uma vez ao iniciar o módulo e armazena

def get_connection():
    if "db" not in g:
        g.db = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "root"),
            password=senha,
            database="space_streaming"
        )

    return g.db

def close_connection(exception=None):
    conexao = g.pop("db", None)

    if conexao is not None:
        conexao.close()