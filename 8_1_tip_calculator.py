def main():
    print("Tip Calculator\n")

    while True:
        user_input = input("Cost of meal (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the Tip Calculator.")
            break

        try:
            meal_cost = float(user_input)
        except ValueError:
            print("Please enter a valid numeric value for the cost of the meal.")
            continue

        while True:
            tip_input = input("Enter the tip percentage (e.g., 15 for 15%): ")

            try:
                tip_percentage = float(tip_input)
                if tip_percentage < 0:
                    print("Tip percentage cannot be negative.")
                else:
                    break
            except ValueError:
                print("Please enter a valid numeric value for the tip percentage.")

        tip_amount = meal_cost * (tip_percentage / 100)
        total_cost = meal_cost + tip_amount

        print(f"Meal cost: ${meal_cost:.2f}")
        print(f"Tip amount ({tip_percentage}%): ${tip_amount:.2f}")
        print(f"Total cost: ${total_cost:.2f}")
        print()

if __name__ == "__main__":
    main()
