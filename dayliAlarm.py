#Alert de horarios Especiais
import pygame
import os
from datetime import datetime
# Inicializando o PyGame
pygame.init()

while (1):
    datahora = datetime.now()
    datahoratext = datahora.strftime('%d/%m/%Y %H:%M:%S')
    horatext = datahora.strftime('%H:%M:%S')
    #print(horatext)
    
    #AVISO DE START DE LINHA 5 MIN
    if(horatext == '06:50:00'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('bell.mp3'):
            pygame.mixer.music.load('bell.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
                datahora = datetime.now()
                datahoratext = datahora.strftime('%d/%m/%Y %H:%M:%S')
                horatext = datahora.strftime('%H:%M:%S')
                if(horatext == "06:50:07"):
                    pygame.mixer.music.stop()
                print(horatext)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')
    #Aviso dos 5 min        
    if(horatext == '06:50:08'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('1.1.mp3'):
            pygame.mixer.music.load('1.1.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
                print("Aviso")
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')
    #NUSICA DE 5S
    if(horatext == '06:50:16'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('Zora.mp3'):
            pygame.mixer.music.load('Zora.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
                datahora = datetime.now()
                datahoratext = datahora.strftime('%d/%m/%Y %H:%M:%S')
                horatext = datahora.strftime('%H:%M:%S')
                if(horatext == "06:54:00"):
                    pygame.mixer.music.stop()
                #print(horatext)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')
     
    #Aviso de 1 min
     
    if(horatext == '06:54:01'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('1.2.mp3'):
            pygame.mixer.music.load('1,2.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')
    #marcacao de 5 segundos
    
    if(horatext == '06:54:54'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('5seconds.mp3'):
            pygame.mixer.music.load('5seconds.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')
    
    #Som da Sirene
    
    if(horatext == '06:55:00'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('sirene.mp3'):
            pygame.mixer.music.load('sirene.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')
    
    
    if(horatext == '13:59:47'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('bell.mp3'):
            pygame.mixer.music.load('bell.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
                datahora = datetime.now()
                datahoratext = datahora.strftime('%d/%m/%Y %H:%M:%S')
                horatext = datahora.strftime('%H:%M:%S')
                if(horatext == "13:59:54"):
                    pygame.mixer.music.stop()
                print(horatext)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')
    #Aviso dos 5 min        
    if(horatext == '13:59:54'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('2.1.mp3'):
            pygame.mixer.music.load('2.1.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
                print("Aviso")
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')
    #NUSICA DE 5S
    if(horatext == '14:00:00'):
        
    # Carregando o arquivo MP3 e executando
        if os.path.exists('Zora.mp3'):
            pygame.mixer.music.load('Zora.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(1)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
                datahora = datetime.now()
                datahoratext = datahora.strftime('%d/%m/%Y %H:%M:%S')
                horatext = datahora.strftime('%H:%M:%S')
                if(horatext == "14:02:00"):
                    pygame.mixer.music.stop()
                print(horatext)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')