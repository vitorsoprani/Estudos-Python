import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000 - start_time)
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()

game_active = False

start_time = 0

test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('./graphics/Sky.png').convert()
ground_surf = pygame.image.load('./graphics/ground.png').convert()

snail_surf = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# intro:
player_stand = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

last_score = 0
message_surf = test_font.render('Press space to start...', False, (111, 196, 169))
message_rect = message_surf.get_rect(center = (400, 350))

title = test_font.render("Pixel Runner", False, (111, 196, 169))
title_rect = title.get_rect(center = (400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks()/1000)

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen,
        #                 '#c0e8ec',
        #                 pygame.Rect(score_rect.left - 5,
        #                             score_rect.top - 5,
        #                             score_rect.width + 10,
        #                             score_rect.height + 10),
        #                 border_radius=3)    
        # screen.blit(score_surf, score_rect)
        last_score = display_score()

        snail_rect.x -= 4
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # colisoes:
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        last_score_surf = test_font.render(f'Last score: {last_score}', False, (111, 196, 169))
        last_score_rect = last_score_surf.get_rect(center = (400, 350))

        screen.blit(title, title_rect)
        
        if last_score:
            screen.blit(last_score_surf, last_score_rect)
        else:
            screen.blit(message_surf, message_rect)



    pygame.display.update()
    clock.tick(60)
