lista = {'moeda': 0, 'nota/pix': 0, 'cartao': 0}
cor = ['\033[31m','\033[32m', '\033[33m', '\033[36m', '\033[m']
total = 0
cor_n = 0
for c, n in enumerate(lista.keys()):

    print('\n[ 0 ] para parar\n')
    print(f'{cor[c]}Valor de {n} {cor[-1]}'.center(50, '='), '\n')

    while True:
        valor = float(input(f'digite o valor em {n}: '))
        if valor != 0:
            lista[n] += valor
        else:
            total += lista[n]
            break

lista['total'] = total
print()
for v, k in lista.items():
    print(f'{cor[cor_n]}O valor em {v} é de {k} reais.\033[m')
    cor_n += 1
    