cont = 0

print('==' * 20)
print('OS 10 TERMOS DE UMA PAR')
print('==' * 20)
p = int(input('primeira termo: '))
r = int(input('razao: '))
d = p + (10 - 1) * r
multi = p
while cont < 10:
    print(multi, end=' -> ')
    multi += r
    cont += 1
print('PAUSA', end=' ')
while True:
    repet = int(input('\nDeseja repetir quantas mais vezes? '))
    if repet != 0:
        while repet != 0:
            print(multi, end=' -> ')
            multi += r
            cont += 1
            repet -= 1
        print('PAUSA', end=' ')
    else:
        break
print('Progressao finalizada com {} termos mostrados'.format(cont))


