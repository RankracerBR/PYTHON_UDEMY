from pathlib import Path
import csv
from pydoc import cli

from attr import field

CAMINHO_CSV = Path(__file__).parent / 'aula_294.csv'

lista_clientes = [
    {'Nome': 'Augusto Pontes','Endereco': 'Av 1, 22'},
    {'Nome':'Julia Graziely','Endereco':'R. 2, "1"'}, 
    {'Nome':'Gabriel Almeida','Endereco':"Av B, 3A"},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames = nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)

# lista_clientes = [
#     ['Augusto Pontes', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "2"'],
#     ['Maria Sol', 'Av B, 3A']
# ]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     #nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereco']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         print(cliente.values()) 
#         escritor.writerow(cliente.values())