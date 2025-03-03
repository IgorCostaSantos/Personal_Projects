print('Digite um numero negativo para parar!')
print('white one number negative for break!')
c = 1

while True:
    t = int(input('\nDigite um numero para ver sua tabuada: '))
    if t >= 0:
        for c in range(1, 11):
            print(f'{t} * {c} = {c*t}')
    else:
        break
print('\033[32mPrograma finalizado, Volte sempre!\033[m')





