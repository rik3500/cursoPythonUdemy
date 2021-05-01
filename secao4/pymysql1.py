import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()

cursor.execute('create table pessoas(nome varchar(30), idade int, endereco varchar(100));')

cursor.close()
conexao.close()