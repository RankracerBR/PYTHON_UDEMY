#class MinhaString(str):
#    def upper(self):
#        print('CHAMOU UPPER')
#        retorno = super(MinhaString, self).upper()
#        #super() #Métodos da super classe
#        print('DEPOIS DO UPPER')
#        return retorno

#string = MinhaString('Augusto')
#print(string.upper())

class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')
        
class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')
        
class C(B):
    atributo_c = 'valor c'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('EI, BURLEI O SISTEMA')

    def metodo(self):
        super().metodo() # B
        super(B, self).metodo() # A
        super(B, self).metodo() # object
        print('C')

#print(C.mro())
#print(B.mro())
#print(A.mro())
c = C('Atributo', 'Qualquer')
print(c.atributo)
print(c.outra_coisa)
c.metodo()
#print(c.atributo_a)
#print(c.atributo_b) 
#print(c.atributo_c)
#c.metodo()