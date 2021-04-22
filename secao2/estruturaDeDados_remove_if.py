'''
remove(6)
'''

x = [1, 2, 3, 4, 5]

print(x)

y = int(input('Digite um número para apgar a lista: '))

if y in x:
    x.remove(y)
    print('Removido')

print(x)