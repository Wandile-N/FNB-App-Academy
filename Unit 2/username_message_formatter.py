firstName = input("First Name: ")
lastName = input("Last Name: ")
bioMsg = input("Bio message: \n")

username = f"{firstName[0].lower()}lastName.lower()"

fullName = f"{firstName.title()} {lastName.title()}"
print(fullName)

bioMsg = bioMsg.strip()
print(bioMsg)

len_bioMsg = len(bioMsg)
print(len_bioMsg)

bioMsg = bioMsg.replace("I am", "I'm")



"""
Practical Task
 

Task Overview
Username and Message Formatter
Write a Python script called string_formatter.py that takes a user’s first name, last name, 
and a short bio message as input, then applies multiple string transformations to produce a 
formatted user profile output. This simulates how a real app backend processes user-submitted text.

Requirements
Collect first name, last name, and bio message using input()
Create a username by combining first initial + last name in lowercase (e.g. ‘tdlamini’)
Display the full name in Title Case using .title()
Strip leading/trailing whitespace from the bio before displaying it using .strip()
Count and display the number of characters in the bio using len()
Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
Display all output using f-strings
"""