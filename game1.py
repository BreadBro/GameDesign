import random
import time
import sys
import os

name = input("\nWhat is your name?\n")
words = ['python','java','php','javascript','computer','geeks','keyboard','laptop','headphones','hardware','software','msi','nvidia','intel','logitech','amd','playstation','xbox','nintendo','gamecube','ryzen','cpu','unity particle system']
answer = input("Do you want to guess a word?\n")
while answer == "Yes" or answer == "yes" or answer == "y" or answer == "Y":
    print("Good Luck " + name + "!")
    word = random.choice(words)
    print("Guess my word.")
    guesses = ''
    final = ''
    turns = 10
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char,end='')
                final = final+char
            else:
                print("_",end='')
                failed += 1
            if word in final:
                print("You have won with", + turns, "guesses left.")
                print("The word is:", word)
                answer == input("Do you want to play again?")
                if answer == "Yes" or answer == "yes" or answer == "y" or answer == "Y":
                    os.execl(sys.executable, sys.executable, *sys.argv) # completely restart program
        guess = input("\nGuess a character: ") # This line was screwing up stuff for some reason so I had to do the line above ^ and completely restart the program. (Let's just say its one of those old arcade machines where you need to input your name for a high score every time.)
        guesses += guess
        if guess not in word:
            turns -= 1
            print("That is incorrect")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You have run out of guesses. You have failed.")
                print("GAME OVER, You Lose.")
                answer == input("\nDo you want to play again?")
                if answer == "Yes" or answer == "yes" or answer == "y" or answer == "Y":
                    break

else:
    print("Then why are you here you idiot? Get out!")
    time.sleep(2)
    exit()
