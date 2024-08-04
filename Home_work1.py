func_lam = lambda factor: lambda x: x * factor
multiply = func_lam(6)
result = multiply(10)  
print(result)
#2
def make_adder(n):
    def inner(x):
        return n + x
    return inner
add_5 = make_adder(5)
print(add_5(10))

#3
def apply_twice(f, x):
    return f(f(x))

def square(n):
    return n ** 2
def increment(n):
    return n + 1
res_square = apply_twice(square, 3)
print(res_square)
res_increment = apply_twice(increment, 5)
print(res_increment)

#4
def compose(f,g):
    def composed_foo(x):
        return f(g(x))
    return composed_foo
def add_one(n):
    return n + 1
def square(n):
    return n ** 2
composed = compose(add_one, square)
res = composed(4)
print(res)

#5
def power_factory(n):
    def power(x):
        return x ** n
    return power
cube = power_factory(3)
print(cube(5))

#6
ls = [1, 2, 3, 4, 5]
map_lam = list(map(lambda x: x ** 2, ls))
print(map_lam)

#7
ls2 = [23, 43, 11, 26, 20]
filter_lam = list(filter(lambda x: x % 2 != 0 , ls2))
print(filter_lam)

#8
def make_greeting(greeting):
    def greet(name):
        print(greeting, name)
    return greet
hello_greeting = make_greeting("Hello")
hello_greeting("James")

#9
def make_accumulator(start = 0):
    count = start
    def coll(value):
        nonlocal count
        count +=value
        return count
    return coll
acc = make_accumulator(10)
print(acc(5))

#10
def make_config(key, value):
    def config_func():
        return {key : value}
    return config_func
print_config = make_config("one", "1")
print(print_config())

#11
def make_logger(level):
    def logs_message(message):
        print(level, message)
    return logs_message

info_loger = make_logger("Info")
error_loger = make_logger("Error")

info_loger("Սա տեղեկատվական հաղորդագրություն է։")
error_loger("Սա սխալի հաղորդագրություն է:")

#12
def make_memoize(f):
    result_memoize = {}
    def memoized_function(*args):
        if args in result_memoize:
            return result_memoize[args]
        finish = f(*args)
        return finish
    return memoized_function

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
memoized_factorial = make_memoize(factorial)
print(memoized_factorial(5))

#13
def bar(n):
    functions = []
    for i in range(n):
        def barx(x, i = i):
            return x * i
        functions.append(barx)
    return functions
funcs = [5]

#14
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Հնարավոր չէ բաժանել զրոյի:")
    return x / y

calculator = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}
def calculate(operand1, operand2, operator):
    operation = operations.get(operator)
    if operation is None:
        raise ValueError(f"Չաջակցվող օպերատոր՝ {operator}")
    return operation(operand1, operand2)
try:
    print(calculate(10, 5, '+'))  
    print(calculate(10, 5, '-'))  
    print(calculate(10, 5, '*'))  
    print(calculate(10, 5, '/'))  
    print(calculate(10, 0, '/'))
except ValueError as e:
    print(e)    

#15
def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def to_title_case(s):
    return s.title()

def reverse_string(s):
    return s[::-1]

string_operations = {
    'uppercase': to_uppercase,
    'lowercase': to_lowercase,
    'titlecase': to_title_case,
    'reverse': reverse_string
}

def manipulate_string(s, operation):
    func = string_operations.get(operation)
    
    if func is None:
        raise ValueError(f"Unsupported operation: {operation}")
    
    return func(s)

try:
    print(manipulate_string("hello world", "uppercase"))  
    print(manipulate_string("HELLO WORLD", "lowercase"))  
    print(manipulate_string("hello world", "titlecase")) 
    print(manipulate_string("hello world", "reverse"))   
    print(manipulate_string("hello world", "unknown"))    
except ValueError as e:
    print(e)

#16
#17
def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celsius_kelvin(celsius):
    return celsius + 273.15

conversion_function = {
    ("celsius", "fahrenheit") : celsius_fahrenheit,
    ("celsius", "kelvin") : celsius_kelvin
}
def convert_temperature(value, from_unit, to_unit):
    if (from_unit, to_unit) not in conversion_functions:
         raise ValueError(f"Փոխակերպումը «{from_unit}»-ից «{to_unit}»-ի չի աջակցվում»:")
    conv_func = conversion_function[(from_unit, to_unit)]
    return conv_func
print(f"25°C to Fahrenheit: {convert_temperature(25, 'celsius')}")

#18
