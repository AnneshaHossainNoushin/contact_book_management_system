import contact_storage

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    contacts = contact_storage.load_contacts()
    
    results = [contact for contact in contacts if search_term.lower() in contact[0].lower() or search_term in contact[2]]
    
    if results:
        print("Search Results:")
        for contact in results:
            print(f"Name: {contact[0]}, Email: {contact[1]}, Phone: {contact[2]}, Address: {contact[3]}")
    else:
        print(f"No contacts found for '{search_term}'.")

