# Lists
# Lists are mutable sequences, typically used to store collections of homogeneous items.
# Lists are defined by enclosing a comma-separated sequence of elements in square brackets ([]).
# Lists are zero-indexed.

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)


# Tuples
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Tuples are defined by enclosing a comma-separated sequence of elements in parentheses ().
# Tuples are zero-indexed.
fullname = ("Grace", "M", "Hopper")


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
type(result)
print(result)

# Tuples can be useful when we need to ensure that an element is in a certain position and
# will not change. Since lists are mutable, the order of the elements can be changed on us.
# Since the order of the elements in a tuple can't be changed, the position of the element
# in a tuple can have meaning. A good example of this is when a function returns multiple values.
# In this case, what gets returned is a tuple, with the return values as elements in the tuple.
# The order of the returned values is important, and a tuple ensures that the order isn’t going
# to change. Storing the elements of a tuple in separate variables is called unpacking.
# This allows you to take multiple returned values from a function and store each value in
# its own variable.

# Iterate over lists and tuples
winners = ["Ashley", "Dylan", "Reese"]
for i, person in enumerate(winners):
    print("{} - {}".format(i + 1, person))


def full_emails(people: list) -> list:
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


people = [("grace.hopper@example.com", "Grace Hopper"), ("reese@example.com", "Reese")]

full_emails(people)
## For annexing indexes to the list, the enumerate() function is used.
# The enumerate() function is more idiomatic and readable than the range(len()) pattern.


# List comprehensions
# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element is the result of some operation
# applied to each member of another sequence or iterable, or to create a subsequence of those
# elements that satisfy a certain condition.

# Normal way
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

# Using list comprehension
multiples = [x * 7 for x in range(1, 11)]
print(multiples)


# Using conditionals
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0, 101) if x % 3 == 0]
print(z)


def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples.
    for person in people:
        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"
        name, age, profession = person

        # Format the required sentence and place the 3 variables
        # in the correct placeholders using the .format() method.
        print("{0} is {1} years old and works as {2}".format(name, age, profession))


# Call to the function:
biography_list(
    [("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")]
)

# Click Run to submit code
# Output should match:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer
