#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez.
nome = str(input("Digite o nome ")).strip()
quantidade_a = nome.count('a')
posicao = nome.lower().find('a')
posicao_2 = nome.lower().rfind('a')
print(f"Quantidade de {"A"} é {quantidade_a}\nEle aparece na primeira vez no indice {posicao}\nAparece a ultima vez no indice {posicao_2}")