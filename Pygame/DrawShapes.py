import pygame

pygame.init()

width, height = 1280, 720
window  = pygame.display.set_mode((width, height))
pygame.display.set_caption("desenhos")

clock = pygame.time.Clock()
fps = 30

inGame = True

while inGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            pygame.quit()
            continue

        yellow, green, blue, white = (255, 255, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)
        window.fill(green)

        pygame.draw.polygon(window, yellow, 
                            ((0, int(height/2)),
                             (int(width/2), 0),
                             (width, int(height/2)),
                             (int(width/2), height)))
        pygame.draw.circle(window, blue, (width/2, height/2), height/3)

        pygame.display.update()

        clock.tick(fps)