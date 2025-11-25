import csv
from .person import Person

class Staff(Person):
    def __init__(self, employee_id, name, age, role, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        staff = []
        with open('data/staff.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row["name"], row["age"], row["role"], row["employee_id"], row["password"])
            staff.append(cls(
                    employee_id=int(row["employee_id"]),
                    name=row["name"],
                    age=int(row["age"]),
                    role=row["role"],
                    password=row["password"]
                ))
        return staff

staff_info = {'name' : 'Diana', 'password' : 'password', 'employee_id' : 12345, 'age' : 17, 'role' : 'Student'}
Staff(**staff_info)