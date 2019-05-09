from model.professor import Professor
from infra.log import Log
from wrap_connection import transact
import sqlite3

professores_db = []

class ProfessorJaExiste(Exception):
    pass

def make_connection():
    connection = sqlite3.connect("lms.db")
    return connection
create_table = """
CREATE TABLE IF NOT EXISTS Professores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
)
"""

@transact(make_connection)
def criar_db():
    print('criando tabela professor')
    cursor.execute(create_table)
    connection.commit()
criar_db()

sql_resetar = 'delete from Professores'
@transact(make_connection)
def resetar():
    cursor.execute(sql_resetar)
    connection.commit()

sql_all = 'SELECT * from Professores'
@transact(make_connection)
def listar():
    resposta = []
    cursor.execute(sql_all)
    a = cursor.fetchone()
    while a != None:
        resposta.append(Professor(a[0],a[1]))
        a = cursor.fetchone()
    return resposta

sql_localizar = '''
SELECT * FROM Professores WHERE id = ?
'''
@transact(make_connection)
def localizar(id):
    cursor.execute(sql_localizar,(id,))
    a = cursor.fetchone()
    if a  == None:
        return None
    d = Professor(a[0],a[1])
    return d

sql_create='''INSERT INTO Professores(id,nome) VALUES (?,?)'''
@transact(make_connection)
def criar(id, nome):
    if localizar(id) != None:
        raise ProfessorJaExiste

    log = Log(None)
    criado = Professor(id, nome)
    cursor.execute(sql_create,(id, nome))
    connection.commit()
    log.finalizar(criado)
    return criado

sql_remover = 'delete from Professores where id = ?'
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
UPDATE Professores SET
    id = ?,
    nome = ?
WHERE id = ?
'''
@transact(make_connection)
def atualizar(id_antigo, id_novo, nome):
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise ProfessorJaExiste()
    existente = localizar(id_antigo)
    if existente == None:
        return None
    log = Log(existente)
    existente.atualizar(id_novo, nome)
    cursor.execute(sql_atualizar,(id_novo, nome, id_antigo))
    connection.commit()
    log.finalizar(existente)
    return existente