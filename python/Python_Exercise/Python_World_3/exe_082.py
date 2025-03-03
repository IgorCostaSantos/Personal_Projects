lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    while True:
        r = str(input('Deseja continuar? [S/N] '))[0].upper()
        if r in 'SN':
            break
    if r == 'N':
        break

for c in lista:
    if c % 2 == 0:
        listap.append(c)
    else:
        listai.append(c)
print(f'A lista completa é: {lista}')
print(f'A lista com pares é: {listap}')
print(f'A lista com impares é: {listai}')
