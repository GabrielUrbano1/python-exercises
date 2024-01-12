import csv
import os

# Constants
CONTACTS_FILE = "contacts.csv"

def load_contacts(filename):
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            contacts = list(reader)
        return contacts
    except FileNotFoundError:
        print("Could not find contacts file!")
        return []

def save_contacts(filename, contacts):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def list_contacts(contacts):
    if not contacts:
        print("There are no contacts in the list.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact[0]}")

def view_contact(contacts, contact_number):
    try:
        contact_number = int(contact_number) - 1
        if 0 <= contact_number < len(contacts):
            contact = contacts[contact_number]
            print(f"Number: {contact_number + 1}")
            print(f"Name: {contact[0]}")
            print(f"Email: {contact[1]}")
            print(f"Phone: {contact[2]}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid integer.")

def add_contact(contacts, name, email, phone):
    contacts.append([name, email, phone])
    save_contacts(CONTACTS_FILE, contacts)
    print(f"{name} was added.")

def delete_contact(contacts, contact_number):
    try:
        contact_number = int(contact_number) - 1
        if 0 <= contact_number < len(contacts):
            deleted_contact = contacts.pop(contact_number)
            save_contacts(CONTACTS_FILE, contacts)
            print(f"{deleted_contact[0]} was deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid integer.")

def main():
    contacts = load_contacts(CONTACTS_FILE)

    print("Contact Manager")
    while True:
        print("\nCOMMAND MENU")
        print("list - Display all contacts")
        print("view - View a contact")
        print("add  - Add a contact")
        print("del  - Delete a contact")
        print("exit - Exit program")
        command = input("Command: ").strip().lower()

        if command == "list":
            list_contacts(contacts)
        elif command == "view":
            contact_number = input("Number: ")
            view_contact(contacts, contact_number)
        elif command == "add":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            add_contact(contacts, name, email, phone)
        elif command == "del":
            contact_number = input("Number: ")
            delete_contact(contacts, contact_number)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    main()
