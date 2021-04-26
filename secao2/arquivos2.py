arquivo = open('aulaPython.txt', 'a')

texto = '''Olá, este é um programa que imprime em arquivo textos e demais
dados de escrita pelo teclado.'''

arquivo.write(texto)

arquivo.close()