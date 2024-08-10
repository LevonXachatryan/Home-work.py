def save_file(input_file, output_file):
    try:
        line_count = 0
        word_count = 0
        char_count = 0
        with open(input_file, r) as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
                char_count += len(line)
        rem = (
            f"lines : {line_count}"
            f"words: {word_count}\n"
            f"characters: {char_count}"
        )
        with open(output_file, "w") as file:
            file.write(rem)
        print(output_file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        
    


#3
def positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                raise ValueError(arg)
            
        for key, value in kwargs.items():
            if not isinstance(value, int) or value <= 0:
                raise ValueError(key, value)
        return func(*args, **kwargs)
    return wrapper

@positive
def add_numbers(a, b):
    return a + b


res = add_numbers(7 ,9)
print(res)

#4
import time
from functools import wraps

def retry(max_retry = 3, delay = 1):
    
    def decorator(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            temp = 0
            while temp < max_retry:
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    temp += 1
                    print(temp, e)
                    if temp >= max_retry:
                        print("Raising exception")
                        raise
                    time.sleep(delay)
        return inner
    return decorator            

@retry(max_retry=5, delay=2)
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
    


    