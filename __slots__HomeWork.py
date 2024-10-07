class Person:
    __slots__ = ("name", "age", "email")
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def single(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")
        
person1 = Person("Jack", 30, "jack@example.com")

#Task 2
from abc import ABC, abstractmethod
class MenuItem:
    __slots__ = ("name", "price", "ingredients")
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        
class Appetizer(MenuItem):
    __slots__ = ("spice_level")
    def __init__(self, name, price, ingredients, spice_level):
        super().__init__(name, price, ingredients)
        self.spice_level = spice_level

class Entree(MenuItem):
    __slots__ = ("coking_style",)
    def __init__(self, name, price, ingredients, cooking_style):
        super().__init__(name, price, ingredients)
        self.coking_style = cooking_style

class Dessert(MenuItem):
    __slots__ = ("sweetness_level",)
    def __init__(self, name, price, ingredients, sweetness_level):
        super().__init__(name, price, ingredients)
        self.sweetness_level = sweetness_level

class Customer:
    __slots__ = ("name", "contact_info", "order_history")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []
        
    def place_order(self, order):
        self.order_history.append(order)
        
    def view_order_history(self):
        for i in self.order_history:
            print(i)

class Order(ABC):
    __slots__ = ("customer", "menu_items")
    def __init__(self, customer):
        self.customer = customer
        self.menu_items = []
    
    @abstractmethod
    def total_price(self):
        pass
    
    def add_item(self, menu_item):
        self.menu_items.append(menu_item)
        
class DineInOreder(Order):
    __slots__ = ()
    
    def total_price(self):
        return sum(i.price for i in self.menu_items)

class TakeawayOrder(Order):
    __slots__ = ()
    
    def total_price(self):
        return sum(i.price for i in self.menu_items)
    
class DeliveryOrder(Order):
    __slots__ = ("delivery_fee",)
    def __init__(self, customer, delivery_fee):
        super().__init__(customer)
        self.delivery_fee = delivery_fee
    
    def total_price(self):
        return sum(i.price for i in self.menu_items) + self.delivery_fee   
    
class Review:
    __slots__ = ("customer_name", "order", "rating","comments")
    def __init__(self, customer_name, order, rating, comments):
        self.customer_name = customer_name
        self.order = order
        self.rating = rating
        self.comments = comments
        
if __name__ == "__main__":
    dessert = Dessert("Chocolate", 5.50, ["Chocolate", "sugar"], "Small")