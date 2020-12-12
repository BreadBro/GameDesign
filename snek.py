import pygame, sys, time, datetime, random
from pygame import mouse

# PySnek (pygame version of snake)
# Pseudo Code
    # Instructions: Move with arrow keys, dont run into yourself, grow when running over food
    # 3 options will be easy (speed increase 1), medium (speed increase 2 or 3), hard (speed increase 5)
    # possibly add score multipliers based on difficulty
    # exit using stuff from previous code
    # leaderboard, do a similar thing to other game but add a button for it
    # add a map selector
    # for images make random generator for which food will appear
    # mouse events: clicking the buttons on the main menu
    # key events: moving the snake around
    # screen is 1000 x 800

# Ask for name and set score
p1name = input("What is your name?\n")
P1score = 0

pygame.init()
pygame.mixer.init()

# colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# background images
forest = pygame.image.load("SnekFiles\\forest.png")
dogpic = pygame.image.load("SnekFiles\\dogpic.png")
beach = pygame.image.load("SnekFiles\\beach.png")
blackpic = pygame.image.load("SnekFiles\\black.png")
map = blackpic

# window size
width = 1000
height = 800

# set window color, height, and name
window = pygame.display.set_mode((width,height))
window.fill(black)
pygame.display.set_caption('PySnek')

# frame rate
clock = pygame.time.Clock()

# Defining some variables
LETTER_FONT = pygame.font.SysFont('COPPERPLATE GOTHIC BOLD"', 40)
WORD_FONT = pygame.font.SysFont('COPPERPLATE GOTHIC BOLD"', 60)
TITLE_FONT = pygame.font.SysFont('COPPERPLATE GOTHIC BOLD"', 70)

# size of snake rectangles (10x10)
snakeSize = 10

# fonts
font_style = pygame.font.SysFont("times new roman", 25)
score_font = pygame.font.SysFont("COPPERPLATE GOTHIC BOLD", 35)

def chooseMap():
    a = True
    global map
    # set default background
    map = blackpic
    while a:
        # map choosing Instructions
        window.blit(map,(0,0))
        textA = WORD_FONT.render("This is the map selector.", 1, white)
        window.blit(textA, (int(width/2 - textA.get_width()/2), 140))
        textB = WORD_FONT.render("Use your arrow keys to scroll between maps.", 1, white)
        window.blit(textB, (int(width/2 - textB.get_width()/2), 190))
        textC = WORD_FONT.render("Hit SPACE to lock in your choice.", 1, white)
        window.blit(textC, (int(width/2 - textC.get_width()/2), 240))
        pygame.display.update()

        for event in pygame.event.get():
            # hit X to quit
            if event.type == pygame.QUIT:
                run = False
                sys.quit()
                break

            if event.type == pygame.KEYDOWN:
                # checks which key is down and which map you are on so that it can change the maps in a proper order
                if event.key == pygame.K_LEFT and map == forest:
                    window.fill(white)
                    map = beach
                    break
                    pygame.display.update()

                if event.key == pygame.K_LEFT and map == blackpic:
                    window.fill(white)
                    map = dogpic
                    break
                    pygame.display.update()

                if event.key == pygame.K_LEFT and map == beach:
                    window.fill(white)
                    map = blackpic
                    break
                    pygame.display.update()

                if event.key == pygame.K_RIGHT and map == beach:
                    window.fill(white)
                    map = forest
                    break
                    pygame.display.update()

                if event.key == pygame.K_RIGHT and map == dogpic:
                    window.fill(white)
                    map = blackpic
                    pygame.display.update()
                    break

                if event.key == pygame.K_RIGHT and map == blackpic:
                    window.fill(white)
                    map = beach
                    pygame.display.update()
                    break

                if event.key == pygame.K_SPACE:
                    a = False
    menu()

font_style = pygame.font.SysFont("times new roman", 25)
score_font = pygame.font.SysFont("COPPERPLATE GOTHIC BOLD", 35)

# score in the top left while playing
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    window.blit(value, [0, 0])

