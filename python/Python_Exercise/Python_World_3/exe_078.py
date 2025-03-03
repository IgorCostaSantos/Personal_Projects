maxim = minim = 0
lista = []

for c in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))

print(f'Voce digitou os valores {lista}')

if max(lista) in lista:

    for n, v in enumerate(lista):

        if v == max(lista) and maxim == 0:
            print(f'O maior numero é {v}, e esta na posição {n}', end='... ')
            maxim = 1
        elif v == max(lista) and maxim != 0:
            print(f'{n}...')

    for n, v in enumerate(lista):

        if v == min(lista) and minim == 0:
            print(f'O menos numero é {v}, e esta na posição {n}', end='... ')
            minim = 1
        elif v == min(lista) and minim != 0:
            print(f'{n}...')
