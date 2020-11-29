import pygame
import random

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))

# button variables:
bWidth = 150
bHeight = 100
bColor = (0, 255, 0)
bPosX = (width - bWidth) // 2
bPosY = (height - bHeight) // 2
bFontSize = 18
bFont = pygame.font.SysFont("Arial", bFontSize)
instrFontSize = 24
instrFont = pygame.font.SysFont("Arial", instrFontSize)
buttonOnOff = 0

# game state
inMenu = 0
inPlay = 1
inEnd = 2
gameState = inMenu

bgCol = (255, 255, 255)

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    mouse = pygame.mouse.get_pos()
    # if the mouse is over the button
    if mouse[0] > bPosX and mouse[0] < bPosX + bWidth:
        if mouse[1] > bPosY and mouse[1] < bPosY + bHeight:
            # if the mouse has been clicked!
            if pygame.mouse.get_pressed()[0]:
                if gameState == inMenu:
                    gameState = inPlay
                elif gameState == inPlay:
                    # makes button blue and ends game
                    bColor = (0, 0, 255)
                    # makes button progressively smaller
                    bWidth, bHeight = bWidth - 3, bHeight - 3
                    # changes button color each click
                    if buttonOnOff == 0:
                        bColor = (255, 0, 0)
                        buttonOnOff = 1
                    else:
                        bColor = (0, 255, 0)
                        buttonOnOff = 0
                    # when it gets really small, user wins, game ends
                    if bHeight <= 5:
                        gameState = inEnd
                elif gameState == inEnd:
                    gameOver = True
            if not gameState == inMenu:
                bPosX = random.randint(0, width-bWidth)
                bPosY = random.randint(0, height-bHeight)

    screen.fill(bgCol)

    InstrTextSurf = instrFont.render(
        "Click the button to win the game!", True, (0, 0, 0))
    InstrTextRect = InstrTextSurf.get_rect()
    InstrTextRect.center = (width // 2, instrFontSize)
    screen.blit(InstrTextSurf, InstrTextRect)

    if gameState == inMenu:
        bText = "Start game!"
    if gameState == inPlay:
        bText = "Click Me!"
    button = pygame.draw.rect(screen, bColor, (bPosX, bPosY, bWidth, bHeight))
    bTextSurf = bFont.render(bText, True, (0, 0, 0))
    bTextRect = bTextSurf.get_rect()
    bTextRect.center = (bPosX + bWidth // 2, bPosY + bHeight // 2)
    screen.blit(bTextSurf, bTextRect)

    pygame.display.update()

pygame.quit()
quit()
