import pygame, sys

clock = pygame.time.Clock()

pygame.init()

SCREEN_SIZE = (600, 400)

screen = pygame.display.set_mode(SCREEN_SIZE)

display = pygame.Surface((300, 200)) # Menor que a resolução do jogo e será aumentado depois para que as pixel arts não fiquem minusculas.

pygame.display.set_caption('Movimento de camera')

# Objetos do jogador:
player_img = pygame.image.load('./images/player.png')
player_img.set_colorkey("white") # Deixa transparente as parte sbrancas
player_rect = pygame.Rect(50, 50, player_img.get_width(), player_img.get_height())

# Objetos do cenário:
TILE_SIZE = 16
grass_image = pygame.image.load('./images/grass.png')
dirt_image = pygame.image.load('./images/dirt.png')
tiles = [dirt_image, grass_image]

# Carregando o mapeamento dos tiles do nosso mapa
def load_map(path):
    f = open(path+'.txt', 'r')
    data = f.read()
    f.close

    data = data.split('\n')

    game_map = []
    for row in data:
        game_map.append(list(row))
    
    return game_map


def collision_test(rect, tiles):
    hit_list = []

    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    
    # Move o nosso objeto temporariamente para checar se houve colisão horizontal.
    #   Caso haja colisão, "acopla" os lados que colidiram.
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    
    # Anaálogo ao processo explicado acima, porém levando em conta movimentos verticais.
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
        
    # Retorna o nosso objeto movido e as colisões que ocorreram.
    return rect, collision_types

# Variaveis de movimento do jogador
moving_right = False
moving_left = False
    # Variáveeis da física:
player_y_velocity = 0
player_x_velocity = 4
gravity = 0.6
air_timer = 0

# Variável do movimento de câmera:
scroll = [0, 0]

# Carregando o mapa:
game_map = load_map('./map')

while True:
    # Preenchendo o background
    display.fill((146, 244, 255))
    
    scroll[0] += (player_rect.x - scroll[0] - 147)/10
    scroll[1] += (player_rect.y - scroll[1] - 92)/10

    
    # Montando o mapa através dos tiles.
    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile != '0':
                display.blit(tiles[int(tile) - 1], ((x*TILE_SIZE) - int(scroll[0]), (y * TILE_SIZE) - int(scroll[1])))
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    

    # # Faz o player "dar a volta" na tela.    
    # if player_rect.x > display.get_width() - 1:
    #     player_rect.x = - player_img.get_width() + 1
    # if player_rect.x < - player_img.get_width() - 1:
    #     player_rect.x = display.get_width() - 1
    
    # Inicializa o array de movimentos com 0, 0;
    player_movement = [0, 0]
    
    player_movement[0] = (moving_right - moving_left) * player_x_velocity
    player_movement[1] = player_y_velocity
    
    if player_y_velocity <= 7:
        player_y_velocity += gravity
    
    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom'] == True:
        player_y_velocity = 0
        air_timer = 0
    else:
        air_timer += 1
    
    if collisions['top'] == True:
        player_y_velocity = 0


    display.blit(player_img, (player_rect.x - int(scroll[0]), player_rect.y - int(scroll[1])))


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
                    player_y_velocity = -15*gravity
                    air_timer = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False

    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), (0, 0)) # "Printa" o nosso display aumentado na tela do jogo
    pygame.display.update()
    clock.tick(60)