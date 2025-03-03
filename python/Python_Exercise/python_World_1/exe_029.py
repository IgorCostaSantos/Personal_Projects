km = float(input('A quantos km voce estava: '))

if km >= 80:
    m = (km - 80) * 7.00
    print(f"""
    Voce estava acima do limite maximo permitido, voce sera multado.
    Sua multa é de \033[31;40mR${m :.2f}\033[m""")

else:
    print('\033[32;40mVoce estava no limite permitido, tenha um bom dia.\033[m.')