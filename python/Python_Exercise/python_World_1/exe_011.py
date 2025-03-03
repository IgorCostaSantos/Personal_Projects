L = float(input('Qual a largura da parede: '))
A = float(input('qual a altura da parede: '))

M = L * A
T = M / 2

print(f"""
sua parede tem o diametro de {L} X {A} e a sua area é de \033[1;33;40m{M}M\033[m
Para pintar a sua parede,voce precisara de \033[1;33;40m{T}L\033[m de tinta.""")