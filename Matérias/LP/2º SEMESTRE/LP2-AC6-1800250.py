'''
════════════════════════════════════════════════════════════════════════════════
 Instituição:  Faculdade Impacta Tecnologia
 Curso      :  Análise e Desenvolvimento de Sistemas
 Disciplina :  Linguagem de Programação 2
 Turma      :  2A (manhã)
 Professor  :  Lucio Nunes de Lira
 Aluno      :  Tadeu Inocencio Freitas  
 Matrícula  :  1800250 
 Entrega    :  29/09/2018
════════════════════════════════════════════════════════════════════════════════
 Programa   :  AC6 (tratamento de exceções)
════════════════════════════════════════════════════════════════════════════════
'''

'''
────────────────────────────────────────────────────────────────────────────────
Com base na aula de 26/09/2018, faça o que se pede a seguir:

1) Insira uma asserção no ínicio do código interno da função menor() que verifi-
   que se o índice i (índice inicial do vetor) é menor ou igual ao índice f (ín-
   dice final do vetor);
2) Coloque o código interno da função menor() dentro de um bloco try;
3) Crie dentro da função menor() os except específicos que cubram as exceções
   geradas pelos testes e, ao final, um except genérico.

ATENÇÃO: (a) Os códigos deste arquivo não deverão ser apagados, suas instruções
         devem ser colocadas e adaptadas ao código já existente.
         (b) Para executar os testes não é necessário usar o pytest, basta
         chamar as funções e verificar os erros que ocorrerão para colocá-los
         nos except.
────────────────────────────────────────────────────────────────────────────────
'''

def menor(lista, i, f):
    try:
        assert ([i] <= [f]), "Índice inicial menor que índice final"
        m = lista[i]
        for j in range(i+1, f+1):
            if lista[j] < m:
                m = lista[j]       
        return m
         
    except SyntaxError:
        print("Código com erro de sintaxe")
    except IndexError:
        print("Lista fora de alcance, por favor, insira um novo índice f - 1")
    except TypeError:
        print("Utilizar somente os tipos de dados corretos")
    except AssertionError:
        print("Índice inicial precisa ser menor do que o índice final")
    except Exception:
        print("Erros precisam ser tratados")

def test_menor_1():
    lista = [30,10,20,40,50]
    assert menor(lista, 0, len(lista)-1) == 10

def test_menor_2():
    lista = [30,10,20,40,50]
    assert menor(lista, 3, 4) == 40

def test_menor_3(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,50]
    menor(lista, 0, 5) == 20

def test_menor_4(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,'A']
    menor(lista, 0, 4) == 20

def test_menor_5(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,5]
    menor(lista, 4, 1) == 5
