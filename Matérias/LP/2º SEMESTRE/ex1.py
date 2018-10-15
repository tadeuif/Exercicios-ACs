class Pessoa:
    def __init__(self, n, e, c):
        self.nome = n
        self.email = e
        self.celular = c

    def get_nome(self):
        return 'Caro(a) %s ' % self.nome

    def get_email(self):
        return self.email
    
    def get_celular(self):
        return self.celular
        
    def set_nome(self, nome):
        self.nome = nome

    def set_email(self, email):
        self.email = email

    def set_celular(self, celular):
        self.celular = celular

#nome, email, celular, sigla, disciplinas
class Aluno(Pessoa):
    def __init__(self, n, e, c, s, m, d):
        super().__init__(n, e, c)
        self.disciplinas = []
        self.disciplinas.append(d)
        self.sigla = s
        self.disc = self.disciplinas
        self.mensalidade = m

    def __repr__(self):
        return 'Nome: %s | Curso: %s' % (self.nome, self.sigla)

    def get_sigla(self):
        return '%c.%c.%c.' % (self.sigla[0], self.sigla[1], self.sigla[2])

    def get_mensalidade(self):
        return 'R$ %.2f' % self.mensalidade
    
    def get_disciplina(self):
        return self.disc

    def set_sigla(self, sigla):
        self.sigla = sigla

    def set_mensalidade(self, mensalidade):
        self.mensalidade = mensalidade

    def set_disciplina(self, d):
        self.disciplinas.append(d)
        self.disc = self.disciplinas

    
a = Aluno('Jô','jo@gmail.', 190, 'ADS', 630,'IOT')
a2 = Aluno('Zé','ze@gmail.', 190, 'ADS', 630,'IOT')
a3 = Aluno('Du','du@gmail.', 190, 'ADS', 630,'IOT')

#nome, email, celular, sigla, disciplinas
class Professor(Pessoa):
    def __init__(self, n, e, c, v):
        super().__init__(n, e, c)
        #self.disc = d
        self.hora_aula = float(v)
        
    def __repr__(self):
        return 'Nome: Prof. %s ' % (self.nome)

    def get_nome(self):
        return 'Mestre %s ' % self.nome

    def get_hota_aula(self):
        return self.hora_aula

    def set_hora_aula(self, hora):
        self.hora_aula = hora

p = Professor('Lucio', 'lucio@gmail', 192, 100)

print(a.get_disciplina())
print(a.set_disciplina('LP2'))
print(a.get_disciplina())
print(a.set_disciplina('BD'))
print(a.get_disciplina())
