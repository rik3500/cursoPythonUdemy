import pymysql.cursors
from senha import usuario, senha

conexao = pymysql.connect(
    host='localhost',
    user=usuario,
    password=senha,
    db='interacao',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


with conexao.cursor() as cursor:
    cursor.execute('select * from cadastros')
    dados = cursor.fetchall()

print(dados)