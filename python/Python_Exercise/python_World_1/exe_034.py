s = float(input('Qual seu salario atual: '))

if s >= 1250.00:
    num = s * 10 / 100
    sm = s + num
    porcentagem = 10
else:
    num = s * 15 / 100
    sm = s +num
    porcentagem = 15

print(f'o seu salario com \033[4;33;40m{porcentagem}%\033[m de aumento é \033[4;36;40m{sm :.2f}\033[m')
