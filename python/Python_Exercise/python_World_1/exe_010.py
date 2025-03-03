real = float(input('Quanto de dinheiro voce tem na carteira? R$'))
dollar = real / 5.08
print(f'com RS\033[32;40m{real :.2f}\033[m, voce pode comprar US\033[34;40m{dollar :.2f}\033[m de dolares')
