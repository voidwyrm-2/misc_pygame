import pygame
from random import randint



def limit(input, max):
    if input > max: return max
    return input



# initialize game
pygame.init()

# creating a screen
windratio = 800, 800
screen = pygame.display.set_mode(windratio)  # passing width and height
screen.fill("black")
pygame.display.flip()
clock = pygame.time.Clock()

# title and icon
pygame.display.set_caption("Rhythm Game")
#icon = pygame.image.load('icons/.png')
#pygame.display.set_icon(icon)

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)

dotamount = 10
dotspeed = 4

dotsX = []
dotsY = []
rhythmpos = windratio[0] // 2, windratio[1] // 2
for i in range(dotamount): dotsX.append(1000); dotsY.append(windratio[1] // 2)

def drawdots(x, y): pygame.draw.circle(screen, (0, 0, 255), (x, y), 25)
     


def rhythm():
    for i in range(dotamount):
        distX = dotsX[i] - rhythmpos[0]
        #print(distX)
        if distX < 20 + (dotamount * 2): dotsX[i] = 1000


def drawcircle(xy): pygame.draw.circle(screen, (255, 0, 0), xy, 30, 5)


running = True
while running:
    screen.fill((0, 0, 0))  # background
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: running = False; break

                if event.key == pygame.K_SPACE: rhythm()

    for i in range(dotamount): dotsX[i] -= dotspeed

    for i in range(dotamount):
        if dotsX[i] <= 0: dotsX[i] = 1000

    for i in range(dotamount): drawdots(dotsX[i], dotsY[i])

    drawcircle(rhythmpos)
    #print(dotsX)

    clock.tick(60)

    pygame.display.update()