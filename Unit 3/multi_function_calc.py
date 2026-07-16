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



"""
Practical Task
 
Task Overview
Multi-Function Calculator
Build a Python calculator called calculator.py that takes two 
numbers as input and performs all four basic arithmetic operations 
plus two advanced operations. The calculator must handle user 
input safely using type casting and display results clearly using 
f-strings.

Requirements
Use float(input()) to collect two numbers from the user
Calculate and display: addition, subtraction, multiplication, division
Calculate and display: floor division (//) and modulus (%)
Round all results to 2 decimal places using round()
Handle division by zero — if the second number is 0, display a 
friendly error message instead of crashing
Display all results in a formatted table using f-strings
"""