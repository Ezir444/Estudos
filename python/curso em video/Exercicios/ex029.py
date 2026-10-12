#Escreva um programa que faça um computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
numero_aleatorio = randint(0,5)
num = int(input("Digite um número de 0 a 5 :"))
if num == numero_aleatorio:
    print(f"Parabéns o numero aleatório era {numero_aleatorio}")
else:
    print(f"Você errou o número aleatório era {numero_aleatorio}")
