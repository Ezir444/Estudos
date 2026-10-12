#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Digite o nome: "))
if "SILVA" in nome.upper():
    print("O nome contém silva")
else:
    print("O nome não contém silva")