
from flask import Flask, jsonify, request
from alunos_api import alunos_app
from professores_api import professores_app
from disciplinas_api import disciplinas_app
from ofertadas_api import ofertadas_app

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)
app.register_blueprint(disciplinas_app)
app.register_blueprint(ofertadas_app)

from services.professores_service import resetar as reseta_professores
from services.alunos_service import resetar as reseta_alunos
from services.disciplinas_service import resetar as reseta_disciplinas
from services.ofertadas_service import resetar as reseta_ofertadas
@app.route('/reseta', methods=['POST'])
def reseta():
    reseta_alunos()
    reseta_professores()
    reseta_disciplinas()
    reseta_ofertadas()
    return 'resetado'

from services.professores_service import listar as listar_professores
from services.alunos_service import listar as listar_alunos
from services.disciplinas_service import listar as listar_disciplinas
from services.ofertadas_service import listar as listar_ofertadas
@app.route('/')
def all():
    database = {
        'ALUNOS': listar_alunos(),
        'PROFESSORES': listar_professores(),
        'DISCIPLINAS': listar_disciplinas(),
        'OFERTADAS': listar_ofertadas()
    }
    return jsonify(database)


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)