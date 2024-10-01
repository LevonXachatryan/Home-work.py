#Task1
class Person:
    def __init__(self, age):
        self._age = None
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Error")
        self._age = value
        
p = Person(24)

#Task 2
class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value: float):
        if value < 0:
            raise ValueError("Width cannot be negative.")
        self._width
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value: float):
        if value < 0:
            raise ValueError("height cannot be negative.")
        self._height
    
    @property
    def area(self):
        return self._width * self._height
    
rect = Rectangle(5 ,10)

#Task3
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value: float):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.fahrenheit * 9/5) + 32
    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self._celsius = (value - 32) * 5/9
temp = Temperature(54)

#Task4
class ScoreDescriptore:
    def __init__(self):
        self._score = 0
    
    def __get__(self, instance, owner):
        return self._score
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError()
        self._score

class Student:
    @ScoreDescriptore
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score
    
    def __str__(self):
        return f"Student(name = {self.name}, score = {self.score})"

#Task5
class ValidatedString:
    def __init__(self, min_len):
        self.min_len = min_len
        self._value = ""
    
    def __get__(self, instance, owner):
        self._value
        
    def __get__(self, instance, value):
        if len(value) < self.min_len:
            raise ValueError
        self._value = value
class User:
    @ValidatedString
    def __init__(self, username):
        self.username = username
    
    def __str__(self):
        return f"User(username= {self.username})"

#Task 6
class SalProps:
    def __init__(self, max_sal):
        self.max_sal = max_sal
        self._value = 0
    
    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Error")
        if value > self.max_sal:
            raise ValueError
        self._value = value
        
class Employee:
    @SalProps(max_sal=200000)
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"Employee(name = {self.name}, salary= {self.salary})"
try:
    emp1 = Employee("Alice", 15000)
    print(emp1)
except ValueError as e:
    print(e)

#Task7
class RangeDescriptor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self._value = min_value
    
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if value < self.min_value or value > self.max_value:
            raise ValueError
        self._value = value
class Product:
    @RangeDescriptor(min_value= 1, max_value= 100)
    
    def __init__(self, name, price):
        self.name= name
        self.price = price
    
    def price(self):
        pass
    def __str__(self):
        return f"Product (name = {self.name}, price = {self.price})"
product1 = Product("Cola", 12)
