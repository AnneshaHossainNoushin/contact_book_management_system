import add_contact
import view_contacts
import remove_contact
import search_contact

def display_menu():
    print("Contact Book Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contacts")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Select an option: ")
    
    if choice == '1':
        add_contact.add_new_contact()
    elif choice == '2':
        view_contacts.view_all_contacts()
    elif choice == '3':
        remove_contact.remove_contact()
    elif choice == '4':
        search_contact.search_contact()
    elif choice == '5':
        print("TATA!!")
        break
    else:
        print("Invalid choice!")


