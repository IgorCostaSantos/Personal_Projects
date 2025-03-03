cidade = str(input('Em que cidade voce nasceu? ')).strip().capitalize()


if cidade[:5] == 'Santo':
    print('\033[1;32;40mA cidade que vc nasceu COMEÇA com santos\033[m')
else:
    print('\033[1;31;40mA cidade em que vc nasceu NÃO começa com santos\033[m')