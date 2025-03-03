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
    multi = multi + r
    cont += 1
