# '''#Ridgemont High Student Interface 
# --------------------------------
# Welcome, Richard. Your access level is Principal
#     What would you like to do?
#     Options:
#     1 List All Students
#     2 View Individual Student <student_id>
#     3 Add a Student
#     4 Remove a Student <student_id>
#     5 Quit'''
class School:
    def __init__(self, name):
        self.name = name
        self.staff = []
        self.students = []

class Person:
    def __init__(self, name, age, role, password):
        self.name = name
        self.age = age
        self.role = role
        self.password = password

class Student(Person):
    def __init__(self, school_id, name, age, role, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id


class Staff(Person):
    def __init__(self, employee_id, name, age, role, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

staff_info = {'name' : 'Diana', 'password' : 'password', 'employee_id' : 12345, 'age' : 17, 'role' : 'Student'}
Staff(**staff_info)
student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
Student(**student_info)
print(student_info)
print(staff_info)


