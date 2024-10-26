# Contact Management System

contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").title()
    if name in contacts:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact {name} added successfully.")

# Function to display all contacts
def display_contacts():
    if contacts:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    else:
        print("No contacts available.")

# Function to update an existing contact
def update_contact():
    name = input("Enter the name of the contact to update: ").title()
    if name in contacts:
        phone = input(f"Enter new phone number for {name} (leave blank to keep current): ")
        email = input(f"Enter new email for {name} (leave blank to keep current): ")
        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found!")

# Function to search for a contact
def search_contact():
    name = input("Enter the name of the contact to search: ").title()
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['Phone']}, Email: {contacts[name]['Email']}")
    else:
        print("Contact not found!")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").title()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found!")

# Main menu
def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid option! Please try again.")

# Run the contact management system
if __name__ == "__main__":
    main()
