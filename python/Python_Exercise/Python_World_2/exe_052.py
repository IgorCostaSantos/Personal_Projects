num = int(input('digite um numero: '))
cont = 0
total = 0

for c in range(num):
    cont = cont + 1
    test = num % cont
    if test == 0:
        print('\033[32m{}\033[m'.format(cont), end=' ')
        total += 1
    else:
        print('\033[31m{}\033[m'.format(cont), end=' ')

if total > 2:
    print('o número {} foi divisível {} vezes'
          '\nele \033[31mNAO É PRIMO\033[m'.format(num, total))

elif total == 2:
    print('o número {} foi divisível {} vezes'
          '\nele \033[32mÉ PRIMO\033[m'.format(num, total))

