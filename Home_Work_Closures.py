#1
def make_multiplier_of(n):
    def inner(x):
        return n * x
    return inner


my_multiplier = make_multiplier_of(3)
print(my_multiplier(10))
print(my_multiplier(4))

multiplier = make_multiplier_of(8)
print(multiplier(7))
print(multiplier(5))
#2
def make_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
counter_func = make_counter()
print(counter_func())
print(counter_func())
print(counter_func())
print(counter_func())
counter_func2 = make_counter()
print(counter_func2())
print(counter_func2())