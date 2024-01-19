'''a basic character controller'''
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
pygame.display.set_caption("Bokeh")
icon = pygame.image.load('icons/bokeh-icon.jpg')
pygame.display.set_icon(icon)
## LICENCING INFO
# the icon for bokeh.py was sourced from https://en.wikipedia.org/wiki/Bokeh#/media/File:Bokeh_Example.jpg
# it is made by JWCreations and licenced under CC BY-SA 3.0
# its original name was "Bokeh Example.jpg"
## LICENCING INFO

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)

circlecount = 200
maxradius = 20
circles = []


def generate():
    global circles
    global circlecount
    global maxradius
    circles.clear()
    for i in range(circlecount):
        randomXY = randint(0, windratio[0]), randint(0, windratio[1])
        randomcolor = randint(0, 255), randint(0, 255), randint(0, 255)
        circles.append((randomcolor, randomXY, randint(0, maxradius)))

def drawcircles():
    global circles
    for circle in circles: pygame.draw.circle(screen, circle[0], circle[1], circle[2])


generate()
running = True
while running:
    screen.fill((0, 0, 0))  # background
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: running = False; break

                if event.key == pygame.K_r: generate()

        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d): changedX = 0
        if event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s): changedY = 0


    drawcircles()

    pygame.display.update()