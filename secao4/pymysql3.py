import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

x = 'create table teste(nome varchar(10))'

with conexao.cursor() as cursor:
    cursor.execute(x)
print('Saiu')