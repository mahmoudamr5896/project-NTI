import pandas as pd
import hashlib

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User class for handling registration and login
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    @staticmethod
    def register(connection, username, password, role):
        cursor = connection.cursor()
        hashed_password = hash_password(password)
        cursor.execute('''
            INSERT INTO Users (username, password, role)
            VALUES (?, ?, ?)
        ''', (username, hashed_password, role))
        connection.commit()
        print(f"User {username} registered successfully.")

    @staticmethod
    def login(connection, username, password):
        cursor = connection.cursor()
        hashed_password = hash_password(password)
        cursor.execute('''
            SELECT username, role FROM Users WHERE username = ? AND password = ?
        ''', (username, hashed_password))
        result = cursor.fetchone()
        if result:
            print(f"Welcome, {username}!")
            return User(result[0], result[1])
        else:
            print("Invalid username or password.")
            return None

# Base class: Institute
class Institute:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        print(f"Institution: {self.name}, Location: {self.location}")

# Derived class: Staff
class Staff(Institute):
    def __init__(self, name, location, staff_name, position):
        super().__init__(name, location)
        self.staff_name = staff_name
        self.position = position

    def save_to_db(self, connection):
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Staff (name, position, institute_name, location)
            VALUES (?, ?, ?, ?)
        ''', (self.staff_name, self.position, self.name, self.location))
        connection.commit()
        print(f"Staff {self.staff_name} saved to the database.")

    @staticmethod
    def delete_by_id(connection, staff_id, user):
        if user.role != 'admin':
            print("Only admins can delete staff.")
            return
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Staff WHERE id = ?', (staff_id,))
        connection.commit()
        print(f"Staff with ID {staff_id} deleted.")

    @staticmethod
    def edit_by_id(connection, staff_id, new_name, new_position, user):
        if user.role != 'admin':
            print("Only admins can edit staff.")
            return
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE Staff
            SET name = ?, position = ?
            WHERE id = ?
        ''', (new_name, new_position, staff_id))
        connection.commit()
        print(f"Staff with ID {staff_id} updated.")

    @staticmethod
    def fetch_all(connection, institute_name=None, location=None):
        query = 'SELECT * FROM Staff'
        params = []
        if institute_name and location:
            query += ' WHERE institute_name = ? AND location = ?'
            params = [institute_name, location]
        return pd.read_sql(query, connection, params=params)

# Derived class: Student
class Student(Institute):
    def __init__(self, name, location, student_name, course):
        super().__init__(name, location)
        self.student_name = student_name
        self.course = course

    def save_to_db(self, connection):
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Students (name, course, institute_name, location)
            VALUES (?, ?, ?, ?)
        ''', (self.student_name, self.course, self.name, self.location))
        connection.commit()
        print(f"Student {self.student_name} saved to the database.")

    @staticmethod
    def delete_by_id(connection, student_id, user):
        if user.role != 'admin':
            print("Only admins can delete students.")
            return
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Students WHERE id = ?', (student_id,))
        connection.commit()
        print(f"Student with ID {student_id} deleted.")

    @staticmethod
    def edit_by_id(connection, student_id, new_name, new_course, user):
        if user.role != 'admin':
            print("Only admins can edit students.")
            return
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE Students
            SET name = ?, course = ?
            WHERE id = ?
        ''', (new_name, new_course, student_id))
        connection.commit()
        print(f"Student with ID {student_id} updated.")

    @staticmethod
    def fetch_all(connection, institute_name=None, location=None):
        query = 'SELECT * FROM Students'
        params = []
        if institute_name and location:
            query += ' WHERE institute_name = ? AND location = ?'
            params = [institute_name, location]
        return pd.read_sql(query, connection, params=params)
