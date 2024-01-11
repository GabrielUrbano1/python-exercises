initial_list = ["Wooden staff", "Wizard Hat", "Cloth Shoes"]
max_inventory_size = 4
grab_list = ["Orb", "Food", "Potion"]  # Define the items that can be grabbed

def starting_inventory():
    count = 1
    for item in initial_list:
        print(f"{count}. {item}")
        count += 1

def grab_items():
    count = 1
    print("Pick one of the following items to carry.")
    for item in grab_list:
        print(f"Item {count}. {item}")
        count += 1

    choice = input("Pick the item number from the list: ")

    if choice == "1" and len(initial_list) < max_inventory_size:
        initial_list.append("Orb")
        print(f"Your updated inventory is: {initial_list}")
    elif choice == "2" and len(initial_list) < max_inventory_size:
        initial_list.append("Food")
        print(f"Your updated inventory is: {initial_list}")
    elif choice == "3" and len(initial_list) < max_inventory_size:
        initial_list.append("Potion")
        print(f"Your updated inventory is: {initial_list}")
    elif len(initial_list) >= max_inventory_size:
        print("You can't carry any more items. Drop something first.")
    else:
        print("Invalid choice.")

def edit_items():
    item_number = input("Number: ")
    if item_number.isnumeric():
        item_number = int(item_number)
        if 1 <= item_number <= len(initial_list):
            new_name = input("Updated name: ")
            initial_list[item_number - 1] = new_name
            print(f"Item number {item_number} was updated.")
        else:
            print("Invalid item number.")
    else:
        print("Invalid input. Please enter a number.")

def drop_item():
    item_number = input("Number: ")
    if item_number.isnumeric():
        item_number = int(item_number)
        if 1 <= item_number <= len(initial_list):
            dropped_item = initial_list.pop(item_number - 1)
            print(f"{dropped_item} was dropped.")
        else:
            print("Invalid item number.")
    else:
        print("Invalid input. Please enter a number.")

def command_menu():
    print("The Wizard Inventory program")
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")

    while True:
        command = input("Command: ").lower()
        if command == "show":
            starting_inventory()
        elif command == "grab":
            grab_items()
        elif command == "edit":
            edit_items()
        elif command == "drop":
            drop_item()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

command_menu()