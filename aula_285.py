from itertools import count
import math
import os

def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:

    if tamanho_em_bytes <= 0:
        return "0B"
    
    abreviacao_tamanhos = "B","KB","MB","GB","TB","PB"

    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    potencia = base ** indice_abreviacao_tamanhos

    tamanho_final = round(tamanho_em_bytes / potencia, 2)

    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]

    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

print(formata_tamanho(1000))
print(formata_tamanho(1000000))
print(formata_tamanho(1_000_000_000))
print(formata_tamanho(1000))
print(formata_tamanho(1000))

caminho = os.path.join('/Users', 'Pichau', 'Desktop')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)
    
    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        #tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo, 
             formata_tamanho(tamanho))
        #NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        #os.unlink(caminho_completo_arquivo) CUIDADO!