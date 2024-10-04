# Dictionaries
x = {}
type(x)


# Dictionaries are a built-in Python data structure for mapping keys to values.
# A dictionary is a collection of key-value pairs. The dictionary is enclosed by curly braces.
# Each key is separated from its value by a colon. The key-value pairs are separated by commas.
# The keys must be unique, but the values can be duplicated.
# The keys in a dictionary must be immutable data types, such as strings or numbers.
# The values in a dictionary can be any data type.
# The keys in a dictionary are unordered.
# The values in a dictionary are accessed by key, not by index.

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

file_counts["txt"]
"jpg" in file_counts
"HTML" in file_counts

# When using a key that doesn't exist in the dictionary, a KeyError will occur.
# When storing a key that already exists in the dictionary,
# the value associated with that key will be updated.


# Iterating over dictionaries
# The items() method returns a view object that displays a list of a dictionary's
# key-value tuple pairs. The view object will reflect any changes done to the dictionary.
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)

# Lists vs. Dictionaries
# Lists are ordered, mutable, and allow duplicate elements.
# Dictionaries are unordered, mutable, and do not allow duplicate keys.
# List use data types like integers, strings, and lists.
# Dictionaries use data types like strings, integers, and tuples.


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for items, price in basket.items():
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {
    "bananas": 1.56,
    "apples": 2.50,
    "oranges": 0.99,
    "bread": 4.59,
    "coffee": 6.99,
    "milk": 3.39,
    "eggs": 2.98,
    "cheese": 5.44,
}

print(add_prices(groceries))  # Should print 28.44
