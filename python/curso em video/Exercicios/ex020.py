#Um professor quer sortear um dos seus quatro alunos para apagr um quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
loop = 0
lista = []
while loop < 4:
    loop += 1
    aluno = input("Digite o nome do aluno: ")
    lista.append(aluno)
print(f"O aluno {random.choice(lista)} foi o premiado para apagar o quadro")