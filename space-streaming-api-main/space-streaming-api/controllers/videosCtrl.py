from flask import jsonify
from models import videos

def buscar(busca, pagina): # Chama a função do model e retorna o resultado em json
    resultado = videos.buscar(busca, pagina)

    return jsonify(resultado)
