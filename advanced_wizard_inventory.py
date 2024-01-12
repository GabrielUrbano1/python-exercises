import random
import os

MAX_INVENTORY_SIZE = 4
ITEMS_FILE = "wizard_all_items.txt"
INVENTORY_FILE = "wizard_inventory.txt"

def load_items(filename):
    try:
        with open(filename, "r") as file:
            items = [line.strip() for line in file.readlines()]
        return items
    except FileNotFoundError:
        print(f"Could not find {filename}!")
        return []

def load_inventory(filename):
    try:
        with open(filename, "r") as file:
            inventory = [line.strip() for line in file.readlines()]
        return inventory
    except FileNotFoundError:
        print(f"Could not find {filename}! Starting with no inventory.")
        return []

def save_inventory(filename, inventory):
    with open(filename, "w") as file:
        for item in inventory:
            file.write(item + "\n")

def walk(items, inventory):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("You can't carry more items. Your inventory is full.")
        return
    
    available_items = [item for item in items if item not in inventory]
    if not available_items:
        print("You've already grabbed all available items.")
        return
    
    item_to_grab = random.choice(available_items)
    print(f"While walking down a path, you see a {item_to_grab}.")
    choice = input("Do you want to grab it? (y/n): ").strip().lower()
    
    if choice == "y":
        inventory.append(item_to_grab)
        save_inventory(INVENTORY_FILE, inventory)
        print(f"You picked up a {item_to_grab}.")
    elif choice != "n":
        print("Invalid choice. Enter 'y' for yes or 'n' for no.")

def show(inventory):
    if inventory:
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")
    else:
        print("Your inventory is empty.")

def drop(inventory):
    if not inventory:
        print("Your inventory is empty.")
        return
    
    show(inventory)
    try:
        item_number = int(input("Enter the number of the item to drop: ")) - 1
        if 0 <= item_number < len(inventory):
            dropped_item = inventory.pop(item_number)
            save_inventory(INVENTORY_FILE, inventory)
            print(f"You dropped {dropped_item}.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Enter a valid item number.")

def main():
    items = load_items(ITEMS_FILE)
    inventory = load_inventory(INVENTORY_FILE)

    print("The Wizard Inventory program")
    while True:
        print("\nCOMMAND MENU")
        print("walk - Walk down the path")
        print("show - Show all items")
        print("drop - Drop an item")
        print("exit - Exit program")
        command = input("Command: ").strip().lower()

        if command == "walk":
            walk(items, inventory)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop(inventory)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    main()
