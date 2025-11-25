from school import Person

class Staff(Person):
    def __init__(self, employee_id, name, age, role, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id