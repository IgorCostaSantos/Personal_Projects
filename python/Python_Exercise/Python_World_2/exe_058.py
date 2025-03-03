from random import randint

qtd = 1
n = ''
num = randint(0, 10)

print('-=-' * 20)
print('\033[37;40mEstou pensando em um numero entre 0 e 10. Tente adivinha-lo...\033[m')
print('-=-' * 20)

while n != num:
    n = int(input('Em que numero eu pensei? '))
    if n != num:
        qtd = qtd + 1
    if n < num:
        print('Mais... Tente mais uma vez.')
    elif n > num:
        print('Menos... Tente mais uma vez')

print("""\033[32mVoce acertou PARABENS!!!\033[m
voce precisou de {} tentativas.""".format(qtd))
