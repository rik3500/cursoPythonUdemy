import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

x = str(input('Digite seu nome: '))
y = str(input('Digite eu endereço: '))

with conexao.cursor() as cursor:
    cursor.execute('insert into cadastros(nome, endereco) values("{}", "{}");'.format(x, y))
    conexao.commit()