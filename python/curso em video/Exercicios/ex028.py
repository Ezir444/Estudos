#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana maria de souza
#primeiro = Ana, último = Souza
nome = input("Digite o nome completo: ")
separar = nome.split()
quantidade_palavras = len(separar)
if quantidade_palavras >= 2:
    print(f"A primeira palavra é {separar[0]} e a ultima é {separar[quantidade_palavras-1]}")
else:
    print("O nome é muito curto")