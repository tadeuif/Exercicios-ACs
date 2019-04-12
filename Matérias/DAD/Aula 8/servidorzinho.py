from flask import Flask, request, jsonify 
#from flask import *

app = Flask(__name__) 

database={}
database['ALUNO']=[]
database['PROFESSOR']=[]

@app.route("/") 
def all():
        return jsonify(database)

@app.route('/alunos', methods=['GET'])
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores', methods=['GET'])
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/alunos', methods=['POST'])
def cria_aluno():
    dici = request.json
    lenght_alunos = len(database['ALUNO'])
    for aluno in range(lenght_alunos):
        if dici['id'] == database['ALUNO'][aluno]['id']:
            dic_erro = {'erro': 'id ja utilizada'}
            return jsonify(dic_erro), 400
    if 'nome' not in dici:  #TESTE008 DANDO PAL!
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
    return jsonify(reset_aluno, reset_prof)

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    lenght_alunos = len(database['ALUNO'])
    for aluno in range(lenght_alunos):
        if database['ALUNO'][aluno]['id'] == id_aluno:
            del database['ALUNO'][aluno]
            return 'ID aluno deletado: {}'.format(id_aluno)
    dic_erro = {'erro': 'aluno nao encontrado'}
    return jsonify(dic_erro), 400

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def edita_aluno(id_aluno):
    dici = request.json
    lenght_alunos = len(database['ALUNO'])
    for aluno in range(lenght_alunos):
        if database['ALUNO'][aluno]['id'] == id_aluno:
            novo_nome = request.json['nome']
            database['ALUNO'][aluno]['nome'] = novo_nome
            return 'ID aluno alterado: {}'.format(id_aluno)
        if 'nome' not in dici:  #TESTE008 DANDO PAL!
            dic_erro = {'erro': 'aluno sem nome'}
            return jsonify(dic_erro), 400
    dic_erro = {'erro': 'aluno nao encontrado'}
    return jsonify(dic_erro), 400
    
if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True) 
