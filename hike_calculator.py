print("Hike Calculator")

def miles_to_feet(number):

    feet_walked = number * 5280
    return feet_walked
    
def main():
    user_input = float(input("How many miles did you walk?:"))
    result = miles_to_feet(user_input)
    print(f"you walked {int(result)} Feet")

main()