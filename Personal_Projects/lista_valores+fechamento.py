
valor = 0
lista = {'0001': 1, '0002': 2, '0003': 3}

print('\033[31mstop\033[m para parar ')

while True:
    id = str(input('Digite o id do produto: '))
    if id != 'stop':
        lista[id]
        valor += lista[id]
    else:
        break

dinheiro = float(input('\nDigite o valor recebido: '))

troco = dinheiro - valor
if troco > 0:
    print('O valor a ser dado de troco é {}.'.format(troco))

elif troco == 0:
    print('nao é necessario troco, o valor esta exato')

elif troco < 0:
    print('faltam {} reais'.format(troco))



