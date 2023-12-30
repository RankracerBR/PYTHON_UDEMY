def meu_rpr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct): #crie e retorna a classe
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_rpr

        if 'falar' not in cls.__dict__ or \
            not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls
     
    def __call__(cls, *args, **kwargs): #Cria e retorna a instância
        instancia = super().__call__(*args, **kwargs)
        
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')
        return instancia

class Pessoa(object, metaclass=Meta):
    #falar = 1234

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome
 
    def falar(self):
        print('FALANDO...')

p1 = Pessoa('Luiz')
p1.falar()