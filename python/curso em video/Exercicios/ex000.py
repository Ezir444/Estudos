#Comando simples para mostrar mensagem na tela
loop = 0
msg = "Olá mundo"
while loop < 2:
    loop += 1
    msg = "olá mundo" if loop == 1 else "Oi, tudo bem?"
    print(msg)
