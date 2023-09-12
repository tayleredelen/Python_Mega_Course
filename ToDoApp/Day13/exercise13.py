# Define a get_age function that:
# 1. has two parameters, year_of_birth and current_year .
# 2. the current_year  parameter should be a default parameter.
# The default value should be the current year.
# 3. the function should calculate and return the age of the user
# given the year_of_birth and the current_year.

# Solution:
# def get_age(year_of_birth, current_year=2023):
#     age = current_year - year_of_birth
#     return(age)


# Write a get_nr_items function that:
# 1. gets one parameter.
# The parameter is expected to be a list of strings.
# 2. returns the number of items the list contains.

# Solution:
# def get_nr_items(user_input):
#     items = user_input.split(',')
#     return len(items)
#
#
# print(get_nr_items('hello, hi, bye'))


# Define a function that calculates the area of a square.
# For example, if I was to call your function with foo(7)
# the output would be 49. If I called it with foo(3)  it
# would return 9, and so on. Note that you don't have to name
# your function foo. Give it any name you want.

# Solution:
# def squarea(side):
#     area = side * side
#     return area


# Define a function that:
# (1) takes a temperature as a parameter
# (2) returns "Warm" if the temperature is greater than 7
# (3) returns "Cold" if the temperature is equal to or less than 7
# If I called your function with foo(10) it would return Warm.
# If I called it with foo(7) or foo(5) it would return Cold in both cases, and so on.

# Solution:
# def foo(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"


# Define a function that:
    # (1) takes a string as a parameter
    # (2) returns False if the string contains less than 8 characters
    # (3) returns True if the string contains 8 or more characters
# In other words, if I called your function with foo("mypass") it would
# return False. If I called it with foo("mylongpassword") it would return
# True, and so on.

# Solution:
# def foo(string):
#     if len(string) < 8:
#         return False
#     else:
#         return True


