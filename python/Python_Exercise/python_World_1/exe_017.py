from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir \033[36;40m{hi :.2f}\033[m')
