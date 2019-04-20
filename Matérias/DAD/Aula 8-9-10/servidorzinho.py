'''
Tadeu Inocencio Freitas - RA 1800250
Tibério Cruz - RA 1800110

'''
from flask import Flask, request, jsonify 
#from flask import *

app = Flask(__name__) 

database={}
database['ALUNO']=[]
database['PROFESSOR']=[]
database['DISCIPLINA']=[]
database['OFERTADAS']=[]

@app.route("/") 
def all():
        return jsonify(database)

@app.route('/alunos', methods=['GET'])
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores', methods=['GET'])
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/disciplinas',methods=['GET'])
def disciplina():
    return jsonify(database['DISCIPLINA'])

@app.route('/ofertadas',methods=['GET'])
def ofertadas():
    return jsonify(database['OFERTADAS'])

@app.route('/alunos', methods=['POST'])
def cria_aluno():
    dici = request.json
    lenght_alunos = len(database['ALUNO'])
    for aluno in range(lenght_alunos):
        if dici['id'] == database['ALUNO'][aluno]['id']:
            dic_erro = {'erro': 'id ja utilizada'}
            return jsonify(dic_erro), 400
    if 'nome' not in dici: 
        dic_erro = {'erro': 'aluno sem nome'}
        return jsonify(dic_erro), 400
    database['ALUNO'].append(dici)
    return jsonify(database['ALUNO'])

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
        for aluno in database['ALUNO']:
            if aluno['id'] == id_aluno:
                return jsonify(aluno)
        dic_erro = {'erro': 'aluno nao encontrado'}
        return jsonify(dic_erro), 400
                
@app.route('/reseta', methods=['POST'])
def reseta_lista():
    reset_aluno = database['ALUNO']=[]
    reset_prof = database['PROFESSOR']=[]
    reset_disci = database['DISCIPLINA']=[]
    reset_ofertadas = database['OFERTADAS']=[]
    return jsonify(reset_aluno, reset_prof, reset_disci, reset_ofertadas)

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    lenght_alunos = len(database['ALUNO'])
    for aluno in range(lenght_alunos):
        if database['ALUNO'][aluno]['id'] == id_aluno:
            del database['ALUNO'][aluno]
            return 'ID aluno deletado: {}'.format(id_aluno)
    dic_erro = {'erro': 'aluno nao encontrado'}
    return jsonify(dic_erro), 400

@app.route('/alunos/<int:id_recebido>', methods=['PUT'])
def edita_aluno(id_recebido):
    dici = request.json
    lenght_alunos = len(database['ALUNO'])
    for aluno in range(lenght_alunos):
        if 'nome' not in dici:
            dic_erro = {'erro': 'aluno sem nome'}
            return jsonify(dic_erro), 400

        elif database['ALUNO'][aluno]['id'] == id_recebido:
            novo_nome = dici['nome']
            database['ALUNO'][aluno]['nome'] = novo_nome
            return 'ID aluno alterado: {}'.format(id_recebido)
    
    dic_erro = {'erro': 'aluno nao encontrado'}
    return jsonify(dic_erro), 400
#PROFESSOR
@app.route("/professores",methods=['POST'])
def adiciona_prof():
    dici=request.json
    tamanho=len(database['PROFESSOR'])
    for id_busca in range(tamanho):
        if dici['id'] == database['PROFESSOR'][id_busca]['id']:
            dic_erro = {'erro': 'id ja utilizada'}
            return jsonify(dic_erro), 400
    if 'nome' not in dici:
        dic_erro = {'erro': 'professor sem nome'}
        return jsonify(dic_erro), 400
    database['PROFESSOR'].append(dici)
    return jsonify(database['PROFESSOR'])

@app.route("/professores/<int:id_recebido>",methods=['GET'])
def consulta_prof_por_id(id_recebido):
    for id_busca in database['PROFESSOR']:
        if id_busca['id'] == id_recebido:
            return jsonify(id_busca)
    dic_erro = {'erro': 'professor nao encontrado'}
    return jsonify(dic_erro), 400

@app.route("/professores/<int:id_recebido>",methods=['DELETE'])
def deleta_prof(id_recebido):
    tamanho=len(database['PROFESSOR'])
    for id_busca in range(tamanho):
        if database['PROFESSOR'][id_busca]['id'] == id_recebido:
            del database['PROFESSOR'][id_busca]
            return jsonify(database['PROFESSOR'])
    dic_erro = {'erro': 'professor nao encontrado'}
    return jsonify(dic_erro), 400

@app.route('/professores/<int:id_recebido>', methods=['PUT'])
def edita_prof(id_recebido):
    dici = request.json
    lenght_alunos = len(database['PROFESSOR'])
    for aluno in range(lenght_alunos):
        if 'nome' not in dici:
            dic_erro = {'erro': 'professor sem nome'}
            return jsonify(dic_erro), 400

        elif database['PROFESSOR'][aluno]['id'] == id_recebido:
            novo_nome = dici['nome']
            database['PROFESSOR'][aluno]['nome'] = novo_nome
            return 'ID professor alterado: {}'.format(id_recebido)
    
    dic_erro = {'erro': 'professor nao encontrado'}
    return jsonify(dic_erro), 400
