import pygame
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('Crabbo Pictures\png\Walk (1).png'), pygame.image.load('Crabbo Pictures\png\Walk (2).png'), pygame.image.load('Crabbo Pictures\png\Walk (3).png'), pygame.image.load('Crabbo Pictures\png\Walk (4).png'), pygame.image.load('Crabbo Pictures\png\Walk (5).png'), pygame.image.load('Crabbo Pictures\png\Walk (6).png'), pygame.image.load('Crabbo Pictures\png\Walk (7).png'), pygame.image.load('Crabbo Pictures\png\Walk (8).png'), pygame.image.load('Crabbo Pictures\png\Walk (9).png')]
walkLeft = [pygame.image.load('Crabbo Pictures\png\WalkL (1).png'), pygame.image.load('Crabbo Pictures\png\WalkL (2).png'), pygame.image.load('Crabbo Pictures\png\WalkL (3).png'), pygame.image.load('Crabbo Pictures\png\WalkL (4).png'), pygame.image.load('Crabbo Pictures\png\WalkL (5).png'), pygame.image.load('Crabbo Pictures\png\WalkL (6).png'), pygame.image.load('Crabbo Pictures\png\WalkL (7).png'), pygame.image.load('Crabbo Pictures\png\WalkL (8).png'), pygame.image.load('Crabbo Pictures\png\WalkL (9).png')]
bg = pygame.image.load('Crabbo Pictures\crabbo beach.png')
character = pygame.image.load('Crabbo Pictures\png\Walk (1).png')

pygame.mixer.init()
pygame.mixer.music.load("Crabbo Pictures\CrabRave.mp3")
pygame.mixer.music.play(99999)
pygame.mixer.music.set_volume(0.1)

x = 50
y = 400
width = 40
height = 60
speed = 5
#to control the frames
clock = pygame.time.Clock()

Jump = False
high = 10
#control left and right move
left = False
right = False
#control my list
walkCount = 0

def redrawGameWindow():
    global walkCount #it makes sure is using the global walkCount that created earlier

    screen.blit(bg, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(character, (x, y))
        walkCount = 0
    pygame.display.update()

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < WIDTH - speed - width:
        x += speed
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not(Jump):
        if keys[pygame.K_UP] and y > speed:     # I need to substract to the y
            y -= speed
        if keys[pygame.K_DOWN] and y < HEIGHT - height - speed:    # I need to add to the y
            y += speed
        if keys[pygame.K_SPACE]:
            Jump = True
            left = False
            right = False
            walkCount = 0
    else:
        if high >= -10:
            y -= (high * abs(high)) * 0.5
            high -= 1
        else:
            high = 10
            Jump = False

    redrawGameWindow()

pygame.quit()
