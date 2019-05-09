import requests
import unittest
import sqlite3

class TestStringMethods(unittest.TestCase):

    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5002/alunos')
        self.assertEqual(type(r.json()),type([]))

    def test_001_adiciona_alunos(self):
        r = requests.post('http://localhost:5002/alunos',json={'nome':'fernando','id':1})
        r = requests.post('http://localhost:5002/alunos',json={'nome':'roberto','id':2})
        r_lista = requests.get('http://localhost:5002/alunos')
        achei_fernando = False
        achei_roberto = False
        for aluno in r_lista.json():
            if aluno['nome'] == 'fernando':
                achei_fernando = True
            if aluno['nome'] == 'roberto':
                achei_roberto = True
        if not achei_fernando:
            self.fail('aluno fernando nao apareceu na lista de alunos')
        if not achei_roberto:
            self.fail('aluno roberto nao apareceu na lista de alunos')

    def test_002_aluno_por_id(self):
        r = requests.post('http://localhost:5002/alunos',json={'nome':'mario','id':20})
        r_id = requests.get('http://localhost:5002/alunos/20')
        self.assertEqual(r_id.json()['nome'],'mario')


    
    def test_003_adiciona_e_reseta(self):
        r = requests.post('http://localhost:5002/alunos',json={'nome':'cicero','id':29})
        r_lista = requests.get('http://localhost:5002/alunos')
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r_lista_depois = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista_depois.json()),0)

    def test_004_adiciona_e_deleta(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        requests.post('http://localhost:5002/alunos',json={'nome':'cicero','id':29})
        requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':28})
        r_lista = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista.json()),2)
        requests.delete('http://localhost:5002/alunos/28')
        r_lista = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista.json()),1)
    
    def test_005_edita(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':28})
        r_antes = requests.get('http://localhost:5002/alunos/28')
        self.assertEqual(r_antes.json()['nome'],'lucas')
        requests.put('http://localhost:5002/alunos/28', json={'nome':'lucas mendes', 'id':28})
        r_depois = requests.get('http://localhost:5002/alunos/28')
        self.assertEqual(r_depois.json()['nome'],'lucas mendes')

    def test_006_id_inexistente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.put('http://localhost:5002/alunos/15',json={'nome':'bowser','id':15})
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')
        r = requests.get('http://localhost:5002/alunos/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')
        r = requests.delete('http://localhost:5002/alunos/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')

    def test_007_criar_com_id_ja_existente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'bond','id':7})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'james','id':7})
        self.assertIn(r.status_code,[400,409])
        self.assertEqual(r.json()['erro'],'id ja utilizada')

    def test_008_post_ou_put_sem_nome(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'id':8})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro',r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':'maximus','id':7})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5002/alunos/7',json={'id':7})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro',r.json())
    

    def test_100_professores_retorna_lista(self):
        r = requests.get('http://localhost:5002/professores')
        self.assertEqual(type(r.json()),type([]))
    
    def test_100b_nao_confundir_professor_e_aluno(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        r = requests.post('http://localhost:5002/alunos',json={'nome':'fernando','id':1})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'roberto','id':2})
        self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista.json()),0)
        r_lista_alunos = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista_alunos.json()),2)

    def test_101_adiciona_professores(self):
        r = requests.post('http://localhost:5002/professores',json={'nome':'fernando','id':1})
        r = requests.post('http://localhost:5002/professores',json={'nome':'roberto','id':2})
        r_lista = requests.get('http://localhost:5002/professores')
        achei_fernando = False
        achei_roberto = False
        for professor in r_lista.json():
            if professor['nome'] == 'fernando':
                achei_fernando = True
            if professor['nome'] == 'roberto':
                achei_roberto = True
        if not achei_fernando:
            self.fail('professor fernando nao apareceu na lista de professores')
        if not achei_roberto:
            self.fail('professor roberto nao apareceu na lista de professores')

    def test_102_professores_por_id(self):
        r = requests.post('http://localhost:5002/professores',json={'nome':'mario','id':20})
        r_lista = requests.get('http://localhost:5002/professores/20')
        self.assertEqual(r_lista.json()['nome'],'mario')


    
    def test_103_adiciona_e_reseta(self):
        r = requests.post('http://localhost:5002/professores',json={'nome':'cicero','id':29})
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r_lista_depois = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista_depois.json()),0)

    def test_104_adiciona_e_deleta(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        requests.post('http://localhost:5002/professores',json={'nome':'cicero','id':29})
        requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':28})
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista.json()),2)
        requests.delete('http://localhost:5002/professores/28')
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista.json()),1)
    
    def test_105_edita(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':28})
        r_antes = requests.get('http://localhost:5002/professores/28')
        self.assertEqual(r_antes.json()['nome'],'lucas')
        requests.put('http://localhost:5002/professores/28', json={'nome':'lucas mendes', 'id':28})
        r_depois = requests.get('http://localhost:5002/professores/28')
        self.assertEqual(r_depois.json()['nome'],'lucas mendes')

    def test_106_id_inexistente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.put('http://localhost:5002/professores/15',json={'nome':'bowser','id':15})
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'professor nao encontrado')
        r = requests.get('http://localhost:5002/professores/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'professor nao encontrado')
        r = requests.delete('http://localhost:5002/professores/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'professor nao encontrado')

    def test_107_criar_com_id_ja_existente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'bond','id':7})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'james','id':7})
        self.assertIn(r.status_code,[400,409])
        self.assertEqual(r.json()['erro'],'id ja utilizada')

    def test_108_post_ou_put_sem_nome(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'id':8})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro',r.json())
        r = requests.post('http://localhost:5002/professores',json={'nome':'maximus','id':7})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5002/professores/7',json={'id':7})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro',r.json())

    def test_109_nao_confundir_professor_e_aluno(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        r = requests.post('http://localhost:5002/professores',json={'nome':'fernando','id':1})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'roberto','id':2})
        self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista.json()),2)
        r_lista_alunos = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista_alunos.json()),0)
    
    def test_200_disciplinas_retorna_lista(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        r = requests.get('http://localhost:5002/disciplinas')
        self.assertEqual(type(r.json()),type([]))
        self.assertEqual(len(r.json()),0)
    
    def test_200b_nao_confundir_disciplina_e_pessoas(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        r = requests.post('http://localhost:5002/alunos',json={'nome':'fernando','id':1})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'roberto','id':2})
        self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://localhost:5002/disciplinas')
        self.assertEqual(len(r_lista.json()),0)

    def test_201_adiciona_disciplinas(self):
        r = requests.post('http://localhost:5002/disciplinas',json={'id':100,'nome':'estruturas de dados','status':12,'plano_ensino':'dados','carga_horaria':15})
        r = requests.post('http://localhost:5002/disciplinas',json={'id':101,'nome':'distribuidos','status':12,'plano_ensino':'clientes e servidores','carga_horaria':10})
        r_lista = requests.get('http://localhost:5002/disciplinas')
        achei_dados = False
        achei_distribuidos = False
        for disciplina in r_lista.json():
            if 'dados' in disciplina['nome']:
                achei_dados = True
            if 'distri' in disciplina['nome']:
                achei_distribuidos = True
        if not achei_dados:
            self.fail('disciplina estrutura de dados nao apareceu na lista de disciplinas')
        if not achei_distribuidos:
            self.fail('disciplina distribuidos nao apareceu na lista de disciplinas')

    def test_202_disciplinas_por_id(self):
        r = requests.post('http://localhost:5002/disciplinas',json={'id':103,'nome':'matematica','status':12,'plano_ensino':'funcoes e calculo','carga_horaria':15})
        r_lista = requests.get('http://localhost:5002/disciplinas/103')
        self.assertEqual(r_lista.json()['nome'],'matematica')
        self.assertEqual(r_lista.json()['plano_ensino'],'funcoes e calculo')
        self.assertEqual(r_lista.json()['carga_horaria'],15)
        self.assertEqual(r_lista.json()['status'],12)



    
    def test_203_adiciona_e_reseta(self):
        r = requests.post('http://localhost:5002/disciplinas',json={'id':104,'nome':'lp2','status':12,'plano_ensino':'dicionarios e classes','carga_horaria':15})
        r_lista = requests.get('http://localhost:5002/disciplinas')
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r_lista_depois = requests.get('http://localhost:5002/disciplinas')
        self.assertEqual(len(r_lista_depois.json()),0)

    def test_204_adiciona_e_deleta(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':100,'nome':'estruturas de dados','status':12,'plano_ensino':'dados','carga_horaria':15})
        r = requests.post('http://localhost:5002/disciplinas',json={'id':101,'nome':'distribuidos','status':12,'plano_ensino':'clientes e servidores','carga_horaria':10})
        r_lista = requests.get('http://localhost:5002/disciplinas')
        self.assertEqual(len(r_lista.json()),2)
        requests.delete('http://localhost:5002/disciplinas/100')
        r_lista = requests.get('http://localhost:5002/disciplinas')
        self.assertEqual(len(r_lista.json()),1)
    
    def test_205_edita(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':100,'nome':'estruturas de dados','status':12,'plano_ensino':'dados','carga_horaria':15})
        r_antes = requests.get('http://localhost:5002/disciplinas/100')
        self.assertEqual(r_antes.json()['nome'],'estruturas de dados')
        requests.put('http://localhost:5002/disciplinas/100',json={'id':100,'nome':'algoritmos','status':12,'plano_ensino':'dados','carga_horaria':15})
        #o que mudou foi o nome
        r_depois = requests.get('http://localhost:5002/disciplinas/100')
        self.assertEqual(r_depois.json()['nome'],'algoritmos')

    def test_206_id_inexistente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.put('http://localhost:5002/disciplinas/15',json={'id':15,'nome':'algoritmos 2','status':22,'plano_ensino':'notacao O grande, theta','carga_horaria':15})
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'disciplina nao encontrada')
        r = requests.get('http://localhost:5002/disciplinas/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'disciplina nao encontrada')
        r = requests.delete('http://localhost:5002/disciplinas/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'disciplina nao encontrada')

    def test_207_criar_com_id_ja_existente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':100,'nome':'estruturas de dados','status':12,'plano_ensino':'dados','carga_horaria':15})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':100,'nome':'distribuidos','status':12,'plano_ensino':'clientes e servidores','carga_horaria':10})
        self.assertIn(r.status_code,[400,409])
        self.assertEqual(r.json()['erro'],'id ja utilizada')

    def test_208_post_com_campos_faltando(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':100,'nome':'estruturas de dados','status':12,'plano_ensino':'dados','carga_horaria':15})
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={         'nome':'estruturas de dados','status':12,'plano_ensino':'dados','carga_horaria':15})
        self.assertIn(r.status_code,[400,422])
        self.assertTrue('erro' in r.json())
        r = requests.post('http://localhost:5002/disciplinas',json={'id':101,                             'status':12,'plano_ensino':'dados','carga_horaria':15})
        self.assertIn(r.status_code,[400,422])
        self.assertTrue('erro' in r.json())
        r = requests.post('http://localhost:5002/disciplinas',json={'id':102,'nome':'estruturas de dados','status':12,                       'carga_horaria':15})
        self.assertIn(r.status_code,[400,422])
        self.assertTrue('erro' in r.json())
        r = requests.post('http://localhost:5002/disciplinas',json={'id':103,'nome':'estruturas de dados','status':12,'plano_ensino':'dados'})
        self.assertIn(r.status_code,[400,422])
        self.assertTrue('erro' in r.json())
    
    def test_300_ofertadas_retorna_lista(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        r = requests.get('http://localhost:5002/ofertadas')
        self.assertEqual(type(r.json()),type([]))
        self.assertEqual(len(r.json()),0)
    
    def test_300b_nao_confundir_ofertada_e_outras_entidades(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        r = requests.post('http://localhost:5002/alunos',json={'nome':'fernando','id':1})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'roberto','id':2})
        r = requests.post('http://localhost:5002/disciplinas',json={'id':100,'nome':'estruturas de dados','status':12,'plano_ensino':'dados','carga_horaria':15})
        self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://localhost:5002/ofertadas')
        self.assertEqual(len(r_lista.json()),0)

    def test_301_adiciona_ofertadas(self):
        r = requests.post('http://localhost:5002/ofertadas',json={'id':100,'ano':2019,'semestre':1,'turma':'SI3','data':'2019-04-13'})
        r = requests.post('http://localhost:5002/ofertadas',json={'id':101,'ano':2019,'semestre':1,'turma':'ADS3','data':'2019-04-13'})
        r_lista = requests.get('http://localhost:5002/ofertadas')
        achei_ads = False
        achei_si = False
        for ofertada in r_lista.json():
            if 'SI' in ofertada['turma']:
                achei_si = True
            if 'ADS' in ofertada['turma']:
                achei_ads = True
        if not achei_ads:
            self.fail('ofertada de ads nao apareceu na lista de ofertadas')
        if not achei_si:
            self.fail('ofertada de si nao apareceu na lista de ofertadas')

    def test_302_disciplinas_por_id(self):
        r = requests.post('http://localhost:5002/ofertadas',json={'id':110,'ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20'})
        r_lista = requests.get('http://localhost:5002/ofertadas/110')
        self.assertEqual(r_lista.json()['turma'],'ADS2')
        self.assertEqual(r_lista.json()['data'],'2010-04-20')
        self.assertEqual(r_lista.json()['ano'],2010)
        self.assertEqual(r_lista.json()['semestre'],1)



    
    def test_303_adiciona_e_reseta(self):
        r = requests.post('http://localhost:5002/ofertadas',json={'id':110,'ano':2010,'semestre':2,'turma':'GTI2','data':'2010-04-20'})
        r_lista = requests.get('http://localhost:5002/ofertadas')
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r_lista_depois = requests.get('http://localhost:5002/ofertadas')
        self.assertEqual(len(r_lista_depois.json()),0)

    def test_304_adiciona_e_deleta(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':100,'ano':2019,'semestre':1,'turma':'SI3','data':'2019-04-13'})
        r = requests.post('http://localhost:5002/ofertadas',json={'id':1,'ano':2019,'semestre':1,'turma':'ADS3','data':'2019-11-13'})
        r_lista = requests.get('http://localhost:5002/ofertadas')
        self.assertEqual(len(r_lista.json()),2)
        requests.delete('http://localhost:5002/ofertadas/100')
        r_lista = requests.get('http://localhost:5002/ofertadas')
        self.assertEqual(len(r_lista.json()),1)
    
    def test_305_edita(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':1,'ano':2019,'semestre':1,'turma':'ADS3','data':'2019-11-13'})
        r_antes = requests.get('http://localhost:5002/ofertadas/1')
        self.assertEqual(r_antes.json()['turma'],'ADS3')
        requests.put('http://localhost:5002/ofertadas/1',json={'id':1,'ano':2019,'semestre':1,'turma':'ADS2','data':'2019-11-13'})
        #o que mudou foi a turma
        r_depois = requests.get('http://localhost:5002/ofertadas/1')
        self.assertEqual(r_depois.json()['turma'],'ADS2')

    def test_306_id_inexistente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.put('http://localhost:5002/ofertadas/10',json={'id':10,'ano':2020,'semestre':2,'turma':'SI2','data':'2019-10-13'})
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'ofertada nao encontrada')
        r = requests.get('http://localhost:5002/ofertadas/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'ofertada nao encontrada')
        r = requests.delete('http://localhost:5002/ofertadas/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'ofertada nao encontrada')

    def test_307_criar_com_id_ja_existente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':100,'ano':2019,'semestre':1,'turma':'SI3','data':'2019-04-13'})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':100,'ano':2011,'semestre':1,'turma':'ADS3','data':'2011-11-23'})
        self.assertIn(r.status_code,[400,409])
        self.assertEqual(r.json()['erro'],'id ja utilizada')

    def test_308_post_com_campos_faltando(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':100,'ano':2019,'semestre':1,'turma':'SI3','data':'2019-04-13'})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={         'ano':2019,'semestre':1,'turma':'SI3','data':'2019-04-13'})
        self.assertIn(r.status_code,[400,422])
        self.assertTrue('erro' in r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':101,           'semestre':1,'turma':'SI3','data':'2019-04-13'})
        self.assertIn(r.status_code,[400,422])
        self.assertTrue('erro' in r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':102,'ano':2019,             'turma':'SI3','data':'2019-04-13'})
        self.assertIn(r.status_code,[400,422])
        self.assertTrue('erro' in r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':103,'ano':2019,'semestre':1,'turma':'SI3'                    })
        self.assertIn(r.status_code,[400,422])
        self.assertTrue('erro' in r.json())
        
        
    def test_309_professor_deve_ser_valido_ao_criar_ofertada(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':100,'ano':2019,'semestre':1,'turma':'SI3','data':'2019-04-13','id_professor':500})
        self.assertIn(r.status_code,[400,422])
        r_lista = requests.get('http://localhost:5002/ofertadas')
        self.assertTrue(len(r_lista.json()) == 0)
        requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':500})
        r = requests.post('http://localhost:5002/ofertadas',json={'id':100,'ano':2019,'semestre':1,'turma':'SI3','data':'2019-04-13','id_professor':500})
        self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://localhost:5002/ofertadas')
        self.assertTrue(len(r_lista.json()) == 1)

    def test_400_professor_com_tipos_errados(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':'500'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/professores',json={'nome':12,'id':501})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':502})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5002/professores/500',json={'nome':'lucas','id':'503'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
    
    def test_400a_professor_com_banana(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':504, 'banana':'madura'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
    
    def test_401_aluno_com_tipos_errados(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':'500'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':12,'id':500})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':501})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5002/alunos/500',json={'nome':'lucas','id':'503'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())

    def test_401a_aluno_com_frutas(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':504, 'abacate':'verde'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':504, 'melao':'de redinha'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':504, 'pera':'para deputada'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())

   
    def test_402_disciplina_com_tipos_errados(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':99,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500})
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':'99','nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/disciplinas',json={'id':99,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500})
        self.assertIn(r.status_code,[400,409])
        self.assertIn('erro', r.json())
    
    def test_403_disciplina_coordenador_opcional(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':99,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':98,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500,'id_coordenador':2})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':97,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500,'id_coordenador':'nao devia ser string'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
    
    def test_404_disciplina_com_frutas(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':98,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500,'id_coordenador':2})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':97,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500,'id_coordenador':2,'manga':'ba'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/disciplinas',json={'id':96,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500,'id_coordenador':2,'cajuina':'cristalina em terezina'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())


    def test_405_ofertada_com_tipos_errados(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':110,'ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20'})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':'111','ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':112,'ano':'2010','semestre':1,'turma':'ADS2','data':'2010-04-20'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':113,'ano':2010,'semestre':'1','turma':'ADS2','data':'2010-04-20'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':114,'ano':2010,'semestre':1,'turma':10,'data':'2010-04-20'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':115,'ano':2010,'semestre':1,'turma':'ADS2','data':2010})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
    
    def test_405_ofertada_com_frutas(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':110,'ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20'})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':111,'ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20','maca':'envenenada'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':113,'ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20','abacaxi':'doce, doce'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/ofertadas',json={'id':114,'ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20','fruto':'vermelho'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())

    def test_500_log_professor(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        self.limpa_logs()
        r = requests.post('http://localhost:5002/professores',json={'nome':'cicero','id':29})
        if 'cicero' not in open('sala_aula.log').read():
            self.fail('log incompleto')
    
    def test_501_log_aluno(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        self.limpa_logs()
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':28})
        if 'lucas' not in open('sala_aula.log').read():
            self.fail('log incompleto')

    def test_502_log_disciplina(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        self.limpa_logs()
        r = requests.post('http://localhost:5002/disciplinas',json={'id':99,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500})
        if 'json' not in open('sala_aula.log').read():
            self.fail('log incompleto')
    
    def test_503_log_ofertada(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        self.limpa_logs()
        r = requests.post('http://localhost:5002/ofertadas',json={'id':110,'ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20'})
        if 'ADS2' not in open('sala_aula.log').read():
            self.fail('log incompleto')

    def test_600_db(self):
        try:
            con = sqlite3.connect('lms.db')
        except:
            self.fail('nao achei o arquivo lms.db na pasta do runtests')
        finally:
            con.close()
    
    def test_601_db_aluno(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'id':11,'nome':'paca'})
        self.devo_achar('paca')
        r = requests.put('http://localhost:5002/alunos/11',json={'id':11,'nome':'capivara'})
        self.devo_achar('capivara')
        self.nao_devo_achar('paca')
        r = requests.delete('http://localhost:5002/alunos/11')
        self.nao_devo_achar('capivara')
        self.nao_devo_achar('paca')
    
    def test_602_db_professores(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'id':11,'nome':'paca'})
        self.devo_achar('paca')
        r = requests.put('http://localhost:5002/professores/11',json={'id':11,'nome':'capivara'})
        self.devo_achar('capivara')
        self.nao_devo_achar('paca')
        r = requests.delete('http://localhost:5002/professores/11')
        self.nao_devo_achar('capivara')
        self.nao_devo_achar('paca')


    
    def test_603_db_disciplina(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/disciplinas',json={'id':99,'nome':'distemas distribuidos','status':11,'plano_ensino':'json ou johnson?','carga_horaria':1500})
        self.devo_achar('johnson')
        r = requests.put('http://localhost:5002/disciplinas/99',json={'id':99,'nome':'distemas distribuidos','status':11,'plano_ensino':'json','carga_horaria':1500})
        self.devo_achar('json')
        self.nao_devo_achar('johnson')
        r = requests.delete('http://localhost:5002/disciplinas/99')
        self.nao_devo_achar('json')
        self.nao_devo_achar('johnson')
        
        
    def test_604_db_ofertada(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/ofertadas',json={'id':110,'ano':2010,'semestre':1,'turma':'ADS2','data':'2010-04-20'})
        self.devo_achar('ADS2')
        r = requests.put('http://localhost:5002/ofertadas/110',json={'id':110,'ano':2010,'semestre':1,'turma':'ADS3','data':'2010-04-20'})
        self.nao_devo_achar('ADS2')
        self.devo_achar('ADS3')
        r = requests.delete('http://localhost:5002/ofertadas/110')
        self.nao_devo_achar('ADS2')
        self.nao_devo_achar('ADS3')
        
    def limpa_logs(self):
       open('sala_aula.log', 'w').close()

    #essa funcao verifica se uma string aparece em algum
    #lugar da sua base de dados
    def sql_busca_tosca(self,procurando):
        con = sqlite3.connect('lms.db')
        cursorObj = con.cursor()
        cursorObj.execute('SELECT name from sqlite_master where type= "table"')
        tabelas = [a[0] for  a in cursorObj.fetchall()]
        dados = []
        for tabela in tabelas:
           cursorObj.execute('SELECT * from '+tabela)
           dados.extend(cursorObj.fetchall())
        con.close()
        return procurando in str(dados)

    def devo_achar(self,string):
        if not self.sql_busca_tosca(string):
            self.fail('procurei a string '+string+'''na sua base de dados
                  era para ela estar lá, mas não achei''')
        
    def nao_devo_achar(self,string):
        if self.sql_busca_tosca(string):
            self.fail('procurei a string '+string+'''na sua base de dados
                  era para ela NAO estar lá, mas achei''')


    

    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
