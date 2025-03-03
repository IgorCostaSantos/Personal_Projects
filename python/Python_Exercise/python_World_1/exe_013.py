s = float(input('Qual O salario do funcionario? RS'))
a = s * 15 / 100
sa = s + a

print(f'um funcionario que ganhava \033[33;40m{s :.2f}\033[m, com {15}% de aumento, passa a receber \033[33;40m{sa :.2f}\033[m')