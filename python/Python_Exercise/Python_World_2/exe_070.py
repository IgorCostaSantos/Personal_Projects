somp = cont = preco_min = 0

print('---' * 10)
print('{: ^30}'.format('LOJA SUPER BARATÃO'))
print('---' * 10)

while True:
    nome = str(input('Nome do produto? '))
    preco = float(input('Preco: R$'))
    if preco < preco_min or preco_min == 0:
        preco_min = preco
        nome_min = nome

    if preco > 1000:
        cont += 1
    somp += preco
    while True:
        rep = str(input('Voce quer continuar? [S/N] ')).upper()
        if rep == 'S' or rep == 'N':
            break
    if rep == 'N':
         break

print(f'''
O total gasto foi de R${somp:.2f}
{cont} custam mais de R$1000
o produto mais barato foi {nome_min} que custa R${preco_min:.2f}''')
