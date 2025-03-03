n = input('\033[35;40mdigite algo:\033[m ')
print()
print(f"""
É do tipo: {type(n)}
È numerico? {n.isnumeric()}
È uma letra? {n.isalpha()}
È um numero? {n.isalnum()}
È descimal? {n.isdecimal()}
È um digito? {n.isdigit()}
È um nome? {n.isidentifier()}
esta tudo em minusculo? {n.islower()}
pode ser impresso? {n.isprintable()}
É um espaco? {n.isspace()}
É um titulo? {n.istitle()}
esta tudo em maiusculo? {n.isupper()}
""")


