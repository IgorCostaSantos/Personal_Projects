d = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))

da = d * 60.0
kma = km * 0.15
t = da + kma

print(f'O total a se pagar é de \033[4;35;40m{t :.2f}\033[m')