print('==' * 20)
print('OS 10 TERMOS DE UMA PAR')
print('==' * 20)
p = int(input('primeira termo: '))
r = int(input('razao: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print('{} '.format(c), end='-> ')

