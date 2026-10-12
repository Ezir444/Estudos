#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode compra.
DOLAR = 3.27
try:
    print(f"Cotação atual {DOLAR}")
    num = float(input("Digite o valor em reais a ser convertido: "))
    if num <= 0:
        print(f"Você não pode converter {num} em dólares")
    else:
        print(f"Fazendo a conversão é possivel comprar {num/DOLAR:.2f}US$")
except ValueError:
    print("Digite um numero válido")