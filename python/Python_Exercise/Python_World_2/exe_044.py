valor = float(input('Preço da compra: R$'))
forma = int(input("""
QUAL A FORMA DE PAGAMENTO:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
\033[32mQual é a opção?\033[m """))

if forma == 1:
    desconto = (valor * 10) / 100
    juros = valor - desconto
    print('Voce selecionou Dinheiro/cheque, sua compra de R${:.2f}, ao total vai custar R${:.2f}.'.format(valor, juros))

elif forma == 2:
    desconto = (valor * 5) / 100
    juros = valor - desconto
    print('Voce selecionou Cartão, sua compra de R${:.2f}, ao total vai custar R${:.2f}.'.format(valor, juros))

elif forma == 3:
    juros = valor
    print('Voce selecionou 2x no Cartão, sua compra de R${:.2f}, ao total vai custar R${:.2f}.'.format(valor, juros))

elif forma == 4:
    parcela = int(input('quantas parcelas? '))

    if parcela >= 3:
        desconto = (valor * 20) / 100
        juros = valor + desconto
        juros = juros / parcela
        print('Voce selecionou 3x ou Mais no Cartão, sua compra de R${:.2f}, ao total vai custar R${:.2f}.'.format(valor, juros))
    else:
        print('\033[31mopção invalida, selecione a opção 3, 2 ou 1 de acordo com oq deseja.\033[m')
else:
    print('\033[31mVoce selecionou uma opção invalida, tente novamente.\033[m')
