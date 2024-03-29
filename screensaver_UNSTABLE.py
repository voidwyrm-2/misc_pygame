import pygame
from random import randint
import math



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

canMultiply = False
canGoLowerThanStart = False
shapeDupeRollLength = 100
shapeDupeChance = 40
shapeCap = 60
shapeLife = 100
shapeLifeInc = shapeLife
oneRadius = False
defRadius = 10
minRadius = 5
maxRadius = 20

# A moment of silence for the era when "shapes" was "balls"

initX = 20
initY = 20
initShapes = 2#30
shapes = initShapes
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

def genColor(): return (randint(10, 255), randint(10, 255), randint(10, 255))

def dupeshape(X, Y, speedX, speedY, color):
    global shapes
    if shapes >= shapeCap: return
    shapesX.append(X)
    shapesY.append(Y)
    bChangedX.append(speedX)
    bChangedY.append(speedY)
    shapesColor.append(color)
    if oneRadius: shapesRadius.append(defRadius)
    else: shapesRadius.append(randint(minRadius, maxRadius))
    shapes += 1

def delshape():
    global shapes
    if shapes <= 2 and canGoLowerThanStart: return
    if shapes <= initShapes and not canGoLowerThanStart: return
    del shapesX[0]
    del shapesY[0]
    del bChangedX[0]
    del bChangedY[0]
    del shapesColor[0]
    del shapesRadius[0]
    shapes -= 1



def collicheckX(coX, radius, cindex):
    global shapes
    for i in range(shapes):
        if i != cindex:
            distance = math.sqrt(math.pow(coX - shapesX[i], 2))
            if distance < radius: return True
        else: continue
    return False

def collicheckY(coY, radius, cindex):
    global shapes
    for i in range(shapes):
        if i != cindex:
            distance = math.sqrt(math.pow(coY - shapesY[i], 2))
            if distance < radius: return True
        else: continue
    return False


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
        selfcolX = collicheckX(shapesX[i], shapesRadius[i], i)
        if shapesX[i] <= 0 + shapesRadius[i] or selfcolX:
            if not selfcolX: shapesX[i] = 0 + shapesRadius[i]
            if '-' in str(bChangedX[i]):
                #print(f'found "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = randint(minShapesSpeed, maxShapesSpeed)
                if canMultiply:
                    dupeRoll = randint(0, shapeDupeRollLength)
                    print(f'rolled {dupeRoll} out of {shapeDupeChance}!')
                    if dupeRoll > shapeDupeChance: dupeshape(shapesX[i], shapesY[i], randint(minShapesSpeed, maxShapesSpeed), randint(minShapesSpeed, maxShapesSpeed), genColor())
            else:
                #print(f'didn\'t find "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = -(randint(minShapesSpeed, maxShapesSpeed))
                if canMultiply:
                    dupeRoll = randint(0, shapeDupeRollLength)
                    print(f'rolled {dupeRoll} out of {shapeDupeChance}!')
                    if dupeRoll > shapeDupeChance: dupeshape(shapesX[i], shapesY[i], -randint(minShapesSpeed, maxShapesSpeed), randint(minShapesSpeed, maxShapesSpeed), genColor())
        
        elif shapesX[i] >= windratio[0] - shapesRadius[i] or selfcolX:
            if not selfcolX: shapesX[i] = windratio[0] - shapesRadius[i]
            if '-' in str(bChangedX[i]):
                #print(f'found "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = randint(minShapesSpeed, maxShapesSpeed)
                if canMultiply:
                    dupeRoll = randint(0, shapeDupeRollLength)
                    print(f'rolled {dupeRoll} out of {shapeDupeChance}!')
                    if dupeRoll > shapeDupeChance: dupeshape(shapesX[i], shapesY[i], randint(minShapesSpeed, maxShapesSpeed), randint(minShapesSpeed, maxShapesSpeed), genColor())
            else:
                #print(f'didn\'t find "-" in "{str(bChangedX[i])}"')
                bChangedX[i] = -(randint(minShapesSpeed, maxShapesSpeed))
                if canMultiply:
                    dupeRoll = randint(0, shapeDupeRollLength)
                    print(f'rolled {dupeRoll} out of {shapeDupeChance}!')
                    if dupeRoll > shapeDupeChance: dupeshape(shapesX[i], shapesY[i], -randint(minShapesSpeed, maxShapesSpeed), randint(minShapesSpeed, maxShapesSpeed), genColor())

        selfcolY = collicheckX(shapesY[i], shapesRadius[i], i)
        if shapesY[i] <= 0 + shapesRadius[i] or selfcolY:
            if not selfcolY: shapesY[i] = 0 + shapesRadius[i]
            if '-' in str(bChangedY[i]):
                #print(f'found "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = randint(minShapesSpeed, maxShapesSpeed)
                if canMultiply:
                    dupeRoll = randint(0, shapeDupeRollLength)
                    print(f'rolled {dupeRoll} out of {shapeDupeChance}!')
                    if dupeRoll > shapeDupeChance: dupeshape(shapesX[i], shapesY[i], randint(minShapesSpeed, maxShapesSpeed), randint(minShapesSpeed, maxShapesSpeed), genColor())
            else:
                #print(f'didn\'t find "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = -(randint(minShapesSpeed, maxShapesSpeed))
                if canMultiply:
                    dupeRoll = randint(0, shapeDupeRollLength)
                    print(f'rolled {dupeRoll} out of {shapeDupeChance}!')
                    if dupeRoll > shapeDupeChance: dupeshape(shapesX[i], shapesY[i], -randint(minShapesSpeed, maxShapesSpeed), randint(minShapesSpeed, maxShapesSpeed), genColor())
        elif shapesY[i] >= windratio[1] - shapesRadius[i] or selfcolY:
            if not selfcolY: shapesY[i] = windratio[1] - shapesRadius[i]
            if '-' in str(bChangedY[i]):
                #print(f'found "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = randint(minShapesSpeed, maxShapesSpeed)
                if canMultiply:
                    dupeRoll = randint(0, shapeDupeRollLength)
                    print(f'rolled {dupeRoll} out of {shapeDupeChance}!')
                    if dupeRoll > shapeDupeChance: dupeshape(shapesX[i], shapesY[i], randint(minShapesSpeed, maxShapesSpeed), randint(minShapesSpeed, maxShapesSpeed), genColor())
            else:
                #print(f'didn\'t find "-" in "{str(bChangedY[i])}"')
                bChangedY[i] = -(randint(minShapesSpeed, maxShapesSpeed))
                if canMultiply:
                    dupeRoll = randint(0, shapeDupeRollLength)
                    print(f'rolled {dupeRoll} out of {shapeDupeChance}!')
                    if dupeRoll > shapeDupeChance: dupeshape(shapesX[i], shapesY[i], -randint(minShapesSpeed, maxShapesSpeed), randint(minShapesSpeed, maxShapesSpeed), genColor())

    for i in range(shapes): drawshapes(shapesX[i], shapesY[i], shapesColor[i])

    clock.tick(60)

    if canMultiply:
        if gameticks == shapeLifeInc: delshape(); shapeLifeInc += shapeLife

    if showTicks: showticks(0, 0)
    pygame.display.update()
    gameticks += 1