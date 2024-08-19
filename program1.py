from  logic import Institute ,Staff,Student,User ,hash_password
from db  import connect_to_db
import hashlib

import pandas as pd
def mainstaff(connection, institute_name, location, user):
    while True:
        print("\n--- Staff Management System ---")
        print("1. Add Staff")
        print("2. Display All Staff")
        print("3. Delete Staff by ID")
        print("4. Edit Staff by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            staff_name = input("Enter staff name: ").strip()
            position = input("Enter position: ").strip()

            if staff_name.isnumeric() and position.isnumeric():
                print('invalid input ')
                break
            else:
                staff = Staff(institute_name, location, staff_name, position)
                staff.save_to_db(connection)

        elif choice == '2':
            print("\nAll Staff Members")
            staff_members_df = Staff.fetch_all(connection, institute_name, location)
            print(staff_members_df)
        elif choice == '3':
            staff_id = int(input("Enter Staff ID to delete: "))
            Staff.delete_by_id(connection, staff_id, user)
        elif choice == '4':
            staff_id = int(input("Enter Staff ID to edit: "))
            new_name = input("Enter new staff name: ").strip()
            new_position = input("Enter new position: ").strip()
            Staff.edit_by_id(connection, staff_id, new_name, new_position, user)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

def mainstudent(connection, institute_name, location, user):
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Delete Student by ID")
        print("4. Edit Student by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter student name: ").strip()
            course = input("Enter course: ").strip()
            if student_name.isnumeric() and course.isnumeric():
                print('invalid input ')
                break
            else:
                student = Student(institute_name, location, student_name, course)
                student.save_to_db(connection)
        elif choice == '2':
            print("\nAll Students")
            students_df = Student.fetch_all(connection, institute_name, location)
            print(students_df)

        elif choice == '3':
            student_id = int(input("Enter Student ID to delete: "))
            Student.delete_by_id(connection, student_id, user)
        elif choice == '4':
            student_id = int(input("Enter Student ID to edit: "))
            new_name = input("Enter new student name: ").strip()
            new_course = input("Enter new course: ").strip()
            Student.edit_by_id(connection, student_id, new_name, new_course, user)
        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

# Main program with login, registration, and CRUD operations
def main():
    connection = connect_to_db()

    while True:
        print("\n--- User Authentication ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            role = input("Enter role (admin/staff): ").strip().lower()
            if role not in ['admin', 'staff','student']:
                print("Invalid role. Please choose 'admin' or 'staff' or 'student'.")
                continue
            User.register(connection, username, password, role)

        elif choice == '2':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            user = User.login(connection, username, password)
            if user:
                break

        elif choice == '3':
            print("Exiting the program.")
            connection.close()
            return

        else:
            print("Invalid choice, please try again.")

    # Input validation for institute name
    valid_institutes = ['NTI', 'ITI']
    while True:
        name = input('Choose Institute Name [NTI, ITI]: ').strip().upper()
        if name in valid_institutes:
            break
        else:
            print("Invalid institute name. Please choose either 'NTI' or 'ITI'.")

    # Input validation for location
    while True:
        location = input('Enter Institute Location: ').strip()
        if location.isnumeric() and location:
            print('invalid input ')
            break
        else:
            print("Location cannot be empty. Please enter a valid location.")
    # Create an institute
    institute = Institute(name, location)

    while True:
        print("\n--- Institute Management System ---")
        print("1. Manage Staff")
        print("2. Manage Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            mainstaff(connection, institute.name, institute.location, user)

        elif choice == '2':
            mainstudent(connection, institute.name, institute.location, user)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

    connection.close()

if connect_to_db():
    print('connected succ')

if __name__ == "__main__":
    main()

