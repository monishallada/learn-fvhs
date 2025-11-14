contacts = []

def add_contact():
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "address": address, "phone": phone})
    print("Contact added!")
