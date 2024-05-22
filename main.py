import pygame
from sys import exit

display = pygame.display
clock = pygame.time.Clock()

pygame.init()
screen = display.set_mode((800, 400))
display.set_caption("Forbidden Dynasty")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    display.update()
    clock.tick(60)
