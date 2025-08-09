import random
from random import randint
a = randint(1,100)
# print(a)
print("I'm Thinking of a Number Between 1 to 100")
tries = 0
while True:
    gue = int(input("Guess: "))
    if gue == a:
        print(f"Correct! You Have Guessed It in {tries} tries")
        break
    elif 1<= gue - a <= 10:
        print("Guess is near high")
        tries = tries + 1
    elif 11<= gue - a <= 20:
        print("Guess is close high")
        tries = tries + 1
    elif 21<= gue - a <= 99:
        print("Guess is too high")
        tries = tries + 1
    elif -10<= gue - a <= -1:
        print("Guess is near low")
        tries = tries + 1
    elif -20<= gue - a <= -11:
        print("Guess is close low")
        tries = tries + 1
    elif -99<= gue - a <= -21:
        print("Guess is too low")
        tries = tries + 1