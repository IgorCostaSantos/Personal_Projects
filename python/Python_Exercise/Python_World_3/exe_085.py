lista = [[], []]

for x in range(1, 8):
    n = (int(input(f'Digite o {x}° numero: ')))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 == 1:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'''os valores pares foram {lista[0]}
os valores impares fora {lista[1]}''')


