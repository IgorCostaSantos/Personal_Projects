n = str(input('Digite seu nome completo: ')).title()
nome = n.split()
print(f"""
Muito prazer em te conhecer \033[4;32;40m{nome[0]}\033[m.
Seu primeiro nome è \033[4;32;40m{nome[0]}\033[m.
Seu último nome é \033[4;32;40m{nome[-1]}\033[m.
""")
