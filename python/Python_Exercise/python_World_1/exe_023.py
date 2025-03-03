'''n = int(input('digite um numero de ate 4 digitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10


print(f"""
analizando o numero {n}

Unidade: {n[3]}\033[m
Dezena: {n[2]}\033[m
Centena: {n[1]}\033[m
Milhar: {n[0]}\033[m
""")

'''

n = str(input('digite um numero de ate 4 digitos: '))

print(f"""
analizando o numero {n}

unidade: \033[33;40m{n[3]}\033[m
dezena: \033[34;40m{n[2]}\033[m
centena: \033[35;40m{n[1]}\033[m
milhar: \033[36;40m{n[0]}\033[m""")

