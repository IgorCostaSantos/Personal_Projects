n1 = float(input('primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))
m = (n1 + n2) / 2
print('a media entre {:.1f} e {:.1f}, é igual a \033[4;33;40m{:.1f}\033[m'.format(n1, n2, m))
# depois do ponto flutuante, coloque apenas um digito
# : .(ponto flutuante) 1f