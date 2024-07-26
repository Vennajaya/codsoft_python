import json

# File to store contact data
CONTACT_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file."""
    try:
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    """Display the list of all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    """Search for contacts by name or phone number."""
    search_term = input("Enter name or phone number to search: ").lower()
    
    found = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if found:
        for contact in found:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()
    else:
        print("No contacts found matching the search term.")

def update_contact(contacts):
    """Update contact details."""
    name = input("Enter the name of the contact to update: ").lower()
    
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Contact found!")
            contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email address (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    
    print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").lower()
    
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    
    print("Contact not found.")

def main():
    """Main function to manage the contact book."""
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
