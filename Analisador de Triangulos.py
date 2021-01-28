from time import sleep
print('=*='*10)
print('Analisador de Triangulos:')
print('=*='*10)
p1 = float(input('Digite o primeiro segmento: '))
p2 = float(input('Digite o segundo segmento: '))
p3 = float(input('Digite o terceiro segmento: '))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos acima PODEM FORMAR um triangulo,', end='')
    if p1 == p2 == p3:
        print(' EQUILÁTERO !')
    elif p1 == p2 or p2 == p3 or p3 == p1:
        print(' ISÓSCELES !')
    else:
        print(' ESCALENO !')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')
sleep(5)
