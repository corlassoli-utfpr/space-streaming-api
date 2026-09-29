from flask import jsonify
from models import videos

def buscar(busca, pagina):
    resultado = videos.buscar(busca, pagina)

    return jsonify(resultado)
