import math
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
q = n ** (1/2)
q2 = math.sqrt(n)   #2° alternativa
print("""
O dobro de {} é \033[34;40m{}\033[m
O triplo de {} é \033[35;40m{}\033[m
A raiz quadrada de {} é \033[36;40m{:.3f}\033[m"""
      .format(n, d, n, t, n, q2))