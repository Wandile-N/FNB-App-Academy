num1 = float(input())
num2 = float(input())

print(f"Addition (+): {round(num1 + num2, 2)}")
print(f"Subtraction (-): {round(num1 - num2, 2)}")
print(f"Multiplication (*): {round(num1 * num2, 2)}")
if num2 == 0.0:
    print("Math Error: Cannot divide by zero")
else:
    print(f"Division (/): {round(num1 / num2, 2)}")
    print(f"FLoor division (//): {round(num1 // num2, 2)}")
    print(f"Modus (%): {round(num1 % num2, 2)}")
