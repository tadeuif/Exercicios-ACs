from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
professores_app = Blueprint('professores_app', __name__, template_folder='templates')
from services.professores_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    resetar as service_resetar
from services.alunos_service import resetar as reseta_alunos



campos = ["id", "nome"]
tipos = {"id":int, "nome": str}


@professores_app.route('/professores', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@professores_app.route('/professores/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return jsonify({'erro':'professor nao encontrado'}), 404

@professores_app.route('/professores', methods=['POST'])
def criar():
    dados = request.json
    if not validar_campos(dados, campos, tipos):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    x = service_localizar(dados['id'])
    if x != None:
            erro = {'erro': 'id ja utilizada'}
            return jsonify(erro),400
    criado = service_criar(dados['id'],dados['nome'])
    return jsonify(to_dict(criado))

@professores_app.route('/professores/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return jsonify({'erro':'professor nao encontrado'}), 404

@professores_app.route('/professores/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    index = 0
    if not validar_campos(dados, campos, tipos):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    atualizado = service_atualizar(id, dados['id'], dados['nome'])
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return jsonify({'erro':'professor nao encontrado'}), 404

@professores_app.route('/reseta', methods=['POST'])
def resetar():
    limpa_lista1 = service_resetar()
    limpa_lista2 = reseta_alunos()
    return jsonify('aaa')