#from . import Clientes

class LimiteCreditoExcedidoException(Exception):
    pass #nao precisa fazer nada nessa classe, ela ja define a excessao nova

#crie aqui uma nova excessao LimiteTransferenciaExcedidoException
class LimiteTransferenciaExcedidoException(Exception):
    pass

def pesquisar_cliente(clientes, id):
    todos_indices = list(range(len(clientes)))
    for i in todos_indices:
        if clientes[i]['id'] == id:
            return clientes[i]

def credito(valor, cliente, limite_credito, limite_transferencia):
    cliente['saldo'] = valor + cliente['saldo']

def debito(valor, cliente, limite_credito, limite_transferencia):
    saque_max = cliente['saldo'] + limite_credito
    if valor > saque_max:
        #print("Sem saldo suficiente")
        raise LimiteCreditoExcedidoException
    cliente['saldo'] = cliente['saldo'] - valor

def transferencia(lista_clientes,id_cliente_doador,id_cliente_receptor,valor,limite_credito,limite_transferencia):

    #lista_clientes.pesquisar(lista_clientes, id_cliente_receptor)  
    
    cliente_doador = pesquisar_cliente(lista_clientes, id_cliente_doador)
    cliente_receptor = pesquisar_cliente(lista_clientes, id_cliente_receptor)

    saldo_doador = cliente_doador['saldo'] - valor
    saldo_receptor = cliente_receptor['saldo'] + valor

    todos_indices = list(range(len(lista_clientes)))

    limite_ce = cliente_doador['saldo'] + limite_credito

    if valor > limite_ce or valor > limite_transferencia:
        
        raise LimiteTransferenciaExcedidoException

    else:
        for i in todos_indices:
            if lista_clientes[i]['id'] == id_cliente_doador:
                cliente_doador['saldo'] = saldo_doador
        
        for i in todos_indices:
            if lista_clientes[i]['id'] == id_cliente_receptor:
                cliente_receptor['saldo'] = saldo_receptor

    