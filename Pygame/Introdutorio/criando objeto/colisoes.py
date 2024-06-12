'''
Rect
    usado para detectar colisões
    usado para acessar x e y

    formas de criar:
        1. pygame.Rect(x, y, width, height) #(r maiúsculo!!!)

        #caso ja tenhamos nossa imagem, podemos fazer:

        2.surface.get_rect() #cria um retangulo em volta de uma imagem/superficie
'''

import pygame

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Retangulo")

fps = 30
clock = pygame.time.Clock()

backgroundImage = pygame.image.load("./Resources/background.jpg").convert()
cat = pygame.image.load("./Resources/cat.png").convert_alpha()
cat = pygame.transform.rotozoom(cat, 0, 0.1)
rectCat = cat.get_rect()

rectNew = pygame.Rect(500, 0, 200, 200)


inGame = True
while inGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            pygame.quit

    print(rectCat.colliderect(rectNew))
    rectCat.x += 5

    window.blit(backgroundImage, (0, 0))

    # pygame.draw.rect(window, (255, 0, 0), rectCat)
    # pygame.draw.rect(window, (255, 0, 0), rectNew)
    window.blit(cat, rectCat)

    pygame.display.update()

    clock.tick(fps)
