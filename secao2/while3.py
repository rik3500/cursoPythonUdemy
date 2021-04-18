decisao=0

while True:
    decisao = int(input('Digite 1 para logar\n2 para cadastrar\n3 para sair\n:'))

    if decisao == 3:
        break

    if decisao == 1:
        print('Logado')
    elif decisao == 2:
        print('Cadastrado')

print('Você saiu do sistema')