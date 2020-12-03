import pygame
import math
import random
import os
import time
import datetime

#For instructions use display_message function that is given to print the words on to the screen
#Key and Mouse events used already
#5 images already done
#for leadeboard use code from previous game
#scrolling doesnt make sense
#menu I have no idea
#exit works cause of an error

# setup display
pygame.init()
WIDTH, HEIGHT = 900, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# setup  button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# set up fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("ImagesHM\hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["PYTHON","JAVA","JAVASCRIPT","PHP","COMPUTER","GEEKS","KEYBOARD","LAPTOP","HEADPHONES","HARDWARE","SOFTWARE","MSI","NVIDIA","LOGITECH","INTEL","XBOX","PLAYSTATION","INTEL","AMD","NINTENDO","GAMECUBE","RYZEN","CPU","UNITY"] # make it longer
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# score
def score(P1score):
    date = datetime.datetime.now()
    dskaslg = open('hangmanrecords.txt', 'a')
    with open('hangmanrecords.txt') as s:
        records = open('hangmanrecords.txt','a')
        records.write(str(P1score))
        records.write(' points')
        records.write(' - ')
        records.write(date.strftime('%A, %B %d, %Y %X'))
        records.write('\n')
        records.close()

def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) # Notice centering

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)

def main():
    global hangman_status
    global a
    P1score = 0
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    display_message("Here are your rules.")
    display_message("Click on a letter to guess.")
    display_message("For each turn you can guess one letter.")
    display_message("Guess all of the letters correct to win.")
    keyBoardKey=pygame.key.get_pressed()
    while run == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        while won:
            a = True
            display_message("You WON!")
            score(P1score)
            P1score = P1score + 1
            display_message("Press SPACE to play again, Press ESCAPE to close.")
            while a:
                if event.type == pygame.KEYDOWN:
                    if keyBoardKey[pygame.K_SPACE]:
                        run = True
                        a = False
                    if keyBoardKey[pygame.K_ESCAPE]:
                        run = False
                        sys.exit()
            break

        if hangman_status == 6:
            a = True
            display_message("You LOST!")
            display_message("Press SPACE to play again, Press ESCAPE to close.")
            while a:
                if event.type == pygame.KEYDOWN:
                    if keyBoardKey[pygame.K_SPACE]:
                        run = True
                        a = False
                    if keyBoardKey[pygame.K_ESCAPE]:
                        run = False
                        sys.exit()
            break

while True:

    main()
pygame.quit()
