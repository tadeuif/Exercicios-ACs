from model.ofertada import Ofertada
from infra.log import Log
from services.professores_service import localizar as localizar_professor

ofertadas_db = []

class OfertadaJaExiste(Exception):
    pass

class ProfessorNaoExiste(Exception):
    pass

def resetar():
    ofertadas_db.clear()

def listar():
    return ofertadas_db

def localizar(id):
    for x in ofertadas_db:
        if x.id == id:
            return x
    return None

def criar(id, ano, semestre, turma, data, valores_campos_adicionais):
    if localizar(id) != None:
        raise OfertadaJaExiste

    id_coordenador, id_disciplina, id_curso, id_professor = preparar_campos_opcionais(valores_campos_adicionais)

    if id_professor != None and localizar_professor(id_professor) == None:
        raise ProfessorNaoExiste

    log = Log(None)
    criado = Ofertada(id, ano, semestre, turma, data, id_coordenador, id_disciplina, id_curso, id_professor)
    ofertadas_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    ofertadas_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, ano, semestre, turma, data, valores_campos_adicionais):
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise OfertadaJaExiste()

    id_coordenador, id_disciplina, id_curso, id_professor = preparar_campos_opcionais(valores_campos_adicionais)

    if id_professor != None and localizar_professor(id_professor) == None:
        raise ProfessorNaoExiste

    existente = localizar(id_antigo)
    if existente == None:
        return None
    log = Log(existente)
    existente.atualizar(id_novo, ano, semestre, turma, data, id_coordenador, id_disciplina, id_curso, id_professor)
    log.finalizar(existente)
    return existente

def preparar_campos_opcionais(campos_opcionais):
    id_coordenador, id_disciplina, id_curso, id_professor = None, None, None, None

    if 'id_coordenador' in campos_opcionais:
        id_coordenador = campos_opcionais['id_coordenador']
    else:
        id_coordenador = None

    if 'id_disciplina' in campos_opcionais:
        id_disciplina = campos_opcionais['id_disciplina']
    else:
        id_disciplina = None

    if 'id_curso' in campos_opcionais:
        id_curso = campos_opcionais['id_curso']
    else:
        id_curso = None
    
    if 'id_professor' in campos_opcionais:
        id_professor = campos_opcionais['id_professor']
    else:
        id_professor = None

    return id_coordenador, id_disciplina, id_curso, id_professor
