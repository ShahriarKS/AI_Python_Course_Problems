# Problem: Store student marks using dictionary.

marks = {
    "Rahim": 85,
    "Karim": 78,
    "Nadia": 92
}

name = input("Enter student name: ")
print("Marks:", marks.get(name, "Student not found"))
