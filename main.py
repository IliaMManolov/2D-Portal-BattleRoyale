import pygame
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480))          # sets the window size
pygame.display.set_caption('Portal Battle') # sets the titlebar
# pygame.mouse.set_visible(0)

clock = pygame.time.Clock()     # get a clock for the main loop
running = True                  # and keep account of whether we need to stop

background = pygame.Surface((640, 480))
background.fill(pygame.Color("black"))

def handleEvents():
    global running

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


def update():
    pass

def draw():
    screen.blit(background, (0, 0)) # clear the screen with the black rectangle
    
    pygame.display.flip()

def main():
    # initialization

    # the main loop
    while running:
        deltaTime = clock.tick()
        handleEvents()
        update(deltaTime)
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
