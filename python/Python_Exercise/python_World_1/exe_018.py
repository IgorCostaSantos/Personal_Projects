from math import sin, cos, tan, radians
an = float(input('digite o angulo que você deseja: '))

sin = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))


print(f"""
o ângulo de {an} tem o SENO de \033[33;40m{sin :.2f}\033[m
o ângulo de {an} o COSSENO é de \033[33;40m{cos :.2f}\033[m
o ângulo de {an} o TANGENTE é de \033[33;40m{tan :.2f}\033[m""")