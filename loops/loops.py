# LOOPS
# A loop is a block of code that repeats multiple times.

# while loop
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)


# Quiz
def is_power_of_two(number):
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder. How can you change the while loop to
    # avoid a Python ZeroDivisionError?
    while number % 2 == 0:
        number = number / 2
        if number == 0:
            return False
    # If after dividing by 2 "number" equals 1, then "number" is a power
    # of 2.
    if number == 1:
        return True
    return False


# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


def sum_of_integers(n):
    if n < 1:
        return 0

    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i += 1

    return sum


# Calls to the function
print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier < 6:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


multiplication_table(5)
# Should print:
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25


multiplication_table(8)
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24


def to_celsius(x):
    return (x - 32) * 5 / 9


# Range can take three arguments: start, stop, and step.
for i in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(i, to_celsius(i)))


name = ["Erick", "Juan", "Pedro"]
for i in name:
    print("Welcome " + i)


# Complexity 0(n^2)
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

input = "Four score and seven years ago"
for c in range(len(input)):
    if c in ["a", "e", "i", "o", "u"]:
        print(c)

print([c for c in input if c.lower() in ["a", "e", "i", "o", "u"]])


# Recursion
# Repetition of a procedure or function in a program.
def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)  # Recursively count users in subgroup
        else:
            count += 1  # Count the user
    return count


print(count_users("sales"))  # Should be 3
print(count_users("engineering"))  # Should be 8
print(count_users("everyone"))  # Should be 18


def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop + 1):
        # Complete the inner loop range
        for y in range(start, stop + 1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x * y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above


def all_numbers(minimum, maximum):

    return_string = ""  # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # numbers up to and including the "maximum" value.
    for x in range(minimum, maximum + 1):

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string += str(x) + " "

    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2, 6))  # Should be 2 3 4 5 6
print(all_numbers(3, 10))  # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # Should be -1 0 1
print(all_numbers(0, 5))  # Should be 0 1 2 3 4 5
print(all_numbers(0, 0))  # Should be 0
