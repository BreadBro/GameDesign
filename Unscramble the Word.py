import random
import time
import sys
import os

def menu ():
    print("***************************************************")
    print("*                  Random Words                   *")
    print("*                                                 *")
    print("*     Instructions: A word will be randomly       *")
    print("*     selected from a list. That word will be     *")
    print("*  scrambled. your job is to unscramble the word. *")
    print("*          guess the word in order to win.        *")
    print("*                                                 *")
    print("*  Pick a mode!                                   *")
    print("*  1. Multiplayer                                 *")
    print("*  2. Singleplayer                                *")
    print("*  3. Exit Game                                   *")
    print("***************************************************")
def start ():
    start = input("(1,2,3) ")
    return start




# Function for choosing a random word
def words():
    words = ['python','java','php','javascript','computer','geeks','keyboard','laptop','headphones','hardware','software','msi','nvidia','intel','logitech','amd','playstation','xbox','nintendo','gamecube','ryzen','cpu','unity particle system']
    RandomWord = random.choice(words)
    return RandomWord




# Function for scrambling the word
def scramble(word):
    ScrambledWord = random.sample(word, len(word))
    scramble = ''.join(ScrambledWord)
    return scramble




# Function for telling scores 2p
def ending(p1n,p2n,p1,p2):
    print(p1n, 'Your score is:', p1)
    time.sleep(1)
    print(p2n, 'Your score is:', p2)
    time.sleep(1)
    WhoWon(p1n, p2n, p1, p2)
    print('Thanks for playing!')
    time.sleep(2)




# Function for telling scores 1p
def ending1p(p1n,p1):
    print(p1n, 'your score was:', p1)
    time.sleep(1)
    print('Thanks for playing!')
    time.sleep(2)




# Function for deciding who won
def WhoWon(player1, player2, p1score, p2score):
    if p1score > p2score:
        print("The winner is:", player1)
    elif p2score > p1score:
        print("The winner is:", player2)
    else:
        print("It was a draw. I don't know why you stopped playing, but okay.")




# Function for 2p main code
# Function for choosing a random word
def words():
    words = ['python','java','php','javascript','computer','geeks','keyboard','laptop','headphones','hardware','software','msi','nvidia','intel','logitech','amd','playstation','xbox','nintendo','gamecube','ryzen','cpu','unity particle system']
    RandomWord = random.choice(words)
    return RandomWord




# Function for scrambling the word
def scramble(word):
    ScrambledWord = random.sample(word, len(word))
    scramble = ''.join(ScrambledWord)
    return scramble




# Function for telling scores
def ending(p1n,p2n,p1,p2):
    print(p1n, 'Your score was:', p1)
    time.sleep(1)
    print(p2n, 'Your score was:', p2)
    time.sleep(1)
    WhoWon(p1n, p2n, p1, p2)
    print('Thanks for playing!')
    time.sleep(2)




# Function for deciding who won
def WhoWon(player1, player2, p1score, p2score):
    if p1score > p2score:
        print("The winner is:", player1)
    elif p2score > p1score:
        print("The winner is:", player2)
    else:
        print("It was a draw. I don't know why you stopped playing, but okay.")




# Function for main code
def play():
    # player names
    p1name = input("Player 1, what is your name?\n")
    p2name = input("Player 2 , what is your name?\n")
    # player scores
    P1score = 0
    P2score = 0
    # turns
    turn = 0
    while True:
        picked_word = words()
        # print the scrambled word
        ScrambledWord = scramble(picked_word)
        print("The jumbled word is:", ScrambledWord)
        if turn % 2 == 0:
            # p1 turn
            print(p1name + ', it is your turn.')
            answer = input("Unscramble the word!\n").lower()
            if answer == picked_word:
                # p1 score up by 1 if right
                P1score += 1
                print('Your score is:', P1score)
                turn += 1
            else:
                print("Better luck next time!")
                # player 2 turn
                print(p2name + ', it is your turn.')
                answer = input('Unscramble the word!\n').lower()
                if answer == picked_word:
                    # p2 score up by 1 if right
                    P2score += 1
                    print("Your Score is:", P2score)
                else:
                    print("Better luck next time. The correct word is:", picked_word)




                PlayAgain = (input("Do you want to play again?\n"))
                # if player answers no then program ends, anything else and it restarts
                if PlayAgain == "no" or PlayAgain == "No" or PlayAgain == "NO" or PlayAgain == "n" or PlayAgain == "N":
                    ending(p1name, p2name, P1score, P2score)
                    break
        # for p2 if p1 gets it right
        else:
            print(p2name, 'Your turn.')
            answer = input('Unscramble the word!\n').lower()
            # checks if answer is correct
            if answer == picked_word:
                P2score += 1
                print("Your Score is:", P2score)
                turn += 1
            # what happens if you are incorrect
            else:
                print("Better luck next time!")
                print(p1name, + ', it is your turn.')
                answer = input('Unscramble the word!\n').lower()
                # p1's chance to answer the question
                if answer == picked_word:
                    P1score += 1
                    print("Your Score is:", P1score)
                # if p1 is incorrect as well
                else:
                    print("Better luck next time. The correct word is:", picked_word)
                    PlayAgain = input("Do you want to play again?\n")
                    if PlayAgain == "No" or PlayAgain == "no" or PlayAgain == "NO" or PlayAgain == "n" or PlayAgain == "N":
                        ending(p1name, p2name, P1score, P2score)
                        break
            # if both get it right
            PlayAgain = (input("Do you want to play again?\n"))
            if PlayAgain == "No" or PlayAgain == "no" or PlayAgain == "NO" or PlayAgain == "n" or PlayAgain == "N":
                ending(p1name, p2name, P1score, P2score)
                break
# Function for 1p main code
def play1p():
    # player names
    p1name = input("What is your name?\n")
    # player scores
    P1score = 0
    while True:
        picked_word = words()
        # print the scrambled word
        ScrambledWord = scramble(picked_word)
        print("The jumbled word is:", ScrambledWord)
        answer = input("Unscramble the word!\n").lower()
        if answer == picked_word:
                # p1 score up by 1 if right
            P1score += 1
            print('Correct! Your score is now:', P1score)
            PlayAgain = (input("Do you want to play again?\n"))
                    # if player answers no then program ends, anything else and it restarts
            if PlayAgain == "no" or PlayAgain == "No" or PlayAgain == "NO" or PlayAgain == "n" or PlayAgain == "N":
                ending1p(p1name, P1score)
                break
        else:
            print("Better luck next time. The correct word is:", picked_word)
            # If the answer is incorrect




            PlayAgain = (input("Do you want to play again?\n"))
                # if player answers no then program ends, anything else and it restarts
            if PlayAgain == "no" or PlayAgain == "No" or PlayAgain == "NO" or PlayAgain == "n" or PlayAgain == "N":
                ending1p(p1name, P1score)
                break
xyz = 0
while xyz == 0:
    menu()
    x = start()
    while x == '1':
        play()
        break
    while x == '2':
        play1p()
        break
    if x == '3':
        print('Thanks for playing! Goodbye.')
        break
