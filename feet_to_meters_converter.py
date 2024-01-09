import converter


print("Feet and Meters Converter")


print("Conversions Menu:\na. Feet to Meters\nb. Meters to Feet\n")

choice = "y"
while choice == "y":
    user_choice = input("Select a conversion (a/b):")

    if user_choice.lower() == "a":
        number = float(input("Enter a number to convert"))
        result = converter.feet_to_meters(number)
    elif user_choice.lower() == "b":
        feet = input("Enter a number to convert")
        result = converter.meters_to_feet(feet)
    choice = input("Would you like to perform another conversion? (y/n)")

print("Thanks Bye")