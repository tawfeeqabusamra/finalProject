class Course:
    course_id = 0

    def __init__(self, course_name, course_level):
        self.course_name = course_name
        self.course_level = course_level
        Course.course_id += 1
        self.course_id = Course.course_id


class Student:
    student_id = 0

    def __init__(self, student_name, student_level):
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = []
        Student.student_id += 1
        self.student_id = Student.student_id

    def add_course(self, course):
        if course.course_level == self.student_level:
            self.student_courses.append(course)
            print(f"Course {course.course_name} added to {self.student_name}'s courses.")
        else:
            print(
                f"{self.student_name} cannot take {course.course_name} because it is for {course.course_level} level students only.")

    def display_details(self):
        print(f"Name: {self.student_name}")
        print(f"Class: {self.student_level}")
        print("Courses Enrolled:")
        for course in self.student_courses:
            print(f"{course.course_name} ({course.course_level})")


students = []
courses = []


def add_student():
    name = input("Enter student name: ")
    level = input("Enter student level (A/B/C): ")
    while level not in ["A", "B", "C"]:
        level = input("Invalid input. Enter student level (A/B/C): ")
    new_student = Student(name, level)
    students.append(new_student)
    print(f"{new_student.student_name} saved successfully.")


def remove_student():
    id_to_remove = int(input("Enter student ID: "))
    for i in range(len(students)):
        if students[i].student_id == id_to_remove:
            del students[i]
            print("Delete done successfully.")
            return
    print("User does not exist.")


def edit_student():
    id_to_edit = int(input("Enter student ID: "))
    for i in range(len(students)):
        if students[i].student_id == id_to_edit:
            new_name = input("Enter new name: ")
            new_level = input("Enter new level (A/B/C): ")
            while new_level not in ["A", "B", "C"]:
                new_level = input("Invalid input. Enter new level (A/B/C): ")
            students[i].student_name = new_name
            students[i].student_level = new_level
            print(f"{students[i].student_name} edited successfully.")
            return
    print("User does not exist.")


def display_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            student.display_details()


def create_course():
    name = input("Enter course name: ")
    level = input("Enter course level (A/B/C): ")
    while level not in ["A", "B", "C"]:
        level = input("Invalid input. Enter course level (A/B/C): ")
    new_course = Course(name, level)
    courses.append(new_course)
    print(f"Course {new_course.course_name} created successfully.")


def add_course_to_student():
    id_to_add_to = int(input("Enter student ID: "))
    for i in range(len(students)):
        if students[i].student_id == id_to_add_to:
            course_id_to_add = int(input("Enter course ID: "))
            for j in range(len(courses)):
                if courses[j].course_id == course_id_to_add:
                    students[i].add_course(courses[j])
                    return
            print("Course does not exist.")
            return
    print("Student does not exist.")


while True:
    choice = int(input(
        "\nMenu \n1. Add New Student\n2. Remove the Student\n3. Edit Student\n4. Display all students\n5. Create a new Course\n6. Add Course to student\n chooice an option : "))
    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        edit_student()
    elif choice == 4:
        display_students()
    elif choice == 5:
        create_course()
    elif choice == 6:
        add_course_to_student()
