num = 1
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('peso da {}° pessoa: '.format(num)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso
    num = num + 1

print('''
O maior peso lido foi de {}KG
O menor peso lido foi de {}KG'''.format(maior, menor))
