#1 
class Person:
    def name(self):
        print(self)
        
    def age(self):
        print(self)

person12 = Person("Alice", 32)
#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printed_data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
person1 = Person("James", 32)
person1.printed_data()

#3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printed_data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
    def greet(self):
        print(f"Hello, my name is {self.name}")
        
person1 = Person("James", 32)
person1.printed_data()

#4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if age >= 0:
            self.age = age
        else: 
            raise ValueError("Error")
        
person = Person("Dave", 29)
print(person.get_age())

person.set_age(26)
print(person.set_age())
