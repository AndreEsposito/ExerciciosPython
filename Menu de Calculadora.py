from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
maior = menor = igual = 0
opção = 0
while opção != 6:
    print('''[1] - SOMAR
[2] - SUBTRAIR
[3] - MULTIPLICAR
[4] - VER O MAIOR
[5] - COLOCAR NOVOS NÚMEROS
[6] - SAIR DO PROGRAMA''')
    opção = int(input('Qual é sua opção: '))
    if opção == 1:
        soma = (n1 + n2)
        print('A SOMA entre {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        subtração = (n1 - n2)
        print(f'A SUBTRAÇÃO entre {n1} - {n2} é {subtração}.')
    elif opção == 3:
        multiplicação = (n1 * n2)
        print('A MULTIPLICAÇÃO entre {} x {} é {}.'.format(n1, n2, multiplicação))
    elif opção == 4:
        if n1 > n2:
            maior = n1
            menor = n2
            print('O {} é MAIOR que {}.'.format(maior, menor))
        elif n2 > n1:
            maior = n2
            menor = n1
            print('O {} é MAIOR que {}.'.format(maior, menor))
        else:
            print('Ambos valores são IGUAIS!')
    elif opção == 5:
        print('Informe NOVOS valores:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 6:
        print('Finalizando...')
    elif opção > 6:
        print('Opção inválida! Tente novamente.')
        opção = int(input('Qual é sua opção: '))
    print('=*'*18)
sleep(2)
print('Fim do Programa! Volte sempre!')
sleep(2)
