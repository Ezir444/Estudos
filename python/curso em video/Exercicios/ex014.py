#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
AUMENTO = 15
try:
    
    salario = float(input("Digite o salário do colaborador: "))
    if salario <= 0:
        print("Digite um sálario válido")
    else:
        print(f"O colaborador tera um novo sálario de {salario*AUMENTO/100+salario:.2f} o aumento foi de {salario*AUMENTO/100:.2f}, salario era de {salario:.2f}")

except ValueError:
    print("Digite um sálario válido")
