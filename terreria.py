import pygame
import sys

pygame.init()

size = wight, height = 1250, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption('terraria')

#тектуры
player_right=pygame.image.load("terorrist r.png")
player_left=pygame.image.load("terorrist l.png")

# player
player_img = player_right
player_img = pygame.transform.scale(player_img,(90,90))
player_rect = player_img.get_rect(center=(wight // 2, height // 2))
player_sprint = 2
player_basic_speed = 1
player_speed = player_basic_speed
print(player_rect)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_rect.top>0:
            player_rect.y -= player_speed
    if keys[pygame.K_s]:
        if player_rect.bottom<height:
            player_rect.y += player_speed
    if keys[pygame.K_a]:
        if player_rect.left>0:
            player_rect.x -= player_speed
            player_img=pygame.transform.scale(player_left,(90,90))
    if keys[pygame.K_LSHIFT]:
        player_speed=player_sprint
    else:
        player_speed=player_basic_speed
    if keys[pygame.K_d]:
        if player_rect.right<wight:
            player_rect.x += player_speed
            player_img=pygame.transform.scale(player_right,(90,90))

    screen.fill((8, 239, 255))
    screen.blit(player_img, player_rect)

    pygame.display.flip()
    clock.tick(120)


pygame.quit()
sys.exit()
