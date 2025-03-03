max = min = num = soma = 0

while True:
    val = int(input('Digite os valores: '))
    soma += val
    while True:
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if sn in 'SN':
            break

    if num != 0:
        num += 1
        if max < val:
            max = val

        elif min > val:
            min = val

        if sn == 'N':
            break

    elif num == 0:
        max = min = val
        num += 1

med = soma / num

print(f"""
O maior valor foi de {max}
O menor valor foi de {min}
Tiveram {num} valores digitados ao total
A soma entre todos os numeros foram de {soma}
A media de todos os valores digitados foi de {med :.2f}""")
