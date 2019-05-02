def validar_campos(obj, campos_obrigatorios, tipos):
    if type(obj) != dict:
        return False
    for k in obj:
        if k not in campos_obrigatorios:
            return False
    for k in campos_obrigatorios:
        if k not in obj:
            return False
    for item in obj:
        if type(obj[item]) != tipos[item]:
            return False
    return True
