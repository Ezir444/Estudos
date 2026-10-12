#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimitros
try:
    metros = int(input("Digite o valor em metros"))
    print("O valor convertido fica {} centimetros e {} milímetros".format(metros*100, metros*1000))
except ValueError:
    print("Você digitou um valor errado, digite um numero")