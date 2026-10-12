#Faça um programa que leia um número inteiro e mostre na tela sua tabuada 
operadores = ["+","-","*","/"]
try:
    num = int(input("Digite um numero: "))
    tabuada = input("Digite o operador +,-,/,*")

    if tabuada not in operadores or num < 0:
        print("Número invalido ou tabuada inválida")

    elif tabuada == "*":
        i = 1
        for i in range(1,11):
            print(f"{i} {tabuada} {num} = {num*(i)}")

    elif tabuada == "+":
        i = 1
        for i in range(1,11):
            print(f"{i} {tabuada} {num} = {num+(i)} ")

    elif tabuada == "-":
        i = 1
        for i in range(1,11):
            print(f"{num} {tabuada} {num} = {num-(i)} ")

    elif tabuada == "/":
        print(f"Tabuado do {num}")
        i = 1
        for i in range(1,11):
            print(f"{num} {tabuada} {i} = {num/(i)} ")

except ValueError:
    print("Digite um numero válido")