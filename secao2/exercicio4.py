'''Faça um programa que receba várias idades e calcule a média das idades.
Finalize o programa quando a entrada for iqual a -1.'''

idades = []
entrada = 0
while entrada != -1:
    entrada = int(input('Digite uma idade: '))
    if entrada != -1:
        idades.append(entrada)

print(f'A soma das idades digitadas é {sum(idades)}, e a média delas é {sum(idades) / len(idades)}')