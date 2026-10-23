# LEGB
# - Local
# - Enclosing
# - Global
# - Built-in
# NameError
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)
    inner()
    print(x)

outer()
print(x)


# immutable: tuple int float str bool None
def change(x):
    x = 100
    print("inside x is:", x)

a = 5
change(a)
print("outside a is:", a)

# mutable: list dict set
def add_item(lst):
    lst.append(4)
    print("inside add_items()", lst)

numbers = [1, 2, 3]
add_item(numbers[:])
print("outside add_items()", numbers)


# closure
def make_counter():
    count = 10

    def counter():
        nonlocal count
        count += 1  # count = count + 1
        return count

    return counter

c = make_counter()
print( c() )
print( c() )
print( c() )
print( c() )
print( c() )

# context manager (with)

f = open("data.txt")
try:
    content = f.read()
    print(content)
finally:
    f.close()

print("context manager:----")
with open("data.txt") as f:
    content = f.read()
    print(content)

a = 12
# __enter__
# __exit__

from contextlib import contextmanager

@contextmanager
def my_context():
    print("вход")
    print("какие-то начальные действия")
    yield
    print("какие-то  действия")
    print("выход")

with my_context():
    print("какая-то работа")

# List / Dict Comprehensions
# pythonic code
squares = []
for x in range(10):
    squares.append(x * 2)


print(squares)

squares = [ x * 2 for x in range(10) ]
print(squares)

squares = [ x * 2 for x in range(10) if x % 2 == 0 and x != 4]
print(squares)

# Dictionary comprehensions
mydict = {x: x ** 2 for x in range(4) if x % 2 == 0 and x != 4}
print(mydict)

# Set comprehension
myset = {x ** 2 for x in range(4) if x % 2 == 0 and x != 4}
print(myset)

# packing

def sum_all(mystring, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        sum += num
    return sum

print("-----")
print(sum_all(10, 105, 123 ))
print(sum_all(10, 5, 6, 8))
print(sum_all("abc", 100, 200, 10, 5, 6, 8))


def show_info_o(name, age, city):
    print("name", name)
    print("age", age)
    print("city", city)

show_info_o(age=40, city="Astana", name="Aida")
show_info_o(40, "Astana", "Aida")

def show_info(**kwargs):
    print("kwargs=", kwargs)
    print("type=", type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Ann", age=20, city="Almaty", heigh=180)

def method(age, *mylist, **mydict):
    pass

# unpacking

def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))

nums = [10, 20, 30]
print(add(*nums))

def greeting(name, city):
    return f"{name} {city}!"

mystr = greeting("Aigerim", "Almaty")
print(mystr)

person1 = {
    "city": "Astana",
    "name": "Daulet",
}

mystr = greeting(**person1)
print(mystr)

# Generators
squares_comprehen = [ x * 2 for x in range(10) ] # list comprehension
print(squares)
print(len(squares))

squares_generator = ( x * 2 for x in range(10) ) # generator

for elem in squares_comprehen:
    print(elem)
print("----------")
for elem in squares_comprehen:
    print(elem)

print("----------generator")
for elem in squares_generator:
    print(elem)
print("----------")
for elem in squares_generator:
    print(elem)
print("----------end")


# функция-generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1
        return

print("----------функция-generator-begin")
for elem in countdown(5):
    print(elem)
print("----------функция-generator-end")

# Decorators
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start
        print(f"{func.__name__}: {end_time} seconds")
        return result
    return wrapper

@timer
def slow():
    """
    some description about the function
    :return:
    """
    time.sleep(0.5)
    return "Done"

print("decorator --example ------------------")
print(slow())

