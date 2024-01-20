'''a basic character controller'''
import pygame



# initialize game
pygame.init()

# creating a screen
windratio = 800, 800
screen = pygame.display.set_mode(windratio)  # passing width and height
screen.fill("black")
pygame.display.flip()

# title and icon
pygame.display.set_caption("AIbutbad")
clock = pygame.time.Clock()

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)



isRecording = False
isReplaying = False

plinitxy = 0, 0#windratio[0] // 2, windratio[1] // 2

playerradius = 8.25
playerX = plinitxy[0]
playerY = plinitxy[1]
speed = 4
changedX = 0
changedY = 0
def player(playerX, playerY, size): pygame.draw.circle(screen, (0, 0, 255), (playerX, playerY), size)

aiPlayerradius = 8.25
aiPlayerX = plinitxy[0]
aiPlayerY = plinitxy[1]
aiSpeed = 4
aiChangedX = 0
aiChangedY = 0
def aiPlayer(aiPlayerX, aiPlayerY, size): pygame.draw.circle(screen, (255, 0, 0), (aiPlayerX, aiPlayerY), size)


def reset(): global playerX; global playerY; global playerXY; playerX = 0; playerY = 0; playerXY.clear()


def showcoords(x, y):
    truco = mainfont.render(f'playerX:{playerX},playerY:{playerY}', True, (255, 255, 255))
    screen.blit(truco, (x, y))

def showrecording(x, y):
    recording = mainfont.render(f'You are being recorded', True, (255, 255, 255))
    screen.blit(recording, (x, y))

def showreplaying(x, y):
    replaying = mainfont.render(f'Replaying...', True, (255, 255, 255))
    screen.blit(replaying, (x, y))



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

    # ai player movement
    aiPlayerX += aiChangedX
    aiPlayerY += aiChangedY

    # restricting the ai player inside the window
    if aiPlayerX <= 0:
        aiPlayerX = 0
    elif aiPlayerX >= windratio[0]:
        aiPlayerX = windratio[0]
    
    if aiPlayerY <= 0:
        aiPlayerY = 0
    elif aiPlayerY >= windratio[1]:
        aiPlayerY = windratio[1]

    clock.tick(60)

    player(playerX, playerY, playerradius)
    aiPlayer(aiPlayerX, aiPlayerY, aiPlayerradius)

    #print(len(playerXY))
    pygame.display.update()