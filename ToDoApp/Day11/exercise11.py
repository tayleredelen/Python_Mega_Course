# The code in the code area is incomplete.
# Your task is to:
# 1. complete the get_max function so it calculates and
# prints out the maximum value of the grades list.
# 2. and then call the function and print out the output.
# The output of your code should be:
    # 9.7

# Solution:
# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     return max(grades)
#
#
# print(get_max())


# The get_max function you created in the previous exercise returned 9.7.
# In this exercise, you should:
# 1. change the function so this time it returns the following string:
# "Max: 9.7, Min: 9.2"
# where 9.7 is the maximum, and 9.2 is the minimum.
# Note: For the exercise to be marked as correct by the system, you should return
# the exact string "Max: 9.7, Min: 9.2"

# Solution:
# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_local = max(grades)
#     min_local = min(grades)
#     return f"Max: {max_local}, Min: {min_local}"
#
#
# print(get_max())