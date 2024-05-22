import pygame
from sys import exit

pygame.init()
display = pygame.display
clock = pygame.time.Clock()

screen = display.set_mode((1404, 716))
display.set_caption("Forbidden Dynasty")

background_surface = pygame.image.load("images/background.png")
character_surface = pygame.image.load("images/blob.png")

# surface = pygame.Surface((100, 200))
# surface.fill("Red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # screen.blit(surface, (200, 100))
    screen.blit(background_surface, (0, 0))
    screen.blit(character_surface, (100, 475))
    display.update()
    clock.tick(60)
