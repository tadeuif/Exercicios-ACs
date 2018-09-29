'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 2                                  ║
║ Turma         :  2A (manhã)                                                  ║
║ Professor     :  Lucio Nunes de Lira                                         ║
║ Aluno (1)     :  Tadeu Inocencio Freitas                                     ║
║ Aluno (2)     :                                                              ║
║ Matrícula (1) :  1800250                                                     ║
║ Matrícula (2) :                                                              ║
║ Entrega       :  19/09/2018                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  AC5 (testes automatizados).                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

'''
────────────────────────────────────────────────────────────────────────────────
Com base na aula de 19/09/2018, faça o que se pede a seguir:

Crie uma função que receba como parâmetro um número natural n e devolva o 
termial deste valor.
Obs.: Crie 5 testes automatizados para a função (casos errados e casos corre-
      tos).
────────────────────────────────────────────────────────────────────────────────
'''

def termial (n1):
    x = n1
    for x in range(x, 0, -1):
        n1 += x
        x -= 1
    return n1

print(termial(5))

def test_terminal ():
    assert termial(10) == 2345

def test_terminal2 ():
    assert termial(10) == 98713

def test_terminal3 ():
    assert termial(5) == 20

def test_terminal4 ():
    assert termial(4) == 14

def test_terminal5 ():
    assert termial(3) == 9