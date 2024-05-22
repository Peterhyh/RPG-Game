import pygame
from sys import exit

pygame.init()
display = pygame.display
clock = pygame.time.Clock()

screen = display.set_mode((800, 400))
display.set_caption("Forbidden Dynasty")

surface = pygame.Surface((100, 200))
surface.fill("Red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface, (0, 0))
    display.update()
    clock.tick(60)
