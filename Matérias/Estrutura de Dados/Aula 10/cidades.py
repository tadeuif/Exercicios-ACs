import pandas as pd
import json

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

#print(cidades_por_estado(cidades))

lista_alfa = [chr(ord('A')+i) for i in range(26)]

def cidades_por_letra(cidades):
    d = {}
    for i in lista_alfa:
        lista_cidades = []
        for cidade in cidades:
            if cidade[0] == i:
                lista_cidades.append(cidade)
                d[i] = lista_cidades
    return d

#print(cidades_por_letra(cidades))

def estado_por_cidade(cidades):
    d = {}
    for cidade, estado in zip(cidades, estados):
        if cidade not in d:
            d[cidade] = estado
    return d

#print(estado_por_cidade(cidades))

def arvore_do_brasil(cidades):
    brasil = {}
    for cidade, estado in zip(cidades, estados):
        if estado in brasil:
            brasil[estado].update({cidade: None})
        elif estado not in brasil:
            brasil.update({estado: {cidade: None}}) 
    d = {'Brasil': brasil}    
    return d

#print(arvore_do_brasil(cidades))

brasa = arvore_do_brasil(cidades)
cid = cidades_por_estado(cidades)
cid_letra = cidades_por_letra(cidades)
estado_cid = estado_por_cidade(cidades)
data = {}
data['test'] = 'test'
#json_dicto = json.loads(json_file)
#print(json_file['GO'])
#json_dict = json.dumps(data)

#print(json_dict)

with open('teste.json', 'w') as json_file:
  json.dump(brasa, json_file)