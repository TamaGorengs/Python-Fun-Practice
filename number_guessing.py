import random

random_num = random.randint(1,10)

x = random_num

win = False

while not win == True:

    try:
        guess_number = int(input("Please enter your guess from 1 - 10: "))
        if guess_number == x:
            print("You guessed it !")
            win = True
        elif guess_number > x:
            print("A little less please.")
        elif guess_number < x:
            print("A bit more.")

    except ValueError:
        print("Please enter a number")