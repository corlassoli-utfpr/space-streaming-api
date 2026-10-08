from database.conn import connect

def buscar(busca):
    with connect() as conexao:
        cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

        cursor.execute("""
            SELECT id, nome, descricao
            FROM empresas
            WHERE nome LIKE %s
            ORDER BY id
        """, ("%" + busca + "%",)) # Permite busca por substring

        resultado = cursor.fetchall() # Recolhe os resultados

        return resultado

def buscar_por_id(id):
    with connect() as conexao:
        cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

        # Busca uma empresa pelo seu ID
        cursor.execute("""
            SELECT id, nome, descricao
            FROM empresas
            WHERE id = %s
        """, (id,)) # Apenas encontra o valor onde o id corresponde

        resultado = cursor.fetchone() # Como o id é único, retornará apenas um resultado

        return resultado
