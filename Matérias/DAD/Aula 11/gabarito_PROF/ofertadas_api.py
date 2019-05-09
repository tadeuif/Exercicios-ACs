from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.pega_campos_opcionais import pega_campos_opcionais
from infra.to_dict import to_dict, to_dict_list
ofertadas_app = Blueprint('ofertadas_app', __name__, template_folder='templates')
from services.ofertadas_service import (
    listar as service_listar, 
    localizar as service_localizar, 
    criar as service_criar, 
    remover as service_remover, 
    atualizar as service_atualizar,
    OfertadaJaExiste,
    ProfessorNaoExiste)

campos_obrigatorios = ['id', 'ano', 'semestre', 'turma', 'data']
campos_opcionais = ['id_coordenador','id_disciplina','id_curso','id_professor']
tipos = {'id': int, 'ano': int, 'semestre': int, 'turma': str, 'data': str, 'id_coordenador': int, 'id_disciplina': int, 'id_curso': int, 'id_professor': int}

@ofertadas_app.route('/ofertadas', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@ofertadas_app.route('/ofertadas/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return jsonify({'erro':'ofertada nao encontrada'}), 404

@ofertadas_app.route('/ofertadas', methods=['POST'])
def criar():
    dados = request.json
    if not validar_campos(dados, campos_obrigatorios, tipos, campos_opcionais):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    valores_campos_opcionais = pega_campos_opcionais(dados,campos_opcionais)
    try:
        criado = service_criar(dados['id'], dados['ano'], dados['semestre'], dados['turma'], dados['data'], valores_campos_opcionais)
        return jsonify(to_dict(criado))
    except OfertadaJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409
    except ProfessorNaoExiste:
        return jsonify({'erro':'professor nao existe'}), 400

@ofertadas_app.route('/ofertadas/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return jsonify({'erro':'ofertada nao encontrada'}), 404

@ofertadas_app.route('/ofertadas/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    if not validar_campos(dados, campos_obrigatorios, tipos, campos_opcionais):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    valores_campos_opcionais = pega_campos_opcionais(dados,campos_opcionais)
    try:
        atualizado = service_atualizar(id, dados['id'], dados['ano'], dados['semestre'], dados['turma'], dados['data'], valores_campos_opcionais)
    except OfertadaJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return jsonify({'erro':'ofertada nao encontrada'}), 404
