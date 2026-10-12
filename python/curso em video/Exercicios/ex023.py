#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas.
#Quantas letras ao todo (sem considerar os espaços).
#Quantas letras tem o primeiro nome.

#Uma maneira facil de contar espaços é nome.count(' ')
nome = str(input("Digite seu nome"))
nome_formatado = nome.replace(" ","").strip()
print(f"Seu nome em maiúsculas é {nome.upper()}\nSeu nome em minúsculas é {nome.lower()}\nPossui ao todo {len(nome_formatado)} letras\nA primeira letra possui {len(nome.split()[0])} letras")