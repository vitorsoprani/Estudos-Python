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
cat = pygame.transform.rotozoom(cat, 0, 0.05)
rectCat = cat.get_rect()
xVelocity = 2
yVelocity = 2

rectNew = pygame.Rect(500, 0, 200, 200)
bottom = pygame.Rect(-5, height, width + 10, 5)
top = pygame.Rect(-5, -5, width + 10, 5)
left = pygame.Rect(-5, -5, 5, height + 10)
right = pygame.Rect(width, - 5, 5, height + 10)


inGame = True
while inGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            pygame.quit

    if rectCat.colliderect(bottom) or rectCat.colliderect(top):
        yVelocity = -yVelocity

    if rectCat.colliderect(left) or rectCat.colliderect(right):
        xVelocity = -xVelocity

    rectCat.y += yVelocity
    rectCat.x += xVelocity

    window.blit(backgroundImage, (0, 0))

    window.blit(cat, rectCat)

    pygame.display.update()

    clock.tick(fps)
