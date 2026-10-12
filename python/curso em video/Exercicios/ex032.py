#Desenvolva um programa que pergunte a distância de uma viagem em Km,
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distancia = float(input("informe a distancia em km: "))
if distancia <= 200:
    print(f"O percurso de {distancia}Km sera cobrado {distancia*0.50} de passagem, a taxa por km foi {0.50}")
else:
    print(f"O percurso de {distancia}Km sera cobrado {distancia*0.45} de passagem, a taxa por km foi {0.45}")