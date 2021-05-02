import pymysql.cursors
from senha import senha, usuario

conexao = pymysql.connect(
    host='localhost',
    user=usuario,
    password=senha,
    db='interacao',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

x = str(input('Digite seu nome: '))
y = str(input('Digite seu endereço: '))

with conexao.cursor() as cursor:
    cursor.execute('insert into cadastros(nome, endereco) values ("{}", "{}");'.format(x, y))
    conexao.commit()