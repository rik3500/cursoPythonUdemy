import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacao',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

x = str(input('Digite seu nome: '))

with conexao.cursor() as cursor:
    cursor.execute('insert into teste values("{}");'.format(x.title()))
    conexao.commit()