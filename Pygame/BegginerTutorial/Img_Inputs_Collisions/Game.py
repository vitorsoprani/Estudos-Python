import pygame, sys

clock = pygame.time.Clock()

pygame.init()

SCREE_SIZE = (600, 400)

screen = pygame.display.set_mode(SCREE_SIZE)

pygame.display.set_caption('Movendo coisas pulando e colidindo')

moving_right = False
moving_left = False


player_img = pygame.image.load('./images/cute_cat.png')
player_position = [50,50]
player_y_momentum = 0
player_rect = pygame.Rect(player_position[0], player_position[1], player_img.get_width(), player_img.get_height())

plataform_1 = pygame.Rect(0, 200, 150, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False
    screen.fill("purple")

    if player_y_momentum < 15:
        player_y_momentum += 0.5
    
    if player_position[1] > screen.get_height() - player_img.get_height():
        player_y_momentum = - player_y_momentum
    
    if player_rect.colliderect(plataform_1):
        if player_y_momentum > 0: player_y_momentum = -15
        else: player_y_momentum = 15


    player_position[1] += player_y_momentum

    if player_position[0] > screen.get_width():
        player_position[0] = - player_img.get_width()
    if player_position[0] < - player_img.get_width():
        player_position[0] = screen.get_width() 
    
    if moving_left:
        player_position[0] -= 4
    
    if moving_right:
        player_position[0] += 4

    player_rect.x = player_position[0]
    player_rect.y = player_position[1]

    screen.blit(player_img, player_position)
    pygame.draw.rect(screen,"red", plataform_1)

    pygame.display.update()

    clock.tick(60)