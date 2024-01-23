from cgi import print_arguments
from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'aula_292.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereço'])