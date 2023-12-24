import pygame
import sys
import random


pygame.init()

screen = pygame.display.set_mode((1000, 800))
a = 0
for y in range(50):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    s = pygame.Rect(a, 0, 10, 800)
    pygame.draw.rect(screen, (r, g, b), s, 1)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    de = pygame.Rect(0, a, 1000, 10)
    pygame.draw.rect(screen, (r, g, b), de, 1)
    a = a + 20
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()