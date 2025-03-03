num = int(input('Digite um numero inteiro: '))
resp = int(input("""
Digite:
[ 1 ] para binario
[ 2 ] para octal
[ 3 ] para hexadecimal
Deseja converter este numero para: """))

if resp == 1:
    print(f'O numero {num} transformado em binario é: {bin(num)[2:]}')
elif resp == 2:
    print(f'O numero {num} transformado em octal é: {oct(num)[2:]}')
elif resp == 3:
    print(f'O numero {num} transformado em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção invalida. Tente novamente.')
