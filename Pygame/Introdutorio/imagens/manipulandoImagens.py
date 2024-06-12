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
# pythonLogo = pygame.transform.rotate(pythonLogo, 90) # pode deixar borrado
# rotaciona e escalona suavemente:
pythonLogo = pygame.transform.rotozoom(pythonLogo, 90, 0.5)
# pythonLogo = pygame.transform.flip(pythonLogo, False, True)


inGame = True
while inGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            pygame.quit()

    # pythonLogo = pygame.transform.scale(pythonLogo, (100, 100)) #deixa borrado
    # não deixa borrado:
    # pythonLogo = pygame.transform.smoothscale(pythonLogo, (100, 100))

    window.blit(background, (0, 0))
    window.blit(pythonLogo, (0, 0))

    pygame.display.update()

    clock.tick(fps)
