students = []
def add_student(student: dict):
    students.append(student)

for num in range(0, 5, 1):
    studentName = input("Student name: ")
    subjects = ["maths", "english", "science"]
    marks = []
    student = {}
    student["name"] = studentName

    subjectMarks = dict.fromkeys(["maths", "english", "science"], "marks required") 
    i = 0
    while i < 3:
        mark = float(input(f"Please insert your {subjects[i]} mark: "))
        if mark < 0 or mark > 100:
            print("Your mark is less/greater than mark percentage range!!")
        else:
            marks.append(mark)
            subjectMarks[subjects[i]] = mark
            i += 1

    grade = []
    for key, value in subjectMarks.items():
        if value >= 80 and value <= 100:
            grade.append([key, value, "A"])
        elif value >= 70 and value <= 79:
            grade.append([key, value, "B"])
        elif value >= 60 and value <= 69:
            grade.append([key, value, "c"])
        elif value >= 50 and value <= 59:
            grade.append([key, value, "D"])
        else:
            if value < 40:
                grade.append([key, value, "F", "needs intervention"])
            else:
                grade.append([key, value, "F"])
    student["grades"] = grade
        
    average = sum(marks) / len(marks)
    student["average"] = round(average, 2)
    if average >= 50:
        student["status"] = "Pass"
    else:
        student["status"] = "Fail"

    add_student(student)

studentAverageMarks = []
for student in students:
    studentAverageMarks.append(student["average"])
classAverage = sum(studentAverageMarks) / len(students)

lowestMark = 101
highestMark = -1
lowestStudent = ""
highestStudent = ""
lowestSubject = ""
highestSubject = ""

for student in students:
    for subject, mark, grade, *extra in student["grades"]:
        if mark < lowestMark:
            lowestMark = mark
            lowestStudent= student["name"]
            lowestSubject = subject
        if mark > highestMark:
            highestMark = mark
            highestStudent = student["name"]
            highestSubject = subject

for student in students:
    for key, value in student.items():
        if key == "grades":
            print(f"{key} :")
            for subject, mark, grade, *extra in value:
                result = f"{subject}: {mark}% ({grade})"
                if extra:
                    result += f" - {extra[0]}"
                print(result)
        else:
            print(f"{key}: {value}")
    print("=" * 35)

print("Class statistics")
print(f"Class average score: {round(classAverage, 2)}")
print(f"Student: {highestStudent}, highest mark: {highestMark}, highestSubject: {highestSubject}")
print(f"Student: {lowestStudent}, lowest mark: {lowestMark}, highestSubject: {lowestSubject}")

while True:
    searchName = input("\nEnter student name to search (or type 'exit' to quit): ")

    if searchName.lower() == "exit":
        print("Exiting search...")
        break

    found = False

    for student in students:
        if student["name"].lower() == searchName.lower():
            found = True

            print("\nStudent found:")
            print(f"Name: {student['name']}")
            print(f"Average: {student['average']}")
            print(f"Status: {student['status']}")
            print("Grades:")

            for subject, mark, grade, *extra in student["grades"]:
                result = f"{subject}: {mark}% ({grade})"
                if extra:
                    result += f" - {extra[0]}"
                print(result)

            break

    if not found:
        print("Student not found.")

        

"""
Alice
95
88
91
Brian
72
68
55
Chloe
35
42
38
David
50
51
45
Emma
25
65
40
"""