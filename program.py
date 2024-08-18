from logic import Institute,Staff,Student
from db import connect_to_db
def main():
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
        if location:
            break
        else:
            print("Location cannot be empty. Please enter a valid location.")

    # Create an institute
    institute = Institute(name, location)

    # Connect to the database
    connection = connect_to_db()

    while True:
        print("\n--- Institute Management System ---")
        print("1. Add Staff")
        print("2. Add Student")
        print("3. Display All Staff")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            staff_name = input("Enter staff name: ").strip()
            position = input("Enter position: ").strip()
            staff = Staff(institute.name, institute.location, staff_name, position)
            staff.save_to_db(connection)

        elif choice == '2':
            student_name = input("Enter student name: ").strip()
            course = input("Enter course: ").strip()
            student = Student(institute.name, institute.location, student_name, course)
            student.save_to_db(connection)

        elif choice == '3':
            print("\nStaff Members at", institute.name, "in", institute.location)
            staff_members_df = Staff.fetch_all(connection, institute_name=institute.name, location=institute.location)
            print(staff_members_df)

        elif choice == '4':
            print("\nStudents at", institute.name, "in", institute.location)
            students_df = Student.fetch_all(connection, institute_name=institute.name, location=institute.location)
            print(students_df)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

    connection.close()

if __name__ == "__main__":
    main()