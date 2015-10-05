# guessing game
import random

def guess(numguess):
    secret = random.randrange(1,101)
    for i in range(numguess):
        guess = input ('give me a fucking number!:   ')
        
        if guess < secret:
           print " Too small, You Loser"
        elif guess > secret:
           print " Too high, You suck"
        else:
            print " You are right, you Loser"
            return
    print " you lose "

guess(4)
