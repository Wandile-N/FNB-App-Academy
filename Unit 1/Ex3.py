weight = float(input("Weight: "))
SI_units = input("(K)g or (L)bs: ")
if SI_units == "L" or SI_units == "l":
    print(f"Weight in Kg: {weight * 0.45 }" )
elif SI_units == "K" or SI_units == "k":
    print(f"Weight in Lbs: {weight / 0.45}")
else:
    print("Please choose any of the given SI units!")