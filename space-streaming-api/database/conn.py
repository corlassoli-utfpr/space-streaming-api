import mysql.connector
import os # Permite acessar variáveis com os dados que usaremos na conexão
from getpass import getpass # Permite inputs de dados sensíveis


senha = getpass("Digite a senha do MySQL: ") # Recebe a senha uma vez ao iniciar o módulo e armazena


def connect():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=senha,
        database="space_streaming"
    )


if __name__ == "__main__": # Teste
    conexao = connect()
    print("Conexão realizada com sucesso!")
    conexao.close()