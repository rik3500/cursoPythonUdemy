'''Faça um programa que verifique e mostre os números entre 1000 e 2000(inclusive
que, quando dividido por 11 produz resto igual a 5.'''

vet = []

for i in range(1000, 2001, 1):
    if i % 11 == 5:
        print(i)
        vet.append(i)

print(vet)