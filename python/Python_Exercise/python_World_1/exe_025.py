nome = str(input('Qual seu nome completo: ')).strip().lower()

print('Seu nome tem Silva? {}'.format('silva' in nome))

"""if 'silva' in nome:
    print('\033[1;32;40mO seu nome TEM SILVA na posição {}\033[m'.format(nome.find('silva')+1))
else:
    print('\033[1;31;40mO seu nome NÃO TEM SILVA\033[m')"""