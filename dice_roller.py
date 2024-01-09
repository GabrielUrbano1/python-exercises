import random


choice = "y"

while choice == "y":
    dice_roller_one = random.randint(1,6)
    dice_roller_two = random.randint(1,6)
    dice_total = dice_roller_one + dice_roller_two
    if dice_roller_one and dice_roller_two == 1:
        print(f"You rolled a {dice_roller_one} on die 1\nYou rolled a {dice_roller_two} on die 1\nYour dice total is {dice_total}\nSnake eyes!")
    elif dice_roller_one and dice_roller_two == 6:
        print(f"You rolled a {dice_roller_one} on die 1\nYou rolled a {dice_roller_two} on die 1\nYour dice total is {dice_total}\nBoxCars!")
    else:
        print(f"You rolled a {dice_roller_one} on die 1\nYou rolled a {dice_roller_two} on die 1\nYour dice total is {dice_total}")
    choice = input("Would you like to roll again? (y/n)")
print("Bye")