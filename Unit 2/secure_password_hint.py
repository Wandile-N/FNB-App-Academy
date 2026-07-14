password = input("Password: ")
cleanPassword = password.strip()
firstLetter = cleanPassword[0]
lastLetter = cleanPassword[-1]

print(f"Your password hint: It starts with {firstLetter.upper()} and ends with {lastLetter.upper()}")
