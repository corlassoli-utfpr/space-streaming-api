from database.conn import get_connection

def buscar(busca):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

    try:
        cursor.execute("""
            SELECT id, nome, descricao
            FROM empresas
            WHERE nome LIKE %s
            ORDER BY id
        """, ("%" + busca + "%",)) # Permite busca por substring

        resultado = cursor.fetchall() # Recolhe os resultados

        return resultado
    finally:
        cursor.close()

def buscar_por_id(id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

    try:
        # Busca uma empresa pelo seu ID
        cursor.execute("""
            SELECT id, nome, descricao
            FROM empresas
            WHERE id = %s
        """, (id,)) # Apenas encontra o valor onde o id corresponde

        resultado = cursor.fetchone() # Como o id é único, retornará apenas um resultado

        return resultado
    finally:
        cursor.close()