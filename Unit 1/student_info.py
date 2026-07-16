firstName = input() # asking for the first name
surname = input() # asking for the surname
age = int(input())  # asking for the age as an integer data type
favNumber = float(input()) # taking the favorite number as a float

print(f"Welcome, {firstName+" "+surname}!")
print(firstName.upper())    # name in upper case
print(firstName.title())    # name in title case
print(age*12)   # age in months
print(round(favNumber, 2))      # round off to 2 decimal places

#print data types for all collected data
print(type(firstName))
print(type(surname))
print(type(age))
print(type(favNumber))


"""
Practical Task
Task Overview
Student Info Formatter
Write a Python script called student_info.py that collects personal information from the user 
and displays it in a formatted profile card. The program must demonstrate correct use of all 
four data types, string manipulation, arithmetic, and the f-string output format.

Requirements
Use input() to collect: first name, surname, age (as an integer), and a favourite number (as a float)
Display a formatted greeting using an f-string: ‘Welcome, [Full Name]!’
Display the name in UPPERCASE using .upper() and in Title Case using .title()
Calculate and display the age in months (age × 12)
Round the favourite number to 2 decimal places using round()
Print the data type of each collected value using type()
"""