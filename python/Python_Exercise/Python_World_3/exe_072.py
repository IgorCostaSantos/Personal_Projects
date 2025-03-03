num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'trese', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'desenove', 'vinte')
while True:
    while True:
        val = int(input('Digite um número entre 0 e 20: '))
        if 0 <= val <= 20:
            break
    print(f'Voce digitou o numero \033[32m{num[val]}\033[m')
    while True:
        r = str(input('Voce quer continuar? [S/N] ')).upper()[0]
        if r in ('sSnN'):
            break
    if r == 'N':
        break