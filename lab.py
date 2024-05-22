class Person:
    def __init__(self, name, age, CID):
        self.name = name
        self.age = age
        self.CID = CID
        
    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Teacher(Person):
    de