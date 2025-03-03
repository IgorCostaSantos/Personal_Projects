nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()

print(f"""
\033[7;30;47mAnalisando seu nome...\033[m

Seu nome em maiúsculo é \033[4;32;40m{nome.upper()}.\033[m
O seu nome em minúsculo é \033[4;33;40m{nome.lower()}.\033[m
O seu nome é {nome}, e ele tem \033[4;34;40m{len(nome)} letras.\033[m
O seu primeiro nome é {separa[0]}, e ele tem \033[4;35;40m{len(separa[0])} letras.\033[m
""")
