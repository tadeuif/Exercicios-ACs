import pandas as pd

data = pd.read_csv("cidades_br.csv")
cidade = data['Nome do Município']
ind = cidade[1]
#print(data)

muni_cid = data[['Nome do Município', 'Estado']]
#print(muni_cid)

cidades = data['Nome do Município'].tolist()
estados = data['UF'].tolist()


#print(estados)
def organizar_estados(estados):
    tamanho_lista_estados = len(estados)
    lista_UF_n_duplicados = []
    for i in range(tamanho_lista_estados):
        if estados[i] not in lista_UF_n_duplicados:
            estado = estados[i]
            lista_UF_n_duplicados.append(estado)
        else:
            pass
    return lista_UF_n_duplicados

#print(organizar_estados(estados))
estados_organizados = organizar_estados(estados)
def cidades_por_estado(cidades):
    d = {}
    for cidade, estado in zip(cidades, estados):
        if estado not in d:
            d[estado] = [cidade]
        elif estado in d:
            d[estado] += [cidade]
    return d

print(cidades_por_estado(cidades))