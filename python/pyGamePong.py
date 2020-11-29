import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()

# sets screen dimensions
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# defines elements
ball = pygame.Rect(screenWidth//2 - 15, screenHeight//2 - 15, 30, 30)
paddle1 = pygame.Rect(screenWidth - 20, screenHeight // 2 - 70, 10, 120)
paddle2 = pygame.Rect(10, screenHeight//2 - 70, 10, 120)

bgColor = pygame.Color('grey12')
grey = (200, 200, 200)

# sets ball speeds
ballSpeedX = 7
ballSpeedY = 7

# sets a 'speed' for each player
paddle1Speed = 0
paddle2Speed = 0

# sets a score for each player and defines values for counters
player1 = 0
player2 = 0
instrFontSize = 24
instrFont = pygame.font.SysFont("Arial", instrFontSize)


def restartBall():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth // 2, screenHeight // 2)
    ballSpeedY *= random.choice((1, -1))
    ballSpeedX *= random.choice((1, -1))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # detects down/up arrow key press for first player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # decrease paddle y axis
                paddle1Speed -= 7
            if event.key == pygame.K_DOWN:
                # increase paddle y axis
                paddle1Speed += 7
        # detects w/s key press for second player
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle1Speed += 7
            if event.key == pygame.K_DOWN:
                paddle1Speed -= 7

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle2Speed -= 7
            if event.key == pygame.K_s:
                paddle2Speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle2Speed += 7
            if event.key == pygame.K_s:
                paddle2Speed -= 7

    # sets ball velocity
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    paddle1.y += paddle1Speed
    paddle2.y += paddle2Speed

    # makes ball bounce off paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ballSpeedX *= -1

    # reflects ball and assigns points
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0:
        restartBall()
        player1 += 1
    if ball.right >= screenWidth:
        restartBall()
        player2 += 1

    # draws elements
    screen.fill(bgColor)
    pygame.draw.rect(screen, grey, paddle1)
    pygame.draw.rect(screen, grey, paddle2)
    pygame.draw.rect(screen, grey, ball)
    pygame.draw.aaline(screen, grey, (screenWidth//2, 0),
                       (screenWidth//2, screenHeight))

    # draws the player scores to the screen
    player1Score = instrFont.render(f"{player1}", False, grey,)
    screen.blit(player1Score, (430, 40))
    player2Score = instrFont.render(f"{player2}", False, grey,)
    screen.blit(player2Score, (360, 40))

    pygame.display.flip()
    # ensures consistent speed
    clock.tick(60)
