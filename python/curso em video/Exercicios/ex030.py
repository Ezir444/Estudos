#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
PERMITIDA = 80
velocidade = int(input("Informe a velocidade do veiculo "))
if velocidade <= PERMITIDA:
    print("Não ultrapassado o limite de velocidade")
else:
    valor_multa = (velocidade - PERMITIDA) * 7
    print(f"Foi ultrapassado {velocidade - PERMITIDA} da velocidade permitida e a multa é {valor_multa}")
