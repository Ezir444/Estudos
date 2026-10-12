#Faça um algoritimo que leia o preço de um produto e mostre o novo preço, com 5% de desconto.
try:
    preco = float(input("Digite o preço do produto: "))
    if preco <= 0:
        print("Preço inválido")
    else:
        print(f"O preço do produto de {preco} tera um desconto de {preco*5/100:.2f}")
except ValueError:
    print("Digite um número válido")