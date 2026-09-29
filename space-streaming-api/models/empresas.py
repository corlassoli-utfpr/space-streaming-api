from database.conn import connect


def buscar(busca, pagina):
    conexao = connect()
    cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

    limite = 5 # Total de empresas por página
    offset = (pagina - 1) * limite # Empresas que serão puladas de acordo com a página

    # Busca empresas pelo nome e aplica paginação
    cursor.execute("""
        SELECT id, nome, descricao
        FROM empresas
        WHERE nome LIKE %s
        ORDER BY id
        LIMIT %s OFFSET %s
    """, ("%" + busca + "%", limite, offset))

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