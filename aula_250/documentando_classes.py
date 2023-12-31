variavel_1 = 1

class Foo:
    """Este é um modulo de exemplo"""
    def soma(self, x: int | float, y: int | float) -> int | float:
        """Soma de x e y"""
        return x + y

    def multipicar(
        x: int | float,
        y: int | float,
        z: int | float | None = None
    ) -> int | float:
        """Multiplica x,y e/ ou z"""

        if z is None:
            return x * y
        return x * y * z

    def bar(self) -> int:
        """O que ele faz
        :raises NotImplementedError: Se o método não for definido
        """
        raise NotImplementedError('Teste')

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4