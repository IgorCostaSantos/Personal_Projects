valor_casa = float(input('Qual o valor da casa que quer financiar: R$'))
salario = float(input('Quanto voce ganha por mes: R$'))
anos = float(input('Em quantos anos de financiamento: '))
mensalidade = valor_casa / (anos * 12)

if mensalidade <= salario * 30 / 100:
    print("""
    Para pegar uma casa de {} em {} anos, você pagara {:.2f}
    emprestimo \033[32mCONCEDIDO!\033[m
    """.format(valor_casa, anos, mensalidade))
else:
    print("""
    Para pegar uma casa de {} em {} anos, você pagara {:.2f}
    emprestimo \033[31mNEGADO!\033[m""".format(valor_casa, anos, mensalidade))
