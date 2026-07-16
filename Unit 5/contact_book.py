contact = dict.fromkeys(["name", "phone", "email"], "required")
contacts = []

def add_contact():
    contacts.append(contact.copy())

def search_contact(name:str):
    if name in contact.values():
        return contact
    else:
        return None

def delete_contact(name):
    requiredContact = search_contact(name)
    for cont in contacts:
        if cont == requiredContact:
            contacts.remove(requiredContact)

def view_all():
    for cont in contacts:
        for key, value in cont.items():
            print(f"{key}: {value}")
        print("-" * 30)

view_all()


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