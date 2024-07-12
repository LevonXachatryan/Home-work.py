#home work 1
a = 5
def numbers(a):
    if a < 0:
        return
    for i in range(a, -1, -1):
        print(i)
        
numbers(a)

#home work 2
def print_numbers(n):
    for i in range(n + 1):
        print(i)
        
n = 10
print_numbers(n)

#home work 3
my_ls = [1, 2, 3, 4, 5]
def print_ls(lst):
    for i in lst:
        print(i)
print_ls(my_ls)

# Home work 4
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_digits(123)) 

#home work 5
text = "Python"
def first_char(s):
    for i in s:
        if i.isupper():
            return i
    
result = first_char(text)
print(f"Տողում առաջին հանդիպած մեծատառը {result}")
#home work 6
my_list = [3, 56, 75, 4, 65]
def compersion(lst):
    min_element = lst[0]
    max_element = lst[0]
    
    for i in lst:
        if i < min_element:
            min_element = i
        if i > max_element:
            max_element = i
    return min_element, max_element

res = compersion(my_list)
print(f"List-ի ամենափոքր էլեմենտը՝ {res[0]}")
print(f"List-ի ամենամեծ էլեմենտը՝ {res[1]}")

