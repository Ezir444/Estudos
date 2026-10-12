#Crie a classe Produto,onde podemos cadastrar nome e preço, crie também um métódo que mostra uma etiqueta de preço no produto.
class Produto():
    def __init__(self,nome=None,preco=None):
        if nome and preco == None:
            return "Nenhum produto registrado"
        else:
            self.nome = nome
            self.preco = preco

    def etiqueta(self):
        return f"{"_"*10}Produto{"_"*10} \n{" "*10}{self.nome}{" "*10}\n{"-"*30}\n {"-"*10} {self.preco} {"-"*10}"

a1 = Produto(nome="Moto x Pró",preco=10.99)
print(a1.etiqueta())