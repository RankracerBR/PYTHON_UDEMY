from zipfile import ZipFile
from pathlib import Path
import shutil
import os

CAMINHO_RAIZ= Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_304_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula_304_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula_304_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip',''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def criar_arquivo(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)

criar_arquivo(10, CAMINHO_ZIP_DIR)

#Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            print(file)
            zip.write(os.path.join(root, file), file)

#Lendo arquidos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

#Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)