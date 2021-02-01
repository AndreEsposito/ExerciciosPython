from random import randint
print('=' * 22)
print('Jogo do Par ou Ímpar: ')
print('=' * 22)
vitorias = 0
while True:
    num_jogador = int(input('Digite um valor: '))
    num_computador = randint(0, 10)
    total = num_jogador + num_computador
    tipo = 'p'
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper() [0]
    print(f'Você jogou {num_jogador} e o computador jogou {num_computador}. O total de {total}', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU !!!')
            vitorias += 1
        else:
            print('Você PERDEU !!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU !!!')
            vitorias += 1
        else:
            print('Você PERDEU !!!')
            break
    resp = str(input('Vamos jogar novamente...? [S/N]: ')).strip().upper()
    if resp == 'S':
        continue
    else:
        break
if vitorias == 0:
    print('GAME OVER...!')
elif vitorias == 1:
    print(f'GAME OVER...! Você VENCEU {vitorias} vez!')
elif vitorias == 0 and resp == 'N':
    print('GAME OVER...!')
elif vitorias == 1 and resp == 'N':
    print(f'GAME OVER...! Você VENCEU {vitorias} vez!')
elif vitorias > 1 and resp == 'N':
    print(f'GAME OVER...! Você VENCEU {vitorias} vezes!')
else:
    print(f'GAME OVER...! Você VENCEU {vitorias} vezes!')
