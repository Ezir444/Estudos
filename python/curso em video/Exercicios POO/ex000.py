#Criar uma classe Funcionari, onde podemos cadastrar, nome,setor e cargo. Um métódo também que permita que os fúncionarios se apresentem
class Funcionario:
    #Atributos de classe
    empresa = "Sbt Ltda" #para chamar --> Funcionario.empresa
    def __init__(self,nome,setor,cargo):
        #Atributos de Instância
        self.nome = nome
        self.setor =setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Oi meu nome é {self.nome}, sou do setor {self.setor} cargo {self.cargo}"
a1 = Funcionario("Gustavo","Administração","Contador")
print(a1.apresentacao())