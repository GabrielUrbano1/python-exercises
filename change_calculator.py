print("Change Calculator")


choice = "y"

while choice.lower() == "y":

    user_input = int(input("Enter number of cents (0-99)"))

    quarters = int(user_input / 25)
    quarters_total = 25 * quarters
    print(f"Quarters: {quarters}")

    dimes = int((user_input - quarters_total)/ 10)
    dimes_total = 10 * dimes
    print(f"Dimes: {dimes}")

    nickels = int((user_input - quarters_total - dimes_total)/ 5)
    nickels_total = 5 * nickels
    print(f"Nickels: {nickels}")

    pennies = int((user_input - quarters_total - dimes_total - nickels_total)/1)
    print(f"Pennies: {pennies}")
    choice = input("Continue? (y/n): ")

print("Bye")




