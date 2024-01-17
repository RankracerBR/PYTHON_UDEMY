import os

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
print(os.path.split(caminho))
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
#print(arquivo, extensao_arquivo)
#print(os.path.exists('C:/Users/Pichau/Documents/'))
#print(os.path.abspath('.'))
print(caminho)
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(diretorio))