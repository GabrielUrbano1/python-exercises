
def miles_to_feet(number):
    feet_walked = number * 5280
    return feet_walked
    


def main():
    print("Hike Calculator")
    user_input = float(input("How many miles did you walk?:"))
    result = miles_to_feet(user_input)
    print(f"you walked {int(result)} Feet")

if __name__ == "__main__":

    main()