def validar_campos(objeto, campos_obrigatorios, tipos, campos_opcionais = []):
    if type(objeto) != dict:
        return False

    for chave in objeto:
        if chave not in campos_obrigatorios+campos_opcionais:
            return False

    for chave in campos_obrigatorios:
        if chave not in objeto:
            return False

    for item in objeto:
        if type(objeto[item]) != tipos[item]:
            return False

    return True
