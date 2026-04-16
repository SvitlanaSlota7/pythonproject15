class Person:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old.")

p1 = Person("Carl", "Johnson", 26)
p1.talk()

p2 = Person("Svitlana", "Ivanenko", 30)
p2.talk()