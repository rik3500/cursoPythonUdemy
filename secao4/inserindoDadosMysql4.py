import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

#x = str(input('Digite seu nome: '))

with conexao.cursor() as cursor:
    cursor.execute('create table cadastros(id int primary key auto_increment, nome varchar(50) not null, endereco varchar(300));')
    conexao.commit()