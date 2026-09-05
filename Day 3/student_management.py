def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{age},{course}\n")

    print("Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if not students:
            print("No student records found.")
            return

        print("\n===== Student Records =====")

        for student in students:
            data = student.strip().split(",")

            print("ID:", data[0])
            print("Name:", data[1])
            print("Age:", data[2])
            print("Course:", data[3])
            print("----------------------")

    except FileNotFoundError:
        print("No student records found.")


def search_student():
    search_id = input("Enter Student ID to search: ")

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        found = False

        for student in students:
            data = student.strip().split(",")

            if data[0] == search_id:
                print("\nStudent Found!")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Age:", data[2])
                print("Course:", data[3])
                found = True
                break

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


def main():
    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


main()