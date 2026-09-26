import mysql.connector
import os # Permite acessar variáveis do ambiente com os dados usados na conexão
from getpass import getpass # Permite realizar input de dados sensíveis


def connect():
    senha = getpass("Digite a senha do MySQL: ")

    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"), # Root por padrão
        password=senha,
        database="space_streaming" # Acesso ao banco que usaremos
    )