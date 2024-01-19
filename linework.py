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

# title and icon
pygame.display.set_caption("Line Work")
icon = pygame.image.load('icons/RandomLines.png')
pygame.display.set_icon(icon)

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)

clearprev = True

linecount = 200
minradius = 1
maxradius = 20
lines = []


def generate():
    global lines
    global linecount
    global maxradius
    lines.clear()
    for i in range(linecount):
        randomXYXY = (randint(0, windratio[0]), randint(0, windratio[1])), (randint(0, windratio[0]), randint(0, windratio[1]))
        randomcolor = randint(0, 255), randint(0, 255), randint(0, 255)
        lines.append((randomcolor, randomXYXY, randint(minradius, maxradius)))

def drawlines():
    global lines
    for line in lines: pygame.draw.line(screen, line[0], line[1][0], line[1][1], line[2])


generate()
running = True
while running:
    if clearprev: screen.fill((0, 0, 0))  # background
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: running = False; break

                if event.key == pygame.K_r: generate()


    drawlines()

    pygame.display.update()