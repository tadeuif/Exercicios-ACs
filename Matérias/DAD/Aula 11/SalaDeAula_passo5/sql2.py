import sqlite3
from wrap_connection import transact

def make_connection():
    connection = sqlite3.connect("lms.db")
    return connection

create_sql = """
CREATE TABLE IF NOT EXISTS Professor (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
)
"""

#esse @transact automatizou os passos 1,2 e 5.
#Só falta o passo 3, executar a query
#E o 4, fazer o commit
@transact(make_connection)
def criar_db():
    cursor.execute(create_sql)
    connection.commit()

criar_db()

#esse @transact automatizou os passos 1,2 e 5.
#Só falta o passo 3, executar a query
#E o 4, fazer o commit
sql_criar = "INSERT INTO Professor (id, nome) VALUES (?, ?)"
@transact(make_connection)
def criar(prof_id,nome):
    cursor.execute(sql_criar, (prof_id, nome))
    connection.commit()

try:
    criar(1,'lucas')
    criar(2,'victor')
    criar(3,'emilio')
    criar(4,'outro_professor')
except sqlite3.IntegrityError as e:
    print('o sql está reclamando que os usuários ja foram criados')

sql_localizar = "SELECT id, nome FROM Professor WHERE id = ?"
@transact(make_connection)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    x = cursor.fetchone()            #l1
    if x == None:                    #l2 
        return None                  #l3 
    return {'id':x[0],'nome':x[1]}   #l4
#Fizemos um select. O cursor.fetchone retorna uma tupla
#com um resultado. 
#Se não tiver nenhum resultado, retorna None

#Assim, nas linhas l1 até l4, estamos pegando
#um resultado. Se for None (l2), nao achamos o professor (l3)
#Se achamos, retornamos

#o resultado é uma tupla (id,nome). Por exemplo, (2,'marcos').
#Assim, x[0] é a id do resultado, x[1] é o nome

print(localizar(1))

sql_deletar = "DELETE FROM Professor WHERE id = ?"
@transact(make_connection)
def deletar(id_professor):
    cursor.execute(sql_deletar, (id_professor,))
    connection.commit()

#deletar(4)


sql_todos = "SELECT id, nome FROM Professor"
@transact(make_connection)
def imprime_todos():
    cursor.execute(sql_todos)
    x = cursor.fetchone()             #l1
    while x != None:                  #l2
       print({'id':x[0],'nome':x[1]}) #l3
       x = cursor.fetchone()          #l4
#Fizemos um select. O cursor.fetchone retorna uma tupla
#com um resultado. Se eu chamar de novo,
# retorna a proxima tupla
#Se não tiver nenhum resultado/acabarem os resultados, retorna None

#Assim, nas linhas l1 até l4, estamos pegando
#os resultados. Pega o primeiro (l1)
#Se for None (l2), nao tem nada pra fazer
#Se achamos, retornamos imprimimos (l3) e tentamos pegar mais um (l4)
#E ai verificamos novamente se x já é None (ou seja
#se já terminou a query) na linha l1


imprime_todos()

@transact(make_connection)
def testar_transact(id_pr):
    print(cursor)
    print(connection)
#Esse @transact faz 4 coisas:
#1.roda o make_connection para criar uma conexao
#2.coloca a conexao na variavel connection
#3.coloca um cursor na variavel cursor
#4.depois de executar a funcao localizar, faz o connection.close()

@transact(make_connection)
def imprime_todos2():
    cursor.execute(sql_todos)
    x = cursor.fetchmany(3)
    while x != []:
       print(x)
       x = cursor.fetchmany(200)

@transact(make_connection)
def imprime_description():
    cursor.execute(sql_todos)
    print(cursor.description)
    print(cursor.description[0][0])
    print(cursor.description[1][0])
