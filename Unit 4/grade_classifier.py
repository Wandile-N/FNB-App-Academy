studentName = input("Student name: ")
marks = []

i = 3
while i > 0:
    mark = float(input("Please insert your mark: "))
    if mark < 0 or mark > 100:
        print("Your mark is less/greater than mark percentage range!!")
        mark = float(input("Please insert your mark: "))
    else:
        marks.append(mark)
        i -= 1
    
average = sum(marks) / len(marks)

grade = []
for mark in marks:
    if mark >= 80 and mark <= 100:
        grade.append([mark, "A"])
    elif mark >= 70 and mark <= 79:
        grade.append([mark, "B"])
    elif mark >= 60 and mark <= 69:
        grade.append([mark, "C"])
    elif mark >= 50 and mark <= 59:
        grade.append([mark, "D"])
    else:
        if mark < 40:
            grade.append([mark, "F", "needs intervention"])
        else:
            grade.append([mark, "F"])

student = {}
student["name"] = studentName
student["grades"] = grade
student["avarage"] = average
if average >= 50:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

for key, value in student.items():
    print(f"{key}: {value}")



"""
Practical Task
Task Overview 

Build a student grade classifier called grade_classifier.py that takes a learner’s name and marks for three subjects, 
calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card. The program must 
correctly use conditionals for all grade and status logic.

Requirements 

Collect learner name and marks for three subjects (as floats) using input()
Calculate the average mark across the three subjects
Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
Assign Pass status if the average is 50 or above, Fail otherwise
Flag any individual subject mark below 40 as ‘needs intervention’
Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags
"""