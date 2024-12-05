import contact_storage
import view_contacts

def add_new_contact():
    name = input("Enter the contact's name: ")
    
    # Check if name is empty or contains numbers manually
    while not name or any(char >= '0' and char <= '9' for char in name):
        print("Name must be a valid string (cannot be empty or contain numbers).")
        name = input("Enter the contact's name: ")

    email = input("Enter the email: ")

    phone = input("Enter the phone number: ")
    
    # Check if phone contains only numbers manually
    while any(char < '0' or char > '9' for char in phone):
        print("Invalid phone number! Please enter a valid number.")
        phone = input("Enter the phone number: ")

    address = input("Enter the address: ")

    contacts = contact_storage.load_contacts()

    for contact in contacts:
        if contact[2] == phone:
            print("This phone number is already in use.")
            return

    contacts.append([name, email, phone, address])
    contact_storage.save_contacts(contacts)
    print("Contact added successfully.")  

    view_contacts.view_all_contacts()


