from flask import jsonify
from models import empresas
from models import lancamentos

def buscar(busca, pagina):
    resultado = empresas.buscar(busca, pagina)
    
    return jsonify(resultado)

def pagina(id):
    empresa = empresas.buscar_por_id(id)

    if empresa is None:
        return jsonify({"erro": "Empresa não encontrada"}), 404

    lancamentos_empresa = lancamentos.buscar_por_empresa(id)

    empresa["lancamentos"] = lancamentos_empresa

    return jsonify(empresa)
