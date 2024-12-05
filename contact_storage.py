import csv

CONTACT_FILE = "contacts.csv"

def load_contacts():
    contacts = []
    try:
        with open(CONTACT_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(CONTACT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow(contact)
