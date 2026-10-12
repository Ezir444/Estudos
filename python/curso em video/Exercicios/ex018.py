#Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
try:
    comprimento = int(input("Digite o comprimento do cateto oposto: "))
    cateto = int(input("Digite o cateto adjacente: "))
    print(f"A hipótenusa de {comprimento} e do cateto adjacente {cateto} é {math.hypot(comprimento,cateto):.2f}")
except ValueError:
    print("Digite um número válido")