def user(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

user1 = user("Bob", "Doe")
print(user1)
user2 = user("James", "smith")
print(user2)
#2
def calculate(*prices, num=0):
    power = sum(prices)
    total = power * (1 + num)
    return total
power_price = calculate(10, 20, 30)
print(f"${power_price}")
#3
def user_profile(first_name, last_name, *, age, city):
    profile= f"Name: {first_name} {last_name}, {age} ,{city}"
    return profile

result = user_profile("John", "Smith", age= 20, city="Yerevan")
print(result)
#5
def print_product(name, price, category):
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Category: {category}")
    
product = {
    
    "name": "Coca Cola",
    "price" : "31",
    "category" : "Juse"
}
print_product(**product)

#7
def login(level, *args, **kwargs):
    for i in args:
        print(i)
    
    for key, value in kwargs.items():
        print(key, value)
            
login("Info", 'Application started', 'Connected', timestamp='2024-07-24 15:30:00', user='admin')

#8
def user_setting(**kwargs):
    return kwargs

def user(**kwargs):
    for key,value in kwargs.items():
        print(key, value)
        
settings = user_setting(username='john_doe', email='john@example.com')
user(**settings)