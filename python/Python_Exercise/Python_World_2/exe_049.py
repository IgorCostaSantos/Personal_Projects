n = int(input('digite um numero para saber sua tabuada: '))
tab = -1
m = (n * 10) + 1
for t in range(0, m, n):
    tab = tab + 1
    print('{} X {} = {}'.format(n, tab, t))