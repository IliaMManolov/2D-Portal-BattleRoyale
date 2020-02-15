import pygame
from pygame.locals import *

def handleEvents(gameState):
    for event in pygame.event.get():
        if event.type == QUIT:
            gameState["running"] = False
    return gameState