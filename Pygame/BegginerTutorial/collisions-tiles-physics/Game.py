import pygame, sys

clock = pygame.time.Clock()

pygame.init()

SCREEN_SIZE = (600, 400)

screen = pygame.display.set_mode(SCREEN_SIZE)

display = pygame.Surface((300, 200)) # Menor que a resolução do jogo e será aumentado depois para que as pixel arts não fiquem minusculas.

pygame.display.set_caption('Movendo coisas pulando e colidindo')


player_img = pygame.image.load('./images/player.png')
player_img.set_colorkey("white") # Deixa transparente as parte sbrancas
player_rect = pygame.Rect(50, 50, player_img.get_width(), player_img.get_height())

grass_image = pygame.image.load('./images/grass.png')
dirt_image = pygame.image.load('./images/dirt.png')

TILE_SIZE = 16

tiles = [dirt_image, grass_image]


plataform_1 = pygame.Rect(100, 100, 100, 100)

# Maoeamento dos tiles do nosso mapa, depois será usado arquivos de texto.
game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

def collision_test(rect, tiles):
    hit_list = []

    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
        

    return rect, collision_types

moving_right = False
moving_left = False

player_y_momentum = 0
air_timer = 0
while True:
    display.fill((146, 244, 255))

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile != '0':
                display.blit(tiles[int(tile) - 1], (x * TILE_SIZE, y * TILE_SIZE))
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    

    
    if player_rect.x > display.get_width():
        player_rect.x = - player_img.get_width()
    if player_rect.x < - player_img.get_width():
        player_rect.x = display.get_width()
    
    player_movement = [0, 0]
    
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
     
    if player_y_momentum <= 7:
        player_y_momentum += 0.5
    
    player_rect, collisions = move(player_rect, player_movement, tile_rects)
    if collisions['bottom'] == True:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1
    
    if collisions['top'] == True:
        player_y_momentum = 0


    display.blit(player_img, (player_rect.x, player_rect.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_UP:
                if air_timer < 6:
                    player_y_momentum = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False

    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), (0, 0)) # "Printa" o nosso display aumentado na tela do jogo
    pygame.display.update()
    clock.tick(60)