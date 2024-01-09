
choice = "y"

while choice.lower() == "y":

    user_input = float(input("Enter number item cost"))
    base = float(5.95)
    standerd = float(7.95)
    premium = float(9.95)
    free = int(0)

    if user_input <= 0:
        print("You mus enter a positive number. Please try again")
    elif user_input < 30:
        print(f"Cost of items ordered is: {round(user_input, 2)}\nShipping cost: \t\t {base}\nTotal cost: \t\t {round(base + user_input)}")
    elif user_input < 49.99:
        print(f"Cost of items ordered is: {round(user_input, 2)}\nShipping cost: \t\t {standerd}\nTotal cost: \t\t {round(standerd + user_input)}")

    elif user_input < 74.99:
        print(f"Cost of items ordered is: {round(user_input, 2)}\nShipping cost: \t\t {premium}\nTotal cost: \t\t {round(premium + user_input)}")

    elif user_input > 75:
        print(f"Cost of items ordered is: {round(user_input, 2)}\nShipping cost: \t\t {free}\nTotal cost: \t\t {round(free + user_input)}")


    choice = input("Continue? (y/n): ")

print("Bye")
