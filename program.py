from  logic import Institute ,Staff,Student
import db
import pandas as pd

def main():
    # Create an institute
    Name = input('Choose Institute Name [ NTI , ITI ] :')
    Location =input('Choose Institute Location :')

    institute = Institute(Name, Location)

    # Connect to the database
    connection = db.connect_to_db()

    while True:
        print("\n--- Institute Management System ---")
        print("1. Add Staff")
        print("2. Add Student")
        print("3. Display All Staff")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            staff_name = input("Enter staff name: ")
            position = input("Enter position: ")
            staff = Staff(institute.name, institute.location, staff_name, position)
            staff.save_to_db(connection)
       
        elif choice == '2':
            student_name = input("Enter student name: ")
            course = input("Enter course: ")
            student = Student(institute.name, institute.location, student_name, course)
            student.save_to_db(connection)
        elif choice == '3':
            print("\nStaff Members:")
            staff_members_df = Staff.fetch_all(connection)
            print(staff_members_df)

        elif choice == '4':
            print("\nStudents:")
            students_df = Student.fetch_all(connection)
            print(students_df)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

    # Close the database connection
    connection.close()


if db.connect_to_db():
    print('connected succ')

if __name__ == "__main__":
    main()

