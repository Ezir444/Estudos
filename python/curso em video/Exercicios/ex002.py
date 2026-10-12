x = int(input('digite um numero '))
y = int(input('digite outro numero '))
soma = x + y
# print ('A soma entre' , x , '+' , y , 'è' , soma)
print ('a soma entre {} e {} è {}' .format(x, y , soma)) # .format substitui os valores {} dentro de uma string
#Se ambos os valores não forem int os dados vão ser concatenados, exemplo '7'+'4' = 74
