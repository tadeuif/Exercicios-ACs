def ler_arquivo(nome_do_arquivo, i):
    with open(nome_do_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    linha = linhas[i]
    peca = linha.replace('\n','').split(',')

    return tuple([int(x) for x in peca])

def len_arquivo(nome_do_arquivo):
    with open(nome_do_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    return len(linhas)