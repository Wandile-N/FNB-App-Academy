# The Challenge: “The South African Fuel Cost Calculator”

km = float(input("Trip kilometers: "))
petrolPrice = float(input("Petrol price per liter: "))
liters_needed = km / 10

totalCost = round(liters_needed * petrolPrice, 2)
print(f"The travel cost will be R{totalCost}")