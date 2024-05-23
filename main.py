import pygame
from sys import exit

pygame.init()
display = pygame.display
clock = pygame.time.Clock()

screen = display.set_mode((1404, 716))
display.set_caption("Forbidden Dynasty")

background_surface = pygame.image.load("images/background.png").convert()
character_surface = pygame.image.load("images/blob.png").convert_alpha()
attack_blob_surface = pygame.image.load(
    "images/attackBlob.png").convert_alpha()
attack_blob_x_value = 1000
attack_blob_y_value = 475

attack_blob_right_surface = pygame.image.load(
    "images/attackBlobRight.png").convert_alpha()
attack_blob_right_x_value = 800
attack_blob_right_y_value = 475

moveLeft = True

# surface = pygame.Surface((100, 200))
# surface.fill("Red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # screen.blit(surface, (200, 100))
    screen.blit(background_surface, (0, 0))

    if moveLeft == True:
        screen.blit(attack_blob_surface,
                    (attack_blob_x_value, attack_blob_y_value))
        attack_blob_x_value -= 2
    else:
        screen.blit(attack_blob_right_surface,
                    (attack_blob_right_x_value, attack_blob_right_y_value))
        attack_blob_right_x_value += 2

    if attack_blob_x_value == 800:
        attack_blob_x_value = 1000
        moveLeft = False
    elif attack_blob_right_x_value == 1000:
        attack_blob_right_x_value = 800
        moveLeft = True

    screen.blit(character_surface, (100, 475))
    display.update()
    clock.tick(60)
