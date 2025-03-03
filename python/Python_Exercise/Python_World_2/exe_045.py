import random
from time import sleep
print('{:^25}'.format('jokenpo'))
itens = ('pedra', 'papel', 'tesoura')
ale_usuario = int(input('''
[ 0 ]pedra
[ 1 ]papel
[ 2 ]tesoura
Qual é a sua jogada? '''))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

random = random.choice(['pedra', 'papel', 'tesoura'])

if ale_usuario == 0:
    print('Voce selecionou \033[33m{}\033[m.'.format('pedra'))
    if random == 'tesoura':
        print('o computador selecionou tesoura')
        print('Voce \033[32mGANHOU\033[m')
    elif ale_usuario == random:
        print('empate, voce e o computador jogaram: {}'.format(random))
    else:
        print('Voce \033[31mERROU, tente novamente, o computador jogou\033[m \033[33m{}\033[m'.format(random))

elif ale_usuario == 1:
    print('Voce selecionou \033[33m{}\033[m.'.format('papel'))
    if random == 'pedra':
        print('o computador selecionou pedra')
        print('Voce \033[32mGANHOU\033[m')
    elif ale_usuario == random:
        print('empate, voce e o computador jogaram: {}'.format(random))
    else:
        print('Voce \033[31mERROU, tente novamente, o computador jogou\033[m \033[33m{}\033[m'.format(random))

elif ale_usuario == 2:
    print('Voce selecionou \033[33m{}\033[m.'.format('tesoura'))
    if random == 'papel':
        print('o computador selecionou papel')
        print('Voce \033[32mGANHOU\033[m')
    elif ale_usuario == random:
        print('empate, voce e o computador jogaram: {}'.format(random))
    else:
        print('Voce \033[31mERROU, tente novamente, o computador jogou\033[m \033[33m{}\033[m'.format(random))
else:
    print('\033[31mVoce selecionou uma opção invalida, tente novamente\033[m')
"""
random = random.randint(0,2)

print('computador jogou {}'.format(itens[random]))
print('O jogador jogou {}'.format(itens[ale_usuario]))
if random == 0:
    if ale_usuario == 0:
        print('EMPATE')
    elif ale_usuario == 1:
        print('JOGADOR VENCEU')
    elif ale_usuario == 2:
        print('COMPUTADOR VENCEU')
elif random == 1:
    if ale_usuario == 0:
        print('JOGADOR VENCEU')
    elif ale_usuario == 1:
        print('EMPATE')
    elif ale_usuario == 2:
        print('COMPUTADOR VENCEU')
elif random == 2:
    if ale_usuario == 0:
        print('JOGADOR VENCEU')
    elif ale_usuario == 1:
        print('COMPUTADOR VENCEU')
    elif ale_usuario == 2:
        print('EMPATE')
else:
    print('opção invalida, tente novamente!!')"""