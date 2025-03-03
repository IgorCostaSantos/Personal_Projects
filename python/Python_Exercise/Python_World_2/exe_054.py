num = 1
datam = 0
datan = 0
for c in range(7):
    data = int(input('Digite a data de nascimento da {}° pessoa: '.format(num)))
    if data >= 2000:
        datan = datan + 1
    else:
        datam = datam + 1
    num = num + 1

if data >= 2000:
    print('\033[33mao todo tivemos {} pessoas menores de idade\033[m'.format(datan))
else:
    print('\033[32me tambem tivemos {} pessoas maiores de idade\033[m'.format(datam))
