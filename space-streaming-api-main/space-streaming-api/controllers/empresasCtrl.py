from flask import jsonify
from models import empresas
from models import lancamentos

def buscar(busca): # Chama a função de buscar a empresa por string do model e retorna o resultado em json
    resultado = empresas.buscar(busca)

    return jsonify(resultado)

def pagina(id): # Chama a funçaõ buscar_por_id e utiliza o id providenciado, retornando em json
    empresa = empresas.buscar_por_id(id)

    if empresa is None: # Caso não exista empresa com o id fornecido
        return jsonify({"erro": "Empresa não encontrada"}), 404

    lancamentos_empresa = lancamentos.buscar_por_empresa(id)

    empresa["lancamentos"] = lancamentos_empresa

    return jsonify(empresa)
