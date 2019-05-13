from model.professor import Professor

professores_db = []

def resetar():
    professores_db.clear()

def listar():
    return professores_db

def localizar(id):
    for x in professores_db:
        if x.id == id:
            return x
    return None

def criar(id,nome):
    criado = Professor(id, nome)
    professores_db.append(criado)
    return criado

def remover(id):
    index = 0
    for x in professores_db:
        if x.id == id:
            del professores_db[index]
            return x
        index += 1
    return None

def atualizar(id_antigo, id_novo, nome):
    index = 0
    for x in professores_db:
        if x.id == id_antigo:
            x.atualizar(id_novo,nome)
            return x
        index += 1
    return None

