import pygame
from random import randint
import math



def limitmax(input, max):
    if input > max: return max
    return input

def limitmin(input, min):
    if input < min: return min
    return input


def work(): 'makes the code work'



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



gravity = 0#.5

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

def isWithinRange(collideeX: int | float, collideeY: int | float, collidedX: int | float, collidedY: int | float, colrange: int | float):
    distance = math.sqrt(math.pow(collideeX - collidedX, 2) + (math.pow(collideeY - collidedY, 2)))
    if distance < colrange: return True
    return False

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

        if event.type == pygame.MOUSEBUTTONDOWN: mouseIsGrabbing = True

        if event.type == pygame.MOUSEBUTTONUP: mouseIsGrabbing = False

    mouseX, mouseY = pygame.mouse.get_pos()

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
            elif shapesY[i] >= windratio[1] - shapesRadius[i]:
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
        if i != limitmax(i + 1, shapes - 1):
            if isWithinRange(shapesX[i], shapesY[i], shapesX[i + 1], shapesY[i + 1], shapesRadius[i]):
                shapesX[i + 1] = shapesX[i + 1] + shapesRadius[i + 1]
        if i != limitmin(i - 1, shapes - 1):
            if isWithinRange(shapesX[i], shapesY[i], shapesX[i - 1], shapesY[i - 1], shapesRadius[i]):
                shapesY[i - 1] = shapesY[i - 1] - shapesRadius[i - 1]
        

    for i in range(shapes): drawshapes(shapesX[i], shapesY[i], shapesColor[i])

    clock.tick(60)
    #clock.tick(1)

    if showTicks: showticks(0, 0)
    if showCursorPos: showcursorpos(0, 35)
    pygame.display.update()
    gameticks += 1