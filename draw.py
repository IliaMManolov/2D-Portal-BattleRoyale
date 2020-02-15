import pygame

background = pygame.Surface((640, 480))
background.fill(pygame.Color("white"))

font = pygame.font.Font('Fonts/Vera.ttf', 32) 
startGame = font.render("Start game", True, pygame.Color("black"))
startGameRect = startGame.get_rect()
startGameRect.center = (320, 160)

quitGame = font.render("Quit!", True, pygame.Color("black"))
quitGameRect

def draw(gameState):
    global background
    gameState["screen"].blit(background, (0, 0)) # clear the screen with the black rectangle

    
    pygame.display.flip()

