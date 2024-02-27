import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: Delete sem where
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# cursor.execute(
#     f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}' 
#     '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,' # O autoincrement não vai reordenar a sequência caso um seja deletado
#     'name TEXT,'
#     'weight REAL'
#     ')' 
# )
# connection.commit()

# Registrar valores nas colunas da tabela
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight) '
    'VALUES '
    '(NULL, "Helena", 4), (NULL, "Eduardo", 9.9)'
)
connection.commit()

cursor.close()
connection.close()

