from models.peson import Person

class Staff(Person):
    def __init__(self, name, age, pid, sid):
        super().__init__(name, age, pid)
        self.staff_id = sid

    def __str__(self):
        return f"Staff: {self.staff_id} name: {self.name} age: {self.age}".