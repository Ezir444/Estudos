#Crie a classe ControleRemoto, onde é simulado o funcionamento de um controle simples, (botoes de canal,volume e liga/desliga)
from rich import print
from rich.panel import Panel

tela = Panel("Teste 123 ",title="Titulo", style='red' ,width=40)
desligado = Panel(":+1:")
class Controleremoto():
    def __init__(self,ligar=False):
        self.ligar = False

print(desligado)