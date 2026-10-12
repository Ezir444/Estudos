#Faça um programa que leia um ângulo qualquer e mostre o o valor do seno, cosseno e tangente desse ângulo.
from math import radians,sin,cos,tan
try:
    num = int(input("Digite o ângulo: "))
    seno = sin(radians(num))
    print(f"O ângulo {num} possui um seno de {seno:.2f}")
    cosseno = cos(radians(num))
    tangente = tan(radians(num))
    print(f"O cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}")
except ValueError:
    print("Digite um número válido")