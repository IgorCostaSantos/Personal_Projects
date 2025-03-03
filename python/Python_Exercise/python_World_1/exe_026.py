frase = str(input('Digite uma frase: ')).strip().lower()

print(f"""
A letra \033[1;35;40mA\033[m aparece {frase.count('a')} vezes na frase.
A primeira letra \033[1;35;40mA\033[m apareceu na posição {frase.find('a')+1}.
A ultima letra \033[1;35;40mA\033[m apareceu na posição {frase.rfind('a')+1}.
""")
