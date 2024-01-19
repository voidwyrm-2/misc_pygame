# Pong game using python pygame
# Created by Nuclear Pasta

import pygame
from random import randint




# initialize game
pygame.init()

# creating a screen
windratio = 800, 800
screen = pygame.display.set_mode(windratio)  # passing width and height
screen.fill("black")
pygame.display.flip()
# title and icon
pygame.display.set_caption("Screensaver")
icon = pygame.image.load('icons/screensaver-icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)

gameticks = 0
showTicks = False

oneRadius = False
defRadius = 10
minRadius = 5
maxRadius = 20

initX = 20
initY = 20
balls = 30
ballRadius = []

# defining our balls
ballInfo = []
minBallSpeed = 1
maxBallSpeed = 4
ballColor = []
ballX = []
ballY = []
bChangedX = []
bChangedY = []

def ball(x, y, color): ballInfo.append(pygame.draw.circle(screen, color, (x, y), ballRadius[i]))

for i in range(balls): ballX.append(initX); ballY.append(initY)

for i in range(balls): bChangedX.append(randint(minBallSpeed, maxBallSpeed)); bChangedY.append(randint(minBallSpeed, maxBallSpeed))

for i in range(balls): ballColor.append((randint(10, 255), randint(10, 255), randint(10, 255)))

for i in range(balls):
    if oneRadius: ballRadius.append(defRadius)
    else: ballRadius.append(randint(minRadius, maxRadius))


def showticks(x, y):
    tick = mainfont.render(f'tick:{gameticks}', True, (255, 255, 255))
    screen.blit(tick, (x, y))

running = True
while running:
    screen.fill((0, 0, 0)) #background
    for i in range(balls):
        if bChangedX[i] == bChangedY[i]:
            bChangedX[i] = randint(minBallSpeed, maxBallSpeed)
            bChangedY[i] = randint(minBallSpeed, maxBallSpeed)

    #poll for events
    #pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
                #print("you preesed a key")
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: running = False

    #balls movement
    for i in range(balls):
        ballX[i] += bChangedX[i]
        ballY[i] += bChangedY[i]
    #restricting the balls inside the window
    for i in range(balls):
        if ballX[i] <= 0 + ballRadius[i]:
            ballX[i] = 0 + ballRadius[i]
            if '-' in str(bChangedX[i]):
                #print(f'found "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = randint(minBallSpeed, maxBallSpeed)
            else:
                #print(f'didn\'t find "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = -(randint(minBallSpeed, maxBallSpeed))

        elif ballX[i] >= windratio[0] - ballRadius[i]:
            ballX[i] = windratio[0] - ballRadius[i]
            if '-' in str(bChangedX[i]):
                #print(f'found "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = randint(minBallSpeed, maxBallSpeed)
            else:
                #print(f'didn\'t find "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = -(randint(minBallSpeed, maxBallSpeed))
    
        if ballY[i] <= 0 + ballRadius[i]:
            ballY[i] = 0 + ballRadius[i]
            if '-' in str(bChangedY[i]):
                #print(f'found "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = randint(minBallSpeed, maxBallSpeed)
            else:
                #print(f'didn\'t find "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = -(randint(minBallSpeed, maxBallSpeed))
        elif ballY[i] >= windratio[1] - ballRadius[i]:
            ballY[i] = windratio[1] - ballRadius[i]
            if '-' in str(bChangedY[i]):
                #print(f'found "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = randint(minBallSpeed, maxBallSpeed)
            else:
                #print(f'didn\'t find "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = -(randint(minBallSpeed, maxBallSpeed))

    for i in range(balls): ball(ballX[i], ballY[i], ballColor[i])

    clock.tick(60)

    if showTicks: showticks(0, 0)
    pygame.display.update()
    gameticks += 1