from time import sleep

num1 = int(input('Digite o 1° numero: '))
num2 = int(input('Digite o 2° numero: '))
r = 0

while r != 5:
    sleep(1)
    r = int(input('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa
    O que voce deseja fazer? '''))

    print('\n')

    if r == 1:
        total = num1 + num2
        print('Voce escolheu, Somar.')
        print('\033[32mA soma de {} + {} é igual á {}\033[m'.format(num1, num2, total))

    elif r == 2:
        total = num1 * num2
        print('Voce escolheu, Multiplicar')
        print('\033[32mA multiplicação de {} x {} é igual á {}\033[m'.format(num1, num2, total))

    elif r == 3:
        print('\033[32mO maior numero é\033[m', end=' ')
        if num1 > num2:
            print(num1)
        elif num2 > num1:
            print(num2)

    elif r == 4:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))

    elif r == 5:
        sleep(1)
        print('Finalizando processo...')
        break

    else:
        print('\033[31mOpção invalida\033[m')

print('programa finalisado')
