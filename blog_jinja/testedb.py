from sqlite3 import connect

conn = connect("blog.db")
cursor = conn.cursor()

# Executar a consulta que lista as tabelas e views
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' OR type='view';")
tables = cursor.fetchall()

for table in tables:
    print(table)

conn.close()
