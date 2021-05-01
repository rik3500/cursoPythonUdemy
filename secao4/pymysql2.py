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

x = 'drop table pessoas'

cursor.execute(x)

cursor.close()
conexao.close()