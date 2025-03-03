s = 0
t = 0
for c in range(6):
    n = int(input('digite o {} numero: '.format(c + 1)))
    if n % 2 == 0:
        s = s + n
        t = t + 1
print('Voce informou {} numeros PARES, e a soma foi {}'.format(t, s))
