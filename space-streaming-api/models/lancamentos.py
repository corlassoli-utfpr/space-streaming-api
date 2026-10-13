from database.conn import get_connection

def buscar_por_empresa(empresa_id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

    try:
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

        return resultado
    finally:
        cursor.close()