def my_map(func, iterable):
    res = []
    for i in iterable:
        res.append(func(i))
    return res

#2
def my_filter(func, iterables):
    result = []
    for i in iterables:
        if func(i):
            result.append(i)
    return result
#4
def iteration(numbers):
    index = 0
    while True:
        try:
            number = next(iter(numbers))
            print(number)
        except StopIteration:
            print("End")
            break
        
numbers = [10, 20, 30, 40, 50 ]
iteration(numbers)
#5
def get_nth_element(iterable, n):
    it = iter(iterable)
    try:
        for i in range(n):
            next(it)
        return next(it)
    except StopIteration:
        print("Index out of range")
        
numbers = [10, 20, 30, 40, 50]
element = get_nth_element(numbers)
print(element)
#6
def apply_func(iterable, func):
    return [func(i) for i in iterable]

def square(x):
    return x * x
number = [1, 2, 3, 4, 5]
square_func = apply_func(numbers, square)
print(square_func)