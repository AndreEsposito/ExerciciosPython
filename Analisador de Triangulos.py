print('=*='*10)
print('Analisador de Triangulos:')
print('=*='*10)
p1 = float(input('Digite o primeiro segmento: '))
p2 = float(input('Digite o segundo segmento: '))
p3 = float(input('Digite o terceiro segmento: '))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos acima \033[7mPODEM FORMAR\033[m um triangulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')
