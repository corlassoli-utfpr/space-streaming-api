from database.conn import connect


def buscar(busca, pagina):
    conexao = connect()
    cursor = conexao.cursor(dictionary=True) # Retorna em formato de dicionário

    limite = 5 # Total de vídeos por página
    offset = (pagina - 1) * limite # Total de vídeos que serão 'pulados' de acordo com o número da página

    # Recebe as informações do vídeo e realiza JOIN para identificar o lançamento e a empresa relacionados.
    cursor.execute("""
        SELECT
            v.id,
            v.titulo,
            v.youtube_id,
            v.url,
            v.thumbnail,
            v.duracao,
            l.id AS lancamento_id,
            l.nome AS lancamento,
            e.id AS empresa_id,
            e.nome AS empresa
        FROM videos v
        JOIN lancamentos l ON v.lancamento_id = l.id
        JOIN empresas e ON l.empresa_id = e.id
        WHERE v.titulo LIKE %s
        ORDER BY v.id
        LIMIT %s OFFSET %s
    """, ("%" + busca + "%", limite, offset))

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado