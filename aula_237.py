class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self): #Querer uma string
        return f'({self.x}, {self.y})'

    def __repr__(self): #Saber como o objeto é montado
        #class_name = self.__class__.__name__
        class_name = self.__class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

p1 = Ponto(1,2)
p2 = Ponto(978, 876)
print(p1)
print(repr(p2))
print(f'{p2}') #retorna __str__
print(f'{p2!r}')