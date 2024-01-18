from itertools import count
import os

caminho = os.path.join('/Users', 'Pichau', 'Desktop')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)
    
    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        #NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        #os.unlink(caminho_completo_arquivo) CUIDADO!