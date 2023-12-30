class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando:', self.phone)
        return 2134

call1 = CallMe('2342536456')
retorno = call1('Augusto Pontes')
print(retorno)