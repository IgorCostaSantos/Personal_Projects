n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite  o terceiro numero: '))
# Maior
if n1 > n2 and n1 > n3:
    print(f'O maior numero é \033[4;31;40m{n1}\033[m')
elif n2 > n1 and n2 > n3:
    print(f'O maior numero é \033[4;31;40m{n2}\033[m')
elif n3 > n1 and n3 > n2:
    print(f'O maior numero é \033[4;31;40m{n3}\033[m')
# Menor
if n1 < n2 and n1 < n3:
    print(f'O menor numero é \033[4;34;40m{n1}\033[m')
elif n2 < n3 and n1 < n1:
    print(f'O menor numero é \033[4;34;40m{n2}\033[m')
elif n3 < n2 and n1 < n1:
    print(f'O menor numero é \033[4;34;40m{n3}\033[m')
