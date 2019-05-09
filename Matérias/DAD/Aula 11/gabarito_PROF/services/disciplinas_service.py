from model.disciplina import Disciplina
from infra.log import Log
from services.professores_service import localizar as localizar_professor
from wrap_connection import transact
import sqlite3

disciplinas_db = []

class DisciplinaJaExiste(Exception):
    pass

class ProfessorCoordenadorNaoExiste(Exception):
    pass

def make_connection():
    connection = sqlite3.connect("lms.db")
    return connection
create_table = """
CREATE TABLE IF NOT EXISTS Disciplinas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    status INTEGER NOT NULL,
    plano_ensino TEXT NOT NULL,
    carga_horaria INTEGER NOT NULL,
    id_coordenador INTEGER
)
"""
@transact(make_connection)
def criar_db():
    print('criando tabela disciplinas')
    cursor.execute(create_table)
    connection.commit()
criar_db()

sql_resetar = 'delete from Disciplinas'
@transact(make_connection)
def resetar():
    cursor.execute(sql_resetar)
    connection.commit()

sql_all = 'SELECT * from Disciplinas'
@transact(make_connection)
def listar():
    resposta = []
    cursor.execute(sql_all)
    a = cursor.fetchone()
    while a != None:
        resposta.append(Disciplina(a[0],a[1],a[2],a[3],a[4],a[5]))
        a = cursor.fetchone()
    return resposta

sql_localizar = '''
SELECT * FROM Disciplinas WHERE id = ?
'''
@transact(make_connection)
def localizar(id):
    cursor.execute(sql_localizar,(id,))
    a = cursor.fetchone()
    if a  == None:
        return None
    d = Disciplina(a[0],a[1],a[2],a[3],a[4],a[5])
    return d

sql_create='''INSERT INTO Disciplinas
    (id,
    nome,
    status,
    plano_ensino,
    carga_horaria,
    id_coordenador) VALUES (?,?,?,?,?,?)
'''
@transact(make_connection)
def criar(id, nome, status, plano_ensino, carga_horaria, valores_campos_adicionais):
    if localizar(id) != None:
        raise DisciplinaJaExiste

    id_coordenador = preparar_campos_opcionais(valores_campos_adicionais)


    log = Log(None)
    criado = Disciplina(id, nome, status, plano_ensino, carga_horaria, valores_campos_adicionais)
    cursor.execute(sql_create,(id, nome, status, plano_ensino, carga_horaria, id_coordenador))
    connection.commit()
    log.finalizar(criado)
    return criado

sql_remover = 'delete from Disciplinas where id = ?'
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
UPDATE Disciplinas SET
    id = ?,
    nome = ?,
    status = ?,
    plano_ensino = ?,
    carga_horaria = ?,
    id_coordenador = ?
WHERE id = ?
'''
@transact(make_connection)
def atualizar(id_antigo, id_novo, nome, status, plano_ensino, carga_horaria, valores_campos_adicionais):
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise DisciplinaJaExiste()
    existente = localizar(id_antigo)
    if existente == None:
        return None
    log = Log(existente)
    id_coordenador = preparar_campos_opcionais(valores_campos_adicionais)
    existente.atualizar(id_novo, nome, status, plano_ensino, carga_horaria, id_coordenador)
    cursor.execute(sql_atualizar,(id_novo, nome, status, plano_ensino, carga_horaria, id_coordenador,id_antigo))
    connection.commit()
    log.finalizar(existente)
    return existente

def preparar_campos_opcionais(campos_opcionais):
    id_coordenador = None
    
    if 'id_coordenador' in campos_opcionais:
        id_coordenador = campos_opcionais['id_coordenador']

    return id_coordenador
