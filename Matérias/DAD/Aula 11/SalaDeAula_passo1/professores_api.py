from infra.validacao import validar_campos
from flask import Blueprint, jsonify, request
professores_app = Blueprint('professores_app', __name__, template_folder='templates')
professores_db = []
from services.professores_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    resetar as service_resetar


@professores_app.route('/professores', methods=['GET'])
def listar():
    return jsonify(service_listar())

@professores_app.route('/professores/<int:id>', methods=['GET'])
def localizar(id):
    professor = service_localizar(id)
    if professor != None:
        return jsonify(professor), 404

@professores_app.route('/professores', methods=['POST'])
def criar():
    dados = request.get_json()
    campos = ["id", "nome"]
    tipos = {"id":int, "nome": str}
    if not validar_campos(dados, campos, tipos):
        return jsonify({'erro':'campo inválido'}), 422
    
    lista_profs = service_criar(dados)
    return jsonify(lista_profs)

@professores_app.route('/professores/<int:id>', methods=['DELETE'])
def remover(id):
    index = 0
    for professor in professores_db:
        if professor['id'] == id:
            del professores_db[index]
            return jsonify(professor)
        index += 1
    return jsonify({'erro':'professor nao encontrado'}), 404

@professores_app.route('/professores/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    index = 0
    campos = ["id", "nome"]
    tipos = {"id":int, "nome": str}

    if validar_campos(dados, campos, tipos) == False:
        return jsonify({'erro':'campo inválido'}), 422
    for professor in professores_db:
        if professor['id'] == id:
            professor['id'] = dados['id']
            professor['nome'] = dados['nome']
            return jsonify(professor)
        index += 1
    return jsonify({'erro':'professor nao encontrado'}), 404

@professores_app.route('/professores/reseta', methods=['POST'])
def reseta():
    return jsonify(service_resetar())
