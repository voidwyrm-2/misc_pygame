'''a basic character controller'''
import pygame
import math



def limitmax(input, max):
    if input > max: return max
    return input

def limitmin(input, min):
    if input < min: return min
    return input

def isWithinRange(collideeX: int | float, collideeY: int | float, collidedX: int | float, collidedY: int | float, colrange: int | float):
    distance = math.sqrt(math.pow(collideeX - collidedX, 2) + (math.pow(collideeY - collidedY, 2)))
    if distance < colrange: return True
    return False


def work(): 'makes the code work'



# initialize game
pygame.init()

# creating a screen
windratio = 800, 800
screen = pygame.display.set_mode(windratio)  # passing width and height
screen.fill("black")
pygame.display.flip()

# title and icon
pygame.display.set_caption("SnakeyNotWakey")
#icon = pygame.image.load('.png')
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)

plinitxy = 0, 0#windratio[0] // 2, windratio[1] // 2

#plicon = pygame.image.load('')
playerradius = 8.25
playerX = plinitxy[0]
playerY = plinitxy[1]
speed = 4
changedX = 0
changedY = 0

playerLength = 2
playerSegmentsXY = []



def player(playerX, playerY, size): pygame.draw.circle(screen, (0, 250, 0), (playerX, playerY), size)

def playerSegments(playerX, playerY):
    global playerSegmentsXY
    playerSegmentsXY.clear()
    for i in range(playerLength): playerSegmentsXY.append((playerX - ((i + 1) * 10), playerY))


def drawPlayerSegments(size):
    for i in range(playerLength): pygame.draw.circle(screen, (0, 230, 0), playerSegmentsXY[i], size)


def reset(): global playerX; global playerY; global waypoints; playerX = 0; playerY = 0

def showcoords(x, y):
    truco = mainfont.render(f'playerX:{playerX},playerY:{playerY}', True, (255, 255, 255))
    screen.blit(truco, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))  # background
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: running = False; break

                if event.key == pygame.K_LEFT or event.key == pygame.K_a: changedX = -speed

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: changedX = speed

                if event.key == pygame.K_UP or event.key == pygame.K_w: changedY = -speed

                if event.key == pygame.K_DOWN or event.key == pygame.K_s: changedY = speed

        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d): changedX = 0
        if event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s): changedY = 0


    # player movement
    playerX += changedX
    playerY += changedY

    # restricting the player inside the window
    if playerX <= 0:
        playerX = 0
    elif playerX >= windratio[0]:
        playerX = windratio[0]
    
    if playerY <= 0:
        playerY = 0
    elif playerY >= windratio[1]:
        playerY = windratio[1]

    clock.tick(60)

    showcoords(0, 35)
    
    player(playerX, playerY, playerradius)
    playerSegments(playerX, playerY)
    drawPlayerSegments(playerradius - 0.25)
    pygame.display.update()