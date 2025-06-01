contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
    else:
        print("Contacts:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    query = input("Enter name or phone to search: ")
    results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            results.append(contact)
    if not results:
        print("No matching contacts.")
    else:
        print("Found contacts:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    view_contacts()
    if contacts:
        try:
            num = int(input("Enter contact number to update: "))
            if 1 <= num <= len(contacts):
                contact = contacts[num - 1]
                contact['name'] = input(f"Name ({contact['name']}): ") or contact['name']
                contact['phone'] = input(f"Phone ({contact['phone']}): ") or contact['phone']
                contact['email'] = input(f"Email ({contact['email']}): ") or contact['email']
                contact['address'] = input(f"Address ({contact['address']}): ") or contact['address']
                print("Contact updated!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_contact():
    view_contacts()
    if contacts:
        try:
            num = int(input("Enter contact number to delete: "))
            if 1 <= num <= len(contacts):
                removed = contacts.pop(num - 1)
                print(f"Contact '{removed['name']}' deleted!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
