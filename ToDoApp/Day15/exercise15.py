# Your task is to create a program that generates a random whole number.
# Here is how the program should behave:
#     Enter the lower bound: 1
#     Enter the upper bound: 10
#     7
# As you can see, the program first asks the user to enter a whole number.
# Then, once the user enters a number, the program asks the user again to enter another number.
# Then, the program returns a random number that falls between the two whole numbers.
# Here is another example:
#     Enter the lower bound: 12
#     Enter the upper bound: 15
#     14
# Note: To create this program, you might need to do some internet research or use the Python
# module index to find out what module and what function of that module you can use to generate
# random numbers. While it is easy for me to provide some clues here on what module you
# should use, searching for information and becoming familiar with programming community
# sites such as Stackoverflow is part of the programming skill set you should acquire.
# Thus, it is essential to practice such skills as well, so you are independent after you finish the course.

# Solution:
# import random
#
# low_bound = int(input("Enter the lower bound: "))
# up_bound = int(input("Enter the upper bound: "))
#
# random = random.randint(low_bound, up_bound)
#
# print(random)