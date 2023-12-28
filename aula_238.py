class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x # 4 + 6
        novo_y = self.y + other.y # 2 + 4
        return Ponto(novo_x, novo_y)

    def __gt__(self, other): #greater than
        resultado_self = self.x + other.y 
        resultado_other = other.x + other.y 
        return resultado_self > resultado_other 


if __name__ == '__main__':
    p1 = Ponto(4,2)
    p2 = Ponto(6,4)
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que p2', p1 > p2)
    print('P2 é maior que p1', p2 > p1)