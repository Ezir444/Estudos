#Crie uma classa chamada Gamer, onde podemos cadastrar nome, nick e jogos favoritos da pessoa 
# Crie também uma método para mostrar uma ficha desse gamer
from rich import print
class Gamer():
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def adicionar(self,jogos):
        self.jogos.append(jogos)

    def listar(self):
        lista_jogos ="\nx".join(self.jogos)
        return f"[red]Nome:[\] {self.nome}, Nick: {self.nick} \nJogos favoritos \nx{lista_jogos} "
a = Gamer("Pedro","Angilas")
a.adicionar("Call of dutty")
a.adicionar("Far cry")
a.adicionar("Silent hill")
print(a.listar())
         