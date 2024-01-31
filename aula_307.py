from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo na tela"',
    #type=str, # Tipo do argumento
    #default='Olá mundo', # Valor padrão
    metavar='STRING',
    action='append',
    #nargs='+',# Recebe mais de um valor
)

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='stroe_true'
)

args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
else:
    print('O valor de b',args.basic)