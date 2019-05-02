professores_db = []

def listar():
    return professores_db

def localizar(id):
    for x in professores_db:
        if x['id'] == id:
            return x
    return None

def criar(dados):
    professores_db.append(dados)
    return dados

def remover(id):
    index = 0
    for x in professores_db:
        if x['id'] == id:
            del professores_db[index]
            return x
        index += 1
    return None

def atualizar(id, dados):
    index = 0
    for x in professores_db:
        if x['id'] == id:
            x['id'] = dados['id']
            x['nome'] = dados['nome']
            return x
        index += 1
    return None

def resetar():
    professores_db.clear()