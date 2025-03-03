lista = [[], [], []]
valp = valt = vals = 0
for c in range(0, 3):
    for x in range(0, 3):
        lista[c].append(int(input(f'Digite o valor [{c}, {x}]: ')))
for n in lista:
    print(f'[{n[0]:^5}] [{n[1]:^5}] [{n[2]:^5}]')

for v in lista[1]:
    vals += v
for c in range(0, 3):
    for x in lista[c]:
        valt += x
        if x % 2 == 0:
            valp += x

print(f'''
A soma total dos valores pares sao: {valp}
A soma  de todos os valores é de: {valt}
A soma dos valores da segunda linha é de: {vals}
''')
