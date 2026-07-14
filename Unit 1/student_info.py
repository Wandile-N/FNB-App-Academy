# First task of the FNB App Academy program
# Student info Formatter

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