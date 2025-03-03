s = qtd = 0
print('Digite 999 para parar')
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    else:
        s += num
        qtd += 1

print(f'A soma dos {qtd} valores é de {s}!')








