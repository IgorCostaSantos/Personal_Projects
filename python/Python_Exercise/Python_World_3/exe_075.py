num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
cont = 0
print(f'Voce digitou os numeros {num}')
if num.count(9) >= 1:
       print(f'O numero 9 apareceu {num.count(9)} vezes')
else:
       print(f'O numero 9 NÃO apareceu nenhuma vez')
if num.count(3) >= 1:
       print(f'O numero 3 apareceu pela primeira vez na {num.index(3)+1}° posição')
else:
       print(f'O numero 3 NÃO apareceu em nenhuma posição')
for c in range(0, 4):
       if c % 2 == 0 and c == 0:
              print(f'Os numeros pares que foram: ', end='')
       if (num[c] % 2) == 0:
              print(num[c], end=' ')
              cont += 1

if cont == 0:
       print('Não ouveram veram numeros pares')

