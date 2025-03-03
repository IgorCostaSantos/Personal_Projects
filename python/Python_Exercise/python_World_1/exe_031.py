km = float(input('qual a distancia da sua viagem em km? '))

print(f'Você está prestes a viajar {km}km.')
if km <= 200:
    r1 = km * 0.5

else:
    r1 = km * 0.45

print(f'O valor da sua passagem é de \033[32;40mR${r1 :.2f}\033[m')
