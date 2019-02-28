class LimiteCreditoExcedidoException(Exception):
    pass #nao precisa fazer nada nessa classe, ela ja define a excessao nova

#crie aqui uma nova excessao LimiteTransferenciaExcedidoException

def credito(valor, cliente, limite_credito, limite_transferencia):
    pass # crie aqui a funcao credito

def debito(valor, cliente, limite_credito, limite_transferencia):
    pass # crie aqui a funcao debito

def transferencia(lista_clientes,id_cliente_doador,id_cliente_receptor,valor,limite_credito,limite_transferencia):
    pass # crie aqui a funcao transferencia
