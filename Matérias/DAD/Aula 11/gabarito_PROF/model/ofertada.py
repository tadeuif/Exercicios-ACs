class Ofertada():
    def __init__(self, id, ano, semestre, turma, data, id_coordenador, id_disciplina, id_curso, id_professor):
        self.__id = id
        self.__ano = ano
        self.__semestre = semestre
        self.__turma = turma
        self.__data = data
        self.__id_coordenador = id_coordenador
        self.__id_disciplina = id_disciplina
        self.__id_curso  = id_curso
        self.__id_professor = id_professor
    
    def atualizar(self, id, ano, semestre, turma, data, id_coordenador, id_disciplina, id_curso, id_professor):
        self.__id = id
        self.__ano = ano
        self.__semestre = semestre
        self.__turma = turma
        self.__data = data
        self.__id_coordenador = id_coordenador
        self.__id_disciplina = id_disciplina
        self.__id_curso  = id_curso
        self.__id_professor = id_professor
        return self
    
    @property
    def id(self):
        return self.__id

    @property
    def ano(self):
        return self.__ano

    @property
    def semestre(self):
        return self.__semestre

    @property
    def turma(self):
        return self.__turma

    @property
    def data(self):
        return self.__data

    @property
    def coordenador(self):
        return self.__id_coordenador

    @property
    def disciplina(self):
        return self.__id_disciplina
    
    @property
    def curso(self):
        return self.__id_curso

    @property
    def professor(self):
        return self.__id_professor