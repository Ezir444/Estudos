#Ordem de precedência
#1 - () <-- parenteses
#2 - ** <-- Potência
#3 -*,/,%,// <-- Multiplicação,divisão,divisão inteira e resto
#4 +- Mais e menos
n1 = int(input('digite um numero '))
n2 = int(input('digite outro numero '))
s = n1 + n2    
sub = n1 - n2
mul = n1 * n2
div = n1/n2
pot = n1 ** n2 # Potência
di = n1 // n2 #Pega o inteiro da divisão
r = n1 % n2 #Pega o resto da divisão
print('a soma: {} subtração: {} multiplicação: {} divisão: {} potência: {}\ndivisão inteira: {} , Resto: {}' .format( s , sub , mul , div , pot, di, r ),end=' ')
