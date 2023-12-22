class Pessoa:
    cpf = '1234'
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def fala_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome,self.sobrenome,self.__class__.__name__)
    

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'cpf aluno'

c1 = Cliente('Augusto', 'Pontes')
c1.falar_nome_classe()
a1 = Aluno('Julia', 'Graziely')
a1.fala_nome_classe()
print(a1.cpf)
help(Cliente)