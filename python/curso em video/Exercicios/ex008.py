#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média
try:
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    if nota1 < 0 or nota2 < 0:
        print("Valor inválido")
    else:
        print(f"A média do aluno é {(nota1+nota2)/2}")
except ValueError:
    print("Valor digitado precisa ser um número")