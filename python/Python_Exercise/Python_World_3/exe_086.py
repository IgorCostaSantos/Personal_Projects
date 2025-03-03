lista = [[], [], []]
vp = v3 = vm2 = 0
for c in range(0, 3):
    for x in range(0, 3):
        lista[c].append(int(input(f'Digite o valor [{c}, {x}]: ')))

for n in lista:
    print(f'[{n[0]:^5}] [{n[1]:^5}] [{n[2]:^5}]')

for c in range(0, 3):
    for x in range(0, 3):
        if lista[c][x] % 2 == 0:
            vp += lista[c][x]
    v3 += lista[c][2]

print(f'''
A soma dos valores pares é {vp}.
A soma dos valores da terceira coluna é {v3}
O maior valor da segunda linha é {max(lista[1])}
''')
