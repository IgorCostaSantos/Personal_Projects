from random import randint
from time import sleep

print('-' * 30)
print('{: ^30}'.format('Jogo da mega sena'))
print('-' * 30)

lista, lista2 = [], []

qtd = int(input('Quantos jogos voce deseja sortear? '))

for c in range(0, qtd):
    for d in range(0, 6):
        n = (randint(1, 60))
        if n not in lista2:
            lista2.append(n)
        elif n in lista2:
            while n in lista2:
                n = (randint(1, 60))
            lista2.append(n)
    lista2.sort()
    lista.append(lista2[:])
    lista2.clear()
for c, d in enumerate(lista):
    sleep(0.5)
    print(f'Jogo {c + 1}: {d}')

