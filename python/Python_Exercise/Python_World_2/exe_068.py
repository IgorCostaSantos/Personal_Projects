from random import randint
pc = randint(1, 10)
cont = 0
print('=-=' * 10)
print('{: ^30}'.format('VAMOS JOGAR IMPAR OU PAR'))
print('=-=' * 10)
while True:
    pl = int(input('Digite um valor: '))
    ip = str(input('Impar ou Par [I/P] ')).upper()[0]
    if ip != 'Ii' or ip != 'Pp':
        while ip == 'Ii' or ip == 'Pp':
            ip = str(input('Impar ou Par [I/P] ')).upper()[0]
    res = pl + pc
    div = res % 2

    print('---' * 7)

    print(f'''
    O Computador jogou {pc}.
    A soma {pl} + {pc} é {res}''')

    print('---' * 7)

    if div == 1 and ip == 'I':
        print(f'''Voce jogou {pl} e o computador jogou {pc}
              a soma entre eles da {res}, e da IMPAR''')

        print('\033[32mVoce VENCEU!\033[m')
        print(f'---' * 7)
        print('Vamos jogar novamente...')
        print(f'---' * 7)
        cont += 1

    elif div == 0 and ip == 'P':
        print(f'''Voce jogou {pl} e o computador jogou {pc}
        a soma entre eles da {res}, e da PAR''')

        print('\033[32mVoce VENCEU!\033[m')
        print(f'---' * 7)
        print('Vamos jogar novamente...')
        print('---' * 7)
        cont += 1

    else:
        print('\033[31mVocê perdeu!\033[m')
        break

print('---' * 7)
print(f'GAME OVER! Você vendeu {cont} vezes.')





