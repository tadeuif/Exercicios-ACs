from Clientes import *

class LimiteCreditoExcedidoException(Exception):
    pass #nao precisa fazer nada nessa classe, ela ja define a excessao nova

#crie aqui uma nova excessao LimiteTransferenciaExcedidoException
class LimiteTransferenciaExcedidoException(Exception):
    pass

def credito(valor, cliente, limite_credito, limite_transferencia):
    cliente['saldo'] = valor + cliente['saldo']

def debito(valor, cliente, limite_credito, limite_transferencia):
    saque_max = cliente['saldo'] + limite_credito
    if valor > saque_max:
        #print("Sem saldo suficiente")
        raise LimiteCreditoExcedidoException
    cliente['saldo'] = cliente['saldo'] - valor

def transferencia(lista_clientes,id_cliente_doador,id_cliente_receptor,valor,limite_credito,limite_transferencia):
    saldo_doador = id_cliente_doador['saldo'] - valor
    saldo_receptor = id_cliente_receptor['saldo'] + valor

    cliente_doador = lista_clientes.pesquisar(lista_clientes, id_cliente_doador)                #lista_clientes[id_cliente_doador]
    cliente_receptor = lista_clientes.pesquisar(lista_clientes, id_cliente_receptor)                                                                   #lista_clientes[id_cliente_receptor]
    
    todos_indices = list(range(len(lista_clientes)))

    for i in todos_indices:
       if cliente_doador == lista_clientes[i]:
           cliente_doador['saldo'] = saldo_doador
    
    for i in todos_indices:
       if cliente_receptor == lista_clientes[i]:
           cliente_receptor['saldo'] = saldo_receptor