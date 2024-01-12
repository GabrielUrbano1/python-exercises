import csv
import os

SALES_FILE = "monthly_sales.csv"

def load_sales(filename):
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            sales_data = {row[0]: int(row[1]) for row in reader}
        return sales_data
    except FileNotFoundError:
        print("Could not find sales data file!")
        return {}
    except ValueError:
        print(f"Invalid data in the sales file! Using a value of 0 for calculations.")
        return {}

def save_sales(filename, sales_data):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Month", "Sales"])
        for month, sales in sales_data.items():
            writer.writerow([month, sales])

def view_monthly_sales(sales_data):
    print("Monthly Sales")
    for month, sales in sales_data.items():
        print(f"{month} - {sales}")

def view_yearly_summary(sales_data):
    total_sales = sum(sales_data.values())
    monthly_average = total_sales / 12 if sales_data else 0
    print(f"Using sales amount of 0 for missing months.")
    print(f"Yearly total: {total_sales}")
    print(f"Monthly average: {monthly_average:.2f}")

def edit_sales(sales_data, month, amount):
    try:
        amount = int(amount)
        sales_data[month] = amount
        save_sales(SALES_FILE, sales_data)
        print(f"Sales amount for {month} was modified.")
    except ValueError:
        print("Invalid sales amount. Please enter a valid integer.")

def main():
    sales_data = load_sales(SALES_FILE)

    print("Monthly Sales program")
    while True:
        print("\nCOMMAND MENU")
        print("monthly - View monthly sales")
        print("yearly  - View yearly summary")
        print("edit    - Edit sales for a month")
        print("exit    - Exit program")
        command = input("Command: ").strip().lower()

        if command == "monthly":
            view_monthly_sales(sales_data)
        elif command == "yearly":
            view_yearly_summary(sales_data)
        elif command == "edit":
            month = input("Three-letter Month: ").strip().capitalize()[:3]
            if month not in sales_data:
                print("Invalid month abbreviation.")
                continue
            amount = input("Sales Amount: ")
            edit_sales(sales_data, month, amount)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    main()
