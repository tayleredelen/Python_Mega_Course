# Define a  water_state function that:
# 1. gets a temperature argument
# 2. returns the string "Solid" if the temperature is less than or equal to 0
# 3. returns "Liquid" if the temperature is greater than 0, but less than 100.
# 4. returns "Gas" if the temperature is greater than or equal to 100.

# Solution:
# def water_state(temperature):
#     if temperature <= 0:
#         return "Solid"
#     elif 0 < temperature < 100:
#         return "Liquid"
#     else:
#         return "Gas"


# In the previous exercise, we hardcoded the values 0 and 100.
# However, it is better to place those values in constants.
# Therefore, your task is to:
# 1. create a FREEZING_POINT and a BOILING_POINT variable and
# store the values 0 and 100 in them respectively.
# 2. modify the function of the previous exercise by using those
# variables instead of the hardcoded 0 and 100 values.
# The previous function is given in the code area.

# Solution:
# def water_state(temperature):
#     FREEZING_POINT = 0
#     BOILING_POINT = 100
#     if temperature <= FREEZING_POINT:
#         return "Solid"
#     elif FREEZING_POINT < temperature < BOILING_POINT:
#         return "Liquid"
#     else:
#         return "Gas"


# Define a function that:
#     (1) takes a temperature as a parameter
#     (2) returns "Hot" if the temperature is greater than 25
#     (3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.
#     (4) returns "Cold" if the temperature is less than 15.
# If I called your function with foo(10) it would return "Cold".
# foo(15) or foo(16) or foo(25) would all return "Warm" and foo(26) would return "Hot".

# Solution:
# def foo(temperature):
#     if temperature > 25:
#         return "Hot"
#     elif 15 < temperature < 25:
#         return "Warm"
#     elif temperature < 15:
#         return "Cold"