#DISCIPLINA
@app.route("/disciplinas",methods=['POST'])
def adiciona_disciplina():
    dici=request.json
    tamanho=len(database['DISCIPLINA'])
    lista_campos = ["carga_horaria","id","nome","plano_ensino","status"]
    tamanho_lista_campos = len(lista_campos)
    for campos in range(tamanho_lista_campos):
        if lista_campos[campos] not in dici:
            dic_erro = {'erro': 'campo não encontrado'}
            return jsonify(dic_erro), 400

    for id_busca in range(tamanho):
        if dici['id'] == database['DISCIPLINA'][id_busca]['id']:
            dic_erro = {'erro': 'id ja utilizada'}
            return jsonify(dic_erro), 400
    if 'nome' not in dici:
        dic_erro = {'erro': 'Disciplina sem nome'}
        return jsonify(dic_erro), 400
    database['DISCIPLINA'].append(dici)
    return jsonify(database['DISCIPLINA'])

@app.route("/disciplinas/<int:id_recebido>",methods=['GET'])
def consulta_disci_por_id(id_recebido):
    for id_busca in database['DISCIPLINA']:
        if id_busca['id'] == id_recebido:
            return jsonify(id_busca)
    dic_erro = {'erro': 'disciplina nao encontrada'}
    return jsonify(dic_erro), 400

@app.route("/disciplinas/<int:id_recebido>",methods=['DELETE'])
def deleta_disc(id_recebido):
    tamanho=len(database['DISCIPLINA'])
    for id_busca in range(tamanho):
        if database['DISCIPLINA'][id_busca]['id'] == id_recebido:
            del database['DISCIPLINA'][id_busca]
            return jsonify(database['DISCIPLINA'])
    dic_erro = {'erro': 'disciplina nao encontrada'}
    return jsonify(dic_erro), 400

@app.route('/disciplinas/<int:id_recebido>', methods=['PUT'])
def edita_disc(id_recebido):
    dici = request.json
    lenght_disc = len(database['DISCIPLINA'])
    for disciplina in range(lenght_disc):
        if 'nome' not in dici:
            dic_erro = {'erro': 'disciplina sem nome'}
            return jsonify(dic_erro), 400

        elif database['DISCIPLINA'][disciplina]['id'] == id_recebido:
            novo_nome = dici['nome']
            database['DISCIPLINA'][disciplina]['nome'] = novo_nome
            return 'ID disciplina alterado: {}'.format(id_recebido)
    
    dic_erro = {'erro': 'disciplina nao encontrada'}
    return jsonify(dic_erro), 400
#OFERTADAS
@app.route("/ofertadas",methods=['POST'])
def adiciona_ofertadas():
    dici=request.json
    tamanho=len(database['OFERTADAS'])
    lista_campos = ["ano","id","turma","semestre","data","id_professor"]
    tamanho_lista_campos = len(lista_campos)
    for campos in range(tamanho_lista_campos):
        if lista_campos[campos] == "id_professor":
            if 'id_professor' in dici:
                professor_id = dici['id_professor']
                tamanho_prof = len(database['PROFESSOR'])
                for prof in range(tamanho_prof):
                    profs = professores()
                    id_prof_a_procurar = profs[prof]['id']
                    if professor_id not in id_prof_a_procurar:
                        dic_erro_prof = {'erro': 'Professor não cadastrado'}
                        return jsonify(dic_erro_prof), 400
            if 'id_professor' not in dici:
                pass #Prof não adicionado
        elif lista_campos[campos] not in dici:
            dic_erro = {'erro': '{} faltando'.format(lista_campos[campos])}
            return jsonify(dic_erro), 400

    for id_busca in range(tamanho):
        if dici['id'] == database['OFERTADAS'][id_busca]['id']:
            dic_erro = {'erro': 'id ja utilizada'}
            return jsonify(dic_erro), 400
    '''if 'nome' not in dici:
        dic_erro = {'erro': 'Disciplina sem nome'}
        return jsonify(dic_erro), 400'''
    database['OFERTADAS'].append(dici)
    return jsonify(database['OFERTADAS'])

@app.route("/ofertadas/<int:id_recebido>",methods=['GET'])
def consulta_disci_por_id_ofertadas(id_recebido):
    for id_busca in database['OFERTADAS']:
        if id_busca['id'] == id_recebido:
            return jsonify(id_busca)
    dic_erro = {'erro': 'ofertada nao encontrada'}
    return jsonify(dic_erro), 400

@app.route("/ofertadas/<int:id_recebido>",methods=['DELETE'])
def deleta_disc_ofertadas(id_recebido):
    tamanho=len(database['OFERTADAS'])
    for id_busca in range(tamanho):
        if database['OFERTADAS'][id_busca]['id'] == id_recebido:
            del database['OFERTADAS'][id_busca]
            return jsonify(database['OFERTADAS'])
    dic_erro = {'erro': 'ofertada nao encontrada'}
    return jsonify(dic_erro), 400

@app.route('/ofertadas/<int:id_recebido>', methods=['PUT'])
def edita_disc_ofertadas(id_recebido):
    dici = request.json
    lenght_ofertadas = len(database['OFERTADAS'])
    campos_ofertadas = ["id", "ano", "semestre", "turma", "data"]
    tamanho_ofertadas = len(campos_ofertadas)
    for i in range(lenght_ofertadas):
        for items in range(tamanho_ofertadas):
            if campos_ofertadas[items] not in dici:
                pass
            elif campos_ofertadas[items] in dici:
                novo_item = dici[campos_ofertadas[items]]
                database['OFERTADAS'][i][campos_ofertadas[items]] = novo_item
                return 'ID OFERTADAS alterado: {}'.format(id_recebido)
    
    dic_erro = {'erro': 'ofertada nao encontrada'}
    return jsonify(dic_erro), 400
    
if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True) 
