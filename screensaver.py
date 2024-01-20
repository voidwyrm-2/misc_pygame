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

shapesPoly = 0
#0 or circles
#1 or squares(NOT WORKING)
#1.1 or fsquares: funny squares
#1.2 or frsquares: funnier squares
#2 or hexagons: hexagons are the bestagons

oneRadius = False
defRadius = 10
minRadius = 5
maxRadius = 20

# A moment of silence for the era when "shapes" was "balls"

initX = 20
initY = 20
shapes = 30
shapesRadius = []

# defining our shapes
shapesInfo = []
minShapesSpeed = 1
maxShapesSpeed = 4
shapesColor = []
shapesX = []
shapesY = []
bChangedX = []
bChangedY = []

def drawshapes(x, y, color):
    if shapesPoly == 0 or shapesPoly == 'circles': shapesInfo.append(pygame.draw.circle(screen, color, (x, y), shapesRadius[i]))

    #elif shapesPoly == 1 or shapesPoly == 'squares': shapesInfo.append(pygame.draw.rect(screen, color, (x, y, x, y)))

    elif shapesPoly == 1.1 or shapesPoly == 'fsquares': shapesInfo.append(pygame.draw.rect(screen, color, (x, y, x + shapesRadius[i], y + shapesRadius[i])))

    elif shapesPoly == 1.2 or shapesPoly == 'frsquares': shapesInfo.append(pygame.draw.rect(screen, color, (x, y, x + shapesRadius[i], y + shapesRadius[i]), shapesRadius[i]))

    else: shapesInfo.append(pygame.draw.circle(screen, color, (x, y), shapesRadius[i]))

for i in range(shapes): shapesX.append(initX); shapesY.append(initY)

for i in range(shapes): bChangedX.append(randint(minShapesSpeed, maxShapesSpeed)); bChangedY.append(randint(minShapesSpeed, maxShapesSpeed))

for i in range(shapes): shapesColor.append((randint(10, 255), randint(10, 255), randint(10, 255)))

for i in range(shapes):
    if oneRadius: shapesRadius.append(defRadius)
    else: shapesRadius.append(randint(minRadius, maxRadius))


def showticks(x, y):
    tick = mainfont.render(f'tick:{gameticks}', True, (255, 255, 255))
    screen.blit(tick, (x, y))

running = True
while running:
    screen.fill((0, 0, 0)) #background
    for i in range(shapes):
        if bChangedX[i] == bChangedY[i]:
            bChangedX[i] = randint(minShapesSpeed, maxShapesSpeed)
            bChangedY[i] = randint(minShapesSpeed, maxShapesSpeed)

    #poll for events
    #pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
                #print("you preesed a key")
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: running = False

    #shapes movement
    for i in range(shapes):
        shapesX[i] += bChangedX[i]
        shapesY[i] += bChangedY[i]
    #restricting the shapes inside the window
    for i in range(shapes):
        if shapesX[i] <= 0 + shapesRadius[i]:
            shapesX[i] = 0 + shapesRadius[i]
            if '-' in str(bChangedX[i]):
                #print(f'found "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = randint(minShapesSpeed, maxShapesSpeed)
            else:
                #print(f'didn\'t find "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = -(randint(minShapesSpeed, maxShapesSpeed))

        elif shapesX[i] >= windratio[0] - shapesRadius[i]:
            shapesX[i] = windratio[0] - shapesRadius[i]
            if '-' in str(bChangedX[i]):
                #print(f'found "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = randint(minShapesSpeed, maxShapesSpeed)
            else:
                #print(f'didn\'t find "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = -(randint(minShapesSpeed, maxShapesSpeed))
    
        if shapesY[i] <= 0 + shapesRadius[i]:
            shapesY[i] = 0 + shapesRadius[i]
            if '-' in str(bChangedY[i]):
                #print(f'found "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = randint(minShapesSpeed, maxShapesSpeed)
            else:
                #print(f'didn\'t find "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = -(randint(minShapesSpeed, maxShapesSpeed))
        elif shapesY[i] >= windratio[1] - shapesRadius[i]:
            shapesY[i] = windratio[1] - shapesRadius[i]
            if '-' in str(bChangedY[i]):
                #print(f'found "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = randint(minShapesSpeed, maxShapesSpeed)
            else:
                #print(f'didn\'t find "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = -(randint(minShapesSpeed, maxShapesSpeed))

    for i in range(shapes): drawshapes(shapesX[i], shapesY[i], shapesColor[i])

    clock.tick(60)

    if showTicks: showticks(0, 0)
    pygame.display.update()
    gameticks += 1