# view leaderboard code
def leaderboard():
    # open files
    gamewords = open('snekrecords.txt','r')
    # get info from files
    print("\n")
    scores = []
    for line in gamewords:
        scores.append(line.strip())
    gamewords.close()
    scores = sorted(scores, reverse=True)
    # print info
    print('\n'.join(scores))
    input("Press ENTER to exit leaderboard.\n")
    sys.exit()


# record score for leaderboard
def score(p1name,P1score):
    date = datetime.datetime.now()
    # create file if not already created
    dskaslg = open('snekrecords.txt', 'a')
    with open('snekrecords.txt') as s:
        records = open('snekrecords.txt','a')
        # write score
        records.write(str(P1score))
        records.write(' points')
        records.write(' - ')
        # write name
        records.write(str(p1name))
        records.write('  ')
        # write date
        records.write(date.strftime('%A, %B %d, %Y %X'))
        records.write('\n')
        records.close()

# rectangle for snake
def snake(snakeSize, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, white, [x[0], x[1], snakeSize, snakeSize])

# code for putting messages on the screen
def message(msg, color):
    message = font_style.render(msg, True, color)
    window.blit(message, [width / 6, height / 3])

# menu code, where everything comes back to
def menu():
    pygame.init()
    global speed_increase
    global speed
    global snakeSize
    global mx
    global my
    global run
    global click
    global score_multiplier
    mouse.set_pos(500,400)
    pygame.mixer.music.load("SnekFiles\SnekMenu.mp3")
    pygame.mixer.music.play(99999)
    pygame.mixer.music.set_volume(0.3)
    x = True
    time.sleep(0.5)
    # loop
    while x == True:
        # stuff for buttons in menu
        button_1 = pygame.Rect(100,600,200,50)
        button_2 = pygame.Rect(400,600,200,50)
        button_3 = pygame.Rect(700,600,200,50)
        button_4 = pygame.Rect(100,692,200,50)
        button_5 = pygame.Rect(400,692,200,50)
        button_6 = pygame.Rect(700,692,200,50)
        mx, my = pygame.mouse.get_pos()
        window.fill(white)

        # rectangles for buttons
        pygame.draw.rect(window, (255,0,0), button_1)
        pygame.draw.rect(window, (255,0,0), button_2)
        pygame.draw.rect(window, (255,0,0), button_3)
        pygame.draw.rect(window, (255,0,0), button_4)
        pygame.draw.rect(window, (255,0,0), button_5)
        pygame.draw.rect(window, (255,0,0), button_6)

        # words
        text1 = TITLE_FONT.render("PySnek", 1, black)
        window.blit(text1, (int(width/2 - (text1.get_width()/2)), 20))

        text2 = WORD_FONT.render("Instructions:", 1, black)
        window.blit(text2, (int(width/2 - text2.get_width()/2), 90))

        text2_0 = WORD_FONT.render("Move the Snake using your arrow keys", 1, black)
        window.blit(text2_0, (int(width/2 - text2_0.get_width()/2), 140))

        text2_1 = WORD_FONT.render("so that you eat the fruits.", 1, black)
        window.blit(text2_1, (int(width/2 - text2_1.get_width()/2), 190))

        text2_2 = WORD_FONT.render("When you eat a fruit your snake", 1, black)
        window.blit(text2_2, (int(width/2 - text2_2.get_width()/2), 240))

        text2_3 = WORD_FONT.render("your snake will grow and speed up.", 1, black)
        window.blit(text2_3, (int(width/2 - text2_3.get_width()/2), 290))

        text2_4 = WORD_FONT.render("If you run into your tail, you lose.", 1, black)
        window.blit(text2_4, (int(width/2 - text2_4.get_width()/2), 340))

        text3 = WORD_FONT.render("Easy", 1, black)
        window.blit (text3, (int(width/5 - text3.get_width()/2), 605))

        text4 = WORD_FONT.render("Medium", 1, black)
        window.blit(text4, (int(width/2 - text4.get_width()/2), 605))

        text5 = WORD_FONT.render("Hard", 1, black)
        window.blit(text5, (int(width/1.25 - text5.get_width()/2), 605))

        text6 = WORD_FONT.render("Scores", 1, black)
        window.blit(text6, (int(width/5 - text6.get_width()/2), 700))

        text7 = WORD_FONT.render("Maps", 1, black)
        window.blit(text7, (int(width/2 - text7.get_width()/2), 700))

        text8 = WORD_FONT.render("Quit", 1, black)
        window.blit(text8, (int(width/1.255 - text8.get_width()/2), 700))

        pygame.display.update()
        time.sleep(.5)
        for event in pygame.event.get():
            # to quit game using the X
            if event.type == pygame.QUIT:
                run = False
                sys.quit()
                break
            # checks if you are clicking with your mouse or not
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # code behind clicking the buttons
        if button_1.collidepoint((mx,my)):
            if click:
                speed_increase = 1
                score_multiplier = 1
                pygame.mixer.music.stop()
                x = False
                main()
                pass

        if button_2.collidepoint((mx,my)):
            if click:
                speed_increase = 3
                score_multiplier = 1.25
                pygame.mixer.music.stop()
                x = False
                main()
                pass

        if button_3.collidepoint((mx,my)):
            if click:
                speed_increase = 5
                score_multiplier = 1.5
                pygame.mixer.music.stop()
                x = False
                main()
                pass

        if button_4.collidepoint((mx,my)):
            if click:
                pygame.quit()
                leaderboard()
                pass

        if button_5.collidepoint((mx,my)):
            if click:
                pygame.mixer.music.stop()
                chooseMap()
                pass

        if button_6.collidepoint((mx,my)):
            if click:
                pygame.quit()
                quit()
                pass

        click = False

