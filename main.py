import pygame
from sys import exit

pygame.init()
display = pygame.display
clock = pygame.time.Clock()

screen = display.set_mode((1404, 716))
display.set_caption("Dynasty")

background_surface = pygame.image.load("images/background.png").convert()
character_surface = pygame.image.load("images/blob.png").convert_alpha()
attack_blob_surface = pygame.image.load(
    "images/attackBlob.png").convert_alpha()
attack_blob_surface_rect = attack_blob_surface.get_rect(topleft=(1000, 475))

attack_blob_right_surface = pygame.image.load(
    "images/attackBlobRight.png").convert_alpha()
attack_blob_right_surface_rect = attack_blob_right_surface.get_rect(
    topleft=(800, 475))

moveLeft = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))

    if moveLeft == True:
        screen.blit(attack_blob_surface, attack_blob_surface_rect)
        attack_blob_surface_rect.x -= 2
    else:
        screen.blit(attack_blob_right_surface, attack_blob_right_surface_rect)
        attack_blob_right_surface_rect.x += 2

    if attack_blob_surface_rect.x == 800:
        attack_blob_surface_rect.x = 1000
        moveLeft = False
    elif attack_blob_right_surface_rect.x == 1000:
        attack_blob_right_surface_rect.x = 800
        moveLeft = True

    screen.blit(character_surface, (100, 475))
    display.update()
    clock.tick(60)
