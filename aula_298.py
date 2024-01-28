from datetime import date, datetime
import locale
import string
import json     
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula_298.txt'

locale.setlocale(locale.LC_ALL, '')

def converter_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(2022,12,28)
dados = dict(
    nome='João',
    valor=converter_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)


# print(json.dumps(dados, indent=2, ensure_ascii=False))  

# texto = '''
# Prezado(a) $nome, 

# Informamos que sua mensalidade será cobrada no valor de $valor no dia $data. Caso 
# deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

# Atencionsamente,

# ${empresa},
# Abraços :3  
# '''

# template = string.Template(texto)
# print(template.substitute(dados))

class MyTemplates(string.Template):
    delimite = '%'

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = MyTemplates(texto)
    print(template.substitute(dados))