import time
#Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usúario chegou no fim da leitura.
class Livro():
    def __init__(self,titulo:str,quantidade_paginas:int):
        self.titulo = titulo
        self.paginas = quantidade_paginas

    def avancar_paginas(self,paginas_avancadas:int):
        for i in range(paginas_avancadas):
            self.paginas = self.paginas - 1
            print(self.paginas ,end=" ")
            time.sleep(1)
l1 = Livro(titulo="Dostoiesvk",quantidade_paginas=20)
l1.avancar_paginas(paginas_avancadas=10)

#ainda não terminei