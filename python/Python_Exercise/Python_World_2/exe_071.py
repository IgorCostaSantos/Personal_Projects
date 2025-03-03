v50 = v20 = v10 = v1 = v5 = v4 = v3 = v2 = 0
print('=' * 28,
      '\n{: ^28}'.format('BANCO DO IGOR'))
print('=' * 28)

saque = int(input('Digite o valor a ser sacado: '))
while True:
    if v50 > saque:
        v50 -= 50
        v5 -= 1
        if v50 != 0:
            print(f'Total de {v5} cedulas de R$50')
        break
    v50 += 50
    v5 += 1

saque = saque - v50

if saque != 0:
    while True:
        if saque < v20:
            v20 -= 20
            v4 -= 1
            if v20 != 0:
                print(f'Total de {v4} cedulas de R$20')
            break
        v20 += 20
        v4 += 1
saque = saque - v20

if saque != 0:
    while True:
        if saque < v10:
            v10 -= 10
            v3 -= 1
            if v10 != 0:
                print(f'Total de {v3} cedulas de R$10')
            break
        v10 += 10
        v3 += 1
saque = saque - v10

if saque != 0:
    while True:
        if saque < v1:
            v1 -= 1
            v2 -= 1
            if v1 != 0:
                print(f'Total de {v2} cedulas de R$1')
            break
        v1 += 1
        v2 += 1
