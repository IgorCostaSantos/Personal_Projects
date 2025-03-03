lista = []
print('Digite valores negativos para parar')
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n < 0:
        lista.pop()
        break
print(f'Foram digitados um total de {len(lista)} numeros')
lista.sort(reverse=True)
print(f'A lista de forma decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 esta na posição {lista.index(5)}')
elif 5 not in lista:
    print(f'Nao ha o valor 5 na lista')
