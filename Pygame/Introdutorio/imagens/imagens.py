import pygame

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Teste imagens")

clock = pygame.time.Clock()
fps = 30

inGame = True
while inGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            pygame.exit()

    window.fill((255, 255, 255))
    pygame.display.update()

    clock.tick(fps)
