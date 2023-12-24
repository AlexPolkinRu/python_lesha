import pygame
import sys
import random
import time

shirina = 800
visota = 800

pygame.init()

screen = pygame.display.set_mode((shirina, visota))
screen.fill('white')


def nine_circles():
    krugov_v_stolbike = random.randint(1, 10)
    krugov_v_strochke = random.randint(1, 10)

    rastoyanie_po_y = visota / krugov_v_stolbike
    rastoyanie_po_x = shirina / krugov_v_strochke
    x = shirina / krugov_v_strochke / 2
    y = visota / krugov_v_stolbike / 2
    radius = visota / krugov_v_stolbike / 2
    for i in range(krugov_v_stolbike):
        for j in range(krugov_v_strochke):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pygame.draw.circle(screen, (r, g, b), (x, y), radius, width=0)
            x = x + rastoyanie_po_x
        y = y + rastoyanie_po_y
        x = shirina / krugov_v_strochke / 2


while True:

    nine_circles()
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
