from typing import cast
import pymysql.cursors
import pymysql
import dotenv
import os

dotenv.load_dotenv()

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.DictCursor

connection = pymysql.connect(
    host = os.environ['MYSQL_HOST'],
    user = os.environ['MYSQL_USER'],
    password = os.environ['MYSQL_PASSWORD'],
    database = os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR
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

    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: ')) # sql injection
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 3

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))
        data5 = cursor.fetchall()
        
        for row in data5:
            print(row)

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    # with connection.cursor() as cursor:
    #     sql = (
    #         f'DELETE from {TABLE_NAME} ' # DELETAR ONDE (DELETE WHERE), ATUALIZAR ONDE(UPDATE WHERE)
    #         'WHERE id = %s '
    #     )
    #     cursor.execute(sql)
    #     connection.commit()

    #     cursor.execute(f'SELECT * FROM {TABLE_NAME}')

    #     for row in cursor.fetchall():
    #         print(row)
    
    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR, cursor)
        sql = (
            f'UPDATE {TABLE_NAME} ' # DELETAR ONDE (DELETE WHERE), ATUALIZAR ONDE(UPDATE WHERE)
            'SET nome=%s, idade=%s '
            'WHERE id=%s '
        )
        cursor.execute(sql, ('Eleonor', 26, 4))
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        data6 = cursor.fetchall()

        print()
        print('For 1: ')
        for row in cursor.fetchall():
            print(row)
        

        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1 '
        )
        lastIdFromSelect = cursor.fetchone()

        print(lastIdFromSelect)

        print('resultFromSelect', resultFromSelect)
        print('rowcount', cursor.rowcount)
        print('lastrowid', cursor.lastrowid)
        print('lastrowid na mão', lastIdFromSelect)

        # cursor.scroll(-1)
        print('rownumber', cursor.rownumber)

    connection.commit()