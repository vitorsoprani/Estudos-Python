import pygame

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("teste textos")

fps = 30
clock = pygame.time.Clock()

inGame = True
while inGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            pygame.quit()
    
    window.fill((255, 255, 255))
    
    font = pygame.font.Font('./Resources/fontes/PressStart2P-Regular.ttf', 50)
    text = font.render("Teste de texto", False, (0, 0, 0))
    window.blit(text, (300, 300))
    
    pygame.display.update()

    clock.tick(fps)
