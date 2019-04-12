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

#na url /alunos
#com verbo post
@app.route('/alunos', methods=['POST'])
def cria_aluno():
    #vou receber um dicionario via json
    dici = request.json
    #e colocar na lista
    database['ALUNO'].append(dici)
    return jsonify(database['ALUNO'])

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
        for aluno in database['ALUNO']:
            if aluno['id'] == id_aluno:
                return jsonify(aluno)
        return 'não achei', 404
                
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
    return 'Não encontrado', 404

if __name__ == '__main__':
            app.run(host='localhost', port=5002, debug=True) 
