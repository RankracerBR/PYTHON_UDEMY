import shutil
import os

#DANGER ZONE
HOME = os.path.expanduser('****')
DESKTOP = os.path.join(HOME, '****') #'desktop'
PASTA_ORIGINAL = os.path.join(DESKTOP, '****') #'Exemplo'
NOVA_PASTA = '***'
os.makedirs(NOVA_PASTA)
print(DESKTOP)

os.unlink(NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')


for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        print(caminho_novo_diretorio)
        #os.makedirs(NOVA_PASTA, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA),file)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)