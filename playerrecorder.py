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
pygame.display.set_caption("BasicCharacterController")
#icon = pygame.image.load('')
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)



isRecording = False
isReplaying = False

plinitxy = 0, 0#windratio[0] // 2, windratio[1] // 2

playerXY = []
playerradius = 8.25
playerX = plinitxy[0]
playerY = plinitxy[1]
speed = 4
changedX = 0
changedY = 0
def player(playerX, playerY, size): pygame.draw.circle(screen, (0, 0, 255), (playerX, playerY), size)


def recordPlayer(playerX, playerY):
    global playerXY
    playerXY.append((playerX, playerY))
    print(f'recording ({playerX},{playerY})...')


def replayPlayer(size):
    for xy in playerXY:
        pygame.draw.circle(screen, (0, 0, 255), xy, size)
        #print(f'replaying {xy}')


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

                if event.key == pygame.K_r: reset()

                if event.key == pygame.K_c: playerXY.clear()

                if event.key == pygame.K_p and not isRecording: isRecording = True
                if event.key == pygame.K_o and isRecording: isRecording = False

                if event.key == pygame.K_k and not isReplaying: isReplaying = True
                if event.key == pygame.K_l and isReplaying: isReplaying = False

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

    player(playerX, playerY, playerradius)
    if isRecording and not isReplaying: recordPlayer(playerX, playerY)
    if isRecording and not isReplaying: showrecording(2, 0)

    if isReplaying and not isRecording: replayPlayer(playerradius - 0.25)
    if isReplaying and not isRecording: showreplaying(2, 0)

    #print(len(playerXY))
    pygame.display.update()