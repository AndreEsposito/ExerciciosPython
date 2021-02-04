nome = sexo = resp = ''
idade = total_de_homem = maior_de_18 = mulher_menor_20 = outros = cont = 0
soma_idade = 0
while True:
    print('-'*20)
    print('Cadastre uma Pessoa:')
    print('-' * 20)
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    print('''[1] - MASCULINO
[2] - FEMININO
[3] - OUTROS''')
    sexo = int(input('Genêro: '))
    soma_idade += idade
    resp = str(input('Quer continuar cadastrando [S/N]: ')).strip().upper()
    cont += 1
    if idade >= 18:
        maior_de_18 += 1
    if sexo == 1:
        total_de_homem += 1
    if idade < 20 and sexo == 2:
        mulher_menor_20 += 1
    if sexo == 3:
        outros += 1
    while resp not in 'SN':
        print('Opção inválida! Tente novamente!')
        resp = str(input('Quer continuar cadastrando [S/N]: ')).strip().upper()
    if resp == 'N':
        break
media_idade = soma_idade / cont
print(f'Ao todo temos {cont} pessoas cadastradas em nosso sistema, e a média de idade entre elas é {media_idade:.1f}.')
print('Sendo elas:')
if maior_de_18 == 1:
    print(f'{maior_de_18} pessoa MAIOR de 18 anos, cadastrado.')
elif maior_de_18 > 1:
    print(f'{maior_de_18} pessoas MAIORES de 18 anos, cadastrados. ')
elif maior_de_18 == 0:
    print('Não existindo NENHUMA pessoa MAIOR de 18 anos, cadastrado.')
if total_de_homem == 1:
    print(f'{total_de_homem} homem, cadastrado.')
elif total_de_homem > 1:
    print(f'{total_de_homem} homens, cadastrados. ')
elif total_de_homem == 0:
    print('Não existindo NENHUM homem, cadastrado.')
if mulher_menor_20 == 1:
    print(f'1 mulher MENOR de 20 anos, cadastrada.')
elif mulher_menor_20 > 1:
    print(f'{mulher_menor_20} mulheres MENOR de 20 anos, cadastradas. ')
elif mulher_menor_20 == 0:
    print('Não existindo NENHUMA mulher MENOR de 20 anos, cadastrada.')
if outros == 1:
    print(f'1 genêro INDEFINIDO cadastrado.')
elif outros > 1:
    print(f'{outros} genêros INDEFINIDOS, cadastrados. ')
elif outros == 0:
    print('Não existindo NENHUM genêro INDEFINIDO, cadastrado.')
