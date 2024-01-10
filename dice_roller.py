import random




def dice_roll():
    dice_roll = random.randint(1, 6)
    return dice_roll



def main():
    choice = input("Would you like to roll the dice? (y/n)")
    while choice == "y":
        dice_roller_one = dice_roll()
        dice_roller_two = dice_roll()
        dice_total = dice_roller_one + dice_roller_two
        if dice_roller_one == 1 and dice_roller_two == 1:
            print(f"You rolled a {dice_roller_one} on die 1\nYou rolled a {dice_roller_two} on die 1\nYour dice total is {dice_total}\nSnake eyes!")
        elif dice_roller_one == 6 and dice_roller_two == 6:
            print(f"You rolled a {dice_roller_one} on die 1\nYou rolled a {dice_roller_two} on die 1\nYour dice total is {dice_total}\nBoxCars!")
        else:
            print(f"You rolled a {dice_roller_one} on die 1\nYou rolled a {dice_roller_two} on die 1\nYour dice total is {dice_total}")
        choice = input("Would you like to roll again? (y/n)")
    print("Bye")

if __name__ == "__main__":
    main()