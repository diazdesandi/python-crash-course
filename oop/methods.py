# Methods

## Creating an instance of a class
# To create an instance of a class, you call the class using class name and pass
# in whatever arguments its __init__ method accepts.


class Apple:
    def __init__(self):  # constructor
        self.color = "red"
        self.flavor = "sweet"


honeycrisp = Apple()
print(honeycrisp.color)

## Modifying variables
# You can modify the variables of an instance of a class by accessing the
# variable directly.


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)

## str method
# The __str__ method is a special method that returns a string representation
# of the object. This method is called when you use the print() function on an
# object.


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):  # special method
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


honeycrisp = Apple("red", "sweet")
print(honeycrisp)

# __len__ returns the length of the object or collection.
# __contains__ tests whether the object contains an item.
# __eq__ tests whether two objects are equal.


## Performin special operations
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __add__(self, other):
        return self.area() + other.area()


triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)
