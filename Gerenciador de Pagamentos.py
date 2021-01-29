estabelecimento = input(str('Qual é o tipo do estabelecimento: ')).strip().title()
nome = input(str('Qual é o nome da(o) {}: '.format(estabelecimento))).strip().title()
print('=+='*7)
print(f'{estabelecimento} {nome} :')
print('=+='*7)
preço = float(input('Qual o preço das compras: R$'))
print('FORMAS DE PAGAMENTO:')
print('''[1] - à vista no dinheiro/cheque
[2] - à vista no cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão''')
opção = int(input('Qual a opção de pagamento: '))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    print('Sua compra será parcelada em 2 vezes de R${:.2f} SEM JUROS.'.format(preço/2))
elif opção == 4:
    total = preço + (preço * 20/100)
    parcelas = int(input('Em quantas parcelas: '))
    conta = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, conta))
else:
    total = preço
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE !')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
