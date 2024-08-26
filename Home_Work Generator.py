def fibonacci_generator(n):
    a, b = 0, 1
    res = 0
    if res < n:
        yield a
        a, b = b, a + b
        res += 1
        
n = 10
for i in fibonacci_generator(n):
    print(i)
#2
def prime_generator(lim):
    def is_prime(num):
        if num <= 1:
            return False
        if num <=3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % i(i + 2) == 0:
                return False
            i +=6
        return True
    for i in range(2, lim):
        if is_prime(i):
            yield i
for prime in prime_generator(234):
    print(prime)
#3
def den_foo():
    number = 1
    while True:
        yield number
        number += 1
gen = den_foo()
for _ in range(10):
    print(next(gen))
#4
seq_generator = (x**2 for x in range(1, 21))
for i in seq_generator:
    print(i)
#5
def read_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line
file_path = "test.txt"
for line in read_file(file_path):
    print(line, end= "")
#7
def custom(start, end, step):
    current = start
    while current < end:
        yield current
        current += step
for i in custom(0, 6, 0.5):
    print(i)
#8
numbers_generator = (num for num in range(1, 51) if num % 2 == 0)
for i in numbers_generator:
    print(i)
#9
def gen1():
    for i in range(1, 6):
        yield i
def gen2():
    yield from gen1()
    for i in range(6 ,11):
        yield i
for value in gen2():
    print(value)
#10
def exception_propagator(iterable):
    for i in iterable:
        if i == "error":
            raise ValueError("Error")
        yield i
my_ls = ["list1", "list2", "list3", "error", "list5", "list6",]
try:
    for i in exception_propagator(my_ls):
        print(i)
except ValueError as e:
    print(e)
#13
def custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_lambda = lambda x: x % 2 == 0
for i in custom_filter(is_lambda, numbers):
    print(i)
#14
def custom_map(func, iterable):
    for i in iterable:
        yield func(i)
my_num = [1, 2, 3, 4, 5]
square = lambda x: x ** 2
for res in custom_map(square, my_num):
    print(res)
    