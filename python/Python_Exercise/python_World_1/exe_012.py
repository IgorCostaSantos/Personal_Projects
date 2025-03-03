p = float(input('Qual o preço do produto? '))
d = p * 5 / 100
pd = p - d

print(f'o preço do produto era de \033[32;40m{p :.2f}\033[m, com o desconto de \033[33;40m{5}%\033[m ira custar \033[31;40m{pd :.2f}\033[m')