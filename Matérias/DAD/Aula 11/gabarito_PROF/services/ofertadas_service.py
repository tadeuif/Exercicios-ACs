from model.ofertada import Ofertada
from infra.log import Log
from services.professores_service import localizar as localizar_professor
from wrap_connection import transact
import sqlite3

ofertadas_db = []

class OfertadaJaExiste(Exception):
    pass

class ProfessorNaoExiste(Exception):
    pass

def make_connection():
    connection = sqlite3.connect("lms.db")
    return connection
create_table = """
CREATE TABLE IF NOT EXISTS Ofertadas (
    id INTEGER PRIMARY KEY,
    ano INTEGER NOT NULL,
    semestre INTEGER NOT NULL,
    turma TEXT NOT NULL,
    data TEXT NOT NULL,
    id_coordenador INTEGER,
    id_disciplina INTEGER, 
    id_curso INTEGER, 
    id_professor INTEGER
)
"""

@transact(make_connection)
def criar_db():
    print('criando tabela ofertadas')
    cursor.execute(create_table)
    connection.commit()
criar_db()

sql_resetar = 'delete from Ofertadas'
@transact(make_connection)
def resetar():
    cursor.execute(sql_resetar)
    connection.commit()

sql_all = 'SELECT * from Ofertadas'
@transact(make_connection)
def listar():
    resposta = []
    cursor.execute(sql_all)
    a = cursor.fetchone()
    while a != None:
        resposta.append(Ofertada(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]))
        a = cursor.fetchone()
    return resposta

sql_localizar = '''
SELECT * FROM Ofertadas WHERE id = ?
'''
@transact(make_connection)
def localizar(id):
    cursor.execute(sql_localizar,(id,))
    a = cursor.fetchone()
    if a  == None:
        return None
    d = Ofertada(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])
    return d

#parei aqui
sql_create='''INSERT INTO Ofertadas
    (id,
    ano,
    semestre,
    turma,
    data,
    id_coordenador,
    id_disciplina,
    id_curso,
    id_professor) VALUES (?,?,?,?,?,?,?,?,?)
'''
@transact(make_connection)
def criar(id, ano, semestre, turma, data, valor_coordenador="", valor_disciplina="", valor_curso="", valor_professor=""):
    if localizar(id) != None:
        raise OfertadaJaExiste

    id_coordenador = preparar_campos_opcionais(valor_coordenador)
    id_disciplina = preparar_campos_opcionais(valor_disciplina)
    id_curso = preparar_campos_opcionais(valor_curso)
    id_professor = preparar_campos_opcionais(valor_professor)

    log = Log(None)
    criado = Ofertada(id, ano, semestre, turma, data, valor_coordenador, valor_disciplina, valor_curso, valor_professor)
    cursor.execute(sql_create,(id, ano, semestre, turma, data, id_coordenador, id_disciplina, id_curso, id_professor))
    connection.commit()
    log.finalizar(criado)
    return criado

sql_remover = 'delete from Ofertadas where id = ?'
@transact(make_connection)
def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    #disciplinas_db.remove(existente)
    cursor.execute(sql_remover,(id,))
    connection.commit()
    log.finalizar(None)
    return existente

sql_atualizar = '''
UPDATE Ofertadas SET
    id = ?,
    nome = ?,
    status = ?,
    plano_ensino = ?,
    carga_horaria = ?,
    id_coordenador = ?
WHERE id = ?
'''
@transact(make_connection)
def atualizar(id_antigo, id_novo, ano, semestre, turma, data, valor_coordenador, valor_disciplina, valor_curso, valor_professor):
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise OfertadaJaExiste()

    id_coordenador = preparar_campos_opcionais(valor_coordenador)
    id_disciplina = preparar_campos_opcionais(valor_disciplina)
    id_curso = preparar_campos_opcionais(valor_curso)
    id_professor = preparar_campos_opcionais(valor_professor)

    if id_professor != None and localizar_professor(id_professor) == None:
        raise ProfessorNaoExiste
    existente = localizar(id_antigo)
    if existente == None:
        return None
    log = Log(existente)
    existente.atualizar(id_novo, ano, semestre, turma, data, valor_coordenador, valor_disciplina, valor_curso, valor_professor)
    cursor.execute(sql_atualizar,(id_novo, ano, semestre, turma, data, valor_coordenador, valor_disciplina, valor_curso, valor_professor, id_antigo))
    connection.commit()
    log.finalizar(existente)
    return existente

def preparar_campos_opcionais(campos_opcionais):

    if 'id_coordenador' in campos_opcionais:
        id_coordenador = campos_opcionais['id_coordenador']
    else:
        id_coordenador = ""

    if 'id_disciplina' in campos_opcionais:
        id_disciplina = campos_opcionais['id_disciplina']
    else:
        id_disciplina = ""

    if 'id_curso' in campos_opcionais:
        id_curso = campos_opcionais['id_curso']
    else:
        id_curso = ""
    
    if 'id_professor' in campos_opcionais:
        id_professor = campos_opcionais['id_professor']
    else:
        id_professor = ""

    return id_coordenador, id_disciplina, id_curso, id_professor
