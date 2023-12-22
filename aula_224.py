class A:
    ...
    #def quem_sou(self):
    #    print('A')

class B:
    ...
    def quem_sou(self):
        print('B')

class C:
    ...
    def quem_sou(self):
        print('C')

class D(B,C):
    ...
    #def quem_sou(self):
    #    print('D')

d = D()
d.quem_sou()
#print(D.__mro__)
print(D.mro())