lista = []
print('Digite valores negativos para parar')
while True:
    n = int(input('Digite um numero: '))
    if n not in lista and n >= 0:
        lista.append(n)
    elif n in lista:
        print('este valor ja esta na lista')
    elif n < 0:
        lista.pop()
        break

lista.sort()
print(lista)
