import pygame, sys

clock = pygame.time.Clock() # Usado para "controlar" o fps

pygame.init() # Inicializa a biblioteca;

pygame.display.set_caption('Hello world') #Configura o titulo da janela

WINDOW_SIZE = (400,400)

screen = pygame.display.set_mode(WINDOW_SIZE) # Cria o objeto do nosso display;

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update() # Atualiza a tela: Será mais importante quando tivermos animações.

    clock.tick(60) # Pausa o programa tempo o suficiente para manter em 60 fps
