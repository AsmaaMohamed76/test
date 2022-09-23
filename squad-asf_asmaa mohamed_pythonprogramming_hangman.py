# written By Ahmed Magdy & Asmaa Mohamed

from random import random
from traceback import print_exc
import random


word = random.choice([ 'math','may','hello','hangman','good'])
allowed_errors= 8
guesses = []
right = False
name = input("Enter Your Name: ")
print("hello",name,"let's play Hangman: ")
while not right:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end = " ")
        else:
            print("_", end = " ")
    print("")
    

    guess = input(f" Allowed Errors left {allowed_errors}, Next Guess: ")
    
    guesses.append(guess.lower())
    already_guessed =guess  
    if guess.lower() not in word.lower():
        allowed_errors -= 1
    if allowed_errors == 8:
            print("===========================")
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("===========================")
          

    elif allowed_errors == 7:
            print("===========================")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("===========================")

    elif allowed_errors == 6:
           print("===========================") 
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("===========================")
          

    elif allowed_errors == 5:
            print("===========================")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("===========================")
           

    elif allowed_errors == 4:
            print("===========================")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /  \n"
                  "  |        \n"
                  "__|__\n")
            print("===========================")
    elif allowed_errors == 3:
            print("===========================")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /| \n"
                  "  |        \n"
                  "__|__\n")
            print("===========================")
    elif allowed_errors == 2:
            print("===========================")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |        \n"
                  "__|__\n")
            print("===========================")
    elif allowed_errors == 1:
            print("===========================")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    /  \n"
                  "__|__\n")
            print("===========================")
    elif allowed_errors == 0:
            print("===========================")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n") 
            print("===========================")
 
            break
    right = True
    for letter in word:
        if letter.lower() not in guesses:
            right = False

if right:
    print(f"You Get The Word !!! The Word was {word}")
else:
    print(f"Game Over !! The Word was {word}")
  