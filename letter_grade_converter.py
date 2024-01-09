print("Letter Grade Converter")

choice = "y"

while choice.lower() == "y":
    user_input = int(input("Enter numerical grade: "))
    
    if user_input >= 88:
        print("A")
    elif user_input >= 80:
        print("B")
    elif user_input >= 67:
        print("C")
    elif user_input >= 60:
        print("D")
    else:
        print("F")

    choice = input("Continue? (y/n): ")

print("Bye")
