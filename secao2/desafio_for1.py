'''
Criar uma tabuada com o laço de repetição for
'''

for i in range(0, 11):
    result=0
    for y in range(0, 11):
        result = i * y
        print(f'{i} x {y} = {result}')

    print('*'*12)