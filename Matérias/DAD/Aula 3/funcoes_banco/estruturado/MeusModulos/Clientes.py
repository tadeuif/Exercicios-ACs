class ClienteNaoEncontradoException(Exception):
    pass #nao precisa fazer nada nessa classe, ela ja define a excessao nova

clientes_inicial = [
        {'id': 1, 'nome': "Cliente Um", 'email': "1@cliente.com", "saldo": 10},
        {'id': 2, 'nome': "Cliente Dois", 'email': "2@cliente.com", "saldo": 20},
        {'id': 3, 'nome': "Cliente Tres", 'email': "3@cliente.com", "saldo": 30},
        {'id': 4, 'nome': "Cliente Quatro", 'email': "4@cliente.com", "saldo": 40},
        {'id': 5, 'nome': "Cliente Cinco", 'email': "5@cliente.com", "saldo": 50}
    ]
def nro_clientes(clientes):
    return len(clientes)

def excluir_cliente(clientes, id):
    #todos_indices = list(range(len(clientes) - 1))
    todos_indices = list(range(len(clientes)))
    for i in todos_indices:
        if clientes[i]['id'] == id:
            del clientes[i]
            break
    
def pesquisar_cliente(clientes, id):
    todos_indices = list(range(len(clientes)))
    for i in todos_indices:
        if clientes[i]['id'] == id:
            return clientes[i]
    raise ClienteNaoEncontradoException


