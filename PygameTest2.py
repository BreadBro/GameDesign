import pygame
import time
#Drawing with pygame
#Ask user for a color
#Create the window with that color
#Windows width and height
pygame.init()    # always first command
x = True
while x == True:
    try:
        height = int(input("What would you like the height of your window to be? This value must be a number."))
    except ValueError:
        print("This is not a number.\n")
    else:
        x = False

y = True
while y == True:
    try:
        width = int(input("What would you like the width of your window to be? This value must be a number."))
    except ValueError:
        print("This is not a number.\n")
    else:
        y = False

c = input("What color do you want your window to be? Pick any color of the rainbow.").lower()
if c == "red":
    color = 255,0,0
if c == "orange":
    color = 255,128,0
if c == "yellow":
    color = 255,255,0
if c == "green":
    color = 0,255,0
if c == "blue":
    color = 0,0,255
if c == "indigo":
    color = 51,0,102
if c == "violet":
    color = 127,0,255
if c == "purple":
    color = 102,0,204
if c == "brown":
    color = 51,25,0
if c == "grey":
    color = 96,96,96
if c == "black":
    color = 0,0,0
if c == "white":
    color = 255,255,255
if c == "pink":
    color = 255,51,153
windowName = input("What would you like the name of your window to be?")
screen = pygame.display.set_mode((height,width))    # This is a tuple
screen.fill((color))    # Where you select the color of your background
pygame.display.flip()
pygame.display.set_caption(windowName)
run = True
while run:
    pygame.time.delay(100)
    screen.fill((color))
    pygame.display.update()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
pygame.time.delay(50)
pygame.quit()
