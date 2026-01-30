from models.peson import Person

class Student(Person):
    def __init__(self, name, age, pid, sid):
        super().__init__(name, age, pid)
        self.student_id = sid

    def __str__(self):
        return f"Name: {self.name} age: {self.age} student_id {self.student_id}"