import os

caminho = os.path.join('/Users', 'Pichau', 'Desktop')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(pasta)