from dataclasses import dataclass, asdict, astuple

@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str

    #def __init__(self, nome, sobrenome):
        #self.nome = nome
        #self.sobrenome = sobrenome
        #self.nome_completo = f'{self.nome} {self.sobrenome}'

    #def __post_init__(self):
        #print('POST INIT')

    #@property
    #def nome_completo(self):
        #return f'{self.nome} {self.sobrenome}'

    #@nome_completo.setter
    #def nome_completo(self, valor):
        #nome, *sobrenome = valor.split()
        #self.nome = nome
        #self.sobrenome = ''.join(sobrenome)

if __name__ == '__main__':
    p1 = Pessoa('Augusto', 'Pontes')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])