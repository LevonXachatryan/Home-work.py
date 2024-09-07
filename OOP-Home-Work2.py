#1
class Employe:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")
        
    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.salary = salary
try:
    emp = Employe(213, "James", 500)
    emp.set_salary(5500)
    print(f"New Salary: {emp.get_salary}")
except ValueError as e:
    print(e)

#2
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.__minmum_price = 10
        if self.price < self.__minmum_price:
            raise ValueError(f"Price cannotbe than {self.__minmum_price}")
        
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        if price < self.__minmum_price:
            raise ValueError(f"Price cannotbe than {self.__minmum_price}")
        self.price = price
try:
    book1 = Book("Object-Oriented Analysis and Design with Applications","Grady Booch", 20)
except ValueError as e:
    print(e)

#3
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")
        
    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
student1 = Student("Bob", "W4324r")
student1.add_grade(45)
#4
class ShoppingCart:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.items = []
        
    def get_items(self):
        return self.items()
    
    def print_data(self):
        print(f"name = {self.name}, price = {self.price}, ShoppingCart items = {self.items}")
    
cart1 = ShoppingCart(name = "Ann", price = 12.3)

    
#5
class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock
        if self.quantity_in_stock < 0:
            raise ValueError("Quantity in stock cannot be negative")
    
    def get_product_id(self):
        return self.product_id
    def set_product_id(self, product_id):
        self.product_id = product_id
    
    def get_product_name(self):
        return self.product_name
    def set_product_name(self, product_name):
        self.product_name = product_name
        
    def get_quantity_in_stock(self):
        return self.quantity_in_stock
    def set_quantity_in_stock(self, quantity):
        if self.quantity_in_stock + quantity < 0:
            raise ValueError("negative quantity")
        self.quantity_in_stock += quantity
try:
    prod = Product("Q213", "Laptop", 50)
except ValueError as e:
    print(e)