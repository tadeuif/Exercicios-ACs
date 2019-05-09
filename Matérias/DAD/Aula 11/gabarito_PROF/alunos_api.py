from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
alunos_app = Blueprint('alunos_app', __name__, template_folder='templates')
from services.alunos_service import (
    listar as service_listar, 
    localizar as service_localizar, 
    criar as service_criar, 
    remover as service_remover, 
    atualizar as service_atualizar,
    AlunoJaExiste)

campos = ["id", "nome"]
tipos = {"id": int, "nome": str}

@alunos_app.route('/alunos', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@alunos_app.route('/alunos/<int:id>', methods=['GET'])
def localizar(id):
    aluno = service_localizar(id)
    if aluno != None:
        return jsonify(to_dict(aluno))
    return jsonify({'erro':'aluno nao encontrado'}), 404


@alunos_app.route('/alunos', methods=['POST'])
def criar():
    dados = request.json
    if not validar_campos(dados, campos, tipos):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    try:
        criado = service_criar(dados['id'],dados['nome'])
        return jsonify(to_dict(criado))
    except AlunoJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409

@alunos_app.route('/alunos/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return jsonify({'erro':'aluno nao encontrado'}), 404

@alunos_app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    index = 0
    if not validar_campos(dados, campos, tipos):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    try:
        atualizado = service_atualizar(id, dados['id'], dados['nome'])
    except AlunoJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return jsonify({'erro':'aluno nao encontrado'}), 404
