from database.conn import connect


def buscar_por_empresa(empresa_id):
    conexao = connect()
    cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

    # Busca os lançamentos relacionados a uma empresa
    cursor.execute("""
        SELECT
            id,
            nome,
            data,
            status,
            foguete,
            missao,
            local,
            descricao
        FROM lancamentos
        WHERE empresa_id = %s
        ORDER BY data DESC
    """, (empresa_id,)) # Todos os lançamentos onde o id da empresa é correspondente

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado