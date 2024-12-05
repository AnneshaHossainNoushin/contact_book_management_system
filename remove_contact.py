import contact_storage

def remove_contact():
    phone = input("Enter the phone number of the contact to remove: ")
    
    contacts = contact_storage.load_contacts()
    
    contact_to_remove = next((contact for contact in contacts if contact[2] == phone), None)
    
    if contact_to_remove:
        contacts.remove(contact_to_remove)
        contact_storage.save_contacts(contacts)
        print(f"Contact with phone number {phone} removed successfully.")
    else:
        print(f"No contact found with phone number {phone}.")


