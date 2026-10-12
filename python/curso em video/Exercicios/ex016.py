#Escreva um programa que pergunte a quantidade de dias percorridos por um carro alugado e a quantidade de dias que foi alugado
#Calcule o preço a pagar, sabendo que cada dia custa R$60 por dia e R$0,15 por Km rodado
ALUGUEL_DIA = 60
KM_DIA = 0.15
try:
    km = float(input("Digite a quantidade de km percorridos: "))
    dia = int(input("Informe a quantidade de dias alugado: "))
    print(f"O valor referente ao dias alugados foi {dia*ALUGUEL_DIA:.2f} e de km percorridos é {km*KM_DIA:.2f}\nO valor total a ser pago è {(dia*ALUGUEL_DIA)+(km*KM_DIA):.2f}")
except ValueError:
    print("Digite um número válido")