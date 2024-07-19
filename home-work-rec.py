# home work1
def flatten_list(nested_list):
    flatten = []
    for i in nested_list:
        if isinstance(i, list):
            flatten.append(i)
    return flatten

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flatten = flatten_list(nested_list)
print(flatten)
# homew work2
def sum_list(my_ls):
    if not my_ls:
        return 0
    else:
        return my_ls[0] + sum_list(my_ls[1:])
    
my_ls = [1, 2, 3, 4, 5]
print(sum_list(my_ls))
#home work3
def sorted(lst):
    if len(lst) <= 1:
        return True
    else: 
        return lst[0] <= lst[1]

lst = [1, 2, 3, 4, 5]
print(sorted(lst))
#home work 4
#home work 5
def max(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
        
    if c > max_num:
        max_num = c
    return max_num
print(max(3, 5, 7))
#home work6
def fibonacci_list(n):
    fib_ls = []
    a, b = 0,1
    for i in range(n):
        fib_ls.append(a)
        a, b = b, a + b
    return fib_ls
print(fibonacci_list(10))
#home work 7
def power(n):
    if  n <= 0:
        return False
    return (n & (n - 1)) == 0
print(power(16))
