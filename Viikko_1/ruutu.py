"""
Minimaalinen pygame-esimerkki, joka piirtää tyhjän
Hello World! -nimisen ikkunan.
"""
import pygame, sys
from pygame.locals import *

# Alustaa ikkunan
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')

# Tehdään taustasta mukavan pinkki
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 102, 204))


# Main-loop, joka sallii ikkunan sulkemisen
while True:
    for event in pygame.event.get():
        # QUIT-tapahtuma lähetetään ohjelmalle, kun käyttäjä painaa
        # ikkunan yläkulman rastia.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Piirretään ikkuna
    screen.blit(background, (0,0))
    pygame.display.update()
