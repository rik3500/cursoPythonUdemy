import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacao',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


with conexao.cursor() as cursor:
    cursor.execute('select * from cadastros')
    resultado = cursor.fetchall()

for dado in resultado:
    print(dado)