from contextlib import contextmanager

#with open('aula_240.txt', 'w') as arquivo:
#    ...

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        #raise class_exception(*exception_.args).with_traceback(traceback_)

        #print(class_exception)
        #print(exception_)
        #print(traceback_)

        #raise ConnectionError('Não deu para conectar')

        #exception_.add_note('Minha nota')

        #return True #Tratei a exceção

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrinco arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('aula_242.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)