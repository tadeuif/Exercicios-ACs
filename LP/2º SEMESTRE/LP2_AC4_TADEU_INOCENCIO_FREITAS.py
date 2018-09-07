'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 2                                  ║
║ Turma         :  2A (manhã)                                                  ║
║ Professor     :  Lucio Nunes de Lira                                         ║
║ Aluno         :  Tadeu Inocencio Freitas                                     ║
║ Matrícula     :  1800250                                                     ║
║ Entrega       :  07/09/2018                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  AC4 (construtor com parâmetros default, atributos privados, ║
║                  métodos get() e set()).                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

'''
────────────────────────────────────────────────────────────────────────────────
Com base no arquivo criado na AC3, faça o que se pede a seguir:

Faça com que a classe Aluno fique com os seguintes atributos:
    - Nome          (string) - público
    - Matrícula     (int)    - público
    - Nota de AC    (float)  - público
    - Nota de Prova (float)  - público
    - Média         (float)  - privado
    - Faltas        (int)    - privado

Faça com que a classe Aluno fique com os seguintes métodos:
    - def __init__(Parâmetro "self" e parâmetros para todos os atributos
                   definidos, exceto "média", e com "Nota de AC", "Nota de
                   Prova" e "Faltas" com valor default zerado).
                   Obs.: Todos os atributos definidos em __init__ devem ser
                   inicializados com os valores dos parâmetros, exceto a média
                   que será inicializada com a fórmula 60% nota de AC + 40%
                   nota de prova.
    - def aprovado(<apenas com o parâmetro self>)
                   Devolve um valor booleano indicando se o aluno está aprovado
                   com base na média, que deve ser maior ou igual a 6, e
                   faltas, que deve ser menor ou igual a 4.
    - def abona_faltas(<com o parâmetro self e o número N de faltas abonadas>)
                   Reduz as faltas do aluno em N unidades, se for possível.
                   Caso o valor de N seja superior ao número de faltas do aluno,
                   não reduzir e exibir uma mensagem indicando a falha.
    - def get_media(<apenas com o parâmetro self>)
                   Devolve a média do aluno.
    - def get_faltas(<apenas com o parâmetro self>)
                   Devolve o número de faltas do aluno.

Faça os seguintes testes no programa principal:
    a) Crie um objeto aluno passando os dados como parâmetros, exceto os default;
    b) Altere o nome;
    c) Abone um número de faltas;
    d) Exiba a média;
    e) Exiba a quantidade de faltas;
    f) Exiba a situação de aprovação do aluno;
    g) Abone um número de faltas de modo que garanta aprovação;
    h) Altere a nota de AC e a nota de prova de modo que garantam aprovação;
    i) Repita as instruções d), e) e f);
    j) Entenda o que aconteceu, será indagado em aula.
────────────────────────────────────────────────────────────────────────────────
'''

class Aluno:
    def __init__(self, nome = "Tadeu Inocencio", matricula = 1800250, nota_AC=0, nota_prova=0, __faltas=0):   
        if nota_AC != 0:
            self.nota_AC = nota_AC
        if nota_prova != 0:
            self.nota_prova = nota_prova
        self.__media = float((self.nota_AC * 0.6) + (self.nota_prova * 0.4))
        self.__faltas = 0
    
    def aprovado(self):
        if self.__media >= 6 and self.__faltas <= 4:
            return True
        else:
            return False

    def abona_faltas(self, N):
        if N > self.__faltas:
            print("Faltas abonadas maior do que o número de faltas")
            print("Faltas não abonadas, por favor utilize um número N <= número de faltas")
        else:  
            self.__faltas -= N
            if self.__faltas < 0:
                self.__faltas = 0
            else:
                pass

    def get_media(self):
        return self.__media

    def get_faltas(self):
        return self.__faltas

    def set_faltas(self, N):
        self.__faltas = N
        return self.__faltas

    def set_media(self, N1, N2):
        self.nota_AC = N1
        self.nota_prova = N2
        self.__media = float((self.nota_AC * 0.6) + (self.nota_prova * 0.4))
        return self.__media

#TESTES

#a)
aluno = Aluno("Tadeu Inocencio",1800250, 4, 3, 5)
#b)
aluno.nome = "Mike Wazalski"
#c)
aluno.set_faltas(6)
aluno.abona_faltas(1)
#d)
print(aluno.get_media())
#e)
print(aluno.get_faltas())
#f)
print(aluno.aprovado())
#g)
aluno.set_faltas(6)
aluno.abona_faltas(2)
print(aluno.get_faltas())
print(aluno.aprovado())
#h)
#Método set criado para alterar a média, pois self.__media é privado
aluno.set_media(8,9)
#i)
    #d)
print(aluno.get_media())
    #e)
print(aluno.get_faltas())
    #f)
print(aluno.aprovado())