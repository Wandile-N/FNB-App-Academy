contacts = []

def add_contact():
    contact = {
        "name": input("Name: "),
        "phone": input("Phone: "),
        "email": input("Email: ")
    }
    contacts.append(contact)

def search_contact(name:str):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

def delete_contact(name):
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully.")
    else:
        print("Contact not found!")

def view_all():
    for contact in contacts:
        for key, value in contact.items():
            print(f"{key}: {value}")
        print("-" * 35)

def display_contact(contact: dict):
    print("-" * 35)
    for key, value in contact.items():
        print(f"{key}: {value}")
    print("-" * 35)

while True:
    action = input("1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit \n Please choose your action: ")

    try:
        do = int(action)
        if do == 1:
            add_contact()
        elif do == 2:
            display_contact(search_contact(input("Search name: ")))
        elif do == 3:
            delete_contact(input("Name of the contact to delete: "))
        elif do == 4:
            view_all()
        elif do == 5:
            break
        else:
            print("Choose a number between 1 and 5.")
    except ValueError:
        print("Please enter a number.")











"""
Practical Task
Task Overview

Build a command-line contact book called contact_book.py that stores contacts as 
a list of dictionaries and allows the user to add, search, view, and delete contacts.
 This is a foundational data structure pattern used in virtually every real app.

Requirements

Store contacts as a list of dictionaries, each with keys: name, phone, email
Implement an add_contact() function that appends a new dictionary to the list
Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)
Implement a delete_contact(name) function that removes a contact by name
Implement a view_all() function that displays all contacts in a formatted layout
Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)
"""