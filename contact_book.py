# contact_book.py
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contact(name):
    if name in contacts:
        print(f"{name}'s phone number is {contacts[name]}")
    else:
        print("Contact not found.")
# Example usage

if __name__ == "__main__":
    add_contact("Akshay", "9876543210")
    add_contact("Rakshana", "9123456780")

    view_contacts()
    search_contact("Akshay")
    seaech_contact("Rakshana")
