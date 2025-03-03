n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
cores = {
'vermelho' : '\033[31m',
'azul' : '\033[34m',
'roxo' : '\033[35m',
'stop' : '\033[m',
}
if n1 > n2:
    print('{}O PRIMEIRO numero é o maior{}'.format(cores['vermelho'], cores['stop']))
elif n1 < n2:
    print('{}O SEGUNDO numero é o maior{}'.format(cores['azul'], cores['stop']))
else:
    print('{}AMBOS TEM O MESMO VALOR{}'.format(cores['roxo'], cores['stop']))
