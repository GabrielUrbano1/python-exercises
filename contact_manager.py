contact_list = [
    [1, "Guido van Rossum", "guido@guidorossum.com", "44 20 7946 1029"],
    [2, "Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]
]

def display_contact_list():
    item_count = 1
    for contact in contact_list:
        contact_name = contact[1]
        print(f"{item_count}. {contact_name}")
        item_count += 1

def view_contact_details():
    user_input = input("Select a contact number: ")
    found = False

    for contact in contact_list:
        contact_number, contact_name, contact_email, contact_phone = contact

        if int(user_input) == contact_number:
            print("Contact Number:", contact_number)
            print("Contact Name:", contact_name)
            print("Contact Email:", contact_email)
            print("Contact Phone:", contact_phone)
            found = True
            break

    if not found:
        print("Contact not found")

def add_contact():
    contact_name = input("Enter the contact's name: ")
    contact_email = input("Enter the contact's email: ")
    contact_phone = input("Enter the contact's phone number: ")

    # Find the next available contact number
    next_contact_number = max([contact[0] for contact in contact_list]) + 1

    # Add the new contact to the list
    contact_list.append([next_contact_number, contact_name, contact_email, contact_phone])

    print("Contact added successfully!")

def delete_contact():
    user_input = input("Enter the contact number to delete: ")
    found = False

    for contact in contact_list:
        contact_number, _, _, _ = contact

        if int(user_input) == contact_number:
            contact_list.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break

    if not found:
        print("Contact not found")

while True:
    print("\nContact Manager Menu")
    print("1. Display Contact List")
    print("2. View Contact Details")
    print("3. Add Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        display_contact_list()
    elif choice == "2":
        view_contact_details()
    elif choice == "3":
        add_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid choice. Please try again.")
