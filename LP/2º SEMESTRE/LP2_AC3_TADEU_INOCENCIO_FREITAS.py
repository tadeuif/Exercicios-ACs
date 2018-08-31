'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 2                                  ║
║ Turma         :  2A (manhã)                                                  ║
║ Professor     :  Lucio Nunes de Lira                                         ║
║ Aluno         :  Tadeu Inocencio Freitas                                     ║
║ Matrícula     :  RA 1800250                                                  ║
║ Entrega       :  01/09/2018                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  AC3 (Classes, objetos, atributos e métodos)                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

'''
────────────────────────────────────────────────────────────────────────────────
Crie a classe Aluno com os seguintes atributos:
    - Nome      (string)
    - Matrícula (int)
    - Média     (real)
    - Faltas    (int)
e com os seguintes métodos:
    - def __init__(<apenas com o parâmetro self>)
    - def aprovado(<apenas com o parâmetro self>)
      devolve um valor booleano indicando se o aluno
      está aprovado com base na nota e no número de faltas.
    - abona_faltas(<Com o parâmetro self e o número N de faltas abonadas>)
      remove N faltas do aluno (considere que não ficará negativo).
────────────────────────────────────────────────────────────────────────────────
'''

class Aluno:
    def __init__(self):   
        self.nome = "Tadeu Inocencio"
        self.matricula = 1800250
        self.media = float(10)
        self.faltas = 3
    
    def aprovado(self):
        if self.media >= 6 and self.faltas <= 4:
            return True
        else:
            return False

    def abona_faltas(self, N):
        self.faltas -= N
        if self.faltas < 0:
            self.faltas = 0
        else:
            pass
#TESTES

#a)
aluno = Aluno()
#b)
aluno.nome = "Juca Bala"
#c)
print(aluno.aprovado())
#d)
aluno.abona_faltas(1)
print(aluno.faltas)

