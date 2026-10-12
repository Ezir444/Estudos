#faça um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados
#Ex: Digite um número: 1834, unidade:4,dezena:3,centena:8,milhar:1
num = str(input("Digite um número: "))
numero_inteiro = int(num)
if numero_inteiro >= 1000:
    print(f"A unidade: {num[-1]}\ndezena:{num[-2]}\ncentena: {num[-3]}\nmilhar: {num[-4]}")
elif numero_inteiro >= 100:
    print(f"A unidade: {num[-1]}\ndezena: {num[-2]}\ncentena: {num[-3]}")
elif numero_inteiro >= 10:
    print(f"A unidade: {num[-1]}\ndezena: {num[-2]}")
elif numero_inteiro >= 0:
    print(f"A unidade: {num[-1]}")