#Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule sua área  e quantidade de tinta necessária para pintá-la
#Sabendo que cada litro de tinta, pinta uma área de 2m2

QUANTIDADE_POR_LITRO = 2
try:
    altura = float(input("Digite a altura da parede: "))
    largura = float(input("Digite a largura da parede "))
    if altura <= 0 or largura <= 0:
        print("Largura e altura não podem ser negativos ou zero")
    else:
        print(f"A área total é {altura*largura:.2f}m2 e área que pode-se pintar {(altura*largura)/QUANTIDADE_POR_LITRO:.2f}")
except ValueError:
    print("Digite um numéro válido")