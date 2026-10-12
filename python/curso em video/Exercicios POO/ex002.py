#Crie a classe Churrasco, onde é possivel informar quantidade de pessoas e calcular quanto de carne a ser comprada e custo total por pessoa.
#Considerando
#Consumo padrão : 400 g por pessoa
#Preço : R$82,40/Kg

class Churrasco():
    def __init__(self,qunatidade_pessoas=int):
        self.pessoas = qunatidade_pessoas

    def calculo_consumo(self):
        consumo_padrao = 400
        preco = 82.40
        quantidade_carne = self.pessoas * consumo_padrao
        consumo_em_kg = quantidade_carne/1000
        custo_total = consumo_em_kg * preco
        return f"Churrasco do Pedrão quantidade de pessoas {self.pessoas}\nSera nessario um total de {consumo_em_kg}kg de carne\nCusto por pessoa: {custo_total/self.pessoas}kg\nCusto total: {custo_total:.2f}"

a1 = Churrasco(qunatidade_pessoas=100)
print(a1.calculo_consumo())