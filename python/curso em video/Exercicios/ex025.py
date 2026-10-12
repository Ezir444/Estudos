#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO".
nome = str(input("Digite o nome da cidade: ")).strip()
n = nome.split()[0]
if n.upper() == "SANTO":
    print("A cidade começa com SANTO")
else:
    print("A cidade não começa com SANTO")
