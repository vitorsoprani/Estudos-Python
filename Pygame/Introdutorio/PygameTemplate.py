"""
Estrutura básica de desenvolvimento usando pygame:
    Import
    Inicialização
    Criação de uma janela
    Inicialização do clock (definição de um frame-rate)

    Loop
        Detecta eventos
            if quit
                quit pygame
        Logica
        Atualiza a janela (desenha)
        Set FPS
        teste
"""

#Import
import pygame

#inicialização
pygame.init()

#Create Window
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("teste")

#inicializando o clock
fps =  30
clock = pygame.time.Clock()

#loop principal
inGame = True

while inGame:
    #get event

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            pygame.quit()

    #Logica
    window.fill((255, 255, 255))

    #atualização do display
    pygame.display.update()

    #set fps
    clock.tick(fps)
