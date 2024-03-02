import pymysql
import dotenv
import os

dotenv.load_dotenv()

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host = os.environ['MYSQL_HOST'],
    user = os.environ['MYSQL_USER'],
    password = os.environ['MYSQL_PASSWORD'],
    database = os.environ['MYSQL_DATABASE'],
)

print(os.environ['MYSQL_DATABASE'])

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Começo a manipular dados a partir daqui
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(age)s)'
        )
        data2 = {
            "nome": "Le",
            "age": 37
            }

        result = cursor.execute(sql, data2)
        print(sql, data2)
        print(result)
    connection.commit()

        # Começo a manipular dados a partir daqui
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s)'
        )
        data3 = (
            {"name": "Siri","age": 33, },
            {"name": "Júlia","age": 21, },

        )
        result = cursor.executemany(sql, data3)
        print(sql, data3)
        print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s)'
        )
        data4 = (
            ("Siri", 22),
            ("Helena", 15),
        )
        result = cursor.executemany(sql, data4)
        print(sql, data4)
        print(result)
    connection.commit()