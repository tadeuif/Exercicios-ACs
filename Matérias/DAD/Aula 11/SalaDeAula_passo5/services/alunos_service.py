from model.aluno import Aluno

alunos_db = []

def resetar():
    alunos_db.clear()

def listar():
    return alunos_db

def localizar(id):
    for x in alunos_db:
        if x.id == id:
            return x
    return None

def criar(id,nome):
    criado = Aluno(id, nome)
    alunos_db.append(criado)
    return criado

def remover(id):
    index = 0
    for x in alunos_db:
        if x.id == id:
            del alunos_db[index]
            return x
        index += 1
    return None

def atualizar(id_antigo, id_novo, nome):
    index = 0
    for x in alunos_db:
        if x.id == id_antigo:
            x.atualizar(id_novo,nome)
            return x
        index += 1
    return None