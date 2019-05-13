
from flask import Flask, jsonify, request
from alunos_api import alunos_app, alunos_db
from professores_api import professores_app


database = {
        "ALUNOS": alunos_db,
}

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)

from services.professores_service import resetar as reseta_professores
@app.route('/reseta', methods=['POST'])
def reseta():
    database['ALUNOS'].clear()
    reseta_professores()
    return 'resetado'

from services.professores_service import listar as listar_professores
@app.route('/')
def all():
    database = {
        "ALUNOS": alunos_db,
        "PROFESSORES": listar_professores()
    }
    return jsonify(database)


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)


