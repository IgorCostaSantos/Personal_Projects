num = int(input('Digite um numero: '))
r = num % 2

if r == 0:
    print(f'Seu numero é {num}, e ele é \033[33;40mPAR\033[m')
else:
    print(f'Seu numero é {num}, e ele é \033[34;40mIMPAR\033[m')