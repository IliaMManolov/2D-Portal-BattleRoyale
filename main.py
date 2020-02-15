import pygame
import random
from init import initGame, initMain
from handleEvents import handleEvents
from update import update
from draw import draw
from pygame.locals import *

def main():
    # initialization
    pygame.init()
    screen = pygame.display.set_mode((640, 480))          # sets the window size
    pygame.display.set_caption('Portal Battle') # sets the titlebar
    # pygame.mouse.set_visible(0)

    clock = pygame.time.Clock()     # get a clock for the main loop

    gameState = initMain({"screen": screen})

    # the main loop
    while gameState["running"]:
        deltaTime = clock.tick()
        handleEvents(gameState)
        update(gameState, deltaTime)
        draw(gameState)

    pygame.quit()

if __name__ == "__main__":
    main()
