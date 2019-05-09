def pega_campos_opcionais(dados, lista_campos):
        valores_campos_opcionais = {}
        for chave in dados:
            if chave in lista_campos:
                valores_campos_opcionais[chave] = dados[chave]
        return valores_campos_opcionais
