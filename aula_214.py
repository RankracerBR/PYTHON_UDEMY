from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'        

        
    def metodo_publico(self):
        self._metodo_protected()
        print(self.__exemplo)
        return 'metodo_public'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
    
f = Foo()
print(f.public)
print(f.metodo_publico())
#print(f._metodo_protected())
print(f.__metodo_private())