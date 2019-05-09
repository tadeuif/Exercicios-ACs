from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.pega_campos_opcionais import pega_campos_opcionais
from infra.to_dict import to_dict, to_dict_list
disciplinas_app = Blueprint('disciplinas_app', __name__, template_folder='templates')
from services.disciplinas_service import (
    listar as service_listar, 
    localizar as service_localizar, 
    criar as service_criar, 
    remover as service_remover, 
    atualizar as service_atualizar,
    DisciplinaJaExiste)

campos_obrigatorios = ['id', 'nome', 'status', 'plano_ensino', 'carga_horaria']
campos_opcionais = ['id_coordenador']
tipos = {'id':int, 'nome': str, 'status': int, 'plano_ensino': str, 'carga_horaria': int, 'id_coordenador': int}


@disciplinas_app.route('/disciplinas', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@disciplinas_app.route('/disciplinas/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return jsonify({'erro':'disciplina nao encontrada'}), 404

@disciplinas_app.route('/disciplinas', methods=['POST'])
def criar():
    dados = request.json
    if not validar_campos(dados, campos_obrigatorios, tipos, campos_opcionais):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    valores_campos_opcionais = pega_campos_opcionais(dados,campos_opcionais)
    try:
        criado = service_criar(dados['id'], dados['nome'], dados['status'], dados['plano_ensino'], dados['carga_horaria'], valores_campos_opcionais)
        return jsonify(to_dict(criado))
    except DisciplinaJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409


@disciplinas_app.route('/disciplinas/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return jsonify({'erro':'disciplina nao encontrada'}), 404

@disciplinas_app.route('/disciplinas/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    if not validar_campos(dados, campos_obrigatorios, tipos):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    valores_campos_opcionais = pega_campos_opcionais(dados,campos_opcionais)
    try:
        atualizado = service_atualizar(id, dados['id'], dados['nome'], dados['status'], dados['plano_ensino'], dados['carga_horaria'], valores_campos_opcionais)
    except DisciplinaJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return jsonify({'erro':'disciplina nao encontrada'}), 404
