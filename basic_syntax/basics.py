# EXPRESSIONS
## Annotate a variable
name: str = "Betty"
age: int = 34

## Dynamic Typing
a = 3
a = "Hello world"

## Duck typing
a = "Hello world" # Looks like a string
captain = "Picard" # type str

## Direct annotation
captain: str = "Picard"

## Basic arithmetic operations
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests

print("Each person pays: " + str(share_per_person))

# FUNCTIONS
def greet(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
greet("Betty", "IT Support")

## Built-in functions
## print()
print("Hello world")

# type() - returns the type of an object
print(type(3))

# str() - returns a string representation of an object
print(str(3))

# int() - returns an integer object
print(int("3"))

# len() - returns the length of an object
print(len("Hello world"))

arr = [1, 2, 3, 4, 5]

# max() - returns the largest item in an iterable
print(max(arr))

# min() - returns the smallest item in an iterable
print(min(arr))

# sorted() - returns a sorted list from the iterable
print(sorted(arr))

# CONDITIONALS
## Comparison operators
## ==, !=, <, >, <=, >=
print( 3 < 1)
print( 3 != 1)
print("dog" == "cat")
print("dog" != "cat")

## Logical operators
## and, or, not
def isAuthenticated(username, password):
    if username == "admin" and password == "admin":
        return True
    else:
        return False

print(isAuthenticated("admin", "admin"))

# Branching
# The ability of a program to alter its execution sequence
def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(4))

def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

print(is_odd(3))

# elif
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    elif number % 2 != 0:
        return "Odd"
    else:
        return "Invalid"

print(is_even_or_odd(3))