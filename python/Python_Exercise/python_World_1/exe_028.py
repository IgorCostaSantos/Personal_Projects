from random import randint
from time import sleep

print('-=-' * 20)
print('\033[37;40mEstou pensando em um numero entre 0 e 5. Tente adivinha-lo...\033[m')
print('-=-' * 20)

n = int(input('Em que numero eu pensei? '))
num = randint(0, 5)

print('Processando...')
sleep(0.5)

if n == num:
    print('Parábens, você acertou')
else:
    print(f'Sinto muito, voce errou, o numero era \033[4;35;40m{num}\033[m')
