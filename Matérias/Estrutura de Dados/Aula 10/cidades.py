'''
Tadeu Inocencio Freitas - RA 1800250
Tibério Cruz - RA 1800110

'''

import pandas as pd
import json

data = pd.read_csv("cidades_br.csv")

cidades = data['Nome do Município'].tolist()
estados = data['UF'].tolist()

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

estados_organizados = organizar_estados(estados)
def cidades_por_estado(cidades):
    d = {}
    for cidade, estado in zip(cidades, estados):
        if estado not in d:
            d[estado] = [cidade]
        elif estado in d:
            d[estado] += [cidade]
    return d

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

def estado_por_cidade(cidades):
    d = {}
    for cidade, estado in zip(cidades, estados):
        if cidade not in d:
            d[cidade] = estado
    return d

def arvore_do_brasil(cidades):
    brasil = {}
    for cidade, estado in zip(cidades, estados):
        if estado in brasil:
            brasil[estado].update({cidade: None})
        elif estado not in brasil:
            brasil.update({estado: {cidade: None}}) 
    d = {'Brasil': brasil}    
    return d

brasa = arvore_do_brasil(cidades)
cid = cidades_por_estado(cidades)
cid_letra = cidades_por_letra(cidades)
estado_cid = estado_por_cidade(cidades)

with open('teste.json', 'w') as json_file:
  json.dump(brasa, json_file)