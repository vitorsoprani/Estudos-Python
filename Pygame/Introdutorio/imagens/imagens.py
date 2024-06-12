import pygame

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Teste imagens")

clock = pygame.time.Clock()
fps = 30

# carregando imagens
# o .convert() transforma a imagagem para um formato que melhora a performance
background = pygame.image.load("./Resources/background.jpg").convert()
# para png usamos ".convert_alpha()"
pythonLogo = pygame.image.load("./Resources/python.png").convert_alpha()

inGame = True
while inGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            pygame.quit()

    window.blit(background, (0, 0))
    window.blit(pythonLogo, (200, 300))

    pygame.display.update()

    clock.tick(fps)
