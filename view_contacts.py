import contact_storage

def view_all_contacts():
    contacts = contact_storage.load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("Contacts List:")
    for index, contact in enumerate(contacts):
        phone = str(contact[2])
        while len(phone) < 10:
            phone = "0" + phone
        print(f"{index + 1}. Name: {contact[0]}, Email: {contact[1]}, Phone: {phone}, Address: {contact[3]}")

