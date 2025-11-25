from person import Person

class Student(Person):
    def __init__(self, school_id, name, age, role, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id