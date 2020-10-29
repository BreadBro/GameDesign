import random
import time
import sys
import os

name = input("\nWhat is your name?\n")
words = ['python','java','php','JavaScript','computer','geeks','keyboard','laptop','headphones','hardware','software']
answer = input("Do you want to guess a word?\n")
while answer == "Yes" or answer == "yes" or answer == "y" or answer == "Y":
    print("Good Luck " + name + "!")
    word = random.choice(words)
    print("Guess my word.")
    guesses = ''
    turns = 10
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
            if failed == 0:
                print("You have won with", + turns, "guesses left.")
                print("The word is:", word)
                answer == input("Do you want to play again?")
                if answer == "Yes" or answer == "yes" or answer == "y" or answer == "Y":
                    os.execl(sys.executable, sys.executable, *sys.argv) # completely restart program
        guess = input("Guess a character: ") # This line was screwing up stuff for some reason so I had to do the line above ^ and completely restart the program. (Let's just say its one of those old arcade machines where you need to input your name for a high score every time.)
        guesses += guess
        if guess not in word:
            turns -= 1
            print("That is incorrect")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You have run out of guesses. You have failed.")
                print("GAME OVER, You Lose.")
                answer == input("Do you want to play again?")
                if answer == "Yes" or answer == "yes" or answer == "y" or answer == "Y":
                    break

else:
    print("Then why are you here you idiot? Get out!")
    time.sleep(2)
    exit()
