import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'usuario',
    password = 'senha',
    database = 'base_de_dados',
)

with connection:
    with connection.cursor() as cursor:
        print(cursor)
