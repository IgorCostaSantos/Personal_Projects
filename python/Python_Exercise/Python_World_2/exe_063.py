print('_____' * 6)
print('Sequencia de Fibonacci')
print('_____' * 6)
var = int(input('quantos termos deseja mostrar? '))
n = 0
n2 = 1
n3 = n

print('~~~~~' * 6)
cont = 3
print('{} -> {}'.format(n, n2), end=' -> ')

while cont <= var:
    n3 = n + n2

    print(n3, end=' -> ')

    n = n2
    n2 = n3
    cont += 1

print('FIM')
print('~~~~~' * 6)
