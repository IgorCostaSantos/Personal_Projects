frase = str(input('digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('temos um palindromo')
else:
    print('a frase digitada NÃO é um PALÍNDROMO')




