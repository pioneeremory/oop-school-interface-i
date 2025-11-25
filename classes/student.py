import csv
from .person import Person

class Student(Person):
    def __init__(self, school_id, name, age, role, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        students = []
        with open('data/students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row["name"], row["age"], row["role"], row["school_id"], row["password"])
            students.append(cls(
                    school_id=int(row["school_id"]),
                    name=row["name"],
                    age=int(row["age"]),
                    role=row["role"],
                    password=row["password"]
                ))
        return students

student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
Student(**student_info)