# main code for easy difficulty
def main():
    # speed of the snake
    speed = 10
    # loops
    game_over = False
    game_close = False

    snakeX = width / 2
    snakeY = height / 2

    # get a random image
    imageNumber = random.randrange(1, 5)
    fruitImage = pygame.image.load("SnekFiles\\fruit" + str(imageNumber) + ".png")

    snakeX_change = 0
    snakeY_change = 0

    snake_List = []
    snakeLength = 1

    # random position for the food to spawn
    foodx = round(random.randrange(0, width - snakeSize) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snakeSize) / 10.0) * 10.0

    while not game_over:
        # when game ends
        while game_close == True:
            window.fill(black)
            message("You Lost! Press SPACE to Play Again or ESCAPE for Menu.", red)
            Your_score(snakeLength - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        P1score = (snakeLength - 1)*score_multiplier
                        score(p1name, P1score)
                        mouse.set_pos(500,400)
                        menu()
                    if event.key == pygame.K_SPACE:
                        main()

        # code for snake moving
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snakeX_change = -snakeSize
                    snakeY_change = 0
                elif event.key == pygame.K_RIGHT:
                    snakeX_change = snakeSize
                    snakeY_change = 0
                elif event.key == pygame.K_UP:
                    snakeY_change = -snakeSize
                    snakeX_change = 0
                elif event.key == pygame.K_DOWN:
                    snakeY_change = snakeSize
                    snakeX_change = 0

        # if the snake hits the borders you lose
        if snakeX >= width or snakeX < 0 or snakeY >= height or snakeY < 0:
            game_close = True
        snakeX += snakeX_change
        snakeY += snakeY_change
        window.blit(map,(0,0))
        window.blit(fruitImage, (foodx, foody))
        snake_Head = []
        snake_Head.append(snakeX)
        snake_Head.append(snakeY)
        snake_List.append(snake_Head)
        # if snake hits itself
        if len(snake_List) > snakeLength:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snakeSize, snake_List)
        Your_score(snakeLength - 1)

        pygame.display.update()

        # if snake hits the food then it grows and speeds up
        if snakeX == foodx and snakeY == foody:
            foodx = round(random.randrange(0, width - snakeSize) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snakeSize) / 10.0) * 10.0
            pygame.mixer.init()
            pygame.mixer.music.load("SnekFiles\\EatSound.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.4)
            snakeLength += 1
            speed += speed_increase
            imageNumber = random.randrange(1, 5)
            fruitImage = pygame.image.load("SnekFiles\\fruit" + str(imageNumber) + ".png")

        clock.tick(speed)

    pygame.quit()
    quit()




menu()
