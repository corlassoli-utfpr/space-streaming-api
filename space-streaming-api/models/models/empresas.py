from database.conn import connect

def buscar(busca):
    conexao = connect()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, nome, descricao
        FROM empresas
        WHERE nome LIKE %s
        ORDER BY id
    """, ("%" + busca + "%",))

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado

def buscar_por_id(id):
    conexao = connect()
    cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

    # Busca uma empresa pelo seu ID
    cursor.execute("""
        SELECT id, nome, descricao
        FROM empresas
        WHERE id = %s
    """, (id,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado
