print('-=-' * 13)
print('analisador de triangulos')
print('-=-' * 13)

r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento'))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('\033[4;32;40mcom estes segmentos acima PODE SER FORMADO um trialgulo\033[m')
else:
    print('\033[4;31;40mcom estes segmentos acima NAO PODE SER FORMADO um triangulo\033[m')
