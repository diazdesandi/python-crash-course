# Strings
## The parts of a string
fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])

fruit = "Mangosteen"
fruit[1:4]

## Upper and lower case
"Mountains".upper()
"Mountains".lower()

## Removes whitespace from the beginning and end of a string
" yes ".strip()

## Removes whitespace from the beginning of a string
" yes ".lstrip()

## Removes whitespace from the end of a string
" yes ".rstrip()

## Formatting strings
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))


def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))


# Palindrome
def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:

        # The if-statement checks if the "letter" is not a space.
        if letter != " ":

            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string = letter + new_string
            reverse_string = reverse_string + letter

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code.
    if new_string.lower() == reverse_string.lower():

        # If True, the "input_string" contains a palindrome.
        return True

    # Otherwise, return False.
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {} km".format(miles, round(km, 1))
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km
