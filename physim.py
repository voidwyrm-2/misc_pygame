import pygame
from random import randint
from common import *



# initialize game
pygame.init()

# creating a screen
windratio = 800, 800
screen = pygame.display.set_mode(windratio)  # passing width and height
screen.fill("black")
pygame.display.flip()
# title and icon
pygame.display.set_caption("Physim")
icon = pygame.image.load('icons/Physgun.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)


shouldTheCodeWork = True

isFirstMousebound = False

gravity = 0.5

gameticks = 0
showTicks = False
showCursorPos = True
oneRadius = True
defRadius = 10
minRadius = 5
maxRadius = 20

mouseX = 0
mouseY = 0
extraMouseRange = 5

# A moment of silence for the era when "shapes" was "balls"

initX = 10
initY = 20
shapes = 20
shapeCap = 40
shapesRadius = []

mouseIsGrabbing = False

# defining our shapes
shapesInfo = []
minShapesSpeed = 1
maxShapesSpeed = 4
shapesColor = []
shapesX = []
shapesY = []
bChangedX = []
bChangedY = []
shapesGrav = []
shapesBounded = []
shapeGrabbed = []


def genColor(): return (randint(10, 255), randint(10, 255), randint(10, 255))

def drawshapes(x, y, color): shapesInfo.append(pygame.draw.circle(screen, color, (x, y), shapesRadius[i]))

for i in range(shapes): shapesX.append(initX + randint((30 * i), (30 * i) + 10)); shapesY.append(initY)

for i in range(shapes): bChangedX.append(0); bChangedY.append(0)#bChangedX.append(randint(minShapesSpeed, maxShapesSpeed)); bChangedY.append(randint(minShapesSpeed, maxShapesSpeed))

for i in range(shapes): shapesColor.append(genColor())

for i in range(shapes): shapesGrav.append(True)

for i in range(shapes): shapesBounded.append(True)

for i in range(shapes): shapeGrabbed.append(False)

for i in range(shapes):
    if oneRadius: shapesRadius.append(defRadius)
    else: shapesRadius.append(randint(minRadius, maxRadius))


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


def showticks(x, y):
    tick = mainfont.render(f'tick:{gameticks}', True, (255, 255, 255))
    screen.blit(tick, (x, y))

def showcursorpos(x, y):
    global mouseX
    global mouseY
    cp = mainfont.render(f'mouse_pos:{mouseX},{mouseY}', True, (255, 255, 255))
    screen.blit(cp, (x, y))

def showShapePos(x, y, Sx, Sy, Si):
    tick = mainfont.render(f'shapePos({Si}):{Sx}, {Sy}', True, (255, 255, 255))
    screen.blit(tick, (x, y))

def showwhatever(x, y):
    moose = mainfont.render(f'try grabbing one of the circles with your mouse!', True, (255, 255, 255))
    screen.blit(moose, (x, y))


running = True
while running:
    if shouldTheCodeWork: work()
    screen.fill((0, 0, 0)) #background

    #poll for events
    #pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
            #print("you pressed a key")
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: running = False

            if event.key == pygame.K_1: shapesX[0] = mouseX; shapesY[0] = mouseY

            if event.key == pygame.K_k and not isFirstMousebound: isFirstMousebound = True
            if event.key == pygame.K_l and isFirstMousebound: isFirstMousebound = False

        if event.type == pygame.MOUSEBUTTONDOWN: mouseIsGrabbing = True

        if event.type == pygame.MOUSEBUTTONUP: mouseIsGrabbing = False


    mouseX, mouseY = pygame.mouse.get_pos()

    if isFirstMousebound: shapesX[0] = mouseX
    if isFirstMousebound: shapesY[0] = mouseY

    for i in range(shapes):
        if shapesGrav[i]:
            bChangedY[i] += gravity

    #shapes movement
    for i in range(shapes):
        shapesX[i] += bChangedX[i]
        shapesY[i] += bChangedY[i]
        #print(shapesY)
    #restricting the shapes inside the window
    for i in range(shapes):
        # X wall collision
        if shapesBounded[i]:
            if shapesX[i] <= 0 + shapesRadius[i]:
                shapesX[i] = 0 + shapesRadius[i]
            elif shapesX[i] >= windratio[0] - shapesRadius[i]:
                shapesX[i] = windratio[0] - shapesRadius[i]

        # Y wall collision
        if shapesBounded[i]:
            if shapesY[i] <= 0 + shapesRadius[i]:
                shapesY[i] = 0 + shapesRadius[i]
                if mouseIsGrabbing and shapeGrabbed[i]: print(f'found collison with ceiling at {shapesX[i]}, {shapesY[i]}!')
            elif shapesY[i] > windratio[1] - shapesRadius[i]:
                shapesY[i] = windratio[1] - shapesRadius[i]

        # XY mouse grabbing
        if mouseIsGrabbing:
            if isWithinRange(mouseX, mouseY, shapesX[i], shapesY[i], 10 + extraMouseRange): shapesGrav[i] = False; shapesX[i] = mouseX; shapesY[i] = mouseY; shapeGrabbed[i] = True
            else: shapesGrav[i] = True; shapeGrabbed[i] = False

    for i in range(shapes):
        if mouseIsGrabbing and shapeGrabbed[i]: showShapePos(0, 70, shapesX[i], shapesY[i], i)
            #print(f'found collison with floor at !')

    for i in range(shapes):
        #break
        i1 = limitminmax(i + 1, 0, shapes)
        i2 = limitminmax(i - 1, 0, shapes)
        if isWithinRange(shapesX[i], shapesY[i], shapesX[i1], shapesY[i1], shapesRadius[i]):
            shapesX[i1] = shapesX[i1] + shapesRadius[i1]

        if isWithinRange(shapesX[i], shapesY[i], shapesX[i2], shapesY[i2], shapesRadius[i]):
            shapesY[i2] = shapesY[i2] - shapesRadius[i2]


    for i in range(shapes): drawshapes(shapesX[i], shapesY[i], shapesColor[i])

    clock.tick(60)
    #clock.tick(1)

    if showTicks: showticks(0, 0)
    if showCursorPos: showcursorpos(0, 35)
    showwhatever(1, 70)
    pygame.display.update()
    gameticks += 1