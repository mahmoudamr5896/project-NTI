from  logic import Institute ,Staff,Student
import pandas as pd
class Institute:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        print(f"Institution: {self.name}, Location: {self.location}")

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
    def fetch_all(connection, institute_name=None, location=None):
        query = 'SELECT * FROM Students'
        params = []
        if institute_name and location:
            query += ' WHERE institute_name = ? AND location = ?'
            params = [institute_name, location]
        return pd.read_sql(query, connection, params=params)