from flask import jsonify
from models import videos

def buscar_video(busca, pagina):
    resultado = videos.buscar(busca, pagina)

    return jsonify(resultado)