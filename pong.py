import pygame
import random

pygame.init()

screen_size = (1040, 800)
screen = pygame.display.set_mode(screen_size)
background = (255, 255, 255)

# BALL
square = pygame.Rect(520, 400, 40, 40)

# BORDERS
rectL = pygame.Rect(0, 0, 25, 800)   # left
rectR = pygame.Rect(1015, 0, 25, 800)   # right

rectU = pygame.Rect(0, 0, 1040, 25)   # up
rectD = pygame.Rect(0, 775, 1040, 25)   # down

# PADDLES
paddleL = pygame.Rect(100, 300, 25, 175)   # paddle left
paddleR = pygame.Rect(915, 300, 25, 175)   # paddle right

EXTpaddleL = pygame.Rect(115, 300, 10, 175)   # exterior paddle left
EXTpaddleR = pygame.Rect(915, 300, 10, 175)   # exterior paddle right

# MISC
middle = pygame.Rect(520, 25, 15, 750) # middle line

aFactor = 1
bFactor = 1

direction_ballX = 1
direction_ballY = -1

directionXA = 0
directionYA = 0

directionXB = 0
directionYB = 0

points_playerA = 0
points_playerB = 0

# SPEED BOOST
speed_boost = pygame.image.load("lightning_bolt.png")
speed_boost_square = pygame.Rect((random.randint(200, 900), random.randint(100, 700)), speed_boost.get_size())

# SLOW DOWN
slow_down = pygame.image.load("clock_timer.png")
slow_down_square = pygame.Rect((random.randint(200, 900), random.randint(100, 700)), slow_down.get_size())

print("-POINTS-\n")

while True:
    screen.fill(background)
# DRAW
    # MIDDLE LINE
    pygame.draw.rect(screen, (220, 220, 220), middle)

    # BALL
    pygame.draw.rect(screen, (96, 138, 252), square)

    # BORDER DRAW
    pygame.draw.rect(screen, (94, 145, 145), rectL)
    pygame.draw.rect(screen, (94, 145, 145), rectR)
    pygame.draw.rect(screen, (173, 219, 208), rectU)
    pygame.draw.rect(screen, (173, 219, 208), rectD)

    # PADDLE DRAW
    pygame.draw.rect(screen, (55, 79, 79), paddleL)
    pygame.draw.rect(screen, (55, 79, 79), paddleR)

    # PADDLE OUTER LAYER DRAW
    pygame.draw.rect(screen,(75, 95, 95), EXTpaddleL)
    pygame.draw.rect(screen,(75, 95, 95), EXTpaddleR)

    events = pygame.event.get()
    for event in events:
        # If a button was pressed
        if event.type == pygame.QUIT:
            exit()

# COLLISION
    # BALL COLLISION
    if square.colliderect(rectL):
        direction_ballX = 1.5
        points_playerB += 1
        print("PLAYER A: ", points_playerB)
        print("PLAYER B: ", points_playerB, "\n")
    elif square.colliderect(rectR):
        direction_ballX = -1.5
        points_playerA += 1
        print("PLAYER A: ", points_playerA)
        print("PLAYER B: ", points_playerB, "\n")

    elif square.colliderect(rectU):
        direction_ballY = 1.5
    elif square.colliderect(rectD):
        direction_ballY = -1.5

    # PLAYER A PADDLE COLLISION
    if paddleL.colliderect(rectU):
        directionYA = 0
    elif paddleL.colliderect(rectD):
        directionYA = 0

    # PLAYER B PADDLE COLLISION
    if paddleR.colliderect(rectU):
        directionYB = 0
    elif paddleR.colliderect(rectD):
        directionYB = 0

    # PLAYER A PADDLE AND BALL COLLISION
    if square.colliderect(EXTpaddleL):
        direction_ballX = 2
    elif square.colliderect(EXTpaddleR):
        direction_ballX = -2

    # SPEED BOOST AND BALL COLLISION
    if square.colliderect(speed_boost_square):
        aFactor += 1
        direction_ballX = 2 * (-1) ** aFactor
        speed_boost_square.x = random.randint(150, 900)
        speed_boost_square.y = random.randint(50, 700)

    # SLOW DOWN AND BALL COLLISION
    if square.colliderect(slow_down_square):
        bFactor += 1
        direction_ballX = 1 * (-1) ** bFactor
        slow_down_square.x = random.randint(150, 900)
        slow_down_square.y = random.randint(50, 700)

    keys_pressed = pygame.key.get_pressed()
# CONTROLS PLAYER A
    if keys_pressed[pygame.K_w] == 1:
        directionYA = -2
    if keys_pressed[pygame.K_s] == 1:
        directionYA = 2

# CONTROLS PLAYER B
    if keys_pressed[pygame.K_UP] == 1:
        directionYB = -2
    if keys_pressed[pygame.K_DOWN] == 1:
        directionYB = 2

# MOVEMENT
    square = square.move(direction_ballX, direction_ballY)
    paddleL = paddleL.move(directionXA, directionYA)
    paddleR = paddleR.move(directionXB, directionYB)
    EXTpaddleL = EXTpaddleL.move(directionXA, directionYA)
    EXTpaddleR = EXTpaddleR.move(directionXB, directionYB)

    # FONT
    score_font = pygame.font.Font('Halogen.otf', 50)
    score_colour = (75, 95, 95)

    scoreA = score_font.render("Player A:  {0}".format(points_playerA), True, score_colour)
    scoreB = score_font.render("Player B:  {0}".format(points_playerB), True, score_colour)
    screen.blit(scoreA, (220, 45))
    screen.blit(scoreB, (590, 45))

    screen.blit(speed_boost, speed_boost_square)
    screen.blit(slow_down, slow_down_square)

    pygame.display.update()
