num = 0
num2 = 0
val = 0
print('Digite 999 para parar')

while True:
    val = int(input('Digite um valor: '))
    if val != 999:
        num2 += val
        num += 1
    else:
        break

print('A soma total é de {} numeros é de {}'.format(num, num2))
