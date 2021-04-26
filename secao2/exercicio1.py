'''
    Faça um programa que receba o peso de 7 pessoas. Calcule e mostre:
    * a quantidade de pessoas acima de 90 kg
    * a média dos pesos das pessoas
'''

pesos = []
contador=0

for i in range(0,7):
    pesos.append(float(input('Digite seu peso: \n')))
    if pesos[i] > 90:
        contador += 1

print(f'Existem {contador} pessoas acima de 90Kg e a média de todos os pesos é {sum(pesos)/len(pesos):.2f}')