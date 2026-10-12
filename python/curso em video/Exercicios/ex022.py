#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
import pygame
import time
som = {
    "letras" : ['plin plin plon','plin plin plon','plin plon','plin plin plon','plin plin plon','plin plon','plon','plin plon','plin plin plin plon','plin plin plon','plin plon','plin plin plin plon','plin plin plin','plin plin plin plon','plin plin plon','plin plin plin','plin plon','plon'],
                "tempo" : [1,4,7,13,16,18,22,25,26,30,36,38,42,45,50,52.55,58]
}
opcao = input("")
if opcao == "toque plin plin plon":
    pygame.mixer.init()
    pygame.mixer.music.load('gwyn.mp3')
    pygame.mixer.music.play()
    for i in range(60):
        pygame.mixer_music.get_busy()
        print(f'{som["letras"][i]}')
        time.sleep(som['tempo'][i+1] - som['tempo'][i])