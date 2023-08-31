import pygame
import sys
import math
import palette



# Initialise pygame

pygame.init()

# Initialise clock

clock = pygame.time.Clock()

# Initialise Screen

WIDTH, HEIGHT = 1920, 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")

# Color Palettes



### Execution ###


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    
    screen.fill(pygame.Color(255, 255, 255))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

print("done")
