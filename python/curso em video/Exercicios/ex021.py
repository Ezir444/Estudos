#O mesmo professor anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
lista = []
for i in range(4):
    aluno = input("Digite o nome do aluno: ")
    lista.append(aluno)
print(f"A ordem dos alunos sorteado foi {random.sample(lista)}")