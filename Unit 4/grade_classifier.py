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