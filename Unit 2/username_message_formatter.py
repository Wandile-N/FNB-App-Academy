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