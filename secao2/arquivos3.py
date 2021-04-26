arquivo = open('aulaPython.txt', 'r')

texto = arquivo.readlines()

for i in texto:
    print(i)

arquivo.close()