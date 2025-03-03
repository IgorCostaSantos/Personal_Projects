from time import sleep
num = 0

print('''
[ 0 ] para parar
\033[33m{}Soma de produtos{}\033[m
'''.format('=-=-' * 4, '=-=-' * 4))

while True:
    s = float(input('Digite o valor que deseja somar: '))
    if s != 0:
        num += s
    else:
        break

sleep(0.3)
print('\n\033[32mO valor total da soma é {}\033[m.'.format(num))
