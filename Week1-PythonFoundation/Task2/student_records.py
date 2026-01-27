students = []


def add_student(name, marks):
    student = {"name": name, "marks": marks}
    students.append(student)


def display_students():
    for student in students:
        print(f"Name: {student['name']}, Marks: {student['marks']}")


add_student("Ayesha", 85)
add_student("Ali", 90)
display_students